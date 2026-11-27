#!/usr/bin/env python3
"""Exact finite relative affine-frontier, dual labels and gate-history replay."""
from collections import Counter
from functools import lru_cache
from itertools import product, combinations
from random import Random
from functools import reduce
from marked_graph_replay import initial, space

def dot(a,b):return (a&b).bit_count()&1

def xor_rank(xs):
    piv={}
    for a in xs:
        while a:
            j=a.bit_length()-1
            if j not in piv:piv[j]=a;break
            a^=piv[j]
    return len(piv)

def basis(V):
    bs=[]
    for v in V:
        if xor_rank(bs+[v])>len(bs):bs.append(v)
    assert space(bs)==V
    return bs

def coords(n):
    return [sum(((i>>j)&1)<<i for i in range(1<<n)) for j in range(n)]

@lru_cache(None)
def restrict(V,C):return frozenset(v&C for v in V)

@lru_cache(None)
def A(V,C,f):
    assert not f&~C
    U=restrict(V,C)
    if f in U:return 0
    return 1+min(max(A(V,z,f&z),A(V,C^z,f&(C^z)))
                 for z in U if z and z!=C)

def choose_tree(V,C,f):
    if f in restrict(V,C):
        return ('leaf',next(v for v in V if v&C==f))
    z=min((v for v in V if v&C not in (0,C)),
          key=lambda v:max(A(V,C&v,f&v),A(V,C&~v,f&~v)))
    return ('query',z,choose_tree(V,C&~z,f&~z),choose_tree(V,C&z,f&z))

def verify_tree(T,V,C,f):
    if T[0]=='leaf':
        assert T[1] in V and T[1]&C==f
        return {i:0 for i in range(C.bit_length()) if C>>i&1}
    _,q,L,R=T
    assert q in V and C&q and C&~q
    d0=verify_tree(L,V,C&~q,f&~q)
    d1=verify_tree(R,V,C&q,f&q)
    return {i:d+1 for i,d in (d0|d1).items()}

def translate(T,V,C):
    q=next(v for v in V if v&C==T[1]&C)
    if T[0]=='leaf':return ('leaf',q)
    if not C&q:return translate(T[2],V,C)
    if not C&~q:return translate(T[3],V,C)
    return ('query',q,translate(T[2],V,C&~q),translate(T[3],V,C&q))

def lift(T,V,C,f,u,v):
    if f in restrict(V,C):
        return ('leaf',next(w for w in V if w&C==f))
    if (u&v&C) in restrict(V,C):return translate(T,V,C)
    assert C&u and C&~u
    return ('query',u,translate(T,V,C&~u),translate(T,V,C&u))

def bilinear_rank(lam,bs):
    rows=[sum(dot(lam,u&v)<<j for j,v in enumerate(bs)) for u in bs]
    return xor_rank(rows)

def masks(C):
    a=C
    while True:
        yield a
        if not a:return
        a=(a-1)&C

def labels(V,C):
    return tuple(l for l in masks(C) if all(not dot(l,v) for v in V))

def state_check(n,V):
    M=(1<<(1<<n))-1;bs=basis(V);freq=Counter(u&v for u,v in product(V,repeat=2))
    den=len(V)**2;cells=witnesses=target_witnesses=0
    ranks={}
    for l in labels(V,M):
        r=bilinear_rank(l,bs);ranks[l]=r
        assert r%2==0
        hit=sum(w for g,w in freq.items() if dot(l,g))
        assert (hit*(1<<r)*2)==den*((1<<r)-1)
        witnesses+=1
    for C in range(1,M+1):
        U=restrict(V,C);D=labels(V,C)
        assert len(U)*len(D)==1<<C.bit_count()
        hit=sum(w for g,w in freq.items() if g&C not in U)
        if len(U)==1<<C.bit_count():assert hit==0
        else:
            assert hit*8>=3*den
            cells+=1
        for f in masks(C):
            if f in U:continue
            assert any(dot(l,f) and ranks[l]>0 for l in D)
            target_witnesses+=1
    return cells,witnesses,target_witnesses

