from fractions import Fraction
import unittest


class NSCIA2L5C2ActiveBandTests(unittest.TestCase):
    def test_two_thirds_far_low_has_lambda_squared_scaling(self) -> None:
        # lambda_q=2^q.  For r=floor(2Q/3), lambda_r^3 <= lambda_Q^2.
        for q_active in range(3, 31):
            r = (2 * q_active) // 3
            lambda_r_cubed = Fraction(2 ** (3 * r), 1)
            lambda_q_squared = Fraction(2 ** (2 * q_active), 1)
            self.assertLessEqual(lambda_r_cubed, lambda_q_squared)

    def test_two_thirds_is_critical_for_energy_only_far_low_bound(self) -> None:
        # A relative cutoff alpha Q produces lambda_(alpha Q)^3 ~ Lambda^(3 alpha).
        # alpha=2/3 is exactly the largest exponent compatible with Lambda^2.
        alpha = Fraction(2, 3)
        self.assertEqual(3 * alpha, 2)

        # Any rational alpha>2/3 has exponent strictly above the A2 power.
        for alpha_above in (Fraction(7, 10), Fraction(3, 4), Fraction(4, 5)):
            self.assertGreater(3 * alpha_above, 2)

    def test_far_low_packet_sum_is_controlled_by_energy_supremum(self) -> None:
        # Finite exact model of
        # sum_{q<=r} ||u_q||_inf^2 <= C sum lambda_q^3 E_q
        # <= C lambda_r^3 sum E_q <= C U0^2 Lambda^2.
        for q_active in range(3, 12):
            r = (2 * q_active) // 3
            energies = [Fraction(q + 1, (r + 1) * (r + 2)) for q in range(r + 1)]
            u0_sq = sum(energies)
            lhs_model = sum(Fraction(2 ** (3 * q), 1) * energies[q] for q in range(r + 1))
            upper = Fraction(2 ** (3 * r), 1) * u0_sq
            a2_scale = Fraction(2 ** (2 * q_active), 1) * u0_sq
            self.assertLessEqual(lhs_model, upper)
            self.assertLessEqual(upper, a2_scale)

    def test_dimension_one_concentration_factor_identity(self) -> None:
        # chi_q = ||u_q||_inf^2 / (lambda_E lambda_q^2 E_q)
        # and d_q = nu lambda_q^2 E_q imply
        # ||u_q||_inf^2 = (lambda_E/nu) chi_q d_q exactly.
        nu = Fraction(5, 3)
        lambda_e = Fraction(7, 11)
        for q in range(1, 9):
            lam = Fraction(2**q, 1)
            energy = Fraction(q + 2, 13)
            amplitude_sq = Fraction((q + 1) ** 2, 17)
            chi = amplitude_sq / (lambda_e * lam**2 * energy)
            dissipation_density = nu * lam**2 * energy
            reconstructed = (lambda_e / nu) * chi * dissipation_density
            self.assertEqual(reconstructed, amplitude_sq)

    def test_active_threshold_sets_dimension_one_volume_ceiling(self) -> None:
        # At q=Q, ||u_Q||_inf >= c0 nu Lambda and E_Q<=U0^2.
        # Thus V_Q=E_Q/||u_Q||_inf^2
        # <= c0^-2 lambda_E^-1 Lambda^-2.
        c0 = Fraction(2, 5)
        nu = Fraction(3, 2)
        u0 = Fraction(7, 3)
        lambda_e = (nu / u0) ** 2

        for q in range(2, 9):
            lam = Fraction(2**q, 1)
            energy = u0**2
            amplitude_sq = (c0 * nu * lam) ** 2
            volume = energy / amplitude_sq
            ceiling = Fraction(1, 1) / (c0**2 * lambda_e * lam**2)
            self.assertEqual(volume, ceiling)

            chi = amplitude_sq / (lambda_e * lam**2 * energy)
            self.assertEqual(chi, c0**2)

    def test_chi_weighted_dissipation_is_exact_top_band_packet_sum(self) -> None:
        nu = Fraction(4, 3)
        lambda_e = Fraction(3, 10)
        q_active = 12
        r = (2 * q_active) // 3
        packet_sum = Fraction(0, 1)
        weighted = Fraction(0, 1)

        for q in range(r + 1, q_active + 1):
            lam = Fraction(2**q, 1)
            energy = Fraction(q + 1, 19)
            amplitude_sq = Fraction((2 * q + 1) ** 2, 23)
            chi = amplitude_sq / (lambda_e * lam**2 * energy)
            d_q = nu * lam**2 * energy
            packet_sum += amplitude_sq
            weighted += (lambda_e / nu) * chi * d_q

        self.assertEqual(packet_sum, weighted)


if __name__ == "__main__":
    unittest.main()
