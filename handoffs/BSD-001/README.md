# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Active tracker: `grandchallenge/MATHSOLVE#215`.
- Current bounded operation: `grandchallenge/MATHSOLVE#233` (`WP60L`).
- Source authority: `grandchallenge/MATHFORGE`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- Certification authority: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Use protected repository state as authority. Do not use mutable issue text, stale summaries, numerical evidence, or odd-prime theorems as substitute authority.

## Canonical read order

After re-fetching protected live heads, read:

1. this file;
2. `handoffs/BSD-001/WP60L_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60L_BSS_SELMER_RESTRICTED_HYP32III/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60L_BSS_SELMER_RESTRICTED_HYP32III/01_SELECTED_MOD4_SELMER_RESTRICTED_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60L_BSS_SELMER_RESTRICTED_HYP32III/03_CLAIM_LEDGER.yaml`;
6. the protected WP60K mod-4 Hypothesis-3.2 obstruction package;
7. the protected WP60J residual Hypothesis-3.2/full-image package;
8. the protected WP60I H2/H3 package;
9. the protected WP60H four-fiber relation package;
10. the protected WP60G self-dual pairwise-localization package;
11. the protected WP60F proof-boundary package;
12. the protected WP60E finite-level barrier package;
13. the protected WP60D surviving-route reduction;
14. the protected WP60B Kriz–Li obstruction;
15. the protected WP60A determinant-membership package;
16. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
17. protected MATHFORGE WP60H/WP60G/WP60F/WP60E/WP60B/WP60A/WP59 records;
18. only then deeper predecessors needed by the active lane.

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

Protected WP60B proves the selected good-ordinary-at-2 lane forces the normalized Kriz–Li logarithmic factor to be even. Thus

`R3_RETIRED_FOR_SELECTED_GOOD_ORDINARY_LANE_BY_WP60B_LOCAL_OBSTRUCTION`.

Protected WP60E shows the screened finite-level Burns–Kurihara–Sano / Chan-Ho Kim application theorems exclude literal `p=2` in the relevant proved clauses:

`MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.

## BSS literal-p=2 chain

### WP60F — proof-mechanism split

The BSS route separates a core-vertex/localization obligation from elliptic standard-hypothesis obligations. Higher-derivative construction is distinct from integral Fitting control.

### WP60G — residual pairwise localization

Using the admitted BSS Lemma 3.9 affine-fiber interface and residual self-duality, WP60G proves the literal-`2` one-primal/one-dual residual simultaneous-localization step whenever BSS Hypothesis 3.2 holds. The Weil pairing supplies `E[2] ~= E[2]^*(1)`.

### WP60H — four-fiber relation reduction

WP60H proves the exact self-dual `F_2` covering criterion: the BSS bad affine fibers cover the residual Galois group if and only if their classes admit an odd-cardinality linear dependence. For four nonzero classes, coverage occurs exactly when some three sum to zero.

Residual connectivity frontier:

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

### WP60I — infinite H3 obstruction

WP60I proves every selected curve has an odd bad prime with odd multiplicative inertia depth and hence a primitive unipotent in the restricted 2-adic image. Formal BSS `(H2)` holds.

It also proves

`rho_4(G_{Q(mu_{2^infinity})})=SL_2(Z/4)`

and

`rho_4(G_Q)=GL_2(Z/4)`.

An exact finite certificate gives

`H^1(GL_2(Z/4),F_2^2) != 0`,

which inflates to a nonzero BSS III infinite `(H3)` group. Record

`BSS_LITERAL_P2_SELECTED_H2_HOLDS_H3_FAILS`

and

`R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.

### WP60J — residual finite Hypothesis 3.2 holds

WP60J proves

`im(rho_{E,2-adic})=GL_2(Z_2)`.

For `K=Q`, `R=k=F_2`, `A=E[2]`, the finite BSS auxiliary group is `S3 x C2`, and

`H^1(S3 x C2,E[2])=0`.

Together with residual irreducibility, the primitive unipotent quotient, and Weil self-duality, this verifies formal BSS II Hypotheses 3.2 and 3.3 for the selected residual module. Record

`SELECTED_2ADIC_IMAGE_GL2_Z2`,

`BSS_LITERAL_P2_SELECTED_RESIDUAL_HYP32_HYP33_HOLD`,

and

`WP60G_WP60H_RESIDUAL_HYP32_CONDITIONALITY_DISCHARGED`.

### WP60K — finite Hypothesis 3.2 fails at mod 4

Protected WP60J gives

`Gal(Q(E[4])/Q)=GL_2(Z/4)`.

WP60K's exact exhaustive certificate proves

`|H^1(GL_2(Z/4),(Z/4)^2)|=2`.

Inflation into the BSS finite auxiliary field gives

`H^1(K(E[4])_4/Q,E[4]) != 0`.

Hence formal BSS II Hypothesis 3.2(iii) fails already at `E[4]`; the dual clause fails by Weil self-duality. Record

