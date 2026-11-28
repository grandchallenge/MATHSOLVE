#!/usr/bin/env python3
"""Exact finite checks of budget shadow, reverse branches, determinant witnesses."""
from collections import Counter
from itertools import combinations, product
from math import comb
from random import Random
from functools import reduce
from target_ideal_replay import Space, affine, coords, filt, quotient, draw

def require(ok,msg):
    if not ok:raise AssertionError(msg)

def values(V):
    a=[0]
    for v in V:a += [v^w for w in a]
    return a

def xor(xs):
    return reduce(int.__xor__,xs,0)

def mul(xs,one):
    return reduce(int.__and__,xs,one)

def C(t,d):
    return sum(comb(t,j) for j in range(d-1,t+1))

def anf(f,n):
    # Boolean Mobius transform, coefficient mask indexed by monomial subset.
    for j in range(n):
        f ^= (f<< (1<<j)) & coords(n)[j]
    return f

def homogeneous(f,n,d):
    return f & sum(1<<i for i in range(1<<n) if i.bit_count()==d)

def wedge(a,b):
    out=0
    while a:
        x=a&-a;a^=x;i=x.bit_length()-1
        c=b
        while c:
            y=c&-c;c^=y;j=y.bit_length()-1
            if not i&j:out^=1<<(i|j)
    return out

def lin(x,n):
    return sum(1<<(1<<i) for i in range(n) if x>>i&1)

def determinant(rows,k):
    return int(len(Space(rows))==k)

def certificate(h,n,d):
    I=next(i for i in range(1<<n) if h>>i&1)
    require(I.bit_count()==d,"pivot degree")
    for J in range(1<<n):
        if J.bit_count()!=d:continue
        ii=[1<<i for i in range(n) if (I&~J)>>i&1]
        jj=[1<<i for i in range(n) if (J&~I)>>i&1]
        k=len(ii)
        if k<2:continue
        keys=[[I^a^b for b in jj] for a in ii]
        rows=[sum(((h>>s)&1)<<j for j,s in enumerate(row)) for row in keys]
        if determinant(rows,k)!=((h>>J)&1):
            K=[J,*[s for row in keys for s in row]]
            return [1<<I,*[(1<<s) if h>>s&1 else (1<<I)^(1<<s) for s in K]]
    return None

def pairing(a,b):return (a&b).bit_count()&1

def decomposables(n,d):
    forms=[lin(x,n) for x in range(1,1<<n)]
    ps={1}
    for _ in range(d):ps={wedge(p,w) for p in ps for w in forms}
    return ps|{0}

def check_certificates():
    checks=certs=0
    for n in (3,4,5):
        for d in range(2,n+1):
            monos=[1<<i for i in range(1<<n) if i.bit_count()==d]
            # At n<=5 there are at most ten monomials per degree.
            ds=decomposables(n,d)
            for h in values(Space(monos)):
                if not h:continue
                S=certificate(h,n,d)
                require((S is None)==(h in ds),"chart iff decomposability")
                if S:
                    require(len(S)<=d*d+2 and all(pairing(s,h) for s in S),"target witnesses")
                    require(all(any(not pairing(s,p) for s in S) for p in ds),
                            "all decomposable cuts excluded")
                    certs+=1
                checks+=1
    # Explicit unbounded family uses just six coordinates of the coefficient array.
    for d in range(2,8):
        n=d+2;z=(1<<(d-2))-1
        h=(1<<(z|(3<<(d-2))))^(1<<(z|(12<<(d-2))))
        S=certificate(h,n,d)
        require(S is not None and len(S)==6,"six-witness family")
        # Exact constructed d-gate output and independent ANF.
        x=coords(n);a,b,c,e=x[-4:]
        out=(a&b)^(c&e)
        for v in x[:-4]:out&=v
        require(anf(out,n)==h,"explicit d-gate target")
    print("determinant charts",checks,"nondecomposable certificates",certs,
          "six-witness explicit family d=2..7 PASS",flush=True)

