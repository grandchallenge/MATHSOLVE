#!/usr/bin/env python3
"""Exact finite replay of relative Rees relation births and compositions."""
from itertools import product, combinations
from math import comb
from random import Random
from target_ideal_replay import Space, affine, coords, filt, target, kernel, quotient, draw

def require(ok, msg):
    if not ok:
        raise AssertionError(msg)

def mul(U,V):
    return Space(a&b for a in U for b in V)

def add(*spaces):
    return Space(x for S in spaces for x in S)

def subset(U,V):
    return all(x in V for x in U)

def inter(U,V):
    return kernel(U,V.reduce)

def ext(L,F,r):
    # Unrestricted homogeneous ideal extension, independent of one-gate formula.
    return add(*(mul(L[d+1],F[r-d+1]) for d in range(r+1)))

def data(n,states,fs,f):
    full=(1<<(1<<n))-1
    return [[target(F,s,full) for s in (full^f,f)] for F in fs]

def beta(L,base,V,r):
    den=add(base,mul(V,L[r]))
    require(subset(den,L[r+1]),"generator denominator")
    return len(L[r+1])-len(den)

def one_step(n,F,G,V,W,g,L,M):
    grades=gen=action=nonzero=0
    for r in range(n+1):
        I=add(L[r+1],mul(Space([g]),L[r]))
        require(I.equal(ext(L,G,r)),"one-step inherited ideal")
        require(subset(I,M[r+1]),"quotient defined")
        require(subset(M[r+1],L[r+2]),"z kills quotient")
        K=quotient(M[r+1],F[r+1])
        P=quotient(G[r+1],F[r+1])
        T=quotient(L[r+2],F[r+1])
        require(K.equal(inter(P,T)),"leading symbol intersection")
        qM=Space(F[r+1].reduce(g&a) for a in L[r])
        require(subset(qM,K),"q times old relation")
        require(len(M[r+1])-len(I)==len(K)-len(qM),"Tor dimension")
        b=beta(M,I,W,r)
        require(b>=0,"minimal quotient")
        gen+=b
        if r<n:
            I_next=ext(L,G,r+1)
            require(subset(mul(Space([g]),I),I_next),"t action descends")
            require(subset(mul(Space([g]),M[r+1]),M[r+2]),"t action target")
            I_next2=ext(L,G,r+2)
            require(subset(mul(Space([g]),M[r+1]),I_next2),"t squared zero")
            rank=len(add(I_next,mul(Space([g]),M[r+1])))-len(I_next)
            nonzero+=rank>0
            action+=1
        grades+=1
    return grades,gen,action,nonzero

def composite(n,states,fs,ls):
    F,G,H=fs
    L,M,N=ls
    W=states[2]
    grades=lost=0
    profiles=[[],[],[]]
    for r in range(n+1):
        I=ext(L,H,r);J=ext(M,H,r)
        require(subset(I,J) and subset(J,N[r+1]),"nested ideals")
        # Identify multiplication image using the smaller one-step quotient.
        induced=add(I,*(mul(M[d+1],H[r-d+1]) for d in range(r+1)))
        require(induced.equal(J),"base-change image")
        require(len(N[r+1])-len(I)==len(J)-len(I)+len(N[r+1])-len(J),"exactness")
        require(subset(N[r+1],L[min(r+3,len(L)-1)]),"two-step z torsion")
        B=add(I,mul(W,N[r]))
        C=add(J,mul(W,N[r]))
        require(add(B,J).equal(C),"minimal generator cokernel")
        d0=len(N[r+1])-len(B); d1=len(N[r+1])-len(C)
        rank=len(C)-len(B)
        require(d0==rank+d1,"minimal generator sequence")
        lost+=len(J)-len(I)-rank
        profiles[0].append(beta(M,ext(L,G,r),states[1],r))
        profiles[1].append(beta(N,J,W,r))
        profiles[2].append(beta(N,I,W,r))
        grades+=1
    return grades,lost,profiles

