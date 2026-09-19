import math
import unittest


class NSCIA2L5C2IntrinsicDirectionCompressionCostTests(unittest.TestCase):
    def test_factorization_gauge_leaves_v_unchanged(self):
        beta = 2.0
        b_profile = 0.3
        c = 7.0
        self.assertAlmostEqual(beta * b_profile, (c * beta) * (b_profile / c))

    def test_l541_raw_product_is_gauge_dependent(self):
        d_b = 5.0
        a_beta = 3.0
        c = 4.0
        old = math.sqrt(d_b * a_beta)
        new = math.sqrt(d_b * (c * c * a_beta))
        self.assertAlmostEqual(new, c * old)

    def test_time_local_mixed_product_is_gauge_invariant(self):
        d_b_profile = 2.5
        a_beta = 6.0
        c = 3.0
        old = math.sqrt(d_b_profile * a_beta)
        new = math.sqrt((d_b_profile / (c * c)) * (c * c * a_beta))
        self.assertAlmostEqual(new, old)

    def test_one_sided_compression_bound(self):
        k = 1.25
        negative_variation = 0.04
        bound = math.exp(k) * negative_variation / k
        self.assertGreater(bound, 0.0)
        self.assertAlmostEqual(bound, math.exp(1.25) * 0.04 / 1.25)

    def test_periodic_positive_negative_variation_match(self):
        # v_Y = -cos(Y) on a normalized dense grid.
        n = 200000
        dy = 2.0 * math.pi / n
        pos = 0.0
        neg = 0.0
        total = 0.0
        for j in range(n):
            y = (j + 0.5) * dy
            strain = -math.cos(y)
            pos += max(strain, 0.0) * dy
            neg += max(-strain, 0.0) * dy
            total += abs(strain) * dy
        self.assertAlmostEqual(pos, neg, places=8)
        self.assertAlmostEqual(pos, total / 2.0, places=8)

    def test_compression_separator_has_zero_signed_mean(self):
        n = 100000
        dy = 2.0 * math.pi / n
        kappa = 3.0
        s_total = 2.0
        signed = 0.0
        for j in range(n):
            y = (j + 0.5) * dy
            signed += (-(kappa / s_total) * math.cos(y)) * dy
        self.assertAlmostEqual(signed, 0.0, places=10)

    def test_compression_separator_still_compresses_fixed_label(self):
        kappa = 3.0
        s_total = 2.0
        final_j = math.exp(-kappa * s_total / s_total)
        self.assertAlmostEqual(final_j, math.exp(-kappa))
        self.assertLess(final_j, 1.0)

    def test_scope_is_not_a2_closure(self):
        result = "intrinsic_negative_direction_variation"
        self.assertNotEqual(result, "A2_proved")
        self.assertNotEqual(result, "whole_space_compression_bound")


if __name__ == "__main__":
    unittest.main()
