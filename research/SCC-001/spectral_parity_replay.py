#!/usr/bin/env python3
"""Exact regression for common spectral branches and parity geometry."""
from random import Random
from collections import defaultdict
import json

def parity(x): return x.bit_count()&1
def walsh(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h];a[j]=u+v;a[j+h]=u-v
        h*=2
    return a
def span(xs):
    b={}
    for x in xs:
        while x:
            p=x.bit_length()-1
            if p in b:x^=b[p]
            else:b[p]=x;break
    return list(b.values())
def affine(S):
    if not S:return True
    a=next(iter(S));return len(S)==1<<len(span(x^a for x in S))
def v2(a):return (abs(a)&-abs(a)).bit_length()-1
def check_branch(vals):
    S={a for a,z in enumerate(vals) if z}
    if not S:return
    assert affine(S)
    amp=abs(vals[next(iter(S))]); assert amp&(amp-1)==0
    assert all(abs(vals[a])==amp for a in S)
    a=next(iter(S));basis=span(x^a for x in S)
    # Sign on the affine support has degree <= 2.
    coords=[a]
    for b in basis:coords += [x^b for x in coords]
    bits=[int(vals[x]<0) for x in coords]
    for i in range(len(basis)):
        for j in range(len(bits)):
            if j>>i&1:bits[j]^=bits[j^(1<<i)]
    assert all(not x or j.bit_count()<=2 for j,x in enumerate(bits))

def sample(rng,t,r):
    # Gate offsets are masks on earlier outputs, plus constants.
    alpha=[(rng.randrange(1<<j),rng.randrange(2)) for j in range(t)]
    beta=[(rng.randrange(1<<j),rng.randrange(2)) for j in range(t)]
    c=rng.randrange(1<<t)
    cols=[]
    while len(cols)<r:
        x=rng.randrange(1<<(2*t))
        if len(span(cols+[x]))>len(cols):cols.append(x)
    def H(x):
        z=0
        for j in range(t):
            p=(x>>(2*j)&1)^parity(alpha[j][0]&z)^alpha[j][1]
            q=(x>>(2*j+1)&1)^parity(beta[j][0]&z)^beta[j][1]
            z|=(p&q)<<j
        return parity(c&z)
    branches=defaultdict(lambda:[0]*(1<<r));lift=[0]*(1<<(2*t))
    for w in range(1<<(2*t)):
        mask=c;sign=0;active=0
        for j in reversed(range(t)):
            p=w>>(2*j)&1;q=w>>(2*j+1)&1
            if not(mask>>j&1):
                if p or q:break
            else:
                active|=1<<j
                sign^=(p&q)^ (p&alpha[j][1]) ^ (q&beta[j][1])
                if p:mask^=alpha[j][0]
                if q:mask^=beta[j][0]
        else:
            z=(-1 if sign else 1)<<(t-active.bit_count())
            lift[w]=z
            a=sum(parity(w&v)<<i for i,v in enumerate(cols))
            branches[active][a]+=z
    assert [v//(1<<t) for v in walsh([(-1)**H(x) for x in range(1<<(2*t))])]==lift
    rows=[0]
    for col in cols:rows += [x^col for x in rows]
    target=walsh([(-1)**H(x) for x in rows])
    Z=[sum(b[a] for b in branches.values()) for a in range(1<<r)]
    assert all((a<<r)==(b<<t) for a,b in zip(Z,target))
    for b in branches.values():check_branch(b)
    s=min(v2(x) for x in Z if x); assert s<=t
    odd=[(x>>s)&1 for x in Z]
    if s<=1:
        relevant=[b for b in branches.values() if any(b) and min(v2(x) for x in b if x)==s]
        assert all(all(not x or v2(x)>=s for x in b) for b in branches.values())
        assert len(relevant)<= (1 if s==0 else t+1)
        assert odd==[sum(bool(b[a]) for b in relevant)&1 for a in range(1<<r)]
        if s==0:assert affine({a for a,v in enumerate(odd) if v})
    # General bit extraction via GF2 product, evaluated pointwise.
    for a,z in enumerate(Z):
        poly=1; cap=(1<<s)
        for b in branches.values():
            residue=b[a] % (1<<(s+1))
            for j in range(s+1):
                if residue>>j&1:poly=(poly^(poly<<(1<<j)))&((1<<(cap+1))-1)
        assert ((poly>>cap)&1)==odd[a]
    return len(branches),len(Z),s

def fixture(m):
    # y low two bits are the four singleton fibres; the remaining fibres
    # are indexed by the first nonzero bit of y outside those two.
    def pi(y):
        if y<4:return [0,1,2,4][y]
        j=next(i for i in range(2,m) if y>>i&1)
        return 3 if j==2 else 1<<j
    fibres=defaultdict(set)
    for y in range(1<<m):fibres[pi(y)].add(y)
    assert len(span(fibres))==m and all(affine(S) for S in fibres.values())
    # Full exact integer Walsh numerator 2^m W(u,v).
    Z=[sum((-1)**parity(v&y) for y in fibres[u]) for u in range(1<<m) for v in range(1<<m)]
    assert all(not z or abs(z)&(abs(z)-1)==0 for z in Z)
    odd={i for i,z in enumerate(Z) if z&1}
    assert len(odd)==4*(1<<m) and not affine(odd)
    assert len(span(i^next(iter(odd)) for i,z in enumerate(Z) if z))==2*m
    return dict(m=m,dimension=2*m,granularity=m,signed_digit_max=1,odd_count=len(odd),affine=False,new_lower=m+1)

if __name__=="__main__":
    rng=Random(20261128); stats=defaultdict(int)
    for t in range(1,6):
        for i in range(20):
            r=rng.randrange(1,2*t+1);b,a,s=sample(rng,t,r)
            stats["circuits"]+=1;stats["branches"]+=b;stats["frequencies"]+=a
            stats["slack_"+str(s)]+=1
    print(json.dumps(dict(status="PASS",seed=20261128,checks=dict(stats),fixtures=[fixture(m) for m in range(3,9)]),indent=2))
