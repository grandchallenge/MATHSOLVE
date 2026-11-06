"""Independent direct-polynomial and Pell-orbit verification for WP09-018."""
import unittest
from math import isqrt
from research.figurate_wp09_exact_seed_018 import (
    A, B, C, K, L, NORM, PELL_D, R, UNIT_U, UNIT_V,
    AMPLIFICATION_MODULUS, BASE_S, BASE_X, SEED_STEPS,
    construct_seed, construct_next_family_member, pell_multiply,
    unit_order_mod, polygonal,
)


def independent_polygonal(k, n):
    return n + (k - 2) * n * (n - 1) // 2


def independent_replay():
    x, y = BASE_X, BASE_S
    for _ in range(SEED_STEPS):
        x, y = UNIT_U * x + PELL_D * UNIT_V * y, UNIT_V * x + UNIT_U * y
    s = (y + (K - 4)) // (2 * (K - 2))
    t = (x // A + (K - 4)) // (2 * (K - 2))
    d = (independent_polygonal(K, s) - C) // A
    return x, y, s, t, d


class Exact84GonalSeedTests(unittest.TestCase):
    def test_base_norm_and_norm_one_unit(self):
        delta = 8 * (K - 2) * C + (K - 4) ** 2
        self.assertEqual(BASE_X**2 - PELL_D * BASE_S**2,
                         A * (A - B) * delta)
        self.assertEqual(UNIT_U**2 - PELL_D * UNIT_V**2, 1)
        self.assertEqual(NORM, -601536)

    def test_exact_seed_against_independent_polynomial(self):
        result = construct_seed()
        x, y, s, t, d = independent_replay()
        self.assertEqual(result["entries"], (2, 41, d))
        self.assertEqual(result["indices"], (2, s, t))
        self.assertEqual(d, 172124700980346120000589924527450935999)
        self.assertEqual(s, 2897641606046209200)
        self.assertEqual(t, 13119630367519738931)
        self.assertEqual((x, y), result["pell_coordinates"])
        self.assertEqual(
            (2 * 41 + 2, 2 * d + 2, 41 * d + 2),
            tuple(independent_polygonal(K, n) for n in (2, s, t)),
        )
        self.assertEqual(len({2, 41, d}), 3)

    def test_index_lattice_and_norm(self):
        result = construct_seed()
        x, y = result["pell_coordinates"]
        self.assertEqual(y % R, (-L) % R)
        self.assertEqual(x % (A * R), (-A * L) % (A * R))
        self.assertEqual(x * x - PELL_D * y * y, NORM)
        self.assertEqual((y + L) // R, result["indices"][1])
        self.assertEqual((x // A + L) // R, result["indices"][2])

    def test_exact_pell_amplification(self):
        result = construct_seed()
        following = construct_next_family_member()
        self.assertEqual(AMPLIFICATION_MODULUS, 656)
        self.assertEqual(following["amplification_unit_exponent"], 328)
        self.assertGreater(following["entries"][2], result["entries"][2])
        a, b, d = following["entries"]
        r, s, t = following["indices"]
        self.assertEqual(
            (a*b+C, a*d+C, b*d+C),
            tuple(independent_polygonal(K, n) for n in (r, s, t)),
        )
        self.assertEqual(following["pell_coordinates"][0]**2
                         - PELL_D*following["pell_coordinates"][1]**2, NORM)
        self.assertEqual(len(str(d)), 1687)

    def test_modular_unit_order_is_minimal(self):
        self.assertEqual(unit_order_mod(P, UNIT_U, UNIT_V,
                                        AMPLIFICATION_MODULUS), 328)
        x, y = 1, 0
        for exponent in range(1, 328):
            x, y = pell_multiply(P, x, y, UNIT_U, UNIT_V)
            self.assertNotEqual((x % 656, y % 656), (1, 0))
        x, y = pell_multiply(P, x, y, UNIT_U, UNIT_V)
        self.assertEqual((x % 656, y % 656), (1, 0))

    def test_seed_exceeds_previous_entry_census(self):
        d = construct_seed()["entries"][2]
        self.assertGreater(d, 300000)
        self.assertEqual(len(str(d)), 39)

    def test_domain_guards(self):
        with self.assertRaises(ValueError):
            polygonal(2, 3)
        with self.assertRaises(ValueError):
            unit_order_mod(82, 163, 17, 656)


if __name__ == "__main__":
    unittest.main()
