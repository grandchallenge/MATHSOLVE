"""Independent exact quadratic-order conductor Picard oracles (WP09-030)."""
import unittest
from math import gcd

from research.figurate_wp09_square_conductor_picard_030 import (
    narrow_picard_square_conductor, full_ray_order_square_conductor,
    theoretical_projective_order, ring_mul, ring_pow, ring_is_unit,
)
from research.figurate_wp09_ray_kernel_029 import ray_kernel


def brute_projective_classes(f):
    units = {(x,y) for x in range(f) for y in range(f)
             if gcd(x*x-2*y*y,f)==1}
    scalars = [s for s in range(f) if gcd(s,f)==1]
    visited = set()
    classes = []
    for z in sorted(units):
        if z in visited:
            continue
        orbit = {(z[0]*s%f,z[1]*s%f) for s in scalars}
        visited.update(orbit)
        classes.append(orbit)
    if visited != units:
        raise AssertionError("independent projective partition incomplete")
    return classes


def independent_unit_period(f,positive):
    x,y=1%f,0
    e=(3%f,2%f) if positive else (1%f,1%f)
    for n in range(1, f*f+2):
        x,y=(x*e[0]+2*y*e[1])%f,(x*e[1]+y*e[0])%f
        if y==0 and gcd(x,f)==1:
            return n
    raise AssertionError("period exceeded exact finite bound")


def independent_narrow_quotient(f):
    units={(x,y) for x in range(f) for y in range(f)
           if gcd(x*x-2*y*y,f)==1}
    scalars=[s for s in range(f) if gcd(s,f)==1]
    q=(3%f,2%f)
    subgroup=set()
    e=(1%f,0)
    while e not in subgroup:
        for s in scalars:
            subgroup.add((e[0]*s%f,e[1]*s%f))
        e=((e[0]*q[0]+2*e[1]*q[1])%f,
           (e[0]*q[1]+e[1]*q[0])%f)
        if len(subgroup)>len(units):
            raise AssertionError("bad subgroup")
    if e!=(1%f,0):
        # The loop may stop at a scalar, while the subgroup contains it.
        if e[1]!=0:
            raise AssertionError("bad positive-unit relation")
    seen=set()
    reps=[]
    for z in sorted(units):
        if z in seen: continue
        orbit={((z[0]*h[0]+2*z[1]*h[1])%f,
                (z[0]*h[1]+z[1]*h[0])%f) for h in subgroup}
        seen.update(orbit)
        reps.append(z)
    if seen!=units:
        raise AssertionError("bad coset partition")
    return len(reps)


class SquareConductorPicardTests(unittest.TestCase):
    def test_direct_maximal_ring_multiplication(self):
        for f in (1,3,5,7,9,11):
            for x in range(f):
                for y in range(f):
                    z=(x,y)
                    self.assertEqual(ring_mul(f,z,(1%f,0)),z)
                    self.assertEqual(ring_mul(f,z,(0,1%f)),
                                     ((2*y)%f,x))
                    self.assertEqual(ring_is_unit(f,z),
                                     gcd(x*x-2*y*y,f)==1)
                    self.assertEqual(ring_pow(f,z,2),ring_mul(f,z,z))

    def test_projective_conductor_formula(self):
        for f in range(1,50,2):
            q=brute_projective_classes(f)
            self.assertEqual(len(q),theoretical_projective_order(f))

    def test_exact_narrow_order_against_second_coset_oracle(self):
        for f in (1,3,5,7,9,11,13,15,17,19,21):
            data=narrow_picard_square_conductor(f)
            period=independent_unit_period(f,False)
            positive_period=independent_unit_period(f,True)
            self.assertEqual(data["fundamental_negative_unit_projective_order"],
                             period)
            self.assertEqual(data["positive_unit_projective_order"],
                             positive_period)
            self.assertEqual(data["narrow_picard_order"],
                             independent_narrow_quotient(f))
            self.assertEqual(data["ordinary_picard_order"],
                             theoretical_projective_order(f)//period)
            product=1
            for factor in data["narrow_picard_invariant_factors"]:
                product*=factor
            self.assertEqual(product,data["narrow_picard_order"])

    def test_specific_nonmaximal_group_invariants(self):
        expected={
            1:[],3:[2],5:[2],7:[2],9:[2],
            11:[2],13:[2],15:[2,2],17:[4],
            19:[2],21:[2,2]
        }
        for f,inv in expected.items():
            self.assertEqual(narrow_picard_square_conductor(f)
                             ["narrow_picard_invariant_factors"],inv)

    def test_full_oriented_ray_orders_not_unsupported_group_laws(self):
        expected={
            1:(0,1),3:(1,6),5:(3,20),7:(6,84),9:(10,54),
            11:(15,110),13:(21,2028),15:(28,720),
            17:(36,544),19:(45,342),21:(55,1512)
        }
        for f,(m,order) in expected.items():
            z=full_ray_order_square_conductor(f)
            self.assertEqual(z["m"],m)
            self.assertEqual(z["full_oriented_ray_group_order"],order)
            self.assertEqual(z["full_oriented_ray_group_order"],
                             z["narrow_picard_order"]*
                             ray_kernel(m)["kernel_order"])
            self.assertEqual(z["full_oriented_ray_group_complete"],f in (1,3))
            if f not in (1,3):
                self.assertIsNone(z["full_oriented_ray_invariant_factors"])

    def test_resource_guards_never_return_partial_no(self):
        with self.assertRaises(ValueError):
            narrow_picard_square_conductor(21,max_residues=100)
        with self.assertRaises(ValueError):
            full_ray_order_square_conductor(21,max_ray_states=5)
        for f in (-1,0,2,4):
            with self.assertRaises(ValueError):
                narrow_picard_square_conductor(f)
        with self.assertRaises(ValueError):
            theoretical_projective_order(0)
        with self.assertRaises(ValueError):
            ring_pow(5,(1,1),-1)


if __name__=="__main__":
    unittest.main()
