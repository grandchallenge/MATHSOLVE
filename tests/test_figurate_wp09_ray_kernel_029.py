"""WP09-029 independent exact checks of dual-number units and finite kernel."""
import unittest
from math import gcd
from research.figurate_wp09_ray_kernel_029 import (
    residue_map,residue_product,residue_power,ray_kernel,prime_factors,
    expected_residue_group_size,rigorously_classified_full_ray_group
)
from research.figurate_wp09_uniform_pell_lattice_023 import fundamental_unit
from research.figurate_wp09_ray_class_conductor_027 import order_data

def direct_product(A,x,y,u,v):
    return ((x*u+2*A*y*v)%A,(x*v+y*u)%A)

class RayKernelTests(unittest.TestCase):
    def test_dual_number_isomorphism_independent_ring_product(self):
        for A in (1,3,5,9,17,25,41):
            for x in range(A):
                if gcd(x,A)!=1:continue
                for y in range(min(A,5)):
                    for u in range(A):
                        if gcd(u,A)!=1:continue
                        for v in range(min(A,4)):
                            p=residue_map(A,x,y);q=residue_map(A,u,v)
                            a,b=direct_product(A,x,y,u,v)
                            self.assertEqual(residue_map(A,a,b),
                                             residue_product(A,p,q))

    def test_unit_orbit_and_quotient_index(self):
        for m in range(9):
            z=ray_kernel(m)
            A=z["A"];U,V=z["fundamental_positive_unit"]
            self.assertEqual(U*U-z["D"]*V*V,1)
            self.assertEqual(gcd(z["D"],A),A if A==1 else A)
            self.assertEqual(z["residue_group_size"],
                             expected_residue_group_size(A))
            self.assertEqual(z["residue_group_size"],
                             z["kernel_order"]*z["positive_unit_residue_order"])
            self.assertEqual(z["conductor"],order_data(m)["f"])
            self.assertEqual(z["unit_residue"],residue_map(A,U,V))
            product=1
            for factor in z["kernel_invariant_factors"]:product*=factor
            self.assertEqual(product,z["kernel_order"])
            self.assertTrue(all(b%a==0 for a,b in zip(
                z["kernel_invariant_factors"],z["kernel_invariant_factors"][1:])))
            self.assertFalse(z["full_ray_class_group_computed"])
            self.assertFalse(z["narrow_picard_group_computed"])
            self.assertTrue(z["ray_kernel_complete"])

    def test_unit_subgroup_order_independent_brute(self):
        for m in (0,1,2,3,5,6):
            z=ray_kernel(m);A=z["A"];U,V=z["fundamental_positive_unit"]
            x,y=1%A,0
            seen=set()
            while (x,y) not in seen:
                seen.add((x,y))
                x,y=direct_product(A,x,y,U% A,V%A)
            self.assertEqual((x,y),(1%A,0))
            self.assertEqual(len(seen),z["positive_unit_residue_order"])

    def test_kernel_classes_independent_order_distribution(self):
        # Direct coset enumeration and element orders, independent of
        # prime-power torsion used to recover invariant factors.
        for m in (1,2,3):
            z=ray_kernel(m)
            A=z["A"];u=z["unit_residue"]
            H=[];p=(1%A,0)
            while p not in H:
                H.append(p)
                p=residue_product(A,p,u)
            all_points={(x,t) for x in range(A)
                        if gcd(x,A)==1 for t in range(A)}
            seen=set();orders=[]
            for g in sorted(all_points):
                if g in seen:continue
                coset={residue_product(A,g,h) for h in H}
                seen.update(coset)
                q=(1%A,0);j=0
                while True:
                    j+=1;q=residue_product(A,q,g)
                    if q in H:break
                    self.assertLessEqual(j,len(all_points))
                orders.append(j)
            self.assertEqual(len(seen),len(all_points))
            self.assertEqual(len(orders),z["kernel_order"])
            # Compare counts of elements annihilated by every tested e.
            factors=z["kernel_invariant_factors"]
            for exponent in (1,2,3,4,6,8,12):
                lhs=sum(exponent%j==0 for j in orders)
                rhs=1
                for factor in factors:rhs*=gcd(exponent,factor)
                self.assertEqual(lhs,rhs,(m,exponent))

    def test_explicit_trivial_modulus_and_known_conductors(self):
        self.assertEqual(ray_kernel(0)["kernel_order"],1)
        self.assertEqual(ray_kernel(0)["kernel_invariant_factors"],[])
        self.assertEqual(ray_kernel(1)["conductor"],3)
        self.assertEqual(ray_kernel(3)["conductor"],5)
        self.assertEqual(ray_kernel(6)["conductor"],7)

    def test_small_kernel_invariant_factors(self):
        expected={
            0:[],1:[3],2:[16],3:[10],4:[10],5:[20],
            6:[42],7:[3,18],8:[2,60],9:[36],
        }
        for m,group in expected.items():
            self.assertEqual(ray_kernel(m)["kernel_invariant_factors"],group)

    def test_two_rigorously_classified_full_groups(self):
        self.assertEqual(
            rigorously_classified_full_ray_group(0)["full_group_invariant_factors"],[])
        self.assertEqual(
            rigorously_classified_full_ray_group(1)["full_group_invariant_factors"],[6])
        with self.assertRaises(ValueError):
            rigorously_classified_full_ray_group(2)

    def test_guard_and_domain_errors(self):
        with self.assertRaises(ValueError):ray_kernel(-1)
        with self.assertRaises(ValueError):ray_kernel(5,max_states=1)
        with self.assertRaises(ValueError):residue_map(9,3,2)
        with self.assertRaises(ValueError):prime_factors(0)
        with self.assertRaises(ValueError):residue_power(9,(1,1),-1)

if __name__=="__main__":unittest.main()
