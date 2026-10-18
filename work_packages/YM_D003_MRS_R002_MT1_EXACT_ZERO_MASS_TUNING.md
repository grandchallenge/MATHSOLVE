# YM-D003-MRS-R002-MT1 — Exact zero-mass counterterm tuning

Status: `SHARPLY_REDUCED_TO_R2P1__EXACT_ZERO_MASS_TUNING_REMAINS_OPEN`

Parent: `YM-D003-MRS-R002 — SOURCE_PROOF_COMPLETENESS`

## Mission

Close or sharply falsify the exact relevant-mass-counterterm step that MRS explicitly leaves to a fixed-point/two-point renormalization argument.

The task is not to prove global convergence. It is to isolate and solve the smallest upstream missing theorem.

## Protected source fact

MRS introduce a relevant `A^2` counterterm with coefficient `b_rho` and state that it must be tuned exactly so that the renormalized mass is zero. They point to scalar infrared `phi^4_4` fixed-point/two-point methods as an analogy or method template rather than giving an MRS-specific theorem.

## Work decomposition

### MT1-A — fixed-point map typing

Identify from the MRS construction the exact scale-`rho` mass functional
`M_{rho,R}(b; lambda)`
or equivalent two-point/1PI relevant projection for which the renormalization condition is

`M_{rho,R}(b_rho; lambda) = 0`.

Record:

- field/object space;
- regulator parameters;
- renormalization projection;
- dependence on `b`;
- background-field dependence;
- norm/topology;
- all constants and their allowed dependence on fixed `R`.

If no such object can be typed from the primary source, return the exact source/evidentiary blocker.

### MT1-B — invariant interval / a priori bound

Find an interval or ball `I_{rho,R}` for `b` such that the candidate fixed-point map maps `I_{rho,R}` into itself, with control adequate for all sufficiently large `rho`.

### MT1-C — contraction or implicit-function estimate

Prove one of:

- a contraction estimate `|F_{rho,R}(b)-F_{rho,R}(b')| <= q |b-b'|`, `q<1`; or
- an implicit-function/nonvanishing-derivative criterion sufficient for exact zero-mass selection.

Every estimate must be MRS-specific. Do not import scalar `phi^4_4` constants or bounds without a proved comparison.

### MT1-D — multiscale compatibility

Show that the selected `b_rho` is compatible with the MRS scale induction and that inserting the tuned value does not destroy the already protected large-field stability estimates.

### MT1-E — downstream interface

State exactly what MT1 supplies to the later Mayer/polymer convergence node:

- relevant two-point subtraction closed;
- uniformity in ultraviolet cutoff index;
- allowed fixed-IR dependence;
- any remainder norm.

## Falsification tests

The route is falsified or reduced rather than "proved by analogy" if:

1. the MRS paper never defines a quantitative mass map adequate for a fixed-point theorem;
2. the derivative/Lipschitz control needed for a contraction is absent and cannot be derived from the protected estimates;
3. the proposed tuning requires an unproved gauge/background comparison;
4. the needed bound is not uniform in `rho`;
5. exact tuning conflicts with the counterterm structure used in Section VI stability;
6. a cited scalar or Gross-Neveu theorem requires hypotheses not available in the MRS gauge setting.

## Acceptance criterion

A theorem-grade closure must contain a fully typed MRS-specific existence argument for `b_rho(lambda,R)` and the quantitative bound needed downstream.

A sharp reduction is also acceptable if it names the smallest missing estimate and proves that all other fixed-point hypotheses follow from protected MRS material.

## Claim boundary

MT1 concerns only relevant mass-counterterm selection at fixed infrared cutoff within the MRS route. It does not prove global Schwinger convergence, Slavnov defect decay, infrared removal, complete OS axioms, or mass gap.


## 2026-10-03 native disposition

MT1-A and MT1-A1 were executed against protected source authority:

- MATHFORGE `90254084f3d06dcaad1a6a950039396ea85c23f9`;
- MATHFORGE `9b6413a7ca5972b7d724ea8f1594c01b8f46cf45`.

The result is:

`MT1_NOT_STRICTLY_UPSTREAM__COUPLED_TO_LOCAL_RENORMALIZED_TWO_POINT_POLYMER_BOUND`.

The scalar proof template cited by MRS defines its mass subtraction from zero-momentum 1PI two-point Mayer graphs and derives the running mass bound from the corresponding subgraph bounds. MRS does not theoremize the analogous gauge-theory two-point sector.

Therefore the active native target is now:

`YM-D003-MRS-R002-R2P1 — UNIFORM_RENORMALIZED_1PI_TWO_POINT_POLYMER_BOUND_AND_MASS_RECURSION`.

See:

- `work_packages/YM_D003_MRS_R002_MT1_A_FIXED_POINT_GATE.md`
- `work_packages/YM_D003_MRS_R002_MT1_A1_DISPOSITION.md`
- `work_packages/YM_D003_MRS_R002_R2P1_TWO_POINT_POLYMER_MASS_RECURSION.md`

MT1 will close if R2P1 supplies the local two-point constructive induction and the final fixed-point/implicit-function step succeeds.
