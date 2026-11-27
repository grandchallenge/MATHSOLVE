#!/usr/bin/env python3
"""Independent finite replay of matching transport and partition syzygies."""
from collections import deque
from functools import lru_cache
from itertools import combinations
from marked_graph_replay import initial, space, atom_set, graph
from marked_quotient_replay import rank

def xor(xs):
    r = 0
    for x in xs: r ^= x
    return r

def span_rank(xs):
    basis = {}
    for x in xs:
        while x:
            j = x.bit_length()-1
            if j not in basis:
                basis[j] = x
                break
            x ^= basis[j]
    return len(basis)

def distances(A, d):
    out = {0:0}
    q = deque([0])
    while q:
        h = q.popleft()
        for a in A:
            t = h^a
            if t not in out:
                out[t] = out[h]+1
                q.append(t)
    assert len(out)==1<<d
    return out

def matching(A, B):
    adj = tuple(sum(1<<j for j,b in enumerate(A)
                    if i!=j and a^b in B) for i,a in enumerate(A))
    @lru_cache(None)
    def m(S):
        if not S: return 0
        bit = S & -S
        i = bit.bit_length()-1
        T = S ^ bit
        ans = m(T)
        neighbors = T & adj[i]
        while neighbors:
            b = neighbors & -neighbors
            neighbors ^= b
            ans = max(ans, 1+m(T^b))
        return ans
    return m

def exhaustive_dictionaries():
    # Every spanning old dictionary in F2^3, every successor dictionary
    # obtained by any subset of available pair sums, every target syndrome.
    ambient = set(range(1,8))
    extensions = comparisons = strict_nonminimum = 0
    for k in range(3,8):
        for A in combinations(sorted(ambient),k):
            if span_rank(A)!=3: continue
            old = distances(A,3)
            optional = sorted({a^b for a,b in combinations(A,2)}-set(A))
            representations = [(S,xor(A[i] for i in range(k) if S>>i&1))
                               for S in range(1<<k)]
            for t in range(1<<len(optional)):
                B = set(A)|{a for j,a in enumerate(optional) if t>>j&1}
                new = distances(B,3)
                mm = matching(A,B)
                best = [99]*8
                minimum_only = [99]*8
                for S,h in representations:
                    w=S.bit_count()
                    cost=w-mm(S)
                    best[h]=min(best[h],cost)
                    if w==old[h]: minimum_only[h]=min(minimum_only[h],cost)
                for h in range(8):
                    assert best[h]==new[h],(A,B,h,best[h],new[h])
                    strict_nonminimum += minimum_only[h]>new[h]
                    comparisons+=1
                extensions+=1
    print('generic extensions',extensions,'all-syndrome comparisons',comparisons,
          'strict nonminimum cases',strict_nonminimum)

def nonminimum_counterexample():
    # This is an abstract F2^4 dictionary, not claimed to be a Boolean gate state.
    A=(5,7,9,10,13)
    B={5,7,8,9,10,13,14}
    h=6
    assert (distances(A,4)[h],distances(B,4)[h])==(3,2)
    mm=matching(A,B)
    costs=[]
    for S in range(1<<len(A)):
        if xor(a for j,a in enumerate(A) if S>>j&1)==h:
            w=S.bit_count()
            costs.append((w,w-mm(S)))
    assert min(costs)==(3,3)
    assert min(c for w,c in costs)==2
    assert (4,2) in costs
    print('abstract nonminimum counterexample PASS')

def partition_test(n,V):
    k=1<<n
    mask=(1<<(2*k))-1
    A=sorted(atom_set(n,V)-{0})
    ix={a:1<<i for i,a in enumerate(A)}
    coords=[sum(((i>>j)&1)<<i for i in range(2*k)) for j in range(n+1)]
    triples=set()
    for a in A:
        for z in coords:
            b,c=a&z,a&(mask^z)
            if b and c:
                assert b in ix and c in ix and b^c==a
                t=ix[a]^ix[b]^ix[c]
                assert t.bit_count()==3
                triples.add(t)
    assert span_rank(triples)==len(A)-2*k
    # Check every atom against its singleton expansion by exact linear reduction.
    basis={}
    for t in triples:
        while t:
            j=t.bit_length()-1
            if j not in basis: basis[j]=t;break
            t^=basis[j]
    for a in A:
        t=ix[a]^xor(ix[1<<j] for j in range(2*k) if a>>j&1)
        while t:
            j=t.bit_length()-1
            assert j in basis
            t^=basis[j]
    return len(A),len(triples)

def extension_test(n,V,u,v):
    A=sorted(atom_set(n,V)-{0})
    W=space([*V,u&v])
    B=sorted(atom_set(n,W)-{0})
    index={a:1<<i for i,a in enumerate(B)}
    old=set(A)
    assert old<=set(B)
    new=set(B)-old
    rel=[]
    for b in sorted(new):
        a=next(a for a in A if a^b in old)
        c=a^b
        t=index[b]^index[a]^index[c]
        assert t.bit_count()==3 and a^c^b==0
        rel.append(t)
    assert span_rank(rel)==len(new)
    assert all((t&xor(index[b] for b in new)).bit_count()==1 for t in rel)
    return W,len(new)

def real_states():
    count=atoms=triples=extensions=new_rel=0
    for n in (1,2,3):
        V=initial(n)
        k=1<<n
        coords=[sum(((i>>j)&1)<<i for i in range(k)) for j in range(n)]
        states=[V]
        if n>=2:
            W,num=extension_test(n,V,coords[0],coords[1])
            states.append(W);extensions+=1;new_rel+=num
            if n==3:
                U,num=extension_test(n,W,coords[0]&coords[1],coords[2])
                states.append(U);extensions+=1;new_rel+=num
        for S in states:
            a,t=partition_test(n,S)
            count+=1;atoms+=a;triples+=t
    print('partition states',count,'atom expansions',atoms,'partition triples',triples,
          'gate extensions',extensions,'independent new relations',new_rel)
    n=4;k=1<<n;V=initial(n)
    a,b=[sum(((i>>j)&1)<<i for i in range(k)) for j in range(2)]
    W=space([*V,a&b]);A=set(atom_set(n,V))-{0};B=set(atom_set(n,W))-{0}
    f=7;h=graph(f,n)
    good=(0xffff,0x10001,0x60006);bad=(0xff0,0x80008,0xff000)
    assert h==0x7fff8 and xor(good)==xor(bad)==h
    assert set(good)|set(bad)<=A
    assert (rank(n,V,f),rank(n,W,f))==(3,2)
    assert matching(good,B)(7)==1
    assert matching(bad,B)(7)==0
    print('four-bit fixed-target equal-minimum witness PASS')
if __name__=='__main__':
    if not __debug__: raise RuntimeError('assertions required')
    exhaustive_dictionaries()
    nonminimum_counterexample()
    real_states()
