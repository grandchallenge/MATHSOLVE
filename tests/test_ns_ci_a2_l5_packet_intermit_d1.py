from fractions import Fraction
import unittest


class NSCIA2L5PacketIntermittencyD1Tests(unittest.TestCase):
    def test_d1_pointwise_bridge_is_exactly_scale_compatible(self) -> None:
        for q_max in range(1, 9):
            lam_qmax = Fraction(2**q_max, 1)
            inf_sq = [Fraction((q + 2) ** 2, 3) for q in range(q_max + 1)]
            f_sq = max(
                Fraction(2 ** (2 * q), 1) * inf_sq[q]
                for q in range(q_max + 1)
            )
            d1_sum = sum(inf_sq)
            self.assertLessEqual(f_sq, lam_qmax**2 * d1_sum)

    def test_general_packet_exponent_closes_exactly_at_d_ge_one(self) -> None:
        for d in (
            Fraction(1, 1),
            Fraction(5, 4),
            Fraction(3, 2),
            Fraction(2, 1),
            Fraction(3, 1),
        ):
            self.assertLessEqual(Fraction(3, 1) - d, Fraction(2, 1))

        self.assertGreater(
            Fraction(3, 1) - Fraction(3, 4),
            Fraction(2, 1),
        )

    def test_d1_temporal_cauchy_factorization(self) -> None:
        # Set f_i = Lambda_i * b_i and S_i = b_i^2, so the D=1 pointwise
        # bridge is saturated. Weighted Cauchy--Schwarz is then exact.
        durations = [Fraction(1, 2), Fraction(1, 4), Fraction(1, 8)]
        lambdas = [Fraction(2, 1), Fraction(4, 1), Fraction(8, 1)]
        b = [Fraction(3, 2), Fraction(5, 3), Fraction(7, 4)]

        integral_f = sum(dt * lam * bi for dt, lam, bi in zip(durations, lambdas, b))
        lambda_budget = sum(dt * lam**2 for dt, lam in zip(durations, lambdas))
        d1_budget = sum(dt * bi**2 for dt, bi in zip(durations, b))

        self.assertLessEqual(integral_f**2, lambda_budget * d1_budget)

    def test_static_fixture_preserves_a2_scalar_budgets(self) -> None:
        lambda_budget = []
        dissipation_budget = []
        energy = []

        for n in range(1, 9):
            lam = Fraction(2 ** (4 * n), 1)
            duration = Fraction(1, 2 ** (9 * n))
            e_q = Fraction(1, 1)
            a_q = lam**2 * e_q

            lambda_budget.append(lam**2 * duration)
            dissipation_budget.append(a_q * duration)
            energy.append(e_q)

        self.assertLess(sum(lambda_budget), Fraction(1, 1))
        self.assertLess(sum(dissipation_budget), Fraction(1, 1))
        self.assertTrue(all(value == 1 for value in energy))

    def test_static_fixture_d1_left_side_diverges_geometrically(self) -> None:
        terms = []
        for n in range(1, 8):
            lam = Fraction(2 ** (4 * n), 1)
            duration = Fraction(1, 2 ** (9 * n))
            inf_sq = lam**3
            terms.append(duration * inf_sq)

        for left, right in zip(terms, terms[1:]):
            self.assertEqual(right / left, Fraction(8, 1))

    def test_static_fixture_is_compatible_with_selector_threshold_logic(self) -> None:
        # Take (c0 * nu)^2 = 1/16.  The active shell has
        # ||u_Q||_inf^2 = Lambda^3 > (c0 nu)^2 Lambda^2, while all higher
        # shells are zero and therefore satisfy the strict-high threshold.
        threshold_sq = Fraction(1, 16)
        for n in range(1, 7):
            lam = Fraction(2 ** (4 * n), 1)
            active_inf_sq = lam**3
            self.assertGreater(active_inf_sq, threshold_sq * lam**2)


if __name__ == "__main__":
    unittest.main()
