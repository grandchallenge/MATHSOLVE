# BSD-R2-A1-WP07 — forced local-at-2 corrections and reciprocity lane audit

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP07-2RECIPROCITY-LENGTH`.
- Native owner: `grandchallenge/MATHSOLVE#140`.
- Parent: `BSD-R2-A1-WP06-2DESCENT-CONTROL`.
- Protected baseline: `0001c883adaa916571cafd54c09cc7a685dfd5a7`.
- Claim boundary: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Primary type: proved local lemmas plus source-bounded route elimination.

## Material result

For a selected curve, good ordinary reduction at `2` forces

`a_2 in {+1,-1}`

and therefore

`#E_tilde(F_2) = 3-a_2 in {2,4}`.

Thus the commonly used local condition `2 not| #E_tilde(F_2)` cannot occur in this campaign class.

Let `alpha` be the 2-adic unit root of

`X^2-a_2 X+2`.

Then

`ord_2(1-alpha^(-1)) = ord_2(3-a_2)`.

Consequently, under the ordinary normalization whose interpolation multiplier is `(1-alpha^(-1))^2`, that multiplier has exact valuation

- `2` if `a_2=+1`;
- `4` if `a_2=-1`.

It is never a 2-adic unit.

A second independent obstruction is also forced. The residual ordinary filtration at `2` has one-dimensional characters valued in `F_2^x`. Since `F_2^x={1}`, the two residual characters coincide. Hence the standard residual `p`-distinguished condition is impossible at `p=2` for the coefficient field of an elliptic curve over `Q`.

## Consequence

The missing bridge is no longer accurately described as merely an odd-prime theorem waiting to be specialized. Any successful ordinary Iwasawa/reciprocity route must handle both:

1. a non-unit local interpolation correction with a known exact valuation; and
2. the non-distinguished residual ordinary representation at `2`.

Current external results screened in this package either exclude `p=2` explicitly or treat bounded twist/rank families rather than the selected uniform leading-term identity. They remain external reconnaissance, not theorem premises.

## What remains open

WP07 does not prove an integral main conjecture, a rank-one explicit reciprocity law, a p-adic Gross-Zagier theorem at `2`, or `BSD-R2-A1`. It converts the remaining problem into the narrower `BSD-R2-A1-2ND-MAIN-RECIPROCITY` obligation defined in this package.