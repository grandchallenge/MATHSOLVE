"""Exact reachable-state nonminimum witness and affine closure membership test."""
from collections import defaultdict
from marked_graph_replay import initial, space, atom_set, graph
from marked_quotient_replay import rank, quotient_dist

def xor(xs):
    a=0
    for x in xs:a^=x
    return a

def closure_test(features, S):
    """Feature rows include constant 1; S nonempty; row-span closure."""
    piv={}
    def red(x):
        for i,p in sorted(piv.items(),reverse=True):
            if x>>i&1:x^=p
        return x
    for j,row in enumerate(features):
        if S>>j&1:
            x=red(row)
            if x:piv[x.bit_length()-1]=x
    return sum(1<<j for j,row in enumerate(features) if red(row)==0)

def feature_rows(n, gates):
    k=1<<n
    masks=[(1<<(2*k))-1]+[sum(((i>>j)&1)<<i for i in range(2*k)) for j in range(n+1)]+[g|(g<<k) for g in gates]
    return [sum(((w>>i)&1)<<j for j,w in enumerate(masks)) for i in range(2*k)]

def mixed_targets(A,B,k):
    M=(1<<k)-1
    def grouped(D):
        d=defaultdict(list)
        for a in D:d[(a&M)^(a>>k)].append(a&M)
        return d
    X,Y=grouped(A),grouped(B)
    return {M^a^b for p,l in X.items() for a in l for b in Y.get(M^p,())}

if __name__=='__main__':
    if not __debug__:raise RuntimeError('assertions required')
    n=4;k=16;M=65535;a,b,c,d=[sum(((i>>j)&1)<<i for i in range(k)) for j in range(n)]
    V=space([*initial(n),a&b]);g=d&(a^b);W=space([*V,g]);A=atom_set(n,V)-{0};B=atom_set(n,W)-{0}
    assert d in V and a^b in V and g not in V
    assert len(A)==11503 and len(B)==36511
    f=0x127;h=graph(f,n);assert h==0x0127fed8
    old=(0x00000ff0,0x000ff000,0x01280128)
    four=(0x00006699,0x00669900,0x00010001,0x01400140)
    new=(four[0]^four[1],four[2]^four[3])
    assert xor(old)==xor(four)==xor(new)==h
    assert set(old+four)<=A and set(new)<=B-A and len(set(four))==4
    assert h not in A|B and all(h^p not in B for p in A)
    assert (rank(n,V,f),rank(n,W,f))==(3,2)
    R=feature_rows(n,[a&b]);T=feature_rows(n,[a&b,g]);assert all(closure_test(R,p)==p for p in A);assert all(closure_test(T,p)==p for p in B)
    # Independent direct membership via span closure for every mixed-pair candidate.
    assert all(closure_test(T,h^p)!=h^p for p in A)
    old_d,r,_=quotient_dist(n,V);new_d,s,_=quotient_dist(n,W)
    targets={f for f in range(1<<k) if old_d[r(f)]==2 and new_d[s(f)]==1}
    mix=mixed_targets(A,B,k);bad=targets-mix
    assert len(targets)==20736 and len(bad)==4096 and f in bad
    print('PASS: old/new atoms',len(A),len(B),'rank 3->2 targets',len(targets),'strict nonminimum targets',len(bad))
    print('PASS: affine closure membership',len(A)+len(B),'mixed exclusions',len(A),'witness',hex(h),'new pair',tuple(hex(t) for t in new))
