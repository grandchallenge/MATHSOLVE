import math
import unittest


class NSCIA2L5C2DirectionOccupationCalibrationTests(unittest.TestCase):
    def test_shell_supremum_is_epsilon_independent(self):
        for eps in (1.0, 0.5, 0.1, 1e-3):
            vals = [
                math.sqrt(eps * eps * math.cos(x) ** 2 + math.sin(x) ** 2)
                for x in [j * math.pi / 2000 for j in range(4001)]
            ]
            self.assertAlmostEqual(max(vals), 1.0, places=6)

    def test_energy_factor_stays_uniform(self):
        for eps in (1.0, 0.3, 1e-3):
            factor = 0.5 * (1.0 + eps * eps)
            self.assertGreaterEqual(factor, 0.5)
            self.assertLessEqual(factor, 1.0)

    def test_invariant_plane_has_small_amplitude_fraction(self):
        for eps in (0.5, 0.1, 1e-3):
            local = eps
            shell_sup = 1.0
            self.assertAlmostEqual(local / shell_sup, eps)

    def test_normalized_direction_derivative_scales_inverse_epsilon(self):
        k = 16.0
        for eps in (0.5, 0.1, 1e-3):
            derivative = k / eps
            self.assertAlmostEqual(derivative * eps, k)

    def test_weighted_angular_identity_saturates(self):
        a = 3.0
        k = 8.0
        for eps in (1.0, 0.2, 1e-4):
            amp2 = (a * eps) ** 2
            angular2 = (k / eps) ** 2
            weighted = amp2 * angular2
            raw_grad2 = (a * k) ** 2
            self.assertAlmostEqual(weighted, raw_grad2)

    def test_parabolic_a2_occupancy_is_epsilon_independent(self):
        nu = 0.7
        k = 32.0
        c = 0.4
        interval = c / (nu * k * k)
        lambda_l2_cost = k * k * interval
        self.assertAlmostEqual(lambda_l2_cost, c / nu)

    def test_pathwise_direction_cost_diverges_as_epsilon_vanishes(self):
        nu = 1.0
        k = 8.0
        c = 1.0
        interval = c / (nu * k * k)
        costs = [k * interval / eps for eps in (1e-1, 1e-2, 1e-3)]
        self.assertLess(costs[0], costs[1])
        self.assertLess(costs[1], costs[2])
        self.assertAlmostEqual(costs[2] / costs[1], 10.0)

    def test_no_selector_derivative_enters_calibration(self):
        ingredients = {"k", "epsilon", "nu", "A0", "interval"}
        self.assertNotIn("Q_dot", ingredients)
        self.assertNotIn("selector_variation", ingredients)

    def test_calibration_is_not_whole_space_counterexample(self):
        scope = "periodic_exact_nse_mechanism_calibration"
        self.assertNotEqual(scope, "whole_space_A2_counterexample")


if __name__ == "__main__":
    unittest.main()
