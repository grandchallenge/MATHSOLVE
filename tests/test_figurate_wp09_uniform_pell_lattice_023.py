"""Independent integer arithmetic tests for FIGURATE WP09-023."""
import unittest
from math import isqrt
from research.figurate_wp09_uniform_pell_lattice_023 import (
    fundamental_unit, parameters, representative_bound, norm_representatives,
    residue_admissible, orbit_hit, decide, lift_witness,
)

def polygonal_independent(k,n):
    return ((k-2)*n*n-(k-4)*n)//2

class UniformPellLatticeTests(unittest.TestCase):
    def test_fundamental_units(self):
        for q,U,V in ((2,3,2),(82,163,18),(98,99,10),
                      (306,35,2),(354,258065,13716)):
            self.assertEqual(fundamental_unit(q),(U,V))
            self.assertEqual(U*U-q*V*V,1)

    def test_positive_controls_and_exact_lifting(self):
        for k,b in ((84,82),(100,98),(308,306)):
            result=decide(k,2,1,b,2,max_bound=100000)
            self.assertTrue(result["exists"])
            z=lift_witness(result)
            a,b,d=z["entries"]
            r,s,t=z["indices"]
            self.assertEqual((a*b+2,a*d+2,b*d+2),
                             tuple(polygonal_independent(k,n)
                                   for n in (r,s,t)))
            self.assertEqual(len({a,b,d}),3)
            self.assertGreater(d,0)

    def test_complete_negative_fixed_pair(self):
        # k=68,c=2 has an odd-prime obstruction independently proven in WP09-012.
        # This test is for its *fixed first pair* a=1,b=66 only.
        z=decide(68,2,1,66,2,max_bound=100000)
        self.assertFalse(z["exists"])
        self.assertEqual(z["representative_count"],0)
        self.assertGreater(z["complete_bound"],0)

    def test_lattice_residue_periodicity(self):
        p=parameters(84,2,2,41,2)
        M=p["M"]
        for X in range(0,M,19):
            for S in range(0,M,29):
                self.assertEqual(residue_admissible(p,X,S),
                                 residue_admissible(p,X+M,S+M))
        R=p["R"];L=p["L"]
        for s in range(1,70):
            for t in range(1,16):
                X=p["a"]*(R*t-L);S=R*s-L
                self.assertEqual(residue_admissible(p,X,S),
                                 (polygonal_independent(84,s)-2)%p["a"]==0)

    def test_norm_representative_enumeration(self):
        p=parameters(84,2,1,82,2)
        u=fundamental_unit(82)
        reps,cap=norm_representatives(p,u,100000)
        self.assertEqual(cap,representative_bound(p,u))
        independent=[]
        for s in range(1,cap+1):
            n=82*s*s+p["N"]
            if n>0 and isqrt(n)**2==n:
                independent.append((isqrt(n),s))
        self.assertEqual(reps,independent)
        self.assertTrue(any(orbit_hit(p,u,rep) is not None for rep in reps))

    def test_no_false_completion_on_resource_guard(self):
        with self.assertRaises(ValueError):
            decide(84,2,1,82,2,max_bound=100)
        with self.assertRaises(ValueError):
            decide(84,2,1,81,2)
        with self.assertRaises(ValueError):
            fundamental_unit(81)
        with self.assertRaises(ValueError):
            parameters(84,2,1,82,3)

    def test_norm_zero_nonsquare(self):
        p={"N":0,"Q":2}
        self.assertEqual(norm_representatives(p,(3,2)),([],0))

if __name__=="__main__":
    unittest.main()
