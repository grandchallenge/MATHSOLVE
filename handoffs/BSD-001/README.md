# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Active tracker: `grandchallenge/MATHSOLVE#215`.
- Current bounded operation: `grandchallenge/MATHSOLVE#229` (`WP60K`).
- Source authority: `grandchallenge/MATHFORGE`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- Certification authority: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Use protected repository state as authority. Do not use mutable issue text, stale summaries, numerical evidence, or odd-prime theorems as substitute authority.

## Canonical read order

After re-fetching protected live heads, read:

1. this file;
2. `handoffs/BSD-001/WP60K_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60K_BSS_MOD4_HYP32_OBSTRUCTION/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60K_BSS_MOD4_HYP32_OBSTRUCTION/01_SELECTED_MOD4_HYP32_OBSTRUCTION_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60K_BSS_MOD4_HYP32_OBSTRUCTION/03_CLAIM_LEDGER.yaml`;
6. the protected WP60J residual Hypothesis-3.2/full-image package;
7. the protected WP60I H2/H3 package;
8. the protected WP60H four-fiber relation package;
9. the protected WP60G self-dual pairwise-localization package;
10. the protected WP60F proof-boundary package;
11. the protected WP60E finite-level barrier package;
12. the protected WP60D surviving-route reduction;
13. the protected WP60B Kriz–Li obstruction;
14. the protected WP60A determinant-membership package;
15. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
16. protected MATHFORGE WP60H/WP60G/WP60F/WP60E/WP60B/WP60A/WP59 records;
17. only then deeper predecessors needed by the active lane.

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

## Protected arithmetic route reductions

Protected WP55A–WP58A give

`delta_2(E)
 = 1 + 2ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N}ord_2(c_ell)`,

where `lambda_D=L(E^D,1)/Omega(E^D)` and `ord_2(C_f)=0` for the fixed source-compatible parametrization.

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

### WP60F — proof-mechanism split

The BSS route splits into a core-vertex/localization obligation and elliptic standard-hypothesis obligations. The higher-derivative construction is distinct from integral Fitting control.

### WP60G — residual pairwise localization

Using the admitted BSS Lemma 3.9 affine-fiber interface and residual self-duality, WP60G proves the literal-`2` one-primal/one-dual simultaneous-localization step whenever BSS Hypothesis 3.2 holds. The Weil pairing supplies

`E[2] ~= E[2]^*(1)`.

### WP60H — four-fiber relation reduction

WP60H proves the exact self-dual `F_2` covering criterion: BSS bad affine fibers cover the residual Galois group if and only if their classes admit an odd-cardinality linear dependence. For four nonzero classes, coverage occurs exactly when some three sum to zero.

The residual connectivity frontier is

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

### WP60I — infinite H3 obstruction

WP60I proves every selected curve has an odd bad prime with odd multiplicative inertia depth and hence a primitive unipotent in the restricted 2-adic image. Formal BSS `(H2)` holds.

It further proves

`rho_4(G_{Q(mu_{2^infinity})})=SL_2(Z/4)`

and

`rho_4(G_Q)=GL_2(Z/4)`.

An exact finite certificate gives

`H^1(GL_2(Z/4),F_2^2) != 0`,

which inflates to a nonzero BSS III infinite `(H3)` group. Thus

`BSS_LITERAL_P2_SELECTED_H2_HOLDS_H3_FAILS`

and

