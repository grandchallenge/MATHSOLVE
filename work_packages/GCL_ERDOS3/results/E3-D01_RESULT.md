GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-D01-IA-001
assignment: E3-D01
agent_ref: INDEPENDENT-AGENT-E3-D01-001
disposition: FINITE_CARRY_REPRESENTATION_PROVED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY

## Strongest exact statement

Let (m=2^L), (N=2^n), and write every (xin[0,mN)) uniquely as
[
x=iN+u,qquad 0le i<m,quad 0le u<N,
]
and every positive common difference uniquely as
[
d=qN+v,qquad qge0,quad 0le v<N,quad (q,v)
e(0,0).
]
For (t=0,1,2,3), define
[
c_t=leftlfloorrac{u+tv}{N}ightfloor,qquad
r_t=u+tv-c_tN,qquad
b_t=i+tq+c_t.
]
Then
[
x+td=b_tN+r_t,
]
with (0le r_t<N). Hence the progression lies in ([0,mN)) if and only if
[
b_3=i+3q+c_3le m-1;
]
all earlier block indices are then automatically valid because (b_t) is nondecreasing.

The carry vector has exactly the form
[
(c_0,c_1,c_2,c_3)in
{0000,0001,0011,0012,0111,0112,0122,0123},
]
subject to the exact lattice inequalities below. For (Nge4) (hence (4mid N)) all eight types occur. For (N=2) only (0000,0011,0112) occur; for (N=1) only (0000) occurs. No other carry vector is possible.

For (m=4), this yields a complete finite compiler with 21 coarse/carry template families: 4 within-fiber (0000,q=0) templates; 1 (0000,q=1) cross-block template; 9 one-boundary templates; 6 two-boundary templates; and 1 three-boundary template. The resulting binary constraint system is exactly the 4-AP hypergraph of ([0,4N)), so its maximum independent-set size is exactly (r_4(4N)).

No density-loss estimate is proved. In particular, this result does not certify E3-Q4-DENSITY-LOSS, E3-Q4-SERIES, or Erdős Problem 3.

## Derivation / evidence

### 1. Protected-packet verification

The immutable files were read only at commit
`266b0857f3e13524ea9e69e2ef3bf4cd422503b5`.
Their returned Git blob identities exactly match the dispatch:

- `E3-D01.md`: `b7a43c535c59000cfc4cd443b54677ef125d6ca8`;
- `E3-TRANCHE-03.json`: `b3bc9a04a4b041da8fe311bbf69f607df6fee870`;
- `E3-TRANCHE-03_REPRESENTATION.md`: `03314f5581731850cf7c507325e988f3d54842c0`;
- `FRONTIER.json`: `66c453978eab0f192673f247542e19b43b83e3ca`;
- `E3-X01_RESULT.md`: `16fb1935607c4f0391221606b7a48f5e5b61dbc6`.

No repository state later than the task commit was inspected.

### 2. Exact block/residue formula

Starting from (x=iN+u) and (d=qN+v),
[
x+td=(i+tq)N+(u+tv).
]
Euclidean division of (u+tv) by (N) gives
[
u+tv=c_tN+r_t,qquad
c_t=leftlfloorrac{u+tv}{N}ightfloor,quad 0le r_t<N,
]
so
[
x+td=(i+tq+c_t)N+r_t=b_tN+r_t.
]

Since (0le v<N),
[
c_t-c_{t-1}in{0,1}.
]
Also (c_0=0). Thus the three carry increments are binary, giving at most eight words. The exact inequalities below determine which words occur on the integer lattice.

### 3. Necessary and sufficient carry inequalities

In every row assume (0le u,v<N).

| carry vector | necessary and sufficient condition |
|---|---|
| (0000) | (u+3v<N) |
| (0001) | (u+2v<Nle u+3v) |
| (0011) | (u+v<Nle u+2v) and (u+3v<2N) |
| (0012) | (u+v<N) and (2Nle u+3v) |
| (0111) | (Nle u+v) and (u+3v<2N) |
| (0112) | (Nle u+v, u+2v<2Nle u+3v) |
| (0122) | (2Nle u+2v) and (u+3v<3N) |
| (0123) | (3Nle u+3v) |

These are obtained by intersecting
[
c_tNle u+tv<(c_t+1)N,qquad t=1,2,3,
]
and deleting inequalities implied by (0le u,v<N).

For (Nge4), put (h=N/4). Integer witnesses for the eight rows, in the displayed order, are
[
(0,h),(h,h),(0,2h),(0,3h),(3h,h),(h,3h),(2h,3h),(3h,3h).
]
Thus all eight types genuinely occur once (Nge4).

### 4. Complete (m=4) compiler

For (m=4), the terminal condition is
[
i+3q+c_3le3.
]
Therefore (qge2) is impossible. If (q=1), necessarily (i=0) and (c_3=0), hence the carry vector is (0000). Every nonzero carry type has (q=0).

The complete template list is:

