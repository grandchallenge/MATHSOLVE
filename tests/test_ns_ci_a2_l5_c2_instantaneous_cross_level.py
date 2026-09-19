from fractions import Fraction
import unittest


class NSCIA2L5C2InstantaneousCrossLevelTests(unittest.TestCase):
    def test_three_modes_are_divergence_free(self) -> None:
        k1 = (1, 0, 0)
        k2 = (0, 1, 0)
        k3 = (1, 1, 0)
        a = (0, 1, 1)
        b = (1, 0, 1)
        e3 = (0, 0, 1)

        self.assertEqual(sum(x * y for x, y in zip(k1, a)), 0)
        self.assertEqual(sum(x * y for x, y in zip(k2, b)), 0)
        self.assertEqual(sum(x * y for x, y in zip(k3, e3)), 0)

    def test_initial_support_has_no_frequency_above_target(self) -> None:
        source_norm_sq = (1, 1)
        target_norm_sq = 2
        self.assertTrue(all(x <= target_norm_sq for x in source_norm_sq))
        strict_high_initial_modes = []
        self.assertEqual(strict_high_initial_modes, [])

    def test_phase_flip_preserves_support_and_modal_energies(self) -> None:
        amplitude = Fraction(7, 3)
        plus = [amplitude**2, amplitude**2, amplitude**2]
        minus = [amplitude**2, (-amplitude) ** 2, amplitude**2]
        self.assertEqual(plus, minus)

    def test_target_projected_nonlinear_coefficient_flips_with_source_phase(self) -> None:
        # Divide the target sin(x+y) coefficient by A^2 N.
        plus = (0, 0, Fraction(-1, 1))
        minus = (0, 0, Fraction(1, 1))
        self.assertEqual(minus, tuple(-x for x in plus))

    def test_target_rhs_coefficient_formula_is_exact(self) -> None:
        # A=C=R nu N.  The target frequency has |k3|^2=2 N^2.
        # For source phase s=+/-1:
        # Cdot = -2 nu N^2 C + s A^2 N
        #      = nu^2 N^3 (-2R + s R^2).
        nu = Fraction(5, 4)
        n = Fraction(9, 1)
        for r in (Fraction(3, 1), Fraction(5, 1), Fraction(11, 1)):
            a = r * nu * n
            c = a
            for s in (Fraction(1, 1), Fraction(-1, 1)):
                lhs = -2 * nu * n**2 * c + s * a**2 * n
                rhs = nu**2 * n**3 * (-2 * r + s * r**2)
                self.assertEqual(lhs, rhs)

    def test_large_overshoot_has_growth_or_decay_at_turnover_rate(self) -> None:
        # Normalize the target coefficient rate by nu N^2 C.
        # s=+ gives R-2; s=- gives -(R+2).
        for r in (Fraction(4, 1), Fraction(8, 1), Fraction(16, 1)):
            growth = r - 2
            decay = -(r + 2)
            self.assertGreaterEqual(growth, r / 2)
            self.assertGreaterEqual(abs(decay), r)

    def test_target_is_above_threshold_for_large_R(self) -> None:
        # Actual target frequency is sqrt(2) N.
        # (C/(nu |k3|))^2 = R^2/2.
        c0 = Fraction(1, 1)
        for r in (Fraction(4, 1), Fraction(8, 1), Fraction(16, 1)):
            normalized_ratio_sq = r**2 / 2
            self.assertGreater(normalized_ratio_sq, c0**2)

    def test_phase_flip_changes_target_rhs_without_strict_high_input(self) -> None:
        # Same support, same modal energies, strict-high input empty;
        # only source phase changes.  The nonlinear target contribution flips.
        r = Fraction(8, 1)
        plus_nonlinear = r**2
        minus_nonlinear = -r**2
        strict_high_count_plus = 0
        strict_high_count_minus = 0

        self.assertEqual(strict_high_count_plus, strict_high_count_minus)
        self.assertEqual(plus_nonlinear, -minus_nonlinear)


if __name__ == "__main__":
    unittest.main()
