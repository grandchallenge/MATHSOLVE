from fractions import Fraction
import unittest


class NSCIA2L5C2MixCriticalSemiclassicalTests(unittest.TestCase):
    def test_critical_scaling(self) -> None:
        # epsilon=h^3 and s=h tau, so epsilon*tau=h^2 s.
        h_power_epsilon = 3
        h_power_tau = -1
        self.assertEqual(h_power_epsilon + h_power_tau, 2)

    def test_phase_integral_scaling(self) -> None:
        # q_h=h^-3(1-exp(-h^2 s)); p_h=h q_h -> s.
        q_prefactor_power = -3
        first_numerator_power = 2
        p_extra_power = 1
        self.assertEqual(
            q_prefactor_power + first_numerator_power + p_extra_power,
            0,
        )

    def test_critical_diffusion_phase_balance(self) -> None:
        # h^2 q_h^2 = p_h^2 is order one at critical scaling.
        h_power_h2 = 2
        h_power_q2 = -2
        self.assertEqual(h_power_h2 + h_power_q2, 0)

    def test_limit_amplitude_damping_integral(self) -> None:
        # integral_0^s sigma^2 d sigma = s^3/3.
        s = Fraction(3, 2)
        integral = s**3 / 3
        self.assertEqual(integral, Fraction(9, 8))

    def test_scaled_second_moment_is_order_one(self) -> None:
        # n~h^-1 => (h n)^2 is order one.
        h_power_n = -1
        self.assertEqual(2 + 2 * h_power_n, 0)

    def test_scaled_fourth_moment_is_order_one(self) -> None:
        # n~h^-1 => (h n)^4 is order one.
        h_power_n = -1
        self.assertEqual(4 + 4 * h_power_n, 0)

    def test_band_mode_count_is_inverse_h(self) -> None:
        # Fixed band c_-<=|h n|<=c_+ contains O(h^-1) integer modes.
        frequency_power = -1
        self.assertEqual(frequency_power, -1)

    def test_one_coefficient_has_square_root_h_scale(self) -> None:
        # Fixed positive mass over O(h^-1) modes gives |a_n|^2>=c h.
        mass_power = 0
        count_power = -1
        coeff_sq_power = mass_power - count_power
        self.assertEqual(coeff_sq_power, 1)

    def test_threshold_ratio_diverges_as_h_minus_three_halves(self) -> None:
        # A~h^-3, coefficient~h^1/2, lambda~N h^-1.
        exponent = Fraction(-3, 1) + Fraction(1, 2) - Fraction(-1, 1)
        self.assertEqual(exponent, Fraction(-3, 2))

    def test_selector_charge_is_scale_invariant(self) -> None:
        # Lambda^2~N^2 h^-2 and dt~h^2/(nu N^2) ds.
        lambda_sq_h_power = -2
        dt_h_power = 2
        self.assertEqual(lambda_sq_h_power + dt_h_power, 0)


if __name__ == "__main__":
    unittest.main()
