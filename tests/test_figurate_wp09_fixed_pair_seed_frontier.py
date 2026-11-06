"""Independent exact-identity and exhaustive bounded-search controls for WP09-013."""
import unittest
from math import isqrt
from research.figurate_wp09_fixed_pair_seed_frontier import (
    SEEDS,amplify_fixed_pair,find_anchored_seed,seed_record,
)
from research.figurate_wp09_everywhere_local_sieve import classify


def independent_polygonal(k,t):
    return t+(k-2)*t*(t-1)//2


def independent_exact(k,c,entries,indices):
    a,b,d=entries
    r,s,t=indices
    return (min(entries)>0 and len(set(entries))==3 and min(indices)>0
            and (a*b+c,a*d+c,b*d+c)==tuple(independent_polygonal(k,i)
                                             for i in indices))


def separate_bruteforce(k,c,alist,rmax,smax):
    """Different loop order, independent direct discrim integer oracle."""
    R=2*(k-2)
    L=k-4
    for a in alist:
        for s in range(1,smax+1):
            n=independent_polygonal(k,s)-c
            if n<=0 or n%a:continue
            d=n//a
            if d==a:continue
            for r in range(1,rmax+1):
                x=independent_polygonal(k,r)-c
                if x<=0 or x%a:continue
                b=x//a
                if b==a or b==d:continue
                dis=8*(k-2)*(b*d+c)+L*L
                if dis<0:continue
                root=isqrt(dis)
                if root*root!=dis or (root+L)%R:continue
                t=(root+L)//R
                if independent_exact(k,c,(a,b,d),(r,s,t)):
                    return (a,b,d,r,s,t)
    return None


class FixedPairFrontierTests(unittest.TestCase):
    def test_new_exact_witnesses_and_local_sieve(self):
        for name,z in SEEDS.items():
            k,c,a,b,d,r,s,t=z
            self.assertTrue(independent_exact(k,c,(a,b,d),(r,s,t)))
            self.assertNotEqual(isqrt(a*b)**2,a*b)
            self.assertTrue(classify(k,c)["locally_compatible_everywhere"])
        self.assertEqual(SEEDS["52-2"],(52,2,2,25,703,2,8,27))
        self.assertEqual(SEEDS["116-2"],(116,2,1,2399,5602386,7,314,15356))
        self.assertEqual(
            2399*5602386+2,
            independent_polygonal(116,15356))

    def test_general_first_pair_pell_amplification(self):
        for z in SEEDS.values():
            k,c,a,b,d,r,s,t=z
            previous=0
            for step in range(3):
                result=amplify_fixed_pair(*z,step=step)
                self.assertTrue(independent_exact(k,c,result["entries"],
                                                  result["indices"]))
                self.assertEqual(result["entries"][:2],(a,b))
                self.assertGreater(result["entries"][2],previous)
                previous=result["entries"][2]
                S=2*(k-2)*result["indices"][1]-(k-4)
                T=2*(k-2)*result["indices"][2]-(k-4)
                self.assertEqual((a*T)**2-(a*b)*S*S,result["norm"])

    def test_nonunit_first_entry_is_essential(self):
        z=find_anchored_seed(52,2,30,90,(1,))
        self.assertFalse(z["found"])
        self.assertFalse(z["mathematical_nonexistence_proved"])
        positive=find_anchored_seed(52,2,30,90,(1,2))
        self.assertTrue(positive["found"])
        self.assertTrue(independent_exact(52,2,positive["entries"],
                                          positive["indices"]))
        self.assertEqual(positive["entries"],(2,25,703))
        self.assertEqual(positive["indices"],(2,8,27))

    def test_bounded_negative_never_construed_global(self):
        for k,c in ((68,6),(84,2),(100,2)):
            got=find_anchored_seed(k,c,15,45,(1,2,3))
            brute=separate_bruteforce(k,c,(1,2,3),15,45)
            self.assertEqual(got["found"],brute is not None)
            if not got["found"]:
                self.assertFalse(got["mathematical_nonexistence_proved"])
            self.assertTrue(classify(k,c)["locally_compatible_everywhere"])

    def test_full_small_oracle_agreement(self):
        for k,c in ((20,2),(36,6),(52,2),(68,6),(84,2),(100,2),(116,2)):
            got=find_anchored_seed(k,c,16,40,(1,2,3))
            brute=separate_bruteforce(k,c,(1,2,3),16,40)
            self.assertEqual(got["found"],brute is not None,(k,c))
            if got["found"]:
                self.assertTrue(independent_exact(k,c,got["entries"],
                                                  got["indices"]))

    def test_invalid_and_square_product_boundary(self):
        with self.assertRaises(ValueError):
            seed_record(52,2,2,25,704,2,8,27)
        with self.assertRaises(ValueError):
            seed_record(4,0,1,4,9,2,3,6)
        with self.assertRaises(ValueError):
            amplify_fixed_pair(*SEEDS["52-2"],step=-1)
        with self.assertRaises(ValueError):
            find_anchored_seed(52,2,0,15,(1,2))
        with self.assertRaises(ValueError):
            find_anchored_seed(52,2,10,15,(0,1))


if __name__=="__main__":
    unittest.main()
