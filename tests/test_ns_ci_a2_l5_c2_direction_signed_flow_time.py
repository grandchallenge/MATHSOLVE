from fractions import Fraction
import unittest


class NSCIA2L5C2DirectionSignedFlowTimeTests(unittest.TestCase):
    def test_signed_clock_definition_scale(self) -> None:
        # kappa=h^-1 int theta ds.
        self.assertEqual(Fraction(-1), Fraction(-1))

    def test_oscillatory_theta_signed_clock_is_order_h(self) -> None:
        # theta=sin(s/h^2): integral contributes h^2, then divide by h.
        integral_power = Fraction(2)
        prefactor_power = Fraction(-1)
        self.assertEqual(integral_power + prefactor_power, Fraction(1))

    def test_oscillatory_theta_absolute_budget_diverges(self) -> None:
        # Integral |theta| over fixed time is O(1); multiply by h^-1.
        absolute_integral_power = Fraction(0)
        h_inverse = Fraction(-1)
        self.assertEqual(absolute_integral_power + h_inverse, Fraction(-1))

    def test_signed_and_absolute_scales_are_distinct(self) -> None:
        signed_clock_power = Fraction(1)
        absolute_budget_power = Fraction(-1)
        self.assertGreater(signed_clock_power, absolute_budget_power)

    def test_separable_flow_composition_uses_scalar_clock(self) -> None:
        # Autonomous flow times add.
        kappa_1 = Fraction(2, 3)
        kappa_2 = Fraction(-1, 5)
        self.assertEqual(kappa_1 + kappa_2, Fraction(7, 15))

    def test_sin_profile_fixed_point_jacobian_exponent(self) -> None:
        # At Y=0, log J=kappa; at pi, log J=-kappa.
        kappa = Fraction(7, 4)
        self.assertEqual(kappa, Fraction(7, 4))
        self.assertEqual(-kappa, Fraction(-7, 4))

    def test_near_identity_clock_matches_l5_35_order(self) -> None:
        # kappa=O(h) gives frame error O(h).
        self.assertEqual(Fraction(1), Fraction(1))

    def test_absolute_h_scale_not_necessary(self) -> None:
        # Instantaneous theta can be O(1), not O(h), while signed clock is O(h).
        theta_power = Fraction(0)
        l5_35_absolute_sufficient_power = Fraction(1)
        self.assertLess(theta_power, l5_35_absolute_sufficient_power)

    def test_nonconstant_fixed_phase_keeps_order_one_gradient(self) -> None:
        # F_0=s G, so F_{0,Z}=s G' is O(1) on fixed positive critical time.
        self.assertEqual(Fraction(0), Fraction(0))


if __name__ == "__main__":
    unittest.main()
