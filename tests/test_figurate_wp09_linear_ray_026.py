"""Independent finite-orbit and modular polynomial controls for WP09-026."""
import unittest
from math import gcd
from research.figurate_wp09_linear_ray_026 import (
    solve_linear_congruence,linear_ray_hit,linear_gcd_decide,
    verified_hit_modulo,
)
from research.figurate_wp09_odd_ray_lattice_025 import (
    normalized_parameters,normalized_decide,ray_orbit,construct_exact_seed,
)
from research.figurate_wp09_uniform_pell_lattice_023 import fundamental_unit

def independent_P(k,n):
    return ((k-2)*n*n-(k-4)*n)//2

class LinearRayTests(unittest.TestCase):
    def test_linear_congruence_against_brute(self):
        for modulus in range(1,71):
            for coefficient in range(-8,9):
                for rhs in range(-8,9):
                    brute=next((j for j in range(modulus)
                                if (coefficient*j-rhs)%modulus==0),None)
                    self.assertEqual(solve_linear_congruence(coefficient,rhs,modulus),
                                     brute,(modulus,coefficient,rhs))
        with self.assertRaises(ValueError):
            solve_linear_congruence(1,1,0)

    def test_matrix_power_identity(self):
        for m in range(0,22):
            p=normalized_parameters(16*m+4)
            A,Q=p["A"],p["Q"];U,V=fundamental_unit(Q)
            self.assertEqual(U*U%A,1%A)
            for x0,y0 in ((1,0),(2,3),(A//2+1,A//3+1)):
                x,y=x0%A,y0%A
                for n in range(20):
                    if n%2==0:
                        j=n//2
                        xx=x0%A; yy=(y0+2*j*U*V*x0)%A
                    else:
                        j=(n-1)//2
                        xx=U*x0%A
                        yy=(U*y0+(2*j+1)*V*x0)%A
                    self.assertEqual((x,y),(xx,yy),(m,n,x0,y0))
                    x,y=(U*x+Q*V*y)%A,(V*x+U*y)%A

    def test_linear_ray_equivalent_to_full_orbit(self):
        for m in range(0,30):
            p=normalized_parameters(16*m+4)
            unit=fundamental_unit(p["Q"])
            A=p["A"]
            for rep in ((1,1),(2,3),(A//2+1,A//3+1),
                        ((A+1)//2,(A+1)//2),(A+1,A+5)):
                full=ray_orbit(p,unit,rep)
                linear=linear_ray_hit(p,unit,rep)
                self.assertEqual(full is None,linear is None,(m,rep))
                if linear:
                    self.assertEqual(full["step"],linear["step"],(m,rep))
                    self.assertTrue(verified_hit_modulo(p,unit,rep,linear["step"]))
                    self.assertTrue(verified_hit_modulo(
                        p,unit,rep,linear["step"]+linear["period"]))
                else:
                    self.assertFalse(any(
                        verified_hit_modulo(p,unit,rep,j)
                        for j in range(2*A+1)
                    ))

    def test_full_anchor_decisions_and_exact_seeds(self):
        for k in (4,20,36,52,68,84,100,308):
            old=normalized_decide(k,max_bound=100000)
            new=linear_gcd_decide(k,max_bound=100000)
            self.assertEqual(new["exists"],old["exists"])
            self.assertEqual(new["complete_bound"],old["complete_bound"])
            self.assertEqual(new["representative_count"],old["representative_count"])
            self.assertFalse(new["orbit_enumeration_required"])
            if new["exists"]:
                w=construct_exact_seed(new)
                a,b,d=w["entries"];r,s,t=w["indices"]
                self.assertEqual((a,b,r),(1,k-2,2))
                self.assertEqual((a*b+2,a*d+2,b*d+2),
                                 (independent_P(k,r),independent_P(k,s),independent_P(k,t)))
        self.assertFalse(linear_gcd_decide(68,100000)["exists"])

    def test_nontrivial_gcd_branches(self):
        for m in range(2,50):
            p=normalized_parameters(16*m+4)
            A=p["A"];U,V=fundamental_unit(p["Q"])
            g=gcd(V,A)
            self.assertEqual(gcd(2*U,A),1)
            self.assertEqual(gcd(2*V*((A+1)//2),A),g)
            rep=((A+1)//2,(A+1)//2)
            hit=linear_ray_hit(p,(U,V),rep)
            self.assertIsNotNone(hit)
            self.assertEqual(hit["step"],0)
            self.assertEqual(hit["period"],2*(A//g))

    def test_guard_and_invalid_units(self):
        with self.assertRaises(ValueError):
            linear_gcd_decide(84,max_bound=0)
        p=normalized_parameters(84)
        with self.assertRaises(ValueError):
            linear_ray_hit(p,(2,3),(1,1))
        with self.assertRaises(ValueError):
            verified_hit_modulo(p,fundamental_unit(82),(1,1),-1)

if __name__=="__main__":unittest.main()
