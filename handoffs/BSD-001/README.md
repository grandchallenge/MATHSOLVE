# BSD-001 native continuation handoff

## Target repository and authority

- Target repository: `grandchallenge/MATHSOLVE`.
- Current programme owner: `grandchallenge/MATHSOLVE#164`.
- Constitutional authority remains the protected GCL authority chain already bound by the campaign.
- Source/provider admission remains MATHFORGE-owned.
- Mathematical certification remains MATHCERT-only.

## Canonical continuation files

Read in this order after re-fetching protected live state:

1. `handoffs/BSD-001/README.md` — current frontier and authority map;
2. `handoffs/BSD-001/RESEARCH_PLAN_WP16_WP18.md` — approved theorem-construction programme;
3. `handoffs/BSD-001/TAKEOVER_PROMPT_WP16_WP18.md` — reusable fresh-session takeover pointer;
4. `work_packages/BSD_R2_A1_WP16A_FINITE_SELMER_STABILIZATION/` — the finite-level theorem now controlling the representation change;
5. protected WP15 and any earlier work package referenced by the next proof step;
6. the current protected MATHFORGE BSD provider manifest and exact admitted source audits before external theorem use.

Do not treat mutable issue text or conversational history as mathematical authority.

## Protected mathematical state through WP16A

Historical WP00-WP04 remain Programme-owned. Native Solve WP05-WP16A is the mathematical dependency chain for the current frontier.

WP16A was constructed from protected MATHSOLVE baseline

`93b1348d5e4ae77ededd0b5b779780112876c3d8`

and protected MATHFORGE provider baseline

`118ae1b5c2fc2630f53000921b742c610c50db16`.

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

MATHCERT remains pending.

## Closed deductions through WP16A

- WP05 fixes the exact native target/source interfaces, removes the rational-torsion `ord_2` term, and imports analytic-rank-one algebraic rank/finiteness of Sha.
- WP06 records every quadratic `p=2` descent discrepancy exactly.
- WP07 proves the forced good-ordinary local-at-2 corrections and residual non-distinguishedness.
- WP08 isolates the cyclotomic height-one `(2)` / relative-mu defect.
- WP09 supplies an all-`2N`-split auxiliary imaginary quadratic field with twist nonvanishing and corrected Disegni p-adic Gross-Zagier applicability at `p=2`.
- WP10 excludes mechanical specialization of the standard odd-prime Heegner-primitivity route.
- WP11 proves exact odd-degree `C3` Selmer/Sha control conditionally on that branch.
- WP12 eliminates the `C3` branch; every selected curve has residual image `GL_2(F_2) ~= S3`.
- WP13 proves the exact local Tamagawa/inertia dictionary and identifies residual-conductor drop with even-Tamagawa support.
- WP14 closes the exact Chao Li applicability matrix: auxiliary order-two-Frobenius level-raising primes are constructible, while all-bad-Tamagawa-odd, local nontriviality at `2`, and minimal 2-Selmer remain substantive source restrictions.
- WP15 proves finite Sha has square order via the protected Cassels-Tate interface and finite-group algebra; therefore its `2`-primary length is even, and modulo-square/parity information cannot determine the exact unsquared length. WP15 also closes the four named screened source escape routes without asserting literature nonexistence.
- WP16A proves for every `n >= 1`

  `s_n(E) := ord_2 #Sel_{2^n}(E/Q) - n = ord_2 #Sha(E/Q)[2^n]`,

  proves eventual stabilization, and proves

  `lim_n s_n(E) = len_Z2 Sha(E/Q)[2^infinity]`.

  The proof uses rank one, odd rational torsion, finite Sha, Kummer exactness, and elementary group algebra only. It does not use BSD.

## Current exact frontier after WP16A

Define

`delta_2(E) := ord_2(L'(E,1)/(Omega_E Reg_E)) - sum_{ell|N} ord_2(c_ell)`.

WP16A proves that the selected unresolved equality is exactly equivalent to

`delta_2(E) = lim_{n -> infinity} s_n(E)`.

The campaign has therefore crossed the finite-level representation step. The next frontier is

`BSD-R2-A1-S3-INTEGRAL-SELMER-REPRESENTATION`.

The named substantive boundary is

`MISSING_EXACT_INTEGRAL_SELMER_INVARIANT_REALIZATION`.

This boundary does not assert that such an invariant or theorem is absent from the literature. It states the next construction obligation: realize the already-proved stable integer as an exact integral Selmer-complex/determinant/Fitting invariant with no hidden `2`-power discrepancy.

## Immediate next executable tranche

**WP16B — exact integral representation.**

Identify the precise finite/integral Selmer complex, determinant line, Fitting ideal, torsion quotient, cone, or equivalent invariant realizing

`lim_n (ord_2 #Sel_{2^n}(E/Q) - n)`.

The theorem package must specify explicitly:

- coefficient ring;
- local condition at `2`;
- local conditions at all bad semistable primes;
- treatment of the rank-one free Mordell-Weil direction;
- the exact finite/torsion object whose length is measured;
- Tamagawa and primitive/imprimitive factors;
- determinant/Fitting normalization;
- any defect between competing Selmer-complex normalizations.

No equality may be recorded merely “up to a unit” when its `2`-adic valuation is part of the target.

Protect WP16B before committing WP17 to a theorem family. Only after the integral invariant is fixed should MATHFORGE reconnaissance be narrowed to external theorems that literally control that object at `p=2`.

## Subsequent approved path

After WP16B:

`exact integral Selmer invariant`

`-> integral p=2 control over the protected WP09 imaginary quadratic field K`

`-> exact quadratic descent back to Q using WP06 discrepancy accounting`.

WP18 may begin once the finite/integral invariant to measure is fixed. Numerical stabilization remains observation only.

## Source discipline

The protected Forge stack currently contains the prior BSD source interfaces through the Cassels-Tate audit. New candidates in modern Selmer-complex/Euler-system/Fitting work, explicit reciprocity, or computational Selmer/Cassels-Tate work are reconnaissance leads only until admitted through MATHFORGE.

No theorem with an odd-prime or `p>2` hypothesis may be silently specialized to `p=2`.

WP16A introduced no new external theorem premise.

## Claim firewall

- `BSD-R2-A1` remains unproved.
- The WP16A equivalence is a representation theorem, not the BSD equality itself.
- Numerical stabilization is observation, not proof.
- Parity or modulo-square control is not exact length.
- “Up to a unit” is not exact integral equality without proof.
- Restricted-family results do not become uniform selected-class results.
- Source admission is not MATHCERT certification.
- No novelty, priority, patentability, or commercial claim follows from this programme.

## Execution and continuity

Proceed autonomously through bounded proof, falsification, source reconnaissance, MATHFORGE admission when necessary, exact-subject non-authoring/read-only Adversary and Referee review, affected CI, protected merge, protected readback, and issue/handoff maintenance. Routine authorized gates do not require Human Steward intervention unless the live governing instrument materially reserves them.

Recoverable tooling, connector, CI, formatting, logging, or workflow failures are not stopping conditions.

Stop only for a genuine theorem/source/authority/authentication/safety/material-state boundary, target or normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.