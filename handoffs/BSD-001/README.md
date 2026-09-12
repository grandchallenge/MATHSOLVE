# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical work repository: `grandchallenge/MATHSOLVE`.
- Current programme owner: `grandchallenge/MATHSOLVE#164`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- External theorem/source admission: `grandchallenge/MATHFORGE` only.
- Mathematical certification: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Do not treat mutable issue text, conversational history, stale campaign summaries, or numerical evidence as mathematical authority.

## Canonical read order

After re-fetching protected live state, read:

1. this file;
2. `handoffs/BSD-001/RESEARCH_PLAN_WP16_WP18.md` for the durable representation-change strategy;
3. `handoffs/BSD-001/TAKEOVER_PROMPT_WP16_WP18.md` for the original continuity contract and claim firewall;
4. the latest protected frontier file, currently `handoffs/BSD-001/WP40_FRONTIER.md` after WP40 protection;
5. the work package named by that frontier;
6. any earlier protected package on which the intended proof step materially depends;
7. the current protected MATHFORGE BSD provider records before using any external theorem.

The WP16/WP18 plan remains historically controlling for the representation change, but its original frontier labels have been superseded by later protected work. Do not restart WP16 or broad WP17 reconnaissance.

## Governing invariant

For the selected rank-one class, define

`delta_2(E)
 := ord_2(L'(E,1)/(Omega_E Reg_E))
    - sum_{ell|N} ord_2(c_ell)`.

Protected WP16A proves

`s_n(E) := ord_2 #Sel_{2^n}(E/Q) - n
        = ord_2 #Sha(E/Q)[2^n]`

for every `n>=1`, and

`lim_n s_n(E) = len_Z2 Sha(E/Q)[2^infinity]`.

Protected WP16B and WP19 define

`X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`

and prove

`v_2(Fitt^1_{Z_2}(X_E))
 = len_Z2 Sha(E/Q)[2^infinity]
 = lim_n s_n(E)`.

Hence the selected target is exactly

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

Protected WP20 gives the universal rank-one determinant/Bockstein factorization. For an admissible square `Z_2[[T]]` determinant datum specializing to the rank-one module,

`ord_2(coeff_T Theta_E(T))
 = v_2(Fitt^1_{Z_2}(X_E)) + v_2(B_E)`

after every specialization defect has been accounted for exactly.

Thus the remaining campaign is an exact integral determinant/normalization problem. Finite-level stabilization itself is closed.

## Protected chain relevant to the live frontier

- WP05: selected source/target interface; rank one; finite Sha over `Q`; odd rational torsion.
- WP06: exact quadratic `2`-descent discrepancy accounting; no division by `2`; no `2`-power torsion growth over the protected quadratic lane.
- WP07: good-ordinary local-at-`2` correction and unit-root normalization.
- WP09: protected imaginary quadratic field `K`; `2N` split; rank-one auxiliary lane; corrected Disegni `p=2` Gross–Zagier applicability.
- WP12: residual image `GL_2(F_2) ~= S3`.
- WP13: exact Tamagawa/residual-conductor dictionary.
- WP15: square-order information does not determine unsquared `2`-primary length.
- WP16A: finite-level `2^n`-Selmer stabilization.
- WP16B: primitive integral torsion/Fitting realization.
- WP18A–WP18C: exact two-control diagnostic atlas; examples do not prove the selected class.
- WP19: `Fitt^1(X_E)` equals the desired torsion Fitting valuation.
- WP20: universal rank-one Bockstein/determinant factorization.
- WP21: exact primitive cyclotomic specialization sequence with kernel `C_E^vee`.
- WP22–WP36: exact local/control analysis, including literal-`p=2` good-ordinary control, Poitou–Tate incidence, universal norms, unit-root reconciliation, finite comparison terms, square presentation, and finite twisted-reciprocity computation.
- WP37: literal-`p=2` Nekovář cyclotomic Bockstein-height formalism over the totally imaginary field `K`; canonical rank-one height ideal; exact DVR leading-term/length formalism conditional on first-height nondegeneracy.
- WP38: bounded fixed-`2` nondegeneracy/derived-height source screen and exact proof that quadratic base change adds no index to the ambient rank-one Mordell–Weil free lattice.
- WP39: literal-`p=2` exact comparison between Nekovář extended/strict Greenberg compact Selmer cohomology and the classical compact Kummer Selmer group over `K`; all ambient local correction lengths are explicit and the surviving compact comparison is the finite global image subgroup `J_K`.
- WP40: Poitou–Tate duality identifies the annihilator of `J_K` with an exact dual global-hit subgroup `D_K`, giving a complementary-length identity with no rank-one scalar assumption.

