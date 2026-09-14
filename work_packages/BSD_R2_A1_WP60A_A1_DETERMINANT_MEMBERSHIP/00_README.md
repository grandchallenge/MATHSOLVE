# BSD-R2-A1-WP60A-A1 — determinant membership at height one `(2)`

## Purpose

Execute the WP60A-A1 falsification test required by protected WP60A-A0.

The question is whether “construct a determinant lift of the analytic/Kato class” is an independent construction problem or simply another form of the missing height-one-`(2)` divisibility.

This package proves the exact determinant-lattice criterion over a discrete valuation ring and applies it as a reduction at the height-one prime `(2)`.

## Protected inputs

- MATHSOLVE WP60A-A0: `20a980fd8fb3e3a4cceabf0e37af838a16c1608e`.
- MATHFORGE WP60A source audit: `e44baeeed5d508fd4e5332c883c837951e51c000`.
- Protected Kato source audit at the same Forge head: `sources/BSD-001/KATO_P2_HEIGHT_ONE_WP17B_SOURCE_AUDIT.md`.
- WP60 tracker: `grandchallenge/MATHSOLVE#215`.

## Result

For a two-term perfect complex over a DVR

`C=[P^1 -> P^2]`

in degrees `1,2`, with `H^1(C)` free rank one and `H^2(C)` finite, the canonical rational determinant trivialization identifies the integral inverse determinant line with

`Fitt^0_R(H^2(C)) * H^1(C)`

inside `H^1(C) tensor_R K`.

Thus for a nonzero class

`z=aP`

with `P` primitive in `H^1(C)`, determinant membership is equivalent to

`v(a) >= length_R H^2(C)`.

The class is the image of a basis of the determinant line exactly when

`v(a)=length_R H^2(C)`.

Consequently:

- `A1-LIFT` is exactly a one-sided Fitting divisibility at height one `(2)`;
- `A1-PRIMITIVITY` is the reverse inequality/equality;
- existence of an integral cohomology class alone does not imply determinant membership.

## Arithmetic consequence

Localizing the relevant rank-one Iwasawa cohomology complex at the height-one prime `(2)` places the problem over a DVR. Kato's protected literal-`p=2` source interface gives torsion/rational rank information but does not supply the all-height-one integral inequality at `(2)`; that clause is protected as requiring `p != 2`.

Therefore the BKS-style determinant lift cannot be obtained merely by repackaging the already protected Kato theorem. A direct finite-level proof would have to establish the same missing one-sided divisibility by genuinely new arithmetic input.

Refined boundary:

`MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.

The primitivity boundary remains

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

## Disposition

WP60A has produced a sharper exact reduction but has not found independent arithmetic input that closes the lift inequality.

Under the WP60 execution contract, the next executable route is WP60B: normalize the Kriz–Li literal-`2` logarithmic condition and test whether it supplies genuinely independent auxiliary-field information or is equivalent to the same unknown index parity.

## Firewall

No determinant lift, height-one-`(2)` divisibility, primitivity, WP59 R5, D2d reopening, BSD-R2-A1, or MATHCERT claim is promoted.
