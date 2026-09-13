# WP50A theorem — intrinsic strict-H2 realization of the WP40 defect

## Setup

Retain protected WP48A and WP49A. Put

`B_str := C_str,0`, `C_Kum := C_Kum,0`,

and

`Q_fin := Cone(B_str -> C_Kum)`.

Protected WP48A proves

`Q_fin ~= V_K[-1]`,

`0 -> R_K -> V_K --v_Z--> Zloc -> 0`,

where `Zloc:=Z_{2,K}^loc`, and

`im(H^1(C_Kum) -> V_K)=J_K subset R_K`.

Protected WP49A fixes

`pi_Z:H^2(B_str) -> Zloc`.

No new external theorem premise is used.

## 1. Degree-two comparison kernel

The triangle

`B_str -> C_Kum -> Q_fin -> B_str[1]`

gives

`H^1(C_Kum) -> V_K --d_fin--> H^2(B_str) -> H^2(C_Kum) -> 0`,

because `H^2(Q_fin)=0`.

Since the image of `H^1(C_Kum)` in `V_K` is exactly `J_K`, exactness gives:

### Theorem `BSD-A1-WP50A-H2-KERNEL-001`

`d_fin` induces a canonical isomorphism

`bar_d_fin: V_K/J_K
 ~= ker(H^2(B_str) -> H^2(C_Kum))`.

## 2. Compatibility with the ordinary higher term

The WP48A octahedron also gives

`v_Z:V_K -> Zloc = H^2(Q_aug)`.

The same octahedral diagram contains

`B_str -> Q_aug`,

whose degree-two map is `pi_Z`.

With the signed distinguished-triangle convention already used in WP48A/WP49A, naturality gives the exactly commuting square

`V_K --d_fin--> H^2(B_str)`

` |v_Z              |pi_Z`

` v                 v`

`Zloc -----id----> Zloc`.

Thus:

### Lemma `BSD-A1-WP50A-H2-Z-COMPAT-002`

`v_Z = pi_Z o d_fin`.

Changing to the other standard triangle sign changes the two connecting maps simultaneously. The kernel theorem below is therefore sign-independent; no unspecified `2`-adic unit is introduced.

## 3. Strict-H2 silent kernel

Define

`K_K^sil
 := ker(
      H^2(B_str)
      -> H^2(C_Kum) direct_sum Zloc
    )`.

Equivalently,

`K_K^sil
 = ker(H^2(B_str)->H^2(C_Kum))
   intersect ker(pi_Z)`.

The word `silent` means only that the class is invisible both to the finite Kummer degree-two target and to the ordinary local higher-cohomology projection. It does not mean the class vanishes.

### Theorem `BSD-A1-WP50A-SILENT-KERNEL-003`

There is a canonical isomorphism

`R_K/J_K ~= K_K^sil`.

### Proof

Because `R_K=ker(v_Z)` and `J_K subset R_K`,

`R_K/J_K = ker(V_K/J_K -> Zloc)`.

Theorem `H2-KERNEL-001` identifies `V_K/J_K` with

`ker(H^2(B_str)->H^2(C_Kum))`.

Lemma `H2-Z-COMPAT-002` identifies the induced map to `Zloc` with the restriction of `pi_Z`. Its kernel is therefore exactly `K_K^sil`. QED.

## 4. Exact WP40 defect

Protected WP40 gives a perfect pairing

`R_K x R_K^dual -> Q_2/Z_2`

and

`D_K=ann(J_K)`.

Hence

`D_K ~= (R_K/J_K)^vee`.

Combining with Theorem `SILENT-KERNEL-003` gives:

### Theorem `BSD-A1-WP50A-DK-H2-004`

`D_K ~= (K_K^sil)^vee`,

or equivalently

`D_K^vee ~= K_K^sil`.

This is map-level and integral. It does not use an equality of lengths.

## 5. Reconciliation with WP49A

WP49A proved

`D_K^vee
 ~= U_K^aug / ((Zloc tensor t_cyc)+C_K^ctrl)`.

Therefore WP50A canonically identifies

`U_K^aug / ((Zloc tensor t_cyc)+C_K^ctrl)
 ~= K_K^sil`.

The full control image is no longer an independent missing datum for locating `D_K`.

## 6. Relation to the strict Bockstein

Protected WP49A proves

`lambda_K
 = beta_Q^{-1} o (pi_Z tensor 1) o beta_str`.

WP50A places the dual WP40 defect in

`K_K^sil subset ker(pi_Z) subset H^2(B_str)`.

Thus the visible local tangent component and the finite WP40 defect are now located on the same strict degree-two cohomology surface. WP50A does not identify `K_K^sil` with an image, cokernel, radical, or orthogonal complement of the Bockstein/height pairing.

## 7. Refined boundary

WP49A left

`MISSING_P2_GLOBAL_KUMMER_CONTROL_IMAGE_TO_STRICT_BOCKSTEIN_DUALITY`.

WP50A replaces it by the narrower boundary

`MISSING_P2_STRICT_H2_SILENT_KERNEL_TO_BOCKSTEIN_HEIGHT_DUALITY`.

A successor must determine, at literal integral `p=2`, how

`K_K^sil subset H^2(C_str,0)`

sits under Nekovar Selmer duality and the strict cyclotomic Bockstein/height pairing. Equal lengths are insufficient.

## Claim firewall

WP50A does not prove `K_K^sil=0`, `D_K=0`, `J_K=R_K`, fixed-`2` height nondegeneracy, a pure Bockstein formula for `D_K`, D1c, remaining Disegni normalization, WP00 normalization, final quadratic descent, `BSD-R2-A1`, or MATHCERT certification/novelty/priority.