def branches(initial_count,gates,output):
    terms=[(0,(output,))]
    for j in range(len(gates)-1,-1,-1):
        bit=1<<(initial_count+j)
        U,V=gates[j];next_terms=[]
        for mask,fs in terms:
            ids=[i for i,f in enumerate(fs) if f&bit]
            if not ids:
                next_terms.append((mask,fs));continue
            i=ids[0];l=fs[i]^bit
            base=[f for a,f in enumerate(fs) if a!=i]
            for a in ids[1:]:
                b=a-int(a>i)
                base[b]=1^l^(fs[a]^bit)
            next_terms.append((mask|(1<<j),tuple([*base,U,V])))
            next_terms.append((mask,tuple([*base,l])))
        terms=next_terms
        require(all(not f&bit for m,fs in terms for f in fs),"eliminated variable")
    require(len({m for m,fs in terms})==len(terms),"unique increase labels")
    require(all(len(fs)<=m.bit_count()+1 for m,fs in terms),"branch factor bound")
    return terms

def random_replay():
    rng=Random(281126);outputs=terms_checked=layers=0
    for n in (2,3,4,5):
        one=(1<<(1<<n))-1
        for mode in (0,1):
            for t in range(7):
                for repeat in range(12):
                    base=[one,*coords(n)]
                    if mode:
                        for _ in range(2):
                            g=draw(Space(base),rng)&draw(Space(base),rng)
                            if g not in Space(base):base.append(g)
                    init=Space(base);F=filt(init,n)
                    xs=base[:];gates=[]
                    for j in range(t):
                        u=rng.randrange(1<<len(xs));v=rng.randrange(1<<len(xs))
                        gates.append((u,v))
                        xs.append(mul((xor(x for i,x in enumerate(xs) if u>>i&1),
                                       xor(x for i,x in enumerate(xs) if v>>i&1)),one))
                    for _ in range(4):
                        o=rng.randrange(1<<len(xs))
                        f=xor(x for i,x in enumerate(xs) if o>>i&1)
                        ts=branches(len(base),gates,o)
                        def ev(a):return xor(x for i,x in enumerate(base) if a>>i&1)
                        ps=[(m,mul((ev(a) for a in fs),one)) for m,fs in ts]
                        require(xor(p for m,p in ps)==f,"exact reverse substitution")
                        freq=Counter(m.bit_count() for m,p in ps)
                        require(all(c<=comb(t,j) for j,c in freq.items()),"binomial count")
                        for d in range(2,min(t+2,n+2)):
                            lo=F[d] # F_(d-1)
                            high=[p for m,p in ps if p not in lo]
                            require(len(high)<=C(t,d),"truncated atom cap")
                            require((f^xor(high)) in lo,"projection equality")
                            if mode==0:
                                require(xor(high).bit_count()*(1<<d)<=C(t,d)*(1<<n),
                                        "degree approximation bound")
                            layers+=1
                        outputs+=1;terms_checked+=len(ps)
    print("reverse outputs",outputs,"branch terms",terms_checked,"layer checks",layers,flush=True)

def top_shadows():
    # Compute actual reachable feature spaces on three bits and compare
    # their maximal quotient images to independently enumerated products.
    n=3;V=affine(n);one=255
    starts=[V]
    for g in {u&v for u,v in product(values(V),repeat=2)}:
        W=Space([*V,g])
        if len(W)>len(V) and not any(W.equal(U) for U in starts):starts.append(W)
    cases=cosets=0
    for base in starts:
        F=filt(base,n);spaces=[base]
        fs=values(base)
        for t in (1,2):
            nexts={}
            for U in spaces:
                for g in {u&v for u,v in product(values(U),repeat=2)}:
                    W=Space([*U,g])
                    nexts.setdefault(tuple(sorted(values(W))),W)
            spaces=list(nexts.values())
            lo=F[t+1];hi=F[t+2]
            actual=set()
            for W in spaces:
                require(all(w in hi for w in W),"degree ceiling")
                L=quotient(W,lo)
                require(len(L)<=1,"one maximal-layer direction")
                p=next(iter(L),0);actual.add(p)
                cases+=1
            expected={0}
            for ws in combinations(fs,t+1):
                expected.add(lo.reduce(mul(ws,one)))
            require(actual==expected,"exact projected reachability")
            for f in values(hi):
                h=lo.reduce(f)
                if not h:continue
                ls=[l for l in range(256) if all(not pairing(l,a) for a in lo) and pairing(l,f)]
                for p in actual:
                    live=[l for l in ls if not pairing(l,p)]
                    require(len(live)==(len(ls) if not p else 0 if p==h else len(ls)//2),
                            "projected coset cardinality")
                    cosets+=1
    print("maximal shadows",cases,"projected coset cuts",cosets,"PASS",flush=True)

if __name__=="__main__":
    check_certificates()
    random_replay()
    top_shadows()
