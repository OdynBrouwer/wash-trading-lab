#!/usr/bin/env python3
"""D01-D06 - de T0-detectoren, zoals gespecificeerd in docs/02-detectoren.md.

Elke detector geeft per bar een score waarbij **hoger = verdachter**. De flag is
score > drempel, en die drempel komt uit de spec -- niet uit de labels. Anders
zou de benchmark zichzelf leggen.

Alleen de standaardbibliotheek.

    from detectors_t0 import DETECTORS, run
    name, scores, flags = run("D01", bars)
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable

DAY_15M = 96          # bars per dag bij 15 minuten
WEEK_15M = 7 * DAY_15M


# --------------------------------------------------------------------------- #
# Robuuste statistiek
# --------------------------------------------------------------------------- #
def median(values: list[float]) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2.0


def mad(values: list[float]) -> float:
    """Mediaan absolute afwijking; schaalvast gemaakt met 1,4826 = z-score."""
    if not values:
        return 0.0
    center = median(values)
    return median([abs(x - center) for x in values])


def robust_z(value: float, window: list[float]) -> float:
    if len(window) < 8:
        return 0.0
    center = median(window)
    spread = 1.4826 * mad(window)
    if spread <= 0:
        spread = 1e-9
    return (value - center) / spread


def pearson(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    if n < 3:
        return 0.0
    mx = sum(xs) / n
    my = sum(ys) / n
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    sy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if sx == 0 or sy == 0:
        return 0.0
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (sx * sy)


def returns(bars: list[dict]) -> list[float]:
    out = [0.0]
    for prev, cur in zip(bars, bars[1:]):
        out.append((cur["c"] - prev["c"]) / prev["c"] if prev["c"] else 0.0)
    return out


def ranges(bars: list[dict]) -> list[float]:
    return [max(bar["h"] - bar["l"], 0.0) for bar in bars]


# --------------------------------------------------------------------------- #
# Detectoren
# --------------------------------------------------------------------------- #
def d01_robust_volume_outlier(bars: list[dict], window: int = WEEK_15M) -> list[float]:
    """Robuuste z-score van volume tegen zijn eigen recente historie."""
    volumes = [bar["v"] for bar in bars]
    scores = []
    for i, value in enumerate(volumes):
        history = volumes[max(0, i - window):i]
        scores.append(robust_z(value, history))
    return scores


def d02_volume_per_movement(bars: list[dict], window: int = WEEK_15M) -> list[float]:
    """Volume per eenheid prijsrange (VR uit formules §4.2), als robuuste z."""
    logs = []
    for bar in bars:
        span = max(bar["h"] - bar["l"], 1e-12)
        logs.append(math.log(max(bar["v"], 1e-12) / span))
    scores = []
    for i, value in enumerate(logs):
        history = logs[max(0, i - window):i]
        scores.append(robust_z(value, history))
    return scores


def d03_price_volume_correlation(bars: list[dict], window: int = DAY_15M) -> list[float]:
    """Negatieve score = volume beweegt niet mee met de prijs."""
    rets = returns(bars)
    volumes = [bar["v"] for bar in bars]
    scores = []
    for i in range(len(bars)):
        if i < window:
            scores.append(0.0)
            continue
        xs = [abs(r) for r in rets[i - window:i]]
        ys = volumes[i - window:i]
        scores.append(-pearson(xs, ys))
    return scores


def d04_zero_volume(bars: list[dict], context: int = 8) -> list[float]:
    """Nul-volume met volume ervoor en erna: de discontinuiteit, niet het dunne uur."""
    volumes = [bar["v"] for bar in bars]
    scores = []
    for i, value in enumerate(volumes):
        if value > 0:
            scores.append(0.0)
            continue
        left = [v for v in volumes[max(0, i - context):i] if v > 0]
        right = [v for v in volumes[i + 1:i + 1 + context] if v > 0]
        scores.append(1.0 if left and right else 0.0)
    return scores


def d05_session_profile(bars: list[dict], lookback_days: int = 14) -> list[float]:
    """Tweezijdige afwijking van het uurprofiel: te veel én te weinig volume."""
    volumes = [bar["v"] for bar in bars]
    scores = []
    for i, value in enumerate(volumes):
        hour = (bars[i]["ts"] // 3600) % 24
        history = []
        for back in range(1, lookback_days + 1):
            j = i - back * DAY_15M
            if j < 0:
                break
            if (bars[j]["ts"] // 3600) % 24 == hour:
                history.append(volumes[j])
        if len(history) < 5:
            scores.append(0.0)
            continue
        scores.append(abs(robust_z(value, history)))
    return scores


def d06_event_without_range(bars: list[dict], calendar: list[int] | None = None,
                            half_window: int = 2, baseline: int = WEEK_15M) -> list[float]:
    """Volume rond een bekend event zonder dat de range meegroeit.

    De kalender komt van buiten en bevat ook tijdstippen zonder ingreep; anders
    zou de detector zijn eigen antwoord krijgen.
    """
    scores = [0.0] * len(bars)
    if not calendar:
        return scores
    index = {bar["ts"]: i for i, bar in enumerate(bars)}
    spans = ranges(bars)

    for stamp in calendar:
        i = index.get(stamp)
        if i is None:
            continue
        lo = max(0, i - half_window)
        hi = min(len(bars), i + half_window + 1)
        base_lo = max(0, lo - baseline)
        base = [bar["v"] for bar in bars[base_lo:lo]] or [bar["v"] for bar in bars[hi:hi + baseline]]
        if not base:
            continue
        base_volume = median(base)
        base_range = median(spans[base_lo:lo]) or median(spans) or 1e-12
        vi = (median([bar["v"] for bar in bars[lo:hi]]) / base_volume) if base_volume > 0 else 0.0
        re = median(spans[lo:hi]) / base_range if base_range > 0 else 1.0
        if vi > 3.0 and re < 1.5:
            for j in range(lo, hi):
                scores[j] = max(scores[j], vi)
    return scores


# --------------------------------------------------------------------------- #
# Register
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class Detector:
    code: str
    name: str
    fn: Callable[..., list[float]]
    threshold: float
    needs_calendar: bool = False


DETECTORS = {
    "D01": Detector("D01", "Robuuste volume-uitbijter", d01_robust_volume_outlier, 3.5),
    "D02": Detector("D02", "Volume per bewegingseenheid", d02_volume_per_movement, 3.5),
    "D03": Detector("D03", "Prijs-volume-correlatie", d03_price_volume_correlation, -0.1),
    "D04": Detector("D04", "Nul-volume en stale candles", d04_zero_volume, 0.5),
    "D05": Detector("D05", "Sessieprofiel-afwijking", d05_session_profile, 3.5),
    "D06": Detector("D06", "Volume zonder range rond event", d06_event_without_range, 0.5,
                    needs_calendar=True),
}


def run(code: str, bars: list[dict], calendar: list[int] | None = None):
    detector = DETECTORS[code]
    scores = (detector.fn(bars, calendar=calendar) if detector.needs_calendar
              else detector.fn(bars))
    flags = [score > detector.threshold for score in scores]
    return detector.name, scores, flags
