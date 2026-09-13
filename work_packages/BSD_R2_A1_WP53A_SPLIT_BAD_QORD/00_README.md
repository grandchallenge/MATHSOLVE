# BSD-R2-A1 WP53A — exact split semistable bad-prime `Q^ord` factor

## Operation

`BSD-R2-A1-WP53A-SPLIT-BAD-QORD`

## Protected predecessors

- MATHSOLVE WP52A: `3aae8375de252a782eaf82e0bb393814e033f857`.
- MATHFORGE WP53 source admission: `c1aaf027df8e03fd79783cfc8ed14c9d58632a50`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## Objective

Protected WP41B rewrites the corrected ordinary p-adic Gross–Zagier formula so that the remaining automorphic normalization is `Q^ord`. Protected WP42B computes the selected good-ordinary split-`2` local factor exactly.

WP53A computes the odd bad semistable factors on the source-compatible newvector/test-vector line without hiding measure scalars.

## Result

For every odd bad semistable `ell|N`, protected WP09 gives:

- `K/Q` split at `ell`;
- trivial toric character;
- a conductor-one special local representation, an unramified twist of Steinberg.

Protected MATHFORGE WP53 matches Disegni's local toric ratio exactly to Cai–Shu–Tian's normalized local beta functional and gives, in the CST local Haar measure,

`Q_{ell,dt_ell^CST}=1+ell^(-1)`.

Thus

`ord_2 Q_{ell,dt_ell^CST}=ord_2(ell+1)`.

Define the CST-normalized bad-prime product

`Q_bad^CST := product_{ell|N, ell odd} (1+ell^(-1))`.

Then

`ord_2 Q_bad^CST
 = sum_{ell|N, ell odd} ord_2(ell+1)`.

For a local component of Disegni's globally volume-one measure written

`dt_ell=s_ell dt_ell^CST`,

one has exactly

`Q_{ell,dt_ell}=s_ell(1+ell^(-1))`.

Hence, with

`s_bad := product_{ell|N, ell odd} s_ell`,

the actual product over odd bad local components is

`Q_bad = s_bad Q_bad^CST`.

No unit claim is made about `s_bad`.

## D2c disposition

The local bad-prime newvector problem is resolved. The surviving boundary is

`MISSING_P2_DISEGNI_GLOBAL_MEASURE_AND_AUXILIARY_QORD_RECONCILIATION`.

The remaining work is to reconcile the globally volume-one Disegni measure decomposition and any nonbad auxiliary/vector factors. WP53A does not assert that `Q^ord` has the same valuation as `Q_bad^CST`.

## Claim boundary

WP53A does not prove global `Q^ord=1`, fixed-`2` height nondegeneracy, D1c, WP00 normalization, final quadratic descent, BSD, or certification.