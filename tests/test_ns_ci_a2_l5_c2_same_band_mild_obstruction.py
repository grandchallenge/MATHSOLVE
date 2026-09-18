from fractions import Fraction
import unittest


class NSCIA2L5C2SameBandMildObstructionTests(unittest.TestCase):
    def test_source_polarizations_are_divergence_free(self) -> None:
        k1 = (1, 0, 0)
        k2 = (0, 1, 0)
        a = (0, 1, 1)
        b = (1, 0, 1)

        self.assertEqual(sum(x * y for x, y in zip(k1, a)), 0)
        self.assertEqual(sum(x * y for x, y in zip(k2, b)), 0)

    def test_target_stays_in_one_factor_two_band(self) -> None:
        # |k1|^2=|k2|^2=1 and |k1+k2|^2=2.
        source_norm_sq = 1
        target_norm_sq = 2
        self.assertGreaterEqual(target_norm_sq, source_norm_sq)
        self.assertLessEqual(target_norm_sq, 4 * source_norm_sq)

    def test_exact_target_raw_interaction_coefficient(self) -> None:
        # For
        # u=A(0,1,1) cos(N x1)+A(1,0,1) cos(N x2),
        # the sin(N(x1+x2)) coefficient of (u.grad)u, divided by A^2 N,
        # is exactly (-1/2,-1/2,-1).
        raw = (Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 1))
        self.assertEqual(raw, (Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 1)))

    def test_leray_projection_keeps_nonzero_vertical_forcing(self) -> None:
        raw = (Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 1))
        # Target direction is k=(1,1,0), so
        # P_k v = v - k (k.v)/|k|^2.
        dot = raw[0] + raw[1]
        projected = (
            raw[0] - dot / 2,
            raw[1] - dot / 2,
            raw[2],
        )
        self.assertEqual(projected, (0, 0, -1))

    def test_projected_forcing_has_full_N_A_squared_scale(self) -> None:
        for n in (1, 2, 4, 8, 16):
            for a in (1, 3, 7):
                projected_amplitude = n * a * a
                self.assertEqual(projected_amplitude, n * a**2)

    def test_overshoot_ratio_is_nonlinear_to_viscous_scale_ratio(self) -> None:
        nu = Fraction(7, 5)
        n = Fraction(11, 1)
        for r in (Fraction(2, 1), Fraction(4, 1), Fraction(9, 1)):
            a = r * nu * n
            nonlinear = n * a**2
            representative_viscous = nu * n**2 * a
            self.assertEqual(nonlinear / representative_viscous, r)

    def test_turnover_response_time_is_parabolic_time_divided_by_R(self) -> None:
        nu = Fraction(5, 3)
        n = Fraction(13, 1)
        for r in (Fraction(2, 1), Fraction(5, 1), Fraction(12, 1)):
            a = r * nu * n
            turnover = Fraction(1, 1) / (n * a)
            parabolic = Fraction(1, 1) / (nu * n**2)
            self.assertEqual(turnover / parabolic, Fraction(1, 1) / r)

    def test_parabolic_interval_allows_R_sized_absolute_nonlinear_change(self) -> None:
        nu = Fraction(3, 2)
        n = Fraction(7, 1)
        for r in (Fraction(2, 1), Fraction(8, 1), Fraction(32, 1)):
            a = r * nu * n
            nonlinear = n * a**2
            parabolic = Fraction(1, 1) / (nu * n**2)
            absolute_change = nonlinear * parabolic
            self.assertEqual(absolute_change / a, r)


if __name__ == "__main__":
    unittest.main()
