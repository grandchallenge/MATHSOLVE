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
4. the latest protected frontier, currently `handoffs/BSD-001/WP48_FRONTIER.md` after WP48A protection;
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
- WP37: literal-`p=2` Nekovar cyclotomic Bockstein-height formalism over totally imaginary `K`; first height exists but nondegeneracy is not proved.
- WP38: bounded fixed-`2` nondegeneracy screen; quadratic base change adds no index to the rank-one Mordell-Weil free lattice.
- WP39: exact literal-`p=2` finite strict-Greenberg/compact-Kummer comparison over `K`; finite global hit `J_K` isolated.
- WP40: exact Poitou-Tate annihilator theorem `ann(J_K)=D_K` and complementary-length identity.
- WP41A: separates strict cyclotomic Bockstein deformation from fixed-level strict/Kummer comparison.
- WP41B: exact Disegni ordinary normalization `e_{2,infinity}^{-1}Q_special=Q^ord`.
- WP42B: canonical split-prime-`2` local factor `Q^ord_{2,dt_2^can}=1` with explicit measure firewall.
- WP43A: strict Greenberg first-order cyclotomic augmentation is exact and its specialization connecting morphism is the WP37 Bockstein.
- WP44A: primitive classical-Kummer cyclotomic control transports integrally to `K`; local norm-limit Kummer modules have exact base-projection cokernel `U_w`.
- WP45A: canonical compact Kummer Iwasawa local conditions and global Selmer complex; exact local derived augmentation defect.
- WP46A: the Kummer local condition is the lower truncation of the strict condition. At `w|2`, `Z_w^str ~= Lambda_w/(2^{m_2},gamma_w-1)`, `B_w^Kum=0`, and `0 -> Z_w^str -> U_w -> R_w -> 0`.
- WP47A: the strict-H2 and formal/reduction universal-norm filtrations are identical map-by-map; `Z_w^str=F_w^norm` inside `U_w` and `R_w` is literal reduction under the canonical ordinary connecting isomorphism.
- WP48A: the reverse comparison globalizes; its derived augmentation produces the exact specialization octahedron. The finite cone contains `R_K` canonically, the global image in it is exactly `J_K`, and protected WP40 places `D_K=ann(J_K)` on this same derived comparison surface.

## Current D1 boundary

### D1c — analytic determinant at height-one `(2)`

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

Kato gives literal-`p=2` control away from the height-one prime containing `2`; screened all-height-one upgrades retain odd-prime restrictions. WP35 is algebraic only.

## Current D2 boundaries

### D2a — fixed-`2` height nondegeneracy

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

WP37 proves existence of the first height, not nonvanishing. WP38 records that the closest screened derived-height/Stark-system and Eisenstein-Heegner routes do not apply to the protected surjective-`E[2]` branch.

### D2b — exact Bockstein identification of the WP40 annihilator

The local and global strict/Kummer comparison problems are now closed through the finite WP39/WP40 objects.

WP48A gives

`Q_infty ~= direct_sum_{w|2} Ind_w(Z_w^str[-2])`

and, after derived augmentation,

`H^1(Q_aug)=Z_2,K^loc tensor t_cyc`,

`H^2(Q_aug)=Z_2,K^loc`.

Its specialization octahedron yields

`0 -> Z_2,K^loc tensor t_cyc
   -> U_K^aug
   -> V_K
   -> Z_2,K^loc
   -> 0`,

with

`R_K=ker(V_K -> Z_2,K^loc)`

and

`im(S_2(E/K) -> V_K)=J_K subset R_K`.

Protected WP40 then gives

`D_K=ann_{R_K^dual}(J_K)`.

The live boundary is now

`MISSING_P2_IDENTIFICATION_OF_WP40_ANNIHILATOR_WITH_STRICT_BOCKSTEIN_SUBQUOTIENT`.

A successor must compare the protected strict Bockstein

`beta_str:H~^1_f(K,T) -> H~^2_f(K,T) tensor t_cyc`

with the canonical WP48A tangent term and identify exactly which Bockstein subquotient, if any, is Pontryagin-dual to `D_K`. Do not infer the answer from complementary lengths.

### D2c — ordinary Disegni local factors

Protected WP42B gives

`Q^ord_{2,dt_2^can}=1`.

The next exact local boundary is

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

The unresolved global `Q^ord` ledger still contains Haar-measure reconciliation, split semistable bad-prime terms, auxiliary finite places, remaining local L/vector normalizations, and residual global/archimedean normalization.

### D2d — classical/WP00 normalization

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

A `2`-adic height is not the WP00 Neron-Tate regulator.

### D2e — exact descent back to `Q`

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

Retain every plus/minus overlap, twist, period, Tamagawa, and local term.

## Immediate executable successors

### WP49A — strict Bockstein / WP40 annihilator comparison

Construct the morphism between the protected first-order strict augmentation triangle and the WP48A reverse comparison triangle after derived augmentation. Track the global-to-local map on `H~^2_f(K,T)` and determine the exact finite Bockstein subquotient controlling `Z_2,K^loc tensor t_cyc`. Then compare its annihilator with `D_K` under the protected local Tate pairing.

Do not assume height nondegeneracy.

### WP49B — split semistable bad-prime toric factors

Bind and evaluate the exact normalized split Steinberg/newvector toric factors in Disegni's packet, including Haar measure, local L-factors, denominator pairing, and Tamagawa-sensitive scalars. Do not infer a unit from interpolation alone.

Any new external theorem premise must first be admitted through MATHFORGE.

## Provider-index state

MATHFORGE protected main `4306aaeef25ac0923e4442ca1c8c1068ed55b514` reconciles the canonical BSD provider manifest against all 30 protected native BSD source audits through WP46A. No provider-index maintenance debt remains at the current frontier.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- `D_K` to a Bockstein image/kernel/cokernel/radical before WP49A;
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
