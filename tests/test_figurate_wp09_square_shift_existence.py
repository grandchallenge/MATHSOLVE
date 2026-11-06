"""Independent exact-integer controls for FIGURATE WP09-010.

Tests use a separately written polygonal formula and do not rely on
the producer's exact_type_b predicate.
"""
import unittest
from math import isqrt
from research.figurate_wp09_square_shift_existence import (
    square_shift_family, formal_repeat_seed, promote_formal_seed,
    choose_nonsquare_norm, shifted_square_case,
)


def independent_P(k,t):
    return t+((k-2)*t*(t-1))//2


def independent_check(k,c,entries,indices):
    a,b,d=entries
    r,s,t=indices
    return (min(entries)>0 and len(set(entries))==3
            and min(indices)>0 and
            [a*b+c,a*d+c,b*d+c]==
            [independent_P(k,r),independent_P(k,s),independent_P(k,t)])


class SquareShiftExistenceTests(unittest.TestCase):
    def test_cross_order_exact_seed_existence(self):
        for k in range(3,22):
            for u in range(1,5):
                for a in range(1,5):
                    with self.subTest(k=k,u=u,a=a):
                        result=square_shift_family(k,u,a)
                        c=independent_P(k,u)-a*a
                        self.assertEqual(result["offset"],c)
                        self.assertTrue(independent_check(
                            k,c,result["entries"],result["indices"]))
                        self.assertEqual(result["entries"][0],a)

    def test_multiple_distinct_exact_lifts(self):
        for k,u,a in ((3,1,2),(4,1,1),(4,2,2),(5,1,2),
                      (6,2,3),(7,2,2),(8,1,3),(11,3,2),(20,2,1)):
            last=0
            for step in (1,2,3):
                r=square_shift_family(k,u,a,step)
                self.assertTrue(independent_check(
                    k,r["offset"],r["entries"],r["indices"]))
                self.assertGreater(r["entries"][2],last)
                last=r["entries"][2]

    def test_nonsquare_search_multiple_fixed_pairs(self):
        for k,u,a in ((3,1,1),(3,2,2),(4,2,1),(5,1,2),
                      (6,2,2),(7,2,2),(11,3,3)):
            last=0
            qs=set()
            for _ in range(8):
                r,b,q=choose_nonsquare_norm(k,u,a,last+1)
                self.assertEqual(r% (2*a),u%(2*a))
                self.assertEqual(a*b,q)
                self.assertNotEqual(isqrt(q)**2,q)
                z=formal_repeat_seed(k,u,a,r)
                self.assertEqual(z["X"]**2-q*z["S"]**2,z["norm"])
                lift=promote_formal_seed(k,u,a,r)
                self.assertTrue(independent_check(
                    k,lift["offset"],lift["entries"],lift["indices"]))
                qs.add(q)
                last=(r-u)//(2*a)
            self.assertEqual(len(qs),8)

    def test_repeated_seed_not_false_type_b(self):
        k,u,a=7,2,2
        r,b,q=choose_nonsquare_norm(k,u,a)
        z=formal_repeat_seed(k,u,a,r)
        self.assertEqual(z["offset"],independent_P(k,u)-a*a)
        self.assertEqual(z["X"]**2-q*z["S"]**2,z["norm"])
        self.assertFalse(len({a,b,a})==3)

    def test_square_exception_and_invalid_inputs(self):
        for u in (1,2,3,7):
            self.assertTrue(shifted_square_case(4,u,u))
            for step in (1,2,5):
                z=square_shift_family(4,u,u,step)
                self.assertEqual(z["offset"],0)
                self.assertTrue(independent_check(4,0,z["entries"],z["indices"]))
        for k,u,a in ((2,1,1),(3,0,1),(4,1,0)):
            with self.assertRaises(ValueError):
                square_shift_family(k,u,a)
        with self.assertRaises(ValueError):
            square_shift_family(7,2,2,0)
        with self.assertRaises(ValueError):
            choose_nonsquare_norm(4,2,2)
        with self.assertRaises(ValueError):
            promote_formal_seed(7,2,2,6,0)

    def test_known_non_wp09_009_example(self):
        z=square_shift_family(7,2,2)
        self.assertEqual(z["offset"],3)
        self.assertEqual(z["entries"][0:2],(2,39))
        self.assertTrue(independent_check(7,3,z["entries"],z["indices"]))
        # offset 3 is not P_7(v)-1 for any positive v
        self.assertNotIn(4,{independent_P(7,v) for v in range(1,100)})


if __name__=="__main__":
    unittest.main()
