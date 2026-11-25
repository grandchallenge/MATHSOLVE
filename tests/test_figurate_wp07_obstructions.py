"""WP07: independently exercise uniform congruence proofs and exact witnesses."""
import itertools
import unittest

from research.figurate_census import polygonal, polygonal_index, verify_tuple
from research.figurate_wp07_obstructions import (
    certificate, pair_extension_residues, polygonal_residues,
    type_c_pair_residue_witnesses,
)


def independent_image(k: int, m: int) -> set[int]:
    return {(((k - 2) * t * t - (k - 4) * t) // 2) % m
            for t in range(1, 8 * m + 1)}


def independent_candidates(k: int, c: int, a: int, b: int,
                           m: int, kind: str) -> set[int]:
    image = independent_image(k, m)
    return {d for d in range(m)
            if (a * d + c) % m in image
            and (b * d + c) % m in image
            and (kind == "B" or d in image)}


class WP07ResidueObstructions(unittest.TestCase):
    def test_uniform_type_c_and_a_no_pairs(self):
        # For all k=0 mod 4, P_k(t) is 0 or 1 modulo 4.
        for k in range(4, 65, 4):
            self.assertEqual(set(polygonal_residues(k, 4)), {0, 1})
            for c in (-14, -10, -6, -2, 2, 6, 10, 14):
                self.assertEqual(type_c_pair_residue_witnesses(k, c, 4), ())
                for a, b in itertools.combinations(
                        [polygonal(k, t) for t in range(1, 15)], 2):
                    self.assertIsNone(verify_tuple((a, b), "A", k, c))
                    self.assertIsNone(verify_tuple((a, b), "C", k, c))

    def test_octagonal_c2_pair_family_is_not_extendible(self):
        self.assertEqual(polygonal_residues(8, 8), (0, 1, 5))
        for c in (-14, -6, 2, 10, 18):
            for t in (2, 18, 34):
                b = polygonal(8, t) - c
                if b <= 1:
                    continue
                self.assertEqual(b % 8, 6)
                self.assertEqual(verify_tuple((1, b), "B", 8, c),
                                 {"1," + str(b): t})
                self.assertEqual(pair_extension_residues(
                    8, c, 1, b, 8), ())
                for d in range(1, 301):
                    if d not in (1, b):
                        self.assertIsNone(verify_tuple((1, b, d), "B", 8, c))

    def test_octagonal_c3_pair_family_is_not_extendible(self):
        self.assertEqual(polygonal_residues(8, 16), (0, 1, 5, 8))
        for c in (-29, -13, 3, 19, 35):
            for t in (2, 34, 66):
                b = polygonal(8, t) - c
                if b <= 1:
                    continue
                self.assertEqual(b % 16, 5)
                self.assertEqual(verify_tuple((1, b), "B", 8, c),
                                 {"1," + str(b): t})
                self.assertEqual(pair_extension_residues(
                    8, c, 1, b, 16), ())
                for d in range(1, 301):
                    if d not in (1, b):
                        self.assertIsNone(verify_tuple((1, b, d), "B", 8, c))

    def test_independent_exhaustive_modular_certificate(self):
        for k in range(3, 11):
            for m in (4, 8, 9, 16, 25):
                self.assertEqual(set(polygonal_residues(k, m)),
                                 independent_image(k, m))
                for c in (-1, 0, 1, 2, 3):
                    expected = {(x, y) for x in independent_image(k, m)
                                for y in independent_image(k, m)
                                if (x * y + c) % m in independent_image(k, m)}
                    self.assertEqual(set(type_c_pair_residue_witnesses(
                        k, c, m)), expected)
                    for a, b in ((1, 2), (1, 5), (2, 6)):
                        for kind in ("B", "C"):
                            self.assertEqual(set(pair_extension_residues(
                                k, c, a, b, m, kind)),
                                independent_candidates(k, c, a, b, m, kind))

    def test_nonempty_local_filter_is_not_sufficiency(self):
        # A compatible local residue is not necessarily a valid integer edge.
        self.assertIsNotNone(polygonal_index(8, 8))
        self.assertFalse(
            type_c_pair_residue_witnesses(8, 0, 4) == ())
        self.assertIsNone(polygonal_index(8, 2))
        self.assertEqual(certificate(8, 2, 8, 1, 6)["extension_residues"], [])
        self.assertEqual(certificate(8, 3, 16, 1, 5)["extension_residues"], [])


if __name__ == "__main__":
    unittest.main()
