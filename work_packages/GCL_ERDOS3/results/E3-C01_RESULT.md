GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-C01-IA-001
assignment: E3-C01
agent_ref: INDEPENDENT-AGENT-E3-C01-001
disposition: FINITE_PATTERN_DISCOVERED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY

## Strongest exact statement

I found two exact finite/model statements and one sharply checked finite obstruction.

1. **Exact sparse dual for the raw cross-fiber LP, and an exact description of its failure mode.**  
   Let (H^	imes_{m,N}) be the hypergraph of 4-term APs in ([0,mN)) that meet more than one consecutive length-(N) fiber, and consider
   [
   max sum_{i,u}x_{i,u}
   ]
   subject to every cross-AP inequality (sum_{vin e}x_vle 3), fiber caps (sum_u x_{i,u}le r_4(N)), and (0le xle1). For both required values (min{4,8}),
   [
   operatorname{LP}^{	imes}_{m,N}
   =min!left{m,r_4(N),rac34 mNight}.
   ]
   This is not a finite-data extrapolation: the identity has a direct primal/dual proof. The fiber caps give the first upper bound. For (m=4), summing the (N) vertical AP inequalities
   [
   (u,N+u,2N+u,3N+u),qquad 0le u<N,
   ]
   gives (|A|le3N). For (m=8), summing the (2N) disjoint vertical AP inequalities
   [
   (u,2N+u,4N+u,6N+u),qquad
   (N+u,3N+u,5N+u,7N+u)
   ]
   gives (|A|le6N). Conversely the uniform fractional assignment
   [
   x_{i,u}=t:=min{r_4(N)/N,3/4}
   ]
   satisfies every cross-AP inequality and every fiber cap, attaining the minimum above. Thus this vertex LP can never detect any gluing loss beyond the two obvious caps; all additional exact loss seen below is integral/configurational.

2. **Exact gluing values on the tested range.**  
   Independent exhaustive subset enumeration gives
   [
   (r_4(1),ldots,r_4(16))
   =(1,2,3,3,4,5,5,6,7,8,8,8,9,9,10,10).
   ]
   Exact optimization plus an independent exact hitting-set decision replay gives
   [
   r_4(20)=12,quad r_4(24)=14,quad r_4(28)=17,quad r_4(32)=18.
   ]
   Hence, for the required blockings:

   | (m) | (N) | (r_4(N)) | (r_4(mN)) | (G_m(N)=m r_4(N)-r_4(mN)) | deficits of recorded global extremizer | first feasible uniform deficit (d_0) | max size with all fibers (ge r_4(N)-d_0) | first deficit admitting a global extremizer | raw cross-LP |
   |---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
   |4|2|2|6|2|[0,1,0,1]|1|6|1|6|
   |4|3|3|8|4|[0,1,1,2]|1|8|1|9|
   |4|4|3|10|2|[0,0,1,1]|1|10|1|12|
   |4|5|4|12|4|[1,0,3,0]|1|12|1|15|
   |4|6|5|14|6|[1,3,0,2]|2|14|2|18|
   |4|7|5|17|3|[0,1,2,0]|1|16|2|20|
   |4|8|6|18|6|[0,4,2,0]|2|18|2|24|
   |8|2|2|10|6|[0,1,1,0,1,1,1,1]|1|10|1|12|
   |8|3|3|14|10|[1,1,1,3,0,1,3,0]|2|14|2|18|
   |8|4|3|18|6|[0,0,2,2,0,2,0,0]|1|17|2|24|

   Here
   [
   d_0=leftlceil G_m(N)/mightceil
   ]
   in every tested case. The lower bound on (d_0) is just total cardinality, and a witness at (d_0) was found in every case.

3. **Finite defect-localization obstruction at ((m,N)=(4,7)).**  
   Although (G_4(7)=3), so the average fiber deficit is only (3/4), no 17-point global extremizer can have every fiber within deficit (1) of (r_4(7)=5). Equivalently, the conditioned optimum under (|A_i|ge4) for all four fibers is exactly (16), while (r_4(28)=17); every 17-point extremizer must place deficit at least (2) in some fiber. This was checked independently of the MIP by enumerating all locally admissible ((5,4,4,4)) fiber profiles: there are 9 AP-free 5-subsets and 30 AP-free 4-subsets of ([0,7)), so all
   [
   4cdot 9cdot 30^3=972{,}000
   ]
   translated configurations were checked, and none is globally 4-AP-free. A balanced 16-point witness exists, so the conditioned optimum is exactly 16.

A second instance shows the same qualitative concentration numerically/exact-MIP: for ((m,N)=(8,4)), (r_4(32)=18), but the maximum with all eight fibers of size at least (2) is (17); a global extremizer requires some fiber deficit (2).

