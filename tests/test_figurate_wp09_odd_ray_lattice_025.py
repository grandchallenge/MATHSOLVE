"""Independent exact norm, congruence and complete-decision tests WP09-025."""
import unittest
from math import isqrt
from research.figurate_wp09_odd_ray_lattice_025 import (
    normalized_parameters,ray_admissible,ray_orbit,normalized_decide,
    construct_exact_seed,independent_norm_identity,
)
from research.figurate_wp09_anchor_index_lattice_024 import decide_anchor

def independent_polygonal(k,n):
    return ((k-2)*n*n-(k-4)*n)//2

class OddRayTests(unittest.TestCase):
    def test_symbolic_normalization_all_orders(self):
        for m in range(55):
            k=16*m+4
            p=normalized_parameters(k)
            A=8*m+1
            q=k-2
            L=k-4
            R=2*q
            Delta=8*q*2+L*L
            N=(1-q)*Delta
            self.assertEqual((p["A"],p["Q"]),(A,q))
            self.assertEqual(Delta,32*p["H"])
            self.assertEqual(N,16*p["N"])
            self.assertEqual(R,4*A)
            self.assertEqual(L,2*(A-1))
            self.assertEqual(2*p["target"]%A,1%A)
            self.assertEqual(p["N"],-2*(2*A-1)*p["H"])

    def test_odd_ray_characterization(self):
        for m in range(35):
            k=16*m+4;p=normalized_parameters(k)
            A=p["A"]
            for x in range(0,min(A*2,250)):
                expected=(x-p["target"])%A==0
                self.assertEqual((2*x-1)%A==0,expected)
                self.assertEqual(ray_admissible(p,x,x),expected)
                self.assertEqual(ray_admissible(p,x,x+A),expected)

    def test_complete_equivalence_with_prior_decider(self):
        for k in (20,36,52,68,84,100,308):
            old=decide_anchor(k,max_bound=100000)
            new=normalized_decide(k,max_bound=100000)
            self.assertEqual(new["exists"],old["exists"],k)
            self.assertEqual(new["params"]["A"]*4,old["modulus"])
            self.assertLess(new["complete_bound"],old["complete_bound"])
            if new["exists"]:
                w=construct_exact_seed(new)
                a,b,d=w["entries"]
                r,s,t=w["indices"]
                self.assertEqual((a,b,r),(1,k-2,2))
                self.assertEqual((a*b+2,a*d+2,b*d+2),
                                 tuple(independent_polygonal(k,n) for n in (r,s,t)))
                self.assertTrue(independent_norm_identity(k,s,t,d))

    def test_explicit_exact_308_control(self):
        k,s,t,d=308,49173,860168,369944066839
        self.assertEqual((d+2,(k-2)*d+2),
                         (independent_polygonal(k,s),independent_polygonal(k,t)))
        self.assertTrue(independent_norm_identity(k,s,t,d))
        p=normalized_parameters(k)
        x=p["A"]*t-(p["A"]-1)//2
        y=p["A"]*s-(p["A"]-1)//2
        self.assertTrue(ray_admissible(p,x,y))
        self.assertEqual(x*x-p["Q"]*y*y,p["N"])

    def test_negative_is_fixed_anchor_not_global(self):
        z=normalized_decide(68,max_bound=100000)
        self.assertFalse(z["exists"])
        self.assertGreater(z["complete_bound"],0)
        self.assertIsNone(z["hit"])
        with self.assertRaises(ValueError):
            construct_exact_seed(z)

    def test_guard_and_errors(self):
        for k in (3,8,12,16,24,32):
            with self.assertRaises(ValueError):normalized_parameters(k)
        with self.assertRaises(ValueError):normalized_decide(84,max_bound=1)
        self.assertFalse(independent_norm_identity(308,49173,860168,7))
        self.assertFalse(independent_norm_identity(308,0,860168,369944066839))

    def test_positive_lift_preserves_residue_period(self):
        for k in (84,100,308):
            z=normalized_decide(k,max_bound=100000)
            self.assertTrue(z["exists"])
            self.assertGreaterEqual(z["hit"]["period"],1)
            rep=z["hit"]["representative"]
            again=ray_orbit(z["params"],z["unit"],rep)
            self.assertEqual(again,z["hit"])
            w=construct_exact_seed(z)
            self.assertEqual((w["indices"][1]%2,w["indices"][2]%4),(1,0))
            self.assertEqual(w["entries"][2]%8,7)

if __name__=="__main__":unittest.main()
