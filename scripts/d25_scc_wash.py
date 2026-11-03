#!/usr/bin/env python3
"""D25 - wash-trade detection via strongly connected components.

Implementatie van Victor & Weintraud (WWW '21), *Detecting and Quantifying Wash
Trading on Decentralized Cryptocurrency Exchanges*, algoritme 1 (iteratief SCC's
tellen) en algoritme 2 (volume matching).

Formules: zie `washtrading-formules.md` §10.

Alleen de standaardbibliotheek. Geen pandas, geen networkx.

Gebruik:
    python scripts/d25_scc_wash.py --csv data/EtherDeltaTrades.slice.csv
    python scripts/d25_scc_wash.py --csv data/slice.csv --min-occurrence 10 --max-rows 400000

Beperkingen die je moet kennen:
- Self-trades (verkoper == koper) zijn per definitie wash trades en worden apart
  geteld; ze zijn geen SCC van twee knopen.
- De uitkomst is een ONDERGRENS: de drempels zijn conservatief gekozen.
- Zonder de volledige dataset haalt een SCC zelden de drempel van 100 voorkomens.
  Verlaag dan --min-occurrence en lees het resultaat als demonstratie, niet als meting.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict

ETH = "0x0000000000000000000000000000000000000000"
WEI = 10**18


# --------------------------------------------------------------------------- #
# Inlezen
# --------------------------------------------------------------------------- #
def read_etherdelta(path: str, max_rows: int | None = None):
    """Lees EtherDelta-trades en reducerer tot (ts, token, koper, verkoper, volume_eth).

    EtherDelta Trade-event: `get` ontvangt `tokenGet`, `give` levert `tokenGive`.
    De niet-ETH-kant bepaalt de richting van de tokenstroom; de ETH-kant het volume.
    Trades tussen twee tokens worden overgeslagen (zoals in de paper).
    """
    rows = 0
    with open(path, newline="", encoding="utf-8") as fh:
        for rec in csv.DictReader(fh):
            rows += 1
            if max_rows and rows > max_rows:
                return
            # Een slice kan midden in een regel eindigen; dan levert DictReader
            # None-waarden. Zulke rijen overslaan in plaats van crashen.
            if any(rec.get(k) is None for k in
                   ("tokenGet", "tokenGive", "get", "give",
                    "amountGet", "amountGive", "timestamp")):
                continue
            token_get = rec["tokenGet"].lower()
            token_give = rec["tokenGive"].lower()
            getter = rec["get"].lower()
            giver = rec["give"].lower()
            try:
                ts = int(rec["timestamp"])
            except (TypeError, ValueError):
                continue

            if token_give == ETH:
                token, seller, buyer, raw = token_get, giver, getter, rec["amountGive"]
            elif token_get == ETH:
                token, seller, buyer, raw = token_give, getter, giver, rec["amountGet"]
            else:
                continue

            try:
                vol = int(raw) / WEI
            except (TypeError, ValueError):
                continue
            if vol <= 0:
                continue
            yield ts, token, buyer, seller, vol


# --------------------------------------------------------------------------- #
# Algoritme 1 - iteratief strongly connected components tellen
# --------------------------------------------------------------------------- #
def tarjan_scc(nodes, adj):
    """Iteratieve Tarjan. Geeft een lijst van knoopverzamelingen."""
    index: dict[str, int] = {}
    low: dict[str, int] = {}
    on_stack: set[str] = set()
    stack: list[str] = []
    result: list[set[str]] = []
    counter = 0

    for root in nodes:
        if root in index:
            continue
        index[root] = low[root] = counter
        counter += 1
        stack.append(root)
        on_stack.add(root)
        work = [(root, iter(adj.get(root, ())))]

        while work:
            v, it = work[-1]
            advanced = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = counter
                    counter += 1
                    stack.append(w)
                    on_stack.add(w)
                    work.append((w, iter(adj.get(w, ()))))
                    advanced = True
                    break
                if w in on_stack and index[w] < low[v]:
                    low[v] = index[w]
            if advanced:
                continue

            work.pop()
            if work:
                parent = work[-1][0]
                if low[v] < low[parent]:
                    low[parent] = low[v]
            if low[v] == index[v]:
                comp: set[str] = set()
                while True:
                    w = stack.pop()
                    on_stack.discard(w)
                    comp.add(w)
                    if w == v:
                        break
                result.append(comp)

    return result


def iterative_scc_counting(edges: dict[tuple[str, str], int], max_iter: int):
    """Algoritme 1. `edges` is {(u, v): multipliciteit}. Geeft {frozenset: aantal}."""
    weights = dict(edges)
    counts: dict[frozenset, int] = defaultdict(int)
    truncated = False

    for _ in range(max_iter):
        adj: dict[str, list[str]] = defaultdict(list)
        nodes = set()
        for (u, v), w in weights.items():
            if w > 0:
                adj[u].append(v)
                nodes.add(u)
                nodes.add(v)
        if not nodes:
            break

        for comp in tarjan_scc(sorted(nodes), adj):
            if len(comp) > 1:
                counts[frozenset(comp)] += 1

        empty = []
        for key in weights:
            weights[key] -= 1
            if weights[key] <= 0:
                empty.append(key)
        for key in empty:
            del weights[key]
        if not weights:
            break
    else:
        truncated = True

    return counts, truncated


# --------------------------------------------------------------------------- #
# Algoritme 2 - volume matching
# --------------------------------------------------------------------------- #
def volume_matching(trades, margin: float):
    """Algoritme 2. `trades` = lijst (ts, koper, verkoper, volume), tijdgesorteerd.

    Geeft de gevonden wash-set of None. Positie p_i = gekocht - verkocht; alle
    deelnemers moeten op |p_i| <= m * gemiddeld volume uitkomen.
    """
    current = list(trades)
    while len(current) > 1:
        positions: dict[str, float] = {}
        total = 0.0
        for _ts, buyer, seller, vol in current:
            positions[buyer] = positions.get(buyer, 0.0) + vol
            positions[seller] = positions.get(seller, 0.0) - vol
            total += vol
        mean_vol = total / len(current)
        if mean_vol > 0 and all(abs(p) <= margin * mean_vol for p in positions.values()):
            return current
        current.pop()
    return None


WINDOWS = (3600, 86400, 604800)  # 1 uur, 1 dag, 1 week


def find_wash_sets(trades, margin: float):
    """Drie passes over de trades van één SCC, van klein naar groot venster."""
    labeled: set[int] = set()
    found: list[list[tuple]] = []

    for window in WINDOWS:
        i = 0
        while i < len(trades):
            if i in labeled:
                i += 1
                continue
            start_ts = trades[i][0]
            j = i
            block = []
            while j < len(trades) and (trades[j][0] - start_ts) <= window:
                if j not in labeled:
                    block.append((j, trades[j]))
                j += 1
            if len(block) > 1:
                result = volume_matching([t for _, t in block], margin)
                if result:
                    hit = block[len(block) - len(result):]
                    for idx, _ in hit:
                        labeled.add(idx)
                    found.append([t for _, t in hit])
            i = j if j > i else i + 1

    return found


# --------------------------------------------------------------------------- #
# Hoofdprogramma
# --------------------------------------------------------------------------- #
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="D25 - wash trading via SCC's")
    ap.add_argument("--csv", required=True, help="EtherDeltaTrades.csv (of een slice)")
    ap.add_argument("--min-occurrence", type=int, default=100,
                    help="SCC moet zo vaak voorkomen om kandidaat te zijn (default 100)")
    ap.add_argument("--margin", type=float, default=0.01,
                    help="marge op de gemiddelde tradegrootte (default 0.01)")
    ap.add_argument("--max-iter", type=int, default=200,
                    help="maximum aantal SCC-iteraties (default 200)")
    ap.add_argument("--max-rows", type=int, default=None, help="inlezen beperken tot N rijen")
    args = ap.parse_args(argv)

    # 1. inlezen
    trades_by_token: dict[str, list[tuple]] = defaultdict(list)
    self_trades = 0
    self_volume = 0.0
    total_trades = 0
    total_volume = 0.0
    min_ts = max_ts = None

    for ts, token, buyer, seller, vol in read_etherdelta(args.csv, args.max_rows):
        total_trades += 1
        total_volume += vol
        if min_ts is None or ts < min_ts:
            min_ts = ts
        if max_ts is None or ts > max_ts:
            max_ts = ts
        if buyer == seller:
            self_trades += 1
            self_volume += vol
            continue
        trades_by_token[token].append((ts, buyer, seller, vol))

    if not total_trades:
        print("Geen bruikbare trades gevonden.")
        return 1

    print(f"Trades met ETH-leg      : {total_trades:,}")
    print(f"Tokens                  : {len(trades_by_token):,}")
    print(f"Volume                  : {total_volume:,.2f} ETH")
    print(f"Self-trades             : {self_trades:,}  ({self_volume:,.2f} ETH)")
    print(f"Periode                 : {min_ts} .. {max_ts} (unix)")

    # 2. per token: SCC's tellen
    candidates = 0
    multi_sets: list[tuple[str, frozenset]] = []
    truncated_tokens = 0

    for token, trades in trades_by_token.items():
        edges: dict[tuple[str, str], int] = defaultdict(int)
        for _ts, buyer, seller, _vol in trades:
            edges[(seller, buyer)] += 1
        counts, truncated = iterative_scc_counting(edges, args.max_iter)
        if truncated:
            truncated_tokens += 1
        for comp, count in counts.items():
            if count >= args.min_occurrence:
                candidates += 1
                multi_sets.append((token, comp))

    print(f"\nKandidaat-SCC's (>= {args.min_occurrence} voorkomens): {candidates:,}")
    if truncated_tokens:
        print(f"  let op: {truncated_tokens} token(s) afgekapt op --max-iter")

    # 3. volume matching per kandidaat
    wash_trades = 0
    wash_volume = 0.0
    shapes: dict[int, int] = defaultdict(int)

    for token, comp in multi_sets:
        relevant = [
            t for t in sorted(trades_by_token[token], key=lambda x: x[0])
            if t[1] in comp and t[2] in comp
        ]
        if len(relevant) < 2:
            continue
        for group in find_wash_sets(relevant, args.margin):
            wash_trades += len(group)
            wash_volume += sum(t[3] for t in group)
            participants = {t[1] for t in group} | {t[2] for t in group}
            shapes[len(participants)] += 1

    print(f"\nWash trades (multi-account): {wash_trades:,}  ({wash_volume:,.2f} ETH)")
    print(f"Gevonden wash-sets         : {sum(shapes.values()):,}")
    if shapes:
        print("  deelnemers per set       : " + ", ".join(
            f"{k}->{v}" for k, v in sorted(shapes.items())))
    print("\nLet op: dit is een ONDERGRENS. Drempels zijn conservatief gekozen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