No statement above is extrapolated to large (N), and none proves the protected density-loss frontier.

## Derivation / evidence

### Exact global witnesses

The following 0-based sets are 4-AP-free and have the certified optimum cardinalities:

- (r_4(8)=6): ({0,1,2,4,5,7}).
- (r_4(12)=8): ({0,1,2,4,5,7,8,9}).
- (r_4(16)=10): ({0,1,3,4,6,7,8,11,13,14}).
- (r_4(20)=12): ({0,1,4,5,6,8,9,11,15,17,18,19}).
- (r_4(24)=14): ({0,1,3,5,6,8,12,13,14,16,17,21,22,23}).
- (r_4(28)=17): ({0,1,2,4,5,7,11,12,13,15,16,20,22,23,25,26,27}).
- (r_4(32)=18): ({0,1,2,5,6,7,9,15,16,17,19,22,24,26,27,29,30,31}).

For (n=1,dots,16), all (2^n) subsets were directly checked. For (n=20,24,28,32), the lower bound is the displayed witness and the upper bound was independently replayed as an exact hitting-set decision problem: a complement of an AP-free set must hit every 4-AP. To prove (r_4(n)le R), I exhaustively proved that no hitting set of size at most (n-R-1) exists. The exact decision searches visited 1,606 states for ((20,R=12)), 13,902 for ((24,14)), 19,686 for ((28,17)), and 626,633 for ((32,18)); the same check at ((16,10)) visited 279 states.

### Conditioned witnesses at the first cardinality-possible deficit

These witnesses satisfy (|A_i|ge r_4(N)-d_0); each line is also directly rechecked for absence of 4-APs.

- ((4,2),d_0=1): ({0,1,2,5,6,7}), fiber sizes ([2,1,1,2]), size 6.
- ((4,3),d_0=1): ({0,1,4,5,6,8,9,11}), fiber sizes ([2,2,2,2]), size 8.
- ((4,4),d_0=1): ({0,1,2,6,7,8,10,11,13,15}), fiber sizes ([3,2,3,2]), size 10.
- ((4,5),d_0=1): ({0,2,3,5,6,8,12,13,14,16,17,19}), fiber sizes ([3,3,3,3]), size 12.
- ((4,6),d_0=2): ({0,2,3,5,6,7,11,12,14,16,19,20,22,23}), fiber sizes ([4,3,3,4]), size 14.
- ((4,7),d_0=1): ({0,1,2,5,7,11,12,13,15,16,18,20,23,25,26,27}), fiber sizes ([4,4,4,4]), size 16.
- ((4,8),d_0=2): ({2,4,5,7,8,9,13,15,16,18,19,20,24,26,27,29,30,31}), fiber sizes ([4,4,4,6]), size 18.
- ((8,2),d_0=1): ({0,2,3,4,7,9,10,12,14,15}), fiber sizes ([1,2,1,1,1,1,1,2]), size 10.
- ((8,3),d_0=2): ({0,1,2,5,6,7,9,14,15,18,19,20,22,23}), fiber sizes ([3,1,2,1,1,1,3,2]), size 14.
- ((8,4),d_0=1): ({1,2,4,5,8,9,12,14,17,18,21,23,24,26,28,29,31}), fiber sizes ([2,2,2,2,2,2,2,3]), size 17.

For all instances except ((4,7)) and ((8,4)), the first feasible deficit already admits a global extremizer. At those two instances the global optimum forces an additional one-unit concentration in at least one fiber.

### Digit/carry hypergraph

Every progression was generated exactly as
[
(a,a+d,a+2d,a+3d),qquad dge1,quad a+3d<mN,
]
then mapped to vertices ((i_t,u_t)) by (a+td=i_tN+u_t). Equivalently, writing (a=iN+u) and (d=qN+v), the block sequence is
[
i_t=i+tq+leftlfloorrac{u+tv}{N}ightfloor,
]
with residue ((u+tv)mod N). The numbers of cross-fiber hyperedges in the tested instances were respectively
[
7,18,31,49,72,97,127
]
for (m=4,N=2,ldots,8), and
[
35,84,147
]
for (m=8,N=2,3,4).

The exact LP identity in the first section shows that all nonvertical carry constraints are redundant at the optimum of this *fractional vertex relaxation*. This does **not** say they are combinatorially redundant: the integer optima are often much smaller, and the ((4,7)) conditioned obstruction is a direct example.

### Replay code / pseudocode

The following is sufficient to replay the exact model. The exhaustive (nle16) loop is run before any solver-dependent measurement.

