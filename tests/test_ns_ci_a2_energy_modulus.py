import unittest
from fractions import Fraction


class NSCIA2EnergyModulusTests(unittest.TestCase):
    def test_energy_interpolation_time_exponent(self) -> None:
        # ||u||_4 <= ||u||_2^(1/4) ||grad u||_2^(3/4).
        # Choosing p makes (3/4)p=2, hence p=8/3.
        gradient_power = Fraction(3, 4)
        time_exponent = Fraction(2, 1) / gradient_power
        self.assertEqual(time_exponent, Fraction(8, 3))

        # Squaring u gives the forcing coefficient ||u||_4^2 in L^(4/3)_t.
        forcing_time_exponent = time_exponent / 2
        self.assertEqual(forcing_time_exponent, Fraction(4, 3))

    def test_localized_forcing_frequency_cost(self) -> None:
        derivative_cost = Fraction(1, 1)
        bernstein_l2_to_linf_cost = Fraction(3, 2)
        self.assertEqual(
            derivative_cost + bernstein_l2_to_linf_cost,
            Fraction(5, 2),
        )

    def test_holder_interval_gain(self) -> None:
        r = Fraction(4, 3)
        interval_power = 1 - Fraction(1, 1) / r
        self.assertEqual(interval_power, Fraction(1, 4))

    def test_energy_class_dwell_exponent_is_six(self) -> None:
        # lambda^(5/2) delta^(1/4) must be no larger than the
        # threshold scale lambda^1. Thus delta <= lambda^-6.
        forcing_frequency_power = Fraction(5, 2)
        threshold_power = Fraction(1, 1)
        interval_power = Fraction(1, 4)
        dwell_exponent = (
            forcing_frequency_power - threshold_power
        ) / interval_power
        self.assertEqual(dwell_exponent, Fraction(6, 1))

    def test_complete_dwell_bound_is_scale_covariant(self) -> None:
        # U scales as rho^-1/2, so U^-8 contributes rho^4.
        # lambda^-6 contributes rho^-6. The product contributes rho^-2.
        energy_scaling = Fraction(-1, 2)
        energy_factor_power = -8
        frequency_factor_power = -6
        total_scaling = energy_scaling * energy_factor_power + frequency_factor_power
        self.assertEqual(total_scaling, Fraction(-2, 1))

    def test_subparabolic_layer_cake_cost_is_summable(self) -> None:
        threshold_square_power = 2
        dwell_power = -6
        cost_power = threshold_square_power + dwell_power
        self.assertEqual(cost_power, -4)
        self.assertLess(cost_power, 0)

    def test_parabolic_forcing_condition(self) -> None:
        # A forcing estimate with frequency cost lambda^alpha and time
        # exponent r reaches a lambda^-2 interval only if alpha+2/r<=3.
        energy_alpha = Fraction(5, 2)
        energy_r = Fraction(4, 3)
        energy_total = energy_alpha + Fraction(2, 1) / energy_r
        self.assertEqual(energy_total, Fraction(4, 1))
        self.assertGreater(energy_total, 3)

        temporal_upgrade_r = Fraction(4, 1)
        self.assertEqual(
            energy_alpha + Fraction(2, 1) / temporal_upgrade_r,
            Fraction(3, 1),
        )

        spatial_upgrade_alpha = Fraction(3, 2)
        self.assertEqual(
            spatial_upgrade_alpha + Fraction(2, 1) / energy_r,
            Fraction(3, 1),
        )

    def test_threshold_fraction_does_not_preserve_original_threshold(self) -> None:
        c0 = Fraction(1, 1)
        eta = Fraction(1, 2)
        self.assertLess(eta * c0, c0)

        # A factor-two buffered event can lose one half and still meet c0.
        buffered_threshold = 2 * c0
        self.assertEqual(eta * buffered_threshold, c0)


if __name__ == "__main__":
    unittest.main()
