#!/usr/bin/env python3
"""Exact integer replay of common Fourier lifts and fibre/digit constraints."""
from collections import Counter, deque
from functools import lru_cache
from random import Random
from target_ideal_replay import Space

def require(x,msg):
    if not x:raise AssertionError(msg)

def parity(x):return x.bit_count()&1

def walsh(bits):
    a=[1-2*b for b in bits];n=len(a);d=1
    while d<n:
        for i in range(0,n,2*d):
            for j in range(i,i+d):
                x,y=a[j],a[j+d];a[j],a[j+d]=x+y,x-y
        d*=2
    return a

@lru_cache(None)
def weight(z):
    z=abs(z)
    if z<=1:return z
    if not z&1:return weight(z//2)
    return 1+min(weight(z//2),weight(z//2+1))

def truth(t,alpha,beta,c):
    out=[]
    for x in range(1<<(2*t)):
        g=1 # bit zero is constant one
        for j in range(t):
            u=((x>>(2*j))&1)^parity(alpha[j]&g)
            v=((x>>(2*j+1))&1)^parity(beta[j]&g)
            g|=(u&v)<<(j+1)
        out.append(parity(c&g))
    return out

def lifted_coefficient(t,alpha,beta,c,freq):
    # Integer numerator with denominator 2^t (not 2^(2t)).
    sign=1;k=0
    for j in range(t-1,-1,-1):
        p=(freq>>(2*j))&1;q=(freq>>(2*j+1))&1
        if not c>>(j+1)&1:
            if p or q:return 0
            continue
        c ^= (1<<(j+1)) ^ (alpha[j] if p else 0) ^ (beta[j] if q else 0)
        if p&q:sign=-sign
        k+=1
    if c&1:sign=-sign
    return sign*(1<<(t-k))

def digit_check():
    # Independent shortest paths on a finite signed-power addition graph.
    # A finite graph gives an upper bound on unrestricted minimum weight;
    # the recursion itself supplies explicit signed representations.
    d={0:0};q=deque([0]);powers=[1<<i for i in range(10)]
    while q:
        a=q.popleft()
        for p in powers:
            for b in (a+p,a-p):
                if -512<=b<=512 and b not in d:d[b]=d[a]+1;q.append(b)
    require(all(d[z]==weight(z) for z in range(-255,256)),"signed digit BFS")
    for s in range(1,129):
        k=(4**s-1)//3
        require(weight(k)==s and weight(k<<17)==s,"alternating digit family")
    print("signed-digit BFS",511,"alternating digit checks",128,flush=True)

def lift_checks():
    rng=Random(281126);lifts=coeffs=fibres=joint=0
    for t in range(0,7):
        for rep in range(12):
            a=[rng.randrange(1<<(j+1)) for j in range(t)]
            b=[rng.randrange(1<<(j+1)) for j in range(t)]
            masks=list(range(1<<(t+1))) if t<=2 and rep<3 else [rng.randrange(1<<(t+1))]
            for c in masks:
                bits=truth(t,a,b,c);N=len(bits)
                direct=walsh(bits)
                actual=[lifted_coefficient(t,a,b,c,i) for i in range(N)]
                require(all(v*(1<<t)==w for v,w in zip(actual,direct)),"exact common recursion")
                require(sum(v*v for v in actual)==1<<(2*t),"Parseval")
                require(all(not v or abs(v)&(abs(v)-1)==0 for v in actual),"dyadic spectrum")
                coeffs+=N;lifts+=1
                for r in sorted({0,t,2*t,rng.randrange(2*t+1)}):
                    # Draw full-column-rank maps, including arbitrary cross-pair correlations.
                    cols=[];S=Space()
                    while len(cols)<r:
                        z=rng.randrange(N)
                        if z not in S:S.add(z);cols.append(z)
                    image=[0]
                    for col in cols:image += [z^col for z in image]
                    rhs=[bits[z] for z in image]
                    # A free affine output shifts frequencies and signs.
                    ell=rng.randrange(1<<r);const=rng.randrange(2)
                    rhs=[v^parity(ell&x)^const for x,v in enumerate(rhs)]
                    got=walsh(rhs);merged=[0]*(1<<r);sizes=[0]*(1<<r);counts=[0]*(1<<r)
                    for freq,w in enumerate(actual):
                        idx=sum(parity(freq&z)<<i for i,z in enumerate(cols))^ell
                        merged[idx]+=(-1 if const else 1)*w
                        sizes[idx]+=1;counts[idx]+=int(w!=0)
                    require(all(v*(1<<r)==w*(1<<t) for v,w in zip(merged,got)),"fibre identity")
                    require(all(s==1<<(2*t-r) for s in sizes),"parallel fibre sizes")
                    require(all(weight(v)<=k for v,k in zip(merged,counts)),"digit capacity")
                    support=[i for i,w in enumerate(got) if w]
                    rd=len(Space(i^support[0] for i in support))
                    require(rd<=r,"nonlinear dimension")
                    if r<=6:
                        structures=sum(all((rhs[x]^rhs[x^u])==(rhs[0]^rhs[u]) for x in range(1<<r)) for u in range(1<<r))
                        require(structures==1<<(r-rd),"Fourier support dimension identity")
                        joint+=1
                    require(all(weight(v)<=1<<(2*t-rd) for v in merged),"intrinsic digit capacity")
                    fibres+=len(merged)
    print("lifted outputs",lifts,"Walsh coefficients",coeffs,"fibre sums",fibres,
          "direct linearity checks",joint,flush=True)

def pi_table(m):
    k=(4**(m//2)-1)//3
    p=[0]*k+[2,3]
    for i in range(2,m):p.extend([1<<i]*2)
    p.extend([1]*((1<<m)-len(p)))
    return k,p

def examples():
    for m in (4,6,8,10,12,14):
        k,p=pi_table(m)
        require(len(p)==1<<m and p.count(0)==k,"zero fibre")
        require(all(1<<i in p for i in range(m)),"basis image")
        require(all(sum(v>>i&1 for v in p)%2==0 for i in range(m)),
                "degree parity")
        require(weight(k)==m//2,"digit improvement")
        if m<=8:
            # Independent full scalar truth table and Walsh transform.
            bits=[parity(x&z) for z in p for x in range(1<<m)]
            W=walsh(bits)
            require(W[0]==k*(1<<m) and all(v%(1<<m)==0 for v in W),"exact granularity")
            # Affine hull of support gives r=2m independently of period proof.
            support=[i for i,v in enumerate(W) if v]
            require(len(Space(i^support[0] for i in support))==2*m,"full nonlinear dimension")
            # Degree via Mobius transform.
            anf=bits[:]
            for j in range(2*m):
                for x in range(1<<(2*m)):
                    if x>>j&1:anf[x]^=anf[x^(1<<j)]
            require(max(i.bit_count() for i,z in enumerate(anf) if z)<=m,"degree bound")
        gap=0
        while 4**gap<m//2:gap+=1
        print("explicit family",m,"zero fibre",k,"new floor",m+gap,"baseline",m,flush=True)

if __name__=="__main__":
    digit_check();lift_checks();examples();print("PASS")
