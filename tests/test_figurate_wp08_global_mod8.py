"""Independent tests of the global Type B modular triple obstruction."""
import itertools
import unittest

from research.figurate_census import polygonal, verify_tuple
from research.figurate_wp08_global_mod8 import (
    exclusions, local_triples, mod8_classification, polygonal_image,
)


def independent_residues(k, m):
    return {((k - 2) * t * t - (k - 4) * t) // 2 % m
            for t in range(1, 5 * m + 1)}


def independent_local_triples(k, c, m):
    image = independent_residues(k, m)
    return tuple(x for x in itertools.combinations_with_replacement(
        range(m), 3) if all((x[i]*x[j]+c) % m in image
                           for i, j in ((0,1),(0,2),(1,2))))


class GlobalMod8ObstructionTests(unittest.TestCase):
    def test_complete_mod8_classification(self):
        self.assertEqual(exclusions(), {
            0: (2, 6), 1: (), 2: (), 3: (),
            4: (), 5: (), 6: (), 7: ()
        })
        table = mod8_classification()
        self.assertEqual(len(table), 8)
        for k in range(3, 131):
            for c in range(-18, 19):
                got = local_triples(k, c)
                self.assertEqual(got, independent_local_triples(k, c, 8),
                                 (k, c))
                self.assertEqual(bool(got),
                                 not (k % 8 == 0 and c % 8 in (2, 6)))

    def test_modular_period_and_repeated_classes(self):
        for m in (3, 4, 5, 7, 8, 9, 12, 16):
            for k in range(3, 3 + 2*m):
                self.assertEqual(set(polygonal_image(k, m)),
                                 independent_residues(k, m))
                for c in range(m):
                    expected = independent_local_triples(k, c, m)
                    self.assertEqual(local_triples(k, c, m), expected)
                    self.assertEqual(
                        local_triples(k + m, c, m), expected)

    def test_positive_compatible_pairs_still_exist(self):
        # This theorem is about triples, not pairs. Verify actual unbounded
        # compatible pair construction at several k/c and t choices.
        for k in (8, 16, 24, 40):
            for c in (-14, -10, -6, -2, 2, 6, 10, 14):
                self.assertEqual(local_triples(k, c), ())
                for t in (3, 4, 7, 15, 30, 60):
                    b = polygonal(k, t) - c
                    if b > 1:
                        self.assertEqual(
                            verify_tuple((1, b), "B", k, c),
                            {f"1,{b}": t})

    def test_exact_finite_adversarial_search(self):
        for k in (8, 16, 24):
            for c in (-6, -2, 2, 6, 10):
                for a, b, d in itertools.combinations(range(1, 38), 3):
                    self.assertIsNone(verify_tuple((a, b, d), "B", k, c),
                                      (k, c, a, b, d))

    def test_no_claim_for_other_offsets_or_orders(self):
        # Nonempty local classes do not prove any exact triple exists.
        for k, c in ((3, 2), (4, 2), (8, 1), (8, 0), (16, 3)):
            self.assertTrue(local_triples(k, c, 8))
        # Known exact Type B triangular triples are not erroneously excluded.
        self.assertIsNotNone(verify_tuple((1, 2, 27), "B", 3, 1))


if __name__ == "__main__":
    unittest.main()
