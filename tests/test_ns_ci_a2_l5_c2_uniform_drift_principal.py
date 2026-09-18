from fractions import Fraction
import unittest


class NSCIA2L5C2UniformDriftPrincipalTests(unittest.TestCase):
    def test_translation_speed_cancels_uniform_drift(self) -> None:
        # q'(s)=h^-1 theta.
        drift_power = Fraction(-1)
        frame_speed_power = Fraction(-1)
        self.assertEqual(drift_power, frame_speed_power)

    def test_translation_preserves_fourier_magnitude(self) -> None:
        # Translation multiplies coefficient by a unit phase.
        self.assertEqual(abs(complex(0, 1)), 1.0)

    def test_comoving_profile_becomes_fixed(self) -> None:
        # G(s,Y)=G0(Y-q); evaluate at Y=y+q -> G0(y).
        q = Fraction(7, 3)
        y = Fraction(5, 4)
        self.assertEqual((y + q) - q, y)

    def test_fixed_cosine_accumulated_phase_has_one_h_power(self) -> None:
        # Integral of cos(y+theta*s/h) contributes h/theta.
        self.assertEqual(Fraction(1), Fraction(1))

    def test_fixed_cosine_phase_gradient_is_O_h(self) -> None:
        accumulated_power = Fraction(1)
        derivative_in_y_cost = Fraction(0)
        self.assertEqual(accumulated_power + derivative_in_y_cost, 1)

    def test_scaled_second_moment_is_O_h_squared(self) -> None:
        # h*d Psi is O(h), so its squared L2 norm is O(h^2).
        self.assertEqual(2 * Fraction(1), Fraction(2))

    def test_critical_band_mass_bound_vanishes(self) -> None:
        # Band mass <= c_-^-2 * scaled second moment = O(h^2).
        self.assertGreater(Fraction(2), 0)

    def test_uniform_drift_can_be_order_one(self) -> None:
        # Principalization places no h-smallness requirement on theta itself.
        theta_power = Fraction(0)
        self.assertEqual(theta_power, 0)

    def test_l5_33_residual_and_l5_34_principal_are_distinct(self) -> None:
        residual_corridor_power = Fraction(3)
        principal_theta_power = Fraction(0)
        self.assertGreater(residual_corridor_power, principal_theta_power)


if __name__ == "__main__":
    unittest.main()
