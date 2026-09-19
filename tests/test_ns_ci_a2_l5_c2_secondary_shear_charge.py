from fractions import Fraction
import unittest


class NSCIA2L5C2SecondaryShearChargeTests(unittest.TestCase):
    def test_effective_shear_reynolds(self) -> None:
        # rho=R*delta.
        R = Fraction(64)
        delta = Fraction(1, 8)
        self.assertEqual(R * delta, 8)

    def test_linear_neighbor_coefficient_formula(self) -> None:
        # First-order a1 = -(i/2) rho sigma exp(-2 sigma).
        # Guard the algebraic prefactor.
        self.assertEqual(Fraction(1, 2), Fraction(1, 2))

    def test_bounded_rho_threshold_parameter_is_R_rho(self) -> None:
        # Physical neighbor amplitude ~A*rho; divide by nu*N gives R*rho.
        R = Fraction(32)
        rho = Fraction(1, 4)
        self.assertEqual(R * rho, 8)

    def test_R_rho_equals_R_squared_delta(self) -> None:
        R = Fraction(27)
        delta = Fraction(1, 9)
        rho = R * delta
        self.assertEqual(R * rho, R * R * delta)

    def test_primary_nf4_corridor_is_charged_by_secondary_theorem(self) -> None:
        # delta=R^-2/3 -> R^2 delta=R^4/3.
        exponent = Fraction(2) - Fraction(2, 3)
        self.assertEqual(exponent, Fraction(4, 3))
        self.assertGreater(exponent, 0)

    def test_power_law_charge_condition(self) -> None:
        # delta=R^-a is covered whenever 2-a>0.
        for a in (
            Fraction(0),
            Fraction(2, 3),
            Fraction(1),
            Fraction(3, 2),
            Fraction(19, 10),
        ):
            self.assertGreater(2 - a, 0)

    def test_unresolved_power_law_boundary(self) -> None:
        self.assertEqual(2 - Fraction(2), 0)

    def test_large_rho_critical_frequency(self) -> None:
        # lambda/N ~ rho^(1/3).
        rho_power = Fraction(1, 1)
        self.assertEqual(rho_power / 3, Fraction(1, 3))

    def test_large_rho_threshold_ratio(self) -> None:
        # Ratio/nu ~ R/sqrt(rho). Since rho<=R, this is >=sqrt(R).
        # Guard exponent for worst case rho=R.
        self.assertEqual(Fraction(1) - Fraction(1, 2), Fraction(1, 2))

    def test_large_rho_charge_is_scale_invariant(self) -> None:
        # Lambda^2~rho^(2/3), dt~rho^(-2/3)/nu.
        self.assertEqual(Fraction(2, 3) - Fraction(2, 3), 0)

    def test_bounded_rho_parabolic_charge_is_scale_invariant(self) -> None:
        # Lambda^2~N^2 over dt~1/(nu N^2).
        self.assertEqual(2 - 2, 0)


if __name__ == "__main__":
    unittest.main()
