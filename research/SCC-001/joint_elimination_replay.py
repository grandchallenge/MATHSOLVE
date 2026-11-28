"""Exact finite replay: joint fixed-witness elimination and atom-closure transfer."""
from collections import Counter

def dot(a,b): return (a&b).bit_count()&1

def basis(xs):
    piv={}
    for x in xs:
        while x:
            i=x.bit_length()-1
            if i not in piv: piv[i]=x; break
            x^=piv[i]
    return tuple(piv.values())

def space(bs):
    s={0}
    for b in bs:s|={a^b for a in s}
    return tuple(sorted(s))

def coordinates(n):return tuple(sum(((p>>i)&1)<<p for p in range(1<<n)) for i in range(n))

def filtration(n,V):
    F=[((1<<(1<<n))-1,)]
    for _ in range(n):F.append(basis([*F[-1],*(a&b for a in F[-1] for b in V)]))
    assert len(F[-1])==1<<n
    return F

def level(F,l):return next(d for d,b in enumerate(F) if any(dot(l,a) for a in b))

def active(n,V,L):
    F=filtration(n,V);live=[(l,level(F,l)) for l in L if not any(dot(l,v) for v in V)]
    P=sum((1<<(d-1))-1 for l,d in live)
    forms=space(V);freq=Counter(u&v for u in forms for v in forms)
    scores={};totals={l:0 for l,d in live}
    for g,m in freq.items():
        saving=0
        for l,d in live:
            if any(dot(l,g&w) for w in F[d-2]):
                totals[l]+=m;saving+=1<<(d-2)
        scores[g]=saving
    den=len(forms)**2
    assert all(8*total>=3*den for total in totals.values())
    assert 16*sum(freq[g]*s for g,s in scores.items())>=3*den*P
    g=max(scores,key=scores.get);W=basis([*V,g]);F1=filtration(n,W)
    assert P-scores[g]==sum((1<<(level(F1,l)-1))-1 for l in L)
    return W,len(live),P,len(freq),len(live)*len(freq)

def target_trials():
    steps=checks=cases=0
    for n in (2,3):
        M=(1<<(1<<n))-1;V0=basis([M,*coordinates(n)])
        all_live=[l for l in range(1,M+1) if all(not dot(l,v) for v in V0)]
        for f in range(M+1):
            L=[l for l in all_live if dot(l,f)]
            if n==3 and f%7:continue
            V=V0;P0=None
            while True:
                W,c,P,g,comparisons=active(n,V,L)
                checks+=comparisons
                if P0 is not None:assert 16*P<=13*P0
                if not c:break
                assert len(W)>len(V);P0=P;V=W;steps+=1
            assert f in space(V);cases+=1
    # A sparse family can disappear without computing its target.
    n=3;M=255; a,b,c=coordinates(n);V=basis([M,a,b,c,a&b,a&c,b&c]);f=a&b&c
    assert f not in space(V)
    live=[l for l in range(1,256) if dot(l,f) and all(not dot(l,v) for v in V)]
    assert live==[255]
    print('PASS target-complete greedy cases',cases,'charged steps',steps,'witness/gate comparisons',checks,'sparse false-completion live',live)

def closure_tests():
    n=2;k=4;M=15; a,b=coordinates(n);V0=basis([M,a,b]);W0=basis([*(v|(v<<k) for v in V0),M<<k]);Wfull=basis([*(v|(v<<k) for v in basis([M,a,b,a&b])),M<<k])
    def atoms(W):
        A={255}
        for v in space(W):A|={v&t for t in A}
        return A
    def witnesses(S,p,W):
        return [l for l in range(1,256) if l&p and not l&~(S|p) and all(not dot(l,w) for w in W)]
    A0=atoms(W0);Afull=atoms(Wfull);checks=target_checks=0
    for S in range(1,256):
        obs=[l for j in range(8) if not S>>j&1 for l in witnesses(S,1<<j,W0)]
        projected={(l&M)^(l>>k) for l in obs}
        assert (not obs)==(S in A0)
        assert (0 not in projected)==(S in Afull)
        for f in range(16):
            W=basis([*W0,f|(f<<k)]);actual=S in atoms(W)
            assert actual==all(dot(l,f) for l in projected);target_checks+=1
        checks+=1
    print('PASS support-closure witness cases',checks,'arbitrary one-feature transfers',target_checks)

if __name__=='__main__':
    if not __debug__:raise RuntimeError('assertions required')
    target_trials();closure_tests()