| carry | (q) | allowed (i) | block word ((b_0,b_1,b_2,b_3)) | residual word ((r_0,r_1,r_2,r_3)) |
|---|---:|---|---|---|
| (0000) | 0 | (0,1,2,3) | ((i,i,i,i)) | ((u,u+v,u+2v,u+3v)) |
| (0000) | 1 | (0) | ((0,1,2,3)) | ((u,u+v,u+2v,u+3v)) |
| (0001) | 0 | (0,1,2) | ((i,i,i,i+1)) | ((u,u+v,u+2v,u+3v-N)) |
| (0011) | 0 | (0,1,2) | ((i,i,i+1,i+1)) | ((u,u+v,u+2v-N,u+3v-N)) |
| (0111) | 0 | (0,1,2) | ((i,i+1,i+1,i+1)) | ((u,u+v-N,u+2v-N,u+3v-N)) |
| (0012) | 0 | (0,1) | ((i,i,i+1,i+2)) | ((u,u+v,u+2v-N,u+3v-2N)) |
| (0112) | 0 | (0,1) | ((i,i+1,i+1,i+2)) | ((u,u+v-N,u+2v-N,u+3v-2N)) |
| (0122) | 0 | (0,1) | ((i,i+1,i+2,i+2)) | ((u,u+v-N,u+2v-2N,u+3v-2N)) |
| (0123) | 0 | (0) | ((0,1,2,3)) | ((u,u+v-N,u+2v-2N,u+3v-3N)) |

For every row, (u,v) must additionally satisfy that row's carry inequalities above and (qN+v>0).

The forbidden relation is uniformly
[
mathbf 1_{A_{b_0}}(r_0)+
mathbf 1_{A_{b_1}}(r_1)+
mathbf 1_{A_{b_2}}(r_2)+
mathbf 1_{A_{b_3}}(r_3)le3.
]
Because (d>0), the four global vertices ((b_t,r_t)) are distinct even when some block indices or residual coordinates repeat.

This is necessary and sufficient: every forbidden row reconstructs a genuine 4-AP with start (iN+u) and difference (qN+v), and every genuine 4-AP has a unique ((i,u,q,v)), hence lands in exactly one compiled carry/coarse template.

### 5. Separation of progression mechanisms

The exact separation is four-way, not three-way.

1. **Within-fiber.** (q=0), carry (0000), (v>0). All four terms lie in one (A_i), so these are precisely ordinary 4-APs inside that fiber and are controlled by (|A_i|le r_4(N)).

2. **Same-residue cross-block.** (q=1), carry (0000), (v=0). The relation is
[
uin A_0cap A_1cap A_2cap A_3,
]
so 4-AP-freeness forces
[
A_0cap A_1cap A_2cap A_3=arnothing.
]

3. **Carry-free, varying-residue cross-block.** (q=1), carry (0000), (v>0), (u+3v<N). These use blocks (0,1,2,3) but residuals (u,u+v,u+2v,u+3v) vary. They are neither within-fiber, nor same-residue, nor carry-mediated.

4. **Genuine carry-mediated.** Every nonzero carry word above. For (m=4) these all have (q=0) and are exactly the seven nonzero-carry template families.

The fourth class is essential for exactness.

### 6. Minimal proved gluing subsystem

The smallest nonempty cross-block subsystem is the single same-residue family
[
(q,c,v)=(1,0000,0).
]
Its exclusion alone implies a genuine, though only high-density, gluing penalty. Define
[
mu(u)=sum_{i=0}^3mathbf 1_{A_i}(u).
]
Because fourfold membership is forbidden, (mu(u)le3) for every (u), hence
[
sum_{i=0}^3|A_i|le3N.
]
Combining this with the four within-fiber bounds (|A_i|le r_4(N)) gives
[
|A|le min{4r_4(N),3N},
]
or equivalently the exact deficit estimate
[
4r_4(N)-|A|ge igl(4r_4(N)-3Nigr)_+.
]

This subsystem is inclusion-minimal: deleting its only cross-block relation leaves only the independent within-fiber bounds and therefore no gluing statement at all. However, its penalty vanishes once (r_4(N)/Nle3/4), so it is not a frontier-grade sparse-density loss.

### 7. Exact finite combinatorial object

Let the vertex set be
[
V_N={(i,r):0le i<4, 0le r<N}.
]
For every compiled admissible tuple ((i,q,u,v)), add the 4-element hyperedge
[
E(i,q,u,v)={(b_t,r_t):t=0,1,2,3}.
]
Then (Asubseteq[0,4N)) is 4-AP-free if and only if its fiber indicator vector is an independent set of this 4-uniform hypergraph.

Equivalently, with binary variables (z_{i,r}in{0,1}), make one constraint
[
sum_{(i,r)in E} z_{i,r}le3
]
for every compiled edge. If (M_N) is the resulting (0/1) row-edge/column-vertex matrix, then
[
r_4(4N)=
maxleft{mathbf 1^	op z:
M_Nzle3mathbf 1, zin{0,1}^{4N}ight}.
]
This is directly suitable for E3-C01-style exact finite optimization. The carry/coarse template alphabet is independent of (N); only the lattice instantiation of (u,v) grows.

