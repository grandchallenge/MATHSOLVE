# BSD R5-CW-P2-WEIGHT — universal half-weight cover

Operation: `BSD-R5-CW-P2-WEIGHT` / #329.

Protected entering anchors:

- MATHSOLVE launch base: `aca548821935600c36a03b70aca76a4a7f31e03b`;
- MATHFORGE provider: `716979bcae4e67a82c52f15c99b20da555fcdfca`;
- constitutional authority: `grandchallenge/INTELLECT@7662e9b5eeecb065e75173176d535d57a5a42dee`;
- R5-WIT protected completion: `89f7b57b48875990c1df499dc306920ff7419cca`.

## Purpose

The protected provider isolates the first literal-`2` algebraic break in the
Colmez–Wang Chapter-15 determinant-variable descent.  At odd `p`, the
principal weight character can be divided by two inside the same weight
algebra.  At `p=2`, the correct principal weight group is

`Gamma = 1+4 Z_2`

and squaring lands in `1+8 Z_2`, not all of `Gamma`.

This package constructs the exact finite-flat cover on which the universal
weight character does have a continuous square root.

## Result

The package proves:

`Lambda = Z_2[[Gamma]] ~= Z_2[[T]]`, with universal element `U=1+T`, and

`Lambda_half := Lambda[Y]/(Y^2-U)`

is finite free of rank two and complete local.  Equivalently, with
`S=Y-1`,

`Lambda_half ~= Z_2[[S]]`

and the structure map is

`T |-> 2S+S^2`.

The universal half-character is

`kappa_half(5^a)=Y^a=(1+S)^a`, `a in Z_2`,

and satisfies

`kappa_half^2 = kappa`

after base change.

The cover is ramified/non-etale at the residual point; modulo two the weight
map is `T |-> S^2`.

## What this does not prove

This package does not prove that the Colmez–Wang Chapter-15 globalization,
Poitou–Tate argument, classical-point density, or family Kato comparison
commutes with this cover.  The exact successor is

`MISSING_P2_COLMEZ_WANG_SQUARE_ROOT_COVER_CHAPTER15_GLOBALIZATION_COMPATIBILITY`.

Historical R5-RES #273 remains closed.  No residual Kato witness is produced.
