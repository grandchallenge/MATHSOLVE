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
4. the latest protected frontier, currently `handoffs/BSD-001/WP47_FRONTIER.md` after WP47A protection;
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
- WP43A: strict Greenberg first-order cyclotomic augmentation is exact and its specialization connecting morphism is the WP37 Bockstein.
- WP44A: primitive classical-Kummer cyclotomic control transports integrally to `K`; local norm-limit Kummer modules have exact base-projection cokernel `U_w`.
- WP45A: canonical compact Kummer Iwasawa local conditions and global Selmer complex; local Kummer augmentation has no `Tor_1` term.
- WP46A: the Kummer local condition is the lower truncation of the strict condition. At `w|2`, `Z_w^str=H^2(U_{w,infty}^{+,str}) ~= Lambda_w/(2^{m_2},gamma_w-1)`, `B_w^Kum=0`, and `0 -> Z_w^str -> U_w -> R_w -> 0`.
- WP47A: the WP46A derived-control filtration and WP28 formal/reduction universal-norm filtration are identical map-by-map. The compact strict/Kummer quotient is literal reduction under the canonical isomorphism `rho_w:E_tilde(F_2)~=R_w`; hence `Z_w^str=F_w^norm` as the same subgroup of `U_w`.

## Current D1 boundary

### D1c — analytic determinant at height-one `(2)`

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

Kato gives literal-`p=2` control away from the height-one prime containing `2`; screened all-height-one upgrades retain odd-prime restrictions. WP35 is algebraic only.

## Current D2 boundaries

### D2a — fixed-`2` height nondegeneracy

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

WP37 proves existence of the first height, not nonvanishing. WP38 records that the closest screened derived-height/Stark-system and Eisenstein-Heegner routes do not apply to the protected surjective-`E[2]` branch.

### D2b — global strict/Kummer comparison cone and WP40 defect

The ordinary local map-level mismatch is closed. At each `w|2`,

`0 -> Z_w^str -> U_w -> R_w -> 0`

and

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`

are the same filtration, with

`Z_w^str=F_w^norm`

inside `U_w` and canonical

`rho_w:E_tilde(F_2) ~= R_w`.

The local quotient map satisfies

`qbar_w=rho_w o redbar_w`.

The live boundary is now

`MISSING_P2_GLOBAL_STRICT_KUMMER_COMPARISON_CONE_TO_WP40_BOCKSTEIN_DEFECT`.

A successor must assemble the local Kummer-to-strict comparison triangles into the global Selmer-complex comparison, compute derived cyclotomic augmentation of the global cone, and identify its finite specialization map-by-map with protected WP39/WP40 `J_K,D_K`. Only then may `D_K` be compared with the protected Bockstein/height triangle.

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

### WP48A — global strict/Kummer comparison cone

Use completed induction and Nekovář's mapping-fibre functoriality to assemble the protected local morphisms

`U_{w,infty}^{+,Kum} -> U_{w,infty}^{+,str}`

into the global comparison. Compute the cone and its derived augmentation. The finite specialized maps must recover WP39's actual image `J_K` and WP40's dual annihilator `D_K`, not just their lengths.

### WP48B — split semistable bad-prime toric factors

Bind and evaluate the exact normalized split Steinberg/newvector toric factors in Disegni's packet, including Haar measure, local L-factors, denominator pairing, and Tamagawa-sensitive scalars. Do not infer a unit from interpolation alone.

Any new external theorem premise must first be admitted through MATHFORGE.

## Provider-index state

MATHFORGE protected main `4306aaeef25ac0923e4442ca1c8c1068ed55b514` reconciles the canonical BSD provider manifest against all 30 protected native BSD source audits through WP46A. No provider-index maintenance debt remains at the current frontier.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- `D_K` to a Bockstein/height defect before the global comparison cone is fixed;
- `D_K=0` or `J_K=R_K`;
- height existence to height nondegeneracy;
- canonical local `Q^ord_2=1` to global `Q^ord=1`;
- interpolation of a local zeta integral to an explicit semistable value;
- an odd-prime or rationalized result to literal integral `p=2`;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, source admission when required, exact-head non-authoring/read-only Adversary and Referee review, affected ordinary CI, protected merge, protected readback, issue #164 maintenance, and handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.