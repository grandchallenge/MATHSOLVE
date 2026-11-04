"""FIGURATE WP06 L240 archive: exact source-driven reproduction."""
import csv
import hashlib
import unittest
from pathlib import Path
from research.figurate_wp06_panel import FIELDS, encode, panel_rows, validate


class FigurateWP06L240Archive(unittest.TestCase):
    def test_archive_complete_and_exact(self):
        path = Path(__file__).resolve().parents[1] / "research" / "figurate_wp06_L240_panel.csv"
        raw = path.read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),
                         "7d3be393be72d299fe0cf8a288284a35b23feb44dd61f1dcf4670cfd16422f43")
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.assertEqual(tuple(reader.fieldnames), FIELDS)
            saved = list(reader)
        computed = panel_rows(240)
        self.assertEqual(raw, encode(computed))
        self.assertEqual(len(saved), 54)
        validate(computed)

    def test_known_controls_are_not_claimed_novel(self):
        rows = panel_rows(240)
        def row(kind, k, offset, size):
            return next(x for x in rows if
                        (x["kind"], x["k"], x["offset"], x["size"])
                        == (kind, k, offset, size))
        self.assertEqual(row("B", 4, 1, 4)["first_values"], "1;3;8;120")
        self.assertEqual(row("B", 4, 1, 4)["count"], 1)
        self.assertEqual(row("B", 3, 1, 4)["count"], 0)
        self.assertEqual(row("A", 3, 1, 3)["first_values"], "1;3;120")


if __name__ == "__main__":
    unittest.main()
