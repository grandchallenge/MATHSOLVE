"""Independent exact arithmetic tests for FIGURATE WP09-009 seed existence."""
import unittest
from math import isqrt
from research.figurate_wp09_seed_existence import (
    constructive_offset_family, degenerate_pell_seed,
    promote_degenerate_seed, choose_nonsquare_second_entry,
)

def P(k,n):
    return (n*((k-2)*n-(k-4)))//2

def check_independent(k,c,z):
    a,b,d=z["entries"]
    r,s,t=z["indices"]
    return (a==1 and 1<b and d>1 and d!=b
            and min(r,s,t)>0
            and a*b+c==P(k,r)
            and a*d+c==P(k,s)
            and b*d+c==P(k,t))

class SeedExistenceTests(unittest.TestCase):
    def test_wide_orders_offsets_and_exact_identities(self):
        for k in range(3,29):
            for u in range(1,7):
                with self.subTest(k=k,u=u):
                    w=constructive_offset_family(k,u)
                    self.assertEqual(w["offset"],P(k,u)-1)
                    self.assertTrue(check_independent(k,w["offset"],w))

    def test_distinct_pell_steps(self):
        for k,u in ((3,1),(4,2),(5,1),(5,2),(6,2),
                    (7,2),(8,1),(11,4),(20,2),(28,6)):
            first=None
            for step in (1,2,3):
                w=constructive_offset_family(k,u,step=step)
                self.assertTrue(check_independent(k,w["offset"],w))
                if first is not None:
                    self.assertGreater(w["entries"][2],first)
                first=w["entries"][2]

    def test_squares_exception(self):
        for step in (1,2,3,7):
            z=constructive_offset_family(4,1,step=step)
            self.assertEqual(z["method"],"square-exception")
            self.assertTrue(check_independent(4,0,z))
        with self.assertRaises(ValueError):
            choose_nonsquare_second_entry(4,1)

    def test_many_distinct_fixed_second_entries(self):
        for k,u in ((3,1),(4,2),(5,1),(6,2),(7,2),(20,1)):
            previous_r=1
            seen=set()
            for i in range(12):
                r,b=choose_nonsquare_second_entry(k,u,previous_r+1)
                self.assertGreater(r,previous_r)
                self.assertGreater(b,1)
                self.assertNotEqual(isqrt(b)**2,b)
                seed=degenerate_pell_seed(k,u,r)
                self.assertEqual(seed["T"]**2-b*seed["S"]**2,
                                 seed["norm"])
                w=promote_degenerate_seed(k,u,r,1)
                self.assertTrue(check_independent(k,w["offset"],w))
                seen.add(b)
                previous_r=r
            self.assertEqual(len(seen),12)

    def test_bad_input_guard(self):
        for k,u in ((2,1),(4,0)):
            with self.assertRaises(ValueError):
                constructive_offset_family(k,u)
        with self.assertRaises(ValueError):
            constructive_offset_family(7,2,step=0)
        with self.assertRaises(ValueError):
            promote_degenerate_seed(7,2,3,0)
        with self.assertRaises(ValueError):
            degenerate_pell_seed(4,1,2)

    def test_seed_is_not_misrepresented_as_exact_triple(self):
        q=degenerate_pell_seed(7,2,3)
        self.assertEqual(q["c"],P(7,2)-1)
        self.assertEqual(q["S"],q["R"]*2-q["L"])
        self.assertEqual(q["T"],q["R"]*3-q["L"])
        self.assertTrue(check_independent(7,q["c"],
                          promote_degenerate_seed(7,2,3,1)))

if __name__=="__main__":
    unittest.main()
