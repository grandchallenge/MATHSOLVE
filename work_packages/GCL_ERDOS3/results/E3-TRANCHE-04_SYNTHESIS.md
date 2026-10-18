# E3-TRANCHE-04 — native synthesis

Campaign: `GCL-ERDOS3`

Disposition: `NATIVE_REDUCTION__PHASE_ALIGNED_MOTIF_AMPLIFICATION`

Claim boundary: no parent frontier is closed. `E3-Q4-DENSITY-LOSS` remains open; `E3-Q4-GLUING-RADIUS` remains unpromoted pending independent verification of the G01 bridge.

## 1. What tranche 04 has established

### L01 — exact finite family certificate

At (N=7), the C01 exclusion of every ((5,4,4,4)) profile can be compressed from all 97 cross-fibre AP constraints to exactly 10 of the 17 D01 family types.

Five families are individually mandatory:
[
F_2,F_6,F_9,F_{10},F_{16}.
]

Exactly five further families are necessary and sufficient. One minimum 10-family certificate is
[
K={F_1,F_2,F_3,F_4,F_6,F_7,F_9,F_{10},F_{15},F_{16}}.
]

The minimum size 10 is exact.

Effect: the finite obstruction has a compact family-level combinatorial core. The missing asymptotic step is not “understand all 97 APs,” but amplify a bounded motif family.

### Q02 — labelled quadratic forcing

For any valid D01 cross-fibre template on fibres of density at least (eta), zero mixed 4-AP count implies
[
max_t|1_{C_t}-ho_t|_{U^3}
>
rac{eta^4}{15cdot16^4}.
]

Effect: the counting/uniformity stage is discharged at an explicit polynomial norm scale. The missing theorem is not another mixed-counting lemma.

### T01 — scalar (U^3) accumulation obstruction

Across all 17 D01 cross-fibre families, and already across the L01 10-family core, the scalar Q02 inequalities force at least two physical fibres to have large (U^3) norm.

The only minimum two-fibre covers are
[
{0,2},qquad{1,2},qquad{1,3}.
]

Because (U^3) is translation invariant, repeated carry translations of the same physical fibre do not create new scalar information. Therefore repeated Q02 application cannot by itself force rank growth, energy growth, or additional independent quadratic structure.

Effect: any successful structural argument must retain the identity of the quadratic correlation/factor witness, not merely the norm magnitude.

### A04 — synchronized common-core adversary ruled out

If all four fibres differ from one common local extremizer (R), (|R|=r_4(N)), by at most (h) deletions from (R), then the vertical (q=1) carry-free family forces
[
B_0cap B_1cap B_2cap B_3=arnothing
]
and hence
[
hge r_4(N)/4=rac14Na_n.
]

Thus synchronized common-core product/recursive constructions satisfy a stronger deficit bound than the target and cannot refute the (L=2) route.

Effect: a genuine counterexample must deliberately misalign the fibres.

## 2. The smallest live theorem

The combined evidence reduces tranche 04 to the following named bridge.

> **E3-B-QUADRATIC-MOTIF-AMPLIFICATION.**
> Let (B_0,dots,B_3subseteq[0,N-1]) be locally 4-AP-free, each with density at least (eta), and suppose the four-block gluing is globally 4-AP-free.
>
> Use a quantitative (U^3) inverse theorem to attach explicit bounded-complexity quadratic witnesses/factors to the physical fibres whose norm exceeds the Q02 threshold.
>
> Prove that the translated witness relations associated with the 10-family L01 core cannot all coexist unless one fibre loses at least
> [
> ceta^{1+	heta}N
> ]
> points, for some fixed (0<	heta<1).

A sufficient formulation may use:
- local quadratic phases;
- quadratic factors;
- degree-2 nilsequences;
- structured atoms plus a finite compatibility hypergraph;
- or an equivalent witness-retaining decomposition.

The essential requirement is that translated appearances of the **same physical fibre share the same underlying structural witness**. A fresh unrelated phase may not be chosen independently for every carry family.

## 3. Why this is strictly smaller than the previous gap

Before tranche 04, the residual was the broad statement:

[
	ext{forced quadratic nonuniformity across the carry system}
Longrightarrow
	ext{polynomial deletion cost}.
]

After tranche 04:

1. the relevant finite carry subsystem has been reduced to 10 exact families;
2. the norm-forcing step is explicit at scale (ceta^4);
3. scalar norm accumulation is proved insufficient;
4. synchronized common-core constructions are ruled out.

Therefore the unresolved content is specifically **alignment/incompatibility of explicit quadratic witnesses across a bounded carry motif system**.

## 4. Two proof lanes

### Lane A — motif amplification

Lift the nine L01 residual clause types from the (N=7) certificate into positive-density local configurations inside sufficiently large near-extremal fibres.

Required result:
[
	ext{near-extremality + structure}
Longrightarrow
	ext{many occurrences of one of the L01 clause motifs}.
]

Then show each such motif forces a deletion and control overlap strongly enough to obtain exponent (1+	heta<2).

### Lane B — quadratic witness incompatibility

From Q02 plus a quantitative (U^3) inverse theorem, choose explicit witnesses on at least two physical fibres.

Track how translations and the 10 carry families transform those witnesses. Show that simultaneous avoidance of all mixed 4-APs forces either:
- incompatible phase equations;
- excessive quadratic-factor rank/complexity;
- or a large exceptional/deleted set.

This lane bypasses direct finite-motif counting if the phase algebra is stronger.

## 5. Adversarial lane after A04

The remaining serious counterexample class is deliberately misaligned structure:
- affine/Freiman images;
- translated near-extremizers with tiny common intersection;
- differently phased quadratic level sets;
- recursive constructions with no common pointwise core.

Any such construction must still satisfy all 10 L01 core families asymptotically.

## 6. Frontier effect

No promotion is authorized.

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-Q4-GLUING-RADIUS`: **FORMULATED_PENDING_VERIFY**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN**.
- `E3-B-QUADRATIC-MOTIF-AMPLIFICATION`: **FORMULATED_NATIVE_RESIDUAL**.

The next useful work is to prove, falsify, or further reduce `E3-B-QUADRATIC-MOTIF-AMPLIFICATION`.