### 8. Exact quantitative residual exposed by the compiler

Write (r=r_4(N)) and let
[
Gamma_N:=max{mathbf 1^	op z:M_Nzle3mathbf 1, zin{0,1}^{4N}}.
]
By the exact compilation, (Gamma_N=r_4(4N)).

For (L=2), the protected density-loss target
[
a_{n+2}le a_n(1-ca_n^	heta)
]
is therefore exactly equivalent to the eventual finite-hypergraph stability inequality
[
4r-Gamma_N
ge
4c,rleft(rac rNight)^	heta
=
4c,r^{1+	heta}N^{-	heta},
qquad 0<	heta<1.
]
The compiler proves the representation equivalence but not this stability inequality.

A weaker subsystem (mathcal S) of compiled cross-block rows may be used: if its optimum (Gamma_N^{mathcal S}) satisfies the displayed upper bound, then the full system does also because (Gamma_NleGamma_N^{mathcal S}). The same-residue subsystem proves only the high-density bound above; a sparse-regime inequality of the required order remains the exact blocker.

### 9. Independent finite replay check

The proof does not depend on computation, but I performed an exhaustive consistency check using only the definitions above.

Replay pseudocode:

```text
DIRECT(N):
  E = {}
  for x in 0..4N-1:
    for d >= 1 while x+3d < 4N:
      add (x,x+d,x+2d,x+3d) to E

COMPILED(N):
  C = {}
  for i in 0..3:
    for q in 0..3:
      for u in 0..N-1:
        for v in 0..N-1:
          if qN+v == 0: continue
          c_t = floor((u+t v)/N), t=0..3
          b_t = i+tq+c_t
          if all 0 <= b_t < 4:
             r_t = u+t v-c_t N
             add (b_t N+r_t)_{t=0}^3 to C
  assert C == E
```

Results:

- (N=1): 1 direct edge = 1 compiled edge;
- (N=2): 7 = 7;
- (N=4): 35 = 35;
- (N=8): 155 = 155;
- (N=16): 651 = 651.

For (N=4,8,16), every one of the eight carry words appears in the compiled enumeration. No discrepancy was found.

## Adversarial checks

- **Carry increments:** because (v<N), a carry can increase by at most one per step; no skipped carry value is possible.
- **Endpoint inequalities:** all carry rows use half-open Euclidean-division intervals, so equality at (N,2N,3N) is assigned to the higher carry exactly once.
- **Small-(N) check:** the eight words are the complete universal list, but some rows are lattice-empty for (N=1,2); the compiler handles this by the displayed inequalities rather than assuming all eight occur.
- **Positive-difference check:** ((q,v)=(0,0)) is explicitly excluded. In the (q=1,v=0) same-residue family the global difference is (N>0).
- **Terminal-block check:** (b_t) is nondecreasing, so (b_3le m-1) is sufficient; no hidden earlier overflow exists.
- **Carry-free omission check:** (q=1,c=0000,v>0) is a genuine cross-block family and must not be silently discarded.
- **Hypergraph check:** the four global terms are distinct whenever (d>0), even if residual coordinates repeat across different fibers.
- **Frontier check:** exact compilation alone gives no quantitative stability bound and therefore no strict density loss in the sparse regime.

## First defect

The three categories requested in item 4 are not exhaustive if read as a partition. There is an additional carry-free but varying-residue cross-block family: (m=4, q=1, c=0000, v>0, u+3v<N). Any representation that keeps only within-fiber, same-residue, and nonzero-carry relations misses valid 4-APs.

## Frontier effect

The digit-and-carry representation is now exact at the smallest tested useful scale (m=4); (m=8) is not needed to obtain a complete carry compiler. The open analytic/combinatorial burden is no longer representation completeness but the finite-hypergraph stability estimate
[
4r_4(N)-r_4(4N)
gtrsim
r_4(N)left(rac{r_4(N)}Night)^	heta
]
for some (0<	heta<1), or an equally strong bound proved already for a weaker subset of the compiled cross-block rows. No such sparse-density penalty is established here, so E3-Q4-DENSITY-LOSS remains open.

## Next residual

The same-residue row gives an exact but sparse-regime-vacuous penalty, so any frontier-grade advance must use at least one (v
e0) cross-block family. The compiler permits that question to be asked as an explicit weaker-hypergraph stability inequality, with every omitted carry family visible rather than implicit. This is evidence only and carries no scheduling authority.

## Sources

PROTECTED_PACKET_ONLY.

Used only the immutable protected files at commit `266b0857f3e13524ea9e69e2ef3bf4cd422503b5`: `E3-D01.md`, `E3-TRANCHE-03.json`, `E3-TRANCHE-03_REPRESENTATION.md`, `FRONTIER.json`, and `results/E3-X01_RESULT.md`. No outside mathematical source, other tranche-03 return, intake issue, campaign discussion, pull request, unpublished note, later repository state, or tool/solver documentation was consulted.