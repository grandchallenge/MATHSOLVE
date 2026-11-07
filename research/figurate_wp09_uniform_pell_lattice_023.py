"""FIGURATE WP09-023: complete fixed-pair norm and index-lattice decision.

All arithmetic integer-exact. Finite representative bound may be enormous;
the optional resource guard RAISES, never returns an uncertified negative.
"""
from __future__ import annotations
from math import isqrt


def P(k: int, n: int) -> int:
    if k < 3 or n < 1:
        raise ValueError("positive polygonal index and k>=3 required")
    return n + (k - 2)*n*(n - 1)//2


def fundamental_unit(q: int) -> tuple[int, int]:
    """Minimal positive U,V with U**2-q*V**2=1 (q nonsquare)."""
    if q <= 1 or isqrt(q)**2 == q:
        raise ValueError("positive nonsquare q required")
    m,den,a0=0,1,isqrt(q)
    a=a0
    pprev,p=1,a
    vprev,v=0,1
    if p*p-q*v*v==1:
        return p,v
    while True:
        m=den*a-m
        den=(q-m*m)//den
        a=(a0+m)//den
        pprev,p=p,a*p+pprev
        vprev,v=v,a*v+vprev
        if p*p-q*v*v==1:
            return p,v


def parameters(k: int,c: int,a: int,b: int,r: int) -> dict:
    if not (k>=3 and a>0 and b>0 and a!=b and r>=1
            and a*b+c==P(k,r)):
        raise ValueError("exact positive first pair required")
    R=2*(k-2);L=k-4;D=8*(k-2)*c+L*L
    return {"k":k,"c":c,"a":a,"b":b,"r":r,"Q":a*b,
            "R":R,"L":L,"Delta":D,"N":a*(a-b)*D,"M":2*a*R}


def residue_admissible(p: dict, x: int, s: int) -> bool:
    """Complete integrality lattice conditions; positivity handled by orbit."""
    a,R,L,M=p["a"],p["R"],p["L"],p["M"]
    x%=M;s%=M
    if x%a or (x//a+L)%R or (s+L)%R:
        return False
    index=(s+L)//R
    # This quadratic is integer-valued at all integral indices.
    return (index+(p["k"]-2)*index*(index-1)//2-p["c"])%a==0


def representative_bound(p: dict, unit: tuple[int,int]) -> int:
    """Provably safe integer upper bound for S in a unit fundamental region.

    Write alpha=X+sqrt(Q)S, B=sqrt(abs(N)), eps=U+V sqrt(Q).
    Every positive norm solution normalizes to B<alpha<=eps*B.
    Since X>0, S<alpha/sqrt(Q). Replace irrational numbers by
    strict integral upper bounds, rounding outward.
    """
    if p["N"]==0:
        return 0
    Q=p["Q"];U,V=unit
    upper_eps=U+V*(isqrt(Q)+1)
    upper_B=isqrt(abs(p["N"]))+1
    return isqrt((upper_eps*upper_B)**2//Q)+1


def norm_representatives(p:dict,unit:tuple[int,int],
                         max_bound:int|None=None)->tuple[list[tuple[int,int]],int]:
    cap=representative_bound(p,unit)
    if max_bound is not None and cap>max_bound:
        raise ValueError(f"required complete bound {cap} exceeds guard {max_bound}")
    if p["N"]==0:
        return [],0  # Q nonsquare implies no X,S>0 with X^2-Q*S^2=0.
    Q=p["Q"];N=p["N"];reps=[]
    for S in range(1,cap+1):
        x2=Q*S*S+N
        if x2<=0:
            continue
        X=isqrt(x2)
        if X*X==x2:
            reps.append((X,S))
    return reps,cap


def orbit_hit(p:dict,unit:tuple[int,int],
              start:tuple[int,int])->dict|None:
    """Exhaust complete finite orbit modulo M, no heuristic cutoff."""
    Q,M=p["Q"],p["M"];U,V=unit
    x,s=start[0]%M,start[1]%M
    seen=set();j=0
    while (x,s) not in seen:
        seen.add((x,s))
        if residue_admissible(p,x,s):
            return {"representative":start,"step":j,
                    "residue":(x,s),"orbit_prefix":len(seen)}
        x,s=(U*x+Q*V*s)%M,(V*x+U*s)%M
        j+=1
    return None


def decide(k:int,c:int,a:int,b:int,r:int,
           max_bound:int|None=250000)->dict:
    """Yes/no fixed-first-pair seed existence for nonsquare Q.

    Truncated computation raises ValueError, never returns False.
    """
    p=parameters(k,c,a,b,r);Q=p["Q"]
    if Q<=1 or isqrt(Q)**2==Q:
        raise ValueError("nonsquare first pair product required")
    unit=fundamental_unit(Q)
    representatives,cap=norm_representatives(p,unit,max_bound)
    for rep in representatives:
        hit=orbit_hit(p,unit,rep)
        if hit is not None:
            return {"exists":True,"params":p,"unit":unit,
                    "complete_bound":cap,
                    "representative_count":len(representatives),"hit":hit}
    return {"exists":False,"params":p,"unit":unit,
            "complete_bound":cap,"representative_count":len(representatives),
            "hit":None}


def lift_witness(result:dict)->dict:
    """Construct exact positive seed from yes-certificate.

    If the initial lattice hit collides with a,b or has nonpositive index,
    advance one complete residue period at a time: increasing Pell orbits
    eventually give distinct positive d.
    """
    if not result["exists"]:
        raise ValueError("no positive seed established")
    p=result["params"];Q=p["Q"];M=p["M"];U,V=result["unit"]
    X,S=result["hit"]["representative"]
    target_step=result["hit"]["step"]
    x,s=X%M,S%M
    period=0
    while True:
        x,s=(U*x+Q*V*s)%M,(V*x+U*s)%M
        period+=1
        if (x,s)==(X%M,S%M):
            break
    j=0
    while True:
        if j==target_step or (j>target_step and
                             (j-target_step)%period==0):
            a,b,R,L=p["a"],p["b"],p["R"],p["L"]
            if residue_admissible(p,X,S):
                t=(X//a+L)//R
                si=(S+L)//R
                if si>=1 and t>=1:
                    dnum=P(p["k"],si)-p["c"]
                    if dnum%a==0:
                        d=dnum//a
                        if d>0 and d not in (a,b):
                            if (a*b+p["c"],a*d+p["c"],b*d+p["c"]) != (
                                P(p["k"],p["r"]),P(p["k"],si),P(p["k"],t)):
                                raise ArithmeticError("norm lattice lift invalid")
                            return {"entries":(a,b,d),"indices":(p["r"],si,t),
                                    "norm_coordinates":(X,S),"steps":j}
        X,S=U*X+Q*V*S,V*X+U*S
        j+=1
