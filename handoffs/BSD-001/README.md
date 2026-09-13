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
4. the latest protected frontier, currently `handoffs/BSD-001/WP49_FRONTIER.md` after WP49A protection;
5. the work package named by that frontier;
6. any protected predecessor materially used by the next step;
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

The selected theorem is therefore exactly

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

## Current protected chain

- WP05–WP20: source/target normalization, quadratic descent, local data, auxiliary `K`, residual/Tamagawa control, exact primitive Selmer/Fitting invariant, and rank-one Bockstein/determinant formalism.
- WP21–WP36: cyclotomic control, Poitou–Tate incidence, universal norms, unit-root reconciliation, finite comparison terms, square presentation, and twisted-reciprocity computation.
- WP37: literal-`p=2` Nekovar Bockstein/height over totally imaginary `K`; existence, not nondegeneracy.
- WP38: fixed-`2` nondegeneracy screen and exact Mordell–Weil base-change lattice comparison.
- WP39/WP40: finite strict/Kummer quotient `R_K`, actual global hit `J_K`, and exact annihilator `D_K=ann(J_K)`.
- WP41A–WP43A: strict augmentation/Bockstein separated from Kummer comparison; exact Disegni ordinary normalization at split `2`; strict first-order augmentation naturality.
- WP44A–WP47A: compact Kummer Iwasawa complex, exact derived control, reverse Kummer-to-strict comparison, explicit strict `H^2`, and map-level identification `Z_w^str=F_w^norm` with literal reduction quotient at both `w|2`.
- WP48A: global reverse comparison cone and specialization octahedron; `J_K` and `D_K` recovered canonically on the derived comparison surface.
- WP49A: the WP48A tangent comparison boundary is exactly the localized strict cyclotomic Bockstein. If `C_K^ctrl` is the full global Kummer-control image in `U_K^aug`, then
  `C_K^ctrl intersect (Zloc tensor t_cyc)=im(lambda_K)`,
  `0 -> im(lambda_K) -> C_K^ctrl -> J_K -> 0`, and
  `D_K ~= (U_K^aug/((Zloc tensor t_cyc)+C_K^ctrl))^vee`.
  Therefore `D_K` is not formally a pure Bockstein image/cokernel; the missing datum is the full control image.

## Live boundaries

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

`MISSING_P2_GLOBAL_KUMMER_CONTROL_IMAGE_TO_STRICT_BOCKSTEIN_DUALITY`.

The localized strict Bockstein is known exactly. A successor must characterize the entire subgroup

`C_K^ctrl subset U_K^aug`

through a literal-`p=2` global Poitou–Tate/Selmer-complex duality theorem compatible with the strict Bockstein or height pairing. The missing object is not merely `im(lambda_K)`.

Protected MATHFORGE `79f7c88cf4e59886902c2f12d29d7c73afced379` records that Macias Castillo–Sano 2026 is a close structural comparator but assumes `p` odd throughout; it cannot authorize this literal-`p=2` bridge.

### D2c

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

Protected local `Q^ord_2=1` does not imply global `Q^ord=1`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate executable successors

### WP50A — literal-`p=2` control-image duality

Search for, or derive directly from already-protected duality diagrams, an exact theorem characterizing `C_K^ctrl` or its quotient through global Poitou–Tate/Selmer-complex duality and the strict Bockstein/height. Preserve all finite `2`-primary terms. If the source route is unavailable, record the exact theorem/source boundary rather than importing an odd-prime comparator.

### WP50B — split semistable bad-prime `Q^ord` factors

Bind and compute the normalized split Steinberg/newvector toric factors in Disegni's packet, retaining Haar measure, local `L`-factors, denominator pairing, and Tamagawa-sensitive scalars.

## Provider-index state

MATHFORGE protected main `79f7c88cf4e59886902c2f12d29d7c73afced379` indexes all 31 current BSD source audits through the WP49 applicability screen. The WP49 screen does not close the literal-`p=2` control-image theorem.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- `D_K` to a pure Bockstein image, kernel, cokernel, or height radical;
- `D_K=0` or `J_K=R_K`;
- height existence to fixed-`2` height nondegeneracy;
- local `Q^ord_2=1` to global `Q^ord=1`;
- an odd-prime result to literal integral `p=2`;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge, protected readback, issue #164 maintenance, and handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
