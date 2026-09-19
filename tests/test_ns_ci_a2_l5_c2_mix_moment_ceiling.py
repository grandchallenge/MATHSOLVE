from fractions import Fraction
import unittest


class NSCIA2L5C2MixMomentCeilingTests(unittest.TestCase):
    def test_moment_barrier_exponent(self) -> None:
        # X_s <= C epsilon^(-2s/3), so ||D^s phi|| <= C epsilon^(-s/3).
        for s in (1, 2, 3, 5, 8):
            squared_exponent = Fraction(2 * s, 3)
            norm_exponent = Fraction(s, 3)
            self.assertEqual(squared_exponent / 2, norm_exponent)

    def test_barrier_terms_have_same_epsilon_scaling(self) -> None:
        # At X_s ~ eps^(-2s/3):
        # source ~ eps^(-(s-1)/3) X_s^(1/2)
        # and damping ~ eps X_s^(1+1/s)
        # both scale as eps^(-(2s-1)/3).
        for s in (1, 2, 3, 5, 8):
            source_exp = Fraction(s - 1, 3) + Fraction(s, 3)
            damping_exp = Fraction(2 * s + 2, 3) - 1
            target = Fraction(2 * s - 1, 3)
            self.assertEqual(source_exp, target)
            self.assertEqual(damping_exp, target)

    def test_threshold_reach_exponent_formula(self) -> None:
        for s in (1, 2, 5, 10):
            alpha = Fraction(2 * (s + 3), 3 * (2 * s + 1))
            shifted = Fraction(1, 3) + Fraction(5, 6 * s + 3)
            self.assertEqual(alpha, shifted)

    def test_s5_reach_is_below_square_root(self) -> None:
        alpha5 = Fraction(16, 33)
        self.assertLess(alpha5, Fraction(1, 2))

    def test_reach_exponents_decrease_to_one_third(self) -> None:
        alphas = [
            Fraction(2 * (s + 3), 3 * (2 * s + 1))
            for s in (1, 2, 3, 5, 8, 13)
        ]
        self.assertTrue(all(b < a for a, b in zip(alphas, alphas[1:])))
        self.assertTrue(all(a > Fraction(1, 3) for a in alphas))

    def test_fixed_turnover_charge_vanishes_at_s5(self) -> None:
        # Charge exponent is 2 alpha - 1 = -1/33.
        alpha5 = Fraction(16, 33)
        self.assertEqual(2 * alpha5 - 1, Fraction(-1, 33))

    def test_subcubic_window_charge_exponent_is_negative(self) -> None:
        # Choose delta=eta/4. For T_R=R^(1/3-eta), the charge exponent is
        # <= (1/3-eta)+(-1/3+2delta) = -eta/2.
        for eta in (Fraction(1, 12), Fraction(1, 6), Fraction(1, 4)):
            delta = eta / 4
            exponent = (
                Fraction(1, 3) - eta
                - Fraction(1, 3)
                + 2 * delta
            )
            self.assertEqual(exponent, -eta / 2)
            self.assertLess(exponent, 0)

    def test_one_chain_shell_count_contributes_half_power(self) -> None:
        # O(L) chain modes in a dyadic annulus -> sqrt count O(L^(1/2)).
        count_power = Fraction(1, 1)
        cauchy_schwarz_power = count_power / 2
        self.assertEqual(cauchy_schwarz_power, Fraction(1, 2))

    def test_threshold_ratio_power_in_L(self) -> None:
        # block L_inf ~ A eps^(-s/3) L^(1/2-s), divide by lambda=N L.
        for s in (2, 5, 8):
            block_power = Fraction(1, 2) - s
            ratio_power = block_power - 1
            self.assertEqual(ratio_power, -Fraction(2 * s + 1, 2))


if __name__ == "__main__":
    unittest.main()
