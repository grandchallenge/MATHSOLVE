"""Independent arithmetic validation for FIGURATE WP09-014."""
import unittest
from math import isqrt
from research.figurate_wp09_k52_c6_exact_seed import (
    C,SEED_ENTRIES,SEED_INDICES,graph_census,index_for,exact_tuple
)
from research.figurate_wp09_fixed_pair_seed_frontier import (
    seed_record
)
from research.figurate_wp09_everywhere_local_sieve import classify


def independent_polygonal(n):
    return n+50*n*(n-1)//2


def oracle(B):
    # Independent triple loop, with direct polygonal-output set.
    maximum=B*B+C
    outputs=set()
    n=1
    while independent_polygonal(n) <= maximum:
        outputs.add(independent_polygonal(n))
        n+=1
    results=[]
    for a in range(1,B+1):
        for b in range(a+1,B+1):
            if a*b+C not in outputs:
                continue
            for d in range(b+1,B+1):
                if a*d+C in outputs and b*d+C in outputs:
                    results.append((a,b,d))
    return results


class K52OffsetSixTests(unittest.TestCase):
    def test_exact_seed(self):
        z=exact_tuple(SEED_ENTRIES)
        self.assertIsNotNone(z)
        self.assertEqual(z["indices"],SEED_INDICES)
        self.assertEqual(z["pair_outputs"],(4564,9520,10841209))
        self.assertEqual([independent_polygonal(x) for x in SEED_INDICES],
                         [4564,9520,10841209])

    def test_all_place_local_and_not_square_shift(self):
        z=classify(52,6)
        self.assertTrue(z["locally_compatible_everywhere"])
        self.assertEqual(z["discriminant"],4704)
        self.assertEqual(4704,32*3*7*7)
        for n in range(1,9):
            self.assertEqual(independent_polygonal(n)%4,n*n%4)
        self.assertNotIn(6%4,{(independent_polygonal(n)-a*a)%4
                              for n in range(1,9) for a in range(4)})

    def test_complete_bounded_census(self):
        result=graph_census(10000)
        self.assertEqual(result["triple_count"],1)
        self.assertEqual([tuple(z["entries"]) for z in result["triples"]],
                         [SEED_ENTRIES])
        self.assertFalse(result["global_nonexistence_proved"])

    def test_independent_small_brute_oracle(self):
        for B in (8,15,30,70):
            self.assertEqual([tuple(x["entries"]) for x in graph_census(B)["triples"]],
                             oracle(B))

    def test_general_pell_hypotheses_without_expensive_unit_replay(self):
        # The protected WP09-013 theorem supplies the infinite orbit.
        # This test verifies its input norm, nonsquare product and lattice.
        a,b,d=SEED_ENTRIES
        r,s,t=SEED_INDICES
        z=seed_record(52,6,a,b,d,r,s,t)
        self.assertEqual(z["q"],4558)
        self.assertNotEqual(isqrt(4558)**2,4558)
        self.assertEqual(z["D"],4704)
        self.assertEqual(z["R"],100)
        self.assertEqual(z["L"],48)
        self.assertEqual(z["S"],1952)
        self.assertEqual(z["X"],131704)
        self.assertEqual(z["X"]**2-4558*z["S"]**2,
                         a*(a-b)*z["D"])
        self.assertEqual((z["S"]+z["L"])%z["R"],0)
        self.assertEqual((z["X"]//a+z["L"])%z["R"],0)

    def test_invalid_boundary(self):
        for B in (0,2,10001):
            with self.assertRaises(ValueError):
                graph_census(B)
        self.assertIsNone(index_for(-1))
        self.assertIsNone(exact_tuple((2,2,4757)))


if __name__=="__main__":
    unittest.main()
