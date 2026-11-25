"""FIGURATE WP09-012: complete everywhere-local Type B sieve for k=0 mod4,c=2 mod4.

Uses protected WP08 binary all-triple obstructions and WP09-006
complete odd-prime-power criterion. This decides local compatibility,
not exact integer Type B existence or certification.
"""
from __future__ import annotations
import argparse,json
from math import isqrt
from research.figurate_wp09_odd_prime_power_complete import obstructed

def odd_factor_valuations(n: int) -> list[tuple[int,int]]:
    if n==0: return []
    n=abs(n)
    while n%2==0:n//=2
    factors=[]
    p=3
    while p*p<=n:
        if n%p==0:
            v=0
            while n%p==0:n//=p;v+=1
            factors.append((p,v))
        p+=2
    if n>1:factors.append((n,1))
    return factors

def classify(k:int,c:int) -> dict:
    if k<4 or k%4 or c%4!=2:
        raise ValueError("require polygonal order k>=4 divisible by4, c=2 mod4")
    D=8*(k-2)*c+(k-4)**2
    if k%8==0:
        return {"order":k,"offset":c,"locally_compatible_everywhere":False,
                "first_obstruction":{"prime":2,"exponent":3,"modulus":8},
                "discriminant":D,"basis":"protected-WP08-mod8"}
    if k%16==12:
        return {"order":k,"offset":c,"locally_compatible_everywhere":False,
                "first_obstruction":{"prime":2,"exponent":4,"modulus":16},
                "discriminant":D,"basis":"protected-WP08-mod16"}
    if k%16!=4:
        raise AssertionError("uncovered k divisible by 4")
    bad=[]
    for p,v in odd_factor_valuations(D):
        if v%2 and (k-2)%p:
            # At odd p, the complete criterion is nonresidue A and odd v.
            if obstructed(k,c,p,v+1):
                bad.append({"prime":p,"exponent":v+1,"modulus":p**(v+1),
                            "discriminant_valuation":v})
    if bad:
        bad.sort(key=lambda d:d["modulus"])
        return {"order":k,"offset":c,"locally_compatible_everywhere":False,
                "first_obstruction":bad[0],
                "all_odd_prime_obstructions":bad,"discriminant":D,
                "basis":"protected-WP09-006"}
    return {"order":k,"offset":c,"locally_compatible_everywhere":True,
            "first_obstruction":None,"discriminant":D,
            "basis":"WP08-binary-plus-WP09-006-odd-prime-powers",
            "global_exact_integer_existence":"not_determined"}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--order",type=int,default=36)
    p.add_argument("--offset",type=int,default=18)
    a=p.parse_args()
    print(json.dumps(classify(a.order,a.offset),sort_keys=True))
if __name__=="__main__":main()
