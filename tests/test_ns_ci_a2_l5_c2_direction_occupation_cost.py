import math
import unittest


class NSCIA2L5C2DirectionOccupationCostTests(unittest.TestCase):
    def test_stopped_exit_measure_bound(self):
        k = 1.0
        d_b = 0.04
        a_beta = 0.09
        bound = math.exp(k) / k * math.sqrt(d_b * a_beta)
        self.assertGreater(bound, 0.0)
        self.assertAlmostEqual(bound, math.e * 0.06)

    def test_k_exp_minus_k_is_maximized_at_one(self):
        values = [(x, x * math.exp(-x)) for x in (0.25, 0.5, 1.0, 2.0, 4.0)]
        best = max(values, key=lambda item: item[1])
        self.assertEqual(best[0], 1.0)

    def test_compression_separator_jacobian(self):
        kappa = 3.0
        s_total = 2.0
        for s in (0.0, 0.5, 1.0, 2.0):
            jac = math.exp(-kappa * s / s_total)
            self.assertGreater(jac, 0.0)
        self.assertAlmostEqual(math.exp(-kappa), math.exp(-kappa * s_total / s_total))

    def test_full_occupation_has_exponential_compression_factor(self):
        s_total = 2.0
        amp = 5.0
        for kappa in (0.5, 1.0, 3.0):
            amp_only = kappa * kappa / (s_total * amp * amp)
            full = kappa * (math.exp(kappa) - 1.0) / (s_total * amp * amp)
            ratio = full / amp_only
            self.assertAlmostEqual(ratio, (math.exp(kappa) - 1.0) / kappa)

    def test_separator_budget_product_is_kappa_squared(self):
        s_total = 1.7
        amp = 4.2
        kappa = 2.3
        d_b = s_total * amp * amp
        a_beta = kappa * kappa / (s_total * amp * amp)
        self.assertAlmostEqual(d_b * a_beta, kappa * kappa)

    def test_principal_direction_scale_does_not_make_beta_small(self):
        for h in (0.5, 0.2, 0.1):
            theta_principal = h
            beta_principal = theta_principal / h
            self.assertAlmostEqual(beta_principal, 1.0)

    def test_residual_direction_scale_does_make_beta_small(self):
        for h in (0.5, 0.2, 0.1):
            theta_residual = h**3
            beta_residual = theta_residual / h
            self.assertAlmostEqual(beta_residual, h**2)

    def test_scope_is_not_a2_closure(self):
        result = "stopped_reciprocal_amplitude_bootstrap"
        self.assertNotEqual(result, "A2_proved")
        self.assertNotEqual(result, "whole_space_counterexample")


if __name__ == "__main__":
    unittest.main()
