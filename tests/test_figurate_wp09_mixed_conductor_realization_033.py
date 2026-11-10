"""Independent exact regression oracle for FIGURATE WP09-033.

Matrix powering and square-discriminant inversion do not use the producer's
quadratic-ring multiplication or polygonal-membership validator.
"""
from __future__ import annotations

from math import gcd, isqrt
import unittest

from research import figurate_wp09_mixed_conductor_realization_033 as wp
from research import figurate_wp09_power3_global_seeds_032 as previous


def independent_unit_matrix_power(exponent: int, modulus: int) -> tuple[int, int]:
    """Iterated matrix [[3,4],[2,3]] applied to (1,0), binary exponent."""
    a,b,c,d = 3 % modulus, 4 % modulus, 2 % modulus, 3 % modulus
    x,y = 1,0
    while exponent:
        if exponent&1:
            x,y = (a*x+b*y)%modulus,(c*x+d*y)%modulus
        a,b,c,d = ((a*a+b*c)%modulus,(a*b+b*d)%modulus,
                     (c*a+d*c)%modulus,(c*b+d*d)%modulus)
        exponent//=2
    return x,y


def independent_polygonal_root(A: int, n: int) -> int | None:
    """Invert P_(2A+2)(t) = A*t*(t-1)+t via the exact discriminant."""
    if n<1:
        return None
    disc=(A-1)*(A-1)+4*A*n
    q=isqrt(disc)
    if q*q!=disc or (A-1+q)%(2*A):
        return None
    t=(A-1+q)//(2*A)
    return t if t>0 else None


class MixedRayTheoremTests(unittest.TestCase):
    def test_base_unit_orders_and_primitive_slopes(self):
        # Explicit integers derived by multiplication, not by querying producer.
        base = {3:(4,577,408),5:(6,19601,13860),7:(3,99,70)}
        for p,(t,x,y) in base.items():
            self.assertEqual(independent_unit_matrix_power(t,p*p),(x%(p*p),y%(p*p)))
            self.assertEqual(x%p,1)
            self.assertEqual(y%p,0)
            self.assertNotEqual(y%(p*p),0)
            self.assertEqual(x*x-2*y*y,1)

    def test_closed_norm_identity_independent(self):
        for f in (3,5,7,9,15,21,25,35,45,49,63,75,105,315,11025):
            A=f*f
            H=(A*A+6*A+1)//8
            x=(A+4*f+3)//2
            y=(f**3+3*f+2)//2
            self.assertEqual((A*A+6*A+1)%8,0)
            self.assertEqual(x*x-2*y*y,-2*(2*A-1)*H)
            self.assertEqual(gcd(f, 2*(2*A-1)*H),1)

    def test_uniform_modular_ray_using_independent_matrix(self):
        factors=[3**a*5**b*7**c for a in range(3) for b in range(3)
                 for c in range(3) if a+b+c>0]
        self.assertEqual(len(factors),26)
        for f in factors:
            with self.subTest(f=f):
                cert=wp.ray_certificate(f)
                A=f*f
                modulus=f**3
                scalar,radical=independent_unit_matrix_power(cert.lift_exponent,modulus)
                self.assertEqual(scalar,1)
                self.assertEqual(radical%A,0)
                self.assertEqual(gcd(radical//A,f),1)
                self.assertEqual(cert.lift_coefficient*cert.correction_index%f,2%f)
                self.assertEqual(
                    independent_unit_matrix_power(cert.ray_period,modulus),(1,0))
                u,v=independent_unit_matrix_power(cert.unit_exponent,modulus)
                x,y=cert.alpha
                beta_x=(u*x+2*v*y)%modulus
                beta_y=(v*x+u*y)%modulus
                r=(A+1)//2
                self.assertEqual(beta_x,(r+A)%modulus)
                self.assertEqual(beta_y,(f*r)%modulus)
                self.assertGreaterEqual(cert.unit_exponent,0)
                self.assertLess(cert.unit_exponent,cert.ray_period)

    def test_anchor_exact_positive_triples_independently_inverted(self):
        for f in (3,5,7,9,15,21,105):
            with self.subTest(f=f):
                seed=wp.positive_triple(f)
                A=f*f
                self.assertEqual(seed.order,2*A+2)
                self.assertEqual(seed.offset,2)
                self.assertEqual(seed.entries[:2],(1,2*A))
                self.assertEqual(len(set(seed.entries)),3)
                self.assertTrue(all(x>0 for x in seed.entries))
                a,b,d=seed.entries
                checked=tuple(independent_polygonal_root(A,z)
                              for z in (a*b+2,a*d+2,b*d+2))
                self.assertTrue(all(x is not None and x>0 for x in checked))
                self.assertEqual(checked,seed.indices)
                self.assertEqual(checked[0],2)

    def test_power_of_three_predecessor_agreement(self):
        for e in (1,2):
            f=3**e
            successor=wp.ray_certificate(f)
            prior=previous.certificate(e)
            self.assertEqual(successor.unit_exponent,prior.constructive_exponent)
            self.assertEqual(successor.ray_period,prior.unit_period)
            self.assertEqual(wp.positive_triple(f).entries,
                             previous.positive_seed(e)[2:5])

    def test_fixed_small_certificate_regressions(self):
        expected={
            3:(12,1,2,23),
            5:(30,2,1,29),
            7:(21,3,3,62),
            9:(108,7,8,863),
            15:(60,11,7,419),
            21:(84,13,5,419),
            35:(210,11,32,6719),
            105:(420,53,4,1679),
        }
        for f, vals in expected.items():
            cert=wp.ray_certificate(f)
            self.assertEqual((cert.lift_exponent,cert.lift_coefficient,
                              cert.correction_index,cert.unit_exponent),vals)

    def test_domain_and_resource_guards_are_not_nonexistence(self):
        for f in (0,1,2,-3,11,13,15*11,3.0,True):
            with self.assertRaises(wp.UnsupportedConductor):
                wp.ray_certificate(f)
        with self.assertRaises(wp.ResourceGuard):
            wp.ray_certificate(3**50,max_conductor_bits=20)
        with self.assertRaises(wp.ResourceGuard):
            wp.positive_triple(35,max_unit_exponent=1000)


if __name__=="__main__":
    unittest.main()
