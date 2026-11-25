#!/usr/bin/env python3
"""Finite exact negative controls; not an asymptotic width proof or Lean replay."""
from itertools import product

def check():
    generic_cases=0
    # Every pair of disjoint truth tables on two bits, every planted vector.
    for P,Q in product(range(16),repeat=2):
        if P & Q:
            continue
        for p in range(4):
            models=[(s,a) for s in range(2) for a in range(4)
                    if (s or (P>>a)&1) and (s or (Q>>a)&1)
                    and (not s or a==p)]
            if models!=[(1,p)]:
                raise AssertionError((P,Q,p,models))
            generic_cases+=1
    if generic_cases!=324:
        raise AssertionError(generic_cases)
    graph_cases=[]
    for n in (2,3,4):
        masks=[sum(1<<(n*i+j) for i in range(n) for j in range(n)
                   if i!=j and v in (i,j)) for v in range(n)]
        models=[]
        base_models=0
        for a in range(1<<(n*n)):
            base=all(((a&mask).bit_count()&1)==(v==0)
                     for v,mask in enumerate(masks))
            base_models+=int(base)
            for s in (0,1):
                if all(s or ((a&mask).bit_count()&1)==(v==0)
                       for v,mask in enumerate(masks)) and (not s or a==0):
                    models.append((s,a))
        if base_models or models!=[(1,0)]:
            raise AssertionError((n,base_models,models))
        graph_cases.append((n,1<<(n*n+1),len(models)))
    return generic_cases,graph_cases

if __name__=='__main__':
    count,graphs=check()
    print('WP39 exact finite checks:',count,'arbitrary truth-table/plant cases')
    for n,enumerated,models in graphs:
        print('N=',n,'assignments=',enumerated,'models=',models)
