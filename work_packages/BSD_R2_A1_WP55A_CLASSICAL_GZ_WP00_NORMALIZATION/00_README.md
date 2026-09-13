# BSD-R2-A1 WP55A — classical Gross–Zagier to WP00 exact normalization

## Status

`RESEARCH_TARGET_NARROWED_EXACT_SCALAR_COMPARISON`

`BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED`.

## Purpose

WP54A resolved the global Disegni ordinary/test-vector factor exactly. WP55A now transports the independently admitted classical Gross–Zagier identity to the protected WP00 analytic quotient

`L'(E,1)/(Omega_E Reg_E)`

without discarding any period, regulator, height, modular-degree, unit, discriminant, twist-L, Tamagawa, Euler, or test-vector scalar.

## Protected inputs

- MATHSOLVE baseline: `9712ced89096a3a7cde6a8630de734423497ac2d`.
- MATHFORGE classical Gross–Zagier source admission: `2207d9a366e84dc7a1f5726e78e3cfe5e4ab1468`.
- Programme WP00 normalization: `grandchallenge/MATH-PROGRAMME@a4eec4259ae6f7e12028cae1384a17ba865926e4`.
- WP09 auxiliary field `K`: `D_K` fundamental, `(D_K,2N)=1`, `2N` split in `K`, and `L(E^D,1) != 0`.
- WP54A exact ordinary scalar:

  `Q^ord = (u_K/h_K) prod_{ell|N}(1+ell^(-1))`.

## Exact classical input

For a modular parametrization

`f:X_0(N)->E`, `f(infinity)=O`,

the admitted conductor-one trivial-character Cai–Shu–Tian formula is

`L'(E/K,1)
 = [8*pi^2 (phi,phi)/(u_K^2 sqrt(|D_K|))]
   * [hhat_K(P_K(f))/deg(f)]`.

The notation `hhat_K` is retained exactly: it is the source Néron–Tate height **over K**.

## WP55A construction

Let `omega_E` be the protected WP00 minimal Néron differential and define

`A_E := (i/2) integral_{E(C)} omega_E wedge overline(omega_E)`.

Retain the source differential-pullback scalar `C_f>0` by

`f^*omega_E = +/- C_f 2*pi*i phi(z) dz`.

The change-of-variables formula for the finite morphism `f` gives exactly

`4*pi^2 C_f^2 (phi,phi) = deg(f) A_E`.

Substitution into the admitted Gross–Zagier formula and protected WP09 factorization yields

`L'(E,1)/(Omega_E Reg_E)
 = R_GZ/WP00(E,K,f)`,

where

`R_GZ/WP00(E,K,f)
 := [2 A_E/(C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))]
    * [hhat_K(P_K(f))/Reg_E]`.

This is an exact equality. It contains no `up to a unit` clause.

## What WP55A proves

WP55A removes Petersson norm and modular degree from the comparison by an exact geometric identity. It places the classical derivative formula directly in the WP00 period/regulator normalization and exposes the remaining scalar discrepancy as one explicit product.

It does **not** prove that the remaining product has a prescribed 2-adic valuation, nor does it identify the classical Heegner height with the protected p-adic height.

## Residual D2d boundary

The previous broad boundary

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`

is narrowed to

`MISSING_EXACT_CLASSICAL_GZ_WP00_RESIDUAL_SCALAR_COMPARISON`.

Equivalently, D2d closes only after an exact theorem determines the campaign-relevant normalization of

`R_GZ/WP00(E,K,f)`

against the protected ordinary/determinant side, with every power of `2` retained.

The two visible subfactors are:

1. `hhat_K(P_K(f))/Reg_E` — source-height, Mordell–Weil-index, and base-field normalization;
2. `2 A_E/(C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))` — archimedean period, modular differential scalar, unit/discriminant, and rank-zero twist central-value normalization.

## Claim firewall

No equality of real and p-adic heights is asserted. No Manin constant is set to one. No rank-zero BSD formula for `E^D` is used. No WP54A factor is canceled. D1c, D2a, and D2e remain open. No BSD, novelty, priority, commercial, or MATHCERT claim is promoted.
