"""WP08: independent modulo-16 global triple-obstruction certificate tests."""
import itertools
import unittest

from research.figurate_census import polygonal, verify_tuple
from research.figurate_wp08_mod16_classification import (
    full_mod16_exclusions,
    local_certificate,
)


def independent_image(k, modulus):
    return {(((k - 2) * t * t - (k - 4) * t) // 2) % modulus
            for t in range(1, 5 * modulus + 1)}


def independent_nonempty(k, c, modulus=16):
    image = independent_image(k, modulus)
    for a, b, d in itertools.combinations_with_replacement(range(modulus), 3):
        if ((a*b+c) % modulus in image
                and (a*d+c) % modulus in image
                and (b*d+c) % modulus in image):
            return True
    return False


class GlobalMod16Obstructions(unittest.TestCase):
    def test_exact_complete_16_by_16_classification(self):
        expected = {r: () for r in range(16)}
        for r in (0, 8):
            expected[r] = (2, 3, 6, 10, 11, 14)
        expected[12] = (2, 6, 10, 14)
        self.assertEqual(full_mod16_exclusions(), expected)
        for k in range(3, 99):
            for c in range(16):
                self.assertEqual(not independent_nonempty(k, c),
                                 c in expected[k % 16], (k, c))

    def test_lift_positive_and_negative_offsets(self):
        for k in (8, 16, 24, 32, 40, 48):
            for c in (-13, -5, 3, 11, 19, -14, -10, -6, -2, 2, 6):
                cert = local_certificate(k, c)
                self.assertTrue(cert["global_exclusion_by_mod16"])
                self.assertEqual(cert["local_triples"], 0)
                self.assertIsNone(cert["first_local_triple"])

        for k in (12, 28, 44):
            for c in (-14, -10, -6, -2, 2, 6, 10, 14):
                self.assertTrue(local_certificate(k, c)[
                    "global_exclusion_by_mod16"])

    def test_actual_pairs_exist_but_no_triples(self):
        for k, c in ((8, 3), (16, 11), (24, -5),
                     (12, 2), (28, 6), (40, -13)):
            for t in (4, 7, 10):
                b = polygonal(k, t) - c
                if b > 1:
                    self.assertEqual(verify_tuple((1, b), "B", k, c),
                                     {f"1,{b}": t})
            for a, b, d in itertools.combinations(range(1, 38), 3):
                self.assertIsNone(verify_tuple((a, b, d), "B", k, c))

    def test_mod8_only_would_miss_new_cases(self):
        from research.figurate_wp08_global_mod8 import local_triples
        for k, c in ((8, 3), (16, 11), (12, 2)):
            self.assertTrue(local_triples(k, c, 8))
            self.assertFalse(independent_nonempty(k, c, 16))

    def test_local_nonempty_is_not_integer_existence(self):
        for k, c in ((3, 1), (8, 1), (12, 0), (4, 2)):
            self.assertFalse(local_certificate(k, c)[
                "global_exclusion_by_mod16"])


if __name__ == "__main__":
    unittest.main()
