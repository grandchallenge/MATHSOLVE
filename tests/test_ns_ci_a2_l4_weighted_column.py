import math
import unittest
from fractions import Fraction


class NSCIA2L4WeightedColumnTests(unittest.TestCase):
    def test_dimensionless_geometric_row_sum_is_uniform(self) -> None:
        for q in (0, 1, 5, 20, 100):
            row_sum = sum(2.0 ** (-2 * (q - p)) for p in range(q + 1))
            self.assertLessEqual(row_sum, 4.0 / 3.0)

    def test_dimensionless_geometric_column_sum_is_uniform(self) -> None:
        for p in (0, 1, 5, 20):
            truncated = sum(2.0 ** (-2 * (q - p)) for q in range(p, p + 100))
            self.assertAlmostEqual(truncated, 4.0 / 3.0, places=12)

    def test_weighted_column_retains_frequency_factor(self) -> None:
        for p in (0, 5, 10, 20):
            lambda_p = 2.0**p
            weighted = sum(
                lambda_p * 2.0 ** (-2 * (q - p))
                for q in range(p, p + 100)
            )
            self.assertAlmostEqual(weighted / lambda_p, 4.0 / 3.0, places=12)

    def test_pointwise_energy_cap_recovers_lambda_cubed(self) -> None:
        # Sum_{p<=Q} 2^{-2(Q-p)} lambda_p^3
        # = lambda_Q^3 Sum_j 2^{-5j}.
        for q in (1, 5, 10, 20):
            lambda_q = 2.0**q
            shell_sum = sum(
                2.0 ** (-2 * (q - p)) * (2.0**p) ** 3
                for p in range(q + 1)
            )
            normalized = shell_sum / (lambda_q**3)
            self.assertLessEqual(normalized, 32.0 / 31.0)

    def test_packet_box_lambda_l2_cost_converges(self) -> None:
        # tau_q = lambda_q^{-5/2}/(q+1), so lambda_q^2 tau_q
        # = lambda_q^{-1/2}/(q+1).
        partial_50 = sum(2.0 ** (-q / 2.0) / (q + 1) for q in range(50))
        partial_500 = sum(2.0 ** (-q / 2.0) / (q + 1) for q in range(500))
        self.assertTrue(math.isfinite(partial_500))
        self.assertLess(partial_500, 3.0)
        self.assertGreaterEqual(partial_500, partial_50)

    def test_packet_box_total_dissipation_cost_converges(self) -> None:
        # D_q is proportional to lambda_q^2, so D_q tau_q has the
        # same summability exponent as Lambda^2 tau_q.
        partial = sum(2.0 ** (-q / 2.0) / (q + 1) for q in range(1000))
        self.assertLess(partial, 3.0)

    def test_packet_box_weighted_dissipation_diverges(self) -> None:
        # lambda_q D_q tau_q is proportional to lambda_q^{1/2}/(q+1).
        partial_20 = sum(2.0 ** (q / 2.0) / (q + 1) for q in range(20))
        partial_40 = sum(2.0 ** (q / 2.0) / (q + 1) for q in range(40))
        self.assertGreater(partial_40, 100.0 * partial_20)

    def test_packet_box_low_mode_integral_is_harmonic(self) -> None:
        # f_q is proportional to lambda_q^{5/2}; multiplying by tau_q
        # leaves exactly 1/(q+1).
        partial_100 = sum(1.0 / (q + 1) for q in range(100))
        partial_10000 = sum(1.0 / (q + 1) for q in range(10000))
        self.assertGreater(partial_10000, partial_100)
        self.assertGreater(partial_10000, 9.0)

    def test_threshold_ratio_grows_at_high_frequency(self) -> None:
        # For an L2-normalized Bernstein-saturating packet,
        # lambda_q^{-1} ||u_q||_infinity scales as lambda_q^{1/2}.
        ratios = [2.0 ** (q / 2.0) for q in (0, 4, 8, 12)]
        self.assertEqual(ratios, sorted(ratios))
        self.assertGreater(ratios[-1], ratios[0])

    def test_diagonal_weight_must_not_decay_for_pointwise_domination(self) -> None:
        # Squared cutoff-shell domination compares
        # f_q^2 ~ nu^{-1} lambda_q^3 D_q
        # with nu^{-1} Lambda^2 K_qq lambda_q D_q.
        # Since Lambda=lambda_q, the powers match only with K_qq~1.
        source_power = Fraction(3, 1)
        weighted_power = Fraction(2, 1) + Fraction(1, 1)
        self.assertEqual(source_power, weighted_power)

    def test_previous_exit_charge_can_be_added_summably(self) -> None:
        # The physical rapid-exit charge has weight lambda_q^{-1}=2^{-q}.
        charge = sum(2.0 ** (-q) for q in range(1000))
        self.assertAlmostEqual(charge, 2.0, places=12)


if __name__ == "__main__":
    unittest.main()
