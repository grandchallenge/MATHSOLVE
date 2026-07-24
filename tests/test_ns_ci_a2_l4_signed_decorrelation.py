import math
import unittest


class NSCIA2L4SignedDecorrelationTests(unittest.TestCase):
    def test_selector_interval_identity(self) -> None:
        # On an active interval [a,b], e' + d = T gives
        # integral d = integral T + e(a) - e(b).
        integral_transfer = 7.0
        energy_entry = 5.0
        energy_exit = 3.0
        integral_dissipation = integral_transfer + energy_entry - energy_exit
        self.assertEqual(integral_dissipation, 9.0)

    def test_global_transfer_cancellation_does_not_survive_selection(self) -> None:
        transfers = [-11.0, 4.0, 7.0]
        self.assertEqual(sum(transfers), 0.0)
        active_shell = 2
        lambdas = [1.0, 2.0, 4.0]
        selected = lambdas[active_shell] * transfers[active_shell]
        self.assertEqual(selected, 28.0)
        self.assertNotEqual(selected, 0.0)

    def test_occupancy_does_not_control_component_count(self) -> None:
        # A set of fixed total measure can be split into arbitrarily many pieces.
        total_measure = 1.0
        for components in (1, 10, 1000):
            piece_measure = total_measure / components
            reconstructed = components * piece_measure
            self.assertAlmostEqual(reconstructed, total_measure)

    def test_threshold_weighted_entry_cost_is_frequency_independent(self) -> None:
        # Threshold energy floor e_q ~ nu^2 lambda_q^-1 gives
        # lambda_q e_q ~ nu^2.
        nu = 0.3
        for q in (0, 5, 20, 50):
            lambda_q = 2.0**q
            energy_floor = nu**2 / lambda_q
            self.assertAlmostEqual(lambda_q * energy_floor, nu**2)

    def test_nearest_neighbour_flux_conservation(self) -> None:
        # A common flux F along the chain transfers energy from shell 0 to q.
        q = 8
        flux = 3.25
        transfers = [0.0] * (q + 1)
        transfers[0] = -flux
        for p in range(1, q):
            transfers[p] = flux - flux
        transfers[q] = flux
        self.assertAlmostEqual(sum(transfers), 0.0)
        self.assertEqual(transfers[0], -flux)
        self.assertEqual(transfers[q], flux)

    def test_local_flux_shell_balances(self) -> None:
        energy_derivative = -2.0
        dissipation = 5.0
        flux = energy_derivative + dissipation
        self.assertEqual(energy_derivative + dissipation, flux)
        self.assertEqual(flux, 3.0)

    def test_fixture_lambda_l2_and_dissipation_converge(self) -> None:
        # tau_q = lambda_q^-5/2 /(q+1), while both Lambda^2 and D_q
        # contribute lambda_q^2.
        total = sum(2.0 ** (-q / 2.0) / (q + 1) for q in range(1000))
        self.assertTrue(math.isfinite(total))
        self.assertLess(total, 3.0)

    def test_fixture_weighted_active_diagonal_diverges(self) -> None:
        # lambda_q D_q tau_q ~ lambda_q^1/2 /(q+1).
        partial_20 = sum(2.0 ** (q / 2.0) / (q + 1) for q in range(20))
        partial_40 = sum(2.0 ** (q / 2.0) / (q + 1) for q in range(40))
        self.assertGreater(partial_40, 100.0 * partial_20)

    def test_reservoir_loss_is_only_total_dissipation(self) -> None:
        # Smooth ramps return the active-shell energy to zero, so integrated
        # flux equals integrated dissipation rather than energy variation.
        energy_start = 0.0
        energy_end = 0.0
        integral_dissipation = 0.125
        integral_flux = energy_end - energy_start + integral_dissipation
        self.assertAlmostEqual(integral_flux, integral_dissipation)

    def test_strict_high_threshold_excludes_active_shell(self) -> None:
        q = 12
        controlled_shells = list(range(q + 1, q + 5))
        self.assertNotIn(q, controlled_shells)
        self.assertTrue(all(p > q for p in controlled_shells))

    def test_absolute_transfer_destroys_cancellation(self) -> None:
        transfers = [-5.0, 2.0, 3.0]
        self.assertEqual(sum(transfers), 0.0)
        self.assertEqual(sum(abs(value) for value in transfers), 10.0)


if __name__ == "__main__":
    unittest.main()
