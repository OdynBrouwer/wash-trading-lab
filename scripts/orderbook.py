"""Orderboek opbouwen uit een REST-snapshot plus de websocket-diffs.

De collector (`scripts/collector.py`) telt diepte-berichten en bewaakt de volgnummers,
maar weet niet wat er in het boek staat. Dit bestand bouwt dat boek wél op, met de
regels die elke beurs zelf voorschrijft:

- **Binance spot**: haal een snapshot met `lastUpdateId`, gooi alles weg met
  `u <= lastUpdateId`, en accepteer daarna alleen events die aansluiten. Het eerste
  event mag overlappen (`U <= lastUpdateId + 1 <= u`) — dat is geen gat maar het
  event dat de snapshot overbrugt.
- **Bybit spot**: de websocket stuurt eerst een snapshot, daarna deltas met een
  oplopend `u`. Elke delta moet precies `u == vorige + 1` zijn.

Wijkt het volgnummer af, dan is het boek niet meer te vertrouwen en wordt het
opnieuw opgebouwd. Dat is geen fout maar het gatenbeleid uit docs/07-datalaag.md §6:
een gat registreren, nooit opvullen.

Bedragen en hoeveelheden gaan als `Decimal` door het boek, niet als float. Een prijs
als floatsleutel gebruiken betekent dat twee levels die de beurs als dezelfde prijs
bedoelt, net naast elkaar kunnen liggen.

    python scripts/orderbook.py --minutes 2
    python scripts/orderbook.py --venue bybit --minutes 1
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from decimal import Decimal, InvalidOperation
from pathlib import Path

import aiohttp

sys.path.insert(0, str(Path(__file__).resolve().parent))

from collector import (  # noqa: E402
    BINANCE_URL,
    BYBIT_ARGS,
    BYBIT_URL,
    now_ms,
    parse_binance,
    parse_bybit,
)

BINANCE_SNAPSHOT = "https://api.binance.com/api/v3/depth?symbol=BTCUSDT&limit=1000"
BYBIT_SNAPSHOT = "https://api.bybit.com/v5/market/orderbook?category=spot&symbol=BTCUSDT&limit=200"


class Book:
    """Prijsniveaus per kant, met de controle of het boek ooit gekruist raakt."""

    def __init__(self) -> None:
        self.bids: dict[Decimal, Decimal] = {}
        self.asks: dict[Decimal, Decimal] = {}
        self.applied = 0
        self.crossed_events = 0
        self.levels_removed = 0

    @staticmethod
    def _levels(raw) -> list[tuple[Decimal, Decimal]]:
        out = []
        for level in raw or []:
            try:
                out.append((Decimal(level[0]), Decimal(level[1])))
            except (InvalidOperation, IndexError, TypeError):
                continue
        return out

    def apply(self, bids, asks) -> None:
        for price, qty in self._levels(bids):
            if qty == 0:
                if self.bids.pop(price, None) is not None:
                    self.levels_removed += 1
            else:
                self.bids[price] = qty
        for price, qty in self._levels(asks):
            if qty == 0:
                if self.asks.pop(price, None) is not None:
                    self.levels_removed += 1
            else:
                self.asks[price] = qty
        self.applied += 1
        if self.is_crossed():
            self.crossed_events += 1

    def replace(self, bids, asks) -> None:
        self.bids = {p: q for p, q in self._levels(bids) if q != 0}
        self.asks = {p: q for p, q in self._levels(asks) if q != 0}

    def best_bid(self) -> Decimal | None:
        return max(self.bids) if self.bids else None

    def best_ask(self) -> Decimal | None:
        return min(self.asks) if self.asks else None

    def is_crossed(self) -> bool:
        bid, ask = self.best_bid(), self.best_ask()
        return bid is not None and ask is not None and bid >= ask

    def top(self, n: int = 5) -> dict:
        bids = sorted(self.bids.items(), reverse=True)[:n]
        asks = sorted(self.asks.items())[:n]
        return {
            "bids": [[str(p), str(q)] for p, q in bids],
            "asks": [[str(p), str(q)] for p, q in asks],
        }

    def spread_bps(self) -> float | None:
        bid, ask = self.best_bid(), self.best_ask()
        if bid is None or ask is None or bid <= 0:
            return None
        mid = (bid + ask) / 2
        return float((ask - bid) / mid * 10000)


class Sequencer:
    """Houdt bij of het boek nog aansluit op de stream."""

    def __init__(self, venue: str, book: Book) -> None:
        self.venue = venue
        self.book = book
        self.last_update_id: int | None = None
        self.snapshots = 0
        self.resyncs = 0
        self.dropped = 0
        self.applied = 0
        self.last_reason = ""

    def load_snapshot(self, update_id: int, bids, asks) -> None:
        self.book.replace(bids, asks)
        self.last_update_id = int(update_id)
        self.snapshots += 1

    def feed(self, record: dict) -> str:
        """Verwerk één diepte-record. Geeft terug wat er gebeurde."""
        if self.venue == "bybit" and record.get("type") == "snapshot":
            upd = record.get("update_id")
            if upd is None:
                return "genegeerd"
            self.load_snapshot(upd, record.get("bids"), record.get("asks"))
            return "snapshot"

        if self.last_update_id is None:
            return "niet_gesynchroniseerd"

        if self.venue == "binance":
            first = record.get("first_update_id")
            last = record.get("final_update_id")
            if first is None or last is None:
                return "genegeerd"
            if last <= self.last_update_id:
                self.dropped += 1
                return "weggegooid"          # zat al in de snapshot
            if first <= self.last_update_id + 1:
                self.book.apply(record.get("bids"), record.get("asks"))
                self.last_update_id = last
                self.applied += 1
                return "toegepast"
            self.resyncs += 1
            self.last_reason = f"gat: verwacht {self.last_update_id + 1}, kreeg {first}"
            self.last_update_id = None
            return "resync"

        uid = record.get("update_id")
        if uid is None:
            return "genegeerd"
        if uid <= self.last_update_id:
            self.dropped += 1
            return "weggegooid"
        if uid != self.last_update_id + 1:
            self.resyncs += 1
            self.last_reason = f"gat: verwacht {self.last_update_id + 1}, kreeg {uid}"
            self.last_update_id = None
            return "resync"
        self.book.apply(record.get("bids"), record.get("asks"))
        self.last_update_id = uid
        self.applied += 1
        return "toegepast"


async def fetch_binance_snapshot(session: aiohttp.ClientSession) -> tuple[int, list, list]:
    async with session.get(BINANCE_SNAPSHOT) as r:
        data = await r.json()
    return data["lastUpdateId"], data["bids"], data["asks"]


async def fetch_bybit_snapshot(session: aiohttp.ClientSession) -> tuple[int, list, list]:
    async with session.get(BYBIT_SNAPSHOT) as r:
        data = await r.json()
    result = data["result"]
    return result["u"], result["b"], result["a"]


async def run(venue: str, minutes: float) -> dict:
    book = Book()
    seq = Sequencer(venue, book)
    url = BINANCE_URL if venue == "binance" else BYBIT_URL
    subscribe = None if venue == "binance" else {"op": "subscribe", "args": BYBIT_ARGS}
    parse = parse_binance if venue == "binance" else parse_bybit
    fetch = fetch_binance_snapshot if venue == "binance" else fetch_bybit_snapshot

    stop_at = time.monotonic() + minutes * 60
    t_start = time.monotonic()
    messages = 0
    errors: list[str] = []
    t_last_update = t_start

    async with aiohttp.ClientSession() as session:
        if venue == "binance":
            upd, bids, asks = await fetch(session)
            seq.load_snapshot(upd, bids, asks)
            print(f"[{venue}] REST-snapshot: update {upd}, "
                  f"{len(bids)} bids / {len(asks)} asks", flush=True)

        async with session.ws_connect(url, heartbeat=None, max_msg_size=2**23) as ws:
            if subscribe:
                await ws.send_json(subscribe)

            async def keepalive() -> None:
                while True:
                    await asyncio.sleep(15)
                    await ws.send_json({"op": "ping"})

            ping = asyncio.create_task(keepalive()) if subscribe else None
            try:
                while time.monotonic() < stop_at:
                    msg = await asyncio.wait_for(ws.receive(), timeout=40)
                    if msg.type != aiohttp.WSMsgType.TEXT:
                        continue
                    parsed = parse(json.loads(msg.data))
                    if parsed is None:
                        continue
                    stream, records = parsed
                    if stream != "depth":
                        continue
                    messages += 1
                    record = records[0]
                    outcome = seq.feed(record)
                    if outcome in ("toegepast", "snapshot"):
                        t_last_update = time.monotonic()
                    if outcome == "resync":
                        upd, bids, asks = await fetch(session)
                        seq.load_snapshot(upd, bids, asks)
            except Exception as exc:
                errors.append(f"{type(exc).__name__}: {exc}")
                print(f"[{venue}] fout: {errors[-1]}", flush=True)
            finally:
                if ping:
                    ping.cancel()

        # Eindcontrole: klopt het boek nog met een verse snapshot?
        pauze = time.monotonic() - t_last_update
        upd, bids, asks = await fetch(session)

    ref = Book()
    ref.replace(bids, asks)
    mid_boek = (book.best_bid() + book.best_ask()) / 2 if book.best_bid() and book.best_ask() else None
    mid_rest = (ref.best_bid() + ref.best_ask()) / 2 if ref.best_bid() and ref.best_ask() else None
    return {
        "venue": venue,
        "duur_s": round(time.monotonic() - t_start, 1),
        "diepte_berichten": messages,
        "toegepast": seq.applied,
        "weggegooid": seq.dropped,
        "snapshots": seq.snapshots,
        "resyncs": seq.resyncs,
        "laatste_reden": seq.last_reason,
        "gekruist": book.crossed_events,
        "levels_verwijderd": book.levels_removed,
        "levels_bid": len(book.bids),
        "levels_ask": len(book.asks),
        "boek_best_bid": str(book.best_bid()),
        "boek_best_ask": str(book.best_ask()),
        "boek_spread_bps": round(book.spread_bps(), 2) if book.spread_bps() else None,
        "rest_update_id": upd,
        "rest_best_bid": str(ref.best_bid()),
        "rest_best_ask": str(ref.best_ask()),
        "seconden_sinds_laatste_update": round(pauze, 2),
        "verschil_mid_usdt": (
            round(float(abs(mid_boek - mid_rest)), 4)
            if mid_boek is not None and mid_rest is not None else None
        ),
        "fouten": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--venue", choices=["binance", "bybit", "beide"], default="beide")
    parser.add_argument("--minutes", type=float, default=2.0)
    parser.add_argument("--out", default="data/orderbook")
    args = parser.parse_args()

    venues = ["binance", "bybit"] if args.venue == "beide" else [args.venue]
    Path(args.out).mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y-%m-%dT%H%M", time.gmtime())
    results = []
    for venue in venues:
        print(f"{venue}: {args.minutes:g} minuten boek opbouwen", flush=True)
        results.append(asyncio.run(run(venue, args.minutes)))
        print(json.dumps(results[-1], indent=2, ensure_ascii=False), flush=True)

    with open(Path(args.out) / f"check-{stamp}.json", "w", encoding="utf-8", newline="\n") as fh:
        json.dump(results, fh, indent=2, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
