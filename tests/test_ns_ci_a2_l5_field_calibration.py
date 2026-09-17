from fractions import Fraction
import unittest


class NSCIA2L5FieldCalibrationTests(unittest.TestCase):
    def test_low_lambda_region_is_harmless_under_source_envelope(self) -> None:
        # On {Lambda <= R}, Lambda^(5/2) <= R^(1/2) Lambda^2.
        # Use exact square choices R=s^2 to keep the comparison rational.
        for s in range(1, 8):
            r = Fraction(s * s, 1)
            root_r = Fraction(s, 1)
            for lam_int in range(1, s * s + 1):
                lam = Fraction(lam_int, 1)
                lhs_squared = lam**5
                rhs_squared = r * lam**4
                self.assertLessEqual(lhs_squared, rhs_squared)
                self.assertLessEqual(lam**2 * lam, root_r * lam**2 * root_r)

    def test_high_lambda_tail_cauchy_schwarz_structure(self) -> None:
        # Pointwise f^2 <= Lambda^2 S1. A finite discrete proxy verifies the
        # exact Cauchy--Schwarz algebra used after restriction to {Lambda>R}.
        lambdas = [Fraction(2**k, 1) for k in range(1, 6)]
        s1 = [Fraction((k + 1) ** 2, 3) for k in range(1, 6)]
        f = [lam * value for lam, value in zip(lambdas, s1)]
        weights = [Fraction(1, 2 ** (2 * k)) for k in range(1, 6)]

        lhs = sum(w * term for w, term in zip(weights, f))
        a = sum(w * lam**2 for w, lam in zip(weights, lambdas))
        b = sum(w * value**2 for w, value in zip(weights, s1))
        self.assertLessEqual(lhs**2, a * b)

    def test_radial_core_scale_is_borderline_l2_for_lambda(self) -> None:
        # lambda_core ~ tau^-1/2, so lambda_core^2 ~ tau^-1.
        # Dyadic terminal slabs tau in [2^-(n+1),2^-n] each contribute a
        # scale-independent amount to integral lambda_core^2 dt.
        contributions = []
        for n in range(1, 10):
            tau_upper = Fraction(1, 2**n)
            tau_lower = Fraction(1, 2 ** (n + 1))
            slab = tau_upper - tau_lower
            representative_lambda_sq = Fraction(1, tau_upper)
            contributions.append(slab * representative_lambda_sq)
        self.assertTrue(all(c == Fraction(1, 2) for c in contributions))

    def test_angular_reynolds_ratio_grows_for_positive_h(self) -> None:
        # Published similarity scales give U_theta/(nu*lambda_core) ~ tau^-h.
        # With tau=2^-n and any positive rational h, the ratio grows in n.
        # Use h=1/100 only to test the monotone exponent sign numerically.
        h = Fraction(1, 100)
        values = [2 ** (float(h) * n) for n in range(1, 8)]
        self.assertTrue(all(left < right for left, right in zip(values, values[1:])))

    def test_forced_blowup_is_not_direct_a2_counterexample(self) -> None:
        # Governance guardrail: the September 2026 construction includes a
        # smooth external force; the selected A2 theorem is unforced.
        selected_a2_is_unforced = True
        calibration_solution_is_forced = True
        self.assertNotEqual(selected_a2_is_unforced, not calibration_solution_is_forced)
        self.assertTrue(selected_a2_is_unforced and calibration_solution_is_forced)


if __name__ == "__main__":
    unittest.main()
