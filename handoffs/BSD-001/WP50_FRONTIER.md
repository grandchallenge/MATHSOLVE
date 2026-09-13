# BSD-001 frontier after WP50A

## Protected predecessor

- MATHSOLVE WP49A protected merge: `b62a1467608a7069f16efdce2f0375d0ab566299`.
- MATHFORGE protected source state: `79f7c88cf4e59886902c2f12d29d7c73afced379`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## WP50A result

Let

`B_str:=C_str,0`, `C_Kum:=C_Kum,0`,

and let

`pi_Z:H^2(B_str)->Zloc`

be the protected ordinary higher-term projection.

Define

`K_K^sil
 := ker(
      H^2(B_str)
      -> H^2(C_Kum) direct_sum Zloc
    )`.

The finite comparison triangle and the WP48A octahedron give canonically

`V_K/J_K ~= ker(H^2(B_str)->H^2(C_Kum))`,

and the induced map to `Zloc` is exactly `pi_Z`. Therefore

`R_K/J_K ~= K_K^sil`.

Protected WP40 then gives

`D_K ~= (K_K^sil)^vee`.

This eliminates the full Kummer-control image `C_K^ctrl` as an independent missing datum for locating `D_K`.

## Live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2b: `MISSING_P2_STRICT_H2_SILENT_KERNEL_TO_BOCKSTEIN_HEIGHT_DUALITY`.
- D2c: `MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.
- D2d: `MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successor WP51A

Use the literal-`p=2` Nekovar Selmer duality already protected in the campaign to determine the exact dual description of

`K_K^sil subset H^2(C_str,0)`.

Then compare that dual subquotient with the strict cyclotomic Bockstein/height pairing. The desired output is a map-level statement deciding whether `K_K^sil` is the height radical, the dual of a quotient by the Bockstein image, or a different exact Selmer-duality submodule.

Do not assume fixed-`2` height nondegeneracy and do not infer an identification from equal lengths.

## Parallel successor WP51B

Continue the split semistable bad-prime/newvector `Q^ord` normalization lane. Retain Haar measure, local L-factors, denominator pairing, Tamagawa-sensitive scalars, and all powers of `2` exactly.

## Firewall

WP50A does not prove `K_K^sil=0`, `D_K=0`, `J_K=R_K`, fixed-`2` height nondegeneracy, D1c, global `Q^ord=1`, WP00 normalization, final quadratic descent, BSD, or certification.
