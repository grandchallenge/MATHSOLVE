"""Independent integer exact regression for FIGURATE WP09-034.

Independent unit matrix action, brute finite cyclic ray oracle, norm identity,
polygonal discriminant inversion, CRT contradiction, and predecessor comparison.
"""
from __future__ import annotations

from math import gcd, isqrt
import unittest

from research import figurate_wp09_prime_general_crt_034 as wp
from research import figurate_wp09_mixed_conductor_realization_033 as prev


def matrix_unit(n: int, m: int) -> tuple[int,int]:
    """Compute [[3,4],[2,3]]**n times (1,0), independent of producer ring power."""
    a,b,c,d = 3%m,4%m,2%m,3%m
    x,y = 1,0
    while n:
        if n&1: x,y = (a*x+b*y)%m,(c*x+d*y)%m
        a,b,c,d = ((a*a+b*c)%m,(a*b+b*d)%m,
                     (c*a+d*c)%m,(c*b+d*d)%m)
        n//=2
    return x,y


def brute_order(p: int) -> int:
    x,y = 1,0
    for n in range(1,p+2):
        x,y = (3*x+4*y)%p,(2*x+3*y)%p
        if (x,y)==(1,0):
            return n
    raise AssertionError("no norm-one order found")


def brute_ray_exponents(p: int, period: int) -> list[int]:
    mod=p**3
    x,y=1,0
    rays=[]
    for n in range(period):
        if (x,y)==(1,2*p*p%mod):
            rays.append(n)
        x,y = (3*x+4*y)%mod,(2*x+3*y)%mod
    if (x,y)!=(1,0):
        raise AssertionError("period not cyclic")
    return rays


def independent_index(A: int, z: int) -> int|None:
    if z<1:return None
    disc=(A-1)**2+4*A*z
    rt=isqrt(disc)
    if rt*rt!=disc or (A-1+rt)%(2*A):return None
    t=(A-1+rt)//(2*A)
    return t if t>0 else None


class PrimeGeneralCRTTests(unittest.TestCase):
    def test_prime_orders_independently_bruteforced(self):
        known={3:4,5:6,7:3,11:12,13:14,17:8,19:20,23:11,
               29:10,31:15,37:38,41:5,73:36}
        for p,t in known.items():
            with self.subTest(p=p):
                self.assertEqual(brute_order(p),t)
                self.assertEqual(wp.unit_order_mod_prime(p),t)

    def test_two_pell_wieferich_base_valuations(self):
        for p in (13,31):
            with self.subTest(p=p):
                t=brute_order(p)
                x,y=matrix_unit(t,p**3)
                self.assertEqual(x%p,1)
                self.assertEqual(y%(p*p),0)
                self.assertNotEqual(y%(p**3),0)
                record=wp.decide_alpha_orbit(p)
                self.assertIsInstance(record,wp.RaySuccess)
                self.assertEqual(record.conditions[0].unit_slope_valuation,2)

    def test_finite_independent_cyclic_ray_oracles(self):
        for p in (3,5,7,11,13,31):
            with self.subTest(p=p):
                z=wp.decide_alpha_orbit(p)
                self.assertIsInstance(z,wp.RaySuccess)
                period=z.conditions[0].exponent_modulus
                found=brute_ray_exponents(p,period)
                self.assertEqual(found,[z.unit_exponent+1])
                self.assertEqual(z.unit_period,period)

    def test_unbounded_single_prime_power_families(self):
        for p in (3,5,7,11,13,17,19,23,31,37,41,73):
            for e in (1,2):
                with self.subTest(p=p,e=e):
                    f=p**e
                    z=wp.decide_alpha_orbit(f)
                    self.assertIsInstance(z,wp.RaySuccess)
                    m=f**3
                    self.assertEqual(matrix_unit(z.unit_exponent+1,m),
                                     (1,2*f*f % m))
                    self.assertEqual(matrix_unit(z.unit_period,m),(1,0))
                    self.assertEqual(z.beta_mod_f_cubed,
                                     (((f*f+1)//2+f*f)%m,
                                      f*((f*f+1)//2)%m))

    def test_compatible_mixed_conductors_and_predecessors(self):
        for f in (15,21,35,105,33,39,65,93,155,365,403,429,511,1209):
            with self.subTest(f=f):
                z=wp.decide_alpha_orbit(f)
                self.assertIsInstance(z,wp.RaySuccess)
                self.assertEqual(matrix_unit(z.unit_exponent+1,f**3),
                                 (1,2*f*f%(f**3)))
        for f in (3,5,7,9,15,21,35,49,75,105,315):
            with self.subTest(predecessor=f):
                self.assertIsInstance(wp.decide_alpha_orbit(f),wp.RaySuccess)
                self.assertEqual(prev.ray_certificate(f).A,f*f)

    def test_full_positive_polygonal_indices_independent(self):
        for f in (3,5,7,11,13,17,19,23,31,33,39,65,93,155):
            with self.subTest(f=f):
                v=wp.positive_triple(f)
                A=f*f
                a,b,d=v.entries
                self.assertEqual(v.order,2*A+2)
                self.assertEqual((a,b),(1,2*A))
                self.assertEqual(len({a,b,d}),3)
                self.assertTrue(all(x>0 for x in (a,b,d)))
                inds=tuple(independent_index(A,z) for z in (a*b+2,a*d+2,b*d+2))
                self.assertTrue(all(x is not None and x>0 for x in inds))
                self.assertEqual(v.indices,inds)
                self.assertEqual(inds[0],2)

    def test_mixed_3_times_73_is_only_orbit_obstructed(self):
        f=3*73
        z=wp.decide_alpha_orbit(f)
        self.assertIsInstance(z,wp.OrbitObstruction)
        self.assertEqual(z.reason,"crt-incompatible")
        self.assertEqual([(v.prime,v.unit_order,v.unit_slope_valuation)
                          for v in z.conditions],[(3,4,1),(73,36,1)])
        a,b=z.conditions
        self.assertEqual(a.exponent_modulus,36)
        self.assertEqual(a.exponent_residue%36,24)
        self.assertEqual(b.exponent_residue%36,0)
        self.assertEqual(gcd(a.exponent_modulus,b.exponent_modulus),36)
        # This is NOT a global statement about Type B, other ideals, or first pairs.
        with self.assertRaisesRegex(ValueError,"other solutions NOT ruled out"):
            wp.positive_triple(f)

    def test_domain_and_resource_guards(self):
        for f in (1,2,0,-3,13.0,True):
            with self.assertRaises(ValueError):
                wp.decide_alpha_orbit(f)
        with self.assertRaises(wp.ResourceGuard):
            wp.decide_alpha_orbit(3**40,max_conductor_bits=32)
        with self.assertRaises(wp.ResourceGuard):
            wp.decide_alpha_orbit(101*103,max_trial_divisor=7)
        with self.assertRaises(wp.ResourceGuard):
            wp.positive_triple(73,max_unit_exponent=1000)
        self.assertEqual(wp.factor(2**4*3**2*11),((2,4),(3,2),(11,1)))


if __name__=="__main__":
    unittest.main()
