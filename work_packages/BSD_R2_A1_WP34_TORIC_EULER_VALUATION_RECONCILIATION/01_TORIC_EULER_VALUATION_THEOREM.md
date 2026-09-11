# WP34 theorem — the odd-bad toric surplus is exactly the S-truncation valuation shift

## 1. Setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. The conductor is odd and the curve is semistable.

For every bad prime `ell|N`, put

`a_ell=+1`

for split multiplicative reduction and

`a_ell=-1`

for nonsplit multiplicative reduction, and define

`tau_ell := v2(ell-a_ell)`.

Set

`tau_bad(E) := sum_{ell|N} tau_ell`.

Protected WP33 defines

`D_bad^BM := direct_sum_{ell|N} E(Q_ell)^wedge_2`

and proves

`len_Z2 D_bad^BM
 = tau_bad(E) + sum_{ell|N} v2(c_ell)`.

Protected WP22 defines the total odd-bad ambient local-control module `K_bad` and proves

`len_Z2 K_bad^vee
 = sum_{ell|N} v2(c_ell)`.

Protected MATHFORGE commit

`075b91647c22e12aeb0888496966da162db1d771`

admits the Burns–Macias Castillo literal-`p=2` source interfaces used below.

## 2. The algebraic comparison shift

Burns–Macias Castillo equation (20) places the nonarchimedean finite point-completion module between the classical degree-one term and the perfect-complex degree-two term.

For the selected `Q`, `p=2` specialization:

- choose the full allowed local module at `2`, so the source quotient `E(Q_2)^wedge_2/X` is zero;
- protected WP32 shows that the real-place degree-one and degree-two correction groups have equal `Z_2`-length and therefore zero net determinant valuation.

Thus the remaining odd-bad finite comparison module is exactly `D_bad^BM`.

### Lemma `BSD-A1-WP34-ALG-SHIFT-001`

For a finite exact sequence of `Z_2`-modules of the equation-(20) shape

`0 -> A_1 -> B_1 -> D -> A_2 -> B_2 -> 0`,

one has

`(-len A_1 + len A_2)
 - (-len B_1 + len B_2)
 = len D`

whenever the displayed finite lengths are defined.

### Proof

Exactness gives

`len A_1 - len B_1 + len D - len A_2 + len B_2 = 0`.

Rearranging gives the claimed identity. QED.

The same equality is the valuation statement for the corresponding fractional Fitting/determinant ideals. Applying it to the finite correction part of equation (20) and using WP32 gives an odd-bad algebraic comparison shift

`lambda_bad^alg
 := len_Z2 D_bad^BM
 = tau_bad(E) + sum_{ell|N}v2(c_ell)`.

No claim is made here that the full degree-one or degree-two arithmetic modules themselves are finite; only the finite comparison cone is measured.

## 3. Exact analytic S-truncation shift

The admitted source defines `L_S(E,s)` by deleting the Euler factors at the places in `S`.

To isolate only the odd-bad contribution, fix two source-compatible truncation sets `S0 subset S` that agree at every place except that

`S minus S0 = {ell : ell|N}`.

Thus all choices at `2`, infinity, and every good finite place cancel from the ratio.

For multiplicative reduction,

`L_ell(E,s)=(1-a_ell ell^(-s))^(-1)`.

Hence

`L_S(E,s)/L_{S0}(E,s)
 = product_{ell|N}(1-a_ell ell^(-s))`.

Every factor is nonzero at `s=1`, so the two truncated L-functions have the same order of vanishing there and their leading-term ratio is the rational number

`L_S^*/L_{S0}^*
 = product_{ell|N}(1-a_ell/ell)`.

Define the odd-bad analytic truncation shift by

`lambda_bad^an
 := v2(L_S^*/L_{S0}^*)`.

This is well-defined because the displayed ratio lies in `Q^x`. No individual `2`-adic valuation is assigned to either unnormalized real leading term.

### Lemma `BSD-A1-WP34-AN-SHIFT-001`

One has

`lambda_bad^an = tau_bad(E)`.

### Proof

For each odd `ell`, the denominator `ell` is a `2`-adic unit. Therefore

`v2(1-a_ell/ell)
 = v2(ell-a_ell)
 = tau_ell`.

Taking the valuation of the rational product proves the result. QED.

## 4. Toric reconciliation

### Theorem `BSD-A1-WP34-TORIC-RECONCILIATION-001`

