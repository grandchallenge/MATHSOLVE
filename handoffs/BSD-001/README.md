# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Active tracker: `grandchallenge/MATHSOLVE#215`.
- Source authority: `grandchallenge/MATHFORGE`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- Certification authority: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Use protected repository state as authority. Do not use mutable issue text, stale summaries, numerical evidence, or odd-prime theorems as substitute authority.

## Canonical read order

After re-fetching protected live heads, read:

1. this file;
2. `handoffs/BSD-001/WP60E_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60E_FINITE_LEVEL_R5_BARRIER/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60E_FINITE_LEVEL_R5_BARRIER/01_FINITE_LEVEL_R5_BARRIER_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60E_FINITE_LEVEL_R5_BARRIER/02_CLAIM_LEDGER.yaml`;
6. `handoffs/BSD-001/WP60D_FRONTIER.md` and the WP60D theorem package;
7. `handoffs/BSD-001/WP60B_FRONTIER.md` and the WP60B theorem package;
8. protected WP60A-A1 for the determinant-membership theorem;
9. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
10. protected MATHFORGE WP60E/WP60B/WP60A/WP59 records;
11. only then deeper predecessors needed by the active lane.

## Governing invariant

`delta_2(E)
 := ord_2(L'(E,1)/(Omega_E Reg_E))
    - sum_{ell|N}ord_2(c_ell)`.

Protected WP16A/WP16B/WP19 give

`v_2(Fitt^1_{Z_2}(X_E))
 = len_Z2 Sha(E/Q)[2^infinity]
 = lim_n(ord_2 #Sel_{2^n}(E/Q)-n)`.

The selected theorem is exactly

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

## Protected arithmetic reduction

Protected WP55A–WP58A give

`delta_2(E)
 = 1 + 2ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N}ord_2(c_ell)`,

where

`lambda_D=L(E^D,1)/Omega(E^D) in Q^x`

and `ord_2(C_f)=0` for the fixed source-compatible parametrization.

Protected WP59 defines

`R_2(E,K,f)=2ord_2(m_K(f))-ord_2(lambda_D)`.

## WP60A determinant reduction

WP60A-A1 proves that determinant membership for the fixed Kato class at the cyclotomic height-one prime `(2)` is exactly the one-sided Fitting divisibility. The live R5 obligations are:

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Do not replace either obligation by an away-from-`(2)` or after-inverting-`2` theorem.

## WP60B Kriz–Li route disposition

Protected WP60B proves that the selected good-ordinary-at-`2` hypotheses force the normalized Kriz–Li logarithmic factor to be even. Thus Kriz–Li Assumption `(F)` cannot hold on the selected branch.

Disposition:

`R3_RETIRED_FOR_SELECTED_GOOD_ORDINARY_LANE_BY_WP60B_LOCAL_OBSTRUCTION`.

R1 remains the genuine Heegner-index boundary:

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.

## WP60D combined-residual reduction

Protected WP60D proves

`c_infinity(E^D)=c_infinity(E)`

for quadratic twists and therefore

`R_2(E,K,f)
 = ord_2(L'(E,1)/(Omega_E Reg_E))
   -1+ord_2(c_infinity(E))`.

Hence `R_2` is independent of `K`.

R4 is exactly classified as

`R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.

R4 remains logically live, but auxiliary-field selection cannot change the combined residual.

## WP60E finite-level R5 source-interface barrier

Protected MATHFORGE WP60E at

`8d49d253fd10708f09b8cafa262de276bed88f23`

audits the specifically identified finite-level derivative/determinantal/Fitting frameworks.

The admitted interfaces give:

- Burns–Kurihara–Sano's concrete finite-level Fitting containment only for `p>3`;
- their determinantal Mazur–Tate follow-up under a standing hypothesis that explicitly excludes `p=2`;
- Chan-Ho Kim's finite-layer framework for odd `p`, with the principal structural theorem requiring `p>=5`.

Therefore none of these protected interfaces can be specialized to prove the selected literal-`p=2` R5 obligations.

Record the subordinate bounded source/proof boundary

`MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.

This does not replace R5-LIFT or R5-PRIM and is not a theorem-nonexistence or literature-exhaustiveness claim.

### WP60E reopening contract

Do not rescreen the same Burns–Kurihara–Sano/Kim application theorems. Reopen this finite-level route only on:

1. an actual theorem with the required integral Fitting/determinantal conclusion whose standing hypotheses permit literal `p=2`;
2. an independent proof removing the cited odd-prime restriction while retaining the integral Fitting statement, local conditions, and normalization; or
3. a new direct finite-level primitive Kummer/Fitting theorem at literal `p=2`.

A result only after inverting `2`, modulo a `2`-power error, or away from `(2)` is insufficient.

## Current route map

- R1: live — `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: live — `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired on selected lane by WP60B.
- R4: live but reduced to the fixed base analytic leading-term valuation.
- R5-LIFT: live — `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: live — `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- R5 finite-level screened architecture: bounded by `MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.
- D2a: live — `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: live — `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream — `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## Highest-value continuation after WP60E

Stay on R5 proof construction rather than another broad application-paper search.

The immediate successor is to audit the proof mechanism underlying the odd-prime finite-level theorem, beginning with the equivariant higher-rank Euler/Kolyvagin/Stark-system result cited by Burns–Kurihara–Sano as `[10, Th. 6.11]`.

Required sequence:

1. identify the exact foundational theorem and its standing prime hypotheses;
2. locate each point where oddness or `p>3` is used;
3. distinguish an elliptic-image verification issue from a foundational `p=2` obstruction in the Kolyvagin/core-vertex machinery;
4. test whether protected selected hypotheses, especially surjective `E[2]`, replace the relevant lemma without assuming the desired Fitting conclusion;
5. if replacement is possible, construct the literal-`2` theorem and replay WP60A-A1 exactly;
6. otherwise record the minimal proof-construction boundary and move to the next genuinely independent route.

Do not infer that an odd-prime hypothesis is removable merely because it looks technical.

## Claim firewall

Do not promote:

- `m_K(f)` to odd without proof;
- `lambda_D` to a `2`-adic unit or exact valuation without proof;
- invariance of `R_2` to a value of `R_2`;
- an odd-prime finite-level theorem to literal `p=2`;
- the WP60E bounded source barrier to a general no-go theorem;
- R1, R2, R4, R5, D2a, D2d, or D2e to resolved without exact protected proof;
- source admission, numerical evidence, or CI success to MATHCERT certification;
- `BSD-R2-A1`, novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge/readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, logging, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions. Bind every review, run, job, artifact, and merge to the current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or MATHCERT authority boundary.
