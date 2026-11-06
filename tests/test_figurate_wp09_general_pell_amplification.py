"""Independent integer-oracle tests of the general WP09-008 Pell theorem."""
import unittest
from math import isqrt
from research.figurate_wp09_general_pell_amplification import (
    SEEDS, amplify_seed, fundamental_pell_unit,
    positive_pell_seed, residue_preserving_order,
)

def direct_polygonal(k,t):
    return ((k-2)*t*t-(k-4)*t)//2

def positive_exact(k,c,entries,indices):
    a,b,d=entries
    r,s,t=indices
    return (min(entries)>0 and len(set(entries))==3 and min(indices)>0
            and a*b+c==direct_polygonal(k,r)
            and a*d+c==direct_polygonal(k,s)
            and b*d+c==direct_polygonal(k,t))

def discover_seeds():
    for k in range(3,11):
        for c in (-5,-2,0,1,2,3,5):
            for r in range(2,9):
                b=direct_polygonal(k,r)-c
                if b<=1 or isqrt(b)**2==b:
                    continue
                for s in range(2,70):
                    d=direct_polygonal(k,s)-c
                    if d<=1 or d==b:
                        continue
                    value=b*d+c
                    if value<1:
                        continue
                    discr=8*(k-2)*value+(k-4)**2
                    root=isqrt(discr)
                    if root*root!=discr:
                        continue
                    numer=root+k-4
                    denom=2*(k-2)
                    if numer%denom:
                        continue
                    t=numer//denom
                    if t>=1:
                        yield k,c,r,s,t

class GeneralPellTests(unittest.TestCase):
    def test_known_exact_seeds_and_recurrences(self):
        for name,seed in SEEDS.items():
            previous=0
            for step in range(4):
                cert=amplify_seed(*seed,step)
                self.assertTrue(positive_exact(seed[0],seed[1],cert["entries"],cert["indices"]),name)
                self.assertGreater(cert["entries"][2],previous)
                previous=cert["entries"][2]
                b=cert["entries"][1]
                self.assertEqual(cert["pell"]["T"]**2-b*cert["pell"]["S"]**2,
                                 cert["pell"]["norm"])

    def test_exact_original_examples(self):
        self.assertEqual(amplify_seed(*SEEDS["pentagonal"],0)["entries"],(1,3,3430))
        self.assertEqual(amplify_seed(*SEEDS["hexagonal"],0)["entries"],(1,13,43))
        self.assertEqual(amplify_seed(*SEEDS["icosagonal"],0)["entries"],(1,18,13375))

    def test_independent_discovered_seed_amplification(self):
        cases=list(discover_seeds())
        self.assertGreaterEqual(len(cases),20)
        for seed in cases[:30]:
            before=positive_pell_seed(*seed)
            for j in (0,1,2):
                new=amplify_seed(*seed,j)
                self.assertTrue(positive_exact(seed[0],seed[1],new["entries"],new["indices"]))
                self.assertEqual(new["pell"]["norm"],before["norm"])

    def test_fundamental_pell_units_and_modular_order(self):
        for b,unit,modulus,order in (
            (3,(2,1),6,6),(13,(649,180),8,2),(18,(17,4),36,18)):
            self.assertEqual(fundamental_pell_unit(b),unit)
            self.assertEqual(residue_preserving_order(b,*unit,modulus),order)
        for b in (2,3,5,6,7,10,11,13,18,21,29,61):
            u,v=fundamental_pell_unit(b)
            self.assertEqual(u*u-b*v*v,1)

    def test_signed_offsets_and_periodic_seed_indices(self):
        seen_negative=0
        for seed in discover_seeds():
            if seed[1]<0:
                w=amplify_seed(*seed,1)
                self.assertTrue(positive_exact(seed[0],seed[1],w["entries"],w["indices"]))
                seen_negative+=1
            if seen_negative==10:
                break
        self.assertEqual(seen_negative,10)

    def test_invalid_seeds(self):
        with self.assertRaises(ValueError):
            amplify_seed(20,2,2,39,164,-1)
        with self.assertRaises(ValueError):
            amplify_seed(20,2,2,39,165,1)
        with self.assertRaises(ValueError):
            fundamental_pell_unit(9)
        with self.assertRaises(ValueError):
            amplify_seed(4,0,2,3,6,1) # square second entry

if __name__=="__main__":
    unittest.main()
