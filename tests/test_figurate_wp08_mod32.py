"""Independent checks for WP08 full modulus-32 Type B triple classification."""
import itertools
import unittest

from research.figurate_census import polygonal, verify_tuple
from research.figurate_wp08_mod32 import (
    complete_table, exclusions, first_local_witness, polygonal_image,
    table_sha256,
)


def independent_image(k, m):
    # Derived directly from quadratic formula, not the production generator.
    return {
        (((k - 2) * t * t - (k - 4) * t) // 2) % m
        for t in range(1, 3 * m + 1)
    }


def independent_first(k, c, m):
    R = independent_image(k, m)
    ok = [
        [((a * b + c) % m in R) for b in range(m)]
        for a in range(m)
    ]
    for a in range(m):
        for b in range(a, m):
            if not ok[a][b]:
                continue
            for d in range(b, m):
                if ok[a][d] and ok[b][d]:
                    return (a, b, d)
    return None


def expected_mod32():
    result = {k: () for k in range(32)}
    result.update({
        0: (2, 3, 5, 6, 10, 11, 14, 18, 19, 21, 22, 26, 27, 30),
        16: (2, 3, 5, 6, 10, 11, 14, 18, 19, 21, 22, 26, 27, 30),
        8: (2, 3, 6, 9, 10, 11, 14, 18, 19, 22, 25, 26, 27, 30),
        24: (2, 3, 6, 9, 10, 11, 14, 18, 19, 22, 25, 26, 27, 30),
        12: (2, 6, 10, 14, 18, 22, 26, 30),
        28: (2, 6, 10, 14, 18, 22, 26, 30),
    })
    return result


class WP08Mod32Certificate(unittest.TestCase):
    def test_exact_full_32_by_32_table(self):
        self.assertEqual(exclusions(32), expected_mod32())
        table = complete_table(32)
        self.assertEqual(len(table), 32)
        for k in range(32, 64):
            for c in range(32):
                self.assertEqual(
                    table[k % 32][c],
                    independent_first(k, c, 32),
                    (k, c),
                )
        self.assertEqual(len(table_sha256(32)), 64)

    def test_order_periodicity_and_all_nonempty_cell_witnesses(self):
        for k in range(32, 64):
            self.assertEqual(polygonal_image(k, 32), polygonal_image(k + 32, 32))
            for c in range(32):
                witness = first_local_witness(k, c, 32)
                self.assertEqual(witness, first_local_witness(k + 32, c + 32, 32))
                if witness is not None:
                    image = independent_image(k, 32)
                    a, b, d = witness
                    self.assertTrue(all(
                        (x*y+c) % 32 in image
                        for x, y in ((a, b), (a, d), (b, d))
                    ))

    def test_strictly_new_congruence_families(self):
        from research.figurate_wp08_mod16_classification import local_certificate
        for k, c in ((16, 5), (32, 21), (48, -11),
                     (8, 9), (24, 25), (40, -7)):
            self.assertIsNotNone(local_certificate(k, c)["first_local_triple"])
            self.assertIsNone(first_local_witness(k, c, 32))
        # Boundary: no blanket exclusion of other residue classes.
        for k, c in ((16, 1), (24, 1), (8, 5), (12, 3), (3, 1)):
            self.assertIsNotNone(first_local_witness(k, c, 32))

    def test_actual_compatible_pairs_and_direct_counterexample_search(self):
        for k, c in ((16, 5), (32, 5), (48, -11), (8, 9), (24, -7)):
            for t in (3, 6, 12, 33):
                b = polygonal(k, t) - c
                if b > 1:
                    self.assertEqual(
                        verify_tuple((1, b), "B", k, c), {f"1,{b}": t}
                    )
            for a, b, d in itertools.combinations(range(1, 40), 3):
                self.assertIsNone(verify_tuple((a, b, d), "B", k, c))

    def test_mod32_contains_mod16_obstructions(self):
        from research.figurate_wp08_mod16_classification import full_mod16_exclusions
        lower = full_mod16_exclusions()
        upper = exclusions(32)
        for k in range(32):
            for c16 in lower[k % 16]:
                self.assertIn(c16, upper[k])
                self.assertIn(c16 + 16, upper[k])


if __name__ == "__main__":
    unittest.main()
