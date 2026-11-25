"""FIGURATE WP09-010: exact Type B tuples for square-shift polygonal offsets.

For every k>=3,u>=1,a>=1 and c=P_k(u)-a^2, infinitely many exact
distinct positive Type B triples exist. The formal starting triple
(a,b,a) is NEVER itself represented as a valid Type B tuple.
"""
from __future__ import annotations

import argparse
import json
from math import isqrt

from research.figurate_wp09_general_pell_amplification import (
    fundamental_pell_unit, residue_preserving_order, unit_multiply,
)


def polygonal(k: int, n: int) -> int:
    if k < 3 or n < 1:
        raise ValueError("k>=3, n>=1 required")
    return ((k-2)*n*n-(k-4)*n)//2


def exact_type_b(k: int, c: int, entries: tuple[int,int,int],
                 indices: tuple[int,int,int]) -> bool:
    a,b,d=entries
    r,s,t=indices
    return (min(entries)>0 and len(set(entries))==3
            and min(indices)>0
            and a*b+c==polygonal(k,r)
            and a*d+c==polygonal(k,s)
            and b*d+c==polygonal(k,t))


def shifted_square_case(k: int,u: int,a: int) -> bool:
    """Only family where P_k(r)-P_k(u)+a^2 is an exact square polynomial."""
    return k==4 and a==u


def choose_nonsquare_norm(k: int,u: int,a: int,start: int=1) -> tuple[int,int,int]:
    """Find r=u+2a*j, b=(P_k(r)-c)/a, q=a*b nonsquare.

    Termination: F(r)=P_k(r)-P_k(u)+a^2 cannot be eventually square
    on this progression unless (k,a,u)=(4,u,u).
    """
    if k<3 or u<1 or a<1 or start<1:
        raise ValueError("k>=3, u,a,start>=1 required")
    if shifted_square_case(k,u,a):
        raise ValueError("use direct square-order exception")
    c=polygonal(k,u)-a*a
    j=start
    while True:
        r=u+2*a*j
        q=polygonal(k,r)-c
        if q%a:
            raise AssertionError("arithmetic progression not divisible by a")
        b=q//a
        if b>a and q>1 and isqrt(q)**2!=q:
            return r,b,q
        j+=1


def formal_repeat_seed(k: int,u: int,a: int,r: int) -> dict:
    """The repeated (a,b,a) algebraic starting point; not Type B."""
    if k<3 or u<1 or a<1 or r<1:
        raise ValueError("positive indices, order and first entry required")
    c=polygonal(k,u)-a*a
    q=polygonal(k,r)-c
    if q%a:
        raise ValueError("a must divide P_k(r)-c")
    b=q//a
    if b<=a or isqrt(q)**2==q:
        raise ValueError("need b>a and nonsquare q=a*b")
    R,L=2*(k-2),k-4
    S=R*u-L
    T=R*r-L
    D=8*(k-2)*c+L*L
    X=a*T
    N=a*(a-b)*D
    if X*X-q*S*S !=N:
        raise AssertionError("exact generalized Pell identity failed")
    return {"order":k,"offset":c,"a":a,"b":b,"q":q,"r":r,
            "u":u,"R":R,"L":L,"S":S,"T":T,"X":X,"D":D,"norm":N}


def promote_formal_seed(k: int,u: int,a: int,r: int,step: int=1) -> dict:
    if step<1:
        raise ValueError("Pell step must be positive")
    z=formal_repeat_seed(k,u,a,r)
    q,R,L=z["q"],z["R"],z["L"]
    # Fix the S coordinate modulo 2*a*R: then the new polygonal index
    # s is congruent to u modulo 2*a and P_k(s)-c is divisible by a.
    # Fix X modulo 2*a*R: X/a stays an integer with valid t index.
    modulus=2*a*R
    unit=fundamental_pell_unit(q)
    order=residue_preserving_order(q,*unit,modulus)
    base=(1,0)
    for _ in range(order):
        base=unit_multiply(base,unit,q)
    multiplier=(1,0)
    n=step
    while n:
        if n&1:
            multiplier=unit_multiply(multiplier,base,q)
        base=unit_multiply(base,base,q)
        n>>=1
    U,V=multiplier
    X=U*z["X"]+q*V*z["S"]
    S=V*z["X"]+U*z["S"]
    if X*X-q*S*S != z["norm"]:
        raise AssertionError("Pell norm lost")
    if (X-z["X"])%modulus or (S-z["S"])%modulus:
        raise AssertionError("full congruence preservation failed")
    if X%a:
        raise AssertionError("X not divisible by a")
    T=X//a
    if (T+L)%R or (S+L)%R:
        raise AssertionError("polygonal index residues failed")
    t=(T+L)//R
    s=(S+L)//R
    if min(t,s)<1:
        raise AssertionError("nonpositive polygonal index")
    output=polygonal(k,s)-z["offset"]
    if output%a:
        raise AssertionError("third entry integrality failed")
    d=output//a
    entries=(a,z["b"],d)
    indices=(r,s,t)
    if not exact_type_b(k,z["offset"],entries,indices):
        raise AssertionError("promoted tuple not exact and distinct")
    return {"order":k,"offset":z["offset"],"seed_index":u,
            "first_entry":a,"entries":entries,"indices":indices,
            "norm":z["norm"],"nonsquare_q":q,
            "pell_unit":unit,"unit_order":order,"step":step,
            "method":"square-shift-Pell-promotion"}


def square_order_exception(u: int,step: int=1) -> dict:
    if u<1 or step<1:
        raise ValueError("u,step>=1 required")
    # k=4, a=u, c=0: products of entries (u,4u,(step+2)^2*u)
    # are exact squares, indexed by 2u, (step+2)u, 2(step+2)u.
    n=step+2
    entries=(u,4*u,n*n*u)
    indices=(2*u,n*u,2*n*u)
    if len(set(entries))!=3 or not exact_type_b(4,0,entries,indices):
        raise AssertionError("square-order exception failed")
    return {"order":4,"offset":0,"seed_index":u,
            "first_entry":u,"entries":entries,"indices":indices,
            "step":step,"method":"square-order-exception"}


def square_shift_family(k: int,u: int,a: int,step: int=1,
                        start: int=1) -> dict:
    if k<3 or u<1 or a<1 or step<1 or start<1:
        raise ValueError("k>=3 and u,a,step,start>=1 required")
    if shifted_square_case(k,u,a):
        return square_order_exception(u,step)
    r,b,q=choose_nonsquare_norm(k,u,a,start)
    result=promote_formal_seed(k,u,a,r,step)
    if result["entries"][1]!=b or result["nonsquare_q"]!=q:
        raise AssertionError("chosen nonsquare second entry mismatched")
    return result


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--order",type=int,default=7)
    p.add_argument("--index",type=int,default=2)
    p.add_argument("--first-entry",type=int,default=2)
    p.add_argument("--step",type=int,default=1)
    a=p.parse_args()
    print(json.dumps(square_shift_family(a.order,a.index,a.first_entry,
                                         a.step),sort_keys=True))


if __name__=="__main__":
    main()
