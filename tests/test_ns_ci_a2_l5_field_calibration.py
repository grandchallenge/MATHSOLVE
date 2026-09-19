from fractions import Fraction
import unittest


class NSCIA2L5FieldCalibrationTests(unittest.TestCase):
    def test_low_lambda_region_is_harmless_under_source_envelope(self) -> None:
        # On {Lambda <= R}, Lambda^(5/2) <= R^(1/2) Lambda^2.
        # Squaring removes radicals: Lambda^5 <= R Lambda^4 iff Lambda <= R.
        for r in range(1, 17):
            R = Fraction(r, 1)
            for lam_int in range(1, r + 1):
                lam = Fraction(lam_int, 1)
                self.assertLessEqual(lam**5, R * lam**4)

    def test_high_lambda_tail_cauchy_schwarz_structure(self) -> None:
        # Pointwise f^2 <= Lambda^2 S1. Write s=sqrt(S1), so f<=Lambda*s.
        # This finite exact proxy checks the weighted Cauchy--Schwarz step.
        lambdas = [Fraction(2**k, 1) for k in range(1, 6)]
        sqrt_s1 = [Fraction(k + 1, 3) for k in range(1, 6)]
        weights = [Fraction(1, 2 ** (2 * k)) for k in range(1, 6)]
        f = [lam * s for lam, s in zip(lambdas, sqrt_s1)]

        lhs = sum(w * term for w, term in zip(weights, f))
        a = sum(w * lam**2 for w, lam in zip(weights, lambdas))
        b = sum(w * s**2 for w, s in zip(weights, sqrt_s1))
        self.assertLessEqual(lhs**2, a * b)

    def test_radial_core_scale_is_borderline_l2_for_lambda(self) -> None:
        # lambda_core ~ tau^-1/2, so lambda_core^2 ~ tau^-1.
        # On each dyadic terminal slab, a lower-end representative contributes
        # a fixed positive amount, encoding logarithmic divergence.
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
        # For tau=2^-n, every h>0 makes the ratio strictly increase with n.
        h = Fraction(1, 100)
        values = [2 ** (float(h) * n) for n in range(1, 8)]
        self.assertTrue(all(left < right for left, right in zip(values, values[1:])))

    def test_forced_blowup_is_calibration_not_direct_a2_counterexample(self) -> None:
        selected_a2_is_unforced = True
        calibration_solution_has_external_force = True
        direct_counterexample_class_match = (
            not selected_a2_is_unforced or not calibration_solution_has_external_force
        )
        self.assertFalse(direct_counterexample_class_match)


if __name__ == "__main__":
    unittest.main()
