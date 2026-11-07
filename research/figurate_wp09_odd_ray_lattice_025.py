"""FIGURATE WP09-025: exact normalized odd-modulus anchor Pell criterion.

For k=16m+4,c=2, anchor (a,b,r)=(1,k-2,2), write A=8m+1.
The original norm coordinates X,S are divisible by four on the
required lattice. x=X/4,y=S/4 then satisfy an exact reduced Pell norm
and the single residue (2*x,2*y)==(1,1) modulo the ODD integer A.

The criterion decides anchor existence, not global existence for all
possible first pairs. Resource guards never produce false NO claims.
"""
from __future__ import annotations
from math import isqrt
from research.figurate_wp09_uniform_pell_lattice_023 import (
    P,fundamental_unit,norm_representatives,representative_bound,
)

def normalized_parameters(k:int)->dict:
    if k<4 or k%16!=4:
        raise ValueError("requires polygonal order k=4 mod 16")
    m=(k-4)//16
    A=8*m+1
    q=2*A
    H=8*m*(m+1)+1
    N=-2*(2*A-1)*H
    return {"k":k,"m":m,"A":A,"Q":q,"H":H,"N":N,
            "target":(A+1)//2,"modulus":A}

def ray_admissible(p:dict,x:int,y:int)->bool:
    A=p["A"]
    return (2*x-1)%A==0 and (2*y-1)%A==0

def ray_orbit(p:dict, unit:tuple[int,int],
              rep:tuple[int,int])->dict|None:
    A,Q=p["A"],p["Q"];U,V=unit
    x,y=rep[0]%A,rep[1]%A
    seen=set();first=None;j=0
    while (x,y) not in seen:
        seen.add((x,y))
        if first is None and ray_admissible(p,x,y):
            first={"representative":rep,"step":j,"residue":(x,y)}
        x,y=(U*x+Q*V*y)%A,(V*x+U*y)%A
        j+=1
    if (x,y)!=(rep[0]%A,rep[1]%A):
        raise ArithmeticError("noninvertible orbit, impossible for Pell unit")
    if first is not None:
        first["period"]=j
    return first

def normalized_decide(k:int,max_bound:int|None=250000)->dict:
    """Complete YES/NO for the anchor (1,k-2), not all first pairs."""
    p=normalized_parameters(k)
    unit=fundamental_unit(p["Q"])
    reps,cap=norm_representatives(p,unit,max_bound)
    for rep in reps:
        hit=ray_orbit(p,unit,rep)
        if hit:
            return {"exists":True,"params":p,"unit":unit,
                    "complete_bound":cap,"representative_count":len(reps),
                    "hit":hit}
    return {"exists":False,"params":p,"unit":unit,
            "complete_bound":cap,"representative_count":len(reps),
            "hit":None}

def construct_exact_seed(result:dict,max_lift_steps:int|None=None)->dict:
    """Convert reduced norm + congruence hit into exact positive Type B seed."""
    if not result["exists"]:
        raise ValueError("cannot construct a seed from a NO certificate")
    p=result["params"]
    k,A,Q=p["k"],p["A"],p["Q"];U,V=result["unit"]
    step=result["hit"]["step"];period=result["hit"]["period"]
    x,y=result["hit"]["representative"]
    n=0
    while True:
        if n>=step and (n-step)%period==0:
            if not ray_admissible(p,x,y):
                raise ArithmeticError("lost residue lattice")
            # s=(S+k-4)/R=(y+(A-1)/2)/A; same for t with x.
            s=(y+(A-1)//2)//A
            t=(x+(A-1)//2)//A
            if s>=1 and t>=1:
                d=P(k,s)-2
                if d>0 and d not in (1,Q):
                    if (Q+2,d+2,Q*d+2)!=(P(k,2),P(k,s),P(k,t)):
                        raise ArithmeticError("lifted norm is not exact")
                    return {"entries":(1,Q,d),"indices":(2,s,t),
                            "reduced_coordinates":(x,y),"pell_steps":n,
                            "modulus":A}
        if max_lift_steps is not None and n>=max_lift_steps:
            raise ValueError("explicit constructive step guard reached; not a NO")
        x,y=U*x+Q*V*y,V*x+U*y
        n+=1

def independent_norm_identity(k:int,s:int,t:int,d:int)->bool:
    """Exact direct control of both the primitive norm and index lattice."""
    p=normalized_parameters(k)
    A,Q,H=p["A"],p["Q"],p["H"]
    if min(s,t,d)<1 or P(k,s)!=d+2 or P(k,t)!=Q*d+2:
        return False
    x=A*t-(A-1)//2
    y=A*s-(A-1)//2
    return (x*x-Q*y*y==-2*(2*A-1)*H
            and ray_admissible(p,x,y))
