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
4. the latest protected frontier file, currently `handoffs/BSD-001/WP41_FRONTIER.md` after WP41 protection;
5. the work package named by that frontier;
6. any earlier protected package on which the intended proof step materially depends;
7. the current protected MATHFORGE BSD provider records before using any external theorem.

Do not restart WP16 or broad WP17 reconnaissance. Their representation changes remain protected background; later work has narrowed the actual frontier substantially.

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

Hence the selected theorem is exactly

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E)`

with the closing parenthesis understood as the Fitting ideal valuation.

Protected WP20 gives the rank-one determinant/Bockstein factorization, and WP35 supplies the primitive cyclotomic square presentation with exact specialization defect. The remaining campaign is therefore an exact integral determinant/height/normalization problem, not a finite-level stabilization problem.

## Protected chain relevant to the live frontier

- WP05–WP15: source/target normalization, quadratic descent, good-ordinary `2`-local data, auxiliary field `K`, residual image, Tamagawa dictionary, and parity/square-order firewalls.
- WP16A/WP16B/WP19: exact primitive integral Selmer/Fitting invariant.
- WP20: universal rank-one Bockstein/determinant factorization.
- WP21–WP36: primitive cyclotomic control, local kernels, Poitou–Tate incidence, universal norms, unit-root reconciliation, finite comparison terms, square presentation, and finite twisted-reciprocity computation.
- WP37: literal-`p=2` Nekovar cyclotomic Bockstein-height formalism over totally imaginary `K`; first height exists but nondegeneracy is not proved.
- WP38: bounded fixed-`2` nondegeneracy source screen; quadratic base change adds no index to the rank-one Mordell–Weil free lattice.
- WP39: exact literal-`p=2` comparison between Nekovar extended/strict Greenberg compact Selmer cohomology and classical compact Kummer over `K`; finite compact global hit `J_K` isolated.
- WP40: exact Poitou–Tate annihilator theorem `ann(J_K)=D_K` and complementary-length formula.
- WP41A: protected interfaces do not yet identify `D_K` with a Bockstein/height defect; an Iwasawa-level strict/Kummer compatibility theorem is required.
- WP41B: in Disegni's source-compatible ordinary normalization, `e_{2,infinity}^{-1}Q_special=Q^ord` exactly; the remaining D2c datum is the place-by-place valuation of `Q^ord`.

## Current D1 boundary

### D1c — analytic determinant at height-one `(2)`

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

Kato gives literal-`p=2` control away from the height-one prime containing `2`; screened all-height-one upgrades retain odd-prime restrictions. WP35 is algebraic only. A valid successor must determine the integral analytic determinant at `(2)` or an exact equivalent.

## Current D2 boundaries

### D2a — fixed-`2` height nondegeneracy

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

WP37 proves existence of the first height, not its nonvanishing. WP38 records that the closest screened derived-height/Stark-system and Eisenstein-Heegner routes do not apply to the protected surjective-`E[2]` branch.

### D2b — dual global hit and Bockstein compatibility over `K`

WP40 proves

`j_K+d_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`,

where `j_K=len J_K` and `d_K=len D_K`.

WP41A proves that the current protected chain does not contain the naturality theorem required to identify `D_K` with a WP37 Bockstein image/radical/subquotient. The exact bridge is

`MISSING_P2_IWASAWA_STRICT_KUMMER_BOCKSTEIN_COMPATIBILITY_OVER_K`.

Do not infer `D_K=0`, `J_K=R_K`, or equality with a height defect.

### D2c — ordinary Disegni local factors

`MISSING_P2_DISEGNI_QORD_LOCAL_FACTOR_VALUATIONS`.

Protected MATHFORGE WP41B and downstream WP41B prove, for the selected trivial-weight special ordinary test vectors,

`e_{2,infinity}^{-1} Q_special = Q^ord`.

The interpolation factor no longer needs a separate valuation in this normalization. Disegni Lemma 4.3.3 / (4.3.4) decomposes `Q^ord` into explicit local toric pairings, Haar-volume terms, local L-factors, vector-normalization factors, and the ordinary `p infinity` term. Every one of those factors remains to be evaluated exactly.

### D2d — classical/WP00 normalization

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

Compare the same Heegner line with the classical Gross–Zagier and WP00 Neron–Tate/period conventions. A `2`-adic height is not a real height.

### D2e — exact descent back to `Q`

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

Use WP06 to descend the final normalized identity while retaining every plus/minus overlap, twist, period, Tamagawa, and local term.

## Immediate executable successors

### WP42A — Iwasawa strict/Kummer Bockstein compatibility

Search narrowly for, or construct from Nekovar's mapping-fibre formalism, a `K`-side cyclotomic comparison triangle

`C_str,infty -> C_Kum,infty -> Q_infty -> C_str,infty[1]`

whose derived augmentation recovers WP39/WP40 and whose augmentation connecting maps commute with the WP37 Bockstein.

A theorem only after inverting `2`, only up to finite error, or only for odd `p` is insufficient.

### WP42B — exact valuation ledger for `Q^ord`

Bind the exact ordinary test-vector packet and evaluate Disegni (4.3.4) place by place. Start at the split prime `2`, then the split bad primes `ell|N`, then the remaining auxiliary/unramified places and global measure convention.

The target is an additive exact ledger for `ord_2(Q^ord)`, not a blanket unit assertion.

Any new external theorem premise must first be admitted through MATHFORGE.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- numerical stabilization, parity, or modulo-square information to exact proof;
- height existence to height nondegeneracy;
- formal similarity between Poitou–Tate and Bockstein to equality of finite modules;
- source-normalization cancellation to `ord_2(Q^ord)=0`;
- a local `Q^ord` factor to a unit without exact calculation;
- a Heegner point to a primitive generator without an index proof;
- an odd-prime theorem to `p=2`;
- an equality after inverting `2` or up to a unit to an integral determinant claim;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge, protected readback, and issue #164/handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
