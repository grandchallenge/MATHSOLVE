"""WP08: independent complete order/offset classification, and order lifting."""
import unittest

from research.figurate_census import polygonal, verify_tuple
from research.figurate_wp07_obstructions import pair_extension_residues
from research.figurate_wp08_mod8_classification import (
    anchored_obstruction_classes, modulus_eight_classifier,
    nonempty_obstruction_classes,
)


def independent_residues(k, m):
    # Direct polynomial, no use of the WP07 residue implementation.
    return {((k - 2) * t * t - (k - 4) * t) // 2 % m
            for t in range(1, 4 * m + 1)}


def independent_classification(k, m):
    image = independent_residues(k, m)
    output = {}
    for c in range(m):
        bad = []
        for b in range(m):
            if (b + c) % m not in image:
                continue
            if not any((d + c) % m in image and
                       (b * d + c) % m in image for d in range(m)):
                bad.append(b)
        if bad:
            output[c] = tuple(bad)
    return output


class FigurateWP08OrderClassification(unittest.TestCase):
    def test_complete_modulus_eight_classification(self):
        expected = {
            0: {2: (3, 6, 7), 6: (2, 3, 7)},
            1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {},
        }
        self.assertEqual(modulus_eight_classifier(), expected)
        for k in range(3, 100):
            self.assertEqual(nonempty_obstruction_classes(k, 8),
                             expected[k % 8])
            self.assertEqual(nonempty_obstruction_classes(k, 8),
                             independent_classification(k, 8))

    def test_all_moduli_independent_exhaustive(self):
        for m in (3, 4, 5, 8, 9, 12, 16):
            for k in range(3, 3 + 2 * m):
                expected = independent_classification(k, m)
                self.assertEqual(nonempty_obstruction_classes(k, m),
                                 expected, (k, m))
                self.assertEqual(
                    nonempty_obstruction_classes(k + m, m), expected)

    def test_compatible_nonextendible_infinite_family_representatives(self):
        for k in (8, 16, 24, 32, 40):
            for c in (-14, -6, 2, 10, 18, -10, -2, 6, 14, 22):
                # k divisible by 8; c modulo 8 is 2 or 6.
                for t in (2, 18, 34, 50):
                    b = polygonal(k, t) - c
                    if b <= 1:
                        continue
                    self.assertEqual(verify_tuple((1, b), "B", k, c),
                                     {"1," + str(b): t})
                    self.assertEqual(
                        pair_extension_residues(k, c, 1, b, 8), ())
                    for d in range(2, 100):
                        if d != b:
                            self.assertIsNone(
                                verify_tuple((1, b, d), "B", k, c))

    def test_modulus_sixteen_family_order_lift(self):
        for k in (8, 24, 40, 56):
            for c in (-29, -13, 3, 19, 35):
                for t in (2, 34, 66):
                    b = polygonal(k, t) - c
                    if b <= 1:
                        continue
                    self.assertEqual(b % 16, 5)
                    self.assertEqual(verify_tuple((1, b), "B", k, c),
                                     {"1," + str(b): t})
                    self.assertEqual(pair_extension_residues(
                        k, c, 1, b, 16), ())

    def test_necessary_not_sufficient(self):
        # No residue-class obstruction does not prove an integer triple exists.
        self.assertEqual(nonempty_obstruction_classes(3, 8), {})
        self.assertEqual(anchored_obstruction_classes(3, 8)[1], ())


if __name__ == "__main__":
    unittest.main()
