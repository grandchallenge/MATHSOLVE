"""FIGURATE WP09-011: diagonal anchor gaps versus exact Type B solutions.

For every k divisible by 4 and c=2 mod 4, there is no local diagonal
entry residue modulo 4, but the distinct residue triple (1,2,3) works.
Actual integer examples include k=4 (all c), k=20,c=2, k=36,c=2.
"""
from __future__ import annotations
import argparse
import json
from math import isqrt
from research.figurate_wp09_general_pell_amplification import amplify_seed

def polygonal(k: int, n: int) -> int:
    if k<3 or n<1:
        raise ValueError("order and positive polygonal index required")
    return ((k-2)*n*n-(k-4)*n)//2

def exact_type_b(k: int,c: int,entries: tuple[int,int,int],
                 indices: tuple[int,int,int]) -> bool:
    a,b,d=entries
    r,s,t=indices
    return (min(entries)>0 and len(set(entries))==3 and min(indices)>0
            and a*b+c==polygonal(k,r)
            and a*d+c==polygonal(k,s)
            and b*d+c==polygonal(k,t))

def anchor_gap_mod_four(k: int,c: int) -> dict:
    if k<4 or k%4:
        raise ValueError("k must be divisible by four")
    if c%4!=2:
        raise ValueError("c must equal 2 modulo four")
    # P_k(n) = n²+(k-4)n(n-1)/2, and 4 divides (k-4).
    for n in range(1,5):
        assert (polygonal(k,n)-n*n)%4==0
    image={polygonal(k,n)%4 for n in range(1,9)}
    squares={n*n%4 for n in range(4)}
    diagonal={(p-q)%4 for p in image for q in squares}
    if 2 in diagonal or image!={0,1}:
        raise AssertionError("diagonal mod-four obstruction failed")
    # Every pair simultaneously has a genuine k-gonal output residue:
    # ab+c=0, ad+c=1, bd+c=0 (mod 4).
    entries=(1,2,3)
    indices=(4,1,4)
    for (x,y),t in zip(((1,2),(1,3),(2,3)),indices):
        if (x*y+c-polygonal(k,t))%4:
            raise AssertionError("non-diagonal residue witness failed")
    return {"order":k,"offset":c,"modulus":4,"diagonal_exists":False,
            "entry_residues":entries,"index_residues":indices}

def square_order_exact(c: int,seed: int=0) -> dict:
    if c%4!=2:
        raise ValueError("square-order gap requires c=2 mod four")
    t=max(2,abs(c)+3)+seed
    if seed<0:
        raise ValueError("seed>=0 required")
    entries=(1,t*t-c,(t+1)*(t+1)-c)
    indices=(t,t+1,t*(t+1)-c)
    if not exact_type_b(4,c,entries,indices):
        raise AssertionError("exact Euler regular tuple fails")
    return {"order":4,"offset":c,"entries":entries,"indices":indices,
            "method":"Euler-regular"}

SEEDS={
    20: (20,2,2,39,164),
    36: (36,2,5,20,362),
}

def exact_gap_seed(k: int,step: int=0) -> dict:
    if k not in SEEDS or step<0:
        raise ValueError("supported k is 20 or 36, step>=0")
    z=amplify_seed(*SEEDS[k],steps=step)
    if z["offset"]!=2 or not exact_type_b(k,2,z["entries"],z["indices"]):
        raise AssertionError("invalid exact gap family")
    if not anchor_gap_mod_four(k,2):
        raise AssertionError("anchor gap certificate unavailable")
    return {"order":k,"offset":2,"entries":z["entries"],
            "indices":z["indices"],"step":step,"pell":z["pell"]}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--order",type=int,default=36)
    ap.add_argument("--offset",type=int,default=2)
    ap.add_argument("--step",type=int,default=0)
    args=ap.parse_args()
    if args.order==4:
        result=square_order_exact(args.offset,args.step)
    elif args.order in SEEDS and args.offset==2:
        result=exact_gap_seed(args.order,args.step)
    else:
        result=anchor_gap_mod_four(args.order,args.offset)
    print(json.dumps(result,sort_keys=True))

if __name__=="__main__":
    main()
