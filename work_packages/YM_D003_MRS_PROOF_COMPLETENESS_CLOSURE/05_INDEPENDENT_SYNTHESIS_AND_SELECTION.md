# YM-D003-MRS-R002 — independent synthesis and native-node selection

Date: 2026-10-03

## Inputs

Protected external evidence:

- WP-A source-dependency reconstruction: issue #716, comment `5967005635`, declared disposition `REDUCED`.
- WP-B convergence closure: issue #717, comment `5966952070`, declared disposition `PROVED`.
- WP-C adversarial audit: issue #718, comment `5966936787`, declared disposition `REFUTED`.

All three returns are evidence only. This synthesis is a new GCL-owned adjudicative analysis; it does not adopt contributor dispositions as authority.

## Independent replay

### Source target and global qualification

Magnen–Rivasseau–Sénéor, *Construction of YM_4 with an infrared cutoff*, CMP 155 (1993), state a fixed-infrared-cutoff ultraviolet-limit construction for pure four-dimensional SU(2) in a regularized axial-gauge setup, but explicitly say they do not provide the full detailed proof.

### Large-field stability is not the smallest open node

The Section VI stability estimate is materially proved in-body. The paper explicitly completes Lemma VI.1 and obtains the stabilizing bound (VI.35). This supports WP-A's classification of the large-field suppression mechanism as substantially closed inside MRS.

### Finite-order Slavnov limit passage is conditional, not the smallest missing theorem

Section VIII states that at finite ultraviolet cutoff the identity has right-hand side `E_N + delta_N(rho)`, that the normalized cutoff Schwinger functions tend to the constructed no-UV-cutoff functions, and that the expansion makes `delta_N(rho)` tend to zero.

WP-B's narrow lemma is independently valid: at fixed infrared regulator and fixed hierarchy order, once the required smeared/distributional Schwinger convergence and defect convergence hold, the finite linear differential/contraction identity passes to the limit by continuity of distributional differentiation and finite linear operations.

Therefore the pure finite-order limit-passage step is not selected as the smallest missing theorem. Its premises remain upstream debt.

### Typed topology/domain objection is material

WP-C is correct that bibliographic completeness is insufficient. Every imported dependency must be typed by exact object/domain, topology or norm, held-fixed regulators, uniformity parameters, hypotheses, and conclusion. Fixed-order convergence cannot silently become hierarchy convergence; fixed-IR statements cannot silently become IR-uniform statements.

This requirement is incorporated into the native target below.

### Exact zero-mass tuning is explicitly left open at theorem grade

MRS Section III states that the relevant counterterm `b_rho ∫(A^2/2)` must be tuned exactly to make the renormalized mass zero. It then says this is the same problem as critical bare-mass selection in infrared scalar `phi^4_4` and **should be solved** by a fixed-point argument as in Rivasseau [R] or by a full two-point/1PI analysis as in [FMRS1].

The cited FMRS1 theorem is not a theorem in the MRS Yang-Mills setting. It concerns the scalar massless `phi^4_4` thermodynamic/infinite-volume limit with an ultraviolet cutoff. MRS instead needs a gauge-field relevant-counterterm selection inside a four-dimensional SU(2) ultraviolet-limit construction at fixed infrared cutoff, with gauge-restoring counterterms and background-dependent gauges.

No protected comparison theorem transports the scalar fixed-point theorem to the MRS gauge problem.

## Dependency synthesis

The independently supported dependency order is:

1. MRS-specific large-field stability: substantially proved in-body.
2. **Exact relevant mass-counterterm tuning: theorem-grade gap.**
3. Mayer/effective-coupling and polymer summability: partly sketched / method-referred.
4. Cutoff-uniform Schwinger convergence: downstream composite gap.
5. Defect estimate `delta_N(rho) -> 0`: upstream quantitative premise for Slavnov passage.
6. Finite-order Slavnov limit passage: conditionally closed once 4 and 5 hold.

Because node 2 is upstream of the global summability/convergence claims and is explicitly isolated by MRS as a problem to be solved by analogy rather than proved in the paper, it is the smallest confirmed theorem-grade gap presently suitable for native proof/falsification.

## Selected native node

`YM-D003-MRS-R002-MT1 — EXACT_ZERO_MASS_COUNTERTERM_TUNING`

### Exact target

Fix:

- the MRS pure `SU(2)` four-dimensional construction;
- the trivial topological sector;
- one admissible fixed infrared regulator `R`;
- the MRS regularized axial/background-gauge and ultraviolet cutoff family;
- sufficiently small coupling in the regime required by the MRS expansion.

Construct, or prove the existence of, an exact relevant counterterm choice `b_rho(lambda,R)` for every sufficiently large ultraviolet cutoff index `rho` such that the selected renormalized two-point/1PI mass functional is exactly zero, with quantitative control strong enough to be inserted into the MRS multiscale/polymer induction.

The theorem must state explicitly:

1. the renormalized two-point object whose zero-momentum/relevant part defines the mass condition;
2. the domain of the counterterm parameter;
3. the exact fixed-point or implicit equation defining `b_rho`;
4. existence, and any uniqueness actually needed downstream;
5. scale-to-scale compatibility;
6. the norm/topology in which the two-point remainder is controlled;
7. which constants may depend on the fixed infrared regulator;
8. the uniform-in-`rho` estimate required by the later polymer/Schwinger convergence step.

### Native first gate

`YM-D003-MRS-R002-MT1-A — FIXED_POINT_MAP_TYPING_AND_CONTRACTION_GATE`

Produce one of:

- `PROVED`: an MRS-specific fixed-point/implicit-function theorem with all hypotheses verified from protected MRS estimates;
- `REDUCED`: a mathematically sharp reduction to one or more named MRS-specific derivative/Lipschitz/invariance estimates;
- `REFUTED`: a counterexample or incompatibility showing the proposed fixed-point formulation cannot deliver the required exact mass condition under the stated hypotheses;
- `SOURCE_BLOCKED`: the exact MRS quantity/estimate required for typing the map cannot be recovered from available primary material.

A scalar `phi^4_4` fixed-point theorem is not itself sufficient. It may be used only as a proof template after each hypothesis is re-established in the MRS gauge-field setting.

## Why MT1 is smaller than the other candidates

- It is a single relevant-parameter selection problem rather than the whole polymer convergence theorem.
- MRS identifies it explicitly and separately before the global convergence discussion.
- The global Schwinger convergence node depends on this tuning.
- WP-B removes finite-order Slavnov limit passage from contention as a separate smallest gap.
- WP-C's topology/domain requirement can be enforced locally in the MT1 theorem statement.

## Advancement

Only after MT1 is proved or sharply reduced should GCL choose between the next two native targets:

- MRS-specific all-scale Mayer/polymer summability; or
- the cutoff-error insertion estimate needed for `delta_N(rho) -> 0`.

No advancement to `YM-D003-MRS-R003 — IR_AND_INFINITE_VOLUME_REMOVAL` is authorized by this selection.

## Claim boundary

This synthesis selects a bounded proof obligation. It does not prove the MRS fixed-IR ultraviolet construction, infrared removal, OS reconstruction, nontrivial topology, a physical mass gap, or YM-001 closure.
