from fractions import Fraction
import unittest


class NSCIA2L5C2MixSubcriticalLowerTests(unittest.TestCase):
    def test_inviscid_second_moment(self) -> None:
        # ||D exp(-i tau cos y)||_2^2 = tau^2 <sin^2 y> = tau^2/2.
        tau2 = Fraction(25, 1)
        self.assertEqual(tau2 * Fraction(1, 2), Fraction(25, 2))

    def test_inviscid_fourth_moment_coefficients(self) -> None:
        # ||D^2 phi||^2 = tau^2/2 + 3 tau^4/8.
        tau = Fraction(2, 1)
        value = tau**2 / 2 + 3 * tau**4 / 8
        self.assertEqual(value, 8)

    def test_paley_zygmund_lower_mass(self) -> None:
        # For tau>=1:
        # E[n^2]=tau^2/2, E[n^4]<=7 tau^4/8.
        # theta=1/2 gives P(|n|>=tau/2)>=1/14.
        lower = Fraction(1, 4) * Fraction(1, 4) / Fraction(7, 8)
        self.assertEqual(lower, Fraction(1, 14))

    def test_outer_tail_markov_bound(self) -> None:
        # P(|n|>2tau) <= (7/8)/16 = 7/128.
        self.assertEqual(Fraction(7, 8) / 16, Fraction(7, 128))

    def test_ballistic_band_mass_constant(self) -> None:
        mass = Fraction(1, 14) - Fraction(7, 128)
        self.assertEqual(mass, Fraction(15, 896))
        self.assertGreater(mass, 0)

    def test_subcritical_comparison_error_vanishes(self) -> None:
        # epsilon T^3 with T=R^beta is R^(3beta-1).
        betas = [
            Fraction(1, 6),
            Fraction(1, 4),
            Fraction(3, 10),
        ]
        for beta in betas:
            exponent = 3 * beta - 1
            self.assertLess(exponent, 0)

    def test_coefficient_from_band_mass_has_tau_inverse_half_scale(self) -> None:
        # mass >= m0/4 spread over <=6 tau modes gives
        # |a_n|^2 >= m0/(24 tau).
        m0 = Fraction(15, 896)
        coeff_sq_factor = m0 / 24
        self.assertGreater(coeff_sq_factor, 0)

    def test_threshold_ratio_grows_on_subcritical_window(self) -> None:
        # R tau^-3/2 with tau=R^beta has exponent 1-3beta/2.
        for beta in (
            Fraction(1, 6),
            Fraction(1, 4),
            Fraction(3, 10),
            Fraction(1, 3) - Fraction(1, 100),
        ):
            exponent = 1 - Fraction(3, 2) * beta
            self.assertGreater(exponent, 0)

    def test_selector_charge_lower_exponent(self) -> None:
        # Lambda~N T over normalized duration T gives T^3/(R nu).
        for beta in (
            Fraction(1, 6),
            Fraction(1, 4),
            Fraction(3, 10),
        ):
            exponent = 3 * beta - 1
            self.assertLess(exponent, 0)

    def test_critical_exponent_is_exact_perturbative_boundary(self) -> None:
        beta = Fraction(1, 3)
        self.assertEqual(3 * beta - 1, 0)


if __name__ == "__main__":
    unittest.main()
