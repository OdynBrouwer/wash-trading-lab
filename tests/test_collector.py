"""Tests voor de parsers van scripts/collector.py.

Deze tests praten niet met het netwerk: ze voeren echte berichtvormen door de parsers
en controleren of het resultaat klopt. De berichtvormen komen uit de documentatie van
Binance en Bybit, en uit wat de collector tijdens een testrun daadwerkelijk ontving.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import collector  # noqa: E402

parse_binance = collector.parse_binance
parse_bybit = collector.parse_bybit
seq_of = collector.seq_of
to_ms = collector.to_ms


class TestTimestamps(unittest.TestCase):
    def test_milliseconden_blijven_milliseconden(self):
        # Wat Binance in november 2026 via de live @trade-stream stuurt.
        self.assertEqual(to_ms(1793713559612), (1793713559612, "ms"))

    def test_microseconden_worden_omgerekend(self):
        self.assertEqual(to_ms(1793713559612000), (1793713559612, "us"))

    def test_nanoseconden_worden_omgerekend(self):
        self.assertEqual(to_ms(1793713559612000000), (1793713559612, "ns"))

    def test_seconden_worden_omgerekend(self):
        self.assertEqual(to_ms(1793713559), (1793713559000, "s"))


class TestBinance(unittest.TestCase):
    TRADE = {
        "stream": "btcusdt@trade",
        "data": {
            "e": "trade", "E": 1793713559612, "s": "BTCUSDT", "t": 6814987182,
            "p": "77682.01000000", "q": "0.00031000", "T": 1793713559612,
            "m": True,
        },
    }

    def test_trade_met_maker_aan_koperskant_geeft_een_verkopende_agressor(self):
        stream, records = parse_binance(self.TRADE)
        self.assertEqual(stream, "trade")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["aggressor"], "SELL")

    def test_maker_aan_verkoperskant_geeft_een_kopende_agressor(self):
        payload = {"stream": "btcusdt@trade", "data": dict(self.TRADE["data"], m=False)}
        _, records = parse_binance(payload)
        self.assertEqual(records[0]["aggressor"], "BUY")

    def test_diepte_bericht_bewaart_beide_volgnummers(self):
        payload = {
            "stream": "btcusdt@depth@100ms",
            "data": {"e": "depthUpdate", "E": 1793713559612, "U": 100, "u": 105,
                     "b": [["1", "2"]], "a": []},
        }
        stream, records = parse_binance(payload)
        self.assertEqual(stream, "depth")
        self.assertEqual(seq_of("binance", records[0]), (100, 105))

    def test_onbekend_bericht_geeft_niets(self):
        self.assertIsNone(parse_binance({"stream": "x", "data": {"e": "kline"}}))


class TestBybit(unittest.TestCase):
    TRADE = {
        "topic": "publicTrade.BTCUSDT",
        "type": "snapshot",
        "ts": 1793713619839,
        "data": [
            {"T": 1793713619839, "s": "BTCUSDT", "S": "Sell", "v": "0.00163",
             "p": "77627.7", "i": "2290000001253869370"},
            {"T": 1793713619840, "s": "BTCUSDT", "S": "Buy", "v": "0.00200",
             "p": "77628.0", "i": "2290000001253869371"},
        ],
    }

    def test_meerdere_trades_in_een_bericht_gaan_er_allemaal_uit(self):
        stream, records = parse_bybit(self.TRADE)
        self.assertEqual(stream, "trade")
        self.assertEqual(len(records), 2)

    def test_agressor_wordt_genormaliseerd_maar_ruw_bewaard(self):
        _, records = parse_bybit(self.TRADE)
        self.assertEqual(records[0]["aggressor"], "SELL")
        self.assertEqual(records[0]["aggressor_raw"], "Sell")
        self.assertEqual(records[1]["aggressor"], "BUY")

    def test_lege_data_array_geeft_geen_trades(self):
        _, records = parse_bybit(dict(self.TRADE, data=[]))
        self.assertEqual(records, [])

    def test_orderbook_gebruikt_het_update_id_als_volgnummer(self):
        payload = {
            "topic": "orderbook.50.BTCUSDT", "type": "delta", "ts": 1793713619839,
            "data": {"s": "BTCUSDT", "u": 4711, "seq": 99, "b": [], "a": []},
        }
        stream, records = parse_bybit(payload)
        self.assertEqual(stream, "depth")
        self.assertEqual(seq_of("bybit", records[0]), (4711, 4711))

    def test_ping_reactie_geeft_niets(self):
        self.assertIsNone(parse_bybit({"op": "pong", "success": True}))


if __name__ == "__main__":
    unittest.main()
