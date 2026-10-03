# YM-D003-MRS-R002-MT1 — Exact zero-mass counterterm tuning

Status: `SELECTED_FOR_NATIVE_GCL_PROOF_OR_FALSIFICATION`

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
