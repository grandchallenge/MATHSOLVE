"""FIGURATE WP09-008: general Pell amplification of exact Type B seed triples.

Any exact Type B (1,b,d), b>1 nonsquare, amplifies to infinitely many
exact triples with the first two entries fixed. Every returned pair output
is an EXACT positive-index polygonal integer.
"""
from __future__ import annotations
import argparse
import json
from math import isqrt

def polygonal(k: int, t: int) -> int:
    if k < 3 or t < 1:
        raise ValueError("polygonal order>=3 and index>=1 required")
    return ((k-2)*t*t-(k-4)*t)//2

def verified_seed(k: int, c: int, r: int, s: int, t: int) -> tuple[int, int]:
    b = polygonal(k, r)-c
    d = polygonal(k, s)-c
    if not (1 < b and d > 1 and b != d and b*d+c == polygonal(k, t)):
        raise ValueError("seed must be exact positive Type B (1,b,d), b>1,d>1,b!=d")
    if isqrt(b)**2 == b:
        raise ValueError("second entry b must be nonsquare")
    return b, d

def fundamental_pell_unit(b: int) -> tuple[int,int]:
    """Minimal positive u+v sqrt(b) with u^2-bv^2=1."""
    a0=isqrt(b)
    if b<=1 or a0*a0==b:
        raise ValueError("nonsquare b>1 required")
    m,den,a=0,1,a0
    h_old,h_prev=1,0
    k_old,k_prev=0,1
    while True:
        h=a*h_old+h_prev
        v=a*k_old+k_prev
        if h*h-b*v*v==1:
            return h,v
        h_prev,h_old=h_old,h
        k_prev,k_old=k_old,v
        m=den*a-m
        den=(b-m*m)//den
        a=(a0+m)//den

def unit_multiply(x: tuple[int,int], y: tuple[int,int], b: int
                 ) -> tuple[int,int]:
    u,v=x
    h,j=y
    return u*h+b*v*j,u*j+v*h

def residue_preserving_order(b: int, u: int, v: int, R: int) -> int:
    """Finite order of a norm-one unit modulo R."""
    if R<2:
        raise ValueError("modulus at least 2 required")
    x,y=1,0
    for e in range(1,R*R+1):
        x,y=(u*x+b*v*y)%R,(v*x+u*y)%R
        if (x,y)==(1,0):
            return e
    raise ArithmeticError("unit order unexpectedly exceeded R^2")

def positive_pell_seed(k: int,c: int,r: int,s: int,t: int) -> dict:
    b,d=verified_seed(k,c,r,s,t)
    R=2*(k-2)
    L=k-4
    S=R*s-L
    T=R*t-L
    delta=8*(k-2)*c+L*L
    norm=-(b-1)*delta
    if T*T-b*S*S != norm:
        raise AssertionError("polygonal Pell identity mismatch")
    if (S+L)%R or (T+L)%R or min(S,T)<=0:
        raise AssertionError("seed index or sign invalid")
    return {"order":k,"offset":c,"r":r,"s":s,"t":t,"b":b,"d":d,
            "R":R,"L":L,"S":S,"T":T,"delta":delta,"norm":norm}

def amplify_seed(k: int,c: int,r: int,s: int,t: int,steps: int) -> dict:
    if steps<0:
        raise ValueError("steps>=0 required")
    data=positive_pell_seed(k,c,r,s,t)
    b,R,L=data["b"],data["R"],data["L"]
    u,v=fundamental_pell_unit(b)
    order=residue_preserving_order(b,u,v,R)
    U,V=1,0
    for _ in range(order):
        U,V=unit_multiply((U,V),(u,v),b)
    E,F=1,0
    n=steps
    while n:
        if n&1:
            E,F=unit_multiply((E,F),(U,V),b)
        U,V=unit_multiply((U,V),(U,V),b)
        n>>=1
    T=E*data["T"]+b*F*data["S"]
    S=F*data["T"]+E*data["S"]
    if T*T-b*S*S != data["norm"] or (S+L)%R or (T+L)%R:
        raise ArithmeticError("Pell recurrence lost invariant")
    sn=(S+L)//R
    tn=(T+L)//R
    d=polygonal(k,sn)-c
    if not (1<b and d>1 and b!=d and b*d+c==polygonal(k,tn)):
        raise ArithmeticError("generated exact tuple invalid")
    return {"order":k,"offset":c,"steps":steps,
            "entries":(1,b,d),"indices":(r,sn,tn),
            "pell":{"S":S,"T":T,"norm":data["norm"],
                    "fundamental_unit":(u,v),"residue_order":order}}

SEEDS={
 "pentagonal":(5,2,2,48,83),
 "hexagonal":(6,2,3,5,17),
 "icosagonal":(20,2,2,39,164),
}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--seed",choices=sorted(SEEDS),default="pentagonal")
    p.add_argument("--steps",type=int,default=0)
    a=p.parse_args()
    print(json.dumps(amplify_seed(*SEEDS[a.seed],a.steps),sort_keys=True))

if __name__=="__main__":
    main()
