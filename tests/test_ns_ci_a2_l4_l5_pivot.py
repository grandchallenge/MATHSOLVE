import math
import unittest
from fractions import Fraction


class NSCIA2PivotTests(unittest.TestCase):
    def test_critical_integral_is_scale_invariant(self) -> None:
        # Under u_rho=rho*u(rho*x,rho^2*t), ||u||_6 scales as rho^(1/2).
        l6_scaling = Fraction(1, 2)
        time_scaling = Fraction(-2, 1)
        total = 4 * l6_scaling + time_scaling
        self.assertEqual(total, 0)

    def test_lambda_l2_is_scale_invariant(self) -> None:
        lambda_scaling = Fraction(1, 1)
        time_scaling = Fraction(-2, 1)
        self.assertEqual(2 * lambda_scaling + time_scaling, 0)

    def test_weighted_shell_dissipation_has_f_scaling(self) -> None:
        # ||grad u_q||_2 scales as rho^(1/2), so its square scales as rho.
        shell_dissipation_scaling = Fraction(1, 1)
        frequency_scaling = Fraction(1, 1)
        f_scaling = Fraction(2, 1)
        self.assertEqual(
            shell_dissipation_scaling + frequency_scaling,
            f_scaling,
        )

    def test_low_frequency_baseline_is_scale_correct(self) -> None:
        # U^2 * Lambda^2 * ||grad u||_2^2 has scaling
        # rho^-1 * rho^2 * rho^1 = rho^2, matching ||u||_6^4.
        energy_squared_scaling = Fraction(-1, 1)
        lambda_squared_scaling = Fraction(2, 1)
        gradient_squared_scaling = Fraction(1, 1)
        self.assertEqual(
            energy_squared_scaling
            + lambda_squared_scaling
            + gradient_squared_scaling,
            Fraction(2, 1),
        )

    def test_high_mode_interpolation_leaves_positive_frequency_power(self) -> None:
        # ||u_p||_6^2 <= ||u_p||_2^(2/3)||u_p||_inf^(4/3).
        # The threshold contributes lambda^(4/3).
        # Writing A_p=lambda^2||u_p||_2^2 gives
        # ||u_p||_2^(2/3)=A_p^(1/3)lambda^(-2/3).
        threshold_power = Fraction(4, 3)
        enstrophy_conversion = Fraction(-2, 3)
        self.assertEqual(
            threshold_power + enstrophy_conversion,
            Fraction(2, 3),
        )

    def test_product_of_two_l1_powers_need_not_be_l1(self) -> None:
        # t^-a belongs to L1(0,1) iff a<1.
        a = Fraction(2, 3)
        b = Fraction(2, 3)
        self.assertLess(a, 1)
        self.assertLess(b, 1)
        self.assertGreaterEqual(a + b, 1)

    def test_geometric_kernel_has_uniform_row_sum(self) -> None:
        for cutoff in (10, 100, 1000):
            row_sum = sum(2.0 ** (-j) for j in range(cutoff + 1))
            self.assertLess(row_sum, 2.0)

    def test_endpoint_kernel_row_sum_grows(self) -> None:
        row_10 = sum(1.0 for _ in range(11))
        row_100 = sum(1.0 for _ in range(101))
        self.assertGreater(row_100, row_10)
        self.assertEqual(row_100, 101.0)

    def test_harmonic_endpoint_is_not_uniform(self) -> None:
        row_100 = sum(1.0 / (j + 1) for j in range(100))
        row_10000 = sum(1.0 / (j + 1) for j in range(10000))
        self.assertGreater(row_10000, row_100)
        self.assertGreater(row_10000, math.log(10000))

    def test_inverse_frequency_exit_charge_is_summable(self) -> None:
        total = sum(2.0 ** (-q) for q in range(1000))
        self.assertAlmostEqual(total, 2.0, places=12)

    def test_bernstein_upper_bound_cannot_be_reversed(self) -> None:
        # Abstractly, X <= C*Y and X <= threshold do not imply Y <= threshold/C.
        c = 2.0
        x = 1.0
        y = 100.0
        threshold = 1.0
        self.assertLessEqual(x, c * y)
        self.assertLessEqual(x, threshold)
        self.assertGreater(y, threshold / c)


if __name__ == "__main__":
    unittest.main()
