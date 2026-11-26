"""Exact finite GF(2) replay of target ideal transport; no proof authority."""
from math import comb
from random import Random

class Space:
    def __init__(self, xs=()):
        self.p = {}
        for x in xs: self.add(x)
    def reduce(self, x):
        for i in sorted(self.p, reverse=True):
            if x >> i & 1: x ^= self.p[i]
        return x
    def add(self, x):
        x = self.reduce(x)
        if x: self.p[x.bit_length()-1] = x
    def __iter__(self): return iter(self.p.values())
    def __len__(self): return len(self.p)
    def __contains__(self, x): return self.reduce(x) == 0
    def equal(self, other): return len(self) == len(other) and all(x in other for x in self)

def kernel(S, fun):
    piv, out = {}, Space()
    for x in S:
        y, witness = fun(x), x
        while y:
            i = y.bit_length()-1
            if i not in piv: piv[i] = (y, witness); break
            a, b = piv[i]; y ^= a; witness ^= b
        if not y: out.add(witness)
    return out

def coords(n): return [sum(1 << a for a in range(1 << n) if a >> i & 1) for i in range(n)]
def affine(n): return Space([(1 << (1 << n))-1, *coords(n)])
def filt(V, n):
    F = [Space([(1 << (1 << n))-1])]
    for _ in range(n+1): F.append(Space([*F[-1], *(x & y for x in F[-1] for y in V)]))
    return [Space(), *F]  # index r+1

def quotient(U, L): return Space(L.reduce(x) for x in U)
def target(F, f, full): return [kernel(S, lambda x: x & (full ^ f)) for S in F]
def gen_profile(F, J, n):
    # A is generated in degree one; positive-degree products equal A_1 M_(r-1).
    return [len(J[r+1])-len(Space([*J[r], *(x&y for x in F[2] for y in J[r])])) for r in range(n+1)]
def check(n,V,u,v,f):
    full=(1<<(1<<n))-1; g=u&v; W=Space([*V,g]); F=filt(V,n); P=filt(W,n)
    J=target(F,f,full); L=target(P,f,full); defects=[]; checks=0
    for r in range(n+1):
        # K_r lives in the old grade r+1, represented modulo F_r.
        K=quotient(L[r+1],F[r+1]); qA=quotient(P[r+1],F[r+1]); M=quotient(J[r+2],F[r+1]);
        inter=kernel(qA,M.reduce); assert K.equal(inter)
        assert len(L[r+1])-len(J[r+1])==len(K)
        prev=len(L[r])-len(J[r]); assert len(L[r+1])-len(L[r])==len(J[r+1])-len(J[r])-prev+len(K)
        qM=Space(F[r+1].reduce(g&x) for x in J[r])
        assert all(x in K for x in qM); defects.append(len(K)-len(qM)); checks+=1
    return gen_profile(F,J,n),gen_profile(P,L,n),defects,checks

def draw(V,rng):
    x=0
    for a in V:
        if rng.getrandbits(1): x^=a
    return x

if __name__=='__main__':
    rng=Random(90210); gates=grades=0; V=affine(2); forms=[i for i in range(16) if i in V]
    for u in forms:
        for v in forms:
            for f in range(16):
                *_,c=check(2,V,u,v,f); gates+=1; grades+=c
    for _ in range(64):
        V=affine(4)
        for _ in range(4):
            u,v=draw(V,rng),draw(V,rng); f=rng.randrange(1<<16)
            *_,c=check(4,V,u,v,f); gates+=1; grades+=c; V=Space([*V,u&v])
    fixtures=[]
    for m in range(2,7):
        n=m+2; k=m//2; a,b,*z=coords(n); V=affine(n); full=(1<<(1<<n))-1
        f=sum(1<<x for x in range(1<<n) if x&3==3 and (x>>2).bit_count()>=k)
        p,q,d,c=check(n,V,a,b,f); assert p[k+2]==q[k+1]==comb(m,k) and sum(p)==sum(q)==comb(m,k)
        assert sum(d)==sum(comb(m,j) for j in range(k,m+1)); assert all(any(((f>>x)^(f>>(x^(1<<i))))&1 for x in range(1<<n)) for i in range(n))
        assert all(any(((f>>x)^(f>>(x^s)))&1 for x in range(1<<n)) for s in range(1,1<<n))
        fixtures.append((m,k,comb(m,k),sum(d))); gates+=1; grades+=c
    a,b,c,d=coords(4); V=Space([*affine(4),a&b,c&(a^d)]); F=filt(V,4)
    assert d in V and gen_profile(F,target(F,d,(1<<16)-1),4)==[0,1,2,0,0]
    # A genuine independent spectator must not create new minimal generators.
    a,b,c,d,e=coords(5); V=Space([*affine(5),a&b,c&(a^d)]); F=filt(V,5)
    assert gen_profile(F,target(F,d,(1<<32)-1),5)==[0,1,2,0,0,0]
    print('Completion counterexample and spectator profile: PASS')
    print('PASS:',gates,'target/gate cases;',grades,'graded transport checks; threshold fixtures (m,k,generators,defect dimension):',fixtures,'; seed 90210')
