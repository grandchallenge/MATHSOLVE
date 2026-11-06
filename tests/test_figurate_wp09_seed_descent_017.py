"""Independent exact arithmetic oracles for WP09-017."""
import unittest
from math import isqrt
from research.figurate_wp09_seed_descent_017 import (
    CONTROL,TARGETS,polygonal,inverse_polygonal,
    recover_entries_from_products,seed_from_two_indices,index_window,fixed_pair_norm,
)

def independent_polygonal(k,n):
    return n+(k-2)*n*(n-1)//2

def oracle(k,c,r,s):
    A=independent_polygonal(k,r)-c
    B=independent_polygonal(k,s)-c
    if min(A,B)<=0:return []
    results=[]
    for a in range(1,min(A,B)+1):
        if A%a or B%a:continue
        b=A//a;d=B//a
        if len({a,b,d})!=3:continue
        n=1
        while independent_polygonal(k,n)<=b*d+c:
            if independent_polygonal(k,n)==b*d+c:
                results.append((a,b,d,r,s,n))
            n+=1
    return sorted(results)

class SeedDescentTests(unittest.TestCase):
    def test_exact_product_recovery(self):
        self.assertEqual(recover_entries_from_products(6,10,15),(2,3,5))
        self.assertIsNone(recover_entries_from_products(32,2,2))
        self.assertIsNone(recover_entries_from_products(2,2,2))
        self.assertIsNone(recover_entries_from_products(3,4,5))
        self.assertIsNone(recover_entries_from_products(0,4,5))

    def test_positive_control_and_norm(self):
        k,c,a,b,d,r,s,t=CONTROL
        self.assertEqual((a*b+c,a*d+c,b*d+c),
                         tuple(independent_polygonal(k,n) for n in (r,s,t)))
        self.assertEqual(recover_entries_from_products(a*b,a*d,b*d),(a,b,d))
        found=seed_from_two_indices(k,c,r,s)
        self.assertIn((a,b,d),[tuple(z["entries"]) for z in found])
        self.assertIn((r,s,t),[tuple(z["indices"]) for z in found])
        norm=fixed_pair_norm(k,c,a,b,r)
        self.assertEqual(norm["q"],440330)
        X=a*(norm["R"]*t-norm["L"])
        S=norm["R"]*s-norm["L"]
        self.assertEqual(X*X-a*b*S*S,norm["N"])

    def test_independent_small_index_oracle(self):
        for k,c in ((84,2),(100,2),(52,6),(68,6)):
            for r in range(1,9):
                for s in range(r+1,13):
                    result=seed_from_two_indices(k,c,r,s)
                    got=sorted((*z["entries"],*z["indices"]) for z in result)
                    self.assertEqual(got,oracle(k,c,r,s),(k,c,r,s))

    def test_finite_negative_is_not_global(self):
        for k,c in TARGETS:
            z=index_window(k,c,24,60)
            self.assertEqual(z["seeds"],[])
            self.assertFalse(z["global_nonexistence_proved"])

    def test_inverse_polygonal(self):
        for k in (52,68,84,100):
            for n in range(1,65):
                self.assertEqual(inverse_polygonal(k,independent_polygonal(k,n)),n)
            self.assertIsNone(inverse_polygonal(k,-2))

    def test_domain_checks(self):
        for args in ((84,2,0,3),(84,2,3,3),(2,2,1,3)):
            with self.assertRaises(ValueError):seed_from_two_indices(*args)
        with self.assertRaises(ValueError):index_window(84,2,0,10)
        with self.assertRaises(ValueError):fixed_pair_norm(84,2,2,3,1)

if __name__=="__main__":unittest.main()
