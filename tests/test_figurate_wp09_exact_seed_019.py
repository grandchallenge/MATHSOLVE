"""Independent direct-polynomial and Pell-orbit verification for WP09-019."""
import unittest
from research.figurate_wp09_exact_seed_019 import (
    A, B, C, K, L, NORM, PELL_D, R, UNIT_U, UNIT_V,
    AMPLIFICATION_MODULUS, BASE_S, BASE_X, SEED_STEPS,
    construct_seed, construct_next_family_member, unit_order_mod,
)


def independent_polygonal(k, n):
    return n + (k - 2) * n * (n - 1) // 2


def independent_replay():
    x, y = BASE_X, BASE_S
    for _ in range(SEED_STEPS):
        x, y = UNIT_U*x + PELL_D*UNIT_V*y, UNIT_V*x + UNIT_U*y
    s = (y + (K - 4)) // (2 * (K - 2))
    t = (x // A + (K - 4)) // (2 * (K - 2))
    d = independent_polygonal(K, s) - C
    return x, y, s, t, d


class Exact100GonalSeedTests(unittest.TestCase):
    def test_base_norm_and_unit(self):
        delta = 8 * (K - 2) * C + (K - 4) ** 2
        self.assertEqual(BASE_X**2 - PELL_D*BASE_S**2,
                         A*(A-B)*delta)
        self.assertEqual(UNIT_U**2 - PELL_D*UNIT_V**2, 1)
        self.assertEqual(NORM, -1046048)

    def test_exact_seed_against_independent_polynomial(self):
        result = construct_seed()
        x, y, s, t, d = independent_replay()
        self.assertEqual(result["entries"], (1, 98, d))
        self.assertEqual(result["indices"], (2, s, t))
        self.assertEqual(d, 394141484570467638798107106734400805257750080265189167281283878325018383881627360745786897584655)
        self.assertEqual(s, 89686697824951931533091760698417159299075689513)
        self.assertEqual(t, 887853010999532105318395994347406981537890234904)
        self.assertEqual((x, y), result["pell_coordinates"])
        self.assertEqual(
            (1*98+C, d+C, 98*d+C),
            tuple(independent_polygonal(K, n) for n in (2, s, t)),
        )
        self.assertEqual(len({1, 98, d}), 3)

    def test_lattice_and_norm(self):
        result = construct_seed()
        x, y = result["pell_coordinates"]
        self.assertEqual(y % R, (-L) % R)
        self.assertEqual(x % (A*R), (-A*L) % (A*R))
        self.assertEqual(x*x - PELL_D*y*y, NORM)
        self.assertEqual((y+L)//R, result["indices"][1])
        self.assertEqual((x//A+L)//R, result["indices"][2])

    def test_exact_infinite_family_successor(self):
        seed = construct_seed()
        following = construct_next_family_member()
        self.assertEqual(AMPLIFICATION_MODULUS, 392)
        self.assertEqual(following["amplification_unit_exponent"], 196)
        self.assertGreater(following["entries"][2], seed["entries"][2])
        a,b,d = following["entries"]
        r,s,t = following["indices"]
        self.assertEqual(
            (a*b+C,a*d+C,b*d+C),
            tuple(independent_polygonal(K,n) for n in (r,s,t)),
        )
        x,y = following["pell_coordinates"]
        self.assertEqual(x*x-PELL_D*y*y,NORM)
        self.assertEqual(len(str(d)),996)

    def test_modular_order_is_minimal(self):
        self.assertEqual(unit_order_mod(PELL_D,UNIT_U,UNIT_V,
                                        AMPLIFICATION_MODULUS),196)
        x,y=1,0
        for exponent in range(1,196):
            x,y=UNIT_U*x+PELL_D*UNIT_V*y,UNIT_V*x+UNIT_U*y
            self.assertNotEqual((x%392,y%392),(1,0))
        x,y=UNIT_U*x+PELL_D*UNIT_V*y,UNIT_V*x+UNIT_U*y
        self.assertEqual((x%392,y%392),(1,0))

    def test_seed_beyond_300000(self):
        d=construct_seed()["entries"][2]
        self.assertGreater(d,300000)
        self.assertEqual(len(str(d)),96)

    def test_domain_guards(self):
        from research.figurate_wp09_exact_seed_019 import polygonal
        with self.assertRaises(ValueError):
            polygonal(2,3)
        with self.assertRaises(ValueError):
            unit_order_mod(98,99,9,392)


if __name__ == "__main__":
    unittest.main()
