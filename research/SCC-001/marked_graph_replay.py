#!/usr/bin/env python3
"""Exact minimum XOR-of-affine-atom rank on tiny reachable Boolean states."""
from collections import deque
from itertools import product
from functools import lru_cache

def space(basis):
    s={0}
    for v in basis:s|={x^v for x in s}
    return tuple(sorted(s))

def initial(n):
    M=(1<<(1<<n))-1
    return space([M]+[sum(((x>>j)&1)<<x for x in range(1<<n)) for j in range(n)])

def graph(f,n):
    k=1<<n; M=(1<<k)-1
    return (M^f)|(f<<k)

@lru_cache(None)
def atom_set(n,V):
    k=1<<n; M=(1<<k)-1
    w=space([v|(v<<k) for v in V]+[M<<k])
    # closure under AND: independent of the transport decomposition
    a={M|(M<<k)}
    for v in w:a|={p&v for p in a}
    assert 0 in a
    return frozenset(a)

@lru_cache(None)
def exact(n,V):
    atoms=atom_set(n,V)-{0}
    N=1<<(2*(1<<n))
    d=bytearray([255])*N;d[0]=0
    q=deque([0])
    targets={graph(f,n) for f in range(1<<(1<<n))}
    pending=targets.copy()
    # BFS exhausts all shorter representations before the first discovery.
    while pending:
        h=q.popleft(); r=d[h]+1
        for a in atoms:
            t=h^a
            if d[t]==255:
                d[t]=r;q.append(t);pending.discard(t)
    return tuple(d[graph(f,n)] for f in range(1<<(1<<n)))

def transport(n,V,u,v):
    W=space([*V,u&v])
    old=atom_set(n,V);new=atom_set(n,W)
    # Independently check that every new atom has an old decomposition of length <=2.
    sums=old|{a^b for a in old for b in old}
    assert new<=sums
    r,s=exact(n,V),exact(n,W)
    drop=0
    for f,(a,b) in enumerate(zip(r,s,strict=True)):
        assert (a==1)==(f in V)
        assert (b==1)==(f in W)
        assert 1<=b<=a<=2*b and a<=1<<n
        assert 0<=(a-1).bit_length()-(b-1).bit_length()<=1
        drop=max(drop,a-b)
    return W,len(new),len(r),drop

def main():
    if not __debug__:raise RuntimeError('assertions required')
    V=initial(2); x,y=[sum(((t>>j)&1)<<t for t in range(4)) for j in range(2)]
    W,*_=transport(2,V,x,y)
    assert exact(2,V)[x&y]==2 and exact(2,W)[x&y]==1
    stats=[0,0,0,0]
    def step(n,V,u,v):
        W,a,r,d=transport(n,V,u,v)
        stats[0]+=1;stats[1]+=a;stats[2]+=r;stats[3]=max(stats[3],d)
        return W
    for u,v in product(V,repeat=2):step(2,V,u,v)
    # n=3: distinct representative reachable states, arbitrary nonlinear reuse.
    V3=initial(3)
    a,b,c=[sum(((t>>j)&1)<<t for t in range(8)) for j in range(3)]
    W3=step(3,V3,a,b)
    Q3=step(3,W3,a&b,c)
    R3=step(3,W3,a^c,b^c)
    step(3,Q3,(a&b)^c,b)
    step(3,R3,(a^c)&(b^c),a)
    # Affine-coordinate relabelings on every two-bit target.
    r=exact(2,V)
    for perm in [(0,2,1,3),(1,0,3,2),(0,1,3,2)]:
        for f in range(16):
            h=sum(((f>>p)&1)<<i for i,p in enumerate(perm))
            assert r[h]==r[f]
    # Spectator invariance from both affine and nonlinear two-bit states.
    for base in (V,W):
        extended=space([v|(v<<4) for v in base]+[0xf0])
        for f in range(16):
            assert exact(2,base)[f]==exact(3,extended)[f|(f<<4)]
    print('transitions=%d; atom transport checks=%d; target comparisons=%d; max raw drop=%d'%tuple(stats))
    print('sharp ratio fixture, 48 affine relabelings, 32 spectator checks: PASS')
    print('initial max graph ranks:',{n:max(exact(n,initial(n))) for n in (1,2,3)})
if __name__=='__main__':main()
