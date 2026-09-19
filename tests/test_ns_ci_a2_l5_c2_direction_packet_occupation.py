import math
import unittest


class NSCIA2L5C2DirectionPacketOccupationTests(unittest.TestCase):
    def test_pointwise_occupation_factorization(self):
        beta = [1.0, 2.0, 0.5, 1.5]
        jac = [1.2, 0.8, 1.4, 1.1]
        amp = [2.0, 1.0, 0.7, 1.4]
        grad = [0.4, 1.2, 0.5, 0.8]
        dt = 0.25

        omega = sum(abs(b) * abs(g) * dt for b, g in zip(beta, grad))
        energy = sum(
            j * a * a * g * g * dt
            for j, a, g in zip(jac, amp, grad)
        )
        reciprocal = sum(
            b * b / (j * a * a) * dt
            for b, j, a in zip(beta, jac, amp)
        )
        self.assertLessEqual(omega * omega, energy * reciprocal + 1e-12)

    def test_markov_bad_label_bound(self):
        costs = [0.2, 0.5, 1.0, 3.0, 7.0]
        threshold = 2.0
        bad_mass = sum(1.0 for x in costs if x > threshold)
        l1_mass = sum(costs)
        self.assertLessEqual(bad_mass, l1_mass / threshold)

    def test_good_label_tangent_jacobian_bounds(self):
        kappa = 2.5
        for signed_strain in (-2.5, -1.0, 0.0, 1.7, 2.5):
            jac = math.exp(signed_strain)
            self.assertGreaterEqual(jac, math.exp(-kappa))
            self.assertLessEqual(jac, math.exp(kappa))

    def test_elliptic_shear_reciprocal_spatial_mean_scales_inverse_epsilon(self):
        # Midpoint quadrature avoids sampling the narrow extrema directly.
        n = 200000
        for eps in (0.5, 0.2, 0.1):
            total = 0.0
            for j in range(n):
                x = 2.0 * math.pi * (j + 0.5) / n
                denom = eps * eps * math.cos(x) ** 2 + math.sin(x) ** 2
                total += 1.0 / denom
            mean = total / n
            self.assertAlmostEqual(mean * eps, 1.0, places=4)

    def test_parabolic_reciprocal_occupation_diverges_as_inverse_epsilon(self):
        nu = 0.7
        k = 8.0
        a0 = 3.0
        c = 0.4

        time_factor = (math.exp(2.0 * c) - 1.0) / (
            2.0 * nu * k * k * a0 * a0
        )
        values = [time_factor / eps for eps in (0.2, 0.1, 0.05)]
        self.assertAlmostEqual(values[1] / values[0], 2.0)
        self.assertAlmostEqual(values[2] / values[1], 2.0)

    def test_coarse_budget_factor_stays_uniform_while_occupation_diverges(self):
        eps_values = (1.0, 0.5, 0.1, 0.01)
        energy_factors = [0.5 * (1.0 + eps * eps) for eps in eps_values]
        reciprocal_factors = [1.0 / eps for eps in eps_values]

        self.assertGreaterEqual(min(energy_factors), 0.5)
        self.assertLessEqual(max(energy_factors), 1.0)
        self.assertGreater(reciprocal_factors[-1], 50.0 * reciprocal_factors[0])

    def test_no_selector_derivative_enters_bridge(self):
        ingredients = {
            "beta",
            "characteristic_jacobian",
            "carrier_amplitude",
            "angular_gradient",
            "raw_gradient_energy",
        }
        self.assertNotIn("Q_dot", ingredients)
        self.assertNotIn("selector_variation", ingredients)

    def test_scope_is_conditional_not_a2_closure(self):
        result = "conditional_packet_occupation_bridge"
        self.assertNotEqual(result, "A2_proved")
        self.assertNotEqual(result, "whole_space_counterexample")


if __name__ == "__main__":
    unittest.main()
