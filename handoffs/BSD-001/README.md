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
4. the latest protected frontier file, currently `handoffs/BSD-001/WP39_FRONTIER.md` after WP39 protection;
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
- WP39: literal-`p=2` exact comparison between Nekovář extended/strict Greenberg compact Selmer cohomology and the classical compact Kummer Selmer group over `K`; all ambient local correction lengths are explicit and the surviving comparison is the finite global image subgroup `J_K`.

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

### D2b — exact global hit in the Greenberg-to-Kummer comparison over `K`

`MISSING_P2_KUMMER_GREENBERG_GLOBAL_HIT_SUBGROUP_OVER_K`

WP38 proves

`E(Q)/tors ~= E(K)/tors`

and therefore

`E(Q) tensor Z_2 ~= E(K) tensor Z_2`.

WP39 further proves

`H~^1_f(K,T_2(E)) ~= S_T^str(K)`

and the exact sequence

`0 -> H~^1_f(K,T_2(E))
   -> S_2(E/K)
   -> J_K
   -> 0`,

where `J_K` is the actual image in the finite strict-Greenberg-to-classical-Kummer local comparison module.

The ambient local module has exact length

`2 ord_2(3-a_2)
 + 2 sum_{ell|N} ord_2(c_ell)`.

Thus all ambient local sizes and the global quadratic free-lattice factor are closed. The remaining D2b integer is

`j_K := len_Z2 J_K`.

Do not replace `J_K` by the whole ambient target without an exact global-incidence theorem.

### D2c — Disegni interpolation/test-vector factors

`MISSING_P2_DISEGNI_INTERPOLATION_FACTOR_VALUATIONS`

Compute exactly the `2`-adic ideal/valuation of Disegni's `e_{2,infinity}^{-1} Q` in the protected all-`2N`-split test-vector packet and reconcile it with WP07/WP30. Do not call any factor a unit without proof.

### D2d — classical/WP00 normalization

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`

Compare the same Heegner line with the classical Gross–Zagier and WP00 Néron–Tate/period conventions. A `2`-adic height is not a real height.

### D2e — exact descent back to `Q`

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`

Use WP06 to descend the final normalized identity while retaining every global plus/minus overlap/quotient, twist, period, Tamagawa, and local term.

## Immediate executable successor

Proceed with WP40 on D2b, and continue D2c in parallel where exact source normalization is available.

The narrow WP40 theorem query is:

> Use the already-protected literal-`p=2` Poitou–Tate orthogonality to represent `J_K` as an exact annihilator/global-hit subgroup for the nested strict-Greenberg and classical-Kummer Selmer structures over `K`. Retain the full dual Selmer module unless rank-one/torsion-free structure is proved; do not force a scalar character prematurely.

A useful exact target is an identity of the form

`ann(J_K) = D_K`

inside the Pontryagin-dual finite local quotient, where `D_K` is the image of the corresponding dual global Selmer structure. Equivalently, prove

`len_Z2 J_K + len_Z2 D_K = len_Z2 R_K`

when the local quotient pairing is shown perfect.

The parallel D2c query remains:

> In the exact corrected Disegni Theorem B normalization already admitted in WP09, what are the `2`-adic ideals/valuations of `e_{2,infinity}` and the test-vector ratio `Q` for the protected all-`2N`-split packet, and which factors coincide with the WP07/WP30 unit-root ideal?

Any new external theorem premise must be admitted through MATHFORGE before use.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- numerical stabilization to proof;
- parity or modulo-square information to exact length;
- existence of a `p`-adic height to nondegeneracy;
- equality of Mordell–Weil free lattices to equality of Selmer local conditions;
- `J_K` to the full ambient local module without proof;
- a rank-one character description before the relevant dual Selmer structure is proved rank one and torsion-free;
- a Heegner point to a primitive generator without an index proof;
- an odd-prime theorem to `p=2`;
- an equality up to a unit to a preferred determinant generator;
- a restricted-family theorem to the full selected class;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact source admission when required, exact-head non-authoring/read-only Adversary and Referee review, affected ordinary CI, protected merge, protected readback, and #164/handoff maintenance.

Recoverable connector, CI, formatting, logging, source-access, compiler, or computational-environment failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
