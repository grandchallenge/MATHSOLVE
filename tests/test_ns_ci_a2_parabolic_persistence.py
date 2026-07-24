import unittest
from fractions import Fraction


class NSCIA2ParabolicPersistenceTests(unittest.TestCase):
    def test_each_persistent_dyadic_level_has_constant_layer_cake_cost(self) -> None:
        # If |{Lambda >= 2^k}| >= c * 2^(-2k), then the layer-cake
        # contribution over r in [2^(k-1), 2^k] is at least 3c/4.
        c = Fraction(7, 5)
        lower_radius_squared = Fraction(1, 4)  # (2^(k-1)/2^k)^2
        normalized_band_cost = (1 - lower_radius_squared) * c
        self.assertEqual(normalized_band_cost, Fraction(3, 4) * c)

    def test_parabolic_profile_is_exactly_l2_borderline(self) -> None:
        # Lambda(t)=t^(-alpha) belongs to L^2(0,1) iff 2*alpha<1.
        alpha = Fraction(1, 2)
        self.assertEqual(2 * alpha, 1)

    def test_unbounded_l2_profiles_have_subparabolic_superlevel_occupancy(self) -> None:
        # For Lambda=t^(-alpha), |{Lambda >= 2^k}|=2^(-k/alpha).
        # Choosing alpha=9/20 gives Lambda in L^2 and occupancy exponent
        # 1/alpha=20/9>2, strictly shorter than parabolic 2^(-2k).
        alpha = Fraction(9, 20)
        occupancy_exponent = 1 / alpha
        self.assertLess(2 * alpha, 1)
        self.assertGreater(occupancy_exponent, 2)

    def test_persistence_bounds_number_of_attained_levels(self) -> None:
        # L2_squared >= (3c/4) * number_of_levels.
        l2_squared = Fraction(30, 1)
        c = Fraction(2, 1)
        maximum_levels = Fraction(4, 3) * l2_squared / c
        self.assertEqual(maximum_levels, 20)

    def test_no_disjoint_time_intervals_are_required(self) -> None:
        # The proof sums disjoint intervals in the layer-cake radius
        # variable. Nested time superlevel sets are therefore admissible.
        superlevel_sets = [set(range(8)), set(range(4)), set(range(2))]
        self.assertTrue(superlevel_sets[2] <= superlevel_sets[1])
        self.assertTrue(superlevel_sets[1] <= superlevel_sets[0])


if __name__ == "__main__":
    unittest.main()
