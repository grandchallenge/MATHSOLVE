"""Independent FIGURATE WP08 modulo-64 and binary-lifting validation."""
import unittest

from research.figurate_census import polygonal, verify_tuple
from research.figurate_wp08_2adic import (
    canonical_sha256, complete_table, exclusions, lift_polygonal_index,
    local_first_triple, newly_excluded_from_32, polygonal_image,
)


def independent_image(k, m):
    return {(((k - 2) * t * t - (k - 4) * t) // 2) % m
            for t in range(1, 3 * m + 1)}


def independent_first(k, c, m):
    """Independent set-valued graph construction, no integer bitsets."""
    im = independent_image(k, m)
    neighbors = [
        {b for b in range(m) if (a * b + c) % m in im}
        for a in range(m)
    ]
    for a in range(m):
        for b in sorted(neighbors[a]):
            if b < a:
                continue
            choices = neighbors[a] & neighbors[b]
            candidates = [d for d in choices if d >= b]
            if candidates:
                return a, b, min(candidates)
    return None


def expected_old_plus_new():
    from research.figurate_wp08_mod32 import exclusions as old_exclusions
    prior = old_exclusions(32)
    out = {}
    for k in range(64):
        cells = []
        for c in range(64):
            old = (c % 32 in prior[k % 32])
            new = (
                (k % 32 == 0 and c % 32 == 9)
                or (k % 32 == 16 and c % 32 == 25)
                or (k % 16 == 8 and c % 32 == 13)
                or (k % 16 == 12 and c % 16 == 4)
            )
            if old or new:
                cells.append(c)
        out[k] = tuple(cells)
    return out


class FigurateWP08TwoAdic(unittest.TestCase):
    def test_constructive_binary_lifting_all_orders(self):
        for k in range(3, 80):
            if k % 4 == 0:
                for n in (2, 3, 5):
                    with self.assertRaises(ValueError):
                        lift_polygonal_index(k, 0, n)
                continue
            for exponent in range(1, 11):
                m = 1 << exponent
                targets = (0, 1, 2, 3, m//2, m-2, m-1, 113, 317)
                for c in targets:
                    t = lift_polygonal_index(k, c, exponent)
                    self.assertGreaterEqual(t, 1)
                    self.assertEqual(polygonal(k, t) % m, c % m)
                    self.assertLessEqual(t, 2 * m + 3)

    def test_iff_surjectivity_at_each_power_and_boundary(self):
        for m in (4, 8, 16, 32, 64, 128):
            for k in range(3, 70):
                image = independent_image(k, m)
                self.assertEqual(len(image) == m, k % 4 != 0, (k, m))
                self.assertEqual(set(polygonal_image(k, m)), image)
                if k % 4 == 0:
                    self.assertEqual({x % 4 for x in image}, {0, 1})

    def test_full_mod64_independent_table_and_first_witness(self):
        table = complete_table(64)
        expected = expected_old_plus_new()
        self.assertEqual(exclusions(64), expected)
        for k in range(64, 128):
            for c in range(64):
                self.assertEqual(table[k % 64][c],
                                 independent_first(k, c, 64), (k, c))
        self.assertEqual(canonical_sha256(64),
                         "1218764ff77c735d1fda1d27545c6fd6415b31d18ff377999eb082a808285264")

    def test_new_classes_are_strict_and_older_classes_persist(self):
        from research.figurate_wp08_mod32 import (
            exclusions as old_exclusions, first_local_witness
        )
        old = old_exclusions(32)
        full = expected_old_plus_new()
        actual = set(newly_excluded_from_32())
        expected = {(k, c) for k in range(64) for c in full[k]
                    if c % 32 not in old[k % 32]}
        self.assertEqual(actual, expected)
        for k, c in ((64, 9), (80, 25), (72, 13), (76, 4),
                     (96, 41), (120, 45), (124, 20)):
            self.assertIsNone(local_first_triple(k, c, 64))
            self.assertIsNotNone(first_local_witness(k, c, 32))

    def test_positive_pairs_remain_despite_global_triple_obstructions(self):
        for k, c in ((64, 9), (80, 25), (72, 13), (76, 4)):
            for t in (3, 5, 9):
                b = polygonal(k, t) - c
                if b > 1:
                    self.assertEqual(verify_tuple((1, b), "B", k, c),
                                     {f"1,{b}": t})

    def test_local_nonempty_not_actual_existence(self):
        for k, c in ((3, 1), (4, 2), (6, 7), (8, 1)):
            self.assertIsNotNone(local_first_triple(k, c, 64))


if __name__ == "__main__":
    unittest.main()
