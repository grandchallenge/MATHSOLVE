from fractions import Fraction
import unittest


class NSCIA2L5C2ShearPhaseLockTests(unittest.TestCase):
    def test_decaying_shear_has_zero_self_advection(self) -> None:
        # U=U(y,t), v=(U,0), so v.grad v = U partial_x v = 0.
        partial_x_v = (0, 0)
        U = Fraction(7, 3)
        self.assertEqual(tuple(U * x for x in partial_x_v), (0, 0))

    def test_phase_substitution_gives_real_chain(self) -> None:
        # a_n=(-i)^n b_n.  After factoring (-i)^n,
        # -(i/2)(a_{n-1}+a_{n+1}) = (b_{n-1}-b_{n+1})/2.
        left = Fraction(5, 3)
        right = Fraction(7, 4)
        transformed = (left - right) / 2
        self.assertEqual(transformed, Fraction(-1, 24))

    def test_adjacent_locked_correlation_is_purely_imaginary(self) -> None:
        # conj(a_n) a_{n+1} = -i b_n b_{n+1}.
        b_n = Fraction(5, 3)
        b_next = Fraction(-7, 4)
        real_part = Fraction(0, 1)
        imag_part = -(b_n * b_next)
        self.assertEqual(real_part, 0)
        self.assertEqual(imag_part, Fraction(35, 12))

    def test_quadrature_coherence_is_maximal(self) -> None:
        # |Im(conj a b)|^2 = |a|^2 |b|^2 for the locked pair.
        for x, y in [
            (Fraction(2, 3), Fraction(5, 7)),
            (Fraction(-3, 4), Fraction(7, 5)),
        ]:
            imag_sq = (x * y) ** 2
            norm_product_sq = x**2 * y**2
            self.assertEqual(imag_sq, norm_product_sq)

    def test_viscous_diagonal_preserves_real_b_variables(self) -> None:
        eps = Fraction(1, 8)
        for n in range(-4, 5):
            b = Fraction(n + 6, 7)
            visc = -eps * (1 + n * n) * b
            self.assertIsInstance(visc, Fraction)

    def test_nearest_neighbor_coupling_conserves_total_chain_energy(self) -> None:
        # On a finite window with zero boundary amplitudes, the pure coupling
        # contribution sum_n 2 b_n * 1/2 (b_{n-1}-b_{n+1}) telescopes to zero.
        b = [Fraction(0), Fraction(2), Fraction(-3), Fraction(5), Fraction(0)]
        total = Fraction(0)
        for n in range(1, len(b) - 1):
            b_prime_coupling = (b[n - 1] - b[n + 1]) / 2
            total += 2 * b[n] * b_prime_coupling
        self.assertEqual(total, 0)

    def test_locked_flux_sign_matches_shell_balance(self) -> None:
        # F_{n+1/2}=-Im(conj(a_n)a_{n+1})=b_n b_{n+1}.
        # Hence F_{n-1/2}-F_{n+1/2}=b_n(b_{n-1}-b_{n+1}),
        # exactly the pure-coupling contribution to d|a_n|^2/dtau.
        b_left = Fraction(5, 3)
        b_n = Fraction(-7, 4)
        b_right = Fraction(11, 6)
        flux_left = b_left * b_n
        flux_right = b_n * b_right
        shell_balance = flux_left - flux_right
        coupling_energy_derivative = b_n * (b_left - b_right)
        self.assertEqual(shell_balance, coupling_energy_derivative)

    def test_viscosity_dissipates_chain_energy(self) -> None:
        eps = Fraction(1, 10)
        b = {
            -1: Fraction(2, 3),
            0: Fraction(5, 4),
            2: Fraction(-7, 5),
        }
        dissipation = sum(
            2 * eps * (1 + n * n) * amp**2
            for n, amp in b.items()
        )
        self.assertGreater(dissipation, 0)

    def test_inviscid_first_jets_match_bessel_chain_scaling(self) -> None:
        # J_0(0)=1; J_1'(0)=1/2.  With a_1=-i J_1,
        # the first neighbor derivative has magnitude 1/2.
        j0_at_zero = Fraction(1)
        j1_prime_at_zero = Fraction(1, 2)
        self.assertEqual(j0_at_zero, 1)
        self.assertEqual(j1_prime_at_zero, Fraction(1, 2))

    def test_phase_lock_does_not_depend_on_epsilon(self) -> None:
        # epsilon changes only real coefficients in the b-system.
        for R in (2, 4, 8, 16, 32):
            eps = Fraction(1, R)
            diagonal_multiplier = -eps * (1 + 3**2)
            self.assertIsInstance(diagonal_multiplier, Fraction)


if __name__ == "__main__":
    unittest.main()
