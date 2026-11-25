"""FIGURATE WP06 modular prefilter: exhaustive safety and census regressions."""
import csv
import itertools
import unittest
from pathlib import Path

from research.figurate_census import census, polygonal
from research.figurate_residue_sieve import (
    allowed_residues, census_summary, exact_pair, local_possible,
)


class ResidueSieveTests(unittest.TestCase):
    def test_complete_polygonal_residue_period(self):
        for k in range(3, 13):
            for m in (2, 3, 5, 7, 8, 9, 11, 13):
                residues = allowed_residues("B", k, m)
                self.assertEqual(residues, frozenset(
                    polygonal(k, t) % m for t in range(1, 4 * m + 1)))
                for t in range(1, 2 * m + 1):
                    self.assertEqual(polygonal(k, t) % m,
                                     polygonal(k, t + 2 * m) % m)

    def test_no_false_rejection_in_sampled_full_edges(self):
        for kind in ("A", "B", "C"):
            for k in range(3, 13):
                domain = (range(1, 46) if kind == "B" else
                          [z for z in range(1, 46)
                           if z in {polygonal(k, t) for t in range(1, 46)}])
                for offset in (-2, -1, 0, 1, 2):
                    for a, b in itertools.combinations(domain, 2):
                        if exact_pair(a, b, kind, k, offset):
                            self.assertTrue(local_possible(a, b, kind, k, offset),
                                            (kind, k, offset, a, b))

    def test_full_archived_270_case_counts(self):
        path = Path(__file__).resolve().parents[1] / "research" / "figurate_census_2026_11_03_L60.csv"
        with path.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 270)
        for row in rows:
            summary = census_summary(row["kind"], int(row["k"]), int(row["offset"]),
                                     int(row["entry_limit"]), int(row["size"]))
            self.assertEqual(summary["count"], int(row["count"]), row)
            witness = (list(map(int, row["first_values"].split(";")))
                       if row["first_values"] else None)
            self.assertEqual(summary["first_values"], witness, row)
            self.assertEqual(summary["candidate_pairs"],
                             summary["residue_rejected"] + summary["exact_pair_checks"])

    def test_larger_examples_against_baseline(self):
        for kind, k, offset, limit, size in (
            ("B", 3, 1, 120, 3), ("B", 5, -1, 150, 3),
            ("B", 4, 1, 120, 4), ("A", 3, 1, 240, 3),
            ("C", 4, 0, 120, 4),
        ):
            expected = census(kind, k, offset, limit, size)
            observed = census_summary(kind, k, offset, limit, size)
            self.assertEqual(observed["count"], len(expected))
            self.assertEqual(observed["first_values"],
                             expected[0]["values"] if expected else None)

    def test_invalid_modulus_and_domain(self):
        with self.assertRaises(ValueError):
            allowed_residues("B", 3, 1)
        with self.assertRaises(ValueError):
            census_summary("B", 3, 1, 20, 3, (1,))


if __name__ == "__main__":
    unittest.main()
