#!/usr/bin/env python3
"""Exact ordinary F2 polynomial checks of Tseitin extension elimination."""
from itertools import product
from random import Random
from functools import reduce
from operator import xor

Z=frozenset()
O=frozenset({()})
def var(i):return frozenset({(i,)})
def mul(a,b):
    r=set()
    for u in a:
        for v in b:r.symmetric_difference_update({tuple(sorted(u+v))})
    return frozenset(r)
def prod(xs):return reduce(mul,xs,O)
def dot(a,b):return reduce(xor,(mul(x,y) for x,y in zip(a,b,strict=True)),Z)
def defect(a):return mul(a,a)^a
def scale(a,hs):return [mul(a,h) for h in hs]
def add(a,b):return [x^y for x,y in zip(a,b,strict=True)]
def unit(n,i):return [O if k==i else Z for k in range(n)]
def subst(p,vs):return reduce(xor,(prod(vs[i] for i in t) for t in p),Z)
def eval_cube(p,a):return sum(all(a[i] for i in t) for t in p)%2
def reduced_lift(p,n):
    r=Z; hs=[Z]*n
    for t in p:
        es=[t.count(i) for i in range(n)]
        for i,e in enumerate(es):
            if e>1:
                for k in range(e-1):
                    m=tuple(j for j in range(n) for _ in range(k if j==i else es[j]))
                    hs[i]^=frozenset({m})
                es[i]=1
        r^=frozenset({tuple(i for i,e in enumerate(es) if e)})
    assert r^dot(hs,[defect(var(i)) for i in range(n)])==p
    return r,hs

def check_circuit(gates):
    n=2;s=len(gates);m=sum(3 if op=='and' else 2 for op,*_ in gates)
    xs=[var(i) for i in range(n)]; B=list(map(defect,xs))
    wires=xs.copy(); arith=xs.copy(); defects=[unit(n,i) for i in range(n)]
    ds=[[Z]*m for _ in range(n)]
    clauses=[]; lifts=[]
    for k,(op,a,b) in enumerate(gates):
        z=var(n+k);u=wires[a];v=wires[b];g=arith[a];h=arith[b]
        c=len(clauses)
        if op=='and':
            cs=[mul(z,O^u),mul(z,O^v),prod([O^z,u,v])]
            dg=add(scale(mul(h,h),defects[a]),scale(g,defects[b]))
            local=add(add(unit(m,c),scale(u,unit(m,c+1))),unit(m,c+2))
            d=add(local,add(scale(u,ds[b]),scale(h,ds[a])))
            fs=[scale(h,defects[a]),scale(g,defects[b]),dg]
            val=mul(g,h)
        else:
            cs=[mul(z,u),mul(O^z,O^u)]
            dg=defects[a];d=add(add(unit(m,c),unit(m,c+1)),ds[a])
            fs=[dg,dg];val=O^g
        wires.append(z);arith.append(val);defects.append(dg);ds.append(d)
        clauses+=cs;lifts+=fs
        assert dot(dg,B)==defect(val)
        assert all(subst(c0,arith)==dot(f,B) for c0,f in zip(cs,fs,strict=True))
    assert len(clauses)==m
    for z,g,d in zip(wires,arith,ds,strict=True):assert z^g==dot(d,clauses)
    g=arith[-1];z=wires[-1]
    sat=any(eval_cube(g,a) for a in product((0,1),repeat=n))
    rem,H=reduced_lift(g,n);assert bool(rem)==sat
    if sat:return 0
    # Forward certificate: gate constraints, output constraint, all Boolean axioms.
    axioms=clauses+[O^z]+list(map(defect,wires))
    coeff=ds[-1]+[O]+H+[Z]*s
    assert dot(coeff,axioms)==O
    # Perturb by a nontrivial Koszul relation, then reverse.
    for i,j in [(0,m),(m,m+n+s)]:
        t=coeff.copy();t[i]^=axioms[j];t[j]^=axioms[i]
        assert dot(t,axioms)==O
        t=[subst(p,arith) for p in t]
        U=t[m];A=[Z]*n
        for q,L in zip(t[:m],lifts,strict=True):A=add(A,scale(q,L))
        for q,L in zip(t[m+1:],defects,strict=True):A=add(A,scale(q,L))
        assert O==mul(U,O^g)^dot(A,B)
        K=add(scale(U,defects[-1]),scale(g,A))
        assert g==dot(K,B)
    return 1

def choices(k):
    return [('not',i,0) for i in range(k)]+[('and',i,j) for i in range(k) for j in range(k)]

def main():
    if not __debug__:raise RuntimeError('assertions required')
    rng=Random(44026)
    circuits=[(a,b,c) for a in choices(2) for b in choices(3) for c in choices(4)]
    circuits += [tuple(rng.choice(choices(2+k)) for k in range(5)) for _ in range(200)]
    u=sum(check_circuit(c) for c in circuits)
    print(f'Circuits={len(circuits)}, UNSAT={u}, SAT controls={len(circuits)-u}, perturbed reverse lifts={2*u}')
if __name__=='__main__':main()
