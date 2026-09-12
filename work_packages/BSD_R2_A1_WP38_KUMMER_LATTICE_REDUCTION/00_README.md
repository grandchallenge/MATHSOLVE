# BSD-R2-A1 WP38 — fixed-`2` height screen and quadratic Kummer-lattice reduction

## State

`PROVED_BOUNDED_REDUCTION`

Protected predecessor:

`grandchallenge/MATHSOLVE@a9b823e526059ffefb62b3d331d85f04c456a97d` — WP37.

Protected source premise:

`grandchallenge/MATHFORGE@5a5bf90af046e91ed13949ad8087c35e6a74d059` — bounded fixed-`2` height-nondegeneracy / derived-height applicability screen.

## Purpose

WP37 left two principal theorem boundaries:

- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_K_HEIGHT_NONDEGENERACY_AND_INTEGRAL_NORMALIZATION_COMPARISON`.

WP38 first screens the narrow D2a theorem query. The closest derived-height and Heegner-point routes screened do not apply literally to the selected good-ordinary, surjective-`E[2]`, fixed-`p=2` branch. This is a bounded source result, not a theorem-nonexistence statement.

WP38 then advances D2b by proving a purely algebraic fact from protected inputs: quadratic base change from `Q` to the protected WP09 field `K` introduces **no index in the global rank-one Mordell–Weil free lattice**. Thus the remaining D2b index cannot be blamed on a hidden enlargement of `E(Q)/tors` inside `E(K)/tors`; it is concentrated in the comparison between Nekovář's source-compatible extended/ordinary Selmer lattice and the primitive Kummer lattice/local conditions.

## Main exact result

Restriction induces an isomorphism

`E(Q)/E(Q)_tors  ~=  E(K)/E(K)_tors`.

Consequently

`E(Q) tensor Z_2  ~=  E(K) tensor Z_2`.

This does **not** say that a Heegner point is primitive, and it does **not** identify the Nekovář extended Selmer lattice with the primitive Kummer lattice.

## Refined D2b boundary

The former D2b label

`height lattice -> primitive Kummer lattice`

is narrowed to

`MISSING_P2_NEKOVAR_EXTENDED_TO_PRIMITIVE_KUMMER_LOCAL_INDEX`.

Any remaining power of `2` in D2b must arise from the exact Selmer/local-condition comparison (including extended-Selmer terms), not from the rank-one Mordell–Weil lattice under `K/Q`.

## Claim firewall

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

WP38 does not prove:

- fixed-`2` height nondegeneracy;
- a literal-`p=2` derived-height bypass;
- equality of Greenberg/extended and primitive Kummer local conditions;
- primitivity of the Heegner point;
- D1c or the full D2 comparison;
- BSD or MATHCERT certification.
