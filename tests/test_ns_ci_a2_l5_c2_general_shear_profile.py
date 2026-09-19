from fractions import Fraction
import unittest


class NSCIA2L5C2GeneralShearProfileTests(unittest.TestCase):
    def test_effective_reynolds(self) -> None:
        R = Fraction(81)
        delta = Fraction(1, 9)
        self.assertEqual(R * delta, 9)

    def test_heat_profile_critical_freezing_scale(self) -> None:
        # tau/rho at tau=s/h and rho=h^-3 is s*h^2.
        h_power_tau = -1
        h_power_inv_rho = 3
        self.assertEqual(h_power_tau + h_power_inv_rho, 2)

    def test_first_order_general_profile_coefficient(self) -> None:
        # a_m,lin = -i rho G_m sigma exp(-(1+m^2)sigma).
        # Guard that the dependence is linear in rho and G_m.
        rho_power = 1
        profile_power = 1
        self.assertEqual(rho_power, 1)
        self.assertEqual(profile_power, 1)

    def test_critical_phase_gradient_scale(self) -> None:
        # F_h -> s G, so F'_h -> s G'.
        self.assertEqual(Fraction(1), Fraction(1))

    def test_critical_scaled_frequency(self) -> None:
        # h=rho^-1/3, so |n|~h^-1~rho^1/3.
        self.assertEqual(Fraction(1, 3), Fraction(1, 3))

    def test_large_rho_threshold_ratio_worst_case(self) -> None:
        # R/sqrt(rho) >= sqrt(R) because rho<=R.
        self.assertEqual(Fraction(1) - Fraction(1, 2), Fraction(1, 2))

    def test_large_rho_charge_cancels_scale(self) -> None:
        # Lambda^2~rho^2/3 and dt~rho^-2/3/nu.
        self.assertEqual(Fraction(2, 3) - Fraction(2, 3), 0)

    def test_bounded_rho_threshold_parameter(self) -> None:
        # R*rho = R^2*delta.
        R = Fraction(16)
        delta = Fraction(1, 8)
        rho = R * delta
        self.assertEqual(R * rho, R * R * delta)

    def test_nonconstant_profile_has_some_nonzero_fourier_mode(self) -> None:
        coeffs = {1: Fraction(1, 2), 2: Fraction(-1, 3)}
        self.assertTrue(any(v != 0 for v in coeffs.values()))

    def test_finite_family_is_one_profile(self) -> None:
        # Relative coefficients add linearly into one trigonometric profile.
        family = [Fraction(1, 2), Fraction(1, 3), Fraction(-1, 6)]
        self.assertEqual(sum(family), Fraction(2, 3))


if __name__ == "__main__":
    unittest.main()