```python
import itertools, math
import numpy as np
from functools import lru_cache
from scipy.optimize import milp, linprog, LinearConstraint, Bounds
from scipy.sparse import lil_matrix

def aps(n):
    return [(a,a+d,a+2*d,a+3*d)
            for d in range(1,(n-1)//3+1)
            for a in range(n-3*d)]

def apfree(S,n):
    s=set(S)
    return all(not all(v in s for v in e) for e in aps(n))

def brute_r4(n):
    E=[sum(1<<v for v in e) for e in aps(n)]
    best=-1; W=0
    for s in range(1<<n):
        if s.bit_count() <= best: continue
        if all((s&e)!=e for e in E):
            best=s.bit_count(); W=s
    return best,[i for i in range(n) if (W>>i)&1]

# Run this first:
assert [brute_r4(n)[0] for n in range(1,17)] ==        [1,2,3,3,4,5,5,6,7,8,8,8,9,9,10,10]

# Exact upper-bound decision:
# a hitting set B intersects every AP; AP-free A is its complement.
def hitting_set_exists_leq(n,k):
    E=[sum(1<<v for v in e) for e in aps(n)]
    @lru_cache(None)
    def dfs(deleted,krem):
        unc=[e for e in E if not (e & deleted)]
        if not unc: return True
        if krem <= 0: return False

        # safe lower bound: pairwise-disjoint uncovered APs
        used=0; pack=0
        for e in unc:
            if not (e & used):
                used |= e; pack += 1
        if pack > krem: return False

        deg=[0]*n
        for e in unc:
            z=e
            while z:
                b=z & -z; v=b.bit_length()-1
                deg[v]+=1; z-=b
        e=max(unc,key=lambda q:sum(deg[v] for v in range(n) if (q>>v)&1))
        vs=sorted((v for v in range(n) if (e>>v)&1), key=lambda v:-deg[v])
        return any(dfs(deleted|(1<<v),krem-1) for v in vs)
    return dfs(0,k)

# Example exact upper certificate:
# r4(28) >= 17 from the displayed witness, and:
assert not hitting_set_exists_leq(28,10)  # no complement of size <=10
# hence r4(28) <= 17.

def milp_max(n,m=None,N=None,floor_per_fiber=None):
    E=aps(n); extra=0 if floor_per_fiber is None else m
    A=lil_matrix((len(E)+extra,n)); lo=[]; hi=[]
    for j,e in enumerate(E):
        for v in e: A[j,v]=1
        lo.append(-np.inf); hi.append(3)
    if floor_per_fiber is not None:
        for i in range(m):
            for v in range(i*N,(i+1)*N): A[len(E)+i,v]=1
            lo.append(floor_per_fiber); hi.append(np.inf)
    r=milp(c=-np.ones(n), integrality=np.ones(n),
           bounds=Bounds(np.zeros(n),np.ones(n)),
           constraints=LinearConstraint(A.tocsr(),lo,hi),
           options={"mip_rel_gap":0.0})
    x=np.rint(r.x).astype(int)
    W=[i for i,z in enumerate(x) if z]
    assert apfree(W,n)
    return int(round(-r.fun)),W

def cross_lp(m,N,rN):
    n=m*N
    cross=[e for e in aps(n) if len({v//N for v in e})>1]
    A=lil_matrix((len(cross)+m,n)); b=[]
    for j,e in enumerate(cross):
        for v in e: A[j,v]=1
        b.append(3)
    for i in range(m):
        for v in range(i*N,(i+1)*N): A[len(cross)+i,v]=1
        b.append(rN)
    r=linprog(c=-np.ones(n), A_ub=A.tocsr(), b_ub=b,
              bounds=[(0,1)]*n, method="highs")
    return -r.fun

# Independent (4,7) balanced-extremizer check:
P4=[c for c in itertools.combinations(range(7),4) if apfree(c,7)]
P5=[c for c in itertools.combinations(range(7),5) if apfree(c,7)]
checked=0
for pos5 in range(4):
    pools=[P5 if i==pos5 else P4 for i in range(4)]
    for pats in itertools.product(*pools):
        checked += 1
        S=[i*7+u for i,p in enumerate(pats) for u in p]
        assert not apfree(S,28)
assert checked == 972000
```

Software identity: Python 3.13.5; SciPy 1.17.0; `scipy.optimize.milp` and `linprog(method="highs")`, using SciPy's HiGHS backend. Integer optima were requested with zero relative MIP gap; all reported witnesses were separately checked by integer AP enumeration, and the main global upper bounds were independently replayed by the exact hitting-set search above rather than accepted solely from solver status.

### Diagnostic density-loss ratios

Only dyadic instances were used. With (D_{L,n}=a_n-a_{n+L}), the observed exact values are:

