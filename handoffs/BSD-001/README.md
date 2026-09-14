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
2. `handoffs/BSD-001/WP60G_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60G_SELF_DUAL_P2_PAIRWISE_LOCALIZATION/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60G_SELF_DUAL_P2_PAIRWISE_LOCALIZATION/01_SELF_DUAL_PAIRWISE_LOCALIZATION_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60G_SELF_DUAL_P2_PAIRWISE_LOCALIZATION/02_CLAIM_LEDGER.yaml`;
6. protected WP60F proof-boundary package;
7. protected WP60E finite-level barrier package;
8. protected WP60D surviving-route reduction;
9. protected WP60B Kriz–Li obstruction;
10. protected WP60A-A1 determinant-membership theorem;
11. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
12. protected MATHFORGE WP60G/WP60F/WP60E/WP60B/WP60A/WP59 source records;
13. only then deeper predecessors needed by the active lane.

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

WP60A-A1 proves that determinant membership for the fixed Kato class at the cyclotomic height-one prime `(2)` is exactly the missing one-sided Fitting divisibility. The live R5 obligations are:

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

## WP60E finite-level R5 barrier

Protected MATHFORGE WP60E at

`8d49d253fd10708f09b8cafa262de276bed88f23`

shows that the specifically screened finite-level Burns–Kurihara–Sano / Chan-Ho Kim Fitting and determinantal interfaces exclude literal `p=2` in the relevant proved clauses.

Record the subordinate boundary:

`MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.

Do not rescreen the same application theorems unless a new literal-`2` theorem or an actual hypothesis-removal proof appears.

## WP60F foundational BSS split

Protected MATHFORGE WP60F at

`eaaf7b8c660f3f07030608b3af1334ece5598586`

isolates two distinct literal-`2` obligations in the BSS finite-level route:

- F1: `MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`;
- F2: `MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.

Route classification:

`BSS_LITERAL_P2_R5_ROUTE_REQUIRES_F1_AND_F2`.

The higher-derivative construction is distinct from integral Fitting control. Fixing only F1 or only F2 cannot close the full BSS route.

## WP60G self-dual pairwise localization

Protected MATHFORGE WP60G at

`7da6813fcde7eb5f9badd7c86946f58691ed6f0d`

admits the exact BSS Lemma 3.9 affine-fiber interface. In the residual `F_2` case, every nonzero BSS cohomology-to-character map has target `F_2`, so every bad set is an affine index-two fiber.

WP60G proves the abstract covering criterion:

For nonzero `chi_1,chi_2:G->F_2` and `H_i=chi_i^{-1}(a_i)`,

`H_1 union H_2 = G`

if and only if

`chi_1=chi_2` and `a_1 != a_2`.

If `A ~= A^*(1)` `G_K`-equivariantly, the BSS maps and affine constants are natural under this self-duality. For one nonzero primal class and one nonzero dual class:

- unequal residual characters cannot cover by the two-fiber lemma;
- equal residual characters identify the cohomology classes by injectivity of the BSS map, and then naturality identifies the affine constants, so the bad fibers coincide rather than complement each other.

Therefore, under BSS Hypothesis 3.2, the one-primal/one-dual literal-`2` simultaneous-localization step is recovered for self-dual residual modules.

For elliptic curves the Weil pairing supplies the required self-duality

`E[2] ~= E[2]^*(1)`.

This does not prove BSS Hypothesis 3.2/H2/H3 uniformly for the selected class; F2 remains live.

### Exact F1 refinement

The published `s+t<p` count is no longer the obstruction for `s=t=1` in the self-dual residual elliptic setting, conditional on the remaining BSS hypotheses.

This repairs the pairwise counting step used in BSS Lemma 5.14 and the corresponding pairwise step in Lemma 5.17.

It does not repair BSS Lemma 5.15 with `s=2`, where one common prime must satisfy two primal and two dual nonvanishing constraints. Corollary 5.16 uses exactly that step to connect two minimal core vertices.

Record the refined live boundary:

`MISSING_P2_TWO_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_OR_REPLACEMENT_CONNECTIVITY`.

Keep parent F1 open until sufficient graph/Kolyvagin control is recovered:

`MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.

## Current route map

- R1: live — `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: live — `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired on selected lane by WP60B.
- R4: live but reduced — `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT: live — `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: live — `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- R5 finite-level screened architecture: `MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.
- R5-BSS-F1 parent: `MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.
- R5-BSS-F1 refined graph boundary: `MISSING_P2_TWO_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_OR_REPLACEMENT_CONNECTIVITY`.
- R5-BSS-F2: `MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.
- D2a: live — `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: live — `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream — `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## Highest-value continuation after WP60G

Stay on F1 and attack BSS Corollary 5.16 directly.

Two permitted modes:

1. **four-fiber mode**: prove that the four actual BSS affine bad fibers arising from two minimal core vertices cannot cover the residual Galois group, using relations forced by the modified Selmer structures, global duality, and self-duality; or
2. **replacement-connectivity mode**: replace the common-prime construction of Corollary 5.16 by another proof that minimal core vertices lie in one connected component.

The replacement-connectivity mode may test a basis-exchange or matroid-like formulation, but such structure must be derived from the actual BSS modified Selmer conditions before use. Do not infer it by analogy.

A generic hyperplane-counting argument is insufficient: four affine index-two fibers can cover an `F_2` quotient in general.

If minimal-core connectivity is recovered, replay the rest of the graph/Kolyvagin-control chain and identify any next literal-`2` dependency before claiming F1 closure.

F2 remains a parallel independent obligation and must be handled through exact restricted `2`-adic image/cohomology, not residual surjectivity by assertion.

## Claim firewall

Do not promote:

- `m_K(f)` to odd without proof;
- `lambda_D` to a `2`-adic unit or exact valuation without proof;
- invariance of `R_2` to a value of `R_2`;
- an odd-prime finite-level theorem to literal `p=2`;
- existence of a higher derivative to integral Fitting control;
- WP60G pairwise localization to four-constraint localization or graph connectivity;
- residual `E[2]` self-duality or surjectivity to BSS Hypothesis 3.2/H2/H3 without proof;
- the WP60E/WP60F/WP60G bounded results to general no-go or full R5 theorems;
- R1, R2, R4, R5, D2a, D2d, or D2e to resolved without exact protected proof;
- source admission, numerical evidence, or CI success to MATHCERT certification;
- `BSD-R2-A1`, novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge/readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, logging, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions. Bind every review, run, job, artifact, and merge to the current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or MATHCERT authority boundary.
