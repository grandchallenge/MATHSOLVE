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
2. the latest protected frontier, `handoffs/BSD-001/WP60A_A0_FRONTIER.md` after A0 protection;
3. `work_packages/BSD_R2_A1_WP60A_A0_DETERMINANT_DEPENDENCY_MAP/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60A_A0_DETERMINANT_DEPENDENCY_MAP/01_EXACT_DETERMINANT_DEPENDENCY_MAP.md`;
5. `work_packages/BSD_R2_A1_WP60A_A0_DETERMINANT_DEPENDENCY_MAP/02_CLAIM_LEDGER.yaml`;
6. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md` for the governing WP60 execution contract;
7. protected MATHFORGE WP60A source audit at current protected Forge state;
8. only then the deeper protected predecessors required by the chosen proof step.

Do not restart WP16 or broad WP17 reconnaissance. Do not reopen the standard odd-prime Heegner-primitivity route rejected by protected WP10. Do not repeat an open-ended main-conjecture or determinant-source sweep unless a candidate supplies a materially new literal-`p=2` construction.

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

## Current protected chain entering WP60A-A0

- WP05–WP20: target/source normalization, exact finite `2`-primary Selmer/Fitting invariant, residual-image control, Heegner-route barrier, and rank-one determinant/Bockstein formalism.
- WP21–WP36: cyclotomic control, Poitou–Tate incidence, universal norms, square presentation, local-factor reconciliation, and finite twisted reciprocity.
- WP37–WP51A: literal-`p=2` Nekovář Bockstein/height over totally imaginary `K`, fixed-`2` nondegeneracy screen, exact strict/Kummer comparison, reverse comparison, specialization, silent-kernel control, and literal-`p=2` Matlis/Pontryagin duality.
- WP52A: exact finite strict/Kummer determinant correction
  `len_Z2 V_K = 4 ord_2(3-a_2) + 2 sum_{ell|N} ord_2(c_ell)`;
  D2b is resolved at determinant-line level.
- WP53A/WP54A: exact split bad-prime and global ordinary/test-vector factors; D2c is resolved.
- WP55A–WP58A: exact classical Gross–Zagier, height/regulator, twist-period, and modular-differential normalization. For the fixed source-compatible parametrization,
  `ord_2(C_f)=0`
  and
  `delta_2(E)
   = 1 + 2 ord_2(m_K(f))
     - ord_2(c_infinity(E^D))
     - ord_2(lambda_D)
     - sum_{ell|N} ord_2(c_ell)`.
- WP59: protected MATHSOLVE `aae4320432a5510146a5af0bebcfd966e36d7419`; it isolates
  `R_2(E,K,f)=2 ord_2(m_K(f))-ord_2(lambda_D)`
  and records the bounded literal-`p=2` source boundary.
- WP60: protected MATHSOLVE `24fb349e28e4cbb5e034f4684edcc413975aed04`; it authorizes the three-lane post-WP59 research programme, with WP60A primary.
- MATHFORGE WP60A audit: protected at `e44baeeed5d508fd4e5332c883c837951e51c000`; it confirms the BKS determinantal-zeta architecture is structurally relevant but does not supply a literal-`p=2` determinant lift or height-one-`(2)` primitivity theorem.
- WP60A-A0: after protection, records the exact reduction that all finite algebraic determinant/control factors are already fixed, so D1c reduces to determinant lift plus primitivity at `(2)`.

## WP60A-A0 exact reduction

Protected WP35 gives a square cyclotomic presentation

`0 -> Lambda^r --A(T)--> Lambda^r -> X_infty -> 0`

and the exact specialization identity

`(coeff_T det A(T)) Z_2
 = Fitt^0(C_E^vee) Fitt^1(X_E) B_A`.

WP36 and WP39–WP52A fix the finite control and strict/Kummer determinant factors. Therefore the next missing datum is not another local correction.

### A1-LIFT

`MISSING_P2_KATO_ZETA_DETERMINANT_LIFT_AT_RESIDUE_CHARACTERISTIC_2`.

Construct an integral literal-`p=2` determinant lift of the normalized analytic/Kato class, or an exact finite-level replacement with the same primitive specialization.

### A1-PRIMITIVITY

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Prove exact basis/primitivity or reverse divisibility at the height-one prime `(2)`. A determinant lift alone is insufficient.

Combined refinement:

`MISSING_LITERAL_P2_KATO_ZETA_DETERMINANT_LIFT_AND_PRIMITIVITY_AT_HEIGHT_ONE_2`.

The campaign-level parent remains

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

## Immediate executable successor

### WP60A-A1 — direct literal-`p=2` determinant lift

Attack A1-LIFT first.

1. Reduce determinant membership to the smallest exact finite-level lattice/module statement compatible with the protected primitive Kummer first-Fitting line.
2. Construct the corresponding analytic/Kato/modular-symbol class integrally over `Z_2`.
3. Prove determinant membership without invoking an odd-prime Stark/Kolyvagin regulator theorem.
4. Transport through the already-protected local and specialization maps.
5. If a lift is obtained, proceed immediately to A1-PRIMITIVITY; do not declare R5 or D1c closed until exact reverse divisibility is proved.

If the determinant-membership condition reduces tautologically to the already missing height-one-`(2)` exponent, record the equivalence rather than relabeling the same unknown.

### WP60B — parallel escape route

If A1-LIFT reaches a genuine theorem boundary with no constructive next step, execute WP60B: normalize the Kriz–Li literal-`2` logarithmic condition under `P_K(f)=m_K(f)P+T` and classify it as independent auxiliary nonvanishing, equivalent to unknown index parity, or mixed.

### WP60C — supporting only

Use exact real-data computation only for falsification and theorem discovery. Numerical patterns do not promote a theorem.

## Live unresolved boundaries

- D1c parent: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- A1-LIFT: `MISSING_P2_KATO_ZETA_DETERMINANT_LIFT_AT_RESIDUE_CHARACTERISTIC_2`.
- A1-PRIMITIVITY: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2b: `RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.
- D2c: `RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.
- D2d: `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

D2e remains downstream. Do not replay WP06 as if D2d were resolved.

## D2d reopening contract

Reopen D2d only on a protected result satisfying at least one exact WP59 form:

1. `R1`: exact literal-`p=2` Heegner-index valuation;
2. `R2`: exact WP00-normalized twist-L-ratio valuation under all WP09 constraints without an unavailable rank-zero seed;
3. `R3`: theorem forcing the Kriz–Li mod-`2` Heegner-log condition for a WP09-compatible field for every selected curve;
4. `R4`: direct exact theorem for `R_2(E,K,f)`;
5. `R5`: literal-`p=2` integral height-one-`(2)` main-conjecture/reciprocity theorem specializing to the protected determinant line.

A0 does not itself reopen D2d.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- a determinant lift to determinant primitivity;
- an equality after inverting `2` to an integral equality;
- an unspecified `2`-unit to a generator;
- BKS/BSS odd-prime or `p>3` results to literal `p=2`;
- `m_K(f)` to odd or `lambda_D` to a `2`-adic unit without proof;
- computational evidence to a theorem;
- source admission or CI success to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge, protected readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, Lean, Sage/PARI, logging, or computational failures are recovery events, not stopping conditions.

Where exact identity matters, bind every action to the current exact head/run/job/artifact and reject stale evidence. Repairs require fresh exact-head replay.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
