"""Exact finite regression for shared interaction advice; no proof authority."""
from functools import lru_cache
from random import Random

def cross(h,a,b):
    return tuple(h[x*b+y]^h[x*b]^h[y]^h[0] for x in range(a) for y in range(b))
def add(u,v): return tuple(x^y for x,y in zip(u,v))
def mul(u,v): return tuple(x&y for x,y in zip(u,v))
def affine(a,b):
    return [tuple(1 for _ in range(a*b))]+[tuple((x>>i)&1 for x in range(a) for y in range(b)) for i in range(a.bit_length()-1)]+[tuple((y>>i)&1 for x in range(a) for y in range(b)) for i in range(b.bit_length()-1)]
def combo(V,k):
    return tuple(sum(h[i] for j,h in enumerate(V) if k>>j&1)%2 for i in range(len(V[0])))
def cost(V,f,a,b):
    advice=[cross(h,a,b) for h in V]; target=cross(f,a,b); fibers={}
    for i in range(a*b):
        key=tuple(h[i] for h in advice); fibers[key]=fibers.get(key,0)|(1<<i)
    rows=[sum(1<<(x*b+y) for y in range(b)) for x in range(a)]
    cols=[sum(1<<(x*b+y) for x in range(a)) for y in range(b)]
    ones=sum(v<<i for i,v in enumerate(target))
    @lru_cache(None)
    def dp(P):
        if all(not(P&m&ones) or not(P&m&~ones) for m in rows+cols): return 0
        best=a.bit_length()+b.bit_length()
        for blocks in (rows,cols):
            active=[m&P for m in blocks if m&P]
            for z in range(1,1<<(len(active)-1)):
                Q=0
                for j,m in enumerate(active):
                    if z>>j&1: Q|=m
                best=min(best,1+max(dp(Q),dp(P^Q)))
        return best
    return max(map(dp,fibers.values()))
def check(V,u,v,targets,a,b):
    g=mul(u,v); c_u,c_v,c_g=map(lambda h:cross(h,a,b),(u,v,g)); W=V+[g]
    for x in range(a):
        for y in range(b):
            i=x*b+y
            U=c_u[i]^u[x*b]^u[y]^u[0]; Q=c_v[i]^v[x*b]^v[y]^v[0]
            assert c_g[i]==((U&Q)^(u[x*b]&v[x*b])^(u[y]&v[y])^(u[0]&v[0]))
    assert cost(W,g,a,b)==0
    for f in targets:
        old,new=cost(V,f,a,b),cost(W,f,a,b)
        assert 0<=old-new<=3 and old<=min(a.bit_length(),b.bit_length())
    return W,len(targets)
if __name__=='__main__':
    V=affine(2,2); forms=[combo(V,k) for k in range(1<<len(V))]; targets=[tuple(k>>i&1 for i in range(4)) for k in range(16)]; count=0; gates=0
    for u in forms:
        for v in forms:
            _,c=check(V,u,v,targets,2,2); count+=c; gates+=1
    rng=Random(90210)
    for _ in range(64):
        V=affine(4,4)
        for j in range(4):
            u,v=[combo(V,rng.randrange(1<<len(V))) for _ in range(2)]; targets=[tuple(rng.randrange(2) for _ in range(16)) for _ in range(4)]
            V,c=check(V,u,v,targets,4,4); count+=c; gates+=1
    for _ in range(8):
        V=affine(2,2); V+=[mul(combo(V,rng.randrange(8)),combo(V,rng.randrange(8)))]; f=tuple(rng.randrange(2) for _ in range(4)); old=cost(V,f,2,2)
        for a,b in [(4,2),(2,4)]:
            lift=lambda h:tuple(h[(x%2)*2+(y%2)] for x in range(a) for y in range(b))
            assert cost([lift(h) for h in V]+affine(a,b),lift(f),a,b)==old
    print(f'PASS: {gates} gate reconstructions; {count} exact target protocol comparisons; {gates} completion checks; 16 spectator comparisons; seed 90210')
