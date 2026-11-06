"""Independent polygonal and mod-four tests for FIGURATE WP09-011."""
import unittest
from research.figurate_wp09_nondiagonal_anchor_gap import (
    anchor_gap_mod_four,square_order_exact,exact_gap_seed,SEEDS
)

def P(k,t):
    return t+((k-2)*t*(t-1))//2

def exact(k,c,z):
    a,b,d=z["entries"]
    r,s,t=z["indices"]
    return (min(a,b,d,r,s,t)>0 and len({a,b,d})==3
            and (a*b+c,a*d+c,b*d+c)==(P(k,r),P(k,s),P(k,t)))

class NonDiagonalAnchorGapTests(unittest.TestCase):
    def test_uniform_mod_four_gap_and_nondiagonal_witness(self):
        for k in range(4,161,4):
            for c in (-22,-14,-6,2,10,18,26):
                z=anchor_gap_mod_four(k,c)
                self.assertFalse(z["diagonal_exists"])
                a,b,d=z["entry_residues"]
                r,s,t=z["index_residues"]
                self.assertEqual(tuple((v-c2)%4 for v,c2 in
                    zip((a*b+c,a*d+c,b*d+c),(P(k,r),P(k,s),P(k,t)))),
                    (0,0,0))
                anchor={(P(k,u)-v*v)%4 for u in range(1,9)
                        for v in range(4)}
                self.assertNotIn(c%4,anchor)

    def test_arbitrary_offset_square_global_constructions(self):
        for c in (-102,-22,-6,2,6,14,34,102):
            for step in range(5):
                w=square_order_exact(c,step)
                self.assertTrue(exact(4,c,w))
                self.assertEqual(c%4,2)

    def test_twenty_and_thirtysix_exact_and_pell_lifts(self):
        for k in (20,36):
            last=0
            for step in range(3):
                w=exact_gap_seed(k,step)
                self.assertTrue(exact(k,2,w))
                self.assertGreater(w["entries"][2],last)
                last=w["entries"][2]
                self.assertNotEqual(w["entries"][1]**0,0)
                b=w["entries"][1]
                R=2*(k-2)
                L=k-4
                S=R*w["indices"][1]-L
                T=R*w["indices"][2]-L
                D=8*(k-2)*2+L*L
                self.assertEqual(T*T-b*S*S,-(b-1)*D)

    def test_new_36_gonal_seed_numbers(self):
        w=exact_gap_seed(36)
        self.assertEqual(w["entries"],(1,343,6478))
        self.assertEqual(w["indices"],(5,20,362))
        self.assertEqual((P(36,5),P(36,20),P(36,362)),
                         (345,6480,2221956))

    def test_shift_not_necessary_even_locally(self):
        for k in (4,8,12,20,36,44,84):
            self.assertEqual({P(k,u)%4 for u in range(1,9)},{0,1})
            # A diagonal triple would require x²+c square mod 4.
            for x in range(4):
                self.assertNotIn((x*x+2)%4,{0,1})
        with self.assertRaises(ValueError):
            anchor_gap_mod_four(7,2)
        with self.assertRaises(ValueError):
            anchor_gap_mod_four(20,3)
        with self.assertRaises(ValueError):
            exact_gap_seed(8)

if __name__=="__main__":
    unittest.main()
