# BSD-001 frontier after WP56A

## Protected anchors

- MATHSOLVE pre-WP56A protected head: `456656135cd425410d3b64d46d56d7702171f3b5`.
- MATHFORGE WP56 protected source head: `6c2f7c8a9a1f646ad48eb1fd13eba845343bf6dd`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

This frontier becomes authoritative only after the containing WP56A candidate is protected and read back from `main`.

## WP56A result

Let `P` be a primitive generator of `E(Q)/E(Q)_tors`. Protected WP38 gives

`E(Q)/E(Q)_tors ->~ E(K)/E(K)_tors`.

Hence the CST Heegner trace has a unique free coordinate

`P_K(f)=m_K(f)P+T`,

with `T` torsion and `m_K(f) != 0`.

Protected MATHFORGE WP56 admits the exact CST/YZZ height conversion on the quadratic lane:

`hhat_K(Q)=2 hhat_Q(Q)`.

Since the WP00 rank-one regulator is `Reg_E=hhat_Q(P)`, WP56A proves

`hhat_K(P_K(f))/Reg_E = 2 m_K(f)^2`

and therefore

`ord_2(hhat_K(P_K(f))/Reg_E)
 = 1 + 2 ord_2(m_K(f))`.

Substitution into protected WP55A yields exactly

`L'(E,1)/(Omega_E Reg_E)
 = 4 m_K(f)^2 A_E
   / (C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))`.

No valuation is assigned to the remaining real period/twist scalar before an exact algebraicity comparison.

## D2d disposition

The height-over-K versus WP00-regulator normalization subdefect is resolved.

The remaining D2d boundary is

`MISSING_EXACT_HEEGNER_INDEX_AND_AREA_PERIOD_TWIST_SCALAR_COMPARISON`.

It has two explicit components:

### H1 — genuine Heegner index

Determine `ord_2(m_K(f))` at literal `p=2` for the selected class. Protected WP10 proves that the screened odd-prime Heegner-primitivity/rank-lowering chain cannot be specialized mechanically to `p=2`. Do not infer that `m_K(f)` is odd.

### H2 — exact area/period/twist scalar

Transport

`A_E/(C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))`

onto an exact algebraic/rational line and determine its `2`-adic contribution. Retain real/imaginary period, connected-component, minimal-differential/Manin, discriminant, unit, and rank-zero twist normalization factors explicitly.

A particularly sharp next source/theorem query is an exact rank-zero twist/modular-period identity compatible with the WP00 minimal Néron differential and the same modular parametrization `f`. Do not assume rank-zero BSD for `E^D` merely because `L(E^D,1) != 0`.

## Other live boundaries

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2b: `RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.
- D2c: `RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.
- `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## Execution order

1. Protect WP56A after exact-head Adversary, Referee, ordinary CI and GCL conformance.
2. Pursue H2 by internal normalization algebra and sharply scoped source admission if required; this lane may progress independently of the H1 primitivity barrier.
3. Pursue H1 only with literal-`p=2` evidence; do not reopen generic odd-prime screening already rejected.
4. Once D2d is on an exact algebraic `2`-adic line, replay WP06 normalization descent for D2e.

No MATHCERT certification, novelty, priority, patentability, or commercial claim is promoted.
