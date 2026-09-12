# WP43A theorem — source-qualified strict Greenberg augmentation/Bockstein compatibility

## 1. Protected objects

Let `T=T_2(E)` over the protected auxiliary imaginary quadratic field `K`, and let

`C_str`

be the strict Greenberg/Nekovář Selmer complex used in protected WP37–WP40.

Protected WP37 supplies the cyclotomic first Bockstein and height at literal `p=2` over totally imaginary `K`.

Protected MATHFORGE WP43A supplies the missing formal compatibility statement from Nekovář §0.16.

## 2. Exact first-order strict triangle

Let `J` be the cyclotomic augmentation ideal and let `t_cyc` denote the rank-one tangent direction represented source-theoretically by `J/J^2`.

### Theorem `BSD-A1-WP43A-STRICT-AUG-001`

The first-order cyclotomic augmentation triangle induces an exact triangle of strict Greenberg Selmer complexes whose specialized connecting morphism is the WP37 first cyclotomic Bockstein

`beta_str : H~^1_f(K,T) -> H~^2_f(K,T) tensor t_cyc`.

### Proof

Protected MATHFORGE WP43A admits Nekovář Introduction §0.16 / (0.16.0.1): Greenberg local conditions induced on the terms of the first-order augmentation triangle are compatible and their Selmer complexes form the corresponding exact triangle. The source defines the connecting morphism of the specialized Selmer complex to be the Bockstein entering the generalized height pairing.

Protected WP37 has already verified that this formalism is literal at `p=2` over the totally imaginary field `K`. Therefore the source triangle applies to the selected strict complex and its connecting morphism is exactly `beta_str`. QED.

## 3. Consequence for the WP41A separation

Protected WP41A correctly observed that two operations had not yet been linked:

- cyclotomic augmentation of the strict complex;
- fixed-level enlargement of local conditions from strict Greenberg to classical Kummer.

Theorem `STRICT-AUG-001` closes the first operation completely. It proves that no additional theorem is needed merely to make the strict Greenberg Bockstein natural under cyclotomic augmentation.

The second operation remains separate.

## 4. Exact remaining compatibility datum

Protected WP39–WP40 use the finite fixed-level quotient

`R_K = U_Kum/U_str`

and its dual global hit `D_K`.

To compare `D_K` with the Bockstein triangle, one still needs all of:

1. an integral cyclotomic classical-Kummer local-condition/Selmer object `C_Kum,infty` over `K`;
2. a morphism
   `C_str,infty -> C_Kum,infty`;
3. a comparison cone `Q_infty`;
4. derived augmentation identifying the specialized cone with the exact fixed-level strict/Kummer quotient of WP39–WP40;
5. compatibility of the resulting comparison triangle with the already-qualified strict augmentation triangle.

None of these classical-Kummer Iwasawa objects is supplied by WP43A.

### Corollary `BSD-A1-WP43A-BOUNDARY-002`

The live D2b compatibility boundary is precisely

`MISSING_P2_KUMMER_IWASAWA_LOCAL_CONDITION_COMPLEX_AND_SPECIALIZATION_OVER_K`.

The earlier broader label

`MISSING_P2_IWASAWA_STRICT_KUMMER_BOCKSTEIN_COMPATIBILITY_OVER_K`

is no longer minimal because its strict-Greenberg augmentation half is now protected.

## 5. What would close the bridge

A sufficient successor theorem would give an integral Iwasawa-level Kummer comparison triangle

`C_str,infty -> C_Kum,infty -> Q_infty -> C_str,infty[1]`

and prove

`Q_infty tensor^L_{Lambda_K} Z_2`

recovers the WP39 local-condition quotient with no hidden finite or `2`-power discrepancy.

Naturality with the source-qualified strict Bockstein triangle could then be used to test whether WP40's `D_K` is an explicit Bockstein subquotient.

A comparison after tensoring with `Q_2`, after inverting the augmentation parameter, or only up to finite error is not sufficient: the missing datum is itself an exact finite `2`-primary defect.

## 6. Claim firewall

WP43A does not prove:

- existence of `C_Kum,infty`;
- exact derived augmentation for a Kummer comparison cone;
- `D_K` equals a Bockstein image, kernel, cokernel, or height radical;
- `D_K=0` or `J_K=R_K`;
- fixed-`2` height nondegeneracy;
- D1c, D2c–D2e;
- `BSD-R2-A1`;
- MATHCERT certification.