def transition(n,V,u,v,rng):
    g=u&v;W=space([*V,g]);M=(1<<(1<<n))-1
    b0,b1=basis(V),basis(W)
    old=labels(V,M);new=labels(W,M)
    assert set(new)=={l for l in old if not dot(l,g)}
    for l in new:
        assert bilinear_rank(l,b1)-bilinear_rank(l,b0) in (0,2)
    checks=0
    for C in range(1,M+1):
        U=restrict(V,C);act=int(g&C not in U)
        for f in masks(C):
            a,b=A(V,C,f),A(W,C,f)
            assert 0<=a-b<=act*int(f not in U)
            assert (a==0)==(f in U)
            assert a<=max(n-1,0)
            checks+=1
    profiles=0
    for _ in range(24):
        C=rng.randint(1,M);f=rng.randrange(M+1)&C
        T=choose_tree(W,C,f);oldT=lift(T,V,C,f,u,v)
        d=verify_tree(T,W,C,f);e=verify_tree(oldT,V,C,f)
        cap=int(g&C not in restrict(V,C) and f not in restrict(V,C))
        assert max(d.values())==A(W,C,f)
        assert all(e[i]<=d[i]+cap for i in d)
        profiles+=len(d)
    return W,checks,len(old),len(new),profiles

def forward_history(n,gates):
    V0=initial(n);M=(1<<(1<<n))-1;V=V0
    frontier={M:()}
    states=[V]
    for j,(u,v) in enumerate(gates):
        assert u in V and v in V
        g=u&v;W=space([*V,g]);new={}
        for C,history in frontier.items():
            U=restrict(V0,C)
            assert restrict(V,C)<=U
            if g&C in U:new[C]=history
            else:
                q=next(w for w in V0 if w&C==u&C)
                assert C&q and C&~q
                new[C&q]=history+(j,);new[C&~q]=history+(j,)
        V=W;frontier=new;states.append(V)
        assert all(restrict(V,C)<=restrict(V0,C) for C in frontier)
    assert sum(C.bit_count() for C in frontier)==1<<n
    assert all(tuple(sorted(set(p)))==p for p in frontier.values())
    depths={i:len(p) for C,p in frontier.items() for i in range(1<<n) if C>>i&1}
    weights=[1,2,3,5,7,11,13,17][:1<<n]
    denom=sum(weights)
    cells=range(1,M+1)
    ws={C:1+C.bit_count() for C in cells}
    for f in V:
        assert all(f&C in restrict(V0,C) for C in frontier)
        assert A(V0,M,f)<=max(depths.values())<=len(gates)
        psi=sum(ws[C]*A(V0,C,f&C) for C in cells)
        cost=0
        for Vj,(u,v) in zip(states,gates):
            cost+=sum(ws[C] for C in cells
                      if f&C not in restrict(Vj,C) and u&v&C not in restrict(Vj,C))
        assert psi<=cost
        assert sum(weights[i]*depths[i] for i in depths)<=denom*len(gates)
    return len(V),len(frontier)


def independent(xs):
    piv={}
    for a in xs:
        while a:
            j=a.bit_length()-1
            if j not in piv:piv[j]=a;break
            a^=piv[j]
    return tuple(piv.values())

@lru_cache(None)
def filtration(n,V):
    M=(1<<(1<<n))-1
    fs=[(M,)];bs=basis(V)
    for _ in range(n):
        fs.append(independent(a&b for a in fs[-1] for b in bs))
    assert len(fs[-1])==1<<n
    return tuple(fs)

def visibility(lam,fs):
    return next(j for j,F in enumerate(fs) if any(dot(lam,v) for v in F))

