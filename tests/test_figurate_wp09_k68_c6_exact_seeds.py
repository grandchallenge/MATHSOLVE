"""Independent finite exact arithmetic checks of WP09-015."""
import unittest
from math import isqrt
from research.figurate_wp09_k68_c6_exact_seeds import (
 WITNESSES,exact_witness,complete_entry_bounded_census
)
from research.figurate_wp09_everywhere_local_sieve import classify
from research.figurate_wp09_fixed_pair_seed_frontier import seed_record

def alternate_polygonal(t):
    return t+66*t*(t-1)//2

def brute_small(bound):
    outputs=set()
    n=1
    while alternate_polygonal(n)<=bound**2+6:
        outputs.add(alternate_polygonal(n));n+=1
    result=[]
    for a in range(1,bound+1):
        for b in range(a+1,bound+1):
            if a*b+6 not in outputs:continue
            for d in range(b+1,bound+1):
                if a*d+6 in outputs and b*d+6 in outputs:
                    result.append((a,b,d))
    return result

class Exact68Tests(unittest.TestCase):
    def test_five_independently_verified_witnesses(self):
        self.assertEqual(len(WITNESSES),5)
        for a,b,d,r,s,t in WITNESSES:
            self.assertTrue(exact_witness((a,b,d,r,s,t)))
            self.assertEqual((a*b+6,a*d+6,b*d+6),
                             (alternate_polygonal(r),
                              alternate_polygonal(s),alternate_polygonal(t)))
            self.assertNotEqual(isqrt(a*b)**2,a*b)
            self.assertEqual(seed_record(68,6,a,b,d,r,s,t)["q"],a*b)

    def test_all_place_local_criterion(self):
        z=classify(68,6)
        self.assertTrue(z["locally_compatible_everywhere"])
        self.assertEqual(z["discriminant"],7264)
        self.assertEqual(7264,2**5*227)
        self.assertEqual(pow(33,(227-1)//2,227),1)

    def test_finite_census(self):
        result=complete_entry_bounded_census(100000)
        self.assertEqual(result["witnesses"],[])
        self.assertFalse(result["global_nonexistence_proved"])

    def test_small_oracle(self):
        for bound in (12,24,48,96):
            result=complete_entry_bounded_census(bound)
            self.assertEqual([w[:3] for w in result["witnesses"]],
                             brute_small(bound))

    def test_bounds(self):
        for bound in (2,100001):
            with self.assertRaises(ValueError):
                complete_entry_bounded_census(bound)

if __name__=="__main__":unittest.main()
