# WP49A theorem — localized strict Bockstein and the full Kummer-control quotient

## 1. Protected setup

Retain protected WP48A. Write

`A_Kum := C_Kum,infty tensor^L_Lambda Z_2`,

`B_str := C_str,0`,

and let

`Q_aug := Q_infty tensor^L_Lambda Z_2`.

The protected reverse comparison gives the exact triangle

`A_Kum -> B_str -> Q_aug -> A_Kum[1]`.

Put

`Zloc := Z_{2,K}^loc := direct_sum_{w|2} Z_w^str`.

Protected WP48A proves

`H^1(Q_aug)=Zloc tensor t_cyc`,

`H^2(Q_aug)=Zloc`.

Let

`lambda_K:H^1(B_str) -> Zloc tensor t_cyc`

be the degree-one comparison boundary.

Protected WP37/WP43A gives the strict cyclotomic Bockstein

`beta_str:H^1(B_str)
          -> H^2(B_str) tensor t_cyc`.

## 2. The comparison-cone Bockstein

The Iwasawa comparison cone is

`Q_infty ~= direct_sum_{w|2} Ind_w(Z_w^str[-2])`.

Each `Z_w^str` is annihilated by the local augmentation parameter `t_w=gamma_w-1`.

For one such module, use the standard augmentation resolution

`0 -> Lambda_w --t_w--> Lambda_w -> Z_2 -> 0`.

After tensoring with `Z_w^str`, the differential is zero. Thus the two cohomology groups of derived augmentation are the `Tor_1` copy and the specialization copy of the same module.

The first-order Bockstein connecting morphism for this two-term complex is the canonical identification

`beta_Q:
 H^1(Q_aug)
 -> H^2(Q_aug) tensor t_cyc`.

The sign is fixed by the same augmentation convention used in protected WP43A. No multiplication by a nontrivial element of `Z_2` is introduced.

### Lemma `BSD-A1-WP49A-CONE-BOCKSTEIN-001`

`beta_Q` is an isomorphism. Under the protected tangent-line convention it is the canonical identity between

`Zloc tensor t_cyc`

and

`Zloc tensor t_cyc`.

## 3. Naturality gives the exact localized Bockstein

The Iwasawa morphism

`C_str,infty -> Q_infty`

induces after augmentation the protected map

`B_str -> Q_aug`.

Bockstein connecting morphisms are natural for morphisms of the underlying first-order augmentation triangles. Therefore the square

`H^1(B_str)  --beta_str-->  H^2(B_str) tensor t_cyc`

`    | lambda_K                    | pi_Z tensor 1`

`    v                             v`

`H^1(Q_aug) --beta_Q--> H^2(Q_aug) tensor t_cyc`

commutes, where

`pi_Z:H^2(B_str) -> H^2(Q_aug)=Zloc`

is the canonical map induced by `B_str -> Q_aug`.

### Theorem `BSD-A1-WP49A-LOCALIZED-BOCKSTEIN-002`

One has exactly

`lambda_K
 = beta_Q^{-1} o (pi_Z tensor 1) o beta_str`.

Thus the WP48A comparison boundary is the ordinary-local projection of Nekovar's protected strict cyclotomic Bockstein.

This is an equality of maps with the fixed augmentation convention. It is not an equality only up to a `2`-adic unit.

## 4. The full global Kummer-control image

Protected WP48A has the Kummer augmentation triangle

`A_Kum -> C_Kum,0 -> Delta_Kum ->`,

with

`H^1(Delta_Kum)=U_K^aug`.

Let

`delta_Kum:
 H^1(C_Kum,0)=S_2(E/K)
 -> U_K^aug`

be its connecting morphism, and define

`C_K^ctrl := im(delta_Kum)`.

The WP48A octahedron gives a commutative diagram between this triangle and the finite strict-to-Kummer comparison triangle. Its degree-one local quotient identifies

`R_K
 = U_K^aug/(Zloc tensor t_cyc)`

and the image of `S_2(E/K)` in `R_K` is exactly protected WP39 `J_K`.

## 5. Intersection theorem

### Theorem `BSD-A1-WP49A-INTERSECTION-003`

Inside `U_K^aug`,

`C_K^ctrl intersect (Zloc tensor t_cyc)
 = im(lambda_K)`.

### Proof

For the forward inclusion from right to left, take

`b in H^1(B_str)`.

Its image in `H^1(C_Kum,0)` is a base Kummer Selmer class. Naturality of the octahedral diagram identifies its Kummer-control boundary with the image of `lambda_K(b)` under

`H^1(Q_aug) -> H^1(Delta_Kum)=U_K^aug`.

Hence every element of `im(lambda_K)` belongs to `C_K^ctrl` and to the local tangent submodule.

Conversely take

`c in C_K^ctrl intersect (Zloc tensor t_cyc)`.

Choose `s in H^1(C_Kum,0)` with

`delta_Kum(s)=c`.