def higher_visibility(states):
    cuts=probabilities=weighted=0
    for n,V in sorted(states):
        M=(1<<(1<<n))-1;bs=basis(V);F=filtration(n,V)
        ls=[l for l in range(1,M+1) if not dot(l,M)]
        d={l:visibility(l,F) for l in ls}
        freq=Counter(u&v for u,v in product(V,repeat=2))
        drops={}
        for g in freq:
            W=space([*V,g]);G=filtration(n,W)
            ds={}
            for l in ls:
                k=d[l];j=visibility(l,G)
                assert 0<=k-j<=1
                if k>=2:
                    # Contraction of the first nonzero alternating form,
                    # evaluated independently on distinct basis tuples.
                    hit=any(dot(l,g&reduce(int.__and__,ws,M))
                            for ws in combinations(bs,k-2))
                    assert hit==(j==k-1)
                    cuts+=1
                ds[l]=k-j
            drops[g]=ds
        den=len(V)**2
        for l,k in d.items():
            if k<2:continue
            hit=sum(freq[g]*drops[g][l] for g in freq)
            assert hit*(1<<k)*(1<<(k-1))>=den*((1<<k)-1)*((1<<(k-1))-1)
            probabilities+=1
        # Fixed, unequal, positive weights on every target-disagreeing functional.
        for f in range(M+1):
            ws={l:1+l.bit_count() for l in ls if dot(l,f)}
            P=sum(w*(d[l]-1) for l,w in ws.items())
            live=sum(w for l,w in ws.items() if d[l]>1)
            K=max(sum(w*ds[l] for l,w in ws.items()) for ds in drops.values())
            assert (P==0)==(f in V)
            assert K*8>=3*live and P*3<=8*max(n-1,0)*K
            weighted+=1
    sharp=[]
    for n in (2,3,4,5):
        M=(1<<(1<<n))-1;V=initial(n);F=filtration(n,V)
        assert visibility(M,F)==n
        bs=basis(V)
        terms=tuple(reduce(int.__and__,ws,M) for ws in combinations(bs,n-2))
        count=sum(any(dot(M,u&v&t) for t in terms) for u,v in product(V,repeat=2))
        den=len(V)**2
        assert count*(1<<n)*(1<<(n-1))==den*((1<<n)-1)*((1<<(n-1))-1)
        sharp.append((n,count,den))
    print('all-orders contraction checks',cuts,'probability checks',probabilities,
          'weighted actual-drop certificates',weighted,'sharp flat counts',sharp)

def main():
    rng=Random(261127);states=set();transitions=checks=oldw=neww=profiles=0
    for n in (1,2,3):
        V=initial(n);M=(1<<(1<<n))-1;x=coords(n)
        if n<=2:
            gs={u&v:(u,v) for u,v in product(V,repeat=2)}
            histories=[[(u,v)] for u,v in gs.values()]
        else:
            a,b,c=x
            histories=[[(a,b),(a&b,c),(a^c,b^c),((a&b)^c,(b^c))],
                       [(b,c),(a,b&c),(a^b,c),(a,a)]]
        for hist in histories:
            V=initial(n);states.add((n,V))
            for u,v in hist:
                assert u in V and v in V
                W,k,d,e,p=transition(n,V,u,v,rng)
                transitions+=1;checks+=k;oldw+=d;neww+=e;profiles+=p
                states.add((n,W));V=W
    totals=[0,0,0]
    for n,V in sorted(states):
        for j,k in enumerate(state_check(n,V)):totals[j]+=k
    a,b=coords(2);V=initial(2)
    hits=sum((u&v) not in V for u,v in product(V,repeat=2))
    assert hits*8==3*len(V)**2
    assert A(V,15,a&b)==1 and A(space([*V,a&b]),15,a&b)==0
    V4=initial(4);a,b,c,d=coords(4);f=(a&b)^(c&d)
    assert A(V4,65535,f)==2
    assert A(space([*V4,a&b]),65535,f)==1
    base=initial(2);wide=initial(3);spectators=0
    for C in range(1,16):
        for f in masks(C):
            assert A(base,C,f)==A(wide,C|(C<<4),f|(f<<4))
            spectators+=1
    a,b,c=coords(3)
    complete,leaves=forward_history(3,[(a,b),(a&b,c),(a^c,b^c),
                                      ((a&b)^c,b^c)])
    print('states',len(states),'transitions',transitions,'local comparisons',checks,
          'witness cut old/new checks',oldw,neww,'pointwise profile checks',profiles)
    print('unresolved cells',totals[0],'bilinear probability checks',totals[1],
          'target-disagreeing visible witness checks',totals[2])
    print('sharp activation 3/8; AND and inner product depth controls;',spectators,'spectator checks')
    print('labelled history completed targets',complete,'frontier leaves',leaves,'PASS')
    higher_visibility(states)
if __name__=='__main__':
    if not __debug__:raise RuntimeError('assertions required')
    main()
