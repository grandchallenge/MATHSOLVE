"""FIGURATE WP09-009: explicit seed existence for c=P_k(u)-1.

For any order k>=3 and positive integer u, this offset has infinitely
many exact Type B triples. For (k,u)!=(4,1), nonsquare fixed second
entries occur infinitely often; a degenerate equal-entry starting point
is promoted by an exact Pell unit to distinct positive integers.
The exceptional (4,1) case has direct square-output triples.
"""
from __future__ import annotations
import argparse
import json
from math import isqrt
from research.figurate_wp09_general_pell_amplification import (
    fundamental_pell_unit, residue_preserving_order, unit_multiply
)


def polygonal(k: int, t: int) -> int:
    if k < 3 or t < 1:
        raise ValueError("k>=3 and t>=1 required")
    return ((k - 2)*t*t - (k - 4)*t)//2


def exact_type_b(k: int, c: int, entries: tuple[int,int,int],
                 indices: tuple[int,int,int]) -> bool:
    a,b,d=entries
    r,s,t=indices
    return (min(entries)>0 and len(set(entries))==3
            and min(indices)>0
            and a*b+c==polygonal(k,r)
            and a*d+c==polygonal(k,s)
            and b*d+c==polygonal(k,t))


def choose_nonsquare_second_entry(k: int, u: int, start: int=2) -> tuple[int,int]:
    """Termination proved by eventual-polynomial-square contradiction.

    Does not apply to the square-number c=0 exception (k,u)=(4,1).
    """
    if k<3 or u<1 or start<1:
        raise ValueError("invalid polygonal order, u or start")
    if (k,u)==(4,1):
        raise ValueError("all candidate second entries are squares")
    c=polygonal(k,u)-1
    r=max(2,start)
    while True:
        b=polygonal(k,r)-c
        if b>1 and isqrt(b)**2!=b:
            return r,b
        r+=1


def degenerate_pell_seed(k: int, u: int, r: int) -> dict:
    """Exact identities for (1,b,1) used only as a formal seed.

    The repeated-entry seed is NOT a Type B triple.
    """
    if k<3 or u<1 or r<1:
        raise ValueError("positive polygonal parameters required")
    c=polygonal(k,u)-1
    b=polygonal(k,r)-c
    if b<=1 or isqrt(b)**2==b:
        raise ValueError("choose b>1 nonsquare")
    R,L=2*(k-2),k-4
    S,T=R*u-L,R*r-L
    D=8*(k-2)*c+L*L
    N=-(b-1)*D
    if (T*T-b*S*S)!=N:
        raise AssertionError("formal seed norm identity fails")
    return {"k":k,"u":u,"r":r,"c":c,"b":b,
            "R":R,"L":L,"S":S,"T":T,"D":D,"norm":N}


def promote_degenerate_seed(k: int, u: int, r: int, step: int=1) -> dict:
    """Construct an actual exact Type B triple from the formal repeated seed.

    step=0 is prohibited: it would retain the repeated entry d=1.
    """
    if step<1:
        raise ValueError("step must be positive")
    seed=degenerate_pell_seed(k,u,r)
    b,R,L=seed["b"],seed["R"],seed["L"]
    fundamental=fundamental_pell_unit(b)
    order=residue_preserving_order(b,*fundamental,R)
    # Norm-one unit raised to a finite ring order preserves both indices.
    unit=(1,0)
    for _ in range(order):
        unit=unit_multiply(unit,fundamental,b)
    multiplier=(1,0)
    while step:
        if step&1:
            multiplier=unit_multiply(multiplier,unit,b)
        unit=unit_multiply(unit,unit,b)
        step//=2
    E,F=multiplier
    T=E*seed["T"]+b*F*seed["S"]
    S=F*seed["T"]+E*seed["S"]
    if T*T-b*S*S!=seed["norm"] or (T+L)%R or (S+L)%R:
        raise AssertionError("Pell norm / index congruence failed")
    t,s=(T+L)//R,(S+L)//R
    d=polygonal(k,s)-seed["c"]
    entries=(1,b,d)
    indices=(r,s,t)
    if not exact_type_b(k,seed["c"],entries,indices):
        raise AssertionError("promoted tuple is not exact or distinct")
    return {"order":k,"offset":seed["c"],"u":u,
            "entries":entries,"indices":indices,
            "pell_norm":seed["norm"],
            "fundamental_unit":fundamental,"residue_order":order}


def constructive_offset_family(k: int,u: int, fixed_seed_start: int=2,
                               step: int=1) -> dict:
    """Universal constructor for c=P_k(u)-1, with explicit square exception."""
    if k<3 or u<1 or step<1:
        raise ValueError("k>=3,u>=1,step>=1 required")
    c=polygonal(k,u)-1
    if (k,u)==(4,1):
        # At c=0 every output is a square. 1, r^2, s^2 are distinct.
        r=max(2,fixed_seed_start)
        s=r+step
        entries=(1,r*r,s*s)
        indices=(r,s,r*s)
        if not exact_type_b(4,0,entries,indices):
            raise AssertionError("square exception construction invalid")
        return {"order":4,"offset":0,"entries":entries,
                "indices":indices,"method":"square-exception"}
    r,_=choose_nonsquare_second_entry(k,u,fixed_seed_start)
    result=promote_degenerate_seed(k,u,r,step)
    result["method"]="degenerate-seed-Pell-promotion"
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--order",type=int,default=7)
    p.add_argument("--index",type=int,default=2)
    p.add_argument("--seed-start",type=int,default=2)
    p.add_argument("--step",type=int,default=1)
    a=p.parse_args()
    print(json.dumps(constructive_offset_family(a.order,a.index,
                                               a.seed_start,a.step),
                     sort_keys=True))


if __name__=="__main__":
    main()
