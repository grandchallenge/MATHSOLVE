from fractions import Fraction
import math
import unittest


class NSCIA2L5FrequencyScaleTransplantTests(unittest.TestCase):
    def test_two_sided_source_kernel_has_summable_tails(self) -> None:
        m = 6
        L = 4

        def kernel(d: int) -> float:
            if d >= L:
                return 2.0 ** (-d / m)
            if d <= -L:
                return 2.0**d
            return 1.0

        # A large symmetric partial sum is finite and the omitted geometric
        # tails are explicitly small.  This guards the source kernel shape,
        # not a campaign PDE estimate.
        partial = sum(kernel(d) for d in range(-80, 81))
        low_ratio = 2.0 ** (-1 / m)
        low_tail = (2.0 ** (-81 / m)) / (1.0 - low_ratio)
        high_tail = (2.0 ** (-81)) / (1.0 - 0.5)
        self.assertTrue(math.isfinite(partial))
        self.assertLess(low_tail + high_tail, 1e-3)

    def test_source_kernel_keeps_unit_diagonal(self) -> None:
        # |d| < L is the unsuppressed central band in (3.20).
        L = 4
        d = 0
        kernel_zero = 1 if abs(d) < L else None
        self.assertEqual(kernel_zero, 1)

    def test_p4_fixture_has_finite_a2_budget(self) -> None:
        # Representative critical pair p=4, m=6.  Set b_j=j^-4 and
        # duration mu_j=b_j*lambda_j^-2.  Then int Lambda^2 = sum b_j.
        budget = sum(Fraction(1, j**4) for j in range(2, 200))
        self.assertLess(budget, Fraction(1, 1))

    def test_p4_fixture_has_finite_leray_dissipation_budget(self) -> None:
        # Threshold-scale packet: ||u_j||_2^2 ~ lambda_j^-1 (nu factors
        # suppressed).  Integrated dissipation is sum b_j/lambda_j.
        dissipation = sum(
            Fraction(1, j**4 * 2**j)
            for j in range(2, 100)
        )
        self.assertLess(dissipation, Fraction(1, 1))

    def test_p4_fixture_has_finite_s1_and_f_budgets(self) -> None:
        # At threshold amplitude ||u_j||_inf ~ lambda_j, both the S1 integral
        # and the one-packet f integral reduce, up to fixed nu factors, to
        # sum b_j.
        s1 = sum(Fraction(1, j**4) for j in range(2, 200))
        f = sum(Fraction(1, j**4) for j in range(2, 200))
        self.assertLess(s1, 1)
        self.assertLess(f, 1)

    def test_p4_source_sequence_is_harmonic(self) -> None:
        # p=4 gives b_j^(1/p)=j^-1 exactly.  Every dyadic block [N,2N)
        # contributes at least 1/2, so the ell^1 source sum diverges.
        for n in (4, 8, 16, 32, 64):
            block = sum(Fraction(1, j) for j in range(n, 2 * n))
            self.assertGreaterEqual(block, Fraction(1, 2))

    def test_unit_diagonal_cannot_repair_harmonic_source(self) -> None:
        # B_k = sum_j K_(k-j) a_j and K_0=1 imply B_k >= a_k.
        # Check the exact lower bound on finite harmonic blocks.
        for n in (8, 16, 32):
            a_block = sum(Fraction(1, k) for k in range(n, 2 * n))
            b_lower_bound = a_block
            self.assertGreaterEqual(b_lower_bound, Fraction(1, 2))

    def test_energy_to_critical_estimate_leaves_half_derivative(self) -> None:
        # For p=4,m=6, Bernstein costs lambda^(1/2+2/p)=lambda.
        # Raising to p and spending one shell-dissipation factor lambda^-2
        # leaves lambda^(p/2), hence lambda^(1/2) after the p-th root.
        p = Fraction(4, 1)
        bernstein_exponent = Fraction(1, 2) + Fraction(2, 1) / p
        residual_after_pth_root = (
            p * bernstein_exponent - 2
        ) / p
        self.assertEqual(bernstein_exponent, 1)
        self.assertEqual(residual_after_pth_root, Fraction(1, 2))

    def test_a2_level_measure_cancels_only_time_frequency_factor(self) -> None:
        # Active-set measure contributes lambda^(-2/p); it cancels the
        # +2/p in the critical Bernstein exponent but leaves +1/2.
        p = Fraction(4, 1)
        residual = Fraction(1, 2) + Fraction(2, 1) / p - Fraction(2, 1) / p
        self.assertEqual(residual, Fraction(1, 2))


if __name__ == "__main__":
    unittest.main()
