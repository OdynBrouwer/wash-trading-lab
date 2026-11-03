"""Minimale collector voor publieke CEX-websockets: Binance spot en Bybit spot.

Doel is niet om zoveel mogelijk data te verzamelen, maar om te meten of deze machine
een publieke stream betrouwbaar kan volgen. Dat is de acceptatie-eis uit
docs/07-datalaag.md §11: geen onverklaarde gaten, geen verloren trades, geen oplopende
achterstand, reconnect zonder datagat, geen geheugenlek.

Wat dit script wel doet:
  - trades volledig wegschrijven, met zowel de beurs- als de lokale ontvangsttijd
  - diepte-berichten tellen en de volgnummers bewaken; elk gat gaat naar gaps.jsonl
  - latentie, verwerkingstijd en queue-achterstand meten

Wat het niet doet: het orderboek reconstrueren. Een snapshot plus diff-toepassing is
per venue anders en vraagt om een aparte, geteste implementatie. Zonder dat kun je de
diepte-stream niet als boek gebruiken, maar wél vaststellen of hij continu is.

    python scripts/collector.py --minutes 2
    python scripts/collector.py --venue bybit --minutes 2

Alles komt in data/collector/<venue>/<jaar-maand-dag>T<hhmm>/, dat is git-ignored.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import random
import statistics
import sys
import time
import tracemalloc
from datetime import datetime, timezone

import aiohttp

SYMBOL = "BTCUSDT"

BINANCE_URL = (
    "wss://stream.binance.com:9443/stream?streams="
    "btcusdt@trade/btcusdt@depth@100ms"
)
BYBIT_URL = "wss://stream.bybit.com/v5/public/spot"
BYBIT_ARGS = ["publicTrade.BTCUSDT", "orderbook.50.BTCUSDT"]


def now_ms() -> int:
    return int(time.time() * 1000)


def to_ms(raw: int) -> tuple[int, str]:
    """Normaliseer een beurs-timestamp naar milliseconden en meld de eenheid.

    De projectdocumentatie gaat ervan uit dat Binance vanaf 2025 microseconden levert
    en Bybit milliseconden. In plaats van dat per venue aan te nemen kijken we naar de
    grootte: dat werkt ook als een beurs zijn eenheid verandert zonder aankondiging.
    """
    if raw > 10**16:          # nanoseconden
        return raw // 10**6, "ns"
    if raw > 10**15:          # microseconden
        return raw // 10**3, "us"
    if raw > 10**12:          # milliseconden
        return raw, "ms"
    return raw * 1000, "s"


class JsonlWriter:
    """Schrijft regels weg en houdt de teller bij, zonder per regel te flushen."""

    def __init__(self, path: str, flush_every: int = 200):
        self._fh = open(path, "w", encoding="utf-8", newline="\n")
        self._pending = 0
        self._flush_every = flush_every
        self.lines = 0

    def write(self, record: dict) -> None:
        self._fh.write(json.dumps(record, separators=(",", ":")) + "\n")
        self.lines += 1
        self._pending += 1
        if self._pending >= self._flush_every:
            self._fh.flush()
            self._pending = 0

    def close(self) -> None:
        self._fh.flush()
        self._fh.close()


class Stats:
    def __init__(self, venue: str):
        self.venue = venue
        self.connected_at = now_ms()
        self.reconnects = 0
        self.errors: list[str] = []
        self.per_stream: dict[str, dict] = {}

    def stream(self, name: str) -> dict:
        return self.per_stream.setdefault(
            name,
            {
                "messages": 0,
                "items": 0,          # trades, of diepte-updates
                "batch_max": 0,      # grootste aantal items in één bericht
                "seq_gaps": 0,
                "seq_missing": 0,    # aantal ontbrekende volgnummers opgeteld
                "latency_ms": [],    # beurs-tijd -> ontvangst
                "parse_us": [],
            },
        )

    def summary(self, seconds: float, queue_max: int, mem_peak: int) -> dict:
        out = {
            "venue": self.venue,
            "duur_s": round(seconds, 1),
            "reconnects": self.reconnects,
            "errors": self.errors[-10:],
            "queue_max": queue_max,
            "tracemalloc_piek_mb": round(mem_peak / 1024 / 1024, 2),
            "streams": {},
        }
        for name, s in self.per_stream.items():
            lat = s["latency_ms"]
            par = s["parse_us"]
            out["streams"][name] = {
                "berichten": s["messages"],
                "items": s["items"],
                "items_per_bericht_max": s["batch_max"],
                "seq_gaps": s["seq_gaps"],
                "seq_missing": s["seq_missing"],
                "latentie_ms_p50": round(statistics.median(lat), 1) if lat else None,
                "latentie_ms_p95": round(sorted(lat)[int(len(lat) * 0.95)], 1) if lat else None,
                "latentie_ms_max": max(lat) if lat else None,
                "parse_us_p95": round(sorted(par)[int(len(par) * 0.95)], 1) if par else None,
            }
        return out


def parse_binance(payload: dict) -> tuple[str, list[dict]] | None:
    """Zet een Binance-bericht om naar (streamnaam, records).

    Eén bericht bevat één trade of één diepte-diff, nooit een lijst.
    """
    stream = payload.get("stream") or ""
    data = payload.get("data") or {}
    kind = data.get("e")
    if kind == "trade":
        ts_ms, unit = to_ms(int(data["T"]))
        return "trade", [
            {
                "venue": "binance",
                "trade_id": data["t"],
                "price": data["p"],
                "qty": data["q"],
                # m = was the buyer the maker; de agressor is de andere kant
                "aggressor": "SELL" if data["m"] else "BUY",
                "aggressor_raw": "SELL" if data["m"] else "BUY",
                "ts_exchange_ms": ts_ms,
                "ts_raw": data["T"],
                "ts_unit": unit,
                "ts_recv_ms": now_ms(),
            }
        ]
    if kind == "depthUpdate":
        ts_ms, unit = to_ms(int(data["E"]))
        return "depth", [
            {
                "venue": "binance",
                "first_update_id": data["U"],
                "final_update_id": data["u"],
                "bids": data["b"],
                "asks": data["a"],
                "ts_exchange_ms": ts_ms,
                "ts_raw": data["E"],
                "ts_unit": unit,
                "ts_recv_ms": now_ms(),
            }
        ]
    return None


def parse_bybit(payload: dict) -> tuple[str, list[dict]] | None:
    """Zet een Bybit-bericht om naar (streamnaam, records).

    Let op: één publicTrade-bericht kan honderden trades bevatten. Wie hier "één
    bericht = één trade" aanneemt, verliest data zonder dat er een fout optreedt.
    """
    topic = payload.get("topic") or ""
    if topic.startswith("publicTrade"):
        out = []
        recv = now_ms()
        for t in payload.get("data") or []:
            ts_ms, unit = to_ms(int(t["T"]))
            raw_side = t.get("S")  # Side of taker: Buy of Sell
            out.append(
                {
                    "venue": "bybit",
                    "trade_id": t["i"],
                    "price": t["p"],
                    "qty": t["v"],
                    # Normaliseer naar BUY/SELL zodat venues vergelijkbaar zijn; de
                    # oorspronkelijke waarde blijft bewaard.
                    "aggressor": raw_side.upper() if raw_side else None,
                    "aggressor_raw": raw_side,
                    "ts_exchange_ms": ts_ms,
                    "ts_raw": t["T"],
                    "ts_unit": unit,
                    "ts_recv_ms": recv,
                }
            )
        return "trade", out
    if topic.startswith("orderbook"):
        d = payload.get("data") or {}
        ts_ms, unit = to_ms(int(payload["ts"]))
        return "depth", [
            {
                "venue": "bybit",
                "type": payload.get("type"),
                "update_id": d.get("u"),
                "seq": d.get("seq"),
                "bids": d.get("b"),
                "asks": d.get("a"),
                "ts_exchange_ms": ts_ms,
                "ts_raw": payload["ts"],
                "ts_unit": unit,
                "ts_recv_ms": now_ms(),
            }
        ]
    return None


def seq_of(venue: str, record: dict) -> tuple[int | None, int | None]:
    """Het bereik van volgnummers waarop het gatenbeleid werkt.

    Binance stuurt per diepte-bericht een bereik [U, u]; opeenvolgende berichten sluiten
    op elkaar aan als het volgende U gelijk is aan het vorige u **plus één**. Vergelijken
    met het vorige U zou dus bij elk bericht een schijngat opleveren. Bybit heeft één
    oplopend `u` per delta.
    """
    if venue == "binance":
        return record.get("first_update_id"), record.get("final_update_id")
    return record.get("update_id"), record.get("update_id")


async def pump(
    session: aiohttp.ClientSession,
    url: str,
    venue: str,
    parse,
    subscribe: dict | None,
    stop_at: float,
    stats: Stats,
    queue: asyncio.Queue,
    gaps: JsonlWriter,
    stats_state: dict,
) -> None:
    backoff = 0.5
    first = True
    while time.monotonic() < stop_at:
        try:
            async with session.ws_connect(url, heartbeat=None, max_msg_size=2**23) as ws:
                print(f"[{venue}] verbonden met {url.split('?')[0]}", flush=True)
                if not first:
                    stats.reconnects += 1
                    # Na een reconnect weten we niet welke volgnummers we gemist hebben
                    # zonder nieuwe snapshot. Registreer het als gat met eigen reden in
                    # plaats van het als seq_jump te tellen.
                    gaps.write(
                        {
                            "venue": venue,
                            "seq_from": stats_state.get(venue),
                            "seq_to": None,
                            "ontbrekend": None,
                            "reden": "reconnect",
                            "ts_local_ms": now_ms(),
                        }
                    )
                    stats_state[venue] = None
                first = False
                if subscribe:
                    await ws.send_json(subscribe)
                backoff = 0.5

                ping_task = None
                if subscribe:
                    async def keepalive() -> None:
                        # Bybit sluit de verbinding als er 20 seconden geen ping is.
                        while True:
                            await asyncio.sleep(15)
                            await ws.send_json({"op": "ping"})

                    ping_task = asyncio.create_task(keepalive())
                try:
                    while time.monotonic() < stop_at:
                        msg = await asyncio.wait_for(ws.receive(), timeout=40)
                        if msg.type != aiohttp.WSMsgType.TEXT:
                            if msg.type in (
                                aiohttp.WSMsgType.CLOSED,
                                aiohttp.WSMsgType.CLOSE,
                                aiohttp.WSMsgType.ERROR,
                            ):
                                raise ConnectionError(f"websocket gesloten: {msg.type}")
                            continue
                        recv = now_ms()
                        t0 = time.perf_counter()
                        try:
                            payload = json.loads(msg.data)
                        except json.JSONDecodeError:
                            stats.stream("parse_error")["messages"] += 1
                            continue
                        parsed = parse(payload)
                        elapsed_us = (time.perf_counter() - t0) * 1e6
                        if parsed is None:
                            continue  # ping/pong en abonnementsbevestigingen
                        stream, records = parsed
                        s = stats.stream(stream)
                        s["messages"] += 1
                        s["items"] += len(records)
                        s["batch_max"] = max(s["batch_max"], len(records))
                        s["parse_us"].append(elapsed_us)
                        if records:
                            s["latency_ms"].append(recv - records[0]["ts_exchange_ms"])
                        if stream == "depth":
                            await queue.put(
                                ("depth", venue, records[0], seq_of(venue, records[0]), stats)
                            )
                        else:
                            await queue.put(("trade", venue, records, None, stats))
                finally:
                    if ping_task:
                        ping_task.cancel()
        except asyncio.CancelledError:
            raise
        except Exception as exc:  # netwerk, sluiting, parse
            stats.errors.append(f"{type(exc).__name__}: {exc}")
            print(f"[{venue}] verbindingsfout: {type(exc).__name__}: {exc}", flush=True)
            pause = backoff * (1 + random.random() * 0.5)
            await asyncio.sleep(pause)
            backoff = min(backoff * 2, 30)


async def drain(queue: asyncio.Queue, writers: dict[str, dict[str, JsonlWriter]],
                 gaps: JsonlWriter, state: dict) -> None:
    """Schrijft weg wat de readers binnenhalen en bewaakt de volgnummers."""
    while True:
        kind, venue, payload, seq, stats = await queue.get()
        state["queue_max"] = max(state.get("queue_max", 0), queue.qsize())
        try:
            if kind == "trade":
                for rec in payload:
                    writers[venue]["trade"].write(rec)
            else:
                writers[venue]["depth"].write(payload)
                if seq is not None:
                    first, last = seq
                    seen = state.get(venue)
                    if first is not None and seen is not None and first > seen + 1:
                        missing = first - seen - 1
                        s = stats.stream("depth")
                        s["seq_gaps"] += 1
                        s["seq_missing"] += missing
                        gaps.write(
                            {
                                "venue": venue,
                                "seq_from": seen,
                                "seq_to": first,
                                "ontbrekend": missing,
                                "reden": "seq_jump",
                                "ts_local_ms": now_ms(),
                            }
                        )
                    if last is not None and (seen is None or last > seen):
                        state[venue] = last
        finally:
            queue.task_done()


async def run(venue: str, minutes: float, out_dir: str) -> dict:
    stop_at = time.monotonic() + minutes * 60
    t_start = time.monotonic()
    stats = Stats(venue)
    writers = {
        venue: {
            "trade": JsonlWriter(os.path.join(out_dir, "trades.jsonl")),
            "depth": JsonlWriter(os.path.join(out_dir, "depth.jsonl")),
        }
    }
    gaps = JsonlWriter(os.path.join(out_dir, "gaps.jsonl"), flush_every=1)
    queue: asyncio.Queue = asyncio.Queue()
    state: dict[str, int | None] = {}

    if venue == "binance":
        target = (BINANCE_URL, "binance", parse_binance, None)
    else:
        target = (
            BYBIT_URL,
            "bybit",
            parse_bybit,
            {"op": "subscribe", "args": BYBIT_ARGS},
        )

    tracemalloc.start()
    async with aiohttp.ClientSession() as session:
        consumer = asyncio.create_task(drain(queue, writers, gaps, state))

        def rapporteer_storing(task: asyncio.Task) -> None:
            """Een schrijftaak die stil sterft, kost je een hele meting. Meld het."""
            if task.cancelled():
                return
            exc = task.exception()
            if exc is not None:
                print(f"[{venue}] schrijftaak gestopt: {type(exc).__name__}: {exc}", flush=True)

        consumer.add_done_callback(rapporteer_storing)

        async def voortgang() -> None:
            while time.monotonic() < stop_at:
                await asyncio.sleep(20)
                delen = [
                    f"{naam}: {s['messages']} berichten, {s['items']} items, "
                    f"{s['seq_gaps']} gaps"
                    for naam, s in stats.per_stream.items()
                ]
                print(
                    f"[{venue}] {int(time.monotonic() - t_start)}s | queue {queue.qsize()} | "
                    + " | ".join(delen),
                    flush=True,
                )

        reporter = asyncio.create_task(voortgang())
        try:
            await pump(session, *target, stop_at, stats, queue, gaps, state)
        finally:
            reporter.cancel()
            await asyncio.sleep(0.5)
            consumer.cancel()
            queue_max = state.get("queue_max", 0)
            _, mem_peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            for w in writers.values():
                for writer in w.values():
                    writer.close()
            gaps.close()

    summary = stats.summary(time.monotonic() - t_start, queue_max, mem_peak)
    summary["trades_weggeschreven"] = writers[venue]["trade"].lines
    summary["diepte_weggeschreven"] = writers[venue]["depth"].lines
    summary["gaten_gelogd"] = gaps.lines
    with open(os.path.join(out_dir, "metrics.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(summary, fh, indent=2, ensure_ascii=False)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--venue", choices=["binance", "bybit", "beide"], default="beide")
    parser.add_argument("--minutes", type=float, default=2.0)
    parser.add_argument("--out", default="data/collector")
    args = parser.parse_args()

    venues = ["binance", "bybit"] if args.venue == "beide" else [args.venue]
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M")
    results = []
    for venue in venues:
        out_dir = os.path.join(args.out, venue, stamp)
        os.makedirs(out_dir, exist_ok=True)
        print(f"{venue}: {args.minutes:g} minuten meten -> {out_dir}", flush=True)
        try:
            results.append(asyncio.run(run(venue, args.minutes, out_dir)))
        except KeyboardInterrupt:
            print("afgebroken", flush=True)
            return 130

    print(json.dumps(results, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