- (L=2,n=1): (a_n=1, a_{n+L}=3/4, D=1/4).
- (L=2,n=2): (a_n=3/4, a_{n+L}=5/8, D=1/8).
- (L=2,n=3): (a_n=3/4, a_{n+L}=9/16, D=3/16).
- (L=3,n=1): (a_n=1, a_{n+L}=5/8, D=3/8).
- (L=3,n=2): (a_n=3/4, a_{n+L}=9/16, D=3/16).

For (	heta=1/4,1/2,3/4), the ratios (D/a_n^{1+	heta}) on the three (L=2) samples are respectively
[
(0.25,0.25,0.25),quad
(0.179095,0.192450,0.206801),quad
(0.268642,0.288675,0.310202).
]
The two (L=3) samples give
[
(0.375,0.375,0.375),quad
(0.268642,0.288675,0.310202).
]
These are diagnostics only. They do not support promotion of any exponent.

## Adversarial checks

- **Indexing:** all sets are subsets of ([0,n)), exactly as required by the WP.
- **Nontrivial APs:** only (dge1) is used.
- **Witness verification:** every reported integer witness is rescanned against every ((a,a+d,a+2d,a+3d)) with (a+3d<n).
- **Independent small baseline:** (r_4(1),ldots,r_4(16)) were obtained by literal exhaustive subset enumeration, not by the MIP.
- **Independent global upper bounds:** for (n=20,24,28,32), the displayed MIP optima were separately certified by exhaustive hitting-set decision search; pruning uses only the exact lower bound supplied by a pairwise-disjoint packing of uncovered APs.
- **Conditioned lower bound:** if every fiber has deficit at most (d), then (|A|ge m(r_4(N)-d)); therefore (d<lceil G_m(N)/mceil) is impossible from the already certified global optimum. The displayed (d_0) witnesses show this cardinality lower bound is sharp for mere feasibility on every tested instance.
- **Balanced-extremizer check:** at ((4,7)), a 17-set with all fibers (ge4) would necessarily have profile ((5,4,4,4)) up to permutation. All 972,000 locally AP-free such configurations were directly checked and rejected.
- **LP dual direction:** the sparse vertical inequalities are upper bounds on the primal occupancy. The uniform fractional assignment gives the matching lower bound, so the LP identity is exact.
- **No theorem-by-trend:** the gluing gaps, deficit profiles, and diagnostic ratios are reported only at the computed finite instances.

## First defect

The first defect in the naive LP-certificate route is exact: for (m=4) and (m=8), the full raw cross-fiber vertex LP is already solved by the minimum of the local fiber caps and a sparse zero-carry vertical certificate. All other digit/carry AP inequalities fail to improve the fractional optimum. Therefore the observed extra gluing defect lives in integrality/configuration compatibility, not in this first-order LP relaxation; a useful certificate must lift the state space (for example to fiber configurations or valid integer cuts) or exploit an exact forbidden-pattern argument.

## Frontier effect

No theorem-level change to `E3-Q4-DENSITY-LOSS` is justified.

The exact vertical certificate gives
[
r_4(mN)le N,r_4(m)
]
for (m=4,8), but on dyadic scales this does not supply a density-dependent loss relative to (a_n); it is weaker than the protected monotonicity mechanism once (n) is beyond the fixed small scale. The computationally useful effect is instead representational: the raw vertex LP can be ruled out as a source of the missing gluing loss, while the ((4,7)) exact conditioned obstruction shows that global optimality can require *localized* fiber deficit even when a balanced near-extremal gluing is feasible.

## Next residual

Evidence points to a lifted configuration/integer-cut model rather than the raw vertex LP: it should be able to certify the exact ((4,7)) exclusion of all ((5,4,4,4)) profiles and, if possible, the analogous ((8,4)) concentration. The finite data do not indicate that such a lifted certificate persists with scale, and no asymptotic exponent is supported. Any use beyond these finite/model statements requires a separate proof-lane argument.

## Sources

PROTECTED_PACKET_ONLY.

- Immutable task: `E3-C01.md`, blob `599f20f0575eedca5deb5051ccdf3d5914471aee`.
- `E3-TRANCHE-03.json`, blob `b3bc9a04a4b041da8fe311bbf69f607df6fee870`.
- `E3-TRANCHE-03_REPRESENTATION.md`, blob `03314f5581731850cf7c507325e988f3d54842c0`.
- `FRONTIER.json`, blob `66c453978eab0f192673f247542e19b43b83e3ca`.
- `E3-X01_RESULT.md`, blob `16fb1935607c4f0391221606b7a48f5e5b61dbc6`.
- Purely mechanical computation software: Python 3.13.5; SciPy 1.17.0, `scipy.optimize.milp` / `linprog(method="highs")` with the bundled HiGHS backend. No outside mathematical source was used.