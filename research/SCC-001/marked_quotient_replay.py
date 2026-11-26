#!/usr/bin/env python3
"""Exact rank modulo available affine features, independent of marked BFS."""
from collections import deque,Counter
from functools import lru_cache
from marked_graph_replay import initial,space,exact

def reducer(V):
    piv={}
    for w in V:
        v=w
        for i,p in sorted(piv.items(),reverse=True):
            if (v>>i)&1:v^=p
        if v:piv[v.bit_length()-1]=v
    ps=tuple(sorted(piv.items(),reverse=True))
    def red(v):
        for i,p in ps:
            if (v>>i)&1:v^=p
        return v
    return red

@lru_cache(None)
def quotient_dist(n,V):
    M=(1<<(1<<n))-1
    atoms={M}
    for v in V:atoms|={v&a for a in atoms}
    red=reducer(V)
    generators={red(a) for a in atoms}-{0}
    d={0:0};q=deque([0])
    while q:
        a=q.popleft()
        for g in generators:
            b=a^g
            if b not in d:d[b]=d[a]+1;q.append(b)
    assert len(d)*len(V)==1<<(1<<n)
    return d,red,len(atoms)

def rank(n,V,f):
    d,r,_=quotient_dist(n,V)
    return 1+d[r(f)]

def main():
    if not __debug__:raise RuntimeError('assertions required')
    # Compare quotient ranks against the independent marker-state BFS for every f.
    eq=0
    for n in (1,2,3):
        V=initial(n)
        for f in range(1<<(1<<n)):
            assert rank(n,V,f)==exact(n,V)[f];eq+=1
        if n>=2:
            a,b=[sum(((x>>i)&1)<<x for x in range(1<<n)) for i in range(2)]
            W=space([*V,a&b])
            for f in range(1<<(1<<n)):
                assert rank(n,W,f)==exact(n,W)[f];eq+=1
    n=4
    a,b,c,d=[sum(((x>>i)&1)<<x for x in range(1<<n)) for i in range(n)]
    V=initial(n)
    histories=[(a,b),(c,d),(a&b,c),(a^c,b^d),((a&b)^(c&d),a^d)]
    # Test full target cube across several distinct reachable transitions.
    states=[V]; checks=0; maxdrop=0
    hist=Counter()
    for i,(u,v) in enumerate(histories):
        assert u in V and v in V
        W=space([*V,u&v])
        x,r,A=quotient_dist(n,V); y,s,B=quotient_dist(n,W)
        for f in range(1<<(1<<n)):
            p=1+x[r(f)];q=1+y[s(f)]
            assert q<=p<=2*q
            assert (q==1)==(f in W)
            hist[p-q]+=1;maxdrop=max(maxdrop,p-q);checks+=1
        print('four-bit step',i+1,'atoms',A,B,'max rho',max(x.values())+1,max(y.values())+1)
        V=W;states.append(V)
    # Sharp raw counterexample: f=1[Hamming weight <=1], g=ab.
    V0=initial(4); W=space([*V0,a&b]); M=65535
    f=sum(1<<i for i in range(16) if i.bit_count()<=1)
    assert f==0x117 and rank(4,V0,f)==4 and rank(4,W,f)==2
    correction=M^a^b^(a&b)
    atom=(M^(a&b))&(M^c^d)&(a^b^c)
    assert correction in W and f==correction^atom
    # Independent lower check: enumerate the initial atom set and test every pair
    # modulo every affine correction, without quotient shortest-path distances.
    A={M}
    for v in V0:A|={v&w for w in A}
    pairs={u^v for u in A for v in A}
    assert all(f^v not in pairs for v in V0)
    assert f==(1^6^0x110) and {1,6,0x110}<=A
    # Exhaustively check the one-hot MOD3 circuit, counting actual nonlinear updates.
    total=0
    for n in range(1,13):
        for x in range(1<<n):
            r=[1,0,0]
            for i in range(n):
                bit=(x>>i)&1
                r=[r[j]^(bit&(r[j]^r[(j-1)%3])) for j in range(3)]
                assert sum(r)==1
            assert 1^r[0]==int(x.bit_count()%3!=0)
            total+=1
    print('sharp raw rank 4 -> 2 witness; independent pair exclusion; MOD3 cases',total)
    print('independent marker/quotient agreements',eq,'four-bit comparisons',checks,
          'raw drop histogram',dict(sorted(hist.items())),'max raw drop',maxdrop)
if __name__=='__main__':main()
