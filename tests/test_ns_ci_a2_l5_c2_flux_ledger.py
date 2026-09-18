from fractions import Fraction
import unittest


class NSCIA2L5C2FluxLedgerTests(unittest.TestCase):
    def test_episode_scaling(self) -> None:
        for n in range(1, 8):
            R = Fraction(2**n, 1)
            lam = R**4
            energy = R**2 / lam
            duration = 1 / (R * lam**2)
            self.assertEqual(energy, R**-2)
            self.assertEqual(duration, R**-9)

    def test_a2_charge_is_inverse_overshoot(self) -> None:
        for n in range(1, 8):
            R = Fraction(2**n, 1)
            lam = R**4
            duration = 1 / (R * lam**2)
            self.assertEqual(lam**2 * duration, 1 / R)

    def test_dissipation_charge_is_cubic_inverse(self) -> None:
        for n in range(1, 8):
            R = Fraction(2**n, 1)
            lam = R**4
            energy = R**2 / lam
            duration = 1 / (R * lam**2)
            dissipation_charge = lam**2 * energy * duration
            self.assertEqual(dissipation_charge, R**-3)

    def test_energy_variation_is_turnover_scale(self) -> None:
        for n in range(1, 8):
            R = Fraction(2**n, 1)
            lam = R**4
            amplitude = R * lam
            energy = R**2 / lam
            duration = 1 / (R * lam**2)
            entry_rate = energy / duration
            turnover_energy_rate = lam * amplitude * energy
            self.assertEqual(entry_rate, turnover_energy_rate)

    def test_absolute_boundary_flux_scale_is_summable(self) -> None:
        # Variation part is O(E)=R^-2; dissipation adds R^-3.
        total = Fraction(0, 1)
        for n in range(1, 20):
            R = Fraction(2**n, 1)
            total += R**-2 + R**-3
        self.assertLess(total, 1)

    def test_all_edge_absolute_flux_is_still_summable(self) -> None:
        # q_n=4n edges, each carrying the same episode flux.
        total = Fraction(0, 1)
        for n in range(1, 20):
            R = Fraction(2**n, 1)
            q = 4 * n
            total += q * (R**-2 + R**-3)
        self.assertLess(total, 10)

    def test_overshoot_charge_is_order_one_per_episode(self) -> None:
        c0 = Fraction(1, 4)
        for n in range(1, 8):
            R = Fraction(2**n, 1)
            lam = R**4
            duration = 1 / (R * lam**2)
            omega = (R - c0) * lam**2
            charge = omega * duration
            self.assertEqual(charge, 1 - c0 / R)
            self.assertGreater(charge, Fraction(3, 4))

    def test_omega_partial_sums_diverge_linearly(self) -> None:
        c0 = Fraction(1, 4)
        charges = []
        for n in range(1, 20):
            R = Fraction(2**n, 1)
            charges.append(1 - c0 / R)
        self.assertGreater(sum(charges), 18)

    def test_frequency_weighted_flux_is_not_selected_budget(self) -> None:
        # lambda * E = R^2 for lambda=R^4 and E=R^-2.
        values = []
        for n in range(1, 8):
            R = Fraction(2**n, 1)
            lam = R**4
            energy = R**-2
            values.append(lam * energy)
            self.assertEqual(values[-1], R**2)
        self.assertTrue(all(b > a for a, b in zip(values, values[1:])))


if __name__ == "__main__":
    unittest.main()
