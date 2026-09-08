# BSD-R2-A1-WP08 — exact `(2)`-height / mu firewall

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP08-2MU-FIREWALL`.
- Native owner: `grandchallenge/MATHSOLVE#143`.
- Parent: `BSD-R2-A1-WP07-2RECIPROCITY-LENGTH`.
- Protected baseline: `6cdaecdbf5d3acd1389c5f2bbbbf91ea3b32af58`.
- Claim boundary: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Primary type: exact commutative-algebra/Iwasawa interface theorem plus source-bounded route audit.

## Material result

Let

`Lambda = Z_2[[T]]`.

For nonzero `f,g in Lambda`, suppose their height-one valuations agree at every height-one prime other than `(2)`. Then there is a unique integer `delta` and a unit `u in Lambda^x` such that, in `Frac(Lambda)`,

`f = 2^delta u g`.

Moreover

`delta = v_(2)(f)-v_(2)(g)`.

Thus equality after inverting `2` determines an integral principal ideal only up to one exact codimension-one datum: a power of `2`.

If `f` and `g` are characteristic elements, this exponent is the difference of their cyclotomic Iwasawa `mu` exponents. If their first nonzero augmentation coefficients occur in degree `r`, then multiplication by `2^delta u` shifts the `ord_2` of that first nonzero coefficient by exactly `delta`.

This is the quantity that an exact 2-primary BSD valuation cannot discard.

## Firewall

This theorem does not assert that any currently screened p=2 main-conjecture theorem supplies equality away from `(2)`. It says something logically stronger for route checking: even a hypothetical complete away-from-`(2)` equality would still not determine the integral 2-primary leading coefficient without the missing `(2)` exponent.

Kato's actual p=2 statements are recorded separately as external reconnaissance and are one-sided at the relevant stage; they do not turn the conditional firewall into a main-conjecture proof.

## Relation to WP07

WP07 computed a forced **local interpolation correction**:

`ord_2((1-alpha^(-1))^2) in {2,4}`

under the normalization containing that multiplier.

WP08 identifies a different object: a **global Iwasawa mu defect** at the height-one prime `(2)`. The known local correction cannot be substituted for the unknown global exponent.

## What remains open

A successful route must now do one of two things:

1. determine the missing `(2)` component integrally and then supply the rank-one reciprocity/height comparison; or
2. bypass cyclotomic characteristic ideals with an exact p=2 Heegner/Kolyvagin or other arithmetic-length theorem that reaches the same WP00-normalized valuation directly.

WP08 does not prove either deep input.