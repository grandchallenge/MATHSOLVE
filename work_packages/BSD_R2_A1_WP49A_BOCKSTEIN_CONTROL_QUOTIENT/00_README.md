# BSD-R2-A1 WP49A — localized Bockstein and global Kummer-control quotient

## State

`PROVED_BOUNDED_BOCKSTEIN_CONTROL_SEPARATION`

## Protected inputs

- MATHSOLVE WP48A: `05a45bd103d33ee828df9f3ff6050a895635a6d7`.
- MATHFORGE provider/source state: `79f7c88cf4e59886902c2f12d29d7c73afced379`.
- WP37/WP43A: literal-`p=2` strict cyclotomic Bockstein and its first-order augmentation naturality.
- WP39/WP40: finite strict/Kummer quotient `R_K`, actual global hit `J_K`, and `D_K=ann(J_K)`.
- WP48A: global reverse comparison cone and exact specialization octahedron.

The newly protected MATHFORGE WP49 source audit records that Macias Castillo–Sano 2026 assumes `p` odd throughout. It is a structural comparator only and is not used as literal-`p=2` authority below.

## Result

Let

`lambda_K:H^1(C_str,0) -> Z_{2,K}^loc tensor t_cyc`

be the comparison boundary from the WP48A augmented reverse-comparison triangle.

WP49A proves by naturality of the Bockstein construction that `lambda_K` is exactly the projection of the protected strict Bockstein

`beta_str:H^1(C_str,0) -> H^2(C_str,0) tensor t_cyc`

to the ordinary local higher-cohomology term. The Bockstein on the comparison cone is the canonical identification between its augmentation `Tor_1` and specialization copies, so no hidden unit or power of `2` enters this equality.

Define the global Kummer-control image

`C_K^ctrl := im(delta_Kum:S_2(E/K) -> U_K^aug)`

from the WP48A Kummer augmentation triangle.

Then

`C_K^ctrl intersect (Z_{2,K}^loc tensor t_cyc)
 = im(lambda_K)`

inside `U_K^aug`, and the quotient map to

`R_K = U_K^aug/(Z_{2,K}^loc tensor t_cyc)`

gives the exact sequence

`0 -> im(lambda_K)
   -> C_K^ctrl
   -> J_K
   -> 0`.

Consequently

`R_K/J_K
 ~= U_K^aug / ((Z_{2,K}^loc tensor t_cyc)+C_K^ctrl)`.

Protected WP40 therefore gives canonically

`D_K
 ~= (U_K^aug / ((Z_{2,K}^loc tensor t_cyc)+C_K^ctrl))^vee`.

This proves that `D_K` is not formally determined by `beta_str` alone. The localized Bockstein determines the intersection of the global Kummer-control image with the local tangent defect; the complementary quotient also depends on the full global Kummer-control image `C_K^ctrl`.

## Refined boundary

The previous request to identify `D_K` with an unspecified strict-Bockstein subquotient is too coarse. The exact missing datum is now

`MISSING_P2_GLOBAL_KUMMER_CONTROL_IMAGE_TO_STRICT_BOCKSTEIN_DUALITY`.

A successor must characterize the full `C_K^ctrl` by a literal-`p=2` global duality/height theorem, not only its intersection with the local tangent module.

## Claim firewall

WP49A does not prove:

- `D_K=0` or `J_K=R_K`;
- `D_K=im(beta_str)`, `coker(beta_str)`, a height radical, or any other pure Bockstein object;
- fixed-`2` height nondegeneracy;
- D1c or D2c–D2e;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
