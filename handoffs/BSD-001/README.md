# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical work repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- External source admission: `grandchallenge/MATHFORGE` only.
- Mathematical certification: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Do not use mutable issue text, conversation history, stale summaries, numerical evidence, or an odd-prime theorem as mathematical authority.

## Canonical read order

After re-fetching protected live state, read:

1. this file;
2. `handoffs/BSD-001/RESEARCH_PLAN_WP16_WP18.md`;
3. `handoffs/BSD-001/TAKEOVER_PROMPT_WP16_WP18.md`;
4. the latest protected frontier, `handoffs/BSD-001/WP55_FRONTIER.md`;
5. `work_packages/BSD_R2_A1_WP55A_CLASSICAL_GZ_WP00_NORMALIZATION/`;
6. materially used protected predecessors, especially WP06, WP09, WP16A/B, WP19, WP38, WP52A, WP53A, and WP54A;
7. current protected MATHFORGE BSD source records before importing any new theorem.

Do not restart WP16 or broad WP17 reconnaissance.

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

## Current protected chain

- WP05–WP20: target/source normalization, exact finite `2`-primary Selmer/Fitting invariant, and rank-one determinant/Bockstein formalism.
- WP21–WP36: cyclotomic control, Poitou–Tate incidence, universal norms, square presentation, local-factor reconciliation, and finite twisted reciprocity.
- WP37–WP43A: literal-`p=2` Nekovář Bockstein/height over totally imaginary `K`, fixed-`2` nondegeneracy screen, exact finite strict/Kummer comparison, `D_K=ann(J_K)`, and strict first-order Bockstein naturality.
- WP44A–WP51A: compact Kummer Iwasawa complex, reverse comparison, exact specialization, localized Bockstein control, silent-kernel description, and literal-`p=2` Matlis/Pontryagin duality.
- WP52A: exact finite strict/Kummer determinant correction
  `len_Z2 V_K = 4 ord_2(3-a_2) + 2 sum_{ell|N} ord_2(c_ell)`;
  D2b is resolved at determinant-line level.
- WP53A: for every selected odd bad semistable `ell|N`,
  `Q_{ell,dt_ell^CST}=1+ell^(-1)` and
  `ord_2 Q_{ell,dt_ell^CST}=ord_2(ell+1)`.
- WP54A: exact global ordinary/test-vector scalar
  `Q^ord=(u_K/h_K) product_{ell|N}(1+ell^(-1))`,
  hence
  `ord_2(Q^ord)=ord_2(u_K)-ord_2(h_K)+sum_{ell|N}ord_2(ell+1)`;
  D2c is resolved.
- WP55A: protected at MATHSOLVE `956024627383d76b7b30212c0eaadf52e2fff7a2`. Using the protected Cai–Shu–Tian classical Gross–Zagier admission and the exact modular-area identity
  `4*pi^2 C_f^2 (phi,phi)=deg(f) A_E`,
  it proves
  `L'(E,1)/(Omega_E Reg_E)=R_GZ/WP00(E,K,f)`
  with
  `R_GZ/WP00
   = [2 A_E/(C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))]
     * [hhat_K(P_K(f))/Reg_E]`.
  Petersson norm and modular degree are eliminated exactly. No `ord_2` is assigned to this real scalar before an exact algebraicity/rational-line comparison.

## Live unresolved boundaries

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

`RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.

### D2c

`RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.

### D2d

`MISSING_EXACT_CLASSICAL_GZ_WP00_RESIDUAL_SCALAR_COMPARISON`.

The residual scalar has two explicit subfactors:

1. `hhat_K(P_K(f))/Reg_E`;
2. `2 A_E/(C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))`.

No cancellation with WP54A, Tamagawa, period, regulator, class-number, unit, discriminant, or bad-prime factors is implied.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate executable successors

### WP56A — classical height/regulator descent

Resolve

`hhat_K(P_K(f))/Reg_E`

as far as protected WP06/WP38 and the admitted Cai–Shu–Tian source permit. Protected WP38 already proves

`E(Q)/E(Q)_tors ->~ E(K)/E(K)_tors`

and therefore no quadratic base-change index occurs in the primitive free Mordell–Weil lattice. Retain the genuine Heegner index and the exact base-field height normalization. Determine every factor of `2` arising from the source height convention, Heegner trace, torsion, conjugation, or lattice index.

Do not import a materially new theorem until the protected internal deductions and admitted source have been exhausted. If a new theorem or source-level normalization is needed, admit it through MATHFORGE first.

### Secondary D2d successor

After the height/regulator factor is exact, attack

`2 A_E/(C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))`

as an exact area/real-period/modular-differential/rank-zero-twist normalization problem. Do not substitute rank-zero BSD for `E^D` without an admitted theorem at the required exact `2`-primary strength.

### WP54B — parallel D1c lane

Continue only the narrow literal-`p=2`, height-one-`(2)` analytic determinant-generator search. Do not reopen broad odd-prime reconnaissance.

### After D2d — exact WP06 normalization descent

Replay protected WP06 discrepancy accounting only after the analytic side is on the exact WP00 normalization line. No power of `2` may disappear in descent.

## Provider-index state

MATHFORGE protected main `2207d9a366e84dc7a1f5726e78e3cfe5e4ab1468` contains and indexes the exact WP55 Cai–Shu–Tian classical Gross–Zagier source audit. The earlier WP54 provider-index reconciliation is complete. The provider manifest is current through WP55 for the presently used source interfaces.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- `D_K=0`, `K_K^sil=0`, or `J_K=R_K`;
- height existence to fixed-`2` height nondegeneracy;
- `C_f=1`;
- the source `K`-height to the WP00 `Q`-regulator without an exact convention comparison;
- the WP54A class-number/unit or bad-prime factors to cancellation with another ledger without proof;
- a rank-zero BSD formula for `E^D` without exact admitted authority;
- an odd-prime result to literal integral `p=2`;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge, protected readback, issue #164 maintenance, and handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
