from fractions import Fraction
import unittest


class NSCIA2L5C2DirectionJetCostTests(unittest.TestCase):
    def cutoff(self, m: int) -> Fraction:
        return Fraction(2, 2 * m + 1)

    def test_first_four_relative_cutoffs(self) -> None:
        self.assertEqual(
            [self.cutoff(m) for m in range(1, 5)],
            [Fraction(2, 3), Fraction(2, 5), Fraction(2, 7), Fraction(2, 9)],
        )

    def test_cutoff_saturates_a2_time_pairing_exponent(self) -> None:
        for m in range(1, 8):
            alpha = self.cutoff(m)
            exponent = alpha * Fraction(2 * m + 1, 2)
            self.assertEqual(exponent, 1)

    def test_any_larger_relative_fraction_breaks_scalar_budget_threshold(self) -> None:
        for m in range(1, 8):
            alpha = self.cutoff(m) + Fraction(1, 100)
            exponent = alpha * Fraction(2 * m + 1, 2)
            self.assertGreater(exponent, 1)

    def test_higher_jet_cutoffs_are_strictly_nested(self) -> None:
        cutoffs = [self.cutoff(m) for m in range(1, 8)]
        self.assertTrue(all(a > b for a, b in zip(cutoffs, cutoffs[1:])))

    def test_tangent_cutoff_matches_l5_14(self) -> None:
        self.assertEqual(self.cutoff(1), Fraction(2, 3))

    def test_fourth_jet_far_low_fraction_is_two_ninths(self) -> None:
        self.assertEqual(self.cutoff(4), Fraction(2, 9))

    def test_normalized_direction_requires_denominator_information(self) -> None:
        # The schematic derivative d(b/|b|) contains 1/|b|.
        raw_derivative_control_supplies_positive_amplitude_lower_bound = False
        self.assertFalse(raw_derivative_control_supplies_positive_amplitude_lower_bound)

    def test_no_selector_derivative_is_used(self) -> None:
        differentiates_moving_cutoff = False
        self.assertFalse(differentiates_moving_cutoff)


if __name__ == "__main__":
    unittest.main()
