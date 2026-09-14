# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical work repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Active WP60 execution tracker: `grandchallenge/MATHSOLVE#215`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- External source admission: `grandchallenge/MATHFORGE` only.
- Mathematical certification: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Do not use mutable issue text, conversation history, stale summaries, numerical evidence, or an odd-prime theorem as mathematical authority.

## Canonical read order

After re-fetching protected live state, read:

1. this file;
2. the latest protected frontier, `handoffs/BSD-001/WP60A_A1_FRONTIER.md` after A1 protection;
3. `work_packages/BSD_R2_A1_WP60A_A1_DETERMINANT_MEMBERSHIP/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60A_A1_DETERMINANT_MEMBERSHIP/01_DETERMINANT_MEMBERSHIP_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60A_A1_DETERMINANT_MEMBERSHIP/02_CLAIM_LEDGER.yaml`;
6. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
7. protected MATHFORGE WP60A and WP59 source audits;
8. only then deeper protected predecessors needed by the chosen lane.

Do not repeat a generic main-conjecture/determinant search. WP60A has reduced determinant lift at `(2)` to the missing Fitting divisibility itself. The next executable lane is WP60B unless materially new literal-`2` arithmetic input directly attacks that inequality.

## Governing invariant

For the selected rank-one class,

`delta_2(E)
 := ord_2(L'(E,1)/(Omega_E Reg_E))
    - sum_{ell|N} ord_2(c_ell)`.

Protected WP16A/WP16B/WP19 give

`v_2(Fitt^1_{Z_2}(X_E))
 = len_Z2 Sha(E/Q)[2^infinity]
 = lim_n (ord_2 #Sel_{2^n}(E/Q)-n)`.

The selected theorem is exactly

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

## Current protected chain entering WP60A-A1

- WP52A resolves the exact finite strict/Kummer determinant correction.
- WP54A resolves the global ordinary/test-vector scalar.
- WP55A–WP58A place the analytic side on the exact rational line and prove `ord_2(C_f)=0` for the fixed source-compatible parametrization.
- WP59 isolates
  `R_2(E,K,f)=2 ord_2(m_K(f))-ord_2(lambda_D)`
  and records the literal-`p=2` source boundary.
- WP60 at `24fb349e28e4cbb5e034f4684edcc413975aed04` establishes the three-lane research programme.
- MATHFORGE WP60A at `e44baeeed5d508fd4e5332c883c837951e51c000` admits the bounded BKS/BSS source audit: the determinant architecture is relevant, but the located lift/regulator chain excludes literal `p=2` and does not prove height-one-`(2)` primitivity.
- WP60A-A0 at `20a980fd8fb3e3a4cceabf0e37af838a16c1608e` proves that all finite algebraic determinant/control factors are already exact and reduces D1c to lift plus primitivity.
- WP60A-A1, after protection, proves the exact determinant-lattice membership criterion and shows that the lift problem itself is the missing one-sided Fitting divisibility at `(2)`.

## WP60A-A1 exact result

Let `R` be a DVR and

`C=[P^1 -> P^2]`

be a two-term perfect complex in degrees `1,2` with free rank-one `H^1(C)` and finite `H^2(C)`.

Under the canonical rational determinant trivialization,

`det_R^{-1}(C)`

maps to exactly

`Fitt^0_R(H^2(C)) H^1(C)`.

For `z=aP` on a primitive basis `P`:

- determinant membership iff `v(a)>=length_R H^2(C)`;
- determinant-generator/primitivity iff `v(a)=length_R H^2(C)`.

At `q=(2)` of `Lambda=Z_2[[T]]`, this means a BKS-style determinant lift of the fixed Kato class is exactly the one-sided Fitting inequality missing from the protected Kato `p=2` interface. Merely exhibiting an integral cohomology class does not prove the lift.

### Refined WP60A boundaries

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Parent D1c remains

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

WP60A does not satisfy WP59 R5 and does not reopen D2d.

## Immediate executable successor — WP60B

Normalize the exact Kriz–Li literal-`2` logarithmic condition under

`P_K(f)=m_K(f)P+T`.

Required work:

1. ensure the exact primary-source formula is admitted through MATHFORGE;
2. transport the logarithmic/differential/local factors into protected WP56A/WP58A normalization;
3. prove the contribution of prime-to-`2` torsion;
4. isolate the factor involving `m_K(f)` and any genuinely `K`-varying term;
5. classify the condition exactly as `INDEPENDENT_AUXILIARY_NONVANISHING`, `EQUIVALENT_TO_UNKNOWN_INDEX_PARITY`, or `MIXED`.

If the condition is equivalent to `m_K(f)` being odd, record that equivalence and terminate WP60B as non-independent. If independent data remains, seek a WP09-compatible field-forcing theorem and test WP59 R3.

## Live unresolved boundaries

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- WP60A one-sided divisibility: `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- WP60A primitivity: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2b: `RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.
- D2c: `RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.
- D2d: `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

D2e remains downstream.

## WP59 reopening contract

D2d reopens only on a protected result satisfying exact R1, R2, R3, R4, or R5 from WP59. WP60A-A1 satisfies none of them.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- determinant formalism to the missing arithmetic divisibility;
- determinant membership to determinant primitivity;
- equality after inverting `2` to an integral equality;
- BKS/BSS/Kato odd-prime clauses to literal `p=2`;
- `m_K(f)` to odd or `lambda_D` to a `2`-adic unit without proof;
- the Kriz–Li condition to a uniform fact before normalization and forcing are proved;
- computation to theorem;
- source admission or CI success to MATHCERT certification.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge, protected readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, Lean, Sage/PARI, logging, or computational failures are recovery events, not stopping conditions.

Bind every review, run, job, and artifact to its current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority.
