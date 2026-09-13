# BSD-R2-A1 WP52A — finite comparison cone determinant correction

## Operation

`BSD-R2-A1-WP52A-FINITE-CONE-DETERMINANT`

## Protected predecessors

- MATHSOLVE WP51A: `3b34edc3e66c4be86a4319bc71da39bb5fc055f0`.
- MATHFORGE WP51 source state: `79302cdc05f3f11c56e048f68e9095d3280872a7`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

No new external theorem premise is used.

## Objective

WP51A separated the finite Matlis/Pontryagin correction `D_K` from first-height nondegeneracy, but conservatively retained

`MISSING_P2_FINITE_MATLIS_CORRECTION_EVALUATION_OR_CANCELLATION_IN_DETERMINANT_NORMALIZATION`.

WP52A asks the determinant-line question actually required by protected WP20:

> Does the strict-to-Kummer determinant comparison require `d_K=len_Z2 D_K` separately, or does the exact finite comparison cone already determine the entire integral correction?

## Result

Protected WP48A gives the exact triangle

`C_str,0 -> C_Kum,0 -> Q_fin ->`

with

`Q_fin ~= V_K[-1]`

and

`0 -> R_K -> V_K -> Zloc -> 0`.

Because `Q_fin` is finite, the first map is a rational quasi-isomorphism. Determinant additivity therefore identifies the integral determinant-line ratio with the determinant of `Q_fin`.

Using the cohomological convention

`v_det(C) := sum_i (-1)^i len_Z2 H^i(C)`

for a finite perfect complex, one has

`v_det(Q_fin) = -len_Z2 V_K`.

Equivalently, converting in the reverse Kummer-to-strict direction contributes `+len_Z2 V_K`.

Protected WP39 and WP48A give

`len_Z2 R_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`

and, since `2` splits in `K`,

`len_Z2 Zloc = 2 ord_2(3-a_2)`.

Hence

`len_Z2 V_K
 = 4 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

This correction is exact and contains no separate unknown `j_K` or `d_K`.

## D2b disposition

The WP51A boundary is resolved:

`D2b = RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.

The individual finite groups `J_K`, `D_K`, and `K_K^sil` remain meaningful structural invariants, but their separate lengths are not independent inputs to the strict/Kummer determinant-line normalization.

## Claim boundary

WP52A does not prove fixed-`2` height nondegeneracy, D1c, remaining Disegni factors, classical Gross–Zagier/WP00 normalization, final quadratic descent, BSD, or certification.