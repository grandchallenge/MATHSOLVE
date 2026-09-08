# Remaining deep theorem: `BSD-R2-A1-2ND-MAIN-RECIPROCITY`

## Purpose

WP05 removed the torsion valuation. WP06 removed the integral quadratic-descent ambiguity. WP07 removes two local-at-2 ambiguities: the unit-root correction is explicit and the standard residual-distinguished hypothesis is known to fail.

The remaining problem is therefore a genuine rank-one analytic-to-arithmetic theorem at `2`.

## Acceptable direct-over-Q theorem

A direct theorem is sufficient if, under exactly the selected `BSD-R2-A1` hypotheses, it determines

`ord_2(L'(E,1)/(Omega_E Reg_E))`

as

`len_Z2 Sha(E/Q)[2^infinity] + sum_{ell|N} ord_2(c_ell)`

with no omitted 2-power.

If proved through ordinary Iwasawa theory, the theorem must explicitly:

1. define the ordinary local condition from the actual good-ordinary 2-divisible-group filtration;
2. work in the non-distinguished residual situation forced by WP07, or prove an exact replacement control theorem;
3. give an integral characteristic/Fitting/finite-length equality rather than equality after inverting `2`;
4. state the p-adic L-function normalization and restore the exact unit-root correction from WP07 when that normalization contains it;
5. connect the rank-one p-adic analytic object to the WP00-normalized complex derivative through an explicit reciprocity, p-adic Gross-Zagier, Heegner-index, or equivalent theorem;
6. retain every Tamagawa, Euler, period, isogeny, Manin, and interpolation correction with its exact `ord_2` contribution.

## Acceptable auxiliary-quadratic theorem

An auxiliary theorem may instead choose an imaginary quadratic `K/Q` satisfying all Heegner and local hypotheses, preferably with every prime dividing `2N` split. It must then provide enough exact rank-one and rank-zero information to combine with WP06.

In particular it must determine, rather than suppress:

- the rank-one 2-primary length over `K`;
- the rank-zero twist contribution over `Q`, unless it is independently proved zero or known exactly;
- all remaining WP06 global defects `D_n^+`, `D_n^-`, `I_n`, `Q_n` at the level needed by the final length computation;
- the exact analytic factorization and period comparison needed to recover the base-curve WP00 normalization.

## Equivalent Heegner/Kolyvagin formulation

A theorem proving integral `p=2` primitivity of the relevant Heegner/Kolyvagin system, together with exact Gross-Zagier and local-index formulas, is also admissible if it yields the same final valuation identity. The campaign does not privilege an Iwasawa characteristic-ideal presentation over an equivalent exact arithmetic-length theorem.

## Rejection test

A candidate theorem is insufficient if any essential conclusion is stated only:

- for odd `p` or `p>2`;
- after inverting `2`;
- up to a power of `2`;
- under residual `p`-distinguishedness without a p=2 replacement;
- under `2 not| #E_tilde(F_2)`;
- for a bounded twist family that does not cover the selected curve;
- with an unspecified conversion from its p-adic normalization to the WP00 complex normalization.

## Claim boundary

This file is an acceptance specification for the missing theorem. It is not a proof that such a theorem currently exists.