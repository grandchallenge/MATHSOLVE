"""Independent direct polynomial, exhaustive residue and p-adic lift checks."""
import unittest
from research.figurate_wp09_odd_prime_power_complete import (
    obstructed, common_residue_witness, polygonal, audit, valuation_mod,
)


def direct(k, t):
    return ((k - 2)*t*t-(k - 4)*t)//2


def independent_all_triple(k, c, q):
    output = {direct(k, t) % q for t in range(1, q+1)}
    allowed = {(v-c) % q for v in output}
    for a in range(q):
        for b in range(q):
            if a*b % q not in allowed:
                continue
            for d in range(q):
                if a*d % q in allowed and b*d % q in allowed:
                    return (a,b,d)
    return None


class OddPrimePowerCompleteTests(unittest.TestCase):
    def test_full_prime_square_and_prime_census(self):
        expected = {(3,1):0, (3,2):6, (5,2):40, (7,2):126}
        for (p,n),excluded in expected.items():
            self.assertEqual(audit(p,n)["excluded"], excluded)

    def test_complete_mod27_and_mod81(self):
        self.assertEqual(audit(3,3)["excluded"], 54)
        self.assertEqual(audit(3,4)["excluded"], 540)

    def test_independent_all_entry_residue_oracle(self):
        for p,n in ((3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(7,2)):
            q=p**n
            for k in range(3, min(3+q, 17)):
                for c in range(min(q,17)):
                    got=independent_all_triple(k,c,q)
                    self.assertEqual(got is None,obstructed(k,c,p,n),
                                     (p,n,k,c))

    def test_common_residue_certificate(self):
        for p,n in ((3,4),(5,3),(7,2),(11,2),(13,2)):
            q=p**n
            for k in range(3, min(32,q+3)):
                for c in (-10**9,-33,-1,0,1,8,26,10**9):
                    result=common_residue_witness(k,c,p,n)
                    self.assertEqual(result is None,obstructed(k,c,p,n))
                    if result:
                        x=result["entry_residue"]
                        t=result["index_residue"]
                        self.assertEqual((x*x+c-direct(k,t))%q,0)
                        a,b,d=result["distinct_positive_entries"]
                        self.assertEqual(len({a,b,d}),3)
                        self.assertTrue(min(a,b,d)>0)
                        self.assertTrue(all((u*v+c-direct(k,t))%q==0
                                            for u,v in ((a,b),(a,d),(b,d))))

    def test_new_higher_power_exclusion(self):
        # p=3,k=3: A=1/2 is nonsquare. v_p(8c+1)=3 gives
        # mod 27 compatibility, but mod 81 impossibility.
        c= (27-1)*pow(8,-1,81)%81
        self.assertEqual(valuation_mod(8*c+1,3,4),3)
        self.assertFalse(obstructed(3,c,3,3))
        self.assertTrue(obstructed(3,c,3,4))
        self.assertIsNone(common_residue_witness(3,c,3,4))

    def test_linear_orders_are_surjective(self):
        for p in (3,5,7,11):
            for n in (1,2,3):
                k=p+2
                for c in (-10**8,-1,0,1,9876543):
                    self.assertFalse(obstructed(k,c,p,n))
                    self.assertIsNotNone(common_residue_witness(k,c,p,n))

    def test_periodicity_and_invalid_inputs(self):
        for p in (3,5,7):
            for n in (1,2,3):
                q=p**n
                for k,c in ((3,4),(5,-11),(21,1000)):
                    self.assertEqual(obstructed(k,c,p,n),
                                     obstructed(k+q,c,p,n))
                    self.assertEqual(obstructed(k,c,p,n),
                                     obstructed(k,c+q,p,n))
        for p,n in ((2,2),(9,2),(3,0)):
            with self.assertRaises(ValueError):
                obstructed(3,0,p,n)
        with self.assertRaises(ValueError):
            obstructed(2,0,3,2)


if __name__ == "__main__":
    unittest.main()
