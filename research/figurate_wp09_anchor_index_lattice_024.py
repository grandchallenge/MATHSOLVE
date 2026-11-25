"""FIGURATE WP09-024: uniform anchor 2-adic branches and minimal safe Pell modulus.

Provides exact necessary restrictions for k=16m+4,c=2,a=1,b=k-2,r=2.
Reduces the orbit modulus used in WP09-023 by a factor of 2 whenever
k is even or a is odd. Does not assert universal seed existence.
"""
from __future__ import annotations
from research.figurate_wp09_uniform_pell_lattice_023 import (
    P, parameters, fundamental_unit, norm_representatives, orbit_hit,
    lift_witness,
)
from math import isqrt

def index_period(k:int,a:int)->int:
    """Smallest of the two universally safe polynomial periods a and 2a."""
    if k<3 or a<1:
        raise ValueError("k>=3,a>=1")
    return a if (k-2)*(a-1)%2==0 else 2*a

def sufficient_residue_modulus(k:int,a:int)->int:
    """M=R*h suffices for all seed lattice and third-entry checks."""
    return 2*(k-2)*index_period(k,a)

def anchor_params(k:int)->dict:
    if k<4 or k%16!=4:
        raise ValueError("anchor classification requires k=4 mod16")
    return parameters(k,2,1,k-2,2)

def anchor_branch_predicate(k:int,s:int,t:int,d:int)->bool:
    """Necessary, not sufficient, congruence signature of an exact seed."""
    if k<4 or k%16!=4 or min(s,t,d)<1:
        raise ValueError("k=4 mod16, s,t,d positive required")
    m=(k-4)//16
    return (s%2==1 and d%8==7 and t%4==0
            and t%8==4*((m+((s*s-1)//8))%2))

def optimized_orbit_decision(k:int,c:int,a:int,b:int,r:int,
                             max_bound:int|None=250000)->dict:
    """WP09-023 complete fixed-pair criterion on a smaller proven modulus.

    A guard failure raises ValueError rather than reporting absence.
    """
    p=parameters(k,c,a,b,r)
    q=p["Q"]
    if q<=1 or isqrt(q)**2==q:
        raise ValueError("nonsquare product required")
    p["M"]=sufficient_residue_modulus(k,a)
    u=fundamental_unit(q)
    reps,cap=norm_representatives(p,u,max_bound)
    for rep in reps:
        hit=orbit_hit(p,u,rep)
        if hit is not None:
            return dict(exists=True,params=p,unit=u,
                        complete_bound=cap,representative_count=len(reps),
                        hit=hit,modulus=p["M"])
    return dict(exists=False,params=p,unit=u,
                complete_bound=cap,representative_count=len(reps),
                hit=None,modulus=p["M"])

def verify_anchor_witness(k:int,s:int,t:int,d:int)->bool:
    """Direct exact equations PLUS necessary 2-adic branch assertions."""
    p=anchor_params(k)
    a,b=1,k-2
    return (anchor_branch_predicate(k,s,t,d)
            and a*b+2==P(k,2)
            and a*d+2==P(k,s)
            and b*d+2==P(k,t))

def decide_anchor(k:int,max_bound:int|None=250000)->dict:
    return optimized_orbit_decision(k,2,1,k-2,2,max_bound=max_bound)
