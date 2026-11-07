"""Independent source-formula and conductor controls for WP09-027."""
import unittest
from math import gcd
from research.figurate_wp09_ray_class_conductor_027 import (
    order_data, square_factor, prime_valuations, inert_prime_obstructions,
    verify_ray_generator, squarefree_order_generator,
)

def alternate_polygonal(k,n):
    return n+(k-2)*n*(n-1)//2

class ConductorRayTests(unittest.TestCase):
    def test_square_factor_exact(self):
        for n in range(1,2000):
            f,d=square_factor(n)
            self.assertEqual(f*f*d,n)
            self.assertTrue(all(d%(p*p) for p in range(2,int(d**.5)+1)))
        self.assertEqual(square_factor(81*7),(9,7))
        with self.assertRaises(ValueError):square_factor(0)

    def test_conductor_and_discriminants(self):
        for m in range(500):
            z=order_data(m)
            A=8*m+1
            f=z["f"];d=z["squarefree_d"]
            self.assertEqual(f*f*d,2*A)
            self.assertEqual(d%4,2)
            self.assertEqual(z["field_discriminant"],4*d)
            self.assertEqual(z["order_discriminant"],8*A)
            self.assertEqual(z["order_discriminant"],
                             f*f*z["field_discriminant"])
            self.assertEqual(gcd(abs(z["N"]),A),1)
            self.assertEqual(gcd(abs(z["rho_norm"]),A),1)
            self.assertTrue(z["conductor_coprime_norm"])

    def test_nonmaximal_conductor_examples(self):
        # A=9 (m=1), 25 (m=3), 49 (m=6): nonmaximal orders.
        for m,f in ((1,3),(3,5),(6,7)):
            z=order_data(m)
            self.assertEqual(z["f"],f)
            self.assertEqual(z["squarefree_d"],2)
            self.assertEqual(z["field_discriminant"],8)
        self.assertEqual(order_data(5)["f"],1)  # A=41 squarefree

    def test_known_positive_ray_generators(self):
        # Protected FIGURATE seeds: (k,s,t,d).
        for k,s,t,d in ((308,49173,860168,369944066839),):
            m=(k-4)//16
            z=squarefree_order_generator(m,s,t)
            self.assertTrue(z["valid"],(k,z))
            self.assertEqual(alternate_polygonal(k,s),d+2)
            self.assertEqual(alternate_polygonal(k,t),(k-2)*d+2)
            self.assertEqual((z["x"]*z["x"]-
                              order_data(m)["D"]*z["y"]*z["y"]),
                             order_data(m)["N"])

    def test_generated_anchor_controls_checked_independently(self):
        from research.figurate_wp09_odd_ray_lattice_025 import (
            normalized_decide,construct_exact_seed
        )
        for k in (84,100):
            witness=construct_exact_seed(normalized_decide(k,100000))
            _,s,t=witness["indices"];_,b,d=witness["entries"]
            self.assertEqual(b,k-2)
            self.assertTrue(squarefree_order_generator((k-4)//16,s,t)["valid"])
            self.assertEqual((independent_polygonal(k,s),independent_polygonal(k,t)),
                             (d+2,b*d+2))

    def test_known_failure_prime_seven(self):
        # This is an anchor/global locally obstructed control, NOT a
        # counterexample to the all-place local-to-global principle.
        bad=inert_prime_obstructions(4)
        self.assertIn({"prime":7,"norm_exponent":1},bad)
        for m in (4,53,102):
            self.assertIn(7,[x["prime"] for x in inert_prime_obstructions(m)])
        self.assertEqual(inert_prime_obstructions(5),[])
        self.assertEqual(inert_prime_obstructions(19),[])

    def test_ray_constraints_are_not_principality(self):
        z=order_data(5)
        self.assertFalse(verify_ray_generator(5,1,1)["valid"])
        self.assertFalse(verify_ray_generator(5,0,0)["valid"])
        self.assertEqual(z["rho_coefficients"],((z["A"]+1)//2,)*2)
        self.assertEqual(verify_ray_generator(5,1,1)["expected_norm"],z["N"])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):order_data(-1)
        with self.assertRaises(ValueError):prime_valuations(0)
        with self.assertRaises(ValueError):squarefree_order_generator(5,0,1)
        with self.assertRaises(ValueError):squarefree_order_generator(5,1,0)
        self.assertEqual(prime_valuations(-49*11),{7:2,11:1})

if __name__=="__main__":unittest.main()
