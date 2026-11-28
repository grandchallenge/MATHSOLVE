#!/usr/bin/env python3
"""Exact checks of common active sets, Gauss packets and spectral carries."""
from collections import defaultdict
from math import comb
from random import Random
from target_ideal_replay import Space
from fourier_fibre_replay import truth, walsh, lifted_coefficient, parity, weight

def require(ok,msg):
    if not ok: raise AssertionError(msg)

def values(basis):
    out=[0]
    for v in basis:out += [a^v for a in out]
    return out

def affine_basis(points):
    p=next(iter(points));B=list(Space(x^p for x in points))
    require(len(points)==1<<len(B),"affine cardinality")
    return p,B

def anf(a):
    a=list(a)
    for i in range((len(a)-1).bit_length()):
        d=1<<i
        for j in range(len(a)):
            if j&d:a[j]^=a[j^d]
    return a

def quadratic(b,t,alpha,beta,c):
    q=c&1
    for j in range(t):
        p=(b>>(2*j))&1;r=(b>>(2*j+1))&1
        q^=(p&r)^(p&(alpha[j]&1))^(r&(beta[j]&1))
    return q

def flags(b,t,alpha,beta,c):
    a=0
    for j in range(t):
        v=(c>>(j+1))&1
        for l in range(j+1,t):
            v^=(((b>>(2*l))&1)*((alpha[l]>>(j+1))&1))
            v^=(((b>>(2*l+1))&1)*((beta[l]>>(j+1))&1))
        a|=v<<j
    return a

def make_strata(t,alpha,beta,c):
    strata=defaultdict(list)
    for b in range(1<<(2*t)):
        A=flags(b,t,alpha,beta,c)
        valid=all(A>>j&1 or not (b>>(2*j)&3) for j in range(t))
        v=(-1)**quadratic(b,t,alpha,beta,c)*(1<<(t-A.bit_count())) if valid else 0
        require(v==lifted_coefficient(t,alpha,beta,c,b),"stratum coefficient")
        if valid:strata[A].append(b)
    for A,P in strata.items():
        _,U=affine_basis(P)
        require(len(U)>=t+1-2*(t-A.bit_count()),"stratum dimension")
    return strata

def gauss(t,A,P,proj,r,alpha,beta,c,ell,const):
    p,U=affine_basis(P)
    K=list(Space(b^p for b in P if proj[b]==proj[p]))
    k=len(K)
    require(k==len(U)-len(Space(proj[b]^proj[p] for b in P)),"fibre dimension")
    Q=lambda b:quadratic(b,t,alpha,beta,c)
    rows=[sum((Q(x^y)^Q(x)^Q(y)^Q(0))<<j for j,y in enumerate(K)) for x in K]
    rank=len(Space(rows));require(rank%2==0,"even polar rank")
    h=rank//2;e=t-A.bit_count()+k-h
    sums=defaultdict(int)
    for b in P:sums[proj[b]^ell]+=(-1)**(Q(b)^const)
    nonzero={a:v for a,v in sums.items() if v}
    if not nonzero:return e,{},0
    require(all(abs(v)==1<<(k-h) for v in nonzero.values()),"Gauss magnitude")
    base,B=affine_basis(nonzero)
    require(len(B)>=t+1-2*e,"packet dimension")
    pts=[base^v for v in values(B)]
    phase=[int(nonzero[a]<0) for a in pts];co=anf(phase)
    require(all(not z or i.bit_count()<=2 for i,z in enumerate(co)),"quadratic sign")
    atoms=[{a for i,a in enumerate(pts) if i&mon==mon} for mon,z in enumerate(co) if z]
    require(len(atoms)<=1+r+comb(r,2),"phase atom cap")
    neg=set()
    for S in atoms:
        affine_basis(S);neg^=S
    require(neg=={a for a,v in nonzero.items() if v<0},"phase affine atoms")
    return e,{a:(-1 if v<0 else 1)*(1<<e) for a,v in nonzero.items()},len(atoms)

def bit_poly(vs,s):
    mask=(1<<(1+(1<<s)))-1;P=1
    for v in vs:
        for j in range(s+1):
            if v>>j&1:P=(P^(P<<(1<<j)))&mask
    return (P>>(1<<s))&1

