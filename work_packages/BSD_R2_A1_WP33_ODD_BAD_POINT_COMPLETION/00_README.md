# BSD-R2-A1 WP33 — odd bad-prime point completion

## Status

Candidate mathematical work package. No claim is protected until exact-head review, affected CI, protected merge, and protected-main readback complete.

## Exact protected inputs

- MATHSOLVE protected base: `08042c26cee67ddc998163b35503c6d7bb2a0d96`.
- MATHFORGE protected source authority: `3966bccfe4c8e788f0ca978b5d62cd2e20119043`.
- Corrected Burns–Macias Castillo audit blob: `a5773cc31e459f37e1b599f657263415776e69e2`.
- Protected WP22 odd local Neron/component calculation.
- Protected WP13 Tamagawa formulas as already imported by WP22.
- Protected WP32 real-place determinant-valuation cancellation.

## Purpose

The corrected Burns–Macias Castillo equation-(20) interface retains, for every odd bad prime `ell|N`, the finite comparison term

`E(Q_ell)^wedge_2`.

WP33 computes this term exactly at the level of `Z_2`-length and Fitting ideal.

It does not identify the term with Tamagawa data alone and does not assert cancellation with an analytic Euler factor.

## Candidate result

Let `ell|N` be odd. The selected class is semistable, so `E` has multiplicative reduction. Define

`a_ell := +1` for split multiplicative reduction,

`a_ell := -1` for nonsplit multiplicative reduction.

Then WP33 proves

`len_Z2 E(Q_ell)^wedge_2
 = v2(ell-a_ell) + v2(c_ell)`.

Equivalently:

- split multiplicative:
  `len = v2(ell-1)+v2(c_ell)`;
- nonsplit multiplicative:
  `len = v2(ell+1)+v2(c_ell)`.

Hence

`Fitt^0_Z2(E(Q_ell)^wedge_2)
 = 2^(v2(ell-a_ell)+v2(c_ell)) Z_2`.

Protected WP22 gives

`len_Z2(K_ell^vee)=v2(c_ell)`.

Therefore the exact surplus of the Burns–Macias bad-prime point-completion term over the already protected ambient Tamagawa/control term is

`v2(ell-a_ell)`.

## Boundaries

WP33 does not prove:

- cancellation of `v2(ell-a_ell)` against a local analytic Euler factor;
- exact integral identification of Burns–Macias `H^2` with `X_E`;
- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- protected WP31 `MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT`;
- `BSD-R2-A1`;
- MATHCERT certification.

The next determinant-side question is the exact source normalization of the toric factors `ell-a_ell`.