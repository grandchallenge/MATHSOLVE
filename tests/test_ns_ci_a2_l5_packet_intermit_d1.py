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

    def test_intrinsic_energy_wavenumber_has_correct_ns_scaling(self) -> None:
        # nu is invariant; U0 scales rho^(-1/2), hence
        # lambda_E=(nu/U0)^2 scales as rho.
        nu_exponent = Fraction(0, 1)
        u0_exponent = Fraction(-1, 2)
        lambda_e_exponent = 2 * (nu_exponent - u0_exponent)
        self.assertEqual(lambda_e_exponent, Fraction(1, 1))

    def test_scale_normalization_matches_whole_space_ns_scaling(self) -> None:
        # PI_D*: lambda_E^D * integrated dissipation.
        # lambda_E contributes rho^D; Dint contributes rho^-1.
        for d in (
            Fraction(0, 1),
            Fraction(1, 1),
            Fraction(5, 4),
            Fraction(3, 2),
            Fraction(2, 1),
            Fraction(3, 1),
        ):
            lhs_exponent = d - Fraction(1, 1)
            rhs_exponent = d + Fraction(-1, 1)
            self.assertEqual(lhs_exponent, rhs_exponent)

    def test_dimensional_normalization_matches_packet_dimensions(self) -> None:
        # Track physical dimensions as (power of length, power of time).
        # [integral S_D dt] = L^(3-D) T^-1.
        # [nu] = L^2 T^-1, [U0] = L^(5/2) T^-1,
        # so [(nu/U0)^2] = L^-1; [Dint] = L^3 T^-1.
        for d in (
            Fraction(0, 1),
            Fraction(1, 1),
            Fraction(5, 4),
            Fraction(3, 2),
            Fraction(2, 1),
            Fraction(3, 1),
        ):
            lhs_dims = (Fraction(3, 1) - d, Fraction(-1, 1))
            lambda_e_dims = (Fraction(-1, 1), Fraction(0, 1))
            dint_dims = (Fraction(3, 1), Fraction(-1, 1))
            rhs_dims = (
                d * lambda_e_dims[0] + dint_dims[0],
                d * lambda_e_dims[1] + dint_dims[1],
            )
            self.assertEqual(lhs_dims, rhs_dims)

    def test_rejects_both_prior_normalization_defects(self) -> None:
        d = Fraction(1, 1)

        # Raw Dint fails Navier--Stokes scaling at D=1.
        lhs_scaling = d - Fraction(1, 1)
        raw_dint_scaling = Fraction(-1, 1)
        self.assertNotEqual(lhs_scaling, raw_dint_scaling)

        # U0^-2D * Dint fixes NS scaling but has the wrong physical units.
        # At D=1 it has dimensions T/L^2 instead of L^2/T.
        lhs_dims = (Fraction(2, 1), Fraction(-1, 1))
        u0_minus_2_dims = (Fraction(-5, 1), Fraction(2, 1))
        dint_dims = (Fraction(3, 1), Fraction(-1, 1))
        intermediate_rhs_dims = (
            u0_minus_2_dims[0] + dint_dims[0],
            u0_minus_2_dims[1] + dint_dims[1],
        )
        self.assertNotEqual(lhs_dims, intermediate_rhs_dims)

    def test_d1_leray_normalization_cancels_energy_scale(self) -> None:
        # Dint <= U0^2/(2 nu). PI_1* multiplies Dint by nu^2/U0^2,
        # leaving nu/2 exactly.
        u0_sq = Fraction(25, 9)
        nu = Fraction(7, 5)
        dissipation_upper = u0_sq / (2 * nu)
        normalized_upper = (nu**2 / u0_sq) * dissipation_upper
        self.assertEqual(normalized_upper, nu / 2)

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
        # Normalize nu=U0=1 and take c0^2=1/16. The active shell has
        # ||u_Q||_inf^2 = Lambda^3 > c0^2 nu^2 Lambda^2, while all higher
        # shells are zero and therefore satisfy the strict-high threshold.
        threshold_sq = Fraction(1, 16)
        for n in range(1, 7):
            lam = Fraction(2 ** (4 * n), 1)
            active_inf_sq = lam**3
            self.assertGreater(active_inf_sq, threshold_sq * lam**2)


if __name__ == "__main__":
    unittest.main()
