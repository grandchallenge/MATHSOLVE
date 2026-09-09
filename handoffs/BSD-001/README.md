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
4. `work_packages/BSD_R2_A1_WP16A_FINITE_SELMER_STABILIZATION/` — exact finite-level stabilization;
5. `work_packages/BSD_R2_A1_WP16B_INTEGRAL_SELMER_FITTING/` — exact integral dual-Selmer/Fitting realization;
6. protected WP06, WP07, WP09, WP13, WP15 and any other earlier package materially used by the next step;
7. the current protected MATHFORGE BSD provider manifest and exact admitted source audits before external theorem use.

Do not treat mutable issue text or conversational history as mathematical authority.

## Protected mathematical dependency chain

Historical WP00-WP04 remain Programme-owned. Native Solve WP05 onward is the mathematical dependency chain for the current frontier.

WP16A is protected at MATHSOLVE main commit

`3fc4567bfe2a5dfe881378f97a14576494b3a746`.

WP16B was constructed from that protected baseline and the protected MATHFORGE provider baseline

`118ae1b5c2fc2630f53000921b742c610c50db16`.

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

MATHCERT remains pending.

## Closed deductions through WP16B

- WP05 fixes the exact native target/source interfaces, removes the rational-torsion `ord_2` term, and imports analytic-rank-one algebraic rank/finiteness of Sha.
- WP06 records every quadratic `p=2` descent discrepancy exactly and explicitly forbids identifying finite Kummer and Greenberg ordinary local conditions at `2` without proof.
- WP07 fixes the good-ordinary local-at-2 correction surface and proves standard residual ordinary `p`-distinguishedness is unavailable at `p=2`.
- WP08 isolates the cyclotomic height-one `(2)` / relative-mu defect.
- WP09 supplies an all-`2N`-split auxiliary imaginary quadratic field `K` with twist nonvanishing and corrected Disegni p-adic Gross-Zagier applicability at `p=2`.
- WP10 excludes mechanical specialization of the standard odd-prime Heegner-primitivity route.
- WP11 proves exact odd-degree `C3` Selmer/Sha control conditionally on that branch.
- WP12 eliminates the `C3` branch; every selected curve has residual image `GL_2(F_2) ~= S3`.
- WP13 proves the exact local Tamagawa/inertia dictionary and identifies residual-conductor drop with even-Tamagawa support.
- WP14 closes the exact Chao Li applicability matrix.
- WP15 proves finite Sha has square order and that parity/modulo-square information cannot determine the exact unsquared length.
- WP16A proves

  `s_n(E) := ord_2 #Sel_{2^n}(E/Q) - n = ord_2 #Sha(E/Q)[2^n]`

  for every `n >= 1`, proves eventual stabilization, and proves

  `lim_n s_n(E) = len_Z2 Sha(E/Q)[2^infinity]`.

- WP16B fixes the integral invariant. Define the primitive classical direct-limit Kummer Selmer group

  `Sel_{2^infinity}^{Kum}(E/Q) := colim_n Sel_{2^n}(E/Q)`

  and its Pontryagin dual

  `X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`.

  Set

  `D_E := E(Q) tensor (Q_2/Z_2)`

  and

  `L_E := D_E^vee`.

  Protected rank one and odd torsion make `L_E` free of rank one over `Z_2`, without choosing a basis. The WP16B theorem package proves canonically

  `0 -> Sha(E/Q)[2^infinity]^vee -> X_E -> L_E -> 0`,

  and therefore

  `T_E := Tor_{Z_2}(X_E) = Sha(E/Q)[2^infinity]^vee`.

  Consequently

  `len_Z2 T_E = lim_n s_n(E)`

  and exactly as an ideal

  `Fitt^0_{Z_2}(T_E) = 2^{lim_n s_n(E)} Z_2`.

  Thus the selected unresolved equality is exactly equivalent to

  `delta_2(E) = v_2(Fitt^0_{Z_2}(T_E))`.

## Exact local-condition contract after WP16B

The invariant uses the primitive classical Kummer condition at every place and every finite level:

`im(E(Q_v)/2^n E(Q_v) -> H^1(Q_v,E[2^n]))`.

This includes the real place, the good-ordinary place `2`, every bad semistable prime `ell | N`, and every other finite place.

The following substitutions are forbidden without an exact comparison theorem:

