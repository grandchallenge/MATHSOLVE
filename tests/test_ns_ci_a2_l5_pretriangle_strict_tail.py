import math
import unittest
from fractions import Fraction


class NSCIA2L5PretriangleStrictTailTests(unittest.TestCase):
    def test_quartic_pair_kernel_is_uniform(self) -> None:
        for r in range(0, 24):
            row = Fraction(0, 1)
            lambda_r = Fraction(2**r, 1)
            for p in range(0, r + 1):
                lambda_p = Fraction(2**p, 1)
                row += (lambda_p / lambda_r) ** 2
            self.assertLessEqual(row, Fraction(4, 3))

    def test_sextic_triple_kernel_has_h2_endpoint(self) -> None:
        for s in range(0, 20):
            lambda_s = Fraction(2**s, 1)
            triple = Fraction(0, 1)
            for r in range(0, s + 1):
                lambda_r = Fraction(2**r, 1)
                for p in range(0, r + 1):
                    lambda_p = Fraction(2**p, 1)
                    triple += (
                        lambda_p**2 * lambda_r**2 / lambda_s**2
                    )
            self.assertLessEqual(
                triple,
                Fraction(64, 45) * lambda_s**2,
            )

    def test_quartic_and_sextic_scaling_are_exact(self) -> None:
        # Under Navier--Stokes scaling, A scales as rho and lambda as rho.
        a_scaling = Fraction(1, 1)
        lambda_scaling = Fraction(1, 1)
        self.assertEqual(a_scaling, Fraction(1, 1))  # ||u||_4^4
        z_scaling = 2 * lambda_scaling + a_scaling
        self.assertEqual(z_scaling, Fraction(3, 1))
        self.assertEqual(Fraction(2, 3) * z_scaling, Fraction(2, 1))

    def test_counterfixture_static_budgets_converge(self) -> None:
        lambda_occupancy = []
        dissipation = []
        energy = []
        for n in range(1, 16):
            lam_q = 2 ** (6 * n)
            duration = Fraction(1, 2 ** (13 * n))
            a_tail = 2 ** (9 * n)
            lambda_occupancy.append(Fraction(lam_q**2, 1) * duration)
            dissipation.append(Fraction(a_tail, 1) * duration)
            energy.append(Fraction(a_tail, lam_q**2))

        self.assertLess(sum(lambda_occupancy), Fraction(1, 1))
        self.assertLess(sum(dissipation), Fraction(1, 1))
        self.assertTrue(all(e <= Fraction(1, 8) for e in energy))

    def test_counterfixture_h2_endpoint_diverges(self) -> None:
        terms = []
        for n in range(1, 12):
            # Ignore the fixed K-shift: it only multiplies by a fixed constant.
            lam_q = 2 ** (6 * n)
            duration = 2.0 ** (-13 * n)
            a_tail = 2.0 ** (9 * n)
            z_tail = (lam_q**2) * a_tail
            terms.append(duration * (z_tail ** (2.0 / 3.0)))

        self.assertTrue(all(math.isfinite(x) for x in terms))
        for left, right in zip(terms, terms[1:]):
            self.assertGreater(right, 1.9 * left)

    def test_packet_multiplicity_matches_tail_enstrophy_exponent(self) -> None:
        # One strict-high threshold packet carries A ~ lambda.
        # M ~ lambda^(1/2) separated packets therefore permit A ~ lambda^(3/2)
        # without increasing the L-infinity threshold.
        for n in range(1, 8):
            lam = 2 ** (6 * n)
            multiplicity = 2 ** (3 * n)
            packet_a = lam
            total_a = multiplicity * packet_a
            self.assertEqual(total_a, 2 ** (9 * n))

    def test_strict_tail_never_uses_threshold_shell(self) -> None:
        q = 17
        k = 2
        strict_tail = range(q + k + 1, q + k + 8)
        self.assertTrue(all(p > q for p in strict_tail))
        self.assertNotIn(q, strict_tail)


if __name__ == "__main__":
    unittest.main()
