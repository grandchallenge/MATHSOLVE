"""FIGURATE WP05: constructive no-go for unrestricted Type B pair exclusions.

Proof is in work_packages/FIGURATE_WP05_SOURCE_FIDELITY_001.md.
These tests exercise the construction, not its infinitude proof.
"""
import unittest
from research.figurate_census import polygonal, verify_tuple


class UnrestrictedTypeBPairsTests(unittest.TestCase):
    def test_constructive_pairs_for_orders_and_signed_offsets(self):
        for k in range(3, 13):
            for c in range(-100, 101, 13):
                last = None
                for t in range(40, 51):
                    b = polygonal(k, t) - c
                    self.assertGreater(b, 1)
                    if last is not None:
                        self.assertGreater(b, last)
                    self.assertEqual(verify_tuple((1, b), "B", k, c),
                                     {"1," + str(b): t})
                    last = b

    def test_type_a_and_b_not_interchangeable(self):
        # Triangular-entry D(n) restrictions never transfer to B by name.
        # For k=3 and c=2, this B-pair exists even though known
        # all-triangular Type A D(2) pairs are excluded modulo 9.
        self.assertIsNotNone(verify_tuple((1, 4), "B", 3, 2))
        self.assertIsNone(verify_tuple((1, 4), "A", 3, 2))


if __name__ == "__main__":
    unittest.main()
