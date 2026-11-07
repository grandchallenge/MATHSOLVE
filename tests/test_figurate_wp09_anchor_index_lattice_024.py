"""Independent modular and exact-integer controls for FIGURATE WP09-024."""
import unittest
from research.figurate_wp09_anchor_index_lattice_024 import (
    index_period,sufficient_residue_modulus,anchor_params,
    anchor_branch_predicate,optimized_orbit_decision,
    verify_anchor_witness,decide_anchor,
)
from research.figurate_wp09_uniform_pell_lattice_023 import (
    decide,lift_witness,
)

def independent_P(k,n):
    return ((k-2)*n*n-(k-4)*n)//2

class UniformAnchorTests(unittest.TestCase):
    def test_polynomial_period_all_parities(self):
        for k in range(3,35):
            for a in range(1,16):
                h=index_period(k,a)
                self.assertEqual(h,a if (k%2==0 or a%2==1) else 2*a)
                for n in range(1,35):
                    self.assertEqual((independent_P(k,n+h)-independent_P(k,n))%a,0)
                self.assertEqual(sufficient_residue_modulus(k,a),2*(k-2)*h)

    def test_even_k_optimized_modulus(self):
        for k,c,a,b,r in ((84,2,1,82,2),(100,2,1,98,2),
                          (308,2,1,306,2),(68,2,1,66,2)):
            original=decide(k,c,a,b,r,max_bound=100000)
            better=optimized_orbit_decision(k,c,a,b,r,max_bound=100000)
            self.assertEqual(original["exists"],better["exists"])
            self.assertEqual(better["modulus"],original["params"]["M"]//2)
            self.assertEqual(original["complete_bound"],better["complete_bound"])
            if better["exists"]:
                found=lift_witness(better)
                a,b,d=found["entries"]
                r,s,t=found["indices"]
                self.assertEqual((a*b+c,a*d+c,b*d+c),
                                 tuple(independent_P(k,n) for n in (r,s,t)))

    def test_stronger_2_adic_anchor_branches(self):
        for m in range(0,45):
            k=16*m+4;q=k-2
            for s in range(1,80):
                d=independent_P(k,s)-2
                rhs=q*d+2
                if s%2==0:
                    # P(t) mod4 is a square, while rhs=2 mod4.
                    self.assertEqual(rhs%4,2)
                else:
                    self.assertEqual(d%8,7)
                    predicted=16*((m+((s*s-1)//8))%2)
                    self.assertEqual(rhs%32,predicted,(k,s))
                    # A third polygonal index (if it exists) is t=0 or 4 mod8.
                    for t in range(1,33):
                        if independent_P(k,t)%32==rhs%32:
                            self.assertTrue(t%4==0)
                            self.assertEqual(t%8,4*((m+((s*s-1)//8))%2))

    def test_exact_known_anchor_seeds(self):
        for k in (84,100,308):
            yes=decide_anchor(k,max_bound=100000)
            self.assertTrue(yes["exists"])
            w=lift_witness(yes)
            a,b,d=w["entries"];_,s,t=w["indices"]
            self.assertEqual((a,b),(1,k-2))
            self.assertTrue(anchor_branch_predicate(k,s,t,d))
            self.assertTrue(verify_anchor_witness(k,s,t,d))
            self.assertEqual(s%2,1)
            self.assertEqual(t%4,0)

    def test_known_negative_anchor(self):
        z=decide_anchor(68,max_bound=100000)
        self.assertFalse(z["exists"])
        self.assertEqual(z["modulus"],2*(68-2))
        with self.assertRaises(ValueError):
            decide_anchor(84,max_bound=0)

    def test_odd_order_even_entry_requires_full_period(self):
        self.assertEqual(index_period(5,2),4)
        self.assertEqual(sufficient_residue_modulus(5,2),24)
        self.assertEqual(index_period(5,3),3)
        self.assertEqual(sufficient_residue_modulus(5,3),18)
        self.assertEqual(index_period(6,2),2)
        self.assertEqual(sufficient_residue_modulus(6,2),16)

    def test_invalid_domains_and_necessary_only(self):
        for k in (3,8,12,16,24,32):
            with self.assertRaises(ValueError):anchor_params(k)
        with self.assertRaises(ValueError):index_period(2,2)
        with self.assertRaises(ValueError):index_period(84,0)
        with self.assertRaises(ValueError):anchor_branch_predicate(84,0,4,7)
        # Congruences are necessary, not sufficient.
        self.assertTrue(anchor_branch_predicate(84,1,0+4,7))
        self.assertFalse(verify_anchor_witness(84,1,4,7))

if __name__=="__main__":unittest.main()
