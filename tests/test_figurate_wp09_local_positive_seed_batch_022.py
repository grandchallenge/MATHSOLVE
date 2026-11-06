"""Independent direct-polynomial tests for WP09-022."""
import unittest
from math import isqrt
from research.figurate_wp09_local_positive_seed_batch_022 import (
    CASES,OFFSET,construct_seed,construct_next_family_member,unit_order_mod,
)

def independent_polygonal(k,n):
    return n+(k-2)*n*(n-1)//2

class LocalPositiveSeedBatch022Tests(unittest.TestCase):
    def test_exact_seeds(self):
        for k in CASES:
            z=construct_seed(k)
            a,b,d=z["entries"];r,s,t=z["indices"]
            self.assertEqual((a,b),(1,k-2))
            self.assertEqual((a*b+OFFSET,a*d+OFFSET,b*d+OFFSET),
                             tuple(independent_polygonal(k,n) for n in (r,s,t)),k)
            self.assertEqual(d,CASES[k][7],k)
            self.assertEqual(len({a,b,d}),3)

    def test_base_norm_and_units(self):
        for k,cfg in CASES.items():
            x0,y0,u,v=cfg[:4]
            delta=8*(k-2)*OFFSET+(k-4)**2
            self.assertEqual(x0*x0-(k-2)*y0*y0,-(k-3)*delta,k)
            self.assertEqual(u*u-(k-2)*v*v,1,k)

    def test_lattice_coordinates(self):
        for k in CASES:
            z=construct_seed(k);x,y=z["pell_coordinates"]
            R=2*(k-2);L=k-4
            self.assertEqual(x%R,(-L)%R,k)
            self.assertEqual(y%R,(-L)%R,k)
            self.assertEqual((x+L)//R,z["indices"][2],k)
            self.assertEqual((y+L)//R,z["indices"][1],k)

    def test_nonsquare_and_infinite_family(self):
        for k in CASES:
            self.assertEqual((k-2)%16,2)
            self.assertNotEqual(isqrt(k-2)**2,k-2)
            seed=construct_seed(k);nxt=construct_next_family_member(k)
            self.assertGreater(nxt["entries"][2],seed["entries"][2],k)
            a,b,d=nxt["entries"];r,s,t=nxt["indices"]
            self.assertEqual((a*b+OFFSET,a*d+OFFSET,b*d+OFFSET),
                             tuple(independent_polygonal(k,n) for n in (r,s,t)),k)
            self.assertEqual(len(str(d)),CASES[k][9],k)

    def test_minimal_unit_orders(self):
        for k,cfg in CASES.items():
            u,v=cfg[2:4];M=4*(k-2);e=cfg[8]
            self.assertEqual(unit_order_mod(k-2,u,v,M),e,k)
            x,y=1,0
            for _ in range(1,e):
                x,y=u*x+(k-2)*v*y,v*x+u*y
                self.assertNotEqual((x%M,y%M),(1,0),k)
            x,y=u*x+(k-2)*v*y,v*x+u*y
            self.assertEqual((x%M,y%M),(1,0),k)

    def test_locally_compatible_parameter_scope(self):
        self.assertEqual(tuple(CASES),(308,340,356))
        for k in CASES:self.assertEqual(k%16,4)

    def test_domain_guards(self):
        from research.figurate_wp09_local_positive_seed_batch_022 import polygonal
        with self.assertRaises(ValueError):construct_seed(324)
        with self.assertRaises(ValueError):polygonal(2,3)

if __name__=="__main__":unittest.main()
