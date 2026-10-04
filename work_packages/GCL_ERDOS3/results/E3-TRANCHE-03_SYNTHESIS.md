# E3-TRANCHE-03 — synthesis against E3-Q4-DENSITY-LOSS

Capture baseline: `a10d4546a6c58aad44bc4f49daf71e14526b4b94`  
Immutable task commit: `266b0857f3e13524ea9e69e2ef3bf4cd422503b5`  
Capture manifest: `work_packages/GCL_ERDOS3/results/E3-TRANCHE-03_CAPTURE.json`

## Decision

All six independent-blind returns were durably captured before synthesis. No live issue text or post-capture repository state is used as mathematical evidence in this adjudication.

The tranche produces one theorem-grade structural advance: **E3-G01 proves that the promoted density-loss target is equivalent, up to the fixed factor (2^L), to a finite near-extremizer gluing-radius lower bound.** Because this is a new bridge theorem, the campaign's default independent replay budget is consumed before it changes the active frontier.

The selected successor candidate is:

> **E3-Q4-GLUING-RADIUS.** Let (N=2^n), (m=2^L), and (a_n=r_4(N)/N). Define (H_{L,n}) as the least integer (hge0) for which there exist (m) fibers (B_isubseteq[0,N-1]), each with (|B_i|ge r_4(N)-h), whose translated union (igcup_i(iN+B_i)) is 4-AP-free, and put (Gamma_{L,n}=H_{L,n}/N). Prove that for some fixed (Lge1), (kappa>0), (0<	heta<1), and (n_0),
> [
> Gamma_{L,n}ge kappa a_n^{1+	heta}qquad(nge n_0).
> ]

E3-G01 claims and proves
[
D_{L,n}:=a_n-a_{n+L}le Gamma_{L,n}le 2^L D_{L,n}.
]
If independently verified, this makes E3-Q4-GLUING-RADIUS equivalent up to constants to E3-Q4-DENSITY-LOSS and therefore sufficient for E3-Q4-SERIES.

Until E3-V03 verifies that bridge, **E3-Q4-DENSITY-LOSS remains the sole active frontier** and E3-Q4-GLUING-RADIUS remains a formulated successor candidate rather than a promoted theorem node.

## Return-by-return synthesis

### E3-R01 — accepted representation theorem, not selected

R01 proves the exact layer-cake identity
[
sum_n a_n=int_{(0,1]}P(alpha),dalpha,
qquad P(alpha)=#{n:a_ngealpha},
]
and establishes that (Pin L^1) is exactly equivalent to convergence of the series. It also proves that power persistence is strictly weaker than fixed-step local drift because arbitrarily long plateaux can satisfy a global persistence envelope.

This is valuable representation control, but (Pin L^1) is equivalent to the parent series itself and therefore does not strictly narrow the unresolved mathematical content. It is retained as an alternate coordinate system, not selected as the successor frontier.

### E3-D01 — accepted exact compiler, supporting

D01 proves the exact digit-and-carry compiler and gives a complete (m=4) finite constraint system, including the carry-free varying-residue family that a coarser three-way classification would miss.

This removes representation ambiguity. It does not supply the sparse-density loss needed to close the active frontier, so it supports the selected gluing-radius route rather than replacing it.

### E3-G01 — accepted theorem-grade structural advance; independent replay required

G01 proves the one-step deficit identity, multilevel extremizer-tree concentration, and the exact finite gluing-radius reduction. The key bridge is
[
D_{L,n}leGamma_{L,n}le2^L D_{L,n}.
]

This is the smallest theorem-grade structural reduction produced by the tranche. It converts the active sequence inequality into a finite carry-constrained near-extremizer feasibility theorem.

Under the frontier gate, this bridge is routed to one independent replay, E3-V03, before active-frontier replacement.

### E3-C01 — accepted computational evidence, not promoted

C01 proves that the raw cross-fiber vertex LP is exactly too weak: for (m=4,8), its optimum is already explained by fiber caps and simple vertical constraints. The observed additional gluing loss is therefore integral/configurational.

Its finite exact computations are useful design evidence for a lifted configuration or integer-cut model, but they do not justify an asymptotic theorem or exponent.

### E3-A03 — accepted adversarial boundary, not promoted

A03 finds no counterexample to the density-loss route in the declared product/separated-construction family. It proves the lower transfer
[
a_{n+m+1}ge 	frac12 a_n a_m
]
and sharpens the diagonal power-recurrence obstruction to (plesqrt2).

This constrains future arguments but neither refutes nor proves the active route.

### E3-S04 — accepted source interface, not promoted

S04 identifies an exact four-function (U^3)/quadratic-uniformity counting interface in the primary literature. It also isolates the missing source-level bridge: convert forced quadratic structure across carry-compatible dense fibers into a transversal or mass deficit of order (a_n^{1+	heta}N) with (	heta<1).

This gives a concrete attack mechanism for E3-Q4-GLUING-RADIUS, but no audited source supplies the required stability theorem.

## Resulting direction

The campaign should no longer search for another generic recurrence or another first-order LP relaxation.

The concrete proof target is a **quantitative near-extremizer gluing stability theorem**. The most promising attack is:

[
	ext{exact digit/carry hypergraph}
;	o;
	ext{forced }U^3	ext{/quadratic structure}
;	o;
	ext{configuration incompatibility / transversal cost}
;	o;
Gamma_{L,n}gtrsim a_n^{1+	heta}.
]

The raw vertex LP has been ruled out as the missing mechanism. A lifted configuration formulation, structural theorem for mutually positioned near-extremizers, or a quadratic-stability argument is required.

## Verification gate

E3-V03 independently replays only the theorem-grade bridge needed for frontier movement:

1. the definition and well-posedness of (H_{L,n}) and (Gamma_{L,n});
2. (D_{L,n}leGamma_{L,n});
3. (Gamma_{L,n}le2^L D_{L,n});
4. the resulting constant-factor equivalence between E3-Q4-DENSITY-LOSS and E3-Q4-GLUING-RADIUS;
5. the exact finite 0-1 carry formulation used to interpret the gluing radius.

No other tranche claim is promoted by that verification.

## Claim boundary

E3-Q4-DENSITY-LOSS remains OPEN. E3-Q4-GLUING-RADIUS is FORMULATED_PENDING_VERIFY, not proved. E3-Q4-SERIES remains OPEN. Erdős Problem 3 remains OPEN.
