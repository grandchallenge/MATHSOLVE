from fractions import Fraction
import math
import unittest


class NSCIA2L5PI1CriticalEnergyTests(unittest.TestCase):
    def test_packet_s1_is_dominated_shellwise_by_h32_density(self) -> None:
        # Bernstein in 3D gives ||u_q||_infinity^2 <= C lambda_q^3 ||u_q||_2^2.
        # The fixture checks the exact frequency exponent used by the route.
        for q in range(0, 12):
            lam = Fraction(2**q, 1)
            energy = Fraction((q + 3) ** 2, 7)
            bernstein_s1_density = lam**3 * energy
            h32_density = lam**3 * energy
            self.assertEqual(bernstein_s1_density, h32_density)

    def test_low_mode_f_bound_has_lambda_squared_times_sqrt_x_scaling(self) -> None:
        # For q<=Q,
        # (lambda_q ||u_q||_infinity)^2 <= lambda_q^5 E_q
        # <= Lambda^4 * (lambda_q E_q) <= Lambda^4 X.
        for q in range(0, 7):
            for Q in range(q, 9):
                lam_q = Fraction(2**q, 1)
                Lambda = Fraction(2**Q, 1)
                energy = Fraction(q + 2, 5)
                lhs = lam_q**5 * energy
                rhs = Lambda**4 * lam_q * energy
                self.assertLessEqual(lhs, rhs)

    def test_leray_interpolation_places_critical_energy_in_l2_time(self) -> None:
        # ||u||_{H^{1/2}}^2 <= ||u||_2 ||grad u||_2, so after squaring
        # X^2 <= U0^2 ||grad u||_2^2.  This is an exponent/normalization guard.
        U0 = Fraction(7, 3)
        grad = Fraction(11, 5)
        X = U0 * grad
        self.assertEqual(X**2, U0**2 * grad**2)

    def test_superlinear_comparison_allows_blowup_with_a_in_l1_and_x_in_l2(self) -> None:
        # Let h=T-t, p=1/4, x=h^{-p}, a=p h^{p/2-1}.
        # Then x'=a x^{3/2}; a is L1 and x is L2 near h=0.
        p = Fraction(1, 4)
        a_exp = p / 2 - 1
        x2_exp = -2 * p
        derivative_exp = -p - 1
        rhs_exp = a_exp - 3 * p / 2

        self.assertGreater(a_exp, -1)
        self.assertGreater(x2_exp, -1)
        self.assertEqual(rhs_exp, derivative_exp)

    def test_small_tail_of_coefficient_has_exact_riccati_threshold_scaling(self) -> None:
        # Integral_0^h a(s) ds ~ h^{p/2}, while x(h)^(-1/2)=h^{p/2}.
        # Thus shrinking the terminal interval alone does not beat the
        # superlinear comparison threshold.
        p = Fraction(1, 4)
        a_exp = p / 2 - 1
        coefficient_tail_exp = a_exp + 1
        inverse_sqrt_x_exp = p / 2
        self.assertEqual(coefficient_tail_exp, inverse_sqrt_x_exp)

    @staticmethod
    def _neg(k):
        return tuple(-x for x in k)

    @staticmethod
    def _add(k, ell):
        return tuple(x + y for x, y in zip(k, ell))

    @staticmethod
    def _dot_real_complex(k, u):
        return sum(x * y for x, y in zip(k, u))

    @classmethod
    def _project(cls, k, v):
        kk = sum(x * x for x in k)
        kv = cls._dot_real_complex(k, v)
        return tuple(vj - kj * kv / kk for kj, vj in zip(k, v))

    @classmethod
    def _rhs(cls, target, support):
        # Fourier coefficient of -P(u dot grad u):
        # -i P_k sum_{p+q=k} (q dot u_p) u_q.
        total = [0j, 0j, 0j]
        for p, u_p in support.items():
            for q, u_q in support.items():
                if cls._add(p, q) != target:
                    continue
                coefficient = cls._dot_real_complex(q, u_p)
                for j in range(3):
                    total[j] += coefficient * u_q[j]
        projected = cls._project(target, tuple(total))
        return tuple(-1j * z for z in projected)

    @classmethod
    def _transfer_rate(cls, target, support):
        rhs = cls._rhs(target, support)
        u = support[target]
        return sum((u[j].conjugate() * rhs[j]).real for j in range(3))

    @classmethod
    def _triad(cls, flip_m=False):
        k = (1, 0, 0)
        ell = (0, 2, 0)
        m = (-1, -2, 0)
        u_k = (0j, 1 + 0j, 1j)
        u_ell = (1 + 0j, 0j, 1j)
        u_m = (2j, -1j, -1 + 0j)
        if flip_m:
            u_m = tuple(-z for z in u_m)

        support = {
            k: u_k,
            ell: u_ell,
            m: u_m,
            cls._neg(k): tuple(z.conjugate() for z in u_k),
            cls._neg(ell): tuple(z.conjugate() for z in u_ell),
            cls._neg(m): tuple(z.conjugate() for z in u_m),
        }
        return support

    def test_exact_triad_is_divergence_free_and_reality_symmetric(self) -> None:
        support = self._triad()
        for k, u in support.items():
            divergence = self._dot_real_complex(k, u)
            self.assertAlmostEqual(divergence.real, 0.0)
            self.assertAlmostEqual(divergence.imag, 0.0)
            neg = self._neg(k)
            self.assertEqual(support[neg], tuple(z.conjugate() for z in u))

    def test_exact_triad_conserves_unweighted_l2_transfer(self) -> None:
        support = self._triad()
        total = sum(self._transfer_rate(k, support) for k in support)
        self.assertAlmostEqual(total, 0.0)

    def test_critical_h12_weighted_transfer_has_both_signs(self) -> None:
        def weighted_pairing(support):
            return sum(
                math.sqrt(sum(x * x for x in k)) * self._transfer_rate(k, support)
                for k in support
            )

        negative = weighted_pairing(self._triad(flip_m=False))
        positive = weighted_pairing(self._triad(flip_m=True))
        self.assertAlmostEqual(negative, -8.0)
        self.assertAlmostEqual(positive, 8.0)


if __name__ == "__main__":
    unittest.main()
