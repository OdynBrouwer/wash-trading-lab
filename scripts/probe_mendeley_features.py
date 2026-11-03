"""Lees een stuk van de Falk et al. (2026) feature-tabel en scoor elke kolom apart.

De dataset staat op Mendeley (DOI 10.17632/4hyxfwzpgg.2, CC BY 4.0). De bestanden zijn
te groot om te committen (gox 940 MB, OpenSea 2 GB), daarom haalt dit script met een
HTTP-Range-verzoek alleen het begin op en rekent in het geheugen. Er wordt niets
opgeslagen.

Doel: laten zien welke features wash trades scheiden, en vooral welke *niet*. De
features die je uit publieke bars kunt halen (prijsafwijking, ronde niveaus, timing,
uur van de dag) horen bij T0; de trade-counts per tegenpartij horen bij T3.

    python scripts/probe_mendeley_features.py --file gox_ml_samples.csv --mb 24
"""

from __future__ import annotations

import argparse
import csv
import json
import urllib.request

API = "https://data.mendeley.com/public-api/datasets/4hyxfwzpgg/files?folder_id=root&version=2"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def auc(values: list[float], labels: list[bool]) -> float | None:
    """Rank-based AUC met gemiddelde rangen bij gelijke waarden."""
    pairs = sorted(zip(values, labels))
    npos = sum(1 for _, lab in pairs if lab)
    nneg = len(pairs) - npos
    if not npos or not nneg:
        return None

    rank_sum = 0.0
    i = 0
    while i < len(pairs):
        j = i
        while j + 1 < len(pairs) and pairs[j + 1][0] == pairs[i][0]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1
        rank_sum += sum(avg_rank for k in range(i, j + 1) if pairs[k][1])
        i = j + 1

    return (rank_sum - npos * (npos + 1) / 2.0) / (npos * nneg)


def fetch(url: str, byte_range: str | None = None) -> bytes:
    headers = dict(UA)
    if byte_range:
        headers["Range"] = byte_range
    return urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()


def download_url(filename: str) -> str:
    files = json.loads(fetch(API))
    for entry in files:
        if entry["filename"] == filename:
            return entry["content_details"]["download_url"]
    raise SystemExit(f"{filename} zit niet in de dataset; wel: " + ", ".join(f["filename"] for f in files))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", default="gox_ml_samples.csv")
    parser.add_argument("--mb", type=int, default=24, help="hoeveel MB vanaf het begin")
    parser.add_argument("--label", default="wash")
    args = parser.parse_args()

    raw = fetch(download_url(args.file), f"bytes=0-{args.mb * 1024 * 1024 - 1}")
    rows = list(csv.reader(raw.decode("utf-8", "replace").split("\n")[:-1]))
    header, data = rows[0], rows[1:]
    label_at = header.index(args.label)

    positives = sum(1 for r in data if r[label_at] == "True")
    print(f"{args.file}: {len(header)} kolommen, {len(data):,} rijen, "
          f"{positives:,} met {args.label}=True ({100.0 * positives / len(data):.1f}%)")

    scored = []
    for col, name in enumerate(header):
        if col == label_at:
            continue
        try:
            values = [float(r[col]) for r in data]
        except ValueError:
            continue
        value = auc(values, [r[label_at] == "True" for r in data])
        if value is not None:
            scored.append((value, name))

    print(f"\n{'feature':<28} {'AUC':>6}")
    for value, name in sorted(scored, reverse=True):
        print(f"{name:<28} {value:6.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
