"""Independent polynomial and residue checks for FIGURATE WP09-003."""
import unittest
from research.figurate_wp09_mod25_global import (
    audit, image, polygonal, witness, obstructed_mod25_formula,
)


def direct_polygonal(k, t):
    return ((k - 2) * t * t - (k - 4) * t) // 2


def independent_witness(k, c, q):
    outputs = {direct_polygonal(k, t) % q for t in range(1, 2 * q + 1)}
    # Entire q^3 triple scan, independent of production pair prefilter.
    return next(((a, b, d) for a in range(q) for b in range(q)
                 for d in range(q)
                 if all(((x * y + c) % q) in outputs
                        for x, y in ((a, b), (a, d), (b, d)))), None)


class Mod25Tests(unittest.TestCase):
    def test_integer_formula(self):
        for k in range(3, 43):
            for t in range(1, 53):
                self.assertEqual(polygonal(k, t), direct_polygonal(k, t))

    def test_full_625_cell_classification(self):
        self.assertEqual(audit(), {"cells": 625, "excluded": 40, "admitted": 585})

    def test_independent_direct_oracle(self):
        for k in range(3, 28):
            for c in range(25):
                result = independent_witness(k, c, 25)
                self.assertEqual(result is None, obstructed_mod25_formula(k, c), (k, c))
                self.assertEqual((result is None), (witness(k, c, 25) is None))

    def test_full_mod5_nonobstruction(self):
        for k in range(3, 8):
            for c in range(5):
                self.assertIsNotNone(independent_witness(k, c, 5))

    def test_negative_offsets_and_order_lifting(self):
        for k in (3, 6, 8, 11, 18, 21, 33, 56):
            for c in (-1003, -997, -43, -22, 3, 8, 13, 23, 1003):
                self.assertEqual(witness(k, c, 25) is None,
                                 obstructed_mod25_formula(k, c))
                self.assertEqual(image(k, 25), image(k + 25, 25))
                self.assertEqual(witness(k, c, 25) is None,
                                 witness(k, c + 25, 25) is None)

    def test_no_distinct_residue_assumption(self):
        # 1, 26, 51 are distinct positive entries with same residue class.
        # A residue-level certificate must allow identical residue values.
        self.assertEqual(1 % 25, 26 % 25)
        self.assertEqual(26 % 25, 51 % 25)
        self.assertIsNone(witness(3, 8, 25))
        self.assertIsNotNone(witness(3, 3, 25))


if __name__ == "__main__":
    unittest.main()