def run_case(n,V,g,h,f):
    W=add(V,Space([g])); Z=add(W,Space([h]))
    states=[V,W,Z];fs=[filt(U,n) for U in states]
    ls=data(n,states,fs,f)
    totals=[0]*6;profiles=[]
    for e in (0,1):
        L,M,N=[l[e] for l in ls]
        for F,G,U,T,p,A,B in ((fs[0],fs[1],V,W,g,L,M),(fs[1],fs[2],W,Z,h,M,N)):
            grades,gen,act,nz=one_step(n,F,G,U,T,p,A,B)
            for j,x in enumerate((grades,gen,act,nz)):totals[j]+=x
        grades,lost,p=composite(n,states,fs,(L,M,N))
        totals[4]+=grades;totals[5]+=lost;profiles.append(p)
    return totals,profiles

def fixtures():
    checks=0
    # Direct truth-space replay of the two-gate threshold family.
    for m in (2,3):
        n=m+4;k=m//2; a,b,c,d,*xs=coords(n); f=sum(1<<i for i in range(1<<n)
                    if i&15==15 and (i>>4).bit_count()>=k)
        V=affine(n);g=a&b;h=c&d
        W=add(V,Space([g]));Z=add(W,Space([h]))
        states=[V,W,Z];fs=[filt(U,n) for U in states]
        L,M,N=[target(F,f,(1<<(1<<n))-1) for F in fs]
        require(f not in Z,"incomplete target")
        for r in range(n+1):
            I=ext(L,fs[2],r);J=ext(M,fs[2],r)
            require(I.equal(L[r+1]) and J.equal(M[r+1]),"support extension")
            require(add(I,N[r]).equal(J),"first image equals zQ")
            checks+=1
        _,_,ps=composite(n,states,fs,(L,M,N))
        expected=comb(m,k)
        require(all(sum(p)==expected for p in ps),"threshold beta")
        require(ps[0][k+3]==ps[1][k+2]==ps[2][k+2]==expected,"threshold grade")
        print("truth-space threshold",m,k,expected,flush=True)
    # Independent explicit monomial cover census (no truth-space elimination).
    for m in range(2,13):
        k=m//2;n=m+4
        support=[15|(s<<4) for s in range(1<<m) if s.bit_count()>=k]
        for i,j in ((0,1),(1,2),(0,2)):
            classes={(s,r) for s in support for r in range(s.bit_count()-j,s.bit_count()-i)}
            # Every available degree-one generator acts by union of supports.
            features=[0,*[1<<l for l in range(n)],*[3,12][:j]]
            generated={(s|a,r+1) for s,r in classes for a in features}&classes
            mins=classes-generated
            require(len(mins)==comb(m,k) and all(r==4+k-j for s,r in mins),"monomial minimal births")
            if i==0 and j==2:
                first={(s,s.bit_count()-1) for s in support}
                require(first==({(s,r+1) for s,r in classes}&classes),"composite image")
                require(first<=generated,"first image erased on generators")
            checks+=1
    return checks

def nonzero_action_fixture():
    n=4;V=affine(n)
    for u,v in ((52275,61455),(38313,22938),(30702,26985)):
        require(u in V and v in V,"legal history")
        V=add(V,Space([u&v]))
    u,v=6838,50115
    require(u in V and v in V,"legal final gate")
    g=u&v;require(g==0x282,"gate identity")
    W=add(V,Space([g]));F,G=filt(V,n),filt(W,n)
    f=0xf853;full=65535;s=full^f
    L,M=target(F,s,full),target(G,s,full)
    a=0x58c
    require(a in M[2] and a not in ext(L,G,1),"live class")
    require(a&g==0x80 and a&g not in ext(L,G,2),"nonzero new-feature action")
    # Verify the explicit symbol action: a=b+gc and q[b] represents ga.
    b=a^g
    require(b in F[2],"adapted decomposition")
    require(F[3].reduce(g&b)==F[3].reduce(g&a),"symbol action")
    # Spectator profile: add one unused bit to the full history.
    def lift(x):return x|(x<<16)
    V5=add(Space(lift(x) for x in V),Space([coords(5)[4]]))
    W5=add(V5,Space([lift(g)]));F5,G5=filt(V5,5),filt(W5,5)
    L5,M5=target(F5,lift(s),(1<<32)-1),target(G5,lift(s),(1<<32)-1)
    ps=[beta(M,ext(L,G,r),W,r) for r in range(n+1)]
    pt=[beta(M5,ext(L5,G5,r),W5,r) for r in range(n+2)]
    require(pt==ps+[0],"spectator minimal profile")
    print("nonzero t-action and spectator fixture PASS",ps,pt)