- Kummer local condition at `2` -> Greenberg/ordinary connected-etale condition;
- primitive bad-prime Kummer condition -> unramified/strict/relaxed/imprimitive condition;
- saturated rank-one quotient `X_E/T_E ~= L_E` -> the span of a possibly nonprimitive Heegner or Mordell-Weil generator;
- `Fitt^0(T_E)` -> `Fitt^0(X_E)`.

Any exact finite kernel, cokernel, index, determinant, or local correction produced by such a comparison must retain its complete `2`-adic length.

## Current exact frontier after WP16B

Define

`delta_2(E) := ord_2(L'(E,1)/(Omega_E Reg_E)) - sum_{ell|N} ord_2(c_ell)`.

WP16B has completed the representation change

`finite Selmer tower -> exact integral Fitting invariant`.

The next frontier is

`BSD-R2-A1-S3-K-INTEGRAL-FITTING-CONTROL`.

The named substantive boundary is

`MISSING_P2_INTEGRAL_FITTING_CONTROL_OVER_PROTECTED_K`.

This boundary does not assert theorem nonexistence. It names the next proof/source obligation.

## Immediate next executable tranche

**WP17A — narrowly targeted MATHFORGE reconnaissance and applicability audit.**

Search only for theorem interfaces that literally include `p=2` and control over the protected WP09 field `K` one of:

1. the primitive rank-one dual-Selmer torsion/Fitting invariant analogous to `Fitt^0(T_E)`;
2. a Selmer-complex determinant/Fitting invariant with an exact comparison to that primitive invariant;
3. a one-sided integral divisibility plus a primitivity/reverse-divisibility theorem sufficient to determine the exact valuation.

For every candidate, verify before admission:

- literal prime range including `2`;
- coefficient-ring hypotheses;
- residual representation hypotheses;
- self-duality and archimedean hypotheses;
- local condition at each place above `2`;
- compatibility or exact defect relative to the WP16B Kummer condition;
- bad-prime primitive/imprimitive conditions;
- exact Tamagawa and residual-conductor corrections in both WP13 regimes;
- treatment of the saturated rank-one free direction and any Heegner-index defect;
- exact strength: equality, inclusion, divisibility, primitivity, characteristic/Fitting ideal, or unit class;
- exact quadratic descent compatibility with WP06;
- whether an explicit reciprocity law reaches the WP00 normalized complex derivative.

Any new external theorem premise must be admitted through MATHFORGE before protected theorem use.

## WP18 availability

WP18 may now begin because both the finite-level observable and the integral target invariant are fixed. The atlas remains diagnostic only. Numerical stabilization or numerical equality may not be promoted to proof or certification.

## Tamagawa normalization

WP16B uses primitive Kummer local conditions and does not insert a separate Tamagawa factor into `T_E`.

The analytic side remains

`delta_2(E) = ord_2(L'/(Omega Reg)) - sum_{ell|N} ord_2(c_ell)`.

Protected WP13 supplies the exact local Tamagawa valuations and residual-conductor regime. A WP17 theorem using imprimitive local conditions must prove the exact comparison defect; no `c_ell` may be called a `2`-adic unit when it is even.

## Claim firewall

- `BSD-R2-A1` remains unproved.
- WP16A and WP16B are exact representation theorems, not the analytic-to-arithmetic equality.
- Numerical stabilization is observation, not proof.
- Parity or modulo-square control is not exact length.
- “Up to a unit” is not license to lose a power of `2`.
- Kummer and Greenberg ordinary conditions at `2` remain distinct interfaces until compared exactly.
- Restricted-family or all-Tamagawa-odd theorems do not become uniform selected-class results.
- Source admission is not MATHCERT certification.
- No novelty, priority, patentability, or commercial claim follows from this programme.

## Execution and continuity

Proceed autonomously through bounded proof, falsification, sharply targeted source reconnaissance, MATHFORGE admission when necessary, exact-subject non-authoring/read-only Adversary and Referee review, affected CI, protected merge, protected readback, and issue/handoff maintenance. Routine authorized gates do not require Human Steward intervention unless the live governing instrument materially reserves them.

Recoverable tooling, connector, CI, formatting, logging, or workflow failures are not stopping conditions.

Stop only for a genuine theorem/source/authority/authentication/safety/material-state boundary, target or normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
