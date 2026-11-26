#!/usr/bin/env python3
"""Exact F2 ordinary-polynomial identities; never reduce x^2=x implicitly."""
from itertools import product
from random import Random

N=3
Z=frozenset()
O=frozenset({(0,)*N})
X=[frozenset({tuple(int(i==j) for i in range(N))}) for j in range(N)]
def mul(a,b):
    p=set()
    for u in a:
        for v in b:
            w=tuple(x+y for x,y in zip(u,v))
            p.symmetric_difference_update({w})
    return frozenset(p)
def prod(ps):
    r=O
    for p in ps:r=mul(r,p)
    return r
def dot(a,b):
    r=Z
    for u,v in zip(a,b,strict=True):r^=mul(u,v)
    return r
def ev(p,a):return sum(all(not e or x for e,x in zip(t,a)) for t in p)%2
B=[mul(x,x)^x for x in X]
def clause(lits):
    return prod(X[abs(l)-1] if l>0 else O^X[abs(l)-1] for l in lits)
def reduce_lift(p):
    r=Z; h=[Z]*N
    for t in p:
        u=list(t)
        for j,e in enumerate(u):
            if e<2:continue
            for k in range(e-1):
                v=u.copy();v[j]=k
                h[j]^=frozenset({tuple(v)})
            u[j]=1
        r^=frozenset({tuple(u)})
    assert p==r^dot(h,B)
    return r,h
def defect(lits):
    p=O; h=[Z]*N
    for l in lits:
        j=abs(l)-1; q=X[j] if l>0 else O^X[j]
        h=[mul(mul(q,q),a)^(p if k==j else Z) for k,a in enumerate(h)]
        p=mul(p,q)
    assert dot(h,B)==mul(p,p)^p
    return p,h
def lifts(cs,lits):
    S=prod(O^c for c in cs)
    W=[]
    for i,ls in enumerate(lits):
        c,e=defect(ls);assert c==cs[i]
        other=prod(O^d for k,d in enumerate(cs) if k!=i)
        w=[mul(a,other) for a in e]; assert dot(w,B)==mul(S,c)
        W.append(w)
    a=[prod(O^c for c in cs[:i]) for i in range(len(cs))]
    assert dot(a,cs)==O^S
    return S,W,a
def linearize(node,fs):
    k=len(fs); zero=[Z]*k
    op,*v=node
    if op=='const':return v[0],v[0],zero
    if op=='y':
        i=v[0]; d=zero.copy();d[i]=O;return Z,fs[i],d
    a,A,da=linearize(v[0],fs);b,Bv,db=linearize(v[1],fs)
    if op=='+': return a^b,A^Bv,[x^y for x,y in zip(da,db)]
    return mul(a,b),mul(A,Bv),[mul(A,y)^mul(b,x) for x,y in zip(da,db)]
def check():
    if not __debug__:raise RuntimeError("assertions required")
    lits=[(),(1,),(-1,),(2,),(-2,),(1,1),(1,-1),(2,3),(-2,-3)]
    cnt=unsat=perturbed=0
    for m in range(4):
        for ls in product(lits,repeat=m):
            cs=[clause(c) for c in ls];S,W,a=lifts(cs,ls)
            r,h=reduce_lift(S)
            sat=any(ev(S,t) for t in product((0,1),repeat=N))
            assert sat==bool(r)
            assert all(ev(S,t)==ev(r,t) for t in product((0,1),repeat=N))
            assert int((1,)*N in r)==sum(ev(S,t) for t in product((0,1),repeat=N))%2
            cnt+=1
            if sat:continue
            unsat+=1
            fs=cs+B; co=a+h
            assert dot(co,fs)==O
            for i,j in [(0,len(fs)-1),(len(fs)-2,len(fs)-1)]:
                if i==j:continue
                cc=co.copy();cc[i]^=fs[j];cc[j]^=fs[i]
                assert dot(cc,fs)==O
                U,V=cc[:m],cc[m:]
                H=[mul(S,V[k])^dot(U,[w[k] for w in W]) for k in range(N)]
                assert dot(H,B)==S
                terms=[('*',('const',u),('y',k)) for k,u in enumerate(cc)]
                node=('const',Z)
                for term in terms:node=('+',node,term)
                node=('+',node,('*',('y',i),('+',('y',j),('const',fs[j]))))
                g0,g1,d=linearize(node,fs)
                assert g0==Z and g1==O and dot(d,fs)==O
                H=[mul(S,d[m+k])^dot(d[:m],[w[k] for w in W]) for k in range(N)]
                assert dot(H,B)==S
                perturbed+=1
    rng=Random(42026)
    fs=X+B
    leaves=[('const',p) for p in X+[Z,O]]+[('y',i) for i in range(len(fs))]
    for _ in range(1000):
        nodes=leaves.copy()
        for j in range(8):
            nodes.append((rng.choice(['+','*']),rng.choice(nodes),rng.choice(nodes)))
        a,A,d=linearize(nodes[-1],fs);assert a^A==dot(d,fs)
    print(f"CNFs={cnt}; UNSAT={unsat}; perturbed general/linear reverse lifts={perturbed}; arbitrary gate-vector identities=1000")
if __name__=='__main__':check()
