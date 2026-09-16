# BSD R5-PRIM — source and dependency note

## Protected provider

The operation binds MATHFORGE protected `main` at
`5aef30aa64730ca777329013e1e33c03f34a6e3a`, specifically:

`sources/BSD-001/CASTELLA_SANO_R5_PRIM_DETERMINANT_DESCENT_SOURCE_AUDIT.md`.

That audit admits Castella–Sano 2026 only as a proof/dependency architecture. Its relevant
theorems remain stated for odd primes / `p>3`; this package does not cite them as literal-`2`
mathematical premises.

## What is replayed internally

Two source dependencies are discharged from already-protected MATHSOLVE results rather than by
prime-range specialization.

First, the structure separation is replayed in the exact cyclotomic coefficient ring. Protected
R5-LIFT gives compatible isomorphisms

`D_{m,n} -> SS_1(T_{m,n}) -> KS_1(T_{m,n})`

over `R_{m,n}=Z/2^m[Gamma_n]`. Their inverse limit gives the cyclotomic Kolyvagin line over
`Lambda=Z_2[[Gamma]]`; localization at `q=(2)` identifies its scalar coordinate with the
determinant coordinate. WP60A-A1 then gives

`v_q(a)=length(H^2(C_q))+M_q(kappa^Kato)`.

This is the literal-`2` structural separation needed for R5-PRIM.

Second, auxiliary-prime rigidity is replayed from the R5-LIFT/WP60R finite-level package:
connected core graphs, finite-singular edge isomorphisms, fresh-prime pairwise localization and
iterative dual killing preserve and expose the same `2`-divisibility through arbitrarily deep
selected auxiliary sets.

Protected WP60T supplies the Kato derivative and first-component compatibility. Protected
R5-LIFT supplies determinant membership. WP60A-A1 supplies the exact DVR
membership-versus-generator criterion.

This package deliberately does **not** identify the localized cyclotomic `Lambda_q` Kolyvagin
line with WP60S's untwisted base-level `Z_2` module. The latter remains a protected predecessor
input, not a substitute coefficient ring.

## What remains external to the protected theorem stack

No protected theorem evaluates

`M_q(kappa^Kato)`.

The provider audit identifies a `p>3` explicit-reciprocity/refined-Kurihara route to the
corresponding source-normalized index, but no protected source authorizes that route at literal
`p=2`. It is optional: a direct proof of the normalized cyclotomic height-one
Kato–Kolyvagin primitivity-index equality would also close the successor frontier.

Accordingly this operation does not request another broad literature screen. Its exact successor
question is mathematical:

`MISSING_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

Only if that direct theorem route requires a new external premise should MATHFORGE be re-entered.

## Negative facts retained

- rank-one freeness does not imply that the Kato-derived element is a basis;
- nonzero does not imply primitive over the DVR `Lambda_(2)`;
- R5-LIFT is one-sided and does not imply R5-PRIM;
- the source's `p>3` explicit reciprocity is not a literal-`2` theorem;
- the raw source normalization is not silently identified term-by-term with the protected
  literal-`2` normalization;
- no CI result, repository merge, or source audit creates mathematical certification.
