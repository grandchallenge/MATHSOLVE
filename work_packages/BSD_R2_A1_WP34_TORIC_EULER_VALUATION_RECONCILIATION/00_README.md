# BSD-R2-A1 WP34 — toric Euler valuation reconciliation

## Status

Candidate mathematical work package. No conclusion is protected until exact-head review, affected CI, protected merge, and protected-main readback complete.

## Exact protected inputs

- MATHSOLVE protected base: `e6c98a0494514d3b74924139edefc9aecd817c4d`.
- MATHFORGE protected source authority: `075b91647c22e12aeb0888496966da162db1d771`.
- Protected WP32 real-place determinant-valuation cancellation.
- Protected WP33 odd bad-prime point-completion formula.
- Protected WP22 odd bad-prime Tamagawa/control length.

## Purpose

Protected WP33 isolated, at each odd bad multiplicative prime `ell`, the surplus

`tau_ell := v2(ell-a_ell)`

inside the Burns–Macias finite point-completion term:

`len_Z2 E(Q_ell)^wedge_2
 = tau_ell + v2(c_ell)`.

Protected MATHFORGE WP34 now fixes the matching analytic normalization: the perfect-complex side uses an `S`-truncated L-function obtained by deleting the Euler factors at the same bad primes, and equation (20) fixes the orientation of the finite local comparison term. The source's stronger Section 6 reconciliation theorem is odd-prime only and is not used.

WP34 proves only the resulting literal-`p=2` valuation/Fitting reconciliation.

## Candidate result

Let

`tau_bad(E) := sum_{ell|N} v2(ell-a_ell)`

and

`D_bad^BM := direct_sum_{ell|N} E(Q_ell)^wedge_2`.

Protected WP33 gives

`len_Z2 D_bad^BM
 = tau_bad(E) + sum_{ell|N} v2(c_ell)`.

If `S` and `S0` differ exactly by the odd bad primes, with all other local truncations held fixed, the admitted source convention gives the rational leading-term ratio

`L_S^*/L_{S0}^*
 = product_{ell|N}(1-a_ell/ell)`

and therefore

`v2(L_S^*/L_{S0}^*) = tau_bad(E)`.

Hence

`len_Z2 D_bad^BM
 - v2(L_S^*/L_{S0}^*)
 = sum_{ell|N} v2(c_ell)`.

Equivalently, if

`J_bad^an := 2^tau_bad(E) Z_2`,

then

`Fitt^0_Z2(D_bad^BM)
 = J_bad^an * Fitt^0_Z2(K_bad^vee)`.

This closes the WP33 boundary

`MISSING_P2_BURNS_MACIAS_TORIC_EULER_FACTOR_RECONCILIATION`

at the valuation/Fitting-ideal level only.

## Retained boundaries

WP34 does not prove a canonical determinant-line or determinant-generator equality. In particular it does not close:

- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- protected WP31 `MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT`;
- `BSD-R2-A1`;
- MATHCERT certification.

The source's Theorem 6.5 is not used because its section assumes `p` odd.