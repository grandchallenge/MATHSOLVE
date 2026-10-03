# YM-D003-MRS-R002-MT1-A — fixed-point map typing and contraction gate

Disposition: `REDUCED`

Date: 2026-10-03

Protected source authority:

- MATHFORGE `90254084f3d06dcaad1a6a950039396ea85c23f9`
- `sources/YM-001/YM_D003_MRS_MT1_SOURCE_BODY_AUDIT.md`

## Question

Can the MRS exact relevant mass-counterterm requirement be closed directly from the protected MRS source and its cited scalar fixed-point template?

## Result

No theorem-grade exact mass tuning follows directly from the protected source packet.

The source is strong enough to type the **form of the missing proof**, but not to supply the Yang-Mills-specific map or quantitative estimate required by that proof.

The exact native residual is:

`YM-D003-MRS-R002-MT1-A1 — UNIFORM_MRS_1PI_MASS_RESPONSE_CONTROL`

## Source-derived facts

1. MRS Eq. (III.1) introduces the relevant counterterm coefficient `b_rho` multiplying the normalized quadratic operator `A^2/2`.
2. Immediately after Eq. (III.1), MRS says this coefficient must be fine-tuned exactly so that the renormalized mass is zero.
3. MRS says the intended proof is a fixed-point argument as in Rivasseau or a full renormalization of the two-point function with a one-particle-irreducible analysis as in FMRS1.
4. Section V.E repeats that the relevant mass operator requires exact fixed-point tuning at the multiscale-flow level.
5. The cited FMRS1 scalar construction defines its running mass subtraction inductively from the negative zero-external-momentum value of one-particle-irreducible two-point subgraphs.
6. MRS does not state the corresponding Yang-Mills 1PI recursion, fixed-point map, invariant interval, or quantitative response estimate.

## Native typing

Fix one admissible infrared regulator `R`, one sufficiently large ultraviolet cutoff index `rho`, and small coupling `lambda` in the MRS regime.

The missing proof can be typed as follows.

Let

`Sigma_rel(rho,R,b,lambda)`

denote the exact local relevant coefficient extracted from the renormalized one-particle-irreducible two-point sector of the MRS gauge-fixed expansion **after removing the explicit tunable quadratic counterterm contribution**, with the sign convention chosen so that the zero-renormalized-mass equation is

`b = F(rho,R,b,lambda)`

where `F` is the corresponding relevant self-energy response.

This is a native definition/target, not a claim that MRS already constructed `F`.

The object must be built with:

- the MRS regularized axial/background/homothetic gauge choices;
- the non-gauge-invariant ultraviolet cutoff and its gauge-restoring counterterms;
- the same relevant `A^2/2` normalization used in Eq. (III.1);
- the same scale decomposition used in the MRS phase-space expansion;
- the fixed infrared regulator retained as a parameter.

## Conditional fixed-point lemma

Assume that for one fixed `R` and sufficiently small `lambda` there exist:

- `rho_0`;
- a closed interval `I_R(lambda)`;
- a number `q_R(lambda) < 1`;

such that for every `rho >= rho_0`:

1. `F(rho,R,.,lambda)` is well defined on `I_R(lambda)`;
2. `F(rho,R,I_R(lambda),lambda) subset I_R(lambda)`;
3. for every `b,b'` in `I_R(lambda)`,
   `|F(rho,R,b,lambda)-F(rho,R,b',lambda)| <= q_R(lambda)|b-b'|`.

Then for every `rho >= rho_0` there is a unique
`b_rho(lambda,R) in I_R(lambda)`
such that

`b_rho = F(rho,R,b_rho,lambda)`.

### Proof

`I_R(lambda)` is complete in the Euclidean metric. For each fixed `rho`, hypothesis 2 makes `F` a self-map of that complete metric space and hypothesis 3 makes it a strict contraction. Banach's fixed-point theorem gives a unique fixed point `b_rho`, and the defining sign convention makes that fixed point exactly the zero-renormalized-mass condition.

The constants may depend on the fixed infrared regulator `R`; no IR-uniform statement is inferred.

This lemma closes only the existence/uniqueness step once the MRS-specific response map and bounds exist.

## Why the protected source does not discharge the lemma hypotheses

### Map construction

MRS points to a 1PI two-point analysis but does not give the gauge-theory analog of the FMRS1 inductive definition of the local zero-momentum 1PI mass subtraction.

Therefore hypothesis 1 is not source-proved at theorem grade in the exact MRS multiscale language.

### Invariant domain

No interval/ball for the exact `b_rho` iteration is stated in MRS, and no all-order estimate is given that maps such a domain to itself.

Therefore hypothesis 2 is not source-proved.

### Response/contraction

No MRS-specific derivative, Lipschitz, contraction, or implicit-function nondegeneracy bound for the exact relevant two-point response is stated.

Therefore hypothesis 3 is not source-proved.

### Uniformity in the ultraviolet cutoff

MT1 needs the exact tuning to coexist with the later `rho -> infinity` constructive expansion. A fixed-`rho` existence argument alone is insufficient unless its admissible domain and response constants remain controlled for all sufficiently large `rho`.

No such exact all-order uniform response theorem is supplied by MRS.

### Section VI compatibility

Section VI checks the normalization and uses the quadratic counterterm in the background-field stability analysis, but that does not prove that an all-order fixed-point value selected from the two-point sector preserves every stability hypothesis.

This compatibility remains a required interface after A1 is proved.

## Smallest missing theorem-grade estimate

The first genuinely new mathematical theorem needed for the fixed-point route is:

> For fixed admissible IR regulator `R` and sufficiently small coupling, construct the exact MRS local 1PI two-point relevant response `F(rho,R,b,lambda)` and prove a `rho`-uniform invariant-domain plus strict-response bound (or an equivalent implicit-function nondegeneracy theorem) in the exact MRS gauge/counterterm/phase-space setting.

This is strictly narrower than proving global polymer convergence or the full Schwinger hierarchy.

## Falsification alternative

A contraction formulation is not mandatory.

A valid A1 result may instead prove an implicit-function route: construct a mass functional `M(rho,R,b,lambda)` and prove, uniformly for sufficiently large `rho`, an admissible domain containing a sign change/root candidate together with a nonvanishing derivative bound sufficient to solve `M=0`.

If neither a contraction nor implicit-function response bound is true, A1 must return a counterexample or exact incompatibility rather than weakening the mass condition.

## MT1-A disposition

`REDUCED_TO_UNIFORM_MRS_1PI_MASS_RESPONSE_CONTROL`

MT1 itself remains open. The source packet does not justify promoting exact zero-mass tuning to a proved MRS theorem.

## Claim boundary

This result proves only a conditional fixed-point implication and identifies the exact missing MRS-specific estimate. It does not prove the response estimate, global expansion convergence, Schwinger convergence, infrared removal, complete OS axioms, or mass gap.
