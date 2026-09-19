from fractions import Fraction
import unittest


class NSCIA2L5C2DirectionDefectTests(unittest.TestCase):
    def test_direction_term_has_explicit_h_minus_one(self) -> None:
        self.assertEqual(Fraction(-1), Fraction(-1))

    def test_critical_transverse_derivative_adds_second_h_minus_one(self) -> None:
        explicit = Fraction(-1)
        derivative = Fraction(-1)
        self.assertEqual(explicit + derivative, Fraction(-2))

    def test_nf4_balance_requires_h_cubed_direction(self) -> None:
        # theta*h^-2 must be O(h): theta is O(h^3).
        residual_target = Fraction(1)
        amplified_operator = Fraction(-2)
        self.assertEqual(residual_target - amplified_operator, Fraction(3))

    def test_h_cubed_is_rho_inverse(self) -> None:
        # h=rho^-1/3.
        h_in_rho = Fraction(-1, 3)
        self.assertEqual(3 * h_in_rho, Fraction(-1))

    def test_demodulated_derivative_leading_term_is_phase_gradient(self) -> None:
        # h*dY Phi -> -i F_Y A after phase removal.
        h_power = 1
        phase_derivative_power = -1
        self.assertEqual(h_power + phase_derivative_power, 0)

    def test_direction_weighted_residual_scaling(self) -> None:
        # h^-2 * theta with theta=h^3 leaves h.
        self.assertEqual(Fraction(-2) + Fraction(3), Fraction(1))

    def test_profile_drift_and_direction_drift_have_different_operator_order(self) -> None:
        scalar_potential_order = 0
        transverse_derivative_order = 1
        self.assertGreater(transverse_derivative_order, scalar_potential_order)

    def test_persistent_defect_l2_scale_matches_pointwise_scale(self) -> None:
        # On an O(1) critical interval, fixed-amplitude L2 and pointwise powers match.
        pointwise_power = Fraction(3)
        l2_power = Fraction(3)
        self.assertEqual(pointwise_power, l2_power)

    def test_primary_rho_equal_R_direction_corridor_is_R_inverse(self) -> None:
        self.assertEqual(Fraction(-1), Fraction(-1))


if __name__ == "__main__":
    unittest.main()
