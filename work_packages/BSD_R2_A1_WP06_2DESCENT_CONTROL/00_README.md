# BSD-R2-A1-WP06 — Exact integral quadratic 2-descent control

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP06-2DESCENT-CONTROL`.
- Native owner: `grandchallenge/MATHSOLVE#138`.
- Parent: `BSD-R2-A1-WP05-SOURCE-INTERFACE-001`.
- Protected baseline: `5aa47e09266e34f855058da7227f2e212cfc2f72`.
- Claim boundary: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Primary type: restricted theorem / exact algebraic control.

## Result

This package discharges the named `BSD-R2-A1-2DESCENT-CONTROL` obstruction.

Let `E/Q` have irreducible `E[2]`, let `K/Q` be quadratic with character `chi`, let `E^d` be the corresponding quadratic twist, and let

`S_n(F) = Sel_{2^n}(E/F)`.

For every `n >= 1`, restriction gives exact control of the plus and minus eigenspaces over `K`, with finite local descent defects that are killed by `2`. The failure of the full integral decomposition is retained in two further exponent-2 groups rather than erased by dividing by `2`.

With the notation defined in this package,

`len_Z2 Sel_{2^n}(E/K)`

`= len_Z2 Sel_{2^n}(E/Q) + len_Z2 Sel_{2^n}(E^d/Q)`

`  + dim_F2 D_n^+ + dim_F2 D_n^- - dim_F2 I_n + dim_F2 Q_n.`

Every correction term is explicitly defined. No factor of `2` is declared a unit.

If the three relevant 2-primary Tate-Shafarevich groups are finite, then for all sufficiently large `n` the rank terms cancel and the same correction gives an exact identity among their `Z_2`-lengths.

## Local-at-2 boundary

For good ordinary reduction at `2`, this package defines the ordinary local condition from the connected-etale sequence of the actual 2-divisible group. If an auxiliary quadratic field is chosen with `2N` split, the local descent defect at `2` and at every bad prime is exactly zero because the local extension is split, not because a power of `2` was discarded.

## What remains open

This package does not prove an integral 2-adic main conjecture, explicit reciprocity law, p-adic Gross-Zagier formula, exact height comparison, or `BSD-R2-A1`. The next obstruction is the integral 2-primary reciprocity/length bridge.