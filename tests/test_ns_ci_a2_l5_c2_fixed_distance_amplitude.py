from fractions import Fraction
from math import isqrt
import unittest


class NSCIA2L5C2FixedDistanceAmplitudeTests(unittest.TestCase):
    def test_dimensionless_viscosity_is_inverse_overshoot(self) -> None:
        nu = Fraction(7, 5)
        n = Fraction(11, 1)
        for r in (2, 5, 13):
            R = Fraction(r, 1)
            amplitude = R * nu * n
            epsilon = nu * n / amplitude
            self.assertEqual(epsilon, Fraction(1, r))

    def test_fixed_annulus_width_can_be_cleared_at_finite_distance(self) -> None:
        # Representative annulus constants only; the theorem uses arbitrary
        # fixed 0<a_LP<b_LP and chooses a finite r_* depending on them.
        a_lp = Fraction(1, 2)
        b_lp = Fraction(2, 1)
        # Initial maximum frequency squared is 2 N^2.
        # At r=6, generated frequency squared is 50 N^2, so the ratio is 5.
        r = 6
        generated_sq = (r + 1) ** 2 + 1
        initial_sq = 2
        # Compare squares to avoid irrational arithmetic:
        # sqrt(generated_sq / initial_sq) > b_lp/a_lp.
        self.assertGreater(
            Fraction(generated_sq, initial_sq),
            (b_lp / a_lp) ** 2,
        )

    def test_partition_of_unity_forces_one_multiplier_of_size_one_over_J(self) -> None:
        multipliers = [
            Fraction(1, 7),
            Fraction(-1, 14),
            Fraction(5, 14),
            Fraction(4, 7),
        ]
        self.assertEqual(sum(multipliers), 1)
        J = len(multipliers)
        self.assertGreaterEqual(max(abs(x) for x in multipliers), Fraction(1, J))

    def test_threshold_condition_is_linear_in_R_at_fixed_distance(self) -> None:
        # If a generated normalized Fourier coefficient is bounded below by b,
        # and one LP multiplier has magnitude at least 1/J, then
        # lambda_p^{-1}||u_p||_inf >= R*nu*a_lp*b/(J*L_r).
        a_lp = Fraction(1, 2)
        b = Fraction(1, 20)
        J = 4
        L_upper = 8  # rational upper stand-in for fixed L_r
        c0 = Fraction(1, 100)
        R = 20
        normalized_ratio = Fraction(R, 1) * a_lp * b / (J * L_upper)
        self.assertGreater(normalized_ratio, c0)

    def test_turnover_window_has_inverse_R_physical_length(self) -> None:
        nu = Fraction(5, 3)
        n = Fraction(7, 1)
        tau_length = Fraction(3, 10)
        for R in (2, 4, 8, 16):
            amplitude = R * nu * n
            physical_length = tau_length / (amplitude * n)
            self.assertEqual(
                physical_length,
                tau_length / (R * nu * n**2),
            )

    def test_fixed_distance_lambda2_charge_certificate_scales_as_inverse_R(self) -> None:
        nu = Fraction(3, 2)
        tau_length = Fraction(1, 5)
        b_lp = Fraction(2, 1)
        lattice_norm_sq = 50  # (r+1)^2+1 for r=6
        charges = []
        for R in (2, 4, 8, 16):
            charge = tau_length * lattice_norm_sq / (b_lp**2 * R * nu)
            charges.append(charge)
        for left, right in zip(charges, charges[1:]):
            self.assertEqual(right / left, Fraction(1, 2))

    def test_geometric_overshoots_can_have_summable_fixed_distance_certificates(self) -> None:
        # With R_n=2^n, any fixed-distance c/R_n certificate is summable.
        partial = sum(Fraction(1, 2**n) for n in range(1, 20))
        self.assertLess(partial, 1)

    def test_order_one_turnover_charge_requires_spectral_distance_squared_like_R(self) -> None:
        # The fixed-distance certificate is proportional to L^2/R.
        # Keeping it order one requires L^2 comparable to R.
        for k in range(2, 10):
            R = 4**k
            L = 2**k
            self.assertEqual(Fraction(L**2, R), 1)

    def test_fixed_distance_growth_is_insufficient_for_sqrt_R_requirement(self) -> None:
        fixed_lattice_norm_sq = 50
        ratios = [
            Fraction(fixed_lattice_norm_sq, 4**k)
            for k in range(2, 10)
        ]
        self.assertTrue(all(b < a for a, b in zip(ratios, ratios[1:])))
        self.assertLess(ratios[-1], Fraction(1, 1000))


if __name__ == "__main__":
    unittest.main()