The image of `c` in the WP48A finite comparison module `V_K` is zero because the tangent submodule is the kernel of

`U_K^aug -> V_K`.

By commutativity of the octahedron, the image of `s` in

`H^1(Q_fin)=V_K`

is therefore zero. Exactness of

`B_str -> C_Kum,0 -> Q_fin`

implies that `s` comes from some

`b in H^1(B_str)`.

Applying the same commutative diagram gives

`c=lambda_K(b)`

inside `U_K^aug`. QED.

By Theorem `LOCALIZED-BOCKSTEIN-002`, this also says

`C_K^ctrl intersect (Zloc tensor t_cyc)
 = im((pi_Z tensor 1) o beta_str)`

under the canonical `beta_Q` identification.

## 6. Exact control-to-global-hit sequence

The quotient map

`U_K^aug -> R_K`

has kernel `Zloc tensor t_cyc`. Protected WP48A proves that the image of the global Kummer-control image in `R_K` is exactly `J_K`.

Theorem `INTERSECTION-003` therefore gives:

### Corollary `BSD-A1-WP49A-CONTROL-JK-004`

There is a canonical exact sequence

`0
 -> im(lambda_K)
 -> C_K^ctrl
 -> J_K
 -> 0`.

Equivalently, the localized strict Bockstein describes exactly the part of the global Kummer-control image that lies in the ordinary tangent defect.

It does not, by itself, describe the full image `C_K^ctrl`.

## 7. Exact quotient dual to `D_K`

Since

`R_K=U_K^aug/(Zloc tensor t_cyc)`

and

`J_K=(C_K^ctrl+(Zloc tensor t_cyc))/(Zloc tensor t_cyc)`,

the third isomorphism theorem gives canonically

`R_K/J_K
 ~= U_K^aug /
    ((Zloc tensor t_cyc)+C_K^ctrl)`.

Protected WP40 gives a perfect pairing

`R_K x R_K^dual -> Q_2/Z_2`

and

`D_K=ann(J_K)`.

For a finite perfectly paired group, the annihilator of `J_K` is canonically the Pontryagin dual of the quotient `R_K/J_K`.

### Theorem `BSD-A1-WP49A-DK-QUOTIENT-005`

There is a canonical isomorphism

`D_K
 ~= (U_K^aug /
      ((Zloc tensor t_cyc)+C_K^ctrl))^vee`.

Equivalently,

`D_K^vee
 ~= U_K^aug /
    ((Zloc tensor t_cyc)+C_K^ctrl)`.

No length-only argument is used.

## 8. Separation theorem

The protected strict Bockstein determines

`im(lambda_K)
 = C_K^ctrl intersect (Zloc tensor t_cyc)`.

The WP40 defect, however, is dual to

`U_K^aug /
 ((Zloc tensor t_cyc)+C_K^ctrl)`.

These are different functorial constructions. The latter depends on the entire global Kummer-control image, not only its intersection with the tangent term.

### Theorem `BSD-A1-WP49A-SEPARATION-006`

From the protected data through WP49A one may not identify `D_K` with

- `im(beta_str)`;
- `ker(beta_str)`;
- `coker(beta_str)`;
- the radical of the first height;
- or any other pure Bockstein subquotient

without an additional theorem characterizing `C_K^ctrl` in strict Bockstein/Poitou-Tate/height terms.

The minimal remaining D2b datum is therefore the full control image `C_K^ctrl`.

## 9. Source screen at the new boundary

Protected MATHFORGE `79f7c88cf4e59886902c2f12d29d7c73afced379` records the bounded WP49 source screen of Macias Castillo–Sano 2026.

That work supplies a close Selmer-complex/Poitou-Tate/derived-height comparator, but it assumes `p` odd throughout. It therefore cannot supply the selected literal-`p=2` theorem characterizing `C_K^ctrl`.

This is an applicability result for that source, not a theorem that no suitable `p=2` theorem exists.

## 10. Refined boundary

The previous boundary

`MISSING_P2_IDENTIFICATION_OF_WP40_ANNIHILATOR_WITH_STRICT_BOCKSTEIN_SUBQUOTIENT`

is replaced by the strictly smaller datum

`MISSING_P2_GLOBAL_KUMMER_CONTROL_IMAGE_TO_STRICT_BOCKSTEIN_DUALITY`.

A sufficient successor theorem must identify the full image

`C_K^ctrl subset U_K^aug`

through literal-`p=2` global Poitou-Tate/Selmer-complex duality and the strict cyclotomic Bockstein or height pairing. It must preserve the exact integral maps and may not discard finite `2`-primary terms.

## 11. Claim firewall

WP49A does not prove:

- `D_K=0`;
- `J_K=R_K`;
- a pure Bockstein formula for `D_K`;
- fixed-`2` height nondegeneracy;
- an analytic determinant generator at height-one `(2)`;
- remaining Disegni factors;
- p-adic/real regulator equality;
- WP00 normalization;
- final quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
