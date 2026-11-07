"""FIGURATE WP09-026: exact linear-gcd replacement for Pell residue orbit.

For normalized anchor q=2A, A=8m+1 odd, the unit matrix modulo A
has a square that is a unipotent shear. Two linear congruences decide
whether a complete infinite norm-one orbit meets the prescribed residue.
No residue-orbit enumeration is needed; this is exact, not a heuristic.
"""
from __future__ import annotations
from math import gcd
from research.figurate_wp09_uniform_pell_lattice_023 import (
    fundamental_unit,norm_representatives,
)
from research.figurate_wp09_odd_ray_lattice_025 import normalized_parameters

def solve_linear_congruence(coefficient:int,rhs:int,modulus:int)->int|None:
    """Least j>=0 solving coefficient*j == rhs modulo modulus.

    Returns None iff gcd(coefficient, modulus) does not divide rhs.
    """
    if modulus<1:
        raise ValueError("positive modulus required")
    coefficient%=modulus
    rhs%=modulus
    g=gcd(coefficient,modulus)
    if rhs%g:
        return None
    n=modulus//g
    if n==1:
        return 0
    return ((rhs//g)*pow(coefficient//g,-1,n))%n

def linear_ray_hit(p:dict,unit:tuple[int,int],
                   rep:tuple[int,int])->dict|None:
    """Complete orbit hit via at most TWO gcd solvability checks.

    Powers modulo odd A:
      T^(2j)   : (x,y) -> (x, y+2*j*U*V*x)
      T^(2j+1) : (x,y) -> (U*x, U*y+(2*j+1)*V*x).
    """
    A,Q=p["A"],p["Q"];U,V=unit
    if A<1 or A%2!=1 or Q!=2*A or U*U-Q*V*V!=1:
        raise ValueError("invalid primitive anchor/unit")
    x,y=rep[0]%A,rep[1]%A
    r=(A+1)//2 %A
    g=gcd(V,A)
    options=[]
    if x==r:
        j=solve_linear_congruence(2*U*V*x,r-y,A)
        if j is not None:
            options.append((2*j,"even",j))
    if U*x%A==r:
        j=solve_linear_congruence(2*V*x,r-(U*y+V*x),A)
        if j is not None:
            options.append((2*j+1,"odd",j))
    if not options:
        return None
    step,branch,j=min(options,key=lambda z:z[0])
    return {"representative":rep,"step":step,"period":2*(A//g),
            "residue":(r,r),"branch":branch,"j":j,"gcd":g}

def linear_gcd_decide(k:int,max_bound:int|None=250000)->dict:
    """Complete YES/NO for specified anchor, with zero orbit enumeration."""
    p=normalized_parameters(k)
    unit=fundamental_unit(p["Q"])
    reps,cap=norm_representatives(p,unit,max_bound)
    for rep in reps:
        hit=linear_ray_hit(p,unit,rep)
        if hit is not None:
            return {"exists":True,"params":p,"unit":unit,"hit":hit,
                    "complete_bound":cap,"representative_count":len(reps),
                    "orbit_enumeration_required":False}
    return {"exists":False,"params":p,"unit":unit,"hit":None,
            "complete_bound":cap,"representative_count":len(reps),
            "orbit_enumeration_required":False}

def verified_hit_modulo(p:dict,unit:tuple[int,int],
                        rep:tuple[int,int],step:int)->bool:
    """Independent direct finite modular power, useful as a certificate."""
    if step<0:
        raise ValueError("nonnegative step required")
    A,Q=p["A"],p["Q"];U,V=unit
    x,y=rep[0]%A,rep[1]%A
    # Fast binary exponentiation for unit action modulo A.
    ux,uy=1%A,0
    vx,vy=U%A,V%A
    n=step
    while n:
        if n&1:
            ux,uy=(ux*vx+Q*uy*vy)%A,(ux*vy+uy*vx)%A
        vx,vy=(vx*vx+Q*vy*vy)%A,(2*vx*vy)%A
        n//=2
    xx,yy=(ux*x+Q*uy*y)%A,(uy*x+ux*y)%A
    target=(A+1)//2%A
    return (xx,yy)==(target,target)
