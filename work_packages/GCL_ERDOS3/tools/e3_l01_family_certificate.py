#!/usr/bin/env python3
"""Exact E3-L01 family-level certificate for the (m,N)=(4,7) obstruction.

Pure Python. No solver. Enumerates the 972,000 locally admissible (5,4,4,4)
profiles and records which D01 coarse/carry cross-fibre template families
occur as contained 4-APs.
"""

from itertools import combinations, product

N=7

def aps(n):
    return [(a,a+d,a+2*d,a+3*d)
            for d in range(1,(n-1)//3+1)
            for a in range(n-3*d)]

def apfree(S,n):
    s=set(S)
    return all(not all(v in s for v in e) for e in aps(n))

P4=[tuple(c) for c in combinations(range(N),4) if apfree(c,N)]
P5=[tuple(c) for c in combinations(range(N),5) if apfree(c,N)]
assert len(P4)==30
assert len(P5)==9

# D01 family key = (starting block i, q=floor(d/N), carry word).
cross=[]
families=[]
for e in aps(4*N):
    if len({x//N for x in e})==1:
        continue
    a=e[0]; d=e[1]-e[0]
    i=a//N; u=a%N; q=d//N; v=d%N
    carry=tuple((u+t*v)//N for t in range(4))
    fam=(i,q,carry)
    if fam not in families:
        families.append(fam)
    cross.append((e,fam))

assert len(cross)==97
assert len(families)==17
F={fam:j for j,fam in enumerate(families)}

def support(Bs):
    A={i*N+u for i,B in enumerate(Bs) for u in B}
    out=set()
    for e,fam in cross:
        if all(x in A for x in e):
            out.add(F[fam])
    return frozenset(out)

supports=[]
witness={}
count=0
for pos5 in range(4):
    pools=[P5 if i==pos5 else P4 for i in range(4)]
    for Bs in product(*pools):
        count+=1
        s=support(Bs)
        assert s, "hypothetical (5,4,4,4) global AP-free gluing found"
        supports.append(s)
        witness.setdefault(s,Bs)
assert count==972000

# Five template families are individually mandatory: each occurs as the
# sole support of at least one locally admissible profile.
mandatory={2,6,9,10,16}
for j in mandatory:
    assert frozenset({j}) in witness

# Remove profiles already hit by the mandatory families.
residual={s for s in supports if s.isdisjoint(mandatory)}
assert len(residual)==596
assert sum(1 for s in supports if s.isdisjoint(mandatory))==1380

# Nine residual support clauses. Each is an actually occurring profile support.
clauses=[
    frozenset({3,4}),
    frozenset({4,5}),
    frozenset({1,7,8}),
    frozenset({7,11}),
    frozenset({1,11,12,13}),
    frozenset({1,14}),
    frozenset({3,5,13,14}),
    frozenset({0,3,5,15}),
    frozenset({13,14,15}),
]
for c in clauses:
    assert c in witness

# Human-checkable lower bound:
#   if F4 is chosen, C6 forces F1 or F14; either choice leaves at least
#   four other clauses requiring >2 remaining selections.
#   if F4 is not chosen, C1 and C2 force F3 and F5; C6 again forces F1
#   or F14, and no single fourth family can hit the remaining clauses.
# We also replay the finite statement directly: no <=4-set hits all 9 clauses.
remaining=set(range(17))-mandatory
for k in range(5):
    for K in combinations(sorted(remaining),k):
        K=set(K)
        assert any(K.isdisjoint(c) for c in clauses)

# Five additional families suffice for every residual profile.
extra={1,3,4,7,15}
assert all(not extra.isdisjoint(s) for s in residual)
certificate=mandatory|extra
assert len(certificate)==10
assert all(not certificate.isdisjoint(s) for s in supports)

# Alternative symmetric 10-family certificate.
alt=mandatory|{1,4,5,7,15}
assert len(alt)==10
assert all(not alt.isdisjoint(s) for s in supports)

def fmtfam(j):
    i,q,c=families[j]
    return f"F{j}=({i},{q},{''.join(map(str,c))})"

print("profiles",count)
print("cross_APs",len(cross))
print("cross_families",len(families))
print("mandatory",*[fmtfam(j) for j in sorted(mandatory)])
print("residual_profiles",sum(1 for s in supports if s.isdisjoint(mandatory)))
print("residual_supports",len(residual))
print("lower_bound_clauses")
for c in clauses:
    print(" ",[fmtfam(j) for j in sorted(c)])
print("minimum_family_certificate_size",10)
print("certificate",*[fmtfam(j) for j in sorted(certificate)])
print("certificate_AP_count",sum(1 for _,fam in cross if F[fam] in certificate))
print("alternative",*[fmtfam(j) for j in sorted(alt)])
print("singleton_witnesses")
for j in sorted(mandatory):
    print(" ",fmtfam(j),witness[frozenset({j})])
print("clause_witnesses")
for c in clauses:
    print(" ",[fmtfam(j) for j in sorted(c)],witness[c])
