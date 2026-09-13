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
4. the latest protected frontier, currently `handoffs/BSD-001/WP52_FRONTIER.md` after WP52A protection;
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
- WP50A: `R_K/J_K ~= K_K^sil` and `D_K ~= (K_K^sil)^vee`, where `K_K^sil` is the strict degree-two silent kernel.
- WP51A: exact literal-`p=2` Matlis/Pontryagin duality gives `0 -> (K_K^sil)^perp -> S_str^dual -> D_K -> 0`; the first `Z_2`-valued height kills finite strict `H^2`, so the finite correction and first-height nondegeneracy are distinct.
- WP52A: determinant additivity for
  `C_str,0 -> C_Kum,0 -> V_K[-1]`
  shows that the complete strict/Kummer determinant correction is `len_Z2 V_K`, not separate values of `j_K` or `d_K`. Exactly
  `len_Z2 V_K = 4 ord_2(3-a_2) + 2 sum_{ell|N} ord_2(c_ell)`.
  D2b is resolved at determinant-line level.

## Live unresolved boundaries

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

`RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.

The structural groups `J_K`, `D_K`, and `K_K^sil` need not vanish. Their separate lengths are not independent inputs to the protected strict/Kummer determinant normalization.

### D2c

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

Protected local `Q^ord_2=1` does not imply global `Q^ord=1`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate executable successors

### WP53A — split semistable bad-prime `Q^ord` factors

Compute the normalized split Steinberg/newvector toric factors at every odd `ell|N`. Retain split/nonsplit multiplicative type, Steinberg twist, Haar measure, local `L`-factors, denominator pairing, newvector scaling, Tamagawa-sensitive scalars, and every power of `2`.

### WP53B — height-one `(2)` analytic determinant screen

Continue only the narrow D1c search. An admissible theorem must work literally at `p=2`, retain the height-one prime containing `2`, and provide an analytic determinant/characteristic generator compatible with the protected primitive rank-one determinant datum. Do not reopen broad odd-prime main-conjecture reconnaissance.

## Provider-index state

MATHFORGE protected main `79302cdc05f3f11c56e048f68e9095d3280872a7` indexes all 32 current BSD source audits through the WP51 strict-H2 duality admission. WP52A uses no new external theorem premise.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- `D_K=0`, `K_K^sil=0`, or `J_K=R_K`;
- the finite Matlis correction to a first-height radical;
- height existence to fixed-`2` height nondegeneracy;
- local `Q^ord_2=1` to global `Q^ord=1`;
- a split bad-prime factor to a unit without exact calculation;
- an odd-prime result to literal integral `p=2`;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge, protected readback, issue #164 maintenance, and handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
