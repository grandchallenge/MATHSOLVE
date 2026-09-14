# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Active tracker: `grandchallenge/MATHSOLVE#215`.
- Current bounded operation: `grandchallenge/MATHSOLVE#227` (`WP60J`).
- Source authority: `grandchallenge/MATHFORGE`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- Certification authority: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Use protected repository state as authority. Do not use mutable issue text, stale summaries, numerical evidence, or odd-prime theorems as substitute authority.

## Canonical read order

After re-fetching protected live heads, read:

1. this file;
2. `handoffs/BSD-001/WP60J_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60J_BSS_RESIDUAL_HYP32/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60J_BSS_RESIDUAL_HYP32/01_SELECTED_RESIDUAL_HYP32_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60J_BSS_RESIDUAL_HYP32/03_CLAIM_LEDGER.yaml`;
6. `handoffs/BSD-001/WP60I_FRONTIER.md` and the WP60I theorem/certificate package;
7. the protected WP60H four-fiber relation package;
8. the protected WP60G self-dual pairwise-localization package;
9. the protected WP60F proof-boundary package;
10. the protected WP60E finite-level barrier package;
11. the protected WP60D surviving-route reduction;
12. the protected WP60B Kriz–Li obstruction;
13. the protected WP60A determinant-membership package;
14. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
15. protected MATHFORGE WP60H/WP60G/WP60F/WP60E/WP60B/WP60A/WP59 source records;
16. only then deeper predecessors needed by the active lane.

## Governing invariant

Define

`delta_2(E)
 := ord_2(L'(E,1)/(Omega_E Reg_E))
    - sum_{ell|N} ord_2(c_ell)`.

Protected WP16A/WP16B/WP19 give

`v_2(Fitt^1_{Z_2}(X_E))
 = len_Z2 Sha(E/Q)[2^infinity]
 = lim_n(ord_2 #Sel_{2^n}(E/Q)-n)`.

The selected theorem is exactly

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

## Protected route reductions

Protected WP55A–WP58A give the exact auxiliary-quadratic formula

`delta_2(E)
 = 1 + 2ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N}ord_2(c_ell)`,

with `lambda_D=L(E^D,1)/Omega(E^D)` and `ord_2(C_f)=0` for the fixed source-compatible parametrization.

Protected WP59 defines

`R_2(E,K,f)=2ord_2(m_K(f))-ord_2(lambda_D)`.

Protected WP60D proves

`R_2(E,K,f)
 = ord_2(L'(E,1)/(Omega_E Reg_E))
   -1+ord_2(c_infinity(E))`,

so `R_2` is auxiliary-field invariant. This does not determine its value.

Protected WP60B proves the selected good-ordinary-at-2 lane forces the normalized Kriz–Li logarithmic factor to be even. Therefore

`R3_RETIRED_FOR_SELECTED_GOOD_ORDINARY_LANE_BY_WP60B_LOCAL_OBSTRUCTION`.

Protected WP60E shows the specifically screened finite-level Burns–Kurihara–Sano / Chan-Ho Kim application theorems exclude literal `p=2` in the relevant proved clauses:

`MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.

## BSS literal-p=2 chain

### WP60F

The BSS route splits into two logically distinct obligations:

- F1: `MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`;
- F2: elliptic standard-hypothesis verification.

The higher-derivative construction is distinct from integral Fitting control.

### WP60G

Using the admitted BSS Lemma 3.9 affine-fiber interface and residual self-duality, WP60G proves the literal-2 one-primal/one-dual simultaneous-localization step whenever BSS Hypothesis 3.2 holds. The Weil pairing supplies

`E[2] ~= E[2]^*(1)`.

### WP60H

WP60H proves the exact self-dual `F_2` covering criterion: BSS bad affine fibers cover the residual Galois group if and only if their classes admit an odd-cardinality linear dependence. For four nonzero classes, coverage occurs exactly when some three sum to zero.

Hence the residual F1 frontier is

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

### WP60I

WP60I proves that every selected curve has an odd bad prime with odd multiplicative inertia depth. The corresponding primitive unipotent lies in the restricted cyclotomic 2-adic image, so formal BSS `(H2)` holds.

It further proves

`rho_4(G_{Q(mu_{2^infinity})})=SL_2(Z/4)`

and

`rho_4(G_Q)=GL_2(Z/4)`.

An exact finite certificate proves

`H^1(GL_2(Z/4),F_2^2) != 0`,

which inflates to a nonzero BSS III infinite `(H3)` group. Thus

`BSS_LITERAL_P2_SELECTED_H2_HOLDS_H3_FAILS`

and

`R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.