def wedge(a,b):
    r=0
    while a:
        x=a&-a;a^=x;i=x.bit_length()-1
        c=b
        while c:
            y=c&-c;c^=y;j=y.bit_length()-1
            if not i&j:r^=1<<(i|j)
    return r

def linear(x,n):
    return sum(1<<(1<<i) for i in range(n) if x>>i&1)

def shared_factor_replay():
    rng=Random(271127);checks=families=0
    for n in (3,4,5,6):
        # All two-plane labels, unique in characteristic two.
        ls=[linear(i,n) for i in range(1,1<<n)]
        labels={}
        for i,u in enumerate(ls):
            for v in ls[i+1:]:
                labels.setdefault(wedge(u,v),(u,v))
        require(len(labels)==((2**n-1)*(2**n-2))//6,"plane count")
        hs=[]
        for _ in range(18 if n<6 else 5):
            fam=[]
            for j in range(rng.randrange(1,4)):
                d=rng.randrange(2,n+1)
                mons=[i for i in range(1<<n) if i.bit_count()==d]
                h=0
                for i in mons:
                    if rng.getrandbits(1):h^=1<<i
                if not h:h=1<<mons[0]
                fam.append((d,h))
            hs.append(fam)
        # A threshold family on four distinguished bits, m=n-4.
        if n==6:hs.append([(5,1<<(15|16)),(5,1<<(15|32))])
        for fam in hs:
            D=Space(w for w in ls if all(not wedge(w,h) for d,h in fam))
            d0=len(D);count=0
            for q,(u,v) in labels.items():
                annih=u in D and v in D
                images={d:Space(wedge(q,1<<i) for i in range(1<<n) if i.bit_count()==d-2)
                        for d in set(d for d,h in fam)}
                div=all(h in images[d] for d,h in fam)
                require(div==annih,"common exterior divisor")
                count+=div;checks+=1
            require(count==((2**d0-1)*(2**d0-2))//6,"compatible count")
            families+=1
        if n==6:require(d0==4 and count==35,"threshold common factor")
    # Nonlinear state: all grade-three symbols vanish, but q does not divide h.
    a,b,c=coords(3);V=add(affine(3),Space([a&b]));F=filt(V,3)
    q=a&c;h=b&c;W=add(V,Space([q]))
    require(q not in V and h not in W,"nonlinear nonpromotion")
    require((a&h) in F[3] and (c&h) in F[3],"annihilation in grade three")
    require(len(F[3])==8,"saturated quadratic space")
    print("shared-factor families",families,"plane comparisons",checks,
          "35 threshold labels; nonlinear annihilator counterexample PASS")

def main():
    rng=Random(261127);totals=[0]*6;cases=0
    n=2;V=affine(n);vs=[i for i in range(16) if i in V]
    gs=sorted({u&v for u,v in product(vs,repeat=2)})
    for g in gs:
        W=add(V,Space([g]));ws=[i for i in range(16) if i in W]
        hs=sorted({u&v for u,v in product(ws,repeat=2)})
        for h in hs:
            for f in range(16):
                t,_=run_case(n,V,g,h,f)
                totals=[a+b for a,b in zip(totals,t)];cases+=1
    for n in (3,4):
        for _ in range(40):
            V=affine(n)
            for j in range(2):
                V=add(V,Space([draw(V,rng)&draw(V,rng)]))
            g=draw(V,rng)&draw(V,rng);W=add(V,Space([g]))
            h=draw(W,rng)&draw(W,rng);f=rng.randrange(1<<(1<<n))
            t,_=run_case(n,V,g,h,f)
            totals=[a+b for a,b in zip(totals,t)];cases+=1
    print("composition histories",cases,"counts (one-step grades, minimal births, t-actions, nonzero t-actions, composite grades, erased image dimensions)",totals,flush=True)
    print("threshold checks",fixtures(),"PASS")
    nonzero_action_fixture()
    shared_factor_replay()

if __name__=="__main__":
    main()
