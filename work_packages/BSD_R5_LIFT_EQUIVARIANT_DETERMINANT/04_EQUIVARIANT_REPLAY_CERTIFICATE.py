#!/usr/bin/env python3
"""Deterministic finite structural certificate for BSD-R5-LIFT-EQUIV.

This certificate checks finite algebra/representation facts used by the theorem.
It is not a substitute for the written all-level argument and creates no
MATHCERT authority.
"""
from __future__ import annotations

import itertools
from collections import deque


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("BSD R5-LIFT equivariant certificate: FAIL: " + msg)


def mm(A, B, mod):
    a,b,c,d=A; e,f,g,h=B
    return ((a*e+b*g)%mod,(a*f+b*h)%mod,(c*e+d*g)%mod,(c*f+d*h)%mod)


def det(A, mod):
    return (A[0]*A[3]-A[1]*A[2])%mod


def inv_sl(A, mod):
    a,b,c,d=A
    return (d%mod,(-b)%mod,(-c)%mod,a%mod)


def sl2(mod):
    return [(a,b,c,d) for a,b,c,d in itertools.product(range(mod), repeat=4)
            if det((a,b,c,d),mod)==1%mod]


def act_res(A, v):
    a,b,c,d=(x%2 for x in A); x,y=v
    return ((a*x+b*y)%2,(c*x+d*y)%2)


def h1_sl2_with_residual_values(mod):
    """Compute H^1(SL2(Z/mod), F2^2) from U,L generators."""
    G=sl2(mod)
    I=(1,0,0,1); U=(1,1,0,1); L=(1,0,1,1)
    gens=[U,L,inv_sl(U,mod),inv_sl(L,mod)]
    vals=list(itertools.product(range(2), repeat=2))
    cocycle_generator_values=[]
    for fU in vals:
        for fL in vals:
            fgens=[fU,fL,act_res(inv_sl(U,mod),fU),act_res(inv_sl(L,mod),fL)]
            f={I:(0,0)}
            q=deque([I]); ok=True
            while q and ok:
                g=q.popleft(); fg=f[g]
                for s,fs in zip(gens,fgens):
                    h=mm(g,s,mod)
                    afs=act_res(g,fs)
                    val=((fg[0]+afs[0])%2,(fg[1]+afs[1])%2)
                    if h in f:
                        if f[h]!=val:
                            ok=False; break
                    else:
                        f[h]=val; q.append(h)
            if ok and len(f)==len(G):
                cocycle_generator_values.append((fU,fL))
    cob=set()
    for v in vals:
        fu=tuple((x+y)%2 for x,y in zip(act_res(U,v),v))
        fl=tuple((x+y)%2 for x,y in zip(act_res(L,v),v))
        cob.add((fu,fl))
    req(len(cocycle_generator_values)%len(cob)==0, "cocycle quotient")
    return len(G), len(cocycle_generator_values)//len(cob)


def gl2_f2():
    return [(a,b,c,d) for a,b,c,d in itertools.product(range(2), repeat=4)
            if det((a,b,c,d),2)==1]


def hom_sl2_residual_dimension():
    """Check dim Hom_{S3}(sl2(F2), F2^2)=1."""
    G=gl2_f2()
    sl=[(a,b,c,a) for a,b,c in itertools.product(range(2), repeat=3)]
    def inv2(A):
        a,b,c,d=A
        return (d,b,c,a)
    def conj(g,x):
        y=mm(mm(g,x,2),inv2(g),2)
        return (y[0],y[1],y[2])
    count=0
    for coeff in itertools.product(range(2), repeat=6):
        def f(coords):
            a,b,c=coords
            return ((coeff[0]*a+coeff[1]*b+coeff[2]*c)%2,
                    (coeff[3]*a+coeff[4]*b+coeff[5]*c)%2)
        ok=True
        for g in G:
            for x in sl:
                if f(conj(g,x)) != act_res(g,f((x[0],x[1],x[2]))):
                    ok=False; break
            if not ok: break
        if ok: count+=1
    req(count==2, "Hom_S3(sl2,V) should contain exactly two maps")
    return 1


def ring_add(a,b,q): return tuple((x+y)%q for x,y in zip(a,b))

def ring_mul(a,b,q):
    d=len(a); out=[0]*d
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[(i+j)%d]=(out[(i+j)%d]+x*y)%q
    return tuple(out)


def check_group_ring(m,n):
    q=2**m; d=2**n
    els=list(itertools.product(range(q), repeat=d))
    zero=(0,)*d
    two=(2%q,)+(0,)*(d-1)
    gamma=(0,1)+(0,)*(d-2) if d>1 else (1,)
    one=(1,)+(0,)*(d-1)
    X=ring_add(gamma,tuple((-x)%q for x in one),q)
    maximal=[a for a in els if sum(a)%2==0]
    req(len(maximal)==len(els)//2, f"residue field size at m={m},n={n}")
    # Socle = annihilator of maximal ideal; generators 2 and X suffice.
    soc=[]
    for a in els:
        if ring_mul(two,a,q)==zero and ring_mul(X,a,q)==zero:
            soc.append(a)
    req(len(soc)==2, f"socle dimension at m={m},n={n}: {len(soc)}")
    return len(els), len(maximal), len(soc)


def main():
    req(len(gl2_f2())==6, "GL2(F2) order")
    homdim=hom_sl2_residual_dimension()
    h1=[]
    for mod in (4,8):
        order,size=h1_sl2_with_residual_values(mod)
        req(size==2, f"H1 SL2 mod {mod} size")
        h1.append((mod,order,size))
    rings=[]
    for m,n in ((1,0),(2,0),(1,1),(2,1),(2,2)):
        rings.append((m,n,*check_group_ring(m,n)))
    print({
        "status":"PASS",
        "operation":"BSD-R5-LIFT-EQUIV",
        "hom_S3_sl2_to_V_dimension":homdim,
        "sample_SL2_H1":h1,
        "sample_group_rings":rings,
        "formal_higher_level_hypothesis_3_2_iii":False,
        "infinite_bss_h3":False,
        "r5_prim":False,
        "bsd_r2_a1":False,
        "mathcert_certification":False,
    })


if __name__=="__main__":
    main()
