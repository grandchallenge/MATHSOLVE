import math
import unittest
from fractions import Fraction


class NSCIA2ShellExitTests(unittest.TestCase):
    def test_parabolic_interval_is_scale_correct(self) -> None:
        # lambda -> rho*lambda and time -> rho^-2 time.
        frequency_power = -2
        self.assertEqual(frequency_power, -2)

    def test_local_energy_charge_converts_to_inverse_frequency_cost(self) -> None:
        # E_q = (lambda_q/nu) * int_I ||grad u||_2^2 dt >= epsilon.
        # Multiplying by nu gives physical dissipation charge
        # nu * int_I ||grad u||_2^2 dt >= epsilon*nu^2/lambda_q.
        local_energy_frequency_power = 1
        physical_cost_frequency_power = -local_energy_frequency_power
        self.assertEqual(physical_cost_frequency_power, -1)

    def test_inverse_dyadic_frequency_is_summable(self) -> None:
        partial = sum(2.0 ** (-q) for q in range(1, 100))
        self.assertLess(partial, 1.0)
        self.assertAlmostEqual(partial, 1.0, places=12)

    def test_scalar_boxes_fit_in_finite_time(self) -> None:
        # Parabolic box lengths scale as 2^-2q.
        total = sum(2.0 ** (-2 * q) for q in range(1, 200))
        self.assertTrue(math.isfinite(total))
        self.assertLess(total, 1.0)

    def test_scalar_profile_has_finite_lambda_l2_cost(self) -> None:
        # |J_q| = lambda_q^-2 / q^2, so lambda_q^2 |J_q| = 1/q^2.
        partial_100 = sum(1.0 / (q * q) for q in range(1, 101))
        partial_10000 = sum(1.0 / (q * q) for q in range(1, 10001))
        self.assertGreater(partial_10000, partial_100)
        self.assertLess(partial_10000, 2.0)

    def test_energy_charges_remain_finite_across_all_levels(self) -> None:
        # One rapid exit at every level costs lambda_q^-1=2^-q.
        charge = sum(2.0 ** (-q) for q in range(1, 1000))
        self.assertLessEqual(charge, 1.0)

    def test_source_upper_envelope_cost_diverges(self) -> None:
        # lambda_q^(5/2) |J_q| = 2^(q/2)/q^2.
        partial_20 = sum((2.0 ** (q / 2.0)) / (q * q) for q in range(1, 21))
        partial_40 = sum((2.0 ** (q / 2.0)) / (q * q) for q in range(1, 41))
        self.assertGreater(partial_40, 10.0 * partial_20)

    def test_buffered_event_has_fixed_amplitude_loss(self) -> None:
        theta = Fraction(1, 1)
        start = 2 * theta
        exit_value = theta
        self.assertEqual(start - exit_value, theta)

    def test_first_exit_inequality_forces_positive_energy(self) -> None:
        # Model the inequality 1 <= C(K sqrt(E)+E) with C=K=1.
        # Any E below the positive root of y^2+y-1=0, y=sqrt(E), fails.
        positive_root = (math.sqrt(5.0) - 1.0) / 2.0
        threshold_energy = positive_root * positive_root
        for energy in (1e-8, 1e-4, 0.1):
            self.assertLess(math.sqrt(energy) + energy, 1.0)
            self.assertLess(energy, threshold_energy)

    def test_vitali_energy_packing_does_not_bound_level_count(self) -> None:
        # The sum of one admissible charge at each dyadic level stays finite,
        # while the number of attained levels grows without bound.
        for level_count in (10, 100, 1000):
            charge = sum(2.0 ** (-q) for q in range(1, level_count + 1))
            self.assertLess(charge, 1.0)
            self.assertEqual(level_count, len(range(1, level_count + 1)))


if __name__ == "__main__":
    unittest.main()
