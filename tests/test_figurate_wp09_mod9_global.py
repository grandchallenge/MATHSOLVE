"""Independent exact tests of WP09 modulo-9 all-triples theorem."""
import itertools
import unittest

from research.figurate_census import polygonal, polygonal_index, verify_tuple
from research.figurate_wp09_mod9_global import (
    residue_image, first_local_triple, classification, certificate)


def independent_image(k,m):
    return {(((k-2)*t*t-(k-4)*t)//2)%m
            for t in range(1,4*m+1)}


def independent_first(k,c,m):
    R=independent_image(k,m)
    for a in range(m):
        for b in range(a,m):
            for d in range(b,m):
                if ((a*b+c)%m in R and
                    (a*d+c)%m in R and
                    (b*d+c)%m in R):
                    return a,b,d
    return None


class WP09GlobalMod9(unittest.TestCase):
    def test_complete_order_offset_classification(self):
        expected={i:() for i in range(9)}
        for r in (0,3,6):
            expected[r]=(4,7)
        self.assertEqual(classification(9),expected)
        for k in range(3,154):
            for c in range(-19,20):
                self.assertEqual(first_local_triple(k,c,9),
                                 independent_first(k,c,9),(k,c))
                self.assertEqual(first_local_triple(k,c,9) is None,
                                 (k%3==0 and c%9 in (4,7)),(k,c))

    def test_exact_complete_polygonal_images(self):
        for k in range(3,120):
            self.assertEqual(set(residue_image(k,9)),independent_image(k,9))
            if k%3==0:
                self.assertEqual(set(residue_image(k,9)),{0,1,3,6})
            self.assertEqual(residue_image(k,9),residue_image(k+9,9))

    def test_mod3_sees_no_contradiction(self):
        self.assertEqual(classification(3),{0:(),1:(),2:()})
        for k in range(3,120,3):
            for c in (4,7,-2,-5,13,16):
                self.assertIsNotNone(first_local_triple(k,c,3))
                self.assertIsNone(first_local_triple(k,c,9))

    def test_direct_parity_analogue_mod3_9(self):
        for c in (4,7):
            R={0,1,3,6}
            allowed={(r-c)%9 for r in R}
            self.assertEqual(allowed,{2,5,8,6 if c==4 else 3})
            self.assertEqual({x%3 for x in allowed},{0,2})
            self.assertEqual({x for x in allowed if x%3==0},
                             {6 if c==4 else 3})
            for a,b,d in itertools.combinations_with_replacement(
                    range(9),3):
                self.assertFalse(all((x*y)%9 in allowed
                                     for x,y in ((a,b),(a,d),(b,d))))

    def test_actual_compatible_pairs_still_exist(self):
        for k,c in ((3,4),(6,7),(9,-2),(12,-5),(24,13),(51,16)):
            for t in (4,8,13):
                b=polygonal(k,t)-c
                if b>1:
                    self.assertEqual(verify_tuple((1,b),"B",k,c),
                                     {f"1,{b}":t})
            for a,b,d in itertools.combinations(range(1,32),3):
                self.assertIsNone(verify_tuple((a,b,d),"B",k,c))

    def test_not_type_a_or_c_or_other_offsets_claim(self):
        for k,c in ((3,1),(6,1),(9,0),(12,2),(4,4)):
            self.assertIsNotNone(first_local_triple(k,c,9))
        for k,c in ((3,4),(6,7),(15,13),(24,-2)):
            cert=certificate(k,c,9)
            self.assertTrue(cert["global_obstruction_by_modulus"])
            self.assertTrue(cert["global_nonexistence_by_mod9_theorem"])
            self.assertIsNone(cert["first_local_triple"])


if __name__=="__main__":
    unittest.main()
