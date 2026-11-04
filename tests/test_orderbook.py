"""Tests voor het orderboek en de volgnummer-machine in scripts/orderbook.py.

Geen netwerk: alle scenario's zijn nagespeelde berichten. De lastige gevallen zijn
de eerste diff na een snapshot (die mag overlappen) en een sprong in het
volgnummer (die moet tot een herbouw leiden, nooit tot stil doorwerken).
"""

import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import orderbook  # noqa: E402


def binance_depth(first, last, bids=(), asks=()):
    return {"venue": "binance", "first_update_id": first, "final_update_id": last,
            "bids": list(bids), "asks": list(asks)}


def bybit_depth(uid, bids=(), asks=(), kind="delta"):
    return {"venue": "bybit", "type": kind, "update_id": uid,
            "bids": list(bids), "asks": list(asks)}


class TestBook(unittest.TestCase):
    def test_nieuw_level_verschijnt(self):
        b = orderbook.Book()
        b.apply([["100.0", "1.5"]], [["101.0", "2.0"]])
        self.assertEqual(b.best_bid(), Decimal("100.0"))
        self.assertEqual(b.best_ask(), Decimal("101.0"))

    def test_hoeveelheid_nul_verwijdert_het_level(self):
        b = orderbook.Book()
        b.apply([["100.0", "1.5"], ["99.0", "1.0"]], [])
        b.apply([["100.0", "0"]], [])
        self.assertEqual(b.best_bid(), Decimal("99.0"))
        self.assertEqual(b.levels_removed, 1)

    def test_best_bid_is_de_hoogste_prijs(self):
        b = orderbook.Book()
        b.apply([["100.0", "1"], ["102.0", "1"], ["101.0", "1"]], [])
        self.assertEqual(b.best_bid(), Decimal("102.0"))

    def test_best_ask_is_de_laagste_prijs(self):
        b = orderbook.Book()
        b.apply([], [["105.0", "1"], ["103.0", "1"], ["104.0", "1"]])
        self.assertEqual(b.best_ask(), Decimal("103.0"))

    def test_gekruist_boek_wordt_geteld(self):
        b = orderbook.Book()
        b.apply([["100.0", "1"]], [["101.0", "1"]])
        self.assertFalse(b.is_crossed())
        b.apply([["102.0", "1"]], [])
        self.assertTrue(b.is_crossed())
        self.assertEqual(b.crossed_events, 1)

    def test_replace_gooit_oude_levels_weg(self):
        b = orderbook.Book()
        b.apply([["100.0", "1"]], [["101.0", "1"]])
        b.replace([["200.0", "1"]], [["201.0", "1"]])
        self.assertEqual(b.bids, {Decimal("200.0"): Decimal("1")})

    def test_spread_in_basispunten(self):
        b = orderbook.Book()
        b.apply([["100.00", "1"]], [["100.10", "1"]])
        self.assertAlmostEqual(b.spread_bps(), 9.99, delta=0.05)

    def test_lege_kant_geeft_geen_spread(self):
        self.assertIsNone(orderbook.Book().spread_bps())


class TestBinanceSequencer(unittest.TestCase):
    def maak(self, last_update_id=100):
        book = orderbook.Book()
        seq = orderbook.Sequencer("binance", book)
        seq.load_snapshot(last_update_id, [["100.0", "1"]], [["101.0", "1"]])
        return book, seq

    def test_eerste_event_mag_de_snapshot_overbruggen(self):
        # U <= lastUpdateId + 1 <= u is geen gat maar aansluiting.
        _, seq = self.maak(100)
        self.assertEqual(seq.feed(binance_depth(95, 105)), "toegepast")
        self.assertEqual(seq.last_update_id, 105)

    def test_daarna_moet_het_aansluiten(self):
        _, seq = self.maak(100)
        seq.feed(binance_depth(95, 105))
        self.assertEqual(seq.feed(binance_depth(106, 110)), "toegepast")
        self.assertEqual(seq.last_update_id, 110)

    def test_event_uit_de_snapshot_wordt_weggegooid(self):
        _, seq = self.maak(100)
        self.assertEqual(seq.feed(binance_depth(90, 100)), "weggegooid")

    def test_sprong_in_volgnummer_geeft_resync(self):
        _, seq = self.maak(100)
        seq.feed(binance_depth(95, 105))
        self.assertEqual(seq.feed(binance_depth(120, 130)), "resync")
        self.assertEqual(seq.resyncs, 1)
        self.assertIsNone(seq.last_update_id)

    def test_na_resync_wordt_niets_meer_toegepast(self):
        _, seq = self.maak(100)
        seq.feed(binance_depth(120, 130))
        self.assertEqual(seq.feed(binance_depth(131, 140)), "niet_gesynchroniseerd")

    def test_niveau_wordt_echt_toegepast(self):
        book, seq = self.maak(100)
        seq.feed(binance_depth(101, 101, bids=[["100.5", "3"]], asks=[]))
        self.assertEqual(book.best_bid(), Decimal("100.5"))


