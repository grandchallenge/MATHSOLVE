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
2. `handoffs/BSD-001/WP60F_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60F_BSS_P2_PROOF_BOUNDARIES/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60F_BSS_P2_PROOF_BOUNDARIES/01_BSS_P2_PROOF_BOUNDARY_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60F_BSS_P2_PROOF_BOUNDARIES/02_CLAIM_LEDGER.yaml`;
6. protected WP60E finite-level barrier package;
7. protected WP60D surviving-route reduction;
8. protected WP60B Kriz–Li obstruction;
9. protected WP60A-A1 determinant-membership theorem;
10. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
11. protected MATHFORGE WP60F/WP60E/WP60B/WP60A/WP59 source records;
12. only then deeper predecessors needed by the active lane.

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

## WP60F foundational BSS proof-boundary split

Protected MATHFORGE WP60F at

`eaaf7b8c660f3f07030608b3af1334ece5598586`

locates the small-prime dependence inside the underlying Burns–Sakamoto–Sano proof mechanism.

### F1 — core-vertex / simultaneous-localization control

`MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.

The admitted simultaneous-localization lemma requires `s+t<p`; the core-vertex connectivity step uses `2s<p`; the relevant Kolyvagin-system/Fitting-control theorems are proved under `p>3`.

At `p=2`, even the one-primal/one-dual case is outside the proved simultaneous-localization lemma.

### F2 — elliptic H2/H3 verification

`MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.

The admitted elliptic proof verifies H2/H3 from a large `p`-adic image using a `p>3` perfectness argument after restriction to the relevant pro-`p` extension. Protected residual surjectivity of `E[2]` does not, from the admitted interfaces, imply those exact hypotheses.

Record the exact route classification:

`BSS_LITERAL_P2_R5_ROUTE_REQUIRES_F1_AND_F2`.

The higher-derivative construction is a distinct interface from integral Fitting control. Do not promote the former to the latter.

Fixing only F1 or only F2 does not close this BSS route. Both must be supplied, or the route must be bypassed by a direct literal-`2` theorem.

## Current route map

- R1: live — `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: live — `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired on selected lane by WP60B.
- R4: live but reduced — `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT: live — `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: live — `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- R5 finite-level screened architecture: `MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.
- R5-BSS-F1: `MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.
- R5-BSS-F2: `MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.
- D2a: live — `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: live — `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream — `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## Highest-value continuation after WP60F

Stay on R5 theorem construction. Attack F1 before primary investment in F2 because F1 blocks the Fitting conclusion independently of the elliptic standard-hypothesis verification.

The immediate bounded research question is:

> Can the `s+t<p` / `2s<p` simultaneous-localization and core-vertex step be replaced at literal `p=2` for the protected selected two-dimensional representation, strongly enough to recover the one-sided integral Fitting containment without assuming it?

Required sequence:

1. reconstruct the exact subgroup-cover/Chebotarev argument behind BSS Lemma 3.9 for one primal and one dual class;
2. specialize the residual representation to the protected `GL_2(F_2)` image and determine the actual field intersections associated with those two classes;
3. decide whether the failure of `2<2` is only a counting-proof limitation or whether an explicit representation-theoretic obstruction exists;
4. if simultaneous localization can be recovered, prove the minimum literal-`2` core-vertex connectivity needed for the one-sided Fitting containment and replay WP60A-A1;
5. if an explicit obstruction exists, protect it and retire this BSS subroute only, preserving other R5 constructions;
6. in parallel, investigate F2 only through exact restricted `2`-adic image/cohomology calculations, never from residual surjectivity by assertion.

A result after inverting `2`, modulo a `2`-power error, or away from `(2)` remains insufficient.

## Claim firewall

Do not promote:

- `m_K(f)` to odd without proof;
- `lambda_D` to a `2`-adic unit or exact valuation without proof;
- invariance of `R_2` to a value of `R_2`;
- an odd-prime finite-level theorem to literal `p=2`;
- existence of a higher derivative to integral Fitting control;
- residual `E[2]` surjectivity to BSS H2/H3 without proof;
- the WP60E/WP60F bounded barriers to general no-go theorems;
- R1, R2, R4, R5, D2a, D2d, or D2e to resolved without exact protected proof;
- source admission, numerical evidence, or CI success to MATHCERT certification;
- `BSD-R2-A1`, novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge/readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, logging, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions. Bind every review, run, job, artifact, and merge to the current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or MATHCERT authority boundary.
