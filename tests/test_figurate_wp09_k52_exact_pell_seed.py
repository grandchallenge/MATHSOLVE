"""Independent exact arithmetic and bounded enumeration for FIGURATE WP09-013."""
import unittest
from math import isqrt
from research.figurate_wp09_k52_exact_pell_seed import (
    exact_member, unit_modulus_check, bounded_triangles
)


def P(n):
    return (50*n*n-48*n)//2


def independently_check(z):
    a,b,d=z["entries"]
    r,s,t=z["indices"]
    return (a>0 and b>0 and d>0 and len({a,b,d})==3
            and min(r,s,t)>0
            and a*b+2==P(r) and a*d+2==P(s) and b*d+2==P(t))


class K52ExactPellTests(unittest.TestCase):
    def test_exact_seed(self):
        z=exact_member()
        self.assertEqual(z["entries"],(2,25,703))
        self.assertEqual(z["indices"],(2,8,27))
        self.assertEqual((P(2),P(8),P(27)),(52,1408,17577))
        self.assertTrue(independently_check(z))

    def test_complete_bounded_search(self):
        # Factor every possible 52-gonal pair product, then find graph triangles.
        self.assertEqual(bounded_triangles(2000),[(2,25,703)])

    def test_pell_preservation_and_two_distinct_orbit_members(self):
        self.assertTrue(unit_modulus_check())
        first=exact_member()
        second=exact_member(1)
        third=exact_member(2)
        last=0
        for z in (first,second,third):
            self.assertTrue(independently_check(z))
            a,b,d=z["entries"]
            r,s,t=z["indices"]
            self.assertEqual((2*(100*t-48))**2-50*(100*s-48)**2,
                             2*(2-25)*3104)
            self.assertGreater(d,last)
            last=d

    def test_local_odd_prime_and_anchor_gap(self):
        # Delta=3104=32*97, and (k-2)/2=25 is square mod 97.
        self.assertEqual(3104,32*97)
        self.assertEqual(25%97,pow(5,2,97))
        self.assertEqual(52%16,4)
        self.assertEqual({P(n)%4 for n in range(1,9)},{0,1})
        self.assertNotIn(2,{(P(n)-a*a)%4 for n in range(1,9)
                             for a in range(4)})

    def test_negative_input(self):
        with self.assertRaises(ValueError):exact_member(-1)
        with self.assertRaises(ValueError):bounded_triangles(2001)


if __name__=="__main__":
    unittest.main()