class TestBybitSequencer(unittest.TestCase):
    def maak(self, uid=500):
        book = orderbook.Book()
        seq = orderbook.Sequencer("bybit", book)
        seq.load_snapshot(uid, [["100.0", "1"]], [["101.0", "1"]])
        return book, seq

    def test_opeenvolgende_delta_wordt_toegepast(self):
        _, seq = self.maak(500)
        self.assertEqual(seq.feed(bybit_depth(501, bids=[["100.2", "1"]])), "toegepast")
        self.assertEqual(seq.last_update_id, 501)

    def test_dubbele_delta_wordt_weggegooid(self):
        _, seq = self.maak(500)
        seq.feed(bybit_depth(501))
        self.assertEqual(seq.feed(bybit_depth(501)), "weggegooid")

    def test_sprong_geeft_resync(self):
        _, seq = self.maak(500)
        self.assertEqual(seq.feed(bybit_depth(503)), "resync")
        self.assertEqual(seq.resyncs, 1)

    def test_websocket_snapshot_herzet_het_boek(self):
        book, seq = self.maak(500)
        seq.feed(bybit_depth(501, bids=[["99.0", "5"]]))
        outcome = seq.feed(bybit_depth(700, bids=[["50.0", "1"]], asks=[["51.0", "1"]], kind="snapshot"))
        self.assertEqual(outcome, "snapshot")
        self.assertEqual(seq.last_update_id, 700)
        self.assertEqual(book.best_bid(), Decimal("50.0"))
        self.assertNotIn(Decimal("99.0"), book.bids)


class TestTopbookRecord(unittest.TestCase):
    def maak(self):
        b = orderbook.Book()
        b.apply([["100.0", "1.5"], ["99.0", "2"]], [["101.0", "3"], ["102.0", "4"]])
        return b

    def test_bevat_top_of_book_en_tien_niveaus(self):
        rec = orderbook.topbook_record(self.maak(), 4711, "binance", 1_700_000_000_000)
        self.assertEqual(rec["best_bid"], "100.0")
        self.assertEqual(rec["best_bid_qty"], "1.5")
        self.assertEqual(rec["best_ask"], "101.0")
        self.assertEqual(rec["update_id"], 4711)
        self.assertEqual(rec["pair"], "BTC/USDT")
        self.assertEqual(rec["levels_bid"], 2)
        self.assertEqual(rec["gekruist"], False)
        self.assertEqual(rec["bids"][0], ["100.0", "1.5"])

    def test_hoeveelheden_blijven_strings(self):
        rec = orderbook.topbook_record(self.maak(), 1, "bybit", 0)
        self.assertIsInstance(rec["best_bid"], str)
        self.assertIsInstance(rec["bids"][0][1], str)

    def test_leeg_boek_geeft_nullen_in_plaats_van_een_fout(self):
        rec = orderbook.topbook_record(orderbook.Book(), None, "binance", 0)
        self.assertIsNone(rec["best_bid"])
        self.assertIsNone(rec["spread_bps"])
        self.assertEqual(rec["bids"], [])


if __name__ == "__main__":
    unittest.main()
