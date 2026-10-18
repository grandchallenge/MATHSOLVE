# YM-D003-MRS-R002-R2P1 — Uniform renormalized 1PI two-point polymer bound and mass recursion

Status: `SHARPLY_REDUCED_TO_R2P1_C__NEW_MRS_SPECIFIC_SUBGRAPH_THEOREM_REQUIRED`

Parent obligations:

- `YM-D003-MRS-R002-MT1 — EXACT_ZERO_MASS_COUNTERTERM_TUNING`
- local two-point part of `YM-D003-MRS-R002-B — EXPANSION_CONVERGENCE_AND_SUMMABILITY`

Protected source authority:

- `grandchallenge/MATHFORGE@90254084f3d06dcaad1a6a950039396ea85c23f9`
- `grandchallenge/MATHFORGE@9b6413a7ca5972b7d724ea8f1594c01b8f46cf45`

## Mission

Construct and bound the exact MRS renormalized local one-particle-irreducible two-point sector sufficiently to define and solve the relevant zero-mass counterterm recursion.

This is the smallest presently identified non-circular native theorem target in the MRS proof-completeness route.

## Required MRS-specific objects

For fixed admissible infrared regulator `R`, define at every ultraviolet/multiscale level:

1. a renormalized 1PI two-point polymer/subgraph kernel
   `K^{(2)}_{i,rho,R}`;
2. its local relevant projection
   `P_rel K^{(2)}_{i,rho,R}`
   onto the normalized `A^2/2` operator;
3. a scale contribution `delta b_i` derived from that relevant projection;
4. an exact running/tuned mass counterterm
   `b_i` or terminal `b_rho`
   built inductively from those contributions.

The sign and normalization must agree with MRS Eq. (III.1) and the Section VI quadratic-counterterm normalization check.

## Core theorem target

Prove a bound of the following functional role, with the exact norm and powers determined by the MRS anisotropic phase-space scaling:

> The renormalized 1PI two-point polymer/subgraph sum at scale `i`, after its local relevant part is extracted, is summable with a scale-decaying remainder; the extracted relevant coefficient is small and Lipschitz/nondegenerate in the running mass parameter; all constants needed for the induction are uniform in the terminal ultraviolet depth `rho` for `rho >= i`, with dependence on fixed `R` exposed.

The theorem must be strong enough to derive:

- boundedness of the running mass recursion;
- existence of the exact zero-mass tuned `b_rho(lambda,R)`;
- compatibility with the MRS local renormalization/Mayer organization;
- compatibility with Section VI stability normalization.

## Required decomposition

### R2P1-A — exact local two-point polymer grammar

Define which MRS polymers/Mayer graphs count as the renormalized 1PI two-point sector and how nested/proper two-point subgraphs are subtracted.

### R2P1-B — relevant projection identity

Define the MRS gauge-theory analog of the scalar zero-external-momentum relevant projection, respecting the fixed IR geometry and gauge/counterterm conventions.

### R2P1-C — subgraph bound

Prove the normed scale bound on the renormalized two-point sector.

This is the load-bearing new estimate.

### R2P1-D — mass recursion

Use R2P1-B/C to define the running exact mass counterterm and prove its induction bound.

### R2P1-E — response/root theorem

Derive the contraction or implicit-function criterion and solve the exact zero-renormalized-mass condition.

### R2P1-F — Section VI compatibility

Verify that the selected exact mass value preserves the counterterm normalization/stability interface used in the background-field effective potential.

## Anti-circularity firewall

Do not assume the full MRS expansion converges in order to prove the local two-point subgraph bound if that full convergence itself depends on exact mass subtraction.

Permitted strategy:

- simultaneous induction in which the two-point subgraph bound and running mass bound close together, as in the scalar proof template.

Not permitted:

- assume global Schwinger convergence;
- define the response using a limiting theory whose existence is downstream;
- import scalar `phi^4_4` or Gross-Neveu bounds without re-proving the hypotheses in the MRS gauge setting.

## Falsification conditions

Return a sharp obstruction if:

1. no non-circular 1PI two-point decomposition can be defined under the MRS background-dependent gauge organization;
2. the relevant projection is not stable under the horizontal/vertical/Mayer operations;
3. the two-point subgraph sum lacks a scale-decaying uniform bound;
4. the response to the mass parameter is not contractive/nondegenerate;
5. the exact tuned counterterm violates the Section VI stability normalization;
6. the proof necessarily requires an already-constructed limiting Schwinger hierarchy.

## Acceptance criterion

R2P1 closes only when the local two-point constructive induction and exact mass recursion are theorem-grade and non-circular.

A sharp proof that R2P1 cannot be separated from a larger explicit MRS polymer theorem is also an admissible falsification/reduction, provided the exact coupled theorem is named.

## Claim boundary

R2P1 does not by itself prove full polymer summability, the fixed-IR ultraviolet Schwinger limit, Slavnov defect decay, infrared removal, OS reconstruction, or mass gap.


## 2026-10-03 execution disposition

The R2P1 source/native replay has been completed.

MRS supplies:

- the location of the divergent two-/four-point sector after horizontal/vertical decoupling;
- the need for a Mayer expansion before local counterterm cancellation;
- the standard polymer convergence criterion;
- MRS-specific propagator decay and anisotropic power-counting/resummation ingredients.

But for the exceptional two-/four-point sector, MRS says renormalization performs the required task “in the usual way” and refers the detailed Mayer/constructive machinery to `[R]`. No MRS-specific normed theorem for the renormalized local two-point subgraph sector is stated.

The scalar critical-mass template confirms that this local two-point subgraph theorem is load-bearing for the exact mass recursion.

Therefore R2P1 is reduced to:

`YM-D003-MRS-R002-R2P1-C — MRS_RENORMALIZED_TWO_POINT_SUBGRAPH_THEOREM`

with disposition:

`MISSING_MRS_SPECIFIC_RENORMALIZED_1PI_TWO_POINT_POLYMER_NORM_AND_SUBGRAPH_BOUND__NEW_NATIVE_PROOF_REQUIRED`.

See:

- `work_packages/YM_D003_MRS_R002_R2P1_SOURCE_REPLAY_AND_BOUNDARY.md`
- `work_packages/YM_D003_MRS_R002_MT1_A1_DISPOSITION.md`

The exact norm and scale exponents are part of the new theorem and are deliberately not invented from the source sketch.
