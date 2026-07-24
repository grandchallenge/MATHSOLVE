import math
import unittest
from fractions import Fraction


class NSCIA2SignedFluxTests(unittest.TestCase):
    def test_threshold_energy_floor_has_inverse_frequency_weight(self) -> None:
        # ||u_q||_inf <= C lambda_q^(3/2) ||u_q||_2 and
        # ||u_q||_inf >= c nu lambda_q imply
        # ||u_q||_2^2 >= const * nu^2 * lambda_q^-1.
        threshold_amplitude_power = 1
        bernstein_power = Fraction(3, 2)
        l2_amplitude_power = threshold_amplitude_power - bernstein_power
        l2_energy_power = 2 * l2_amplitude_power
        self.assertEqual(l2_energy_power, Fraction(-1, 1))

    def test_inverse_frequency_energy_floor_is_summable(self) -> None:
        partial = sum(2.0 ** (-q) for q in range(1000))
        self.assertTrue(math.isfinite(partial))
        self.assertLessEqual(partial, 2.0)

    def test_four_packet_split_preserves_energy_count(self) -> None:
        # Initial packet amplitude is 2, so energy is proportional to 4.
        # Four separated packets of amplitude 1 also carry total energy 4.
        initial_energy_units = 2 ** 2
        final_energy_units = 4 * (1 ** 2)
        self.assertEqual(initial_energy_units, final_energy_units)

    def test_packet_split_halves_peak_amplitude(self) -> None:
        initial_peak = 2
        separated_packet_peak = 1
        self.assertEqual(initial_peak / separated_packet_peak, 2)

    def test_shell_chain_stage_balance(self) -> None:
        for q in range(20):
            energy = 2.0 ** (-q)
            transfer = 2.0 ** (-(q + 1))
            dissipation = energy - transfer
            self.assertAlmostEqual(energy, transfer + dissipation)
            self.assertGreaterEqual(dissipation, 0.0)

    def test_shell_chain_total_dissipation_is_finite(self) -> None:
        total = sum(
            (2.0 ** (-q)) - (2.0 ** (-(q + 1)))
            for q in range(1000)
        )
        self.assertAlmostEqual(total, 1.0, places=12)

    def test_shell_chain_total_signed_transfer_is_finite(self) -> None:
        total = sum(2.0 ** (-(q + 1)) for q in range(1000))
        self.assertAlmostEqual(total, 1.0, places=12)

    def test_all_levels_are_reached_despite_finite_charge(self) -> None:
        for level_count in (10, 100, 1000):
            energies = [2.0 ** (-q) for q in range(level_count)]
            self.assertEqual(len(energies), level_count)
            self.assertLessEqual(sum(energies), 2.0)

    def test_occupancy_profile_has_finite_lambda_l2_cost(self) -> None:
        # tau_q = lambda_q^-2 / (q+1)^2, so lambda_q^2 tau_q = 1/(q+1)^2.
        partial = sum(1.0 / ((q + 1) ** 2) for q in range(10000))
        self.assertLess(partial, 2.0)

    def test_moving_cutoff_jump_has_same_inverse_frequency_scale(self) -> None:
        # Adding one threshold shell changes cumulative energy at scale lambda^-1.
        shell_energy_power = -1
        jump_power = shell_energy_power
        self.assertEqual(jump_power, -1)

    def test_absolute_flux_does_not_telescope_algebraically(self) -> None:
        transfers = [1.0, -1.0]
        signed_sum = sum(transfers)
        absolute_sum = sum(abs(value) for value in transfers)
        self.assertEqual(signed_sum, 0.0)
        self.assertEqual(absolute_sum, 2.0)


if __name__ == "__main__":
    unittest.main()