`R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.

This is a negative applicability result for the screened standard BSS application theorem, not a no-go theorem for every literal-`2` Kolyvagin/Fitting method.

### WP60J — residual finite Hypothesis 3.2 holds

WP60J proves

`im(rho_{E,2-adic})=GL_2(Z_2)`.

For `K=Q`, `R=k=F_2`, `A=E[2]`, it identifies the finite BSS auxiliary Galois group as `S3 x C2` and proves

`H^1(S3 x C2,E[2])=0`.

Together with irreducibility, the primitive unipotent quotient, and Weil self-duality, this verifies formal BSS II Hypotheses 3.2 and 3.3 for the selected residual module.

Record

`SELECTED_2ADIC_IMAGE_GL2_Z2`,

`BSS_LITERAL_P2_SELECTED_RESIDUAL_HYP32_HYP33_HOLD`,

and

`WP60G_WP60H_RESIDUAL_HYP32_CONDITIONALITY_DISCHARGED`.

### WP60K — finite Hypothesis 3.2 fails at mod 4

WP60K tests the next finite coefficient level rather than extrapolating the residual result.

Protected WP60J gives

`Gal(Q(E[4])/Q)=GL_2(Z/4)`.

An exact exhaustive certificate proves

`|H^1(GL_2(Z/4),(Z/4)^2)|=2`.

For `A=E[4]`, the BSS finite auxiliary field `K(A)_4` contains `Q(E[4])`. Its Galois group surjects onto `GL_2(Z/4)` with kernel acting trivially on `A`; inflation therefore injects the displayed nonzero group into

`H^1(K(A)_4/Q,E[4])`.

Hence formal BSS II Hypothesis 3.2(iii) fails already at `E[4]`; Weil self-duality gives the same obstruction for the dual module.

Record

`BSS_LITERAL_P2_SELECTED_FINITE_HYP32III_FAILS_AT_E4`

and

`R5_BSS_STANDARD_FINITE_HYPOTHESIS_ROUTE_BLOCKED_ALREADY_AT_MOD4`.

WP60J and WP60K are compatible: the finite residual condition holds at `E[2]` and fails at `E[4]`. WP60I separately records the infinite-tower failure.

The BSS replacement-control frontier is now

`MISSING_P2_BSS_HYP32III_WEAKENING_OR_BYPASS_FOR_INTEGRAL_FITTING_CONTROL`.

## Current route map

- R1: live — `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: live — `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired on selected lane by WP60B.
- R4: live but reduced — `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT: live — `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: live — `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- R5 finite-level screened application architecture: `MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.
- R5-BSS residual F1: `MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.
- R5-BSS replacement control: `MISSING_P2_BSS_HYP32III_WEAKENING_OR_BYPASS_FOR_INTEGRAL_FITTING_CONTROL`.
- R5-BSS unchanged standard finite hypothesis route: blocked at mod 4 — `R5_BSS_STANDARD_FINITE_HYPOTHESIS_ROUTE_BLOCKED_ALREADY_AT_MOD4`.
- R5-BSS standard infinite application: blocked — `R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.
- D2a: live — `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: live — `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream — `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## Highest-value continuation after WP60K

Do not try to verify the unchanged BSS finite Hypothesis 3.2 level-by-level: WP60K proves this strategy fails at `E[4]`. Do not try to re-prove the full BSS III `(H3)` condition: WP60I proves it fails.

The highest-value BSS-derived successor is now a **weakened finite control theorem**. Trace every use of Hypothesis 3.2(iii) in the BSS localization/core-vertex/Fitting proof and determine whether the nonzero mod-4 cohomology class is actually relevant to the Selmer classes used by the argument. A successful replacement may use a smaller Selmer-restricted injectivity statement, an explicit quotient by the obstruction direction, or a different integral control argument.

Only if such a replacement still needs full residual core-vertex connectivity should the WP60H three-term-relation frontier be pursued in parallel.

Retain direct height-one routes R5-LIFT/R5-PRIM and arithmetic routes R1/R2/R4 independently.

## Claim firewall

Do not promote:

- residual Hypothesis 3.2 at `E[2]` to higher coefficient levels;
- the mod-4 obstruction to impossibility of all literal-`2` Kolyvagin/Fitting methods;
- the full 2-adic image theorem to integral Fitting control;
- WP60G/WP60H residual localization to graph connectivity without the remaining relation step;
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
