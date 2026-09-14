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
2. `handoffs/BSD-001/WP60I_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60I_BSS_H2_H3_SELECTED_LANE/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60I_BSS_H2_H3_SELECTED_LANE/01_SELECTED_P2_H2_H3_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60I_BSS_H2_H3_SELECTED_LANE/03_CLAIM_LEDGER.yaml`;
6. protected WP60H four-fiber relation package;
7. protected WP60G self-dual pairwise-localization package;
8. protected WP60F proof-boundary package;
9. protected WP60E finite-level barrier package;
10. protected WP60D surviving-route reduction;
11. protected WP60B Kriz–Li obstruction;
12. protected WP60A-A1 determinant-membership theorem;
13. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
14. protected MATHFORGE WP60H/WP60G/WP60F/WP60E/WP60B/WP60A/WP59 records;
15. only then deeper predecessors needed by the active lane.

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

`R3_RETIRED_FOR_SELECTED_GOOD_ORDINARY_LANE_BY_WP60B_LOCAL_OBSTRUCTION`.

R1 remains:

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.

## WP60D combined-residual reduction

Protected WP60D proves

`c_infinity(E^D)=c_infinity(E)`

and therefore

`R_2(E,K,f)
 = ord_2(L'(E,1)/(Omega_E Reg_E))
   -1+ord_2(c_infinity(E))`.

Hence `R_2` is independent of `K` and R4 is classified as

`R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.

## WP60E finite-level R5 barrier

Protected MATHFORGE WP60E at

`8d49d253fd10708f09b8cafa262de276bed88f23`

shows that the specifically screened Burns–Kurihara–Sano / Chan-Ho Kim Fitting and determinantal interfaces exclude literal `p=2` in the relevant proved clauses.

`MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.

Do not rescreen the same application theorems unless a new literal-`2` theorem or an actual hypothesis-removal proof appears.

## WP60F foundational BSS split

Protected MATHFORGE WP60F at

`eaaf7b8c660f3f07030608b3af1334ece5598586`

isolated two distinct literal-`2` obligations:

- F1: `MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`;
- F2: `MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.

The higher-derivative construction is distinct from integral Fitting control. WP60I now determines F2 negatively; this does not repair F1 and does not yield the BSS Fitting conclusion.

## WP60G self-dual pairwise localization

Protected MATHFORGE WP60G at

`7da6813fcde7eb5f9badd7c86946f58691ed6f0d`

admits the exact BSS Lemma 3.9 affine-fiber interface. Protected MATHSOLVE WP60G proves that under BSS Hypothesis 3.2 and residual self-duality, the literal-`2` one-primal/one-dual simultaneous-localization step is recovered.

For elliptic curves the Weil pairing supplies

`E[2] ~= E[2]^*(1)`.

This repairs the pairwise counting step used in BSS Lemma 5.14 and the corresponding pairwise step in Lemma 5.17. It does not prove full graph connectivity.

## WP60H four-fiber odd-relation reduction

Protected MATHFORGE WP60H at

`54f1eaea24b35d4ca37e778786345c3622b6fd98`

admits the exact minimal-core transition interface from BSS Lemmas 5.13–5.15 and Corollary 5.16.

WP60H proves the general self-dual `F_2` criterion: for nonzero classes `c_i`, the associated BSS bad affine fibers cover the residual Galois group if and only if the `c_i` admit an odd-cardinality linear dependence. For four nonzero classes, coverage occurs if and only if some three of the four classes sum to zero.

Thus the live F1 frontier is

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

The admitted dimension, inclusion, and finite/transverse statements do not themselves exclude the exceptional three-term relation.

## WP60I selected-lane BSS H2/H3 determination

WP60I uses protected WP12 residual `S3`, protected WP13 local inertia depth, and the protected MATHFORGE WP60F definitions of `(H2)` and `(H3)`.

It proves first that every selected curve must have an odd bad prime with odd multiplicative inertia depth. Otherwise the residual `S3` division field would be unramified outside `2`; a cubic subfield would then have discriminant at most `8`, contradicting Minkowski's cubic discriminant bound.

At such a prime, the WP13 Tate-inertia formula supplies a primitive unipotent inside

`G_{Q(mu_{2^infinity})}`.

Consequently formal literal-`2` BSS `(H2)` holds for `K=F=Q`.

The same element, residual `S3`, and normality imply

`rho_4(G_{Q(mu_{2^infinity})})=SL_2(Z/4)`

and

`rho_4(G_Q)=GL_2(Z/4)`.

An exact finite certificate proves

`H^1(GL_2(Z/4),F_2^2) != 0`.

Inflation to the full `2`-adic image gives a nonzero BSS `(H3)` group; the Weil pairing gives the same obstruction for the dual residual module. Therefore

`BSS_LITERAL_P2_SELECTED_H2_HOLDS_H3_FAILS`.

Replace the former F2 missing-verification boundary by

`R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.

This is a negative applicability result for the currently screened BSS standard-hypothesis architecture. It is not a no-go theorem for every possible literal-`2` Kolyvagin/Fitting argument. A theorem that removes, weakens, or bypasses `(H3)` is a legitimate reopening form.

## Current route map

- R1: live — `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: live — `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired on selected lane by WP60B.
- R4: live but reduced — `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT: live — `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: live — `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- R5 finite-level screened architecture: `MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.
- R5-BSS-F1 parent: `MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.
- R5-BSS-F1 WP60H frontier: `MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.
- R5-BSS-F2: determined negatively — `R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.
- D2a: live — `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: live — `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream — `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## Highest-value continuation after WP60I

The standard BSS application route should not be pursued by attempting to re-prove `(H3)` for the selected lane; WP60I gives an explicit obstruction.

Proceed on the surviving R5 fronts:

1. search for a literal-`2` Kolyvagin/Fitting theorem that removes, weakens, or bypasses BSS `(H3)`;
2. revisit the already-screened characteristic-`2` Nekovar-Selmer/Gorenstein machinery and test whether its exact hypotheses yield the protected determinant/Fitting target without the failed BSS condition;
3. continue the WP60H F1 relation/connectivity question only when it feeds a replacement control theorem whose hypotheses survive WP60I;
4. retain the direct height-one routes R5-LIFT and R5-PRIM.

## Claim firewall

Do not promote:

- `m_K(f)` to odd without proof;
- `lambda_D` to a `2`-adic unit or exact valuation without proof;
- invariance of `R_2` to a value of `R_2`;
- an odd-prime finite-level theorem to literal `p=2`;
- existence of a higher derivative to integral Fitting control;
- WP60G pairwise localization to four-constraint localization or graph connectivity;
- WP60H odd-relation reduction to exclusion of the actual three-term relation;
- WP60I failure of the BSS `(H3)` hypothesis to a general impossibility theorem for literal-`2` Kolyvagin/Fitting methods;
- the bounded WP60 results to R5, D2d, or `BSD-R2-A1`;
- source admission, numerical evidence, or CI success to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge/readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, logging, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions. Bind every review, run, job, artifact, and merge to the current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or MATHCERT authority boundary.
