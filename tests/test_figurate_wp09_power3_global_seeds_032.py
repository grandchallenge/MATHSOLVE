"""Independent exact-arithmetic tests for the WP09-032 3-power anchor theorem."""

from math import isqrt
import unittest

from research import figurate_wp09_power3_global_seeds_032 as wp


def matrix_power_unit(n: int, modulus: int) -> tuple[int, int]:
    """Independent 2-by-2 matrix action on 1, not the producer ring-power code."""
    a, b, c, d = 3 % modulus, 4 % modulus, 2 % modulus, 3 % modulus
    x, y = 1, 0
    while n:
        if n & 1:
            x, y = (a*x+b*y) % modulus, (c*x+d*y) % modulus
        a, b, c, d = (
            (a*a+b*c) % modulus,
            (a*b+b*d) % modulus,
            (c*a+d*c) % modulus,
            (c*b+d*d) % modulus,
        )
        n //= 2
    return x, y


def independent_polygonal_index(A: int, target: int) -> int | None:
    """Invert A*t*(t-1)+t by a discriminant/square-root oracle."""
    if target < 1:
        return None
    discriminant = (A-1)**2+4*A*target
    root = isqrt(discriminant)
    if root*root != discriminant:
        return None
    numerator = (A-1)+root
    if numerator % (2*A):
        return None
    t = numerator//(2*A)
    return t if t > 0 else None


class ThreePowerRayTheoremTests(unittest.TestCase):
    def test_exact_norm_factorization_independent(self):
        for e in range(1, 9):
            f = 3**e
            A = f*f
            H = (A*A+6*A+1)//8
            x, y = (A+4*f+3)//2, (f**3+3*f+2)//2
            self.assertEqual(x*x-2*y*y, -2*(2*A-1)*H)
            self.assertEqual((A*A+6*A+1) % 8, 0)

    def test_unit_lifting_valutations_and_period(self):
        for e in range(1, 9):
            cert = wp.certificate(e)
            f, A, mod = cert.conductor, cert.A, cert.modulus
            scalar, radical = matrix_power_unit(cert.unit_lift_exponent, mod)
            self.assertEqual(scalar, 1)
            self.assertEqual(radical % A, 0)
            self.assertNotEqual((radical//A) % 3, 0)
            self.assertEqual(matrix_power_unit(cert.unit_period, mod), (1, 0))
            self.assertEqual(cert.unit_period, f*cert.unit_lift_exponent)

    def test_target_ray_direct_matrix_oracle(self):
        for e in range(1, 9):
            cert = wp.certificate(e)
            f, A, mod = cert.conductor, cert.A, cert.modulus
            x, y = cert.alpha
            ux, uy = matrix_power_unit(cert.constructive_exponent, mod)
            beta_x = (x*ux+2*y*uy) % mod
            beta_y = (x*uy+y*ux) % mod
            r = (A+1)//2
            self.assertEqual(beta_x % A, r % A)
            self.assertEqual(beta_y % mod, (f*r) % mod)
            self.assertEqual(cert.lift_coefficient*cert.correction_index % f, (-2) % f)
            self.assertGreaterEqual(cert.constructive_exponent, 0)
            self.assertLess(cert.constructive_exponent, cert.unit_period)

    def test_exact_type_b_seeds_without_producer_index_validator(self):
        for e in (1, 2):
            k, c, a, b, d = wp.positive_seed(e)
            A = 9**e
            self.assertEqual((k, c, a, b), (2*A+2, 2, 1, 2*A))
            self.assertEqual(len({a, b, d}), 3)
            self.assertTrue(all(z > 0 for z in (a, b, d)))
            indexes = [
                independent_polygonal_index(A, a*b+c),
                independent_polygonal_index(A, a*d+c),
                independent_polygonal_index(A, b*d+c),
            ]
            self.assertTrue(all(n is not None and n > 0 for n in indexes))
            self.assertEqual(indexes[0], 2)
            self.assertGreater(indexes[1], 2)

    def test_predecessor_base_case_and_new_large_cases(self):
        expected = {
            1: (3, 1, 23, 36),
            2: (9, 1, 863, 972),
            3: (27, 1, 25271, 26244),
            4: (81, 28, 463643, 708588),
            5: (243, 190, 4172795, 19131876),
        }
        for e, (f, j, exponent, period) in expected.items():
            cert = wp.certificate(e)
            self.assertEqual(
                (cert.conductor, cert.correction_index,
                 cert.constructive_exponent, cert.unit_period),
                (f, j, exponent, period),
            )

    def test_guard_never_returns_false_nonexistence(self):
        for invalid in (-2, 0, 1.1):
            with self.assertRaises(ValueError):
                wp.certificate(invalid)
        with self.assertRaises(RuntimeError):
            wp.positive_seed(3, max_unit_exponent=1000)
        with self.assertRaises(RuntimeError):
            wp.certificate(100, max_exponent_bits=4)
        with self.assertRaises(ValueError):
            wp.power((3, 2), -1)


if __name__ == "__main__":
    unittest.main()
