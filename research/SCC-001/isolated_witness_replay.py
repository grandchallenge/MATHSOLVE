#!/usr/bin/env python3
"""Exact finite replay: constrained safe spans and hyperplane reachability."""
from itertools import combinations, product
from target_ideal_replay import Space, affine, coords, kernel

def dot(a,b):
    return (a&b).bit_count()&1

def require(ok,msg):
    if not ok:raise AssertionError(msg)

def span_values(V):
    a=[0]
    for v in V:a += [v^w for w in a]
    return a

def symplectic_basis(V,lam):
    # Build a quotient basis modulo the constant; then symplectic elimination.
    one=(1<<max(v.bit_length() for v in V))-1
    S=Space([one]);w=[]
    for a in V:
        if a not in S:
            w.append(a);S.add(a)
    require(S.equal(V),"quotient basis")
    pairs=[]
    while w:
        hit=next(((i,j) for i,j in combinations(range(len(w)),2)
                  if dot(lam,w[i]&w[j])),None)
        if hit is None:break
        i,j=hit;e,f=w[i],w[j];pairs.append((e,f))
        w=[x^(e if dot(lam,x&f) else 0)^(f if dot(lam,x&e) else 0)
           for k,x in enumerate(w) if k not in (i,j)]
    bs=[x for p in pairs for x in p]+w
    require(Space([one,*bs]).equal(V),"symplectic basis span")
    for i,j in combinations(range(len(bs)),2):
        require(dot(lam,bs[i]&bs[j])==int(i%2==0 and j==i+1 and i<2*len(pairs)),
                "canonical form")
    return pairs,bs

def candidates(V,lam):
    pairs,bs=symplectic_basis(V,lam)
    gates=[(u,v) for u,v in combinations(bs,2) if not dot(lam,u&v)]
    if pairs:
        e,f=pairs[0]
        gates += [(e^a,f^b) for a,b in pairs[1:]]
    require(all(u in V and v in V and not dot(lam,u&v) for u,v in gates),
            "legal safe products")
    return gates

def verify_span(V,lam,gates,brute=False):
    F=Space([*V,*(a&b for a,b in combinations(V,2))])
    H2=kernel(F,lambda x:dot(lam,x))
    C=Space([*V,*(a&b for a,b in gates)])
    require(C.equal(H2),"safe-span identity")
    if brute:
        vs=span_values(V)
        B=Space([*V,*(a&b for a,b in combinations(vs,2) if not dot(lam,a&b))])
        require(B.equal(C),"independent brute safe span")
    return C

def reach(n,V,lam,brute=False):
    N=1<<n;start=len(V);steps=checks=0
    require(lam!=0 and all(not dot(lam,a) for a in V),"initial live witness")
    V=Space(V)
    while len(V)<N-1:
        gs=candidates(V,lam);verify_span(V,lam,gs,brute);checks+=1
        g=next((a&b for a,b in gs if a&b not in V),None)
        require(g is not None,"safe nonredundant gate exists")
        V.add(g);steps+=1
        require(all(not dot(lam,a) for a in V),"preserved witness")
    require(steps==N-1-start,"exact dimension length")
    require(len(V)==N-1,"hyperplane reached")
    require(all(not dot(lam,a) for a in V),"exact endpoint")
    return V,steps,checks

def annihilators(n,V):
    # Independent direct enumeration on small cubes.
    return [l for l in range(1,1<<(1<<n)) if all(not dot(l,v) for v in V)]

def bounded_history():
    n=3;V=affine(n);N=1<<n
    layers=[{tuple(sorted(span_values(V))):V}]
    for _ in range(3):
        layer={}
        for W in layers[-1].values():
            for u,v in combinations(span_values(W),2):
                Z=Space([*W,u&v])
                layer[tuple(sorted(span_values(Z)))]=Z
            layer[tuple(sorted(span_values(W)))]=W
        layers.append(layer)
    hist=[{} for _ in layers];cases=0
    for f in range(1<<N):
        if f in V:continue
        L=[l for l in annihilators(n,V) if dot(l,f)]
        require(len(L)==8,"initial coset size")
        l0=L[0];ds=list(Space(l^l0 for l in L))
        require(len(ds)==3,"parameter dimension")
        for t,layer in enumerate(layers):
            live=[]
            for W in layer.values():
                if f in W:continue
                mask=sum(1<<i for i,l in enumerate(L) if all(not dot(l,w) for w in W))
                require(mask and mask.bit_count()*(1<<t)>=len(L),"survival fraction")
                live.append(mask)
            S=0
            for k in range(min(t,len(ds))+1):
                for subset in combinations(ds,k):
                    l=l0
                    for a in subset:l^=a
                    S|=1<<L.index(l)
            require(all(S&m for m in live),"bounded parameter family")
            minimum=min(s.bit_count() for s in range(1,1<<len(L))
                        if all(s&m for m in live))
            if t==3:require(minimum==len(L),"full horizon necessity")
            hist[t][minimum]=hist[t].get(minimum,0)+1
            cases+=len(live)
    print("bounded horizons",list(map(len,layers)),"incomplete-state target checks",cases,
          "minimum witness-family histograms",hist)

def main():
    counts=[0,0,0,0]
    for n in (2,3,4):
        V=affine(n);ls=annihilators(n,V);N=1<<n
        require(len(ls)==(1<<(N-len(V)))-1,"annihilator count")
        for l in ls:
            H,s,c=reach(n,V,l,brute=n<=3)
            # For n<=3 enumerate independently; for n=4 dimension+annihilation suffices.
            if n<=3:require(annihilators(n,H)==[l],"unique survivor")
            if n<=3:
                for f in range(1<<N):
                    if not dot(l,f):continue
                    require(f not in H,"target remains unavailable")
                    require(sum(all(not dot(k,v) for v in H) for k in ls if dot(k,f))==1,
                            "exact singleton target coset")
                    counts[3]+=1
            counts[0]+=1;counts[1]+=s;counts[2]+=c
        print("n",n,"hyperplanes",len(ls),"PASS",flush=True)
    print("hyperplane paths, safe gates, safe-span checks, singleton target checks",counts)
    # Nonlinear starting states: all distinct legal first gate classes on n=3.
    n=3;V=affine(n);vs=span_values(V);seen={}
    for u,v in combinations(vs,2):
        W=Space([*V,u&v]);key=tuple(sorted(span_values(W)))
        seen[key]=W
    paths=steps=0
    for W in seen.values():
        for l in annihilators(n,W):
            H,s,c=reach(n,W,l,brute=True);paths+=1;steps+=s
    print("nonlinear start states",len(seen),"paths",paths,"gates",steps)
    # Exact all-gate coset transition counts for small states.
    cosets=0
    for W in seen.values():
        ls=annihilators(3,W);vs=span_values(W)
        gs={u&v for u,v in product(vs,repeat=2)}
        for f in range(256):
            if f in W:continue
            L=[l for l in ls if dot(l,f)]
            for g in gs:
                m=sum(not dot(l,g) for l in L)
                expect=len(L) if g in W else 0 if f^g in W else len(L)//2
                require(m==expect,"coset half/all/none")
                cosets+=1
    a,b,c,d=coords(4);V=affine(4);H=Space([*V,(a&b)^(c&d)])
    vs=span_values(V);require(len(H)==len(V)+1,"proper extension")
    require(all(u&v in V for u,v in product(vs,repeat=2) if u&v in H),
            "rank-four safe saturation")
    print("coset transitions",cosets,"rank-four obstruction PASS")
    bounded_history()

if __name__=="__main__":
    main()
