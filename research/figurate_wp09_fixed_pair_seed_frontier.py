"""FIGURATE WP09-013: exact fixed-pair Pell amplification for arbitrary first entry.

A genuine positive Type B seed (a,b,d), with a*b nonsquare, produces
infinitely many genuine positive exact triples with the same (a,b).
This is stronger than WP09-008, which required first entry equal to 1.

Seed search is bounded, reproducible and NOT a nonexistence algorithm.
"""
from __future__ import annotations
import argparse
import json
from math import isqrt

from research.figurate_wp09_general_pell_amplification import (
    fundamental_pell_unit, residue_preserving_order, unit_multiply,
)
from research.figurate_wp09_everywhere_local_sieve import classify


def polygonal(k: int, t: int) -> int:
    if k < 3 or t < 1:
        raise ValueError("k>=3, positive index required")
    return ((k-2)*t*t-(k-4)*t)//2


def exact(k: int, c: int, entries: tuple[int,int,int],
          indices: tuple[int,int,int]) -> bool:
    a,b,d=entries
    r,s,t=indices
    return (min(entries)>0 and len(set(entries))==3 and min(indices)>0
            and (a*b+c,a*d+c,b*d+c)
            == (polygonal(k,r),polygonal(k,s),polygonal(k,t)))


def seed_record(k:int,c:int,a:int,b:int,d:int,r:int,s:int,t:int) -> dict:
    if not exact(k,c,(a,b,d),(r,s,t)):
        raise ValueError("exact positive distinct integer seed required")
    q=a*b
    if q<=1 or isqrt(q)**2==q:
        raise ValueError("product a*b must be nonsquare >1")
    R=2*(k-2)
    L=k-4
    D=8*(k-2)*c+L*L
    S=R*s-L
    T=R*t-L
    X=a*T
    N=a*(a-b)*D
    if X*X-q*S*S!=N:
        raise ArithmeticError("derived exact Pell norm fails")
    return {"order":k,"offset":c,"entries":(a,b,d),"indices":(r,s,t),
            "q":q,"R":R,"L":L,"D":D,"X":X,"S":S,"norm":N}


def amplify_fixed_pair(k:int,c:int,a:int,b:int,d:int,r:int,s:int,t:int,
                       step:int=1) -> dict:
    """step>=0; all returned triples verified, with possible finite collisions rejected."""
    if step<0:
        raise ValueError("step must be nonnegative")
    z=seed_record(k,c,a,b,d,r,s,t)
    q,R,L=z["q"],z["R"],z["L"]
    M=2*a*R
    unit=fundamental_pell_unit(q)
    order=residue_preserving_order(q,*unit,M)
    base=(1,0)
    for _ in range(order):
        base=unit_multiply(base,unit,q)
    E,F=1,0
    n=step
    while n:
        if n&1:
            E,F=unit_multiply((E,F),base,q)
        base=unit_multiply(base,base,q)
        n>>=1
    X=E*z["X"]+q*F*z["S"]
    S=F*z["X"]+E*z["S"]
    if X*X-q*S*S!=z["norm"] or (X-z["X"])%M or (S-z["S"])%M:
        raise ArithmeticError("norm or integer lattice failed")
    if X%a:
        raise ArithmeticError("nonintegral index variable")
    T=X//a
    if (S+L)%R or (T+L)%R:
        raise ArithmeticError("polygonal index lattice failed")
    sn=(S+L)//R
    tn=(T+L)//R
    numerator=polygonal(k,sn)-c
    if numerator%a:
        raise ArithmeticError("third entry not integral")
    new_d=numerator//a
    result=(a,b,new_d)
    new_indices=(r,sn,tn)
    if not exact(k,c,result,new_indices):
        raise ValueError("this step is degenerate or fails exact identities")
    return {"order":k,"offset":c,"entries":result,"indices":new_indices,
            "step":step,"norm":z["norm"],"q":q,
            "unit":unit,"residue_order":order,"modulus":M}


def find_anchored_seed(k:int,c:int,max_r:int,max_s:int,
                       first_entries:tuple[int,...]=(1,)) -> dict:
    """Finite exhaustive scan of a,r,s within specified bounds; no global negatives."""
    if k<3 or max_r<1 or max_s<1 or not first_entries or min(first_entries)<1:
        raise ValueError("positive search bounds and first entries required")
    checked=0
    for a in first_entries:
        if a<1: raise ValueError("positive a required")
        r_options=[]
        for r in range(1,max_r+1):
            number=polygonal(k,r)-c
            if number%a==0:
                b=number//a
                if b>0 and b!=a:
                    r_options.append((r,b))
        s_options=[]
        for s in range(1,max_s+1):
            number=polygonal(k,s)-c
            if number%a==0:
                d=number//a
                if d>0 and d!=a:
                    s_options.append((s,d))
        R,L=2*(k-2),k-4
        for r,b in r_options:
            for s,d in s_options:
                if d==b: continue
                checked+=1
                x=b*d+c
                discr=8*(k-2)*x+L*L
                if discr<0:continue
                root=isqrt(discr)
                if root*root != discr or (root+L)%R:continue
                t=(root+L)//R
                if t<1:continue
                if exact(k,c,(a,b,d),(r,s,t)):
                    return {"found":True,"order":k,"offset":c,
                            "entries":(a,b,d),"indices":(r,s,t),
                            "bounds":{"max_r":max_r,"max_s":max_s,
                                      "first_entries":first_entries},
                            "tested_pairs":checked}
    return {"found":False,"order":k,"offset":c,
            "bounds":{"max_r":max_r,"max_s":max_s,
                      "first_entries":first_entries},
            "tested_pairs":checked,
            "mathematical_nonexistence_proved":False}


SEEDS={
    "52-2":(52,2,2,25,703,2,8,27),
    "116-2":(116,2,1,2399,5602386,7,314,15356),
    "36-6":(36,6,1,30,715,2,7,36),
}


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--seed",choices=sorted(SEEDS),default="52-2")
    p.add_argument("--step",type=int,default=0)
    p.add_argument("--scan",action="store_true")
    p.add_argument("--order",type=int,default=52)
    p.add_argument("--offset",type=int,default=2)
    p.add_argument("--max-r",type=int,default=69)
    p.add_argument("--max-s",type=int,default=1099)
    p.add_argument("--max-a",type=int,default=10)
    args=p.parse_args()
    if args.scan:
        result=find_anchored_seed(args.order,args.offset,args.max_r,args.max_s,
                                  tuple(range(1,args.max_a+1)))
        if args.order>=4 and args.order%4==0 and args.offset%4==2:
            result["local_sieve"]=classify(args.order,args.offset)
    else:
        result=amplify_fixed_pair(*SEEDS[args.seed],step=args.step)
    print(json.dumps(result,sort_keys=True))


if __name__=="__main__":
    main()
