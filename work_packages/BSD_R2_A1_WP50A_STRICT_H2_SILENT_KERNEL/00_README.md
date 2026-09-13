# BSD-R2-A1 WP50A — intrinsic strict-H2 description of the WP40 defect

## Operation

`BSD-R2-A1-WP50A-STRICT-H2-SILENT-KERNEL`

## Protected predecessor

- MATHSOLVE: `b62a1467608a7069f16efdce2f0375d0ab566299` (WP49A protected merge).
- MATHFORGE: `79f7c88cf4e59886902c2f12d29d7c73afced379`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

No new external theorem premise is used.

## Objective

WP49A expresses the protected WP40 defect as

`D_K^vee ~= U_K^aug / ((Zloc tensor t_cyc)+C_K^ctrl)`.

That formula is exact, but it still names the full global Kummer-control image `C_K^ctrl`.

WP50A asks whether the already-protected finite comparison triangle eliminates this auxiliary image and identifies `D_K^vee` directly inside strict degree-two Selmer cohomology.

## Result

Let

`B_str := C_str,0`,

`C_Kum := C_Kum,0`,

and let

`pi_Z:H^2(B_str) -> Zloc`

be the protected WP49A/WP48A ordinary local projection.

Define the strict degree-two silent kernel

`K_K^sil
 := ker(
      H^2(B_str)
      -> H^2(C_Kum) direct_sum Zloc
    )`.

WP50A proves canonically

`R_K/J_K ~= K_K^sil`

and therefore, using protected WP40 perfect local Tate duality,

`D_K ~= (K_K^sil)^vee`.

Thus D2b no longer requires an independent characterization of `C_K^ctrl`.

## Surviving boundary

The remaining question is not the location of `D_K`; it is how the finite strict-H2 submodule `K_K^sil` relates to the cyclotomic Bockstein/height pairing.

New narrow boundary:

`MISSING_P2_STRICT_H2_SILENT_KERNEL_TO_BOCKSTEIN_HEIGHT_DUALITY`.

WP50A does not prove height nondegeneracy, `D_K=0`, BSD, the height-one `(2)` analytic determinant theorem, remaining Disegni normalization, WP00 normalization, final quadratic descent, or certification.
