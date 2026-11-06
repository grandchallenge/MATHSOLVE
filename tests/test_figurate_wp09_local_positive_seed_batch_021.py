"""Independent exact arithmetic checks for four WP09-021 Pell seeds."""
import unittest
from math import isqrt
from research.figurate_wp09_local_positive_seed_batch_021 import (
    CASES,OFFSET,construct_seed,construct_next_family_member,
    unit_order_mod,polygonal,
)

def independent_polygonal(k,n):
    return n+(k-2)*n*(n-1)//2

class LocalPositiveSeedBatchTests(unittest.TestCase):
    def test_exact_seeds_direct_polynomial(self):
        for k in CASES:
            result=construct_seed(k)
            a,b,d=result["entries"]
            r,s,t=result["indices"]
            self.assertEqual((a,b),(1,k-2))
            self.assertEqual(
                (a*b+OFFSET,a*d+OFFSET,b*d+OFFSET),
                tuple(independent_polygonal(k,n) for n in (r,s,t)),
                k,
            )
            self.assertEqual(len({a,b,d}),3)
            self.assertEqual(d,CASES[k][7])

    def test_pell_base_points_and_units(self):
        for k,config in CASES.items():
            x0,y0,u,v,steps=config[:5]
            D=k-2
            delta=8*(k-2)*OFFSET+(k-4)**2
            norm=-(k-3)*delta
            self.assertEqual(x0*x0-D*y0*y0,norm,k)
            self.assertEqual(u*u-D*v*v,1,k)
            result=construct_seed(k)
            x,y=result["pell_coordinates"]
            self.assertEqual(x*x-D*y*y,norm,k)

    def test_index_lattice(self):
        for k in CASES:
            z=construct_seed(k)
            x,y=z["pell_coordinates"]
            R=2*(k-2);L=k-4
            self.assertEqual(x%R,(-L)%R,k)
            self.assertEqual(y%R,(-L)%R,k)
            self.assertEqual((y+L)//R,z["indices"][1],k)
            self.assertEqual((x+L)//R,z["indices"][2],k)

    def test_nonsquare_first_pair_and_infinite_family(self):
        for k in CASES:
            self.assertEqual((k-2)%16,2)
            self.assertNotEqual(isqrt(k-2)**2,k-2)
            seed=construct_seed(k)
            nxt=construct_next_family_member(k)
            self.assertGreater(nxt["entries"][2],seed["entries"][2],k)
            a,b,d=nxt["entries"]
            r,s,t=nxt["indices"]
            self.assertEqual(
                (a*b+OFFSET,a*d+OFFSET,b*d+OFFSET),
                tuple(independent_polygonal(k,n) for n in (r,s,t)),
                k,
            )
            self.assertEqual(len(str(d)),CASES[k][9],k)

    def test_minimal_modular_unit_orders(self):
        for k,config in CASES.items():
            u,v=config[2:4]
            M=2*(2*(k-2))
            expected=config[8]
            self.assertEqual(unit_order_mod(k-2,u,v,M),expected,k)
            x,y=1,0
            for _ in range(1,expected):
                x,y=u*x+(k-2)*v*y,v*x+u*y
                self.assertNotEqual((x%M,y%M),(1,0),k)
            x,y=u*x+(k-2)*v*y,v*x+u*y
            self.assertEqual((x%M,y%M),(1,0),k)

    def test_all_orders_are_locally_compatible_targets(self):
        self.assertEqual(tuple(CASES),(164,196,228,244))
        for k in CASES:
            self.assertEqual(k%16,4)
            self.assertEqual((k-2)%16,2)

    def test_domain_guards(self):
        with self.assertRaises(ValueError):
            construct_seed(84)
        with self.assertRaises(ValueError):
            polygonal(2,3)

if __name__=="__main__":
    unittest.main()
