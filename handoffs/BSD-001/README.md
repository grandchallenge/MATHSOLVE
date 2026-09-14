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
2. the latest protected frontier, `handoffs/BSD-001/WP58_FRONTIER.md` after WP58A protection;
3. `work_packages/BSD_R2_A1_WP58A_MODULAR_DIFFERENTIAL_2UNIT/`;
4. protected WP57A and WP56A when reconstructing the analytic normalization line;
5. materially used protected predecessors, especially WP06, WP09, WP10, WP12, WP16A/B, WP19, WP38, WP52A, WP53A, and WP54A;
6. current protected MATHFORGE BSD source records before importing any new theorem.

Do not restart WP16 or broad WP17 reconnaissance. Do not reopen the standard odd-prime Heegner-primitivity route rejected by protected WP10.

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

- WP05–WP20: target/source normalization, exact finite `2`-primary Selmer/Fitting invariant, residual-image control, Heegner-route barrier, and rank-one determinant/Bockstein formalism.
- WP21–WP36: cyclotomic control, Poitou–Tate incidence, universal norms, square presentation, local-factor reconciliation, and finite twisted reciprocity.
- WP37–WP51A: literal-`p=2` Nekovář Bockstein/height over totally imaginary `K`, fixed-`2` nondegeneracy screen, exact strict/Kummer comparison, reverse comparison, specialization, silent-kernel control, and literal-`p=2` Matlis/Pontryagin duality.
- WP52A: exact finite strict/Kummer determinant correction
  `len_Z2 V_K = 4 ord_2(3-a_2) + 2 sum_{ell|N} ord_2(c_ell)`;
  D2b is resolved at determinant-line level.
- WP53A: for every selected odd bad semistable `ell|N`,
  `Q_{ell,dt_ell^CST}=1+ell^(-1)` and
  `ord_2 Q_{ell,dt_ell^CST}=ord_2(ell+1)`.
- WP54A: exact global ordinary/test-vector scalar
  `Q^ord=(u_K/h_K) product_{ell|N}(1+ell^(-1))`;
  D2c is resolved.
- WP55A: exact Cai–Shu–Tian/WP00 normalization, eliminating Petersson norm and modular degree while retaining the classical height and real-period/twist scalar.
- WP56A: exact height/regulator descent. With `P` primitive in `E(Q)/tors` and
  `P_K(f)=m_K(f)P+T`, protected WP38 and the admitted YZZ/CST height convention give
  `hhat_K(P_K(f))/Reg_E=2m_K(f)^2`.
- WP57A: protected MATHSOLVE `200e3eeab4b3fb2b6fcfcde6b3ec2565879ed11e`. It proves
  `A_E=Omega_E |Omega_E^-|/2`,
  combines exact negative-twist period transport with modular-symbol rationality, proves `u_K=1`, and obtains the exact rational identity
  `L'(E,1)/(Omega_E Reg_E)
   = 2 m_K(f)^2/(C_f^2 c_infinity(E^D) lambda_D)`,
  where
  `lambda_D=L(E^D,1)/Omega(E^D) in Q^x`.
  Therefore
  `delta_2(E)
   = 1+2 ord_2(m_K(f))-2 ord_2(C_f)
     -ord_2(c_infinity(E^D))-ord_2(lambda_D)
     -sum_{ell|N}ord_2(c_ell)`.
- MATHFORGE WP58: protected at `d588543151ddb458d627ac9b9fb37ec57cd90780`. Česnavičius's semistable optimal Manin theorem is admitted exactly, including at `p=2`: the optimal modular-parametrization scalar is `1` in the positive convention.
- WP58A: after protection, fixes `f=psi o f_0`, where `f_0` is optimal and `psi:E_0->E` has minimum degree. Minimality makes `ker(psi)` cyclic; protected irreducibility of `E[2]` forces `deg(psi)` odd; dual-isogeny differential transport then forces the selected scalar `C_f` to be odd. Hence
  `ord_2(C_f)=0`.
  The resulting valuation identity is
  `delta_2(E)
   = 1+2 ord_2(m_K(f))
     -ord_2(c_infinity(E^D))-ord_2(lambda_D)
     -sum_{ell|N}ord_2(c_ell)`.
  This does not assert `C_f=1`.

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

After WP58A protection:

`MISSING_P2_HEEGNER_INDEX_AND_TWIST_LRATIO_VALUATION_CONTROL`.

The two substantive arithmetic residuals are:

1. `ord_2(m_K(f))` for the fixed optimal-composite parametrization;
2. `ord_2(lambda_D)` for
   `lambda_D=L(E^D,1)/Omega(E^D)`.

The factor `c_infinity(E^D)` is an explicit real-topology term. The odd-bad-prime Tamagawa valuations are already protected.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate executable successors

### WP59A — exact twist L-ratio valuation

Determine

`ord_2(lambda_D)`

at literal `p=2` without substituting rank-zero BSD. Acceptable routes must give an exact integral/rational valuation compatible with the protected whole-real-period normalization. A statement only after inverting `2`, only up to a `2`-unit, or only modulo squares is insufficient.

The protected freedom in choosing the auxiliary quadratic field may be exploited only while preserving all WP09 splitting, discriminant, and nonvanishing conditions. Any materially new theorem controlling mod-2 algebraic twist L-values under simultaneous local conditions must be admitted through MATHFORGE before use.

### WP59B — literal-p=2 Heegner-index valuation

Determine

`ord_2(m_K(f))`

for the fixed optimal-composite parametrization. Protected WP10 proves that the screened standard odd-prime rank-lowering/primitivity chain cannot be specialized mechanically to `p=2`. A successful route therefore requires a genuinely literal-`p=2` theorem or a different exact arithmetic bridge.

### Parallel D1c lane

Continue only the narrow literal-`p=2`, height-one-`(2)` analytic determinant-generator search. Do not reopen broad odd-prime main-conjecture reconnaissance.

### After D2d — exact WP06 normalization descent

Replay protected WP06 discrepancy accounting only after the two remaining D2d valuations are on the exact protected line. No power of `2` may disappear in descent.

## Provider-index state

MATHFORGE protected main `d588543151ddb458d627ac9b9fb37ec57cd90780` is current through the WP58 semistable optimal Manin-constant admission. The provider manifest indexes the WP55 classical Gross–Zagier, WP56 height-convention, WP57 twist-period/rationality, and WP58 optimal-Manin interfaces used by the current chain.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- `D_K=0`, `K_K^sil=0`, or `J_K=R_K`;
- height existence to fixed-`2` height nondegeneracy;
- `C_f=1`; WP58A proves only `ord_2(C_f)=0` for its explicit chosen parametrization;
- `m_K(f)` to an odd integer without literal-`p=2` proof;
- `lambda_D` to a `2`-adic unit or to its rank-zero BSD expression without exact admitted authority;
- the WP54A class-number/unit or bad-prime factors to cancellation with another ledger without proof;
- an odd-prime theorem to literal integral `p=2`;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge, protected readback, issue #164 maintenance, and handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
