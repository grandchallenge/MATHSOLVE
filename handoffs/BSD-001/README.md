# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Active tracker: `grandchallenge/MATHSOLVE#215`.
- Current bounded operation: `grandchallenge/MATHSOLVE#235` (`WP60M`).
- Source authority: `grandchallenge/MATHFORGE`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- Certification authority: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Use protected repository state as authority. Do not use mutable issue text, stale summaries, numerical evidence, or odd-prime theorems as substitute authority.

## Canonical read order

After re-fetching protected live heads, read:

1. this file;
2. `handoffs/BSD-001/WP60M_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60M_BSS_ALL_LEVEL_SELMER_HYP32III/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60M_BSS_ALL_LEVEL_SELMER_HYP32III/01_ALL_LEVEL_SELMER_RESTRICTED_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60M_BSS_ALL_LEVEL_SELMER_HYP32III/03_CLAIM_LEDGER.yaml`;
6. protected WP60L mod-4 Selmer-restricted package;
7. protected WP60K mod-4 Hypothesis-3.2 obstruction package;
8. protected WP60J residual Hypothesis-3.2/full-image package;
9. protected WP60I H2/H3 package;
10. protected WP60H four-fiber relation package;
11. protected WP60G self-dual pairwise-localization package;
12. protected WP60F proof-boundary package;
13. protected WP60E finite-level barrier package;
14. protected WP60D surviving-route reduction;
15. protected WP60B Kriz–Li obstruction;
16. protected WP60A determinant-membership package;
17. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
18. protected MATHFORGE WP60H/WP60G/WP60F/WP60E/WP60B/WP60A/WP59 records;
19. only then deeper predecessors needed by the active lane.

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

Protected WP55A–WP60D reduce the arithmetic side but do not determine it. In particular:

- R1 is live: `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`;
- R2 is live: `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`;
- R3 is retired on the selected good-ordinary lane by WP60B;
- R4 is live but reduced: `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`;
- R5-LIFT is live: `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- R5-PRIM is live: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Protected WP60E records that the screened finite-level Kato-derivative/Fitting application theorems do not directly apply at literal `p=2`.

## BSS literal-p=2 chain

### WP60F–WP60H — localization/core-vertex boundary

WP60F separates derivative construction from integral Fitting control. WP60G repairs the residual one-primal/one-dual localization step under residual Hypothesis 3.2 using self-duality. WP60H proves the exact self-dual `F_2` affine-fiber covering criterion and leaves the residual connectivity frontier

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

### WP60I — infinite H3 fails

WP60I proves every selected curve has an odd bad prime with odd multiplicative inertia depth and a primitive unipotent in the restricted 2-adic image. Formal BSS H2 holds, but the infinite BSS III H3 group is nonzero. Record

`BSS_LITERAL_P2_SELECTED_H2_HOLDS_H3_FAILS`

and

`R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.

### WP60J — residual finite Hypothesis 3.2 holds

WP60J proves

`im(rho_{E,2-adic})=GL_2(Z_2)`

and verifies formal BSS II Hypotheses 3.2 and 3.3 for the residual module `E[2]`. This discharges the residual Hypothesis-3.2 conditionality in WP60G/WP60H.

### WP60K — unchanged finite Hypothesis 3.2 fails at mod 4

WP60K proves

`|H^1(GL_2(Z/4),(Z/4)^2)|=2`.

The nonzero class inflates into the BSS finite auxiliary group, so formal Hypothesis 3.2(iii) fails already at `E[4]`. Record

`BSS_LITERAL_P2_SELECTED_FINITE_HYP32III_FAILS_AT_E4`

and

`R5_BSS_STANDARD_FINITE_HYPOTHESIS_ROUTE_BLOCKED_ALREADY_AT_MOD4`.

### WP60L — the mod-4 defect is Selmer-extraneous

WP60L proves that the unique mod-4 defect is ramified at the protected odd-depth multiplicative prime. At that prime the propagated BSS canonical condition is the self-dual finite Kummer image. Hence the defect lies in neither the primal nor dual canonical local condition. Restriction is therefore injective on every canonical modified primal and dual Selmer group at `E[4]`, and the one-class Chebotarev calls used in BSS Lemma 3.10 can be replayed for the selected `E[4] -> E[2]` coefficient reduction.

### WP60M — all finite coefficient levels

For every `m>=2`, WP60M proves

`H^1(GL_2(Z/2^m),(Z/2^m)^2) ~= Z/2`.

The unique nonzero class is the scaled WP60K class. At the fixed protected primitive upper unipotent `U`,

`z_m(U)=(0,2^(m-1))`,

so primitive inertia detects the defect at every level.

The BSS auxiliary cyclotomic extension contributes no additional cohomology class. At the fixed odd-depth multiplicative prime, the unique defect is excluded from both primal and dual propagated canonical local conditions for every `m>=2`. Therefore restriction to the BSS finite auxiliary field is injective on every canonical modified primal and dual Selmer group at every finite coefficient level.

Record

`BSS_LITERAL_P2_SELECTED_ALL_LEVEL_HYP32III_DEFECT_SELMER_EXTRANEOUS`

and

`BSS_LITERAL_P2_SELECTED_ALL_LEVEL_SELMER_RESTRICTED_COEFFICIENT_REDUCTION_AVAILABLE`.

This removes the finite Hypothesis-3.2(iii) restriction-injectivity obstruction from the selected coefficient-reduction/inverse-limit chain. It does **not** make full Hypothesis 3.2(iii) true: the global finite cohomology groups remain nonzero.

## Current BSS frontier after WP60M

The surviving BSS-derived obstruction is now independent of finite cohomology vanishing:

`MISSING_P2_BSS_SIMULTANEOUS_LOCALIZATION_OR_REPLACEMENT_CONNECTIVITY`.

Protected WP60H sharpens its residual bottleneck to

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

The unchanged BSS Lemma 3.9 condition is `s+t<p`; at literal `p=2`, a simultaneous one-primal/one-dual call still fails the numerical inequality. A successor should attack the protected three-term relation directly or prove a replacement core-vertex/connectivity theorem that avoids that call.

Do not return to level-by-level Hypothesis-3.2(iii) verification; WP60M has resolved the Selmer-restricted all-level role.

## Current route map

- R1: live — `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: live — `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired by WP60B.
- R4: live but reduced — `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT: live — `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: live — `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- R5 finite-level screened application architecture: `MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.
- R5-BSS connectivity: `MISSING_P2_BSS_SIMULTANEOUS_LOCALIZATION_OR_REPLACEMENT_CONNECTIVITY`.
- R5-BSS residual bottleneck: `MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.
- unchanged standard finite BSS hypothesis route: blocked at mod 4.
- standard infinite BSS application: blocked by H3.
- D2a: live — `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: live — `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream — `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## Claim firewall

Do not promote:

- Selmer-restricted injectivity to full Hypothesis 3.2(iii);
- WP60M to simultaneous primal/dual localization;
- WP60G/WP60H localization to connectivity without the remaining relation step;
- WP60M to BSS Theorem 5.20, 5.2, 5.25, or Corollary 6.15 at literal `p=2` without a connectivity replacement;
- any WP60 result to R5, D2d, or `BSD-R2-A1`;
- source admission, numerical evidence, or CI success to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head non-authoring/read-only Adversary and Referee review, affected ordinary CI, protected merge/readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, logging, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions. Bind every review, run, job, artifact, and merge to the current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or MATHCERT authority boundary.
