#!/usr/bin/env python3
"""Exact Boolean reconfiguration: path construction, gate lifting and BFS."""
from collections import deque
from functools import lru_cache
from itertools import combinations
from random import Random
from marked_graph_replay import initial, space, atom_set, graph

def xor(xs):
    r=0
    for x in xs:r^=x
    return r

def parity(xs):
    s=set()
    for x in xs:
        if x:s.symmetric_difference_update((x,))
    return frozenset(s)

def coords(D):
    return [sum(((i>>j)&1)<<i for i in range(1<<D)) for j in range(D)]

def restrict(S,C):return parity(a&C for a in S)

def forms(n,V):
    k=1<<n
    return space([v|(v<<k) for v in V]+[((1<<k)-1)<<k])

@lru_cache(None)
def moves(n,V):
    M=(1<<(2*(1<<n)))-1
    return frozenset(frozenset((a,a&z,a&(M^z)))
        for a in atom_set(n,V)-{0} for z in forms(n,V)
        if a&z and a&(M^z))

def split(S,z,M):
    out=[S]
    for a in sorted(S):
        b,c=a&z,a&(M^z)
        if b and c:out.append(out[-1]^frozenset((a,b,c)))
    assert out[-1]==restrict(S,z)^restrict(S,M^z)
    return out

def join(path,tail):
    assert path[-1]==tail[0]
    path.extend(tail[1:])

def refine(S,T,zs,M):
    if S==T:return [S]
    assert zs
    z,*rest=zs
    p=split(S,z,M);q=split(T,z,M)
    s0,s1=restrict(S,M^z),restrict(S,z)
    t0,t1=restrict(T,M^z),restrict(T,z)
    join(p,[R^s1 for R in refine(s0,t0,rest,M)])
    join(p,[t0^R for R in refine(s1,t1,rest,M)])
    join(p,list(reversed(q)))
    return p

def validate(n,V,path):
    A=atom_set(n,V)-{0};h=xor(path[0])
    E=moves(n,V)
    assert all(R<=A and xor(R)==h for R in path)
    assert all(R^S in E for R,S in zip(path,path[1:]))
    return max(map(len,path))

def cell_split(S,u,v,M):
    p=split(S,u,M)
    tail=split(restrict(S,u),v,M)
    fixed=restrict(S,M^u)
    join(p,[fixed^R for R in tail])
    return p

def lift(n,V,u,v,path):
    k=1<<n;M=(1<<(2*k))-1
    u=u|(u<<k);v=v|(v<<k)
    cells=(M^u,u&(M^v),u&v)
    def L(R):return parity(a&C for a in R for C in cells)
    out=cell_split(path[0],u,v,M)
    assert out[-1]==L(path[0])
    E=moves(n,V)
    for R,S in zip(path,path[1:]):
        diffs=[restrict(R^S,C) for C in cells]
        diffs=[t for t in diffs if t]
        assert all(t in E for t in diffs)
        # Each nonzero move lives on its own cell. Decreases first.
        diffs.sort(key=lambda t:len(out[-1]^t)-len(out[-1]))
        for t in diffs:out.append(out[-1]^t)
        assert out[-1]==L(S)
    join(out,list(reversed(cell_split(path[-1],u,v,M))))
    assert max(map(len,out))<=3*max(map(len,path))
    assert len(out)-1<=2*(len(path[0])+len(path[-1]))+3*(len(path)-1)
    return out

def component(S,E,cap):
    prev={S:None};q=deque([S])
    while q:
        R=q.popleft()
        for d in E:
            T=R^d
            if len(T)<=cap and T not in prev:
                prev[T]=R;q.append(T)
    return prev

def recover(prev,T):
    out=[T]
    while prev[out[-1]] is not None:out.append(prev[out[-1]])
    return list(reversed(out))

def exact_barrier():
    n=2;V=initial(n);W=space([*V,8])
    S=frozenset((3,0x84));T=frozenset((5,0x82))
    assert xor(S)==xor(T)==graph(8,n)==0x87
    assert graph(8,n) not in atom_set(n,V)
    E=moves(n,V)
    assert len(E)==77
    prev=component(S,E,3)
    assert len(prev)==9 and T not in prev
    prev=component(S,E,4)
    assert len(prev)==826 and T in prev
    p=recover(prev,T)
    assert validate(n,V,p)==4
    q=recover(component(S,moves(n,W),2),T)
    assert validate(n,W,q)==2
    assert validate(n,V,lift(n,V,10,12,q))<=6
    U=frozenset((0x0f,0x88))
    assert xor(U)==graph(8,n) and U<=atom_set(n,V)
    assert U not in component(S,moves(n,W),2)
    p=recover(component(S,moves(n,W),3),U)
    assert validate(n,W,p)==3
    assert graph(8,n) in forms(n,W)
    print('exact AND barrier: H=4 -> 2; cap-three component=9; cap-four component=826')
    print('completion counterexample: target available, old optimal endpoints still require height 3')

