"""Independent FIGURATE WP09-016 exact arithmetic and bounded oracle."""
import unittest
from math import isqrt
from research.figurate_wp09_frontier_census_016 import (
    TARGETS,complete_census,positive_divisors,primes_up_to,polygonal
)
from research.figurate_wp09_everywhere_local_sieve import classify


def independent_polygonal(k,n):
    return n+(k-2)*n*(n-1)//2

def brute_triples(k,c,bound):
    allowed=set()
    n=1
    while independent_polygonal(k,n)<=bound*bound+c:
        allowed.add(independent_polygonal(k,n))
        n+=1
    answer=[]
    for a in range(1,bound+1):
        for b in range(a+1,bound+1):
            if a*b+c not in allowed:continue
            for d in range(b+1,bound+1):
                if a*d+c in allowed and b*d+c in allowed:
                    answer.append((a,b,d))
    return answer


class FrontierTests(unittest.TestCase):
    def test_local_compatibility(self):
        for k,c in TARGETS:
            self.assertTrue(classify(k,c)["locally_compatible_everywhere"])
        self.assertEqual(classify(84,2)["discriminant"],7712)
        self.assertEqual(classify(100,2)["discriminant"],10784)
        self.assertEqual(7712,32*241)
        self.assertEqual(10784,32*337)

    def test_exact_residue_lemma(self):
        # For every k divisible by 4 and c=2 modulo 4,
        # any three pair products must have residues 2 or 3 modulo 4.
        # The only unordered distinct residue multiset is {1,2,3}.
        compatible=[]
        for a in range(4):
            for b in range(a,4):
                for d in range(b,4):
                    if all((u*v)%4 in (2,3)
                           for u,v in ((a,b),(a,d),(b,d))):
                        compatible.append((a,b,d))
        self.assertEqual(compatible,[(1,2,3)])
        for k,c in TARGETS:
            self.assertEqual({independent_polygonal(k,n)%4
                              for n in range(1,9)},{0,1})

    def test_divisor_oracle(self):
        primes=primes_up_to(1000)
        for n in range(1,1001):
            expected=[d for d in range(1,n+1) if n%d==0]
            self.assertEqual(sorted(positive_divisors(n,primes)),expected)

    def test_complete_small_oracle(self):
        for k,c in TARGETS:
            for B in (12,24,48,96):
                z=complete_census(k,c,B)
                self.assertEqual([w[:3] for w in z["exact_triples"]],
                                 brute_triples(k,c,B))
                self.assertFalse(z["global_nonexistence_proved"])

    def test_full_300000_census(self):
        for k,c in TARGETS:
            z=complete_census(k,c,300000)
            self.assertEqual(z["triangle_count"],0)
            self.assertEqual(z["exact_triples"],[])
            self.assertFalse(z["global_nonexistence_proved"])
            self.assertGreater(z["edge_count"],1000)

    def test_domain(self):
        for k,c,B in ((84,2,2),(100,2,300001),(68,2,20),
                      (84,6,20),(80,2,10)):
            with self.assertRaises(ValueError):
                complete_census(k,c,B)
        with self.assertRaises(ValueError):positive_divisors(0,[])
        with self.assertRaises(ValueError):polygonal(84,0)


if __name__=="__main__":unittest.main()
