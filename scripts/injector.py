#!/usr/bin/env python3
"""Injector - stop nepvolume in OHLCV met bekende ground truth.

Waarom dit bestaat: een detector zonder ground truth is een mening. Echte
gelabelde CEX-data bestaat niet publiek (zie docs/03-datalandschap.md §6.1).
Deze injector maakt daarom van een schone reeks een reeks met een *bekende*
ingreep en levert per bar een label.

Wat je hiermee wel en niet meet:
- WEL: of de implementatie van een detector doet wat de spec zegt.
- NIET: of de detector in de echte wereld werkt. De injectie is door ons
  bedacht, dus een detector die precies onze injectie herkent, kan in het echt
  nog steeds niets waard zijn. Dat staat ook in docs/08-benchmark.md.

Alleen de standaardbibliotheek. Deterministisch: dezelfde seed geeft dezelfde
reeks, dus een resultaat is altijd te reproduceren.

Gebruik:
    python scripts/injector.py --list
    python scripts/injector.py --scenario volume_sticky --out data/injected.csv
    python scripts/injector.py --scenario zero_gaps --seed 3 --days 30
"""

from __future__ import annotations

import argparse
import csv
import math
import random
import sys

BAR_KEYS = ("ts", "o", "h", "l", "c", "v")

# Uurprofiel van een markt met EU/US-overwicht. Gemiddelde is 1,0.
HOUR_PROFILE = (
    0.62, 0.55, 0.50, 0.48, 0.50, 0.56,
    0.62, 0.72, 0.85, 0.95, 0.98, 0.94,
    0.92, 1.08, 1.25, 1.38, 1.42, 1.35,
    1.22, 1.15, 1.08, 0.95, 0.82, 0.70,
)