def exercise():
    rng=Random(281126);stats=defaultdict(int)
    for t in range(1,7):
        for rep in range(12):
            alpha=[rng.randrange(1<<(j+1)) for j in range(t)]
            beta=[rng.randrange(1<<(j+1)) for j in range(t)]
            cs=range(1<<(t+1)) if t<=2 and rep<3 else [rng.randrange(1<<(t+1))]
            for c in cs:
                strata=make_strata(t,alpha,beta,c);bits=truth(t,alpha,beta,c)
                stats["lifts"]+=1;stats["strata"]+=len(strata)
                stats["lifted frequencies"]+=len(bits)
                for r in sorted({0,t,2*t,rng.randrange(2*t+1)}):
                    cols=[];B=Space()
                    while len(cols)<r:
                        z=rng.randrange(1<<(2*t))
                        if z not in B:B.add(z);cols.append(z)
                    proj=[sum(parity(b&v)<<i for i,v in enumerate(cols)) for b in range(len(bits))]
                    ell=rng.randrange(1<<r);const=rng.randrange(2)
                    rhs=[bits[x]^parity(i&ell)^const for i,x in enumerate(values(cols))]
                    W=walsh(rhs);packets=[]
                    for A,P in strata.items():
                        e,D,k=gauss(t,A,P,proj,r,alpha,beta,c,ell,const)
                        require(e>=t-A.bit_count(),"valuation depth")
                        packets.append((e,D,k));stats["Gauss packets"]+=1
                        if D:stats["nonzero packets"]+=1;stats["phase atoms"]+=k
                    Z=[0]*(1<<r)
                    for e,D,k in packets:
                        for a,v in D.items():Z[a]+=v
                    require(all(z*(1<<r)==w*(1<<t) for z,w in zip(Z,W)),"global packet sum")
                    stats["target coefficients"]+=len(Z)
                    s=min((abs(z)&-abs(z)).bit_length()-1 for z in Z if z)
                    require(0<=s<=t,"granularity slack")
                    O={i for i,z in enumerate(Z) if z>>s&1}
                    if s<=1:
                        F=[set(D) for e,D,k in packets if D and e<=s]
                        require(all(e==s for e,D,k in packets if D and e<=s),"no lower packet")
                        require(len(F)<= (1 if s==0 else t+1),"sharper parity packet count")
                        union=set()
                        for P in F:
                            _,U=affine_basis(P);require(len(U)>=t+1-2*s,"odd mask dimension")
                            union^=P
                        require(union==O,"exact parity sum")
                        stats["saturated or one-slack masks"]+=1
                    for j in range(min(t,3)+1):
                        for a,z in enumerate(Z):
                            vs=[D.get(a,0) for e,D,k in packets if e<=j]
                            require(bit_poly(vs,j)==(z>>j&1),"signed carry")
                            stats["bit carry checks"]+=1
                    if s<=3:
                        poly=[1]+[0]*(1<<s)
                        for e,D,k in packets:
                            if not D or e>s:continue
                            for j in range(e,s+1):
                                w=1<<j;n=1 if j==e else k
                                for i in range(1<<s,w-1,-1):
                                    poly[i]+=n*poly[i-w]
                        M=sum(comb(t,j) for j in range(min(t,s)+1))
                        bound=(1+(s+1)*M*(1+r+comb(r,2)))**(1<<s)
                        require(poly[-1]<=bound,"atom expansion bound")
                        stats["atom bound checks"]+=1
    print(dict(stats),flush=True)

def examples():
    for m in range(2,8):
        n=m+1;N=1<<n
        S=lambda u:int(u.bit_count()%3!=0)
        pi=[(y&(N//2-1))|(((y>>m)&S(y&(N//2-1)))<<m) for y in range(N)]
        bits=[parity(x&a) for a in pi for x in range(N)]
        W=walsh(bits)
        require(set(abs(w) for w in W)<= {0,N,2*N},"dyadic magnitudes")
        require(any(abs(w)==N for w in W),"exact gamma")
        require(all(weight(w//N)<=1 for w in W),"signed-digit test blind")
        support=[a for a,w in enumerate(W) if w]
        require(len(Space(a^support[0] for a in support))==2*n,"nonlinear dimension")
        O={a for a,w in enumerate(W) if (w//N)&1}
        require(all((a in O)==bool(S(a&(N//2-1))) for a in range(N*N)),"MOD3 odd mask")
        require({a for a in range(4) if a in O}=={1,2,3},"nonaffine slice")
        co=anf(bits)
        require(all(not b or i.bit_count()<=m+2 for i,b in enumerate(co)),"degree bound")
        print("MOD3 family m",m,"gamma",n,"D=1; odd mask nonaffine PASS",flush=True)

if __name__=="__main__":
    exercise();examples();print("PASS")