This is a negative applicability result for the screened standard BSS application theorem, not a no-go theorem for every literal-2 Kolyvagin/Fitting method.

### WP60J

WP60J distinguishes the finite residual BSS II hypothesis from the infinite BSS III `(H3)` condition.

Using the primitive odd-inertia transvection from WP60I together with protected residual `S3`, WP60J proves

`im(rho_{E,2-adic})=GL_2(Z_2)`.

For `K=Q`, `R=k=F_2`, `A=E[2]`, the finite BSS auxiliary field is

`K(A)_2=Q(E[2])Q(i)`.

The odd ramified transposition implies

`Q(E[2]) intersect Q(i)=Q`,

so

`Gal(K(A)_2/Q)=S3 x C2`.

The natural `S3`-module `E[2]` has no invariants and

`H^1(S3,E[2])=0`.

Because the extra `C2` acts trivially and `E[2]^S3=0`, inflation-restriction gives

`H^1(S3 x C2,E[2])=0`.

Weil self-duality gives the same statement for the dual coefficient module. Together with the primitive unipotent quotient this verifies BSS II Hypotheses 3.2 and 3.3 for the selected residual module.

Record

`SELECTED_2ADIC_IMAGE_GL2_Z2`,

`BSS_LITERAL_P2_SELECTED_RESIDUAL_HYP32_HYP33_HOLD`,

and

`WP60G_WP60H_RESIDUAL_HYP32_CONDITIONALITY_DISCHARGED`.

This does not contradict WP60I: the finite residual cohomology group vanishes while the higher 2-power/infinite division tower creates the nonzero `(H3)` obstruction.

## Current route map

- R1: live — `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: live — `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired on selected lane by WP60B.
- R4: live but reduced — `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT: live — `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: live — `MISSING_P2_DETERMINAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- R5 finite-level screened architecture: `MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.
- R5-BSS-F1 parent: `MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.
- R5-BSS-F1 residual frontier: `MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.
- R5-BSS standard integral application: blocked — `R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.
- D2a: live — `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: live — `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream — `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## Highest-value continuation after WP60J

Do not re-screen or attempt to prove the full BSS III `(H3)` condition; WP60I gives an explicit counter-obstruction.

The highest-value BSS-derived successor is instead a **Selmer-restricted all-level replacement**: determine whether the nonzero higher-level H3 defect classes are excluded by the actual canonical modified-Selmer local conditions, especially at the guaranteed odd multiplicative primitive-transvection prime. A successful theorem must trace every use of BSS Hypothesis 3.2(iii)/(H3) in the integral control proof, not merely Lemma 3.9.

In parallel:

1. attack the actual WP60H minimal-core three-term relation only if it feeds a replacement integral-control theorem;
2. retain direct height-one routes R5-LIFT and R5-PRIM;
3. retain R1/R2/R4 without reusing already-disproved or inapplicable seed hypotheses.

## Claim firewall

Do not promote:

- residual Hypothesis 3.2 to infinite `(H3)`;
- the full 2-adic image theorem to integral BSS Fitting control;
- WP60G/WP60H residual localization to graph connectivity without the three-term-relation step;
- existence of a higher derivative to Fitting equality;
- an odd-prime theorem to literal `p=2`;
- `m_K(f)` to odd or `lambda_D` to a 2-adic unit without proof;
- invariance of `R_2` to a value of `R_2`;
- any WP60 result to R5, D2d, or `BSD-R2-A1`;
- source admission, numerical evidence, or CI success to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head non-authoring/read-only Adversary and Referee review, affected ordinary CI, protected merge/readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, logging, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions. Bind every review, run, job, artifact, and merge to the current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or MATHCERT authority boundary.
