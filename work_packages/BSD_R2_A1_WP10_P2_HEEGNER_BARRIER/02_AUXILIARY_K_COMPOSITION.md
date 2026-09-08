# Exact auxiliary-`K` composition debt

## Protected inputs

WP09 supplies an imaginary quadratic field `K=Q(sqrt(D))` such that:

- `D` is fundamental and `(D,2N)=1`;
- `2` and every `ell|N` split in `K`;
- `L(E^D,1) != 0`;
- `ord_{s=1} L(E/K,s)=1`.

The protected low-rank Gross-Zagier/Kolyvagin interface applied to `E^D/Q` therefore gives algebraic rank zero and finite `Sha(E^D/Q)`. It does not determine the exact 2-primary length of that finite group.

WP06 supplies, for sufficiently large `n`, the exact 2-primary descent identity

`len_Z2 Sha(E/K)[2^infinity]`

`= len_Z2 Sha(E/Q)[2^infinity]`

`  + len_Z2 Sha(E^D/Q)[2^infinity]`

`  + dim_F2 D_n^+ + dim_F2 D_n^- - dim_F2 I_n + dim_F2 Q_n.`

No omitted unit or hidden power of `2` occurs in this identity.

## Proposition `BSD-A1-HB002`

An exact 2-primary Heegner-index/Sha theorem over the WP09 auxiliary field `K` is not, by itself, sufficient to prove `BSD-R2-A1` over `Q`.

**Status:** `PROVED_IN_PACKAGE`.

### Proof

Assume a future theorem determines

`len_Z2 Sha(E/K)[2^infinity]`

exactly from a Heegner index or equivalent arithmetic object.

The protected WP06 identity then determines only the sum

`len_Z2 Sha(E/Q)[2^infinity] + len_Z2 Sha(E^D/Q)[2^infinity]`

up to the explicit, already-recorded finite defect term

`dim D_n^+ + dim D_n^- - dim I_n + dim Q_n`.

Therefore isolating `len_Z2 Sha(E/Q)[2^infinity]` requires, in addition, an exact determination of the rank-zero twist contribution

`len_Z2 Sha(E^D/Q)[2^infinity]`

and the explicit defect groups that do not vanish by the split-local theorem.

The all-split condition does force the local defect groups at `2` and every `ell|N` to vanish. It does not imply that every remaining nonsplit-place defect, `I_n`, or `Q_n` vanishes.

Hence the `K`-side index theorem alone cannot isolate the selected `Q`-side target. QED.

## Analytic counterpart

The same extra twist factor appears before the arithmetic descent.

Quadratic base change gives

`L(E/K,s) = L(E,s)L(E^D,s)`.

Since the selected curve has `L(E,1)=0` and the auxiliary twist has `L(E^D,1) != 0`, differentiation at `s=1` gives

`L'(E/K,1) = L'(E,1)L(E^D,1)`.

Thus a complex Gross-Zagier identity over `K` must still be divided by the exact rank-zero twist special value to recover the `Q`-side derivative. At `p=2`, the 2-adic valuation of that factor cannot be discarded as a unit without an exact theorem in the protected period/Tamagawa normalization.

## Direct-lane debt after WP10

A complete auxiliary-field direct proof must therefore supply all of:

1. an exact integral p=2 Heegner/Kolyvagin index theorem over `K` or equivalent sharp arithmetic-length theorem;
2. the exact 2-primary rank-zero twist contribution for `E^D/Q` in compatible normalization;
3. exact evaluation of the surviving WP06 descent defects;
4. a fully normalized complex Gross-Zagier/special-value comparison carrying the WP00 real period, regulator, Tamagawa, torsion, isogeny, Manin, and local correction ledger;
5. an exact cancellation/composition proving the selected `Q`-side valuation and nothing stronger.

A direct theorem over `Q` that computes the target arithmetic length may bypass items 1-3 and is therefore the parsimonious preferred route if such a theorem can be proved.
