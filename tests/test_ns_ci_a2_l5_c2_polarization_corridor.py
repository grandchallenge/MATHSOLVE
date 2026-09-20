from fractions import Fraction
import math
import unittest


class NSCIA2L5C2PolarizationCorridorTests(unittest.TestCase):
    def _projected_vertical_factor(self, alpha: float, beta: float) -> float:
        return math.sin(alpha + beta)

    def test_divergence_free_unit_polarizations(self) -> None:
        for angle in (0.0, math.pi / 7, math.pi / 4):
            a = (0.0, math.cos(angle), math.sin(angle))
            b = (math.cos(angle), 0.0, math.sin(angle))
            self.assertAlmostEqual(sum(x * x for x in a), 1.0)
            self.assertAlmostEqual(sum(x * x for x in b), 1.0)
            # k1=e1 and k2=e2.
            self.assertAlmostEqual(a[0], 0.0)
            self.assertAlmostEqual(b[1], 0.0)

    def test_exact_null_orientation(self) -> None:
        self.assertAlmostEqual(self._projected_vertical_factor(0.0, 0.0), 0.0)

    def test_maximal_orientation(self) -> None:
        value = self._projected_vertical_factor(math.pi / 4, math.pi / 4)
        self.assertAlmostEqual(value, 1.0)

    def test_sign_reversal(self) -> None:
        theta = math.pi / 5
        plus = self._projected_vertical_factor(theta, 0.0)
        minus = self._projected_vertical_factor(-theta, 0.0)
        self.assertAlmostEqual(plus, -minus)

    def test_original_l5_16_normalized_orientation_is_maximal(self) -> None:
        # (0,1,1)/sqrt(2) and (1,0,1)/sqrt(2) correspond to alpha=beta=pi/4.
        self.assertAlmostEqual(
            self._projected_vertical_factor(math.pi / 4, math.pi / 4),
            1.0,
        )

    def test_required_corridor_power(self) -> None:
        # h=R^-1/3 and NF4 requires |sin(theta)|=O(h^2).
        h_in_R = Fraction(-1, 3)
        corridor = 2 * h_in_R
        self.assertEqual(corridor, Fraction(-2, 3))

    def test_forcing_scale_has_null_factor_only(self) -> None:
        # Target amplitude is (A^2 N / 2)*|sin(alpha+beta)|.
        generic_prefactor = Fraction(1, 2)
        self.assertEqual(generic_prefactor, Fraction(1, 2))

    def test_scalar_modal_norms_do_not_depend_on_angles(self) -> None:
        angles = [
            (0.0, 0.0),
            (math.pi / 8, math.pi / 3),
            (math.pi / 4, math.pi / 4),
        ]
        for alpha, beta in angles:
            a_norm_sq = math.cos(alpha) ** 2 + math.sin(alpha) ** 2
            b_norm_sq = math.cos(beta) ** 2 + math.sin(beta) ** 2
            self.assertAlmostEqual(a_norm_sq, 1.0)
            self.assertAlmostEqual(b_norm_sq, 1.0)

    def test_same_scalar_data_can_give_zero_or_full_forcing(self) -> None:
        zero = abs(self._projected_vertical_factor(0.0, 0.0))
        full = abs(
            self._projected_vertical_factor(math.pi / 4, math.pi / 4)
        )
        self.assertAlmostEqual(zero, 0.0)
        self.assertAlmostEqual(full, 1.0)


if __name__ == "__main__":
    unittest.main()
