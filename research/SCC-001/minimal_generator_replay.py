#!/usr/bin/env python3
"""SCC minimal-generator barrier: exact truth-table and tensor regressions."""
from itertools import product
from math import comb
import json

def span(xs):
    b = {}
    for x in xs:
        while x:
            p = x.bit_length()-1
            if p in b: x ^= b[p]
            else:
                b[p] = x
                break
    return b

def rem(b,x):
    for p,y in sorted(b.items(),reverse=True):
        if (x>>p)&1: x ^= y
    return x

def kernel_on(inputs, transform):
    piv, out = {}, []
    for a in inputs:
        x,w = transform(a),a
        while x:
            p=x.bit_length()-1
            if p not in piv:
                piv[p]=(x,w)
                break
            y,z=piv[p];x^=y;w^=z
        if not x: out.append(w)
    return list(span(out).values())

def filt(v,n):
    fs=[span([(1<<(1<<n))-1])]
    for _ in range(n):
        old=list(fs[-1].values())
        fs.append(span(old+[x&y for x in old for y in v]))
    return fs

def check(m):
    n=2*m+2; one=(1<<(1<<n))-1
    coords=[sum(1<<j for j in range(1<<n) if j>>i&1) for i in range(n)]
    g=coords[0]&coords[1];f=g
    for i in range(m):f &= one^(coords[2+2*i]&coords[3+2*i])
    v=[one]+coords;vp=v+[g]
    F,P=filt(v,n),filt(vp,n)
    J=[];JP=[];new=[];restricted_old=[];restricted_new=[]
    for r,(u,w) in enumerate(zip(F,P)):
        # homogeneous degree-r ideals, identifying a*z^r with its truth table.
        j=kernel_on(u.values(),lambda a:rem(u,f&a))
        jp=kernel_on(w.values(),lambda a:rem(w,f&a))
        J.append(j);JP.append(jp)
        # J'_r /(J_r + R'_1 J'_(r-1)) is the generator space of M.
        inherited=j+([x&y for x in vp for y in JP[r-1]] if r else [])
        assert all(rem(span(jp),x)==0 for x in inherited)
        new.append(len(jp)-len(span(inherited)))
        # Restrict to target support: represented by zero-extended truth tables.
        old_rank=len(span(f&a for a in j));new_rank=len(span(f&a for a in jp))
        restricted_old.append(old_rank);restricted_new.append(new_rank)
        expected=lambda shift:sum(comb(m,k)*2**k for k in range(m+1) if k<=r and 2*m-k+shift<=r)
        assert old_rank==expected(2) and new_rank==expected(1),(m,r,old_rank,new_rank)
    assert new==[0,1]+[0]*(m-1)+[2**m]+[0]*(n-m-1), (m,new)
    assert restricted_new[:m+1]==[0]*(m+1)
    assert restricted_new[m+1]==2**m and restricted_old[m+1]==0
    # Verify exact witness classes in the actual homogeneous quotient.
    den=span(J[m+1]+[x&y for x in vp for y in JP[m]])
    witnesses=[]
    for choice in product((0,1),repeat=m):
        a=one
        for i,c in enumerate(choice):a &= one^coords[2+2*i+c]
        assert rem(P[m+1],a)==0 and rem(P[m+1],f&a)==0
        witnesses.append(a)
    assert len(span(list(den.values())+witnesses))-len(den)==2**m
    return dict(m=m,n=n,grade=m+1,restricted_birth=2**m,actual_minimal_generators_at_grade=new[m+1],all_generator_grades=new,old_support_ranks=restricted_old,new_support_ranks=restricted_new)

if __name__=="__main__":
    print(json.dumps({"status":"PASS","fixtures":[check(m) for m in range(1,4)]},indent=2))
