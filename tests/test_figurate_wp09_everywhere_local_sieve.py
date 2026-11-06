"""Independent arithmetic checks for WP09-012 protected-result integration."""
import unittest
from math import isqrt
from research.figurate_wp09_everywhere_local_sieve import classify,odd_factor_valuations

def P(k,t):return ((k-2)*t*t-(k-4)*t)//2

def brute_three(k,c,q):
    residues={(P(k,t)-c)%q for t in range(2*q)}
    masks=[]
    for a in range(q):
        mask=0
        for b in range(q):
            if (a*b)%q in residues:mask|=1<<b
        masks.append(mask)
    for a in range(q):
        mask=masks[a]
        while mask:
            bit=mask&-mask
            b=bit.bit_length()-1
            if masks[a]&masks[b]:return True
            mask-=bit
    return False

def independent_factor(n):
    n=abs(n)
    if n==0:return []
    d=3
    while n%2==0:n//=2
    result=[]
    while d*d<=n:
        v=0
        while n%d==0:n//=d;v+=1
        if v:result.append((d,v))
        d+=2
    if n>1:result.append((n,1))
    return result

class AllPlaceSieveTests(unittest.TestCase):
    def test_binary_families_against_complete_three_entry_oracle(self):
        for k in range(4,101,4):
            for c in (-14,-6,2,10,18):
                got=classify(k,c)
                self.assertEqual(brute_three(k,c,4),True)
                if k%8==0:
                    self.assertEqual(got["first_obstruction"]["modulus"],8)
                    self.assertTrue(brute_three(k,c,4))
                    self.assertFalse(brute_three(k,c,8))
                elif k%16==12:
                    self.assertEqual(got["first_obstruction"]["modulus"],16)
                    self.assertTrue(brute_three(k,c,8))
                    self.assertFalse(brute_three(k,c,16))
                else:
                    self.assertTrue(brute_three(k,c,16))

    def test_odd_discriminant_obstructions_and_examples(self):
        examples={(4,2):True,(20,2):True,(36,2):True,
                  (36,18):False,(68,2):False,(84,6):False,
                  (8,2):False,(12,2):False,(16,2):False,(24,2):False}
        for (k,c),expected in examples.items():
            got=classify(k,c)
            self.assertEqual(got["locally_compatible_everywhere"],expected,(k,c))
            if k==36 and c==18:
                self.assertEqual([x["prime"] for x in got["all_odd_prime_obstructions"]],[5,37])
            if k==68 and c==2:
                self.assertEqual([x["prime"] for x in got["all_odd_prime_obstructions"]],[7,23])

    def test_discriminant_factorization(self):
        for n in range(-1000,1001):
            self.assertEqual(odd_factor_valuations(n),independent_factor(n))
        self.assertEqual(odd_factor_valuations(0),[])

    def test_odd_prime_power_brute_oracle_small_cases(self):
        for k in (4,20,36,52,68):
            for c in (-6,2,6,10,14,18,22):
                result=classify(k,c)
                D=result["discriminant"]
                for p in (3,5,7,11,13):
                    if (k-2)%p==0:continue
                    # Brute-check p² triple compatibility for manageable p.
                    q=p*p
                    compatible=brute_three(k,c,q)
                    v=0
                    temp=D
                    if temp==0:continue
                    while temp%p==0:v+=1;temp//=p
                    if v==1:
                        A=((k-2)*pow(2,-1,p))%p
                        nonsquare=pow(A,(p-1)//2,p)==p-1
                        self.assertEqual(compatible,not nonsquare,(k,c,p))

    def test_invalid_domain(self):
        for k,c in ((3,2),(4,1),(8,0),(12,3),(0,2)):
            with self.assertRaises(ValueError):classify(k,c)

if __name__=="__main__":unittest.main()
