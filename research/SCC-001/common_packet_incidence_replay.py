#!/usr/bin/env python3
"""Exact common flag incidence and universal packet relaxation replay."""
from collections import defaultdict
from random import Random
from target_ideal_replay import Space, kernel
from fourier_fibre_replay import truth, walsh, parity, lifted_coefficient
from spectral_strata_replay import affine_basis, flags, make_strata, values, quadratic

def require(x,msg):
    if not x:raise AssertionError(msg)

def solve_row(t,j,points,triangular=True):
    shift=2*(j+1) if triangular else 0
    rows={}
    for i,(b,A) in enumerate(points):
        x=1|((b>>shift)<<1);y=(A>>j)&1;w=1<<i
        while x:
            h=x.bit_length()-1
            if h not in rows:
                rows[h]=(x,y,w);break
            a,c,v=rows[h];x^=a;y^=c;w^=v
        if not x and y:
            selected=[k for k in range(len(points)) if w>>k&1]
            xx=yy=0
            for k in selected:
                b,A=points[k];xx^=1|((b>>shift)<<1);yy^=(A>>j)&1
            require(xx==0 and yy==1,"inconsistency certificate")
            require(len(selected)<=2*t-shift+2,"certificate size")
            return None,selected
    sol=0
    for h,(x,y,w) in sorted(rows.items()):
        if parity(x&sol)!=y:sol|=1<<h
    require(all(parity(sol&(1|((b>>shift)<<1)))==((A>>j)&1) for b,A in points),"row solution")
    return sol,None

def bases(strata):
    return [(b,A) for A,(p,U) in strata.items() for b in [p,*[p^u for u in U]]]

def reconstruct(t,strata,alpha,beta,c):
    a=[x&1 for x in alpha];b=[x&1 for x in beta];C=c&1
    points=bases(strata)
    for j in range(t):
        row,cert=solve_row(t,j,points)
        require(cert is None,"genuine row consistent")
        C|=(row&1)<<(j+1)
        for l in range(j+1,t):
            i=1+2*(l-j-1)
            a[l]|=((row>>i)&1)<<(j+1)
            b[l]|=((row>>(i+1))&1)<<(j+1)
    return a,b,C,len(points)

def genuine():
    rng=Random(20261128);lifts=coeffs=basisrows=syndromes=overlaps=0
    for t in range(1,7):
        for _ in range(12):
            a=[rng.randrange(1<<(j+1)) for j in range(t)]
            b=[rng.randrange(1<<(j+1)) for j in range(t)]
            c=rng.randrange(1<<(t+1))
            P=make_strata(t,a,b,c);S={A:affine_basis(ps) for A,ps in P.items()}
            aa,bb,cc,k=reconstruct(t,S,a,b,c)
            actual=make_strata(t,aa,bb,cc)
            require(P==actual,"Parseval completion of labelled strata")
            require(truth(t,a,b,c)==truth(t,aa,bb,cc),"reconstructed Boolean lift")
            lifts+=1;coeffs+=1<<(2*t);basisrows+=k*t
            for r in {0,t,2*t,rng.randrange(2*t+1)}:
                cols=[];B=Space()
                while len(cols)<r:
                    z=rng.randrange(1<<(2*t))
                    if z not in B:B.add(z);cols.append(z)
                M=lambda x:sum(parity(x&v)<<i for i,v in enumerate(cols))
                D=lambda x:flags(x,t,a,b,c)^(c>>1)
                K=kernel(Space(1<<i for i in range(2*t)),M)
                J=Space(D(v) for v in K)
                require(len(J)<=min(t-1,2*t-r),"syndrome rank")
                E={};packets=defaultdict(list)
                for x in range(1<<(2*t)):
                    v=M(x);w=J.reduce(D(x))
                    require(E.setdefault(v,w)==w,"common quotient map")
                    syndromes+=1
                for A,ps in P.items():
                    sums=defaultdict(int)
                    for x in ps:sums[M(x)]+=(-1)**quadratic(x,t,a,b,c)
                    for u,val in sums.items():
                        if val:
                            require(E[u]==J.reduce(A^(c>>1)),"packet incidence")
                            packets[u].append(A)
                for u,labels in packets.items():
                    require(len(Space(A^labels[0] for A in labels))<=len(J),"overlap rank")
                    overlaps+=1
    print("genuine lifts",lifts,"full spectra",coeffs,"basis equations",basisrows,
          "syndrome points",syndromes,"overlap checks",overlaps,flush=True)