`BSS_LITERAL_P2_SELECTED_FINITE_HYP32III_FAILS_AT_E4`

and

`R5_BSS_STANDARD_FINITE_HYPOTHESIS_ROUTE_BLOCKED_ALREADY_AT_MOD4`.

The unchanged level-by-level verification strategy is therefore impossible.

### WP60L — the mod-4 defect is Selmer-extraneous

WP60L determines the exact finite auxiliary field more sharply. With `L=Q(E[4])`, full 2-adic image supplies an element congruent to the identity modulo `4` whose determinant is `5 mod 8`; hence

`L intersect Q(mu_8)=Q(mu_4)`

and

`[K(E[4])_4:L]=2`.

Inflation-restriction plus `E[2]^{GL_2(F_2)}=0` shows inflation is an isomorphism, so

`#H^1(K(E[4])_4/Q,E[4])=2`.

The unique nonzero class is the WP60K class. At the protected odd-depth multiplicative prime `ell`, its primitive-inertia value is `(0,2)` and is nonzero in inertia cohomology.

Protected WP13 makes `c_ell` odd. Protected WP39 then gives

`H^1(Q_ell,T_2E)=H^1_ur(Q_ell,T_2E)`.

Thus the BSS canonical local condition propagated to `E[4]` is the local Kummer image. Tate local duality and the Weil pairing make this Kummer image self-annihilating. The unique ramified defect therefore lies in neither the primal nor dual canonical local condition.

Every BSS modified Selmer structure retains the original canonical local condition at this fixed bad prime. Therefore restriction to `K(E[4])_4` is injective on every canonical modified primal and dual Selmer group at coefficient level `E[4]`.

Record

`BSS_LITERAL_P2_SELECTED_MOD4_HYP32III_DEFECT_SELMER_EXTRANEOUS`

and

`BSS_LITERAL_P2_SELECTED_MOD4_SELMER_RESTRICTED_COEFFICIENT_REDUCTION_AVAILABLE`.

This repairs the Hypothesis-3.2(iii) restriction-injectivity contribution to the one-class Chebotarev calls used in the proof of BSS Lemma 3.10 for the `E[4] -> E[2]` coefficient-reduction step. It does not repair the independent `s+t<p` obstruction for simultaneous primal/dual localization and does not extend automatically to higher `2`-power levels.

The refined BSS replacement frontier is

`MISSING_P2_BSS_ALL_LEVEL_SELMER_RESTRICTED_INJECTIVITY_AND_P2_CONNECTIVITY_CONTROL`.

## Current route map

- R1: live — `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: live — `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired on selected lane by WP60B.
- R4: live but reduced — `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT: live — `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: live — `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- R5 finite-level screened application architecture: `MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.
- R5-BSS residual connectivity: `MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.
- R5-BSS replacement control: `MISSING_P2_BSS_ALL_LEVEL_SELMER_RESTRICTED_INJECTIVITY_AND_P2_CONNECTIVITY_CONTROL`.
- R5-BSS unchanged standard finite hypothesis route: blocked at mod 4 — `R5_BSS_STANDARD_FINITE_HYPOTHESIS_ROUTE_BLOCKED_ALREADY_AT_MOD4`.
- R5-BSS standard infinite application: blocked — `R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.
- D2a: live — `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: live — `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream — `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## Highest-value continuation after WP60L

Do not try to restore the unchanged full Hypothesis 3.2(iii); WP60K proves it false. Instead test the WP60L mechanism uniformly over `A_m=E[2^m]`:

1. determine `H^1(K(E[2^m])_{2^m}/Q,E[2^m])` for all `m>=2` using protected full `GL_2(Z_2)` image;
2. test whether all nonzero restriction-kernel classes are detected by the same primitive odd-inertia element and hence excluded from all canonical modified Selmer spaces;
3. if successful, formulate the all-level Selmer-restricted replacement needed by coefficient reduction and inverse-limit control;
4. separately resolve or bypass the residual simultaneous-localization/core-vertex connectivity frontier from WP60H.

Retain direct height-one R5-LIFT/R5-PRIM and arithmetic routes R1/R2/R4 independently.

## Claim firewall

Do not promote:

- residual or mod-4 restricted injectivity to full Hypothesis 3.2(iii);
- WP60L to higher coefficient levels without proof;
- WP60L to simultaneous one-primal/one-dual localization;
- WP60G/WP60H localization to connectivity without the remaining relation step;
- existence of a higher derivative to Fitting equality;
- any odd-prime theorem to literal `p=2`;
- any WP60 result to R5, D2d, or `BSD-R2-A1`;
- source admission, numerical evidence, or CI success to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head non-authoring/read-only Adversary and Referee review, affected ordinary CI, protected merge/readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, logging, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions. Bind every review, run, job, artifact, and merge to the current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or MATHCERT authority boundary.
