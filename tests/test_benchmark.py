"""Regressietests voor de injector en de T0-detectoren.

Draaien met:  python -m unittest discover -s tests -v

Deze tests bewaken twee dingen:
1. De injector is deterministisch -- hetzelfde zaadje geeft dezelfde reeks.
2. Elke detector doet wat de spec belooft, inclusief de detector die een
   injectie juist *niet* hoort te vangen.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import detectors_t0  # noqa: E402
import injector  # noqa: E402
import run_benchmark  # noqa: E402

DAYS = 20


def scores_for(scenario: str, code: str, seed: int = 7):
    bars, labels, calendar = injector.build(scenario, days=DAYS, seed=seed)
    _name, scores, flags = detectors_t0.run(code, bars, calendar)
    return scores, flags, labels


class TestInjector(unittest.TestCase):
    def test_deterministic(self):
        first = injector.build("volume_sticky", days=DAYS, seed=3)
        second = injector.build("volume_sticky", days=DAYS, seed=3)
        self.assertEqual(first[0], second[0])
        self.assertEqual(first[1], second[1])

    def test_seed_changes_result(self):
        first = injector.build("volume_sticky", days=DAYS, seed=3)
        second = injector.build("volume_sticky", days=DAYS, seed=4)
        self.assertNotEqual(first[0], second[0])

    def test_every_scenario_has_labels(self):
        for scenario in injector.SCENARIOS:
            with self.subTest(scenario=scenario):
                _bars, labels, _calendar = injector.build(scenario, days=DAYS)
                if scenario == "clean":
                    self.assertEqual(sum(labels), 0)
                else:
                    self.assertGreater(sum(labels), 0)

    def test_bar_count(self):
        bars, labels, _ = injector.build("clean", days=DAYS)
        self.assertEqual(len(bars), DAYS * 24 * 4)
        self.assertEqual(len(labels), len(bars))


class TestAuc(unittest.TestCase):
    def test_perfect_separation(self):
        self.assertEqual(run_benchmark.auc([0.0, 1.0], [False, True]), 1.0)

    def test_inverted_separation(self):
        self.assertEqual(run_benchmark.auc([1.0, 0.0], [False, True]), 0.0)

    def test_single_class_is_undefined(self):
        self.assertIsNone(run_benchmark.auc([1.0, 2.0], [False, False]))


class TestDetectors(unittest.TestCase):
    def test_d01_catches_sticky_volume(self):
        scores, _flags, labels = scores_for("volume_sticky", "D01")
        self.assertGreaterEqual(run_benchmark.auc(scores, labels), 0.80)

    def test_d04_catches_zero_gaps(self):
        _scores, flags, labels = scores_for("zero_gaps", "D04")
        confusion = run_benchmark.confusion(flags, labels)
        self.assertEqual(confusion["recall"], 1.0)

    def test_d04_is_silent_on_clean_data(self):
        _scores, flags, labels = scores_for("clean", "D04")
        self.assertEqual(sum(flags), 0)

    def test_d03_catches_anti_correlated_volume(self):
        scores, _flags, labels = scores_for("anti_correlated", "D03")
        self.assertGreaterEqual(run_benchmark.auc(scores, labels), 0.80)

    def test_d06_catches_event_spike(self):
        scores, _flags, labels = scores_for("event_spike", "D06")
        self.assertGreaterEqual(run_benchmark.auc(scores, labels), 0.80)

    def test_d06_ignores_spike_with_real_movement(self):
        """Controlegroep: veel volume MÉT beweging hoort D06 niet te pakken."""
        scores, _flags, labels = scores_for("volume_moved", "D06")
        self.assertLess(run_benchmark.auc(scores, labels), 0.80)

    def test_every_detector_returns_one_score_per_bar(self):
        bars, _labels, calendar = injector.build("event_spike", days=DAYS)
        for code in detectors_t0.DETECTORS:
            with self.subTest(detector=code):
                _name, scores, flags = detectors_t0.run(code, bars, calendar)
                self.assertEqual(len(scores), len(bars))
                self.assertEqual(len(flags), len(bars))


if __name__ == "__main__":
    unittest.main()
