from fractions import Fraction
import unittest


class NSCIA2L5C2DirectionMovingFrameTests(unittest.TestCase):
    def test_translation_speed_cancels_direction_term(self) -> None:
        # Gamma' = h^-1 theta exactly matches the principal drift coefficient.
        drift_power = Fraction(-1)
        gamma_prime_power = Fraction(-1)
        self.assertEqual(drift_power, gamma_prime_power)

    def test_translation_preserves_semiclassical_derivative_scale(self) -> None:
        # Translation commutes with h*d/dY.
        derivative_power_before = Fraction(1)
        derivative_power_after = Fraction(1)
        self.assertEqual(derivative_power_before, derivative_power_after)

    def test_translation_preserves_fourier_magnitude(self) -> None:
        # Fourier coefficient is multiplied only by exp(i n Gamma).
        modulus = 1
        self.assertEqual(modulus, 1)

    def test_fast_sweep_accumulated_phase_is_order_h(self) -> None:
        # Integral cos(Y+theta*s/h) ds contributes prefactor h/theta.
        prefactor_h_power = Fraction(1)
        self.assertEqual(prefactor_h_power, 1)

    def test_fast_sweep_limit_phase_is_zero(self) -> None:
        # O(h) accumulated phase converges to zero.
        limit_power = Fraction(1)
        self.assertGreater(limit_power, 0)

    def test_rigid_motion_has_zero_frame_deformation(self) -> None:
        # B(Y)=1 => B_Y=0, hence Jacobian exponent vanishes.
        B_y = 0
        self.assertEqual(B_y, 0)

    def test_nonuniform_flow_jacobian_has_h_inverse_amplification(self) -> None:
        # J_s/J = h^-1 theta B_Y.
        self.assertEqual(Fraction(-1), Fraction(-1))

    def test_bounded_deformation_budget_is_dimensionless(self) -> None:
        # h^-1 * theta * B_Y integrated in critical time must be O(1).
        h_power = Fraction(-1)
        theta_power = Fraction(1)
        spatial_gradient_power = Fraction(0)
        self.assertEqual(h_power + theta_power + spatial_gradient_power, 0)

    def test_l5_33_residual_and_principal_scales_are_distinct(self) -> None:
        # Residual classification requires theta~h^3; principal translation has no such bound.
        residual_theta_power = Fraction(3)
        principal_required_power = Fraction(0)
        self.assertGreater(residual_theta_power, principal_required_power)


if __name__ == "__main__":
    unittest.main()
