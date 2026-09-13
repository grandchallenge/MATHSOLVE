# WP53A theorem — exact odd semistable split-torus factor in `Q^ord`

## 1. Protected setup

Retain protected WP09, WP33, WP41B, WP42B, WP52A, and protected MATHFORGE WP53.

For each odd bad semistable prime `ell|N`, write

`F_ell := Q_ell`.

The selected auxiliary imaginary quadratic field satisfies

`K tensor Q_ell ~= Q_ell direct_sum Q_ell`.

The local toric character is trivial. The local GL2 representation attached to the selected elliptic curve has conductor exponent one and is an unramified twist of Steinberg.

Let `dt_ell^CST` denote the Cai–Shu–Tian quotient Haar measure admitted by protected MATHFORGE WP53.

## 2. Exact local factor

### Theorem `BSD-A1-WP53A-LOCAL-QORD-001`

On the source-compatible one-dimensional conductor-one test-vector line,

`Q_{ell,dt_ell^CST}
 = 1+ell^(-1)`.

Consequently

`ord_2 Q_{ell,dt_ell^CST}
 = ord_2(ell+1)`.

### Proof

Protected MATHFORGE WP53 matches Disegni's finite local toric ratio exactly with the Cai–Shu–Tian normalized beta functional for the same local Haar measure.

On the selected local branch:

- conductor exponent `n=1`;
- toric conductor `c=0`;
- the quadratic algebra is split;
- the representation is an unramified Steinberg twist, so the CST correction exponent is zero;
- for `F=Q_ell`, the base different and split relative-discriminant factors have absolute value one.

CST Proposition 3.12 therefore gives

`Q_{ell,dt_ell^CST}
 = L(1,1_F)/L(2,1_F)`.

Now

`L(1,1_F)=(1-ell^(-1))^(-1)`

and

`L(2,1_F)=(1-ell^(-2))^(-1)`.

Their ratio is

`(1-ell^(-2))/(1-ell^(-1))
 = 1+ell^(-1)`.

Since `ell` is odd, its denominator is a `2`-adic unit, so

`ord_2(1+ell^(-1))=ord_2(ell+1)`.

QED.

## 3. Independence from split/nonsplit multiplicative type over `Q_ell`

The terms “split torus” and “split multiplicative reduction” refer to different structures here.

The torus is split because the auxiliary quadratic algebra is

`K_ell ~= Q_ell direct_sum Q_ell`.

The elliptic curve itself may have split or nonsplit multiplicative reduction at `ell`. This changes the unramified Steinberg twist. The CST conductor-one formula above depends only on the branch `n=1`, `c=0`, split torus and zero correction exponent. Therefore the normalized value remains

`1+ell^(-1)`

for either multiplicative type in the selected semistable class.

No statement about Tamagawa numbers follows from this independence.

## 4. Product over all odd bad primes

Define

`Q_bad^CST
 := product_{ell|N, ell odd}
      Q_{ell,dt_ell^CST}`.

### Corollary `BSD-A1-WP53A-BAD-PRODUCT-001`

One has exactly

`Q_bad^CST
 = product_{ell|N, ell odd} (1+ell^(-1))`

and

`ord_2 Q_bad^CST
 = sum_{ell|N, ell odd} ord_2(ell+1)`.

This product is an exact source-normalized finite local product. It is not yet the complete `Q^ord`.

## 5. Transport to Disegni's global volume-one decomposition

Disegni fixes an adelic torus measure of total quotient volume one and then chooses local components. The local decomposition has scalar freedom whose product is constrained by the global normalization.

For each odd bad `ell`, write the actual chosen local component as

`dt_ell = s_ell dt_ell^CST`.

Linearity of the local toric integral gives:

### Theorem `BSD-A1-WP53A-MEASURE-TRANSPORT-001`

`Q_{ell,dt_ell}
 = s_ell(1+ell^(-1))`.

Putting

`s_bad:=product_{ell|N, ell odd} s_ell`,

one obtains

`Q_bad
 = s_bad Q_bad^CST`.

At the valuation level, whenever the selected embedding into the `2`-adic coefficient field is fixed,

`ord_2 Q_bad
 = ord_2(s_bad)
   + sum_{ell|N, ell odd} ord_2(ell+1)`.

The term `ord_2(s_bad)` is retained. It is not declared zero.

## 6. Relation to the protected WP34 valuation reconciliation

Protected WP34 concerns a different normalization comparison: odd bad-prime finite point-completion terms versus deleting Euler factors in an `S`-truncated complex. It produces the residual Tamagawa valuation in that determinant/Fitting comparison.

WP53A evaluates Disegni's toric newvector factor. The quantities

`ord_2(ell+1)`

and the WP34 terms involving

`ord_2(ell-a_ell)` and ord_2(c_ell)

must not be identified or cancelled merely because they occur at the same prime.

Any cancellation or recombination in the final BSD normalization must be proved after both expressions are transported into one common measure, period, test-vector, and determinant convention.

## 7. D2c reduction

The prior boundary

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`

is closed by Theorem `LOCAL-QORD-001`.

The remaining D2c boundary is

`MISSING_P2_DISEGNI_GLOBAL_MEASURE_AND_AUXILIARY_QORD_RECONCILIATION`.

A successor must account exactly for:

1. the local rescaling factors used to realize Disegni's global volume-one measure;
2. all nonbad finite factors in `Sigma` and `Sigma'` that survive in the chosen packet;
3. the away-from-`S p infinity` vector ratio;
4. the archimedean/global normalization left after the protected ordinary `p`-factor is removed;
5. every resulting power of `2`.

## 8. Surviving campaign boundaries

After WP53A:

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`;
- D2b: `RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`;
- D2c: `MISSING_P2_DISEGNI_GLOBAL_MEASURE_AND_AUXILIARY_QORD_RECONCILIATION`;
- D2d: `MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`;
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## 9. Claim firewall

WP53A does not prove:

- `s_ell` or `s_bad` is a `2`-adic unit;
- global `Q^ord=1`;
- `ord_2 Q^ord = sum ord_2(ell+1)`;
- cancellation with Tamagawa, Euler, period, or determinant factors;
- fixed-`2` height nondegeneracy;
- D1c;
- WP00 normalization;
- final quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
