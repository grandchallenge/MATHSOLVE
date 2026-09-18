from fractions import Fraction
import unittest


class NSCIA2L5C2OvershootDynamicsTests(unittest.TestCase):
    def test_four_fifths_is_critical_energy_only_cutoff_for_f(self) -> None:
        # For p <= alpha Q:
        # lambda_p ||u_p||_inf <= C U0 lambda_p^(5/2)
        # <= C U0 Lambda^(5 alpha / 2).
        alpha = Fraction(4, 5)
        self.assertEqual(Fraction(5, 2) * alpha, Fraction(2, 1))
        for above in (Fraction(5, 6), Fraction(9, 10), Fraction(1, 1)):
            self.assertGreater(Fraction(5, 2) * above, 2)

    def test_four_fifths_far_low_coefficient_is_a2_controlled(self) -> None:
        for q_active in range(5, 31):
            r = (4 * q_active) // 5
            lambda_r_power = Fraction(2 ** (5 * r), 1)
            lambda_q_power = Fraction(2 ** (4 * q_active), 1)
            # Squaring the energy/Bernstein coefficient:
            # lambda_r^5 <= Lambda^4 exactly when 5r <= 4Q.
            self.assertLessEqual(lambda_r_power, lambda_q_power)

    def test_threshold_overshoot_reconstructs_upper_band_bound(self) -> None:
        nu = Fraction(7, 5)
        c0 = Fraction(1, 3)
        q_active = 15
        lambda_q = Fraction(2**q_active, 1)
        upper = range((4 * q_active) // 5 + 1, q_active + 1)

        amplitudes = {
            p: Fraction((p + 3) * 2**p, 7)
            for p in upper
        }
        f_upper = max(Fraction(2**p, 1) * amplitudes[p] for p in upper)
        omega = max(
            Fraction(2**p, 1)
            * max(
                amplitudes[p] - c0 * nu * Fraction(2**p, 1),
                Fraction(0, 1),
            )
            for p in upper
        )
        baseline = c0 * nu * lambda_q**2
        self.assertLessEqual(f_upper, baseline + omega)

    def test_packet_target_implies_overshoot_target_pointwise(self) -> None:
        q_active = 18
        lambda_q = Fraction(2**q_active, 1)
        upper = range((4 * q_active) // 5 + 1, q_active + 1)
        amplitudes = [Fraction((p + 1) ** 2, 13) for p in upper]

        omega = max(
            Fraction(2**p, 1) * amplitudes[i]
            for i, p in enumerate(upper)
        )
        s_upper = sum(a * a for a in amplitudes)
        # omega <= Lambda * sqrt(S_upper), checked without irrational sqrt.
        self.assertLessEqual(omega * omega, lambda_q**2 * s_upper)

    def test_turnover_time_fixture_has_finite_a2_and_dissipation_budgets(self) -> None:
        a2_charges = []
        dissipation_charges = []
        energies = []

        for n in range(2, 12):
            r = Fraction(2**n, 1)  # overshoot ratio
            lam = r**4
            duration = Fraction(1, 1) / (r * lam**2)
            energy = r**2 / lam

            a2_charges.append(lam**2 * duration)
            dissipation_charges.append(lam**2 * energy * duration)
            energies.append(energy)

            self.assertEqual(a2_charges[-1], Fraction(1, 1) / r)
            self.assertEqual(dissipation_charges[-1], Fraction(1, 1) / r**3)
            self.assertEqual(energy, Fraction(1, 1) / r**2)

        self.assertLess(sum(a2_charges), Fraction(1, 1))
        self.assertLess(sum(dissipation_charges), Fraction(1, 1))
        self.assertLessEqual(max(energies), Fraction(1, 16))

    def test_turnover_time_fixture_saturates_bernstein_and_threshold(self) -> None:
        c0 = Fraction(1, 2)
        for n in range(2, 10):
            r = Fraction(2**n, 1)
            lam = r**4
            amplitude = r * lam
            energy = r**2 / lam

            # Exact Bernstein-saturation scaling:
            # amplitude^2 = lambda^3 E.
            self.assertEqual(amplitude**2, lam**3 * energy)
            self.assertGreater(amplitude / lam, c0)

    def test_turnover_time_overshoot_charge_does_not_decay(self) -> None:
        c0 = Fraction(1, 2)
        charges = []
        for n in range(2, 14):
            r = Fraction(2**n, 1)
            lam = r**4
            amplitude = r * lam
            duration = Fraction(1, 1) / (r * lam**2)
            omega = lam * (amplitude - c0 * lam)
            charge = omega * duration
            charges.append(charge)
            self.assertEqual(charge, Fraction(1, 1) - c0 / r)
            self.assertGreater(charge, Fraction(3, 4))

        self.assertGreater(sum(charges), Fraction(len(charges) * 3, 4))


if __name__ == "__main__":
    unittest.main()