def exhaustive_small():
    n=2;V=initial(n);W=space([*V,8])
    A=sorted(atom_set(n,V)-{0})
    groups={}
    for a,b in combinations(A,2):
        h=a^b;f=h>>4
        if h==graph(f,n) and h not in A:
            groups.setdefault(f,[]).append(frozenset((a,b)))
    assert len(groups)==8 and all(len(v)==7 for v in groups.values())
    # Independent integer-coordinate implementation of bounded connectivity.
    E0=moves(n,V);E1=moves(n,W)
    hist={};pairs=0
    for reps in groups.values():
        for i,S in enumerate(reps):
            reached={}
            for state,E in ((V,E0),(W,E1)):
                ix={a:1<<j for j,a in enumerate(sorted(atom_set(n,state)-{0}))}
                def encode(R):return xor(ix[a] for a in R)
                es=tuple(encode(t) for t in E)
                start=encode(S)
                hs={}
                for cap in (2,3,4):
                    seen={start};q=deque([start])
                    while q:
                        a=q.popleft()
                        for e in es:
                            b=a^e
                            if b.bit_count()<=cap and b not in seen:
                                seen.add(b);q.append(b)
                    for T in reps[i+1:]:
                        if encode(T) in seen:hs.setdefault(T,cap)
                    if len(hs)==len(reps)-i-1:break
                assert len(hs)==len(reps)-i-1
                reached[state]=hs
            for T in reps[i+1:]:
                a,b=reached[V][T],reached[W][T]
                assert b<=a<=3*b
                hist[a,b]=hist.get((a,b),0)+1;pairs+=1
    print('exhaustive two-input optimal-endpoint pairs',pairs,'height histogram',sorted(hist.items()))

def randomized():
    rng=Random(261127);pairs=steps=lifts=lift_steps=spectator_steps=nonredundant=new_moves=0
    for n in (1,2,3):
        D=n+1;k=1<<n;M=(1<<(2*k))-1
        V=initial(n)
        for j in range(4):
            u,v=rng.choice(V),rng.choice(V)
            x=[sum(((i>>l)&1)<<i for i in range(k)) for l in range(n)]
            if n>=2 and j==0:u,v=x[:2]
            if n==3 and j==1:u,v=x[0]&x[1],x[2]
            assert u in V and v in V
            W=space([*V,u&v])
            A=sorted(atom_set(n,V)-{0})
            E=sorted(moves(n,V),key=lambda t:tuple(sorted(t)))
            F=sorted(moves(n,W),key=lambda t:tuple(sorted(t)))
            for i in range(12):
                S=frozenset(rng.sample(A,rng.randint(1,4)))
                T=S
                for _ in range(4):T^=rng.choice(E)
                p=refine(S,T,coords(D),M)
                h=validate(n,V,p)
                assert h<=(D+1)*max(len(S),len(T))
                assert len(p)-1<=((1<<D)-1)*(len(S)+len(T))
                pairs+=1;steps+=len(p)-1
                # Insert successor-only excursions before a refinement path.
                # Endpoints stay in the old dictionary.
                q=[S]
                for _ in range(3):
                    delta=rng.choice(F)
                    q.append(q[-1]^delta)
                    new_moves+=delta not in E
                nonredundant+=W!=V
                q.extend(list(reversed(q))[1:])
                join(q,refine(S,T,coords(D),M))
                validate(n,W,q)
                l=lift(n,V,u,v,q)
                validate(n,V,l)
                assert l[0]==S and l[-1]==T
                lifts+=1;lift_steps+=len(l)-1
                # Test restriction of padded partition moves on a spare input,
                # including arbitrary spectator-dependent affine forms.
                if n<=2 and i==0:
                    def ext(a):
                        low=a&((1<<k)-1);high=a>>k
                        return low|(low<<k)|(high<<(2*k))|(high<<(3*k))
                    VV=space([x|(x<<k) for x in V]+[((1<<k)-1)<<k])
                    def ret(a):
                        return (a&((1<<k)-1))|(((a>>(2*k))&((1<<k)-1))<<k)
                    for t in moves(n+1,VV):
                        d=parity(ret(x) for x in t)
                        assert not d or d in moves(n,V)
                        spectator_steps+=1
                    lifted=[frozenset(ext(a) for a in R) for R in p]
                    assert validate(n+1,VV,lifted)==h
            V=W
    print('refinement pairs',pairs,'moves',steps,'gate path lifts',lifts,
          'lifted moves',lift_steps,'spectator retraction checks',spectator_steps,
          'nonredundant gate lifts',nonredundant,'successor-only excursion moves',new_moves)
    assert nonredundant and new_moves
if __name__=='__main__':
    if not __debug__:raise RuntimeError('assertions required')
    exact_barrier()
    exhaustive_small()
    randomized()