## Current D1 boundary

### D1c — analytic determinant at height-one `(2)`

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`

Protected facts:

- Kato gives literal-`p=2` ordinary control away from the height-one prime containing `2`;
- the screened all-height-one upgrades assume an odd prime;
- WP35 gives the algebraic projective-dimension-one square presentation but no analytic generator.

A valid successor must provide a literal-`p=2` analytic characteristic/determinant theorem at `(2)`, or an exact substitute determining the same integral valuation. Do not infer this from an equality after inverting `2`.

## Current D2 boundaries

### D2a — fixed-`2` height nondegeneracy

`MISSING_P2_K_HEIGHT_NONDEGENERACY`

WP37 proves existence of the first cyclotomic height at `p=2`; it does not prove that height is nonzero. Protected MATHFORGE WP38 records that the nearest screened derived-height/Stark-system and Eisenstein-Heegner routes do not apply to the selected fixed-`2`, surjective-`E[2]` branch. This is not a theorem-nonexistence claim.

### D2b — dual global hit over `K`

`MISSING_P2_DUAL_GLOBAL_HIT_OVER_K`

WP39 proves

`0 -> H~^1_f(K,T_2(E)) -> S_2(E/K) -> J_K -> 0`

and computes the exact ambient local length

`len_Z2 R_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

WP40 defines the dual local quotient

`R_K^dual := U_str^perp/U_Kum^perp`

and the dual global hit

`D_K := im((G_A intersect U_str^perp) -> R_K^dual)`.

Under the perfect local quotient pairing, WP40 proves

`ann(J_K)=D_K`.

Hence, with

`j_K:=len_Z2 J_K`, `d_K:=len_Z2 D_K`,

one has exactly

`j_K+d_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

Thus D2b is solved once `D_K` is evaluated. Do not infer `D_K=0`, `J_K=R_K`, or a rank-one character description without proof.

### D2c — Disegni interpolation/test-vector factors

`MISSING_P2_DISEGNI_INTERPOLATION_FACTOR_VALUATIONS`

The corrected Disegni source contains an exact ordinary-normalization identity: Proposition 4.3.4 absorbs the local `p`-interpolation factor into the ordinary toric pairing. In the selected trivial-weight lane the archimedean interpolation factor is one. A successor must bind the exact source-compatible ordinary test vectors and then decompose the resulting `Q^ord` place by place, retaining every measure, bad-prime, and local `2`-adic factor.

### D2d — classical/WP00 normalization

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`

Compare the same Heegner line with the classical Gross–Zagier and WP00 Néron–Tate/period conventions. A `2`-adic height is not a real height.

### D2e — exact descent back to `Q`

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`

Use WP06 to descend the final normalized identity while retaining every global plus/minus overlap/quotient, twist, period, Tamagawa, and local term.

## Immediate executable successor

Two bounded continuations are executable.

### WP41A — Bockstein/dual-hit comparison

Starting from protected WP37, determine whether `D_K` is canonically an image, cokernel, radical, or exact finite quotient of the first cyclotomic Bockstein map/height complex. Do not infer this merely because both constructions use Selmer duality.

The useful target is

`d_K = length(explicit Bockstein/height defect)`

with a statement that remains valid even if the first height is degenerate. Such a theorem would merge part of D2a with D2b.

### WP41B — ordinary Disegni normalization

For the protected trivial-weight ordinary test-vector packet, use Disegni Proposition 4.3.4 to prove the exact cancellation of `e_{2,infinity}` against the corresponding toric-pairing normalization, then reduce D2c to the remaining place-by-place valuation of `Q^ord`.

Any new external theorem premise beyond the already-admitted interfaces must first be admitted through MATHFORGE.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- numerical stabilization to proof;
- parity or modulo-square information to exact length;
- existence of a `p`-adic height to nondegeneracy;
- `D_K` to zero or `J_K` to the full ambient local module without proof;
- a rank-one character description before the relevant dual Selmer structure is proved rank one and torsion-free;
- a formal analogy between Poitou–Tate and Bockstein to an equality of finite modules;
- a Heegner point to a primitive generator without an index proof;
- an ordinary-pairing normalization to a unit claim before all local factors are computed;
- an odd-prime theorem to `p=2`;
- an equality up to a unit to a preferred determinant generator;
- a restricted-family theorem to the full selected class;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact source admission when required, exact-head non-authoring/read-only Adversary and Referee review, affected ordinary CI, protected merge, protected readback, and #164/handoff maintenance.

Recoverable connector, CI, formatting, logging, source-access, compiler, or computational-environment failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