# --------------------------------------------------------------------------- #
# Een schone basisreeks
# --------------------------------------------------------------------------- #
def synthesize_ohlcv(days: int = 60, interval_min: int = 15, seed: int = 7,
                     start_price: float = 30_000.0) -> list[dict]:
    """Maak een OHLCV-reeks met de eigenschappen waar T0-detectoren op leunen.

    Bewust aanwezig: intraday-seizoenspatroon, positieve samenhang tussen
    absolute return en volume, en af en toe een echte nieuwspiek. Zonder die
    eigenschappen zou elke detector gratis gelijk krijgen.
    """
    rng = random.Random(seed)
    n = days * 24 * 60 // interval_min
    bars: list[dict] = []
    price = start_price
    t0 = 1_700_000_000 - (1_700_000_000 % (interval_min * 60))

    for i in range(n):
        hour = ((i * interval_min) // 60) % 24
        ret = rng.gauss(0.0, 0.0009)
        open_p = price
        close_p = open_p * (1.0 + ret)
        wick = abs(rng.gauss(0.0, 0.0005))
        high_p = max(open_p, close_p) * (1.0 + wick)
        low_p = min(open_p, close_p) * (1.0 - wick)

        volume = (1_200.0 * HOUR_PROFILE[hour]
                  * math.exp(rng.gauss(0.0, 0.40))
                  * (1.0 + 2.0 * abs(ret) / 0.0009))
        if rng.random() < 0.01:  # echte nieuwspiek
            volume *= rng.uniform(3.0, 6.0)

        bars.append({
            "ts": t0 + i * interval_min * 60,
            "o": round(open_p, 2),
            "h": round(high_p, 2),
            "l": round(low_p, 2),
            "c": round(close_p, 2),
            "v": round(volume, 4),
        })
        price = close_p

    return bars


def load_ohlcv_csv(path: str) -> list[dict]:
    """Lees een OHLCV-CSV. Kolomnamen mogen afwijken; we zoeken op naam."""
    aliases = {
        "ts": {"ts", "timestamp", "time", "opentime", "open_time", "date"},
        "o": {"o", "open"},
        "h": {"h", "high"},
        "l": {"l", "low"},
        "c": {"c", "close"},
        "v": {"v", "volume", "vol", "basevolume", "base_volume"},
    }
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError(f"{path}: geen kopregel")
        lookup = {}
        for column in reader.fieldnames:
            key = column.strip().lower()
            for target, names in aliases.items():
                if key in names:
                    lookup[target] = column
        missing = [k for k in BAR_KEYS if k not in lookup]
        if missing:
            raise ValueError(f"{path}: kolommen ontbreken: {', '.join(missing)}")

        bars = []
        for row in reader:
            bars.append({
                "ts": int(float(row[lookup["ts"]])),
                "o": float(row[lookup["o"]]),
                "h": float(row[lookup["h"]]),
                "l": float(row[lookup["l"]]),
                "c": float(row[lookup["c"]]),
                "v": float(row[lookup["v"]]),
            })
    return bars


# --------------------------------------------------------------------------- #
# Ingrepen
# --------------------------------------------------------------------------- #
def _episodes(rng: random.Random, n: int, count: int, low: int, high: int,
              min_gap: int) -> list[tuple[int, int]]:
    """Kies niet-overlappende periodes (start, lengte) met tussenruimte."""
    starts: list[int] = []
    for _ in range(count * 40):
        if len(starts) >= count:
            break
        length = rng.randint(low, high)
        start = rng.randint(0, max(0, n - length - 1))
        if any(abs(start - s) < length + min_gap for s in starts):
            continue
        starts.append(start)
    return sorted((s, rng.randint(low, high)) for s in starts)


def _decoys(rng: random.Random, n: int, count: int, busy: set[int]) -> list[int]:
    """Tijdstippen die geen ingreep zijn: de kalender moet ook ruis aankunnen."""
    picks: list[int] = []
    for _ in range(count * 40):
        if len(picks) >= count:
            break
        idx = rng.randint(0, n - 1)
        if idx in busy or any(abs(idx - p) < 12 for p in picks):
            continue
        picks.append(idx)
    return picks


def scenario_clean(bars, rng):
    return bars, [False] * len(bars), []


def scenario_volume_sticky(bars, rng):
    """F1/F2 op T0-niveau: volume omhoog, prijs beweegt niet mee."""
    out = [dict(b) for b in bars]
    labels = [False] * len(bars)
    for start, length in _episodes(rng, len(bars), count=12, low=3, high=8, min_gap=40):
        factor = rng.uniform(3.0, 9.0)
        for i in range(start, min(start + length, len(bars))):
            out[i]["v"] = round(out[i]["v"] * factor, 4)
            labels[i] = True
    return out, labels, []


def scenario_volume_moved(bars, rng):
    """Controlegroep: veel volume MET echte prijsbeweging. Mag niet verdacht zijn."""
    out = [dict(b) for b in bars]
    labels = [False] * len(bars)
    for start, length in _episodes(rng, len(bars), count=12, low=3, high=8, min_gap=40):
        factor = rng.uniform(3.0, 9.0)
        for i in range(start, min(start + length, len(bars))):
            bar = out[i]
            bar["v"] = round(bar["v"] * factor, 4)
            spread = factor ** 0.5
            mid = (bar["h"] + bar["l"]) / 2.0
            bar["h"] = round(mid + (bar["h"] - mid) * spread, 2)
            bar["l"] = round(mid - (mid - bar["l"]) * spread, 2)
            labels[i] = True
    return out, labels, []


def scenario_event_spike(bars, rng):
    """F5: piek rond een bekend tijdstip, zonder range-expansie. Levert de kalender."""
    out = [dict(b) for b in bars]
    labels = [False] * len(bars)
    starts: list[int] = []
    for start, length in _episodes(rng, len(bars), count=10, low=2, high=4, min_gap=60):
        factor = rng.uniform(3.5, 8.0)
        for i in range(max(0, start - 2), min(start + length + 2, len(bars))):
            out[i]["v"] = round(out[i]["v"] * factor, 4)
            labels[i] = True
        starts.append(start)
    busy = {i for i, flag in enumerate(labels) if flag}
    calendar = [out[i]["ts"] for i in starts] + [out[i]["ts"] for i in _decoys(rng, len(bars), 10, busy)]
    return out, labels, sorted(calendar)


def scenario_zero_gaps(bars, rng):
    """F1-rest: uren met veel volume, dan exact nul, dan weer volume."""
    out = [dict(b) for b in bars]
    labels = [False] * len(bars)
    busy = set()
    for start, _ in _episodes(rng, len(bars), count=25, low=1, high=2, min_gap=30):
        idx = start
        if idx in busy:
            continue
        out[idx]["v"] = 0.0
        labels[idx] = True
        busy.add(idx)
    return out, labels, []


def scenario_flat_session(bars, rng):
    """Volume zonder dag-en-nachtpatroon: uurprofiel weggepoetst (middelste deel)."""
    out = [dict(b) for b in bars]
    labels = [False] * len(bars)
    mid = len(bars) // 2
    span = min(20 * 96, len(bars) - mid)
    window = out[mid:mid + span]
    level = sum(b["v"] for b in window) / len(window)
    for offset, bar in enumerate(window):
        bar["v"] = round(level * (1.0 + rng.uniform(-0.05, 0.05)), 4)
        labels[mid + offset] = True
    return out, labels, []


def scenario_constant_volume(bars, rng):
    """Bijna geen spreiding meer in de groottes: uniformiteit van D09/D02."""
    out = [dict(b) for b in bars]
    labels = [False] * len(bars)
    mid = len(bars) // 2
    window = out[mid:mid + 20 * 96]
    level = sorted(b["v"] for b in window)[len(window) // 2]
    for offset, bar in enumerate(window):
        bar["v"] = round(level * (1.0 + rng.uniform(-0.02, 0.02)), 4)
        labels[mid + offset] = True
    return out, labels, []


def scenario_anti_correlated(bars, rng):
    """Volume dat niet met de prijs meebeweegt: D03 moet dit vangen."""
    out = [dict(b) for b in bars]
    labels = [False] * len(bars)
    mid = len(bars) // 2
    window = out[mid:mid + 20 * 96]
    level = sum(b["v"] for b in window) / len(window)
    for offset, bar in enumerate(window):
        bar["v"] = round(level * math.exp(rng.gauss(0.0, 0.40)), 4)
        labels[mid + offset] = True
    return out, labels, []


SCENARIOS = {
    "clean": scenario_clean,
    "volume_sticky": scenario_volume_sticky,
    "volume_moved": scenario_volume_moved,
    "event_spike": scenario_event_spike,
    "zero_gaps": scenario_zero_gaps,
    "flat_session": scenario_flat_session,
    "constant_volume": scenario_constant_volume,
    "anti_correlated": scenario_anti_correlated,
}


def build(scenario: str, days: int = 60, seed: int = 7,
          bars: list[dict] | None = None) -> tuple[list[dict], list[bool], list[int]]:
    """Bouw een scenario. Geeft (bars, labels, eventkalender)."""
    if scenario not in SCENARIOS:
        raise KeyError(f"onbekend scenario: {scenario}")
    base = bars if bars is not None else synthesize_ohlcv(days=days, seed=seed)
    rng = random.Random(seed * 1_000_003 + len(scenario))
    return SCENARIOS[scenario](base, rng)


# --------------------------------------------------------------------------- #
# Uitvoer
# --------------------------------------------------------------------------- #
def write_csv(path: str, bars: list[dict], labels: list[bool] | None = None) -> None:
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(list(BAR_KEYS) + (["injected"] if labels else []))
        for i, bar in enumerate(bars):
            row = [bar[k] for k in BAR_KEYS]
            if labels:
                row.append(int(labels[i]))
            writer.writerow(row)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--scenario", help="welk scenario (zie --list)")
    parser.add_argument("--out", help="schrijf de reeks als CSV")
    parser.add_argument("--days", type=int, default=60)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--list", action="store_true", help="toon de scenario's")
    args = parser.parse_args(argv)

    if args.list or not args.scenario:
        for name in SCENARIOS:
            print(name)
        return 0

    bars, labels, calendar = build(args.scenario, days=args.days, seed=args.seed)
    print(f"{args.scenario}: {len(bars)} bars, {sum(labels)} gelabeld, "
          f"{len(calendar)} kandidaten in de eventkalender")
    if args.out:
        write_csv(args.out, bars, labels)
        print(f"geschreven naar {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
