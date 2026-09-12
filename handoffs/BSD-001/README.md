# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical work repository: `grandchallenge/MATHSOLVE`.
- Current programme owner: `grandchallenge/MATHSOLVE#164`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- External theorem/source admission: `grandchallenge/MATHFORGE` only.
- Mathematical certification: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Do not treat mutable issue text, conversational history, stale summaries, or numerical evidence as mathematical authority.

## Canonical read order

After re-fetching protected live state, read:

1. this file;
2. `handoffs/BSD-001/RESEARCH_PLAN_WP16_WP18.md`;
3. `handoffs/BSD-001/TAKEOVER_PROMPT_WP16_WP18.md`;
4. the latest protected frontier, currently `handoffs/BSD-001/WP44_FRONTIER.md` after WP44A protection;
5. the work package named by that frontier;
6. any protected predecessor materially used by the next proof step;
7. current protected MATHFORGE BSD provider records before using external theorems.

Do not restart WP16 or broad WP17 reconnaissance.

## Governing invariant

For the selected rank-one class,

`delta_2(E)
 := ord_2(L'(E,1)/(Omega_E Reg_E))
    - sum_{ell|N} ord_2(c_ell)`.

Protected WP16A, WP16B, and WP19 prove

`v_2(Fitt^1_{Z_2}(X_E))
 = len_Z2 Sha(E/Q)[2^infinity]
 = lim_n (ord_2 #Sel_{2^n}(E/Q)-n)`,

where

`X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`.

Thus the selected theorem is exactly

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

Protected WP20 gives the rank-one determinant/Bockstein factorization; WP35 supplies the primitive cyclotomic square presentation with exact specialization defect. The remaining campaign is an exact integral determinant/height/normalization problem.

## Protected chain relevant to the live frontier

- WP05–WP15: source/target normalization, quadratic descent, good-ordinary local data, auxiliary `K`, residual image, Tamagawa dictionary, and square/parity firewalls.
- WP16A/WP16B/WP19: exact primitive integral Selmer/Fitting invariant.
- WP20: universal rank-one Bockstein/determinant factorization.
- WP21–WP36: primitive cyclotomic control, local kernels, Poitou–Tate incidence, universal norms, unit-root reconciliation, finite comparison terms, square presentation, and finite twisted-reciprocity computation.
- WP37: literal-`p=2` Nekovář cyclotomic Bockstein-height formalism over totally imaginary `K`; first height exists but nondegeneracy is not proved.
- WP38: bounded fixed-`2` nondegeneracy screen; quadratic base change adds no index to the rank-one Mordell–Weil free lattice.
- WP39: exact literal-`p=2` finite strict-Greenberg/compact-Kummer comparison over `K`; finite global hit `J_K` isolated.
- WP40: exact Poitou–Tate annihilator theorem `ann(J_K)=D_K` and complementary-length identity.
- WP41A: separates strict cyclotomic Bockstein deformation from fixed-level strict/Kummer comparison.
- WP41B: exact Disegni ordinary normalization `e_{2,infinity}^{-1}Q_special=Q^ord`.
- WP42B: canonical split-prime-`2` local factor `Q^ord_{2,dt_2^can}=1` with explicit measure firewall.
- WP43A: Nekovář strict-Greenberg first-order cyclotomic augmentation is exact and its specialization connecting morphism is the WP37 Bockstein.
- WP44A: primitive classical-Kummer cyclotomic control transports integrally to `K`; the local norm-limit Kummer module has exact base-projection cokernel `U_w`. At `w|2`, `U_w` contains the explicit formal universal-norm term in the protected WP28 filtration.

## Current D1 boundary

### D1c — analytic determinant at height-one `(2)`

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

Kato gives literal-`p=2` control away from the height-one prime containing `2`; screened all-height-one upgrades retain odd-prime restrictions. WP35 is algebraic only. A valid successor must determine the integral analytic determinant at `(2)` or an exact equivalent.

## Current D2 boundaries

### D2a — fixed-`2` height nondegeneracy

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

WP37 proves existence of the first height, not nonvanishing. WP38 records that the closest screened derived-height/Stark-system and Eisenstein-Heegner routes do not apply to the protected surjective-`E[2]` branch.

### D2b — compact Kummer derived lift and exact specialization over `K`

WP40 proves

`j_K+d_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

WP43A closes strict-Greenberg Bockstein naturality. WP44A proves the module-level Kummer cyclotomic object and exact ordinary control over `K`:

`0 -> Sel_K^Kum
   -> (Sel_Kinfty^Kum)^Gamma_K
   -> C_K^Kum
   -> 0`

and

`0 -> (C_K^Kum)^vee
   -> (X_Kinfty^Kum)_Gamma_K
   -> X_K^Kum
   -> 0`.

It also constructs

`M_w^Kum=inverse_limit_n E(K_{n,w})^hat_2`

with exact base-projection cokernel `U_w`.

The surviving boundary is

`MISSING_P2_COMPACT_KUMMER_IWASAWA_COMPLEX_LIFT_AND_DERIVED_SPECIALIZATION_OVER_K`.

A successor must lift the norm-limit Kummer condition to a compact local-condition/Selmer complex compatible with the protected strict Greenberg complex, compute derived augmentation including any `Tor_1`/coinvariant kernel, and identify the specialized comparison cone map-by-map with WP39/WP40.

At each `w|2`, do not discard the protected exact term

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`.

The full `U_w` has twice the length of WP39's reduction-sized local ambient term.

### D2c — ordinary Disegni local factors

Protected WP42B gives

`Q^ord_{2,dt_2^can}=1`.

The next exact local boundary is

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

The unresolved global `Q^ord` ledger still contains Haar-measure reconciliation, split semistable bad-prime terms, auxiliary finite places, remaining local L/vector normalizations, and residual global/archimedean normalization.

### D2d — classical/WP00 normalization

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

A `2`-adic height is not the WP00 Néron–Tate regulator.

### D2e — exact descent back to `Q`

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

Retain every plus/minus overlap, twist, period, Tamagawa, and local term.

## Immediate executable successors

### WP45A — compact Kummer derived lift

Construct the compact classical-Kummer local-condition complex over `Lambda_K` from the protected norm-limit Kummer modules. Prove derived augmentation, not merely ordinary coinvariant control. The specialized comparison cone must recover WP39/WP40 map-by-map, with the formal universal-norm term at `2` carried explicitly.

### WP45B — split semistable bad-prime toric factors

For each odd semistable `ell|N`, with `K/Q` split at `ell` and `chi_ell=1`, bind the exact local representation and test vector selected by the Disegni packet and evaluate the normalized split Rankin–Selberg/newvector toric integral. Retain multiplicative type, Steinberg twist, Haar measure, local L-factor, denominator pairing, and Tamagawa-sensitive scalars.

Any new external theorem premise must first be admitted through MATHFORGE.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- ordinary Kummer coinvariant control to derived compact-complex specialization;
- the discrete Kummer dual `X_Kinfty^Kum` to the compact WP39 lattice;
- equality of local lengths to a canonical isomorphism;
- the full `U_w` at `w|2` to WP39's reduction-sized local target;
- the formal universal-norm term to zero;
- `D_K` to a Bockstein defect before the derived comparison cone is proved;
- canonical `Q^ord_2=1` to global `Q^ord=1`;
- interpolation of a local zeta integral to an explicit semistable value;
- height existence to height nondegeneracy;
- an odd-prime or rationalized result to literal integral `p=2`;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, source admission when required, exact-head non-authoring/read-only Adversary and Referee review, affected ordinary CI, protected merge, protected readback, issue #164 maintenance, and handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.