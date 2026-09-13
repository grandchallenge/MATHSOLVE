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
4. the latest protected frontier, currently `handoffs/BSD-001/WP51_FRONTIER.md` after WP51A protection;
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
- WP50A: define
  `K_K^sil := ker(H^2(C_str,0) -> H^2(C_Kum,0) direct_sum Zloc)`;
  then `R_K/J_K ~= K_K^sil` and `D_K ~= (K_K^sil)^vee`.
- WP51A: under exact literal-`p=2` Matlis/Pontryagin duality,
  `0 -> (K_K^sil)^perp -> S_str^dual -> D_K -> 0`.
  The separate `Z_2`-valued degree-(2,1) pairing used by the first height kills all finite strict `H^2`; hence the first height factors through strict `H^2/tors`. The finite `D_K` correction and first-height nondegeneracy are distinct obligations.

## Live boundaries

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

`MISSING_P2_FINITE_MATLIS_CORRECTION_EVALUATION_OR_CANCELLATION_IN_DETERMINANT_NORMALIZATION`.

Write

`d_K:=len_Z2 D_K=len_Z2 K_K^sil`.

Protected WP40 gives

`j_K+d_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

The first height does not evaluate `d_K`. A successor must compute `d_K` exactly or prove an exact determinant comparison where its contribution cancels against another identified finite term. Do not infer cancellation from perfect duality or from the total-length identity alone.

### D2c

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

Protected local `Q^ord_2=1` does not imply global `Q^ord=1`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate executable successors

### WP52A — determinant placement of the finite Matlis correction

Audit the exact determinant triangles from the strict `K`-side complex to the primitive Kummer determinant target. Track `J_K`, `D_K`, and `R_K` through determinant functor additivity. Determine whether the determinant normalization contains `d_K`, `j_K`, only `j_K+d_K=len R_K`, or an exact dual cancellation. Preserve every power of `2`.

### WP52B — split semistable bad-prime `Q^ord` factors

Continue the normalized split Steinberg/newvector toric-factor computation, retaining Haar measure, local `L`-factors, denominator pairing, Tamagawa-sensitive scalars, and all powers of `2`.

## Provider-index state

MATHFORGE protected main `79302cdc05f3f11c56e048f68e9095d3280872a7` indexes all 32 current BSD source audits through the WP51 strict-H2 duality admission.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- `D_K=0`, `K_K^sil=0`, or `J_K=R_K`;
- the finite Matlis correction to a first-height radical;
- height existence to fixed-`2` height nondegeneracy;
- a total finite comparison length to cancellation in the determinant without an exact determinant theorem;
- local `Q^ord_2=1` to global `Q^ord=1`;
- an odd-prime result to literal integral `p=2`;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge, protected readback, issue #164 maintenance, and handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
