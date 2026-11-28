"""Exact finite two-constraint exterior spanning and safe reachability replay."""
from itertools import combinations
from random import Random

def rank(xs):
    p={}
    for x in xs:
        while x:
            i=x.bit_length()-1
            if i not in p:p[i]=x;break
            x^=p[i]
    return len(p)

def span(xs):
    s={0}
    for x in xs:s|={a^x for a in s}
    return s

def dot(x,y):return (x&y).bit_count()&1

def wedge(u,v,pairs):
    return sum((((u>>i)&1)*((v>>j)&1)^((u>>j)&1)*((v>>i)&1))<<k for k,(i,j) in enumerate(pairs))

def ext_test():
    rng=Random(281126); checks=0; counter=None
    for d in range(2,7):
        pairs=list(combinations(range(d),2));N=len(pairs)
        D={wedge(u,v,pairs) for u in range(1<<d) for v in range(1<<d)}
        masks=range(1<<N)
        tests=((a,b) for a in masks for b in masks) if d<=4 else ((rng.randrange(1<<N),rng.randrange(1<<N)) for _ in range(400))
        for a,b in tests:
            assert rank(q for q in D if not dot(q,a) and not dot(q,b))==N-rank([a,b]);checks+=1
        if d==4:
            # Find a codimension-three allowed exterior space with only a 1D safe span.
            for a,b,c in combinations(range(1,1<<N),3):
                if rank([a,b,c])!=3:continue
                K={q for q in masks if not any(dot(q,z) for z in (a,b,c))}
                if rank(K&D)==1:counter=(a,b,c,sorted(K),sorted(K&D));break
    assert counter is not None
    print('PASS two-constraint exterior checks',checks,'three-constraint counterexample',counter)

def safe_replay():
    rng=Random(281127);cases=steps=pair_checks=0
    for n in (3,4):
        N=1<<n;M=(1<<N)-1;V0=span([M]+[sum(((p>>j)&1)<<p for p in range(N)) for j in range(n)])
        A=[l for l in range(1,M+1) if all(not dot(l,v) for v in V0)]
        P=list(combinations(A,2)) if n==3 else [tuple(rng.sample(A,2)) for _ in range(16)]
        for a,b in P:
            H={v for v in range(M+1) if not dot(v,a) and not dot(v,b)}
            V=set(V0)
            while V!=H:
                g=None
                vals=sorted(V)
                for _ in range(10000):
                    u,v=rng.choice(vals),rng.choice(vals);w=u&v
                    if w in H and w not in V:g=w;break
                if g is None:g=next((u&v for u in vals for v in vals if u&v in H and u&v not in V),None)
                assert g is not None
                V|={v^g for v in V};steps+=1
            assert len(V)==1<<(N-2);cases+=1
            if n==3:
                assert {l for l in A if all(not dot(l,v) for v in V)}=={a,b,a^b}
                for f in range(M+1):
                    if dot(a,f) and dot(b,f):
                        assert f not in V
                        assert {l for l in A if dot(l,f) and all(not dot(l,v) for v in V)}=={a,b}
                        pair_checks+=1
    print('PASS safe codimension-two histories',cases,'nonredundant gates',steps,'exact surviving target pairs',pair_checks)

if __name__=='__main__':
    if not __debug__:raise RuntimeError('assertions required')
    ext_test();safe_replay()
