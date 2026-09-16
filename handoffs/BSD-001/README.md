# BSD-001 canonical continuation handoff

## Cold start

This repository state is the operational authority for continuation. Chat transcripts, mutable issue prose, and stale summaries are context only.

After re-fetching live protected heads, an independent agent SHALL begin with:

1. `.gcl/campaigns/BSD-001/CAMPAIGN_STATE.json`;
2. `.gcl/operations/BSD-WP60S/OPERATION.json`;
3. `handoffs/BSD-001/WP60S_FRONTIER.md`;
4. the WP60S theorem and claim ledger;
5. the exact protected provider and predecessor artifacts named by those records.

Before review or expensive CI, run:

`python tools/gcl_campaign_preflight.py BSD-001 BSD-WP60S`

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Active tracker: `grandchallenge/MATHSOLVE#215`.
- Current bounded operation: `grandchallenge/MATHSOLVE#245` (`WP60S`).
- Protected mathematical base entering WP60S: `grandchallenge/MATHSOLVE@245860ce3d7307a505e48b4165be0850327f996a`.
- Source authority: protected `grandchallenge/MATHFORGE@770f95d1f8e7cfdd3facbd9242bf3c21c0e8b074`.
- Constitutional authority: protected `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Certification authority: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Use protected repository state as authority. Do not use numerical evidence, odd-prime theorems, or workflow success as substitute mathematical authority.

## Governing invariant

Define

`delta_2(E)
 := ord_2(L'(E,1)/(Omega_E Reg_E))
    - sum_{ell|N} ord_2(c_ell)`.

Protected WP16A/WP16B/WP19 give

`v_2(Fitt^1_{Z_2}(X_E))
 = len_Z2 Sha(E/Q)[2^infinity]
 = lim_n(ord_2 #Sel_{2^n}(E/Q)-n)`.

The selected theorem remains exactly

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

## BSS literal-p=2 chain

### WP60G–WP60Q — residual localization and selected connectivity

WP60G repairs one-primal/one-dual residual localization using self-duality. WP60H gives the exact `F_2` odd-relation criterion for simultaneous localization. WP60J verifies selected residual BSS II Hypotheses 3.2/3.3 and full selected `GL_2(Z_2)` image. WP60N proves characteristic-two exchange and full residual core-graph connectivity under coisotropy. MATHFORGE WP60O/WP60P verify selected canonical coisotropy, cartesianness, and core rank one. WP60Q binds those interfaces and records `BSS_LITERAL_P2_SELECTED_RESIDUAL_CORE_GRAPH_CONNECTED`.

### WP60K–WP60M — higher finite restriction defect

WP60K proves unchanged formal finite Hypothesis 3.2(iii) fails already at `E[4]`. WP60M proves the resulting order-two defect persists at every finite coefficient level but is excluded from every actual selected canonical modified primal and dual Selmer group at a fixed local condition. Selmer-restricted restriction injectivity and coefficient reduction are therefore available even though formal higher-level Hypothesis 3.2(iii) remains false.

### WP60R — protected finite BSS theorem replay

Protected MATHSOLVE `245860ce3d7307a505e48b4165be0850327f996a` records:

- `BSS_LITERAL_P2_SELECTED_ALL_FINITE_LEVEL_CORE_GRAPHS_CONNECTED`;
- `BSS_LITERAL_P2_SELECTED_FINITE_LEVEL_HYPOTHESIS_4_2_AVAILABLE`;
- `BSS_LITERAL_P2_SELECTED_THEOREM_5_20_REPLAYED`;
- `BSS_LITERAL_P2_SELECTED_THEOREM_5_2_REPLAYED`.

The finite Theorem 5.20/5.2 boundary is closed on protected `main`. Formal higher-level Hypothesis 3.2(iii) and infinite H3 remain false/unrepaired.

### MATHFORGE WP60S — protected inverse-limit dependency audit

Protected MATHFORGE `770f95d1f8e7cfdd3facbd9242bf3c21c0e8b074` establishes the selected cross-level interfaces needed for the inverse-limit replay while preserving failure of full Hypothesis 4.7(iii):

- nested useful-prime sets;
- Stark coefficient reductions;
- core-vertex persistence;
- regulator-compatible Kolyvagin reductions;
- inverse-limit Stark freeness and Fitting passage.

The provider audit does not assert full BSS Hypothesis 4.7 or infinite H3.

### WP60S — current candidate

WP60S binds the protected finite theorem replay to the protected cross-level interfaces and supplies the selected literal-`2` replay of BSS II Theorem 5.25. Candidate disposition:

`BSS_LITERAL_P2_SELECTED_THEOREM_5_25_REPLAYED`.

This is not protected authority until exact-head Adversary and Referee review, required CI, guarded merge, and protected readback complete.

Entering boundary:

`MISSING_LITERAL_P2_BSS_THEOREM_5_25_INVERSE_LIMIT_REPLAY_AFTER_FINITE_LEVEL_REPLACEMENTS`.

If the candidate is protected, the next exact theorem-level boundary is:

`MISSING_LITERAL_P2_BSS_THEOREM_6_12_COROLLARY_6_15_APPLICATION_REPLAY_WITHOUT_INFINITE_H3`.

## Current route map

- R1: live — `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: live — `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired by WP60B.
- R4: live but reduced — `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT: live — `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: live — `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- R5-BSS selected finite theorem replay: protected complete by WP60R.
- R5-BSS inverse-limit theorem: WP60S candidate closure pending exact-head admission.
- standard infinite BSS application: blocked by protected H3 failure unless the exact downstream use is shown irrelevant or replaced.
- D2a: live — `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: live — `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream — `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## Progress discipline

A mathematical successor package is justified only when the current operation produces one of these theorem-level dispositions:

- `CLOSED`: the named frontier is retired;
- `BLOCKED`: a new irreducible mathematical dependency is identified precisely;
- `FALSIFIED`: the proposed route is shown not to work.

`RECONNAISSANCE` and `MAINTENANCE` are useful operational outcomes but do not count as frontier movement and do not by themselves authorize a new theorem package.

Content SHALL be frozen before exact-head admission review. A changed candidate head invalidates prior exact-head reviews and checks. A changed governed mathematical artifact also invalidates the freeze manifest.

## Claim firewall

Do not promote:

- WP60S to BSS Theorem 6.12 or Corollary 6.15 without the exact application replay;
- selected finite-level or inverse-limit replacements to full formal Hypothesis 3.2(iii), full Hypothesis 4.7(iii), or infinite H3;
- any WP60 result to R5, D2d, or `BSD-R2-A1` without the remaining proofs;
- source admission, numerical evidence, or CI success to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof or falsification, source admission when materially required, deterministic preflight, content freeze, exact-head non-authoring/read-only Adversary and Referee review, affected CI, protected merge/readback, completion receipt, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, logging, formatting, source-access, compiler, environment, routing, or computational failures are recovery events, not stopping conditions. Bind every review, run, job, artifact, and merge to the current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/governance/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or the MATHCERT authority boundary.
