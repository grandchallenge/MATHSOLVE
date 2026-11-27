#!/usr/bin/env python3
"""Independent finite gluing controls; not a lower-bound experiment."""
from itertools import product

def models(clauses, variables):
    return [a for bits in product((False, True), repeat=len(variables))
            for a in (dict(zip(variables, bits)),) if all(any(a[abs(lit)] == (lit > 0) for lit in clause) for clause in clauses)]

def glue(left, right):
    return [a | b for a in left for b in right
            if all(a[i] == b[i] for i in a.keys() & b.keys())]

def freeze(a):
    return tuple(sorted(a.items()))

def check():
    lclauses = [(1,),(-1,),(2,),(-2,), (1,2),(1,-2),(-1,2),(-1,-2)]
    rclauses = [(2,),(-2,),(3,),(-3,), (2,3),(2,-3),(-2,3),(-2,-3)]
    count=0
    for lm,rm in product(range(256),repeat=2):
        L=[c for i,c in enumerate(lclauses) if lm>>i&1]
        R=[c for i,c in enumerate(rclauses) if rm>>i&1]
        truth={freeze(a) for a in models(L+R,[1,2,3])}
        left,right=models(L,[1,2]),models(R,[2,3])
        assert {freeze(a) for a in glue(left,right)} == truth
        for bit in (False,True):
            ls=[a for a in left if a[2]==bit]
            rs=[a for a in right if a[2]==bit]
            assert {freeze(a|b) for a,b in product(ls,rs)} == {
                a for a in truth if dict(a)[2]==bit}
            count+=1
    eq12=[(-1,2),(1,-2)]
    eq23=[(-2,3),(2,-3)]
    neq13=[(1,3),(-1,-3)]
    blocks=[eq12,eq23,neq13]
    assert not models(eq12+eq23+neq13,[1,2,3])
    assert all(models(blocks[i]+blocks[j],[1,2,3]) for i,j in ((0,1),(1,2),(0,2)))
    print(f"WP47 finite gluing controls: {count} conditioned formula pairs; pairwise consistency counterexample PASS")
if __name__=="__main__":
    check()
