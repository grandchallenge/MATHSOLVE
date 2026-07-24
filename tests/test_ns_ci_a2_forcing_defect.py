import math
import unittest
from fractions import Fraction


class NSCIA2ForcingDefectTests(unittest.TestCase):
    def test_low_mode_lipschitz_energy_cost(self) -> None:
        # G_q <= lambda_q^(3/2) ||grad u||_2.
        low_mode_frequency_power = Fraction(3, 2)
        parabolic_interval_power = Fraction(-2, 1)
        holder_gain = parabolic_interval_power / 2
        residual_power = low_mode_frequency_power + holder_gain
        self.assertEqual(residual_power, Fraction(1, 2))

    def test_high_high_local_mass_is_scale_neutral(self) -> None:
        # Output L1->Linf plus derivative costs lambda_q^4.
        # The high-frequency energy tail contributes lambda_q^-2.
        # Normalizing by the threshold nu*lambda_q leaves lambda_q^1,
        # which pairs with a parabolic dissipation mass scaling lambda_q^-1.
        output_cost = 4
        energy_tail_gain = -2
        threshold_normalization = -1
        self.assertEqual(
            output_cost + energy_tail_gain + threshold_normalization,
            1,
        )

    def test_original_and_stricter_thresholds_are_distinct(self) -> None:
        eta = Fraction(1, 2)
        packet_ratio = Fraction(3, 4)
        original_threshold = Fraction(1, 1)
        self.assertGreater(packet_ratio, eta)
        self.assertLess(packet_ratio, original_threshold)

    def test_packet_model_has_finite_total_time(self) -> None:
        total = sum((2.0 ** (-2 * k)) / k for k in range(1, 200))
        self.assertTrue(math.isfinite(total))
        self.assertLess(total, 1.0)

    def test_packet_model_stricter_l2_cost_diverges(self) -> None:
        # lambda_k^2 * |I_k| = 1/k.
        partial_100 = sum(1.0 / k for k in range(1, 101))
        partial_10000 = sum(1.0 / k for k in range(1, 10001))
        self.assertGreater(partial_10000, partial_100)
        self.assertGreater(partial_10000, 9.0)

    def test_packet_model_dissipation_budget_converges(self) -> None:
        # |I_k| * lambda_k^2 * ||u_k||_2^2 scales as 2^-k / k.
        partial_20 = sum((2.0 ** (-k)) / k for k in range(1, 21))
        partial_200 = sum((2.0 ** (-k)) / k for k in range(1, 201))
        self.assertAlmostEqual(partial_20, partial_200, places=6)
        self.assertLess(partial_200, 1.0)

    def test_packet_model_uniform_energy_bound(self) -> None:
        # ||u_k||_2^2 scales as lambda_k^-1=2^-k.
        energies = [2.0 ** (-k) for k in range(1, 100)]
        self.assertLessEqual(max(energies), 0.5)
        self.assertGreater(min(energies), 0.0)

    def test_transport_gain_does_not_meet_parabolic_boundary(self) -> None:
        # After transport cancellation, the effective forcing pair may be
        # viewed as alpha=5/2 with r=2, leaving a half-power deficit:
        # alpha+2/r = 7/2 > 3.
        alpha = Fraction(5, 2)
        r = Fraction(2, 1)
        total = alpha + Fraction(2, 1) / r
        self.assertEqual(total, Fraction(7, 2))
        self.assertGreater(total, 3)


if __name__ == "__main__":
    unittest.main()
