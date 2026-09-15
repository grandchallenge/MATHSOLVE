# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Active tracker: `grandchallenge/MATHSOLVE#215`.
- Current bounded operation: `grandchallenge/MATHSOLVE#237` (`WP60N`).
- Source authority: `grandchallenge/MATHFORGE`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- Certification authority: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Use protected repository state as authority. Do not use mutable issue text, stale summaries, numerical evidence, or odd-prime theorems as substitute authority.

## Canonical read order

After re-fetching protected live heads, read:

1. this file;
2. `handoffs/BSD-001/WP60N_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60N_COISOTROPIC_P2_CONNECTIVITY/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60N_COISOTROPIC_P2_CONNECTIVITY/01_COISOTROPIC_EXCHANGE_CONNECTIVITY_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60N_COISOTROPIC_P2_CONNECTIVITY/03_CLAIM_LEDGER.yaml`;
6. protected WP60M all-level Selmer-restricted package;
7. protected WP60L mod-4 Selmer-restricted package;
8. protected WP60K mod-4 Hypothesis-3.2 obstruction package;
9. protected WP60J residual Hypothesis-3.2/full-image package;
10. protected WP60I H2/H3 package;
11. protected WP60H four-fiber relation package;
12. protected WP60G self-dual pairwise-localization package;
13. protected WP60F proof-boundary package;
14. protected WP60E finite-level barrier package;
15. protected WP60D surviving-route reduction;
16. protected WP60B Kriz–Li obstruction;
17. protected WP60A determinant-membership package;
18. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
19. protected MATHFORGE WP60N/WP60H/WP60G/WP60F/WP60E/WP60B/WP60A/WP59 records;
20. only then deeper predecessors needed by the active lane.

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

- R1 is live: `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2 is live: `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3 is retired on the selected good-ordinary lane by WP60B.
- R4 is live but reduced: `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT is live: `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM is live: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- the screened finite-level Kato-derivative/Fitting application theorems still do not directly apply at literal `p=2`.

## BSS literal-p=2 chain

### WP60G–WP60H — relation reduction

WP60G repairs the residual one-primal/one-dual localization step using self-duality. WP60H proves the exact self-dual `F_2` affine-fiber covering criterion: four bad fibers cover exactly when some three source classes sum to zero. It reduces minimal-core failure to a precise three-term relation.

### WP60I–WP60M — cohomology/hypothesis layer

WP60I proves formal H2 but proves the infinite BSS III H3 group is nonzero:

`BSS_LITERAL_P2_SELECTED_H2_HOLDS_H3_FAILS`.

WP60J verifies residual BSS II Hypotheses 3.2/3.3 and proves full selected `GL_2(Z_2)` image. WP60K proves unchanged formal finite Hypothesis 3.2(iii) fails already at `E[4]`. WP60L proves the mod-4 defect is excluded from both canonical primal and dual local conditions. WP60M proves uniformly for every `m>=2` that the unique finite cohomological defect remains Selmer-extraneous, so restriction to the finite BSS auxiliary field is injective on every canonical modified primal and dual Selmer group at every finite coefficient level.

Record

`BSS_LITERAL_P2_SELECTED_ALL_LEVEL_HYP32III_DEFECT_SELMER_EXTRANEOUS`

and

`BSS_LITERAL_P2_SELECTED_ALL_LEVEL_SELMER_RESTRICTED_COEFFICIENT_REDUCTION_AVAILABLE`.

Formal global Hypothesis 3.2(iii) remains false; do not conflate Selmer-restricted injectivity with global cohomology vanishing.

### WP60N — characteristic-two connectivity under coisotropy

Protected MATHFORGE WP60N admits the residual-coisotropy plane decomposition and proves that the post-minimal arbitrary-core reduction needs only pairwise localization. It also records that Sakamoto's published `p=3` localization lemmas are not literal-`2` theorem interfaces.

MATHSOLVE WP60N proves a new characteristic-two exchange theorem under the explicit hypotheses:

- residual self-duality;
- cartesian Selmer structure;
- core rank one;
- residual coisotropy `F* subset F`.

The coisotropic strict-place signature excludes the two odd relations containing one primal and both dual generators. If a surviving hard relation `p_1+p_2+d_i=0` occurs, one WP60G pairwise exchange move replaces the corresponding removed prime and aligns the new minimal-core primal line with the other primal line. The aligned four-class configuration has no odd relation, so WP60H supplies the common prime. This repairs the minimal-core gcd induction. The arbitrary-core reduction is then pairwise only, hence the full residual core graph is connected under coisotropy.

Record

`P2_BSS_COISOTROPIC_CORE_GRAPH_CONNECTED`.

WP60N does not establish that the selected literal-`2` canonical elliptic residual Selmer structure is coisotropic. The exact BSS applicability frontier is therefore

`MISSING_SELECTED_P2_RESIDUAL_CANONICAL_COISOTROPY_OR_NONCOISOTROPIC_CONNECTIVITY`.

The next BSS action is a place-by-place local-condition comparison under the fixed Weil self-duality. Treat the good-ordinary place `2` and bad semistable primes with even Tamagawa factor explicitly. If coisotropy fails, isolate the exact local failure and test whether WP60N only needs a weaker strict-place/global condition.

## Current route map

- R1: live — `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: live — `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired by WP60B.
- R4: live but reduced — `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT: live — `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: live — `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- R5 finite-level screened application architecture: `MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.
- R5-BSS residual graph connectivity: proved on the cartesian residually coisotropic sublane by WP60N.
- R5-BSS selected applicability: `MISSING_SELECTED_P2_RESIDUAL_CANONICAL_COISOTROPY_OR_NONCOISOTROPIC_CONNECTIVITY`.
- unchanged standard finite BSS hypothesis route: blocked globally at mod 4, though the defect is Selmer-extraneous at every finite level.
- standard infinite BSS application: blocked by H3.
- D2a: live — `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: live — `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream — `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## Claim firewall

Do not promote:

- conditional coisotropic connectivity to selected-lane connectivity before selected residual coisotropy is proved;
- Selmer-restricted injectivity to full formal Hypothesis 3.2(iii);
- WP60N to a repair of infinite H3;
- WP60N to a literal-`2` import of Sakamoto's `F_3` localization lemmas;
- WP60N to BSS integral Fitting control, R5, D2d, or `BSD-R2-A1` without the remaining applicability/downstream hypotheses;
- source admission, numerical evidence, or CI success to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head non-authoring/read-only Adversary and Referee review, affected ordinary CI, protected merge/readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, logging, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions. Bind every review, run, job, artifact, and merge to the current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or MATHCERT authority boundary.
