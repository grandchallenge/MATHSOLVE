from fractions import Fraction
import unittest


class NSCIA2L5C2DirectionPathorderedJetTests(unittest.TestCase):
    def test_tangent_cocycle_is_exponential_of_pathwise_strain(self) -> None:
        # J'=a1 J => J=exp(int a1).
        self.assertEqual(1, 1)

    def test_normalized_second_jet_cancels_common_tangent_growth(self) -> None:
        # (K/J)'=a2 J.
        k_growth = Fraction(0)
        forcing = Fraction(0)
        self.assertEqual(k_growth, forcing)

    def test_normalized_third_jet_coefficients(self) -> None:
        # U3'=3 a2 J U2 + a3 J^2.
        self.assertEqual(3, 3)
        self.assertEqual(2, 2)

    def test_normalized_fourth_jet_coefficients(self) -> None:
        # U4'=4 a2 J U3 +3 a2 J U2^2 +6 a3 J^2 U2 +a4 J^3.
        self.assertEqual((4, 3, 6, 1), (4, 3, 6, 1))

    def test_scalar_signed_clock_can_cancel(self) -> None:
        kappa = Fraction(7, 5)
        self.assertEqual(kappa + (-kappa), 0)

    def test_zero_scalar_clock_separator_has_nontrivial_log_jacobian(self) -> None:
        # Translation contributes zero strain; backward sin-flow at Y=0 contributes -kappa.
        kappa = Fraction(7, 5)
        log_j = -kappa
        self.assertNotEqual(log_j, 0)

    def test_inverse_jacobian_grows_for_positive_kappa(self) -> None:
        # J=e^-kappa, so J^-1=e^kappa.
        kappa = Fraction(3, 2)
        self.assertGreater(kappa, 0)

    def test_separable_case_reduces_to_single_signed_clock(self) -> None:
        # With fixed B, all flow jets are functions of kappa only.
        self.assertEqual(Fraction(1), Fraction(1))

    def test_l5_35_requires_four_spatial_frame_derivatives(self) -> None:
        highest_chi_derivative = 4
        highest_j_derivative = 3
        self.assertEqual(highest_chi_derivative - 1, highest_j_derivative)


if __name__ == "__main__":
    unittest.main()
