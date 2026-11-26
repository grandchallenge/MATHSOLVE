#!/usr/bin/env python3
"""Ordinary sparse polynomial identities, independent of WP42 code."""
from itertools import product

def check(p):
    # 2 clauses on one variable: 4 input presence bits and one witness.
    d=5
    O={(0,)*d:1}; Z={}
    def add(a,b):
        r=a.copy()
        for t,c in b.items():
            v=(r.get(t,0)+c)%p
            if v:r[t]=v
            elif t in r:del r[t]
        return r
    def neg(a):return {t:(-c)%p for t,c in a.items()}
    def sub(a,b):return add(a,neg(b))
    def mul(a,b):
        r={}
        for t,c in a.items():
            for s,k in b.items():
                e=tuple(i+j for i,j in zip(t,s));v=(r.get(e,0)+c*k)%p
                if v:r[e]=v
                elif e in r:del r[e]
        return r
    def prod(xs):
        r=O
        for x in xs:r=mul(r,x)
        return r
    def dot(a,b):
        r=Z
        for x,y in zip(a,b,strict=True):r=add(r,mul(x,y))
        return r
    X=[{tuple(int(j==i) for j in range(d)):1} for i in range(d)]
    B=[sub(mul(x,x),x) for x in X]
    def spec(f,a):
        r=Z
        for t,c in f.items():
            if any(e and not v for e,v in zip(t,a)):continue
            r=add(r,{(0,)*len(a)+t[len(a):]:c})
        return r
    def reduce_lift(f):
        r=Z; h=[Z]*d
        for t,c in f.items():
            u=list(t)
            for i,e in enumerate(u):
                if e<2:continue
                for k in range(e-1):
                    v=u.copy();v[i]=k
                    h[i]=add(h[i],{tuple(v):c})
                u[i]=1
            r=add(r,{tuple(u):c})
        assert f==add(r,dot(h,B))
        return r,h
    def plus(a,b):return ('+',a,b)
    def minus(a,b):return ('-',a,b)
    def times(a,b):return ('*',a,b)
    one=('c',O); x=('c',X[-1])
    literals=[minus(one,x),x]*2
    terms=[minus(one,times(('u',i),minus(one,l))) for i,l in enumerate(literals)]
    v=times(minus(one,times(terms[0],terms[1])),
            minus(one,times(terms[2],terms[3])))
    def diff(g,a):
        op,*t=g; z=[Z]*4
        if op=='c':return t[0],t[0],z
        if op=='u':
            i=t[0];z[i]=O;return X[i],O if a[i] else Z,z
        U,u,A=diff(t[0],a);V,v,Bv=diff(t[1],a)
        if op=='+':return add(U,V),add(u,v),[add(j,k) for j,k in zip(A,Bv)]
        if op=='-':return sub(U,V),sub(u,v),[sub(j,k) for j,k in zip(A,Bv)]
        return mul(U,V),mul(u,v),[add(mul(U,k),mul(v,j)) for j,k in zip(A,Bv)]
    cases=unsat=0
    for a in product((0,1),repeat=4):
        V,S,D=diff(v,a)
        assert S==spec(V,a)
        delta=[sub(X[i],O if a[i] else Z) for i in range(4)]
        assert sub(V,S)==dot(delta,D)
        E=[X[i] if a[i] else sub(O,X[i]) for i in range(4)]
        sel=prod(E)
        U=[]
        for i in range(4):
            q=mul(D[i],prod(E[:i]+E[i+1:]))
            U.append(q if a[i] else neg(q))
        assert mul(sel,sub(V,S))==dot(U,B[:4])
        # independently construct the exact CNF from presence bits
        l=[sub(O,X[-1]),X[-1]]*2
        S0=prod(sub(O,prod(l[i] for i in range(k,k+2) if a[i])) for k in (0,2))
        assert S==S0
        rem,H=reduce_lift(S)
        sat=any(spec(S,(0,0,0,0,b)) for b in (0,1))
        assert bool(rem)==sat
        if not sat:
            unsat+=1
            assert all(not h for h in H[:4])
            C=U+[mul(sel,H[-1])]
            assert mul(sel,V)==dot(C,B)
            assert spec(mul(sel,V),a)==mul(spec(C[-1],a),B[-1])==S
            for other in product((0,1),repeat=4):
                if other!=a:assert not spec(mul(sel,V),other)
        else:
            assert any(spec(mul(sel,V),a+(b,)) for b in (0,1))
        cases+=1
    return cases,unsat

if __name__=='__main__':
    if not __debug__:raise RuntimeError('assertions required')
    for p in (2,3,5):
        c,u=check(p);print(f'F{p}: {c} exact codes, {u} singleton UNSAT lifts')
