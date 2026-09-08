import math
import unittest
from fractions import Fraction


class NSCIA2L5RestartTests(unittest.TestCase):
    def test_target_and_lambda_budget_are_critical(self) -> None:
        l6_norm = Fraction(1, 2)
        dt = Fraction(-2, 1)
        self.assertEqual(4 * l6_norm + dt, 0)
        self.assertEqual(2 * Fraction(1, 1) + dt, 0)

    def test_low_diagonal_and_off_diagonal_have_target_scaling(self) -> None:
        shell_enstrophy = Fraction(1, 1)
        self.assertEqual(2 * shell_enstrophy, Fraction(2, 1))

    def test_low_kernel_identity_and_row_sum(self) -> None:
        for r in range(0, 20):
            lambda_r = Fraction(2**r, 1)
            row_sum = Fraction(0, 1)
            for p in range(0, r + 1):
                lambda_p = Fraction(2**p, 1)
                ratio = Fraction(1, 4 ** (r - p))
                self.assertEqual(lambda_p**2, lambda_r**2 * ratio)
                row_sum += ratio
            self.assertLessEqual(row_sum, Fraction(4, 3))

    def test_two_l1_factors_do_not_force_an_l1_product(self) -> None:
        a = Fraction(2, 3)
        b = Fraction(2, 3)
        self.assertLess(a, 1)
        self.assertLess(b, 1)
        self.assertGreaterEqual(a + b, 1)

    def test_near_cluster_has_fixed_cardinality(self) -> None:
        k = 3
        for q in (k, 10, 100):
            near = list(range(q - k, q + k + 1))
            self.assertEqual(len(near), 2 * k + 1)
            self.assertIn(q, near)
            self.assertIn(q + 1, near)

    def test_strict_tail_starts_beyond_near_cluster(self) -> None:
        q = 11
        k = 2
        tail = list(range(q + k + 1, q + k + 6))
        self.assertTrue(all(p > q + k for p in tail))
        self.assertNotIn(q, tail)

    def test_high_interpolation_retains_positive_frequency_power(self) -> None:
        threshold_power = Fraction(4, 3)
        enstrophy_conversion = Fraction(-2, 3)
        self.assertEqual(
            threshold_power + enstrophy_conversion,
            Fraction(2, 3),
        )

    def test_shell_holder_remainder_diverges(self) -> None:
        partial_10 = sum(2.0**p for p in range(10))
        partial_20 = sum(2.0**p for p in range(20))
        self.assertTrue(math.isfinite(partial_20))
        self.assertGreater(partial_20, 100.0 * partial_10)

    def test_selector_occupancy_does_not_bound_variation(self) -> None:
        total_measure = 1.0
        for components in (1, 10, 1000):
            self.assertAlmostEqual(
                components * (total_measure / components),
                total_measure,
            )

    def test_threshold_shell_is_excluded_from_strict_high_set(self) -> None:
        q = 7
        strict_high = list(range(q + 1, q + 5))
        self.assertNotIn(q, strict_high)
        self.assertTrue(all(p > q for p in strict_high))


if __name__ == "__main__":
    unittest.main()
