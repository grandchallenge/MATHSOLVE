from fractions import Fraction
import unittest


class NSCIA2L5C2DistanceSobolevTailTests(unittest.TestCase):
    def test_plane_frequency_count_yields_one_power_after_cauchy_schwarz(self) -> None:
        # A two-dimensional annulus has O(L^2) lattice sites, so its square-root
        # count contributes one power of L.
        for L in (2, 4, 8, 16):
            count_upper = L**2
            self.assertEqual(Fraction(count_upper, 1) ** Fraction(1, 2), L)

    def test_sobolev_tail_exponent_is_one_minus_s(self) -> None:
        # sqrt(count) contributes L; the H^s shell L2 tail contributes L^-s.
        for s in (4, 6, 8):
            exponent = 1 - s
            self.assertLess(exponent, -2)

    def test_threshold_ratio_cancels_one_frequency_power(self) -> None:
        # Physical block: A * L^(1-s); divide by lambda=N L; A=R nu N.
        # The normalized threshold ratio is therefore R * L^-s.
        R = Fraction(81, 1)
        for s in (4, 6):
            L = Fraction(3, 1)
            lhs = R * L ** (1 - s) / L
            rhs = R * L ** (-s)
            self.assertEqual(lhs, rhs)

    def test_s4_threshold_distance_is_fourth_root_scale(self) -> None:
        # For R=M^4, L=M makes R L^-4 order one.
        for M in (2, 3, 5, 7):
            R = Fraction(M**4, 1)
            L = Fraction(M, 1)
            self.assertEqual(R * L ** (-4), 1)

    def test_fourth_root_scale_is_strictly_below_sqrt_scale(self) -> None:
        for M in (2, 3, 5, 7, 11):
            R = M**4
            r_quarter = M
            r_half = M**2
            self.assertLess(r_quarter, r_half)

    def test_turnover_selector_charge_exponent(self) -> None:
        # Lambda^2 contributes R^(2/s); turnover duration contributes R^-1.
        for s in (4, 6, 8, 10):
            exponent = Fraction(2, s) - 1
            self.assertLess(exponent, 0)

    def test_s4_charge_is_inverse_square_root(self) -> None:
        charges = []
        for M in (2, 4, 8, 16):
            # R=M^4; R^(2/4-1)=R^-1/2=M^-2.
            R = M**4
            charges.append(Fraction(1, M**2))
            self.assertEqual(Fraction(M**2, R), Fraction(1, M**2))
        self.assertTrue(all(b < a for a, b in zip(charges, charges[1:])))

    def test_fixed_distance_lower_certificate_is_compatible_with_s4_upper(self) -> None:
        # L5-19 lower certificate is c/R; L5-20 upper scale is C/sqrt(R).
        # For R>1 the former is asymptotically smaller.
        for R in (4, 16, 64, 256):
            lower_scale = Fraction(1, R)
            # all selected R are perfect squares
            root = int(R**0.5)
            upper_scale = Fraction(1, root)
            self.assertLessEqual(lower_scale, upper_scale)

    def test_any_positive_power_can_be_beaten_by_fixed_sobolev_order(self) -> None:
        # To get R^(1/s) <= R^delta, choose integer s >= 1/delta.
        cases = [
            (Fraction(1, 3), 4),
            (Fraction(1, 5), 6),
            (Fraction(1, 10), 11),
        ]
        for delta, s in cases:
            self.assertLessEqual(Fraction(1, s), delta)


if __name__ == "__main__":
    unittest.main()
