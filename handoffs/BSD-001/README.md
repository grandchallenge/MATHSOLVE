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
4. the latest protected frontier file, currently `handoffs/BSD-001/WP43_FRONTIER.md` after WP43A protection;
5. the work package named by that frontier;
6. any earlier protected package on which the intended proof step materially depends;
7. the current protected MATHFORGE BSD provider records before using any external theorem.

Do not restart WP16 or broad WP17 reconnaissance. Later protected work has narrowed the live frontier to exact integral comparison and normalization objects.

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

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

Protected WP20 gives the rank-one determinant/Bockstein factorization; WP35 supplies the primitive cyclotomic square presentation with exact specialization defect. The remaining campaign is an exact integral determinant/height/normalization problem.

## Protected chain relevant to the live frontier

- WP05–WP15: source/target normalization, quadratic descent, good-ordinary `2`-local data, auxiliary field `K`, residual image, Tamagawa dictionary, and parity/square-order firewalls.
- WP16A/WP16B/WP19: exact primitive integral Selmer/Fitting invariant.
- WP20: universal rank-one Bockstein/determinant factorization.
- WP21–WP36: primitive cyclotomic control, local kernels, Poitou–Tate incidence, universal norms, unit-root reconciliation, finite comparison terms, square presentation, and finite twisted-reciprocity computation.
- WP37: literal-`p=2` Nekovar cyclotomic Bockstein-height formalism over totally imaginary `K`; first height exists but nondegeneracy is not proved.
- WP38: bounded fixed-`2` nondegeneracy screen; quadratic base change adds no index to the rank-one Mordell–Weil free lattice.
- WP39: exact literal-`p=2` comparison between Nekovar extended/strict Greenberg compact Selmer cohomology and classical compact Kummer over `K`; finite compact global hit `J_K` isolated.
- WP40: exact Poitou–Tate annihilator theorem `ann(J_K)=D_K` and complementary-length formula.
- WP41A: separates the strict cyclotomic Bockstein from the fixed-level strict/Kummer comparison.
- WP41B: Disegni's source-compatible ordinary normalization gives `e_{2,infinity}^{-1}Q_special=Q^ord` exactly.
- WP42B: for the selected split prime `2`, canonical Appendix-A.3 vectors and measure give `Q^ord_{2,dt_2^can}=1` exactly; global measure rescaling remains explicit.
- WP43A: Nekovar §0.16 is source-qualified for the literal-`p=2` lane; strict Greenberg local conditions are functorial for the first-order cyclotomic augmentation triangle, the strict Selmer complexes form an exact triangle, and the specialization connecting morphism is the WP37 Bockstein.

## Current D1 boundary

### D1c — analytic determinant at height-one `(2)`

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

Kato gives literal-`p=2` control away from the height-one prime containing `2`; screened all-height-one upgrades retain odd-prime restrictions. WP35 is algebraic only. A valid successor must determine the integral analytic determinant at `(2)` or an exact equivalent.

## Current D2 boundaries

### D2a — fixed-`2` height nondegeneracy

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

WP37 proves existence of the first height, not its nonvanishing. WP38 records that the closest screened derived-height/Stark-system and Eisenstein-Heegner routes do not apply to the protected surjective-`E[2]` branch.

### D2b — classical-Kummer Iwasawa object and exact specialization over `K`

WP40 proves

`j_K+d_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`,

where `j_K=len J_K` and `d_K=len D_K`.

Protected WP43A closes the strict-Greenberg augmentation/Bockstein half of the compatibility problem. The exact remaining boundary is

`MISSING_P2_KUMMER_IWASAWA_LOCAL_CONDITION_COMPLEX_AND_SPECIALIZATION_OVER_K`.

A successor must provide an integral cyclotomic classical-Kummer Selmer object over `K`, a strict-to-Kummer comparison morphism, and derived augmentation whose specialized cone is exactly the WP39/WP40 finite strict/Kummer quotient. Comparisons only after inverting `2` or only up to finite error are insufficient.

### D2c — ordinary Disegni local factors

Protected WP41 reduces the corrected p-adic Gross–Zagier normalization to `Q^ord`. Protected WP42B further proves

`Q^ord_{2,dt_2^can}=1`

for Disegni's canonical local vectors and measure at the selected split prime `2`; the canonical p-local toric factor therefore has zero `2`-adic valuation.

This does not make the global ordinary factor a unit. The next exact local boundary is

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

The unresolved `Q^ord` ledger consists of global/local Haar-measure reconciliation, split semistable bad-prime terms, auxiliary finite places, remaining local L/vector normalizations, and residual global/archimedean normalization.

Disegni §4.2 rewrites split toric periods as Rankin–Selberg zeta integrals; the interpolation machinery does not by itself evaluate the semistable Steinberg/newvector integral. No bad-prime unit or valuation formula is protected yet.

### D2d — classical/WP00 normalization

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

Compare the same Heegner line with the classical Gross–Zagier and WP00 Neron–Tate/period conventions. A `2`-adic height is not a real height.

### D2e — exact descent back to `Q`

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

Use WP06 to descend the final normalized identity while retaining every plus/minus overlap, twist, period, Tamagawa, and local term.

## Immediate executable successors

### WP44A — classical-Kummer Iwasawa local condition over `K`

Search narrowly for a literal integral construction that packages the classical Kummer local condition throughout the cyclotomic tower into a Selmer complex over the Iwasawa algebra. Require:

1. literal integral `p=2` validity;
2. compatibility with corestriction/base change through the tower;
3. a strict-Greenberg-to-Kummer comparison morphism;
4. a controlled derived object over the Iwasawa algebra;
5. derived augmentation equal to the WP39/WP40 finite quotient, not merely isogenous to it.

If no admitted source supplies this exact object, the constructive route is to define the mapping-fibre local condition from finite-level Kummer complexes and prove derived base change directly.

### WP44B — split semistable bad-prime toric factors

For each odd semistable `ell|N`, with `K/Q` split at `ell` and `chi_ell=1`, bind the exact local representation and test vector chosen by the Disegni packet and evaluate the normalized split Rankin–Selberg toric integral. Retain split/nonsplit multiplicative type, Steinberg twist, Haar measure, local L-factor, denominator pairing, and any Tamagawa-sensitive scalar.

The target is an exact local contribution to `ord_2(Q^ord)`, not an interpolation theorem or blanket unit claim.

Any new external theorem premise must first be admitted through MATHFORGE.

## Claim firewall

Do not promote:

- `BSD-R2-A1`;
- strict-Greenberg Bockstein naturality to existence of the missing Kummer Iwasawa object;
- a rationalized or finite-error Kummer comparison to the exact `2`-primary defect;
- canonical `Q^ord_2=1` to global `Q^ord=1`;
- interpolation of a local zeta integral to an explicit semistable value;
- height existence to height nondegeneracy;
- an odd-prime or rationalized result to literal integral `p=2`;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge, protected readback, and issue #164/handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions.

Stop only at a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
