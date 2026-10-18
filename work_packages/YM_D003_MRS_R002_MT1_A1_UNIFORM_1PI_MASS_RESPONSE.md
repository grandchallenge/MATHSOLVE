# YM-D003-MRS-R002-MT1-A1 — Uniform MRS 1PI mass-response control

Status: `ACTIVE_NATIVE_RESEARCH_BOUNDARY`

Parent: `YM-D003-MRS-R002-MT1 — EXACT_ZERO_MASS_COUNTERTERM_TUNING`

Source authority:

- `grandchallenge/MATHFORGE@90254084f3d06dcaad1a6a950039396ea85c23f9`
- `sources/YM-001/YM_D003_MRS_MT1_SOURCE_BODY_AUDIT.md`

## Exact objective

For fixed admissible infrared regulator `R` and sufficiently small coupling `lambda`, construct the exact local relevant response of the MRS one-particle-irreducible two-point sector to the tunable quadratic counterterm and prove enough uniform control in ultraviolet cutoff index `rho` to solve the exact zero-renormalized-mass condition.

## Required object

Construct either:

### Fixed-point form

`F_{rho,R}(b;lambda)`

with exact MRS normalization such that

`b = F_{rho,R}(b;lambda)`

is equivalent to zero renormalized mass;

or

### Implicit form

`M_{rho,R}(b;lambda)`

such that

`M_{rho,R}(b;lambda)=0`

is exactly the MRS zero-renormalized-mass condition.

The construction must expose the local relevant projection of the renormalized 1PI two-point sector and may not replace it by scalar `phi^4_4` data.

## Fixed-point acceptance route

Prove, for each fixed `R`, constants/domain independent of all sufficiently large `rho`:

1. `F_{rho,R}` is well defined on a closed interval `I_R(lambda)`;
2. `F_{rho,R}(I_R(lambda)) subset I_R(lambda)`;
3. `Lip_b(F_{rho,R}) <= q_R(lambda) < 1`;
4. the resulting fixed point is compatible with the MRS scale induction;
5. insertion of the selected counterterm respects the already protected Section VI normalization/stability interface.

## Implicit-function acceptance route

Alternatively prove:

1. `M_{rho,R}` is well defined and continuously differentiable in `b` on an admissible interval;
2. the interval contains a root bracket or other existence datum;
3. `|partial_b M_{rho,R}| >= c_R(lambda) > 0` uniformly for sufficiently large `rho`;
4. the selected root obeys the same multiscale and Section VI compatibility requirements.

## Proof template allowed

FMRS1 may be used as a template for:

- zero-external-momentum relevant projection;
- inductive 1PI two-point subtraction;
- fixed-point organization.

Every estimate must be re-established in the MRS pure-SU(2) gauge setting. No scalar theorem is imported by analogy.

## First required quantitative inequality

The preferred contraction route should reduce the all-order response to a bound of the form

`sup_{rho >= rho_0} sup_{b != b' in I_R} |F_{rho,R}(b)-F_{rho,R}(b')| / |b-b'| <= q_R(lambda) < 1`.

A proof may replace this with a stronger normed polymer/activity estimate that implies it.

## Required provenance in any proof

Every estimate must identify:

- the MRS section/equation or native derived lemma supplying it;
- the field/counterterm sector;
- the norm/topology;
- dependence on fixed `R`;
- uniformity in `rho`;
- dependence on `lambda`;
- background-field/gauge assumptions.

## Stop condition

If the response map cannot be constructed without first proving the entire MRS-specific polymer summability theorem, record

`MT1_NOT_STRICTLY_UPSTREAM__COUPLED_TO_GLOBAL_SUMMABILITY`

and return the exact circular dependency. Do not hide the coupling by assuming convergence of the expansion being proved later.

## Claim boundary

A1 is a local exact-mass-renormalization target. Even a proof of A1 does not establish the global MRS UV construction.
