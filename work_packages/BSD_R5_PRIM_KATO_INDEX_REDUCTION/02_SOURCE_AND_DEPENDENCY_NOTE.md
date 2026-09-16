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
prime-range specialization:

- the Kolyvagin-system structure/Fitting separation is replayed from WP60R/WP60S plus the
  rank-one scaling argument;
- auxiliary-prime rigidity is replayed from WP60R localization, finite-singular comparison,
  iterative dual killing, and connected core graphs.

Protected WP60T supplies the selected Kato-derived system and first-component compatibility.
Protected R5-LIFT supplies determinant membership. WP60A-A1 supplies the exact DVR
membership-versus-generator criterion.

## What remains external to the protected theorem stack

The arithmetic value of the normalized Kato-system common divisibility is not determined by
those structural results.

The provider audit identifies a p>3 explicit-reciprocity/refined-Kurihara route, but no protected
source currently authorizes that route at literal `p=2`. It is optional: a direct proof of the
normalized Kato–Kolyvagin primitivity-index equality would also close the successor frontier.

Accordingly this operation does not request another broad literature screen. Its exact successor
question is mathematical:

`MISSING_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

Only if that direct theorem route requires a new external premise should MATHFORGE be re-entered.

## Negative facts retained

- rank-one freeness does not imply that the Kato-derived system is a basis;
- nonzero does not imply primitive over `Z_2`;
- R5-LIFT is one-sided and does not imply R5-PRIM;
- p>3 explicit reciprocity is not a literal-2 theorem;
- no determinant visualization, CI result, repository merge, or source audit creates
  mathematical certification.