def universal(r,f):
    t=3*r+2;S={};B=2*r+2
    for x in range(1<<r):
        label=sum(1<<(B+i) for i in range(r))
        label|=sum(1<<(2*i+((x>>i)&1)) for i in range(r))
        label|=1<<(2*r+((f>>x)&1))
        p=sum(((x>>i)&1)<<(2*(B+i)+1) for i in range(r))
        U=[1<<(2*(B+i)) for i in range(r)]
        for j in range(B):
            if label>>j&1:U.extend([1<<(2*j),1<<(2*j+1)])
        S[label]=(p,U)
        require(len(U)==3*r+2 and label.bit_count()==2*r+1,"universal packet dimensions")
        require(len(Space(U))==len(U),"independent directions")
    require(len(S)==1<<r,"distinct labels")
    return t,S

def transform(z):
    a=list(z);d=1
    while d<len(a):
        for i in range(0,len(a),2*d):
            for j in range(i,i+d):
                x,y=a[j],a[j+d];a[j],a[j+d]=x+y,x-y
        d*=2
    return a

def relaxed():
    rng=Random(281126);cases=nonaffine=rows=full=merges=sample=0
    for r in (1,2,3,4):
        N=1<<r
        fs=range(1<<N) if r<=3 else [rng.randrange(1<<N) for _ in range(12)]
        for idx,f in enumerate(fs):
            t,S=universal(r,f);B=2*r+2
            pts=bases(S)
            affine=all(((f>>x)^(f>>y)^(f>>(x^y))^f)&1==0 for x in range(N) for y in range(N))
            ans=[solve_row(t,j,pts) for j in range(t)]
            require(all(c is None for _,c in ans)==affine,"triangular consistency iff affine")
            _,cert=solve_row(t,2*r+1,pts,False)
            require((cert is None)==affine,"unrestricted sign flag")
            rows+=t;cases+=1
            if not affine:
                x,y=next((x,y) for x in range(N) for y in range(N)
                         if ((f>>x)^(f>>y)^(f>>(x^y))^f)&1)
                require(len({0,x,y,x^y})==4,"four-point witness")
                nonaffine+=1
            # Full ambient transform for every r<=2 target. At larger r
            # retain every stratum incidence check, and enumerate selected fixtures.
            if r>2 and idx>=4:continue
            M=lambda b:sum(((b>>(2*(B+i)))&1)<<i for i in range(r))
            def Q(b):
                return (sum(((b>>(2*j))&1)*((b>>(2*j+1))&1) for j in range(t))
                         + ((b>>(2*(2*r+1)))&1)+((b>>(2*(2*r+1)+1))&1))&1
            z={}
            for A,(p,U) in S.items():
                for u in values(U):
                    b=p^u
                    require(b not in z,"disjoint packets")
                    require(all(A>>j&1 or not (b>>(2*j)&3) for j in range(t)),"inactive coordinates")
                    z[b]=(-1)**Q(b)
            k=2*r+1
            require(len(z)==1<<(2*k),"unit Parseval")
            out=[0]*N
            for b,v in z.items():out[M(b)]+=v
            require(out==[v*(1<<(k-r)) for v in walsh([(f>>x)&1 for x in range(N)])],"target projection")
            merges+=len(z)
            if r<=2:
                inv=transform(z.get(i,0) for i in range(1<<(2*t)))
                require(all(abs(v)==1<<k for v in inv),"Boolean inverse everywhere")
                full+=len(inv)
            else:
                for _ in range(8):
                    v=rng.randrange(1<<(2*t))
                    require(abs(sum(w*(-1)**parity(v&b) for b,w in z.items()))==1<<k,"Boolean inverse sampled")
                    sample+=1
    print("universal targets",cases,"nonaffine certificates",nonaffine,
          "row systems",rows,"enumerated packet points",merges,
          "full inverse values",full,"larger inverse samples",sample,flush=True)

if __name__=="__main__":
    genuine();relaxed();print("PASS")
