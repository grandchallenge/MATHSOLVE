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
4. the latest protected frontier, `handoffs/BSD-001/WP54_FRONTIER.md` after WP54A protection;
5. the work package named by that frontier;
6. materially used protected predecessors;
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
- WP37–WP43A: literal-`p=2` Nekovar Bockstein/height over totally imaginary `K`, fixed-`2` nondegeneracy screen, exact finite strict/Kummer comparison, `D_K=ann(J_K)`, and strict first-order Bockstein naturality.
- WP44A–WP47A: compact Kummer Iwasawa complex, reverse Kummer-to-strict comparison, explicit strict `H^2`, and map-level `Z_w^str=F_w^norm` at both `w|2`.
- WP48A: global reverse comparison cone and exact specialization octahedron; `J_K` and `D_K` recovered on the derived comparison surface.
- WP49A: localized strict Bockstein identified exactly; full-control formula for `D_K^vee` proved.
- WP50A: `R_K/J_K ~= K_K^sil` and `D_K ~= (K_K^sil)^vee`.
- WP51A: exact literal-`p=2` Matlis/Pontryagin duality separates the finite strict-`H^2` correction from first-height nondegeneracy.
- WP52A: determinant additivity for `C_str,0 -> C_Kum,0 -> V_K[-1]` gives the exact finite strict/Kummer determinant correction
  `len_Z2 V_K = 4 ord_2(3-a_2) + 2 sum_{ell|N} ord_2(c_ell)`.
  D2b is resolved at determinant-line level.
- WP53A: for every selected odd bad semistable `ell|N`, the CST-normalized split-torus conductor-one factor is
  `Q_{ell,dt_ell^CST}=1+ell^(-1)`
  with
  `ord_2 Q_{ell,dt_ell^CST}=ord_2(ell+1)`.
- WP54A: choosing CST quotient measures at all finite places and the unique formal archimedean scaling giving Disegni adelic volume one yields
  `Q^ord=(u_K/h_K) product_{ell|N}(1+ell^(-1))`
  and
  `ord_2(Q^ord)=ord_2(u_K)-ord_2(h_K)+sum_{ell|N}ord_2(ell+1)`.
  Here `h_K=#Cl(K)` and `u_K=[O_K^x:{+1,-1}]`. No unspecified unit remains. D2c is resolved.

## Live unresolved boundaries

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

`RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.

### D2c

`RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.

The exact global ordinary/test-vector factor is now known in the protected WP54A normalization. No cancellation with Tamagawa, determinant, period, regulator, or WP00 factors is implied.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate executable successors

### WP55A — classical Gross–Zagier/WP00 normalization

Transport the exact source-compatible p-adic Gross–Zagier/test-vector normalization, including the WP54A class-number/unit and bad-prime factors, to the protected WP00 complex BSD normalization. Retain every scalar until an exact comparison proves how it combines or cancels.

Any materially new external comparison theorem must first be admitted through MATHFORGE.

### WP54B — height-one `(2)` analytic determinant screen

Continue only the narrow D1c search. An admissible theorem must work literally at `p=2`, retain the height-one prime containing `2`, and provide an analytic determinant/characteristic generator compatible with the protected primitive rank-one determinant datum. Do not reopen broad odd-prime main-conjecture reconnaissance.

### After D2d — exact WP06 quadratic descent

Replay protected WP06 discrepancy accounting only after the analytic side has been transported into the exact WP00 normalization. No power of `2` may disappear during descent.

## Provider-index state

MATHFORGE protected main `52137efd71f1ece6f6a02bbb50c2a3acd21e4b40` contains the protected WP54 Disegni/Cai–Shu–Tian source audit used by this package. The canonical `provider_manifests/BSD-001.json` still requires its administrative WP54 index reconciliation; that indexing debt does not enlarge the admitted source interface and must be closed before importing another new BSD theorem.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- `D_K=0`, `K_K^sil=0`, or `J_K=R_K`;
- height existence to fixed-`2` height nondegeneracy;
- the WP54A class-number/unit or bad-prime factors to cancellation with another ledger without proof;
- coincidence of prime labels to cancellation with WP34 Tamagawa/Euler factors;
- an odd-prime result to literal integral `p=2`;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge, protected readback, issue #164 maintenance, and handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
