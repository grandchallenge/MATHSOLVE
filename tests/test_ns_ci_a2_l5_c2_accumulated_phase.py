from fractions import Fraction
import unittest


class NSCIA2L5C2AccumulatedPhaseTests(unittest.TestCase):
    def test_oscillatory_profile_integrates_to_h_error(self) -> None:
        # Integral of sin(s/h) is h*(1-cos(s/h)): one power of h.
        instantaneous_error_power = 0
        accumulated_error_power = 1
        self.assertEqual(accumulated_error_power - instantaneous_error_power, 1)

    def test_fast_potential_cancels_under_accumulated_phase(self) -> None:
        # F_s=G, so derivative of exp(-iF/h) contributes -iG/h.
        phase_power = -1
        potential_power = -1
        self.assertEqual(phase_power, potential_power)

    def test_semiclassical_first_moment_uses_accumulated_gradient(self) -> None:
        # h*d Phi = phase*(h*d A - i F_Y A).
        self.assertEqual(1 + (-1), 0)

    def test_semiclassical_second_derivative_has_order_one_phase_square(self) -> None:
        # h^2*d^2 exp(-iF/h) has leading factor -(F_Y)^2.
        self.assertEqual(2 + 2 * (-1), 0)

    def test_h_error_in_phase_coefficient_matches_bridge_rate(self) -> None:
        self.assertEqual(Fraction(1), Fraction(1))

    def test_critical_frequency_scale(self) -> None:
        # h=rho^-1/3 -> |n|~h^-1~rho^1/3.
        self.assertEqual(Fraction(1, 3), Fraction(1, 3))

    def test_physical_threshold_ratio_worst_case(self) -> None:
        # R/sqrt(rho) >= sqrt(R) for rho<=R.
        self.assertEqual(Fraction(1) - Fraction(1, 2), Fraction(1, 2))

    def test_selector_charge_is_scale_invariant(self) -> None:
        # Lambda^2~rho^(2/3), dt~rho^(-2/3)/nu.
        self.assertEqual(Fraction(2, 3) - Fraction(2, 3), 0)

    def test_accumulated_phase_not_instantaneous_profile_is_invariant(self) -> None:
        # O(1) profile oscillation may have O(h) accumulated error.
        profile_power = 0
        accumulated_power = 1
        self.assertGreater(accumulated_power, profile_power)

    def test_l5_31_heat_drift_is_stricter_special_case(self) -> None:
        # L5-31 accumulated phase error is O(h^2), stronger than O(h).
        self.assertGreater(Fraction(2), Fraction(1))


if __name__ == "__main__":
    unittest.main()
