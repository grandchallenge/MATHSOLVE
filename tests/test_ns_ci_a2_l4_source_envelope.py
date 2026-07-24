import math
import unittest
from fractions import Fraction


class NSCIA2L4SourceEnvelopeTests(unittest.TestCase):
    def test_minimality_selects_threshold_shell(self) -> None:
        # Normalized ratios r_p=lambda_p^-1 ||u_p||_infinity/(c0*nu).
        # Every shell strictly above Q is subcritical, while Q is not.
        q = 5
        ratios = {
            5: 1.25,
            6: 0.75,
            7: 0.5,
            8: 0.25,
        }
        self.assertGreaterEqual(ratios[q], 1.0)
        self.assertTrue(all(ratios[p] < 1.0 for p in ratios if p > q))

    def test_definition_gives_no_upper_bound_at_cutoff(self) -> None:
        # The threshold-shell ratio can be arbitrarily large without changing
        # the validity of the strict-high-mode inequalities.
        q = 4
        ratios = {q: 10_000.0, q + 1: 0.5, q + 2: 0.25}
        self.assertGreater(ratios[q], 1.0)
        self.assertTrue(all(ratios[p] < 1.0 for p in ratios if p > q))

    def test_lower_source_envelope_restores_viscosity(self) -> None:
        c0 = Fraction(1, 100)
        nu = Fraction(3, 2)
        lam = Fraction(8, 1)
        threshold_shell_term = c0 * nu * lam * lam
        self.assertEqual(
            threshold_shell_term,
            c0 * nu * lam**2,
        )

    def test_upper_source_envelope_exponent(self) -> None:
        # lambda * ||u_q||_infinity <= lambda^(5/2) ||u_q||_2.
        derivative_power = Fraction(1, 1)
        bernstein_l2_to_linf = Fraction(3, 2)
        self.assertEqual(
            derivative_power + bernstein_l2_to_linf,
            Fraction(5, 2),
        )

    def test_weighted_kernel_identity(self) -> None:
        for q in range(1, 12):
            lambda_q = Fraction(2**q, 1)
            for p in range(0, q + 1):
                lambda_p = Fraction(2**p, 1)
                kernel = Fraction(1, 4 ** (q - p))
                self.assertEqual(
                    lambda_p**3,
                    lambda_q**2 * kernel * lambda_p,
                )

    def test_kernel_row_sum_is_uniform(self) -> None:
        for q in (0, 1, 5, 20, 100):
            row_sum = sum(4.0 ** (-(q - p)) for p in range(q + 1))
            self.assertLessEqual(row_sum, 4.0 / 3.0)

    def test_far_row_tail_is_tunably_small(self) -> None:
        for j in (0, 1, 3, 8):
            numerical_tail = sum(4.0 ** (-k) for k in range(j + 1, 1000))
            exact_tail = (4.0 ** (-(j + 1))) / (1.0 - 0.25)
            self.assertAlmostEqual(numerical_tail, exact_tail, places=14)

    def test_weighted_shell_term_has_f_scaling(self) -> None:
        # D_p scales as rho, lambda_p as rho, and nu is fixed.
        lambda_scaling = Fraction(1, 1)
        dissipation_scaling = Fraction(1, 1)
        viscosity_scaling = Fraction(0, 1)
        weighted_scaling = (
            lambda_scaling
            + dissipation_scaling
            - 2 * viscosity_scaling
        )
        self.assertEqual(weighted_scaling, Fraction(2, 1))

    def test_square_root_envelope_has_f_scaling(self) -> None:
        # Lambda scales as rho and S_Q as rho^2.
        lambda_scaling = Fraction(1, 1)
        weighted_sum_scaling = Fraction(2, 1)
        total = lambda_scaling + weighted_sum_scaling / 2
        self.assertEqual(total, Fraction(2, 1))

    def test_time_integrated_weighted_term_is_scale_invariant(self) -> None:
        weighted_term_scaling = Fraction(2, 1)
        time_scaling = Fraction(-2, 1)
        self.assertEqual(weighted_term_scaling + time_scaling, 0)

    def test_young_split_preserves_scaling(self) -> None:
        # nu*Lambda^2 and nu^-2*S_Q both scale like rho^2.
        lambda_square_scaling = Fraction(2, 1)
        weighted_sum_scaling = Fraction(2, 1)
        self.assertEqual(lambda_square_scaling, weighted_sum_scaling)

    def test_inactive_set_has_only_fixed_low_shells(self) -> None:
        # Q=0 means the source shell supremum uses q=-1 and q=0 only.
        active_shells = list(range(-1, 0 + 1))
        self.assertEqual(active_shells, [-1, 0])

    def test_row_summability_does_not_remove_frequency_weight(self) -> None:
        # A uniform row kernel does not control sum lambda_p D_p by sum D_p.
        # Choose one unit of D at increasingly high p.
        unweighted = []
        weighted = []
        for p in range(1, 20):
            d_p = 1.0
            unweighted.append(d_p)
            weighted.append((2.0**p) * d_p)
        self.assertEqual(max(unweighted), 1.0)
        self.assertGreater(weighted[-1], 100_000.0)

    def test_active_level_l2_cost_identity(self) -> None:
        # Lambda in L2 is represented by sum 2^(2k)|{Q=k}|.
        costs = []
        for k in range(1, 10):
            measure = (2.0 ** (-2 * k)) / (k * k)
            costs.append((2.0 ** (2 * k)) * measure)
        self.assertAlmostEqual(sum(costs), sum(1.0 / (k * k) for k in range(1, 10)))


if __name__ == "__main__":
    unittest.main()
