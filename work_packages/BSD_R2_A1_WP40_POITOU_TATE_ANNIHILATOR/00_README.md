# BSD-R2-A1 WP40 — Poitou–Tate annihilator for the `K`-side Kummer/Greenberg defect

## State

`PROVED_BOUNDED_REDUCTION`

Protected predecessor:

`grandchallenge/MATHSOLVE@3d9e94d2b0f06d0e93387f959a0e32c6346e0d21` — WP39.

No new external theorem premise is used. WP40 uses the already-protected literal-`p=2` Greenberg Poitou–Tate/global-local orthogonality interface admitted in MATHFORGE.

## Purpose

WP39 reduces D2b to the finite global image

`J_K subset R_K`,

where

`R_K = U_Kum/U_str`

is the finite local quotient between the classical compact Kummer and strict Greenberg local structures over the protected field `K`.

WP40 dualizes this exact incidence problem rather than guessing that `J_K` is the full local target.

## Main result

Let

`L_Kum := U_Kum^perp`,

`L_str := U_str^perp`

inside the discrete local cohomology of `A=E[2^infinity]`. Then

`L_Kum subset L_str`

and local Tate duality induces a perfect finite pairing

`R_K x R_K^dual -> Q_2/Z_2`,

with

`R_K^dual := L_str/L_Kum`.

Let `G_T` and `G_A` be the compact and discrete global localization images. Define

`D_K := im((G_A intersect L_str) -> R_K^dual)`.

Protected Poitou–Tate orthogonality gives exactly

`ann(J_K) = D_K`.

Therefore, with

`j_K := len_Z2 J_K`, `d_K := len_Z2 D_K`,

one has

`j_K + d_K
 = len_Z2 R_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

No rank-one scalar or global-surjectivity assumption is used.

## D2b reduction

The unknown `j_K` is now exactly complementary to a dual global hit `D_K`. Equivalently,

`D_K ~= Sel_A^{str-perp}(K) / Sel_A^{Kum}(K)`

through the localization map, with the quotient understood as the actual image in `R_K^dual`.

The remaining D2b boundary is

`MISSING_P2_DUAL_GLOBAL_HIT_OVER_K`.

This representation is designed to meet WP37's height/Bockstein lane: the next theorem should determine whether `D_K` is measured by the same dual Selmer direction on which the first Nekovář Bockstein height acts, without assuming nondegeneracy.

## Claim firewall

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

WP40 does not prove:

- `J_K=R_K` or `D_K=0`;
- a value of `j_K` or `d_K`;
- rank one or torsion-freeness of the dual relaxed Selmer structure;
- fixed-`2` height nondegeneracy;
- an identification of `D_K` with a height radical or Bockstein cokernel;
- D1c, D2c, D2d, or D2e;
- BSD or MATHCERT certification.
