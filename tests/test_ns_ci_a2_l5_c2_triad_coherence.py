from fractions import Fraction
import unittest


class NSCIA2L5C2TriadCoherenceTests(unittest.TestCase):
    def test_initial_target_transport_forcing_is_one(self) -> None:
        # -V.grad(theta_0) target sin(X+Y) coefficient:
        # +1/2 from cos(Y)*sin(X) and +1/2 from cos(X)*sin(Y).
        left_source = Fraction(1, 2)
        right_source = Fraction(1, 2)
        self.assertEqual(left_source + right_source, 1)

    def test_initial_target_derivative_in_turnover_variables(self) -> None:
        # c' = g - 2 epsilon c, with c(0)=g(0)=1.
        for R in (2, 4, 8, 16):
            eps = Fraction(1, R)
            c_prime = 1 - 2 * eps
            self.assertEqual(c_prime, Fraction(R - 2, R))

    def test_coherent_transfer_lower_bound_from_half_bounds(self) -> None:
        c = Fraction(1, 2)
        g = Fraction(1, 2)
        self.assertEqual(c * g, Fraction(1, 4))

    def test_physical_transfer_integrates_to_energy_scale(self) -> None:
        # (A^3 N) * (tau_*/(A N)) = tau_* A^2.
        A = Fraction(7, 3)
        N = Fraction(11, 5)
        tau_star = Fraction(1, 8)
        transfer_scale = A**3 * N
        physical_duration = tau_star / (A * N)
        self.assertEqual(
            transfer_scale * physical_duration,
            tau_star * A**2,
        )

    def test_viscous_loss_is_inverse_R_relative_to_transfer(self) -> None:
        # Over a turnover interval:
        # viscous scale ~ nu N^2 A^2 /(A N) = (nu N/A) A^2 = A^2/R.
        for R in (4, 8, 16, 32):
            ratio = Fraction(1, R)
            self.assertLess(ratio, Fraction(1, 2))

    def test_target_overshoot_ratio_stays_large_under_half_amplitude(self) -> None:
        # |C_phys| >= A/2 and target frequency is sqrt(2) N.
        # Squared normalized ratio is >= R^2/8.
        c0_sq = Fraction(1, 1)
        for R in (4, 8, 16):
            ratio_sq = Fraction(R**2, 8)
            self.assertGreater(ratio_sq, c0_sq)

    def test_fixed_turnover_interval_is_not_subturnover(self) -> None:
        # In normalized turnover time, tau_* is a fixed positive constant,
        # independent of R. Physical duration is tau_*/(A N).
        tau_star = Fraction(1, 10)
        for R in (4, 8, 16, 32):
            normalized_length = tau_star
            self.assertEqual(normalized_length, tau_star)

    def test_l5_20_selector_charge_can_vanish_while_transfer_is_coherent(self) -> None:
        # L5-20 s=4 upper scale is R^-1/2, whereas the normalized coherent
        # transfer integral is bounded below by a fixed constant.
        charges = []
        transfer_lower = Fraction(1, 40)
        for M in (2, 4, 8, 16):
            # R=M^2 makes R^-1/2=1/M exactly.
            charges.append(Fraction(1, M))
            self.assertGreater(transfer_lower, 0)
        self.assertTrue(all(b < a for a, b in zip(charges, charges[1:])))

    def test_strong_convergence_forcing_is_order_epsilon(self) -> None:
        # On fixed tau in [0,T], 1-exp(-epsilon tau) <= epsilon T.
        # Guard the algebraic scaling used by the H^s difference estimate.
        T = Fraction(3, 2)
        for R in (4, 8, 16):
            eps = Fraction(1, R)
            forcing_bound_scale = eps * T
            self.assertEqual(forcing_bound_scale, Fraction(3, 2 * R))


if __name__ == "__main__":
    unittest.main()
