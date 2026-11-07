"""FIGURATE WP09-027: conductor-safe oriented ray-norm diagnostics.

Exact discriminant/conductor formula for O=Z[sqrt(2A)], A=8m+1.
Computes necessary inert-prime constraints and verifies a norm/ray generator.
This module DOES NOT compute an order ray class group nor assert principality
without a generator or independently certified ideal class calculation.
"""
from __future__ import annotations
from math import gcd, isqrt

def square_factor(n:int)->tuple[int,int]:
    """Unique n=f^2*d, d positive squarefree."""
    if n<1:raise ValueError("positive integer required")
    f=1;d=1;p=2;remaining=n
    while p*p<=remaining:
        exponent=0
        while remaining%p==0:
            remaining//=p
            exponent+=1
        f*=p**(exponent//2)
        if exponent%2:d*=p
        p+=1 if p==2 else 2
    if remaining>1:d*=remaining
    return f,d

def prime_valuations(n:int)->dict[int,int]:
    if n==0:raise ValueError("nonzero integer required")
    x=abs(n);out={};p=2
    while p*p<=x:
        while x%p==0:
            out[p]=out.get(p,0)+1
            x//=p
        p+=1 if p==2 else 2
    if x>1:out[x]=out.get(x,0)+1
    return out

def order_data(m:int)->dict:
    """Quadratic order O=Z[f*sqrt(d)]; K=Q(sqrt(d)), d=2*a0."""
    if m<0:raise ValueError("m nonnegative")
    A=8*m+1;D=2*A
    f,a0=square_factor(A)
    d=2*a0
    H=8*m*(m+1)+1
    N=-2*(2*A-1)*H
    r=(A+1)//2
    assert d%4==2 and f%2==1 and f*f*a0==A
    assert 8*H==A*A+6*A+1
    assert gcd(abs(N),A)==1
    disc_order=4*D
    disc_field=4*d
    assert disc_order==f*f*disc_field
    rho_norm=r*r*(1-D)
    assert gcd(abs(rho_norm),A)==1
    return {"m":m,"k":16*m+4,"A":A,"D":D,"f":f,
            "squarefree_A":a0,"squarefree_d":d,
            "field_discriminant":disc_field,"order_discriminant":disc_order,
            "H":H,"N":N,"rho_coefficients":(r,r),"rho_norm":rho_norm,
            "conductor_coprime_norm":gcd(abs(N),f)==1}

def inert_prime_obstructions(m:int)->list[dict]:
    """Any odd inert prime at odd norm valuation precludes anchor norm."""
    v=order_data(m)
    d=v["squarefree_d"]
    bad=[]
    for p,e in prime_valuations(v["N"]).items():
        if p==2:continue
        assert d%p!=0 # gcd(|N|,A)=1, odd ramification primes divide A
        legendre=pow(d%p,(p-1)//2,p)
        if legendre==p-1 and e%2:
            bad.append({"prime":p,"norm_exponent":e})
    return bad

def verify_ray_generator(m:int,x:int,y:int)->dict:
    """Check candidate alpha=x+y sqrt(D) in the order, norm and ray."""
    v=order_data(m)
    A=v["A"];r=v["rho_coefficients"][0]
    norm=x*x-v["D"]*y*y
    valid=(x>0 and y>0 and norm==v["N"]
           and (x-r)%A==0 and (y-r)%A==0)
    return {"valid":valid,"norm":norm,"expected_norm":v["N"],
            "ray_coefficients":(x%A,y%A),"target":(r%A,r%A),
            "conductor":v["f"]}

def squarefree_order_generator(m:int,s:int,t:int)->dict:
    """Recover normalized Pell coordinates from exact polygonal indices."""
    if s<1 or t<1:raise ValueError("indices must be positive")
    v=order_data(m);A=v["A"]
    x=A*t-(A-1)//2
    y=A*s-(A-1)//2
    result=verify_ray_generator(m,x,y)
    return {"x":x,"y":y,**result}

def ideal_norm_locally_permitted(m:int)->bool:
    """Exact local ideal-norm criterion in K=Q(sqrt(2A)).

    This is equivalent to the protected WP09-012 every-place local
    Type B criterion for c=2,k=16m+4, but says NOTHING about the
    required oriented ray-principality or exact global anchor seed.
    """
    return len(inert_prime_obstructions(m))==0

def wp09_012_direct_local_oracle(m:int)->bool:
    """Independent direct Legendre formulation from protected WP09-012.

    Delta=32*H, (k-2)/2=A, and gcd(A,H)=1.
    """
    z=order_data(m)
    A,H=z["A"],z["H"]
    for p,e in prime_valuations(H).items():
        if p==2:continue
        if e%2==1 and pow(A%p,(p-1)//2,p)==p-1:
            return False
    return True