The difference between the odd-bad algebraic finite-comparison shift and the odd-bad analytic S-truncation shift is exactly the protected Tamagawa/control length:

`lambda_bad^alg - lambda_bad^an
 = sum_{ell|N} v2(c_ell)`.

Equivalently,

`len_Z2 D_bad^BM
 - v2(L_S^*/L_{S0}^*)
 = len_Z2 K_bad^vee`.

### Proof

Protected WP33 gives

`len_Z2 D_bad^BM
 = tau_bad(E)+sum_{ell|N}v2(c_ell)`.

The preceding analytic lemma gives

`lambda_bad^an=tau_bad(E)`.

Subtract. Protected WP22 identifies the remaining sum with `len_Z2 K_bad^vee`. QED.

## 5. Fitting-ideal form

Define the analytic valuation ideal

`J_bad^an := 2^lambda_bad^an Z_2
          = 2^tau_bad(E) Z_2`.

This notation records only a principal ideal determined by the valuation of the rational leading-term ratio. It is not a chosen determinant generator.

### Corollary `BSD-A1-WP34-FITTING-001`

One has the exact principal-ideal identity

`Fitt^0_Z2(D_bad^BM)
 = J_bad^an * Fitt^0_Z2(K_bad^vee)`.

### Proof

Protected WP33 gives

`Fitt^0_Z2(D_bad^BM)
 = 2^(tau_bad(E)+sum v2(c_ell)) Z_2`.

Protected WP22 gives

`Fitt^0_Z2(K_bad^vee)
 = 2^(sum v2(c_ell)) Z_2`.

Factor the first power of `2` and use `lambda_bad^an=tau_bad(E)`. QED.

Thus the toric factor in the Burns–Macias finite point-completion term is exactly the valuation ideal introduced by deleting the same multiplicative Euler factors from the analytic L-series.

## 6. Why the source's Section 6 theorem is not used

The admitted MATHFORGE audit records that Burns–Macias Castillo Section 6 begins by fixing an odd prime `p`. Their Theorem 6.5 therefore cannot be specialized to the present literal-`p=2` campaign.

WP34 does not use it.

The present result instead combines only:

1. the literal-p=2 equation-(20) comparison orientation;
2. the literal source definition of S-truncation;
3. protected WP32's real-place valuation cancellation;
4. protected WP33's exact odd-bad point-completion length;
5. protected WP22's exact Tamagawa/control length;
6. elementary additivity of lengths and valuations.

Accordingly, WP34 is strictly a valuation/Fitting theorem.

## 7. Boundary closed and stronger boundary retained

WP33 left

`MISSING_P2_BURNS_MACIAS_TORIC_EULER_FACTOR_RECONCILIATION`.

WP34 closes this boundary at the exact valuation/Fitting-ideal level.

It does **not** establish a canonical isomorphism of determinant lines or equality of determinant generators. If such a comparison is needed downstream, its remaining form is

`MISSING_P2_BURNS_MACIAS_CANONICAL_DETERMINANT_LINE_COMPARISON`.

That stronger generator-level issue is not substituted for the existing canonical campaign obligations. In particular D1a, D1c, and D2 remain controlling boundaries.

## 8. Relation to the protected BSD normalization

The protected analytic defect is

`delta_2(E)
 = v2(L'(E,1)/(Omega_E Reg_E))
   - sum_{ell|N}v2(c_ell)`.

WP34 explains why the extra toric lengths appearing in the Burns–Macias `S`-truncated perfect-complex comparison do not create an additional odd-bad valuation term beyond the protected Tamagawa normalization: the rational ratio between the two source-compatible truncations has valuation `tau_bad(E)`, exactly matching the toric part of the finite comparison module.

This statement does not prove the remaining global determinant, height-one `(2)`, or Bockstein/regulator identities needed to identify the full protected normalized analytic quantity with `v2(Fitt^1_Z2(X_E))`.

## 9. Claim firewall

WP34 does not prove:

- Burns–Macias Castillo Theorem 6.5 at `p=2`;
- validity of their refined BSD conjecture;
- a canonical determinant-line or determinant-generator equality;
- exact identification of the perfect-complex degree-two module with protected `X_E`;
- a primitive cyclotomic perfect determinant realization;
- a height-one `(2)` analytic determinant generator;
- the WP20 Bockstein/WP00 normalization;
- the WP31 finite twisted-reciprocity exponent;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.
