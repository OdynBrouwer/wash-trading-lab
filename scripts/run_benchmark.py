#!/usr/bin/env python3
"""Benchmark - score D01-D06 op de injecties uit injector.py.

Elke detector krijgt per scenario: recall, precision, F1 en AUC. De drempel komt
uit de spec, dus de AUC laat zien of de detector *scheidt* zonder dat we hem op
de labels hebben afgesteld.

Wat dit wel en niet is staat in docs/08-benchmark.md. Kort: dit meet of de
implementatie klopt, niet of de detector in de echte wereld werkt.

Alleen de standaardbibliotheek.

Gebruik:
    python scripts/run_benchmark.py
    python scripts/run_benchmark.py --days 30 --seed 3
    python scripts/run_benchmark.py --out docs/08-benchmark.md
"""

from __future__ import annotations

import argparse
import sys

import detectors_t0
import injector


# --------------------------------------------------------------------------- #
# Metrieken
# --------------------------------------------------------------------------- #
def auc(scores: list[float], labels: list[bool]) -> float | None:
    """Rank-based AUC (Mann-Whitney), met gemiddelde rangen bij gelijke scores."""
    positives = [s for s, flag in zip(scores, labels) if flag]
    negatives = [s for s, flag in zip(scores, labels) if not flag]
    if not positives or not negatives:
        return None

    ordered = sorted(range(len(scores)), key=lambda i: scores[i])
    ranks = [0.0] * len(scores)
    i = 0
    while i < len(ordered):
        j = i
        while j + 1 < len(ordered) and scores[ordered[j + 1]] == scores[ordered[i]]:
            j += 1
        average = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[ordered[k]] = average
        i = j + 1

    rank_sum = sum(rank for rank, flag in zip(ranks, labels) if flag)
    n_pos = len(positives)
    n_neg = len(negatives)
    return (rank_sum - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg)


def confusion(flags: list[bool], labels: list[bool]) -> dict[str, float]:
    tp = sum(1 for f, l in zip(flags, labels) if f and l)
    fp = sum(1 for f, l in zip(flags, labels) if f and not l)
    fn = sum(1 for f, l in zip(flags, labels) if not f and l)
    tn = sum(1 for f, l in zip(flags, labels) if not f and not l)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if precision + recall else 0.0
    fpr = fp / (fp + tn) if fp + tn else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn,
            "precision": precision, "recall": recall, "f1": f1, "fpr": fpr}


# --------------------------------------------------------------------------- #
# Uitvoeren
# --------------------------------------------------------------------------- #
def evaluate(days: int, seed: int) -> dict[str, dict[str, dict]]:
    """resultaten[scenario][detector] = {metrics..., scores}."""
    results: dict[str, dict[str, dict]] = {}
    for scenario in injector.SCENARIOS:
        bars, labels, calendar = injector.build(scenario, days=days, seed=seed)
        per_detector = {}
        for code in detectors_t0.DETECTORS:
            _name, scores, flags = detectors_t0.run(code, bars, calendar)
            stats = confusion(flags, labels)
            stats["auc"] = auc(scores, labels)
            stats["flagged"] = sum(flags)
            stats["labeled"] = sum(labels)
            per_detector[code] = stats
        results[scenario] = per_detector
    return results


def _fmt(value: float | None, digits: int = 2) -> str:
    return "—" if value is None else f"{value:.{digits}f}"


def render(results: dict[str, dict[str, dict]], days: int, seed: int) -> str:
    codes = list(detectors_t0.DETECTORS)
    lines = [f"### AUC per scenario ({days} dagen, seed {seed})", ""]
    header = "| Scenario | " + " | ".join(codes) + " |"
    lines.append(header)
    lines.append("|---|" + "---|" * len(codes))
    for scenario, per in results.items():
        cells = [_fmt(per[code]["auc"]) for code in codes]
        lines.append(f"| {scenario} | " + " | ".join(cells) + " |")

    lines += ["", "### Recall bij de drempel uit de spec", ""]
    lines.append(header)
    lines.append("|---|" + "---|" * len(codes))
    for scenario, per in results.items():
        cells = [_fmt(per[code]["recall"]) for code in codes]
        lines.append(f"| {scenario} | " + " | ".join(cells) + " |")

    lines += ["", "### Precision bij de drempel uit de spec", ""]
    lines.append(header)
    lines.append("|---|" + "---|" * len(codes))
    for scenario, per in results.items():
        cells = [_fmt(per[code]["precision"]) for code in codes]
        lines.append(f"| {scenario} | " + " | ".join(cells) + " |")

    lines += ["", "### Fout-positieven op schone data (FPR)", ""]
    lines.append(header)
    lines.append("|---|" + "---|" * len(codes))
    for scenario, per in results.items():
        cells = [_fmt(per[code]["fpr"]) for code in codes]
        lines.append(f"| {scenario} | " + " | ".join(cells) + " |")

    lines += ["", "### Wat elke detector vangt", ""]
    for code in codes:
        hits = [s for s, per in results.items()
                if s != "clean" and (per[code]["auc"] or 0) >= 0.80]
        misses = [s for s, per in results.items()
                  if s != "clean" and (per[code]["auc"] or 0) < 0.80]
        lines.append(f"- **{code}** vangt: {', '.join(hits) if hits else 'niets'}"
                     f" — mist: {', '.join(misses) if misses else 'niets'}")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--days", type=int, default=60)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--out", help="schrijf de tabellen naar dit bestand")
    args = parser.parse_args(argv)

    results = evaluate(args.days, args.seed)
    report = render(results, args.days, args.seed)
    print(report)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(report + "\n")
        print(f"\ngeschreven naar {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
