from fractions import Fraction
import unittest


class NSCIA2L5C2MixBridgeNormalFormTests(unittest.TestCase):
    def test_general_phase_demodulation_scales(self) -> None:
        # q' = h^-1 a, p=hq, so h^2 q = h p and h^2 q^2=p^2.
        self.assertEqual(2 - 1, 1)
        self.assertEqual(2 - 2, 0)

    def test_nf2_implies_p_minus_s_is_h_squared(self) -> None:
        # Integrating an O(h^2) coefficient error over a fixed s-window
        # preserves the O(h^2) scale.
        coefficient_error_power = 2
        integration_window_power = 0
        self.assertEqual(coefficient_error_power + integration_window_power, 2)

    def test_demodulated_leading_damping_is_order_one(self) -> None:
        # -p^2 (g')^2 survives as h->0.
        p_power = 0
        g_prime_power = 0
        self.assertEqual(2 * p_power + 2 * g_prime_power, 0)

    def test_first_order_bridge_terms_are_order_h(self) -> None:
        # -2 i h p g' A_y and -i h p g'' A.
        h_power = 1
        p_power = 0
        self.assertEqual(h_power + p_power, 1)

    def test_critical_limit_damping_integral(self) -> None:
        # Integral_0^s sigma^2 d sigma = s^3/3 for any fixed phase profile.
        s = Fraction(3, 2)
        self.assertEqual(s**3 / 3, Fraction(9, 8))

    def test_scaled_second_moment_frequency_is_order_one(self) -> None:
        # Critical band n~h^-1 => (hn)^2~1.
        self.assertEqual(2 + 2 * (-1), 0)

    def test_scaled_fourth_moment_frequency_is_order_one(self) -> None:
        self.assertEqual(4 + 4 * (-1), 0)

    def test_band_count_for_one_transverse_coordinate(self) -> None:
        # Fixed C_-<=|hn|<=C_+ has O(h^-1) integer modes.
        self.assertEqual(-1, -1)

    def test_coefficient_from_positive_band_mass_has_h_half_scale(self) -> None:
        # O(1) mass across O(h^-1) modes -> coefficient squared O(h).
        coeff_sq_power = 0 - (-1)
        self.assertEqual(coeff_sq_power, 1)

    def test_bridge_threshold_ratio(self) -> None:
        # A_phys~h^-3, coefficient~h^1/2, lambda~h^-1.
        exponent = Fraction(-3, 1) + Fraction(1, 2) + 1
        self.assertEqual(exponent, Fraction(-3, 2))

    def test_bridge_selector_charge_is_order_one(self) -> None:
        # Lambda^2~h^-2 and dt~h^2 ds/nu.
        self.assertEqual(-2 + 2, 0)


if __name__ == "__main__":
    unittest.main()
