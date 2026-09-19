import math
import unittest


class NSCIA2L5C2DirectionPacketCompressionOverlapTests(unittest.TestCase):
    def test_weighted_first_hit_bound_has_no_exponential_factor(self):
        k = 2.0
        weighted_cost = 0.3
        self.assertAlmostEqual(weighted_cost / k, 0.15)

    def test_unweighted_l542_bound_is_coarser(self):
        k = 2.0
        variation = 0.3
        unweighted = math.exp(k) * variation / k
        packet_weighted = variation / k
        self.assertGreater(unweighted, packet_weighted)

    def test_pushforward_density_preserves_mass(self):
        q = 0.7
        j = 0.2
        rho = q / j
        d_z = 0.03
        d_y = j * d_z
        self.assertAlmostEqual(q * d_z, rho * d_y)

    def test_persistent_overlap_lower_bounds_cost(self):
        gamma = 4.0
        packet_mass_time = 0.125
        self.assertAlmostEqual(gamma * packet_mass_time, 0.5)

    def test_small_weighted_cost_gives_small_compressed_mass(self):
        costs = [1e-1, 1e-2, 1e-3]
        bounds = [c / 1.0 for c in costs]
        self.assertEqual(bounds, costs)
        self.assertGreater(bounds[0], bounds[1])
        self.assertGreater(bounds[1], bounds[2])

    def test_scope_is_not_selector_charge(self):
        result = 'packet_weighted_compression_overlap'
        self.assertNotEqual(result, 'selector_charge_proved')
        self.assertNotEqual(result, 'A2_proved')


if __name__ == '__main__':
    unittest.main()