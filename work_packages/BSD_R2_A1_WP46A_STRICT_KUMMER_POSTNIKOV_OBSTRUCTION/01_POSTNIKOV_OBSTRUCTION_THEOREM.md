# WP46A theorem — strict-to-Kummer Iwasawa comparison as a Postnikov lifting problem

## 1. Local setup

Fix a finite place `w` of the protected imaginary quadratic field `K`. Let

`Lambda_w:=Z_2[[Gamma_w]]`

for the local cyclotomic decomposition group, and put

`C_w:=RΓ_Iw(K_w,T)`.

Let

`S_w:=U_{w,infty}^{+,str}`

be the protected strict Greenberg Iwasawa local-condition complex from WP43A, with structural morphism

`i_w^str:S_w->C_w`.

Let

`K_w^Kum:=U_{w,infty}^{+,Kum}`

be the protected WP45A Kummer local-condition complex, with

`K_w^Kum ~= M_w^Kum[-1]`

and structural morphism

`i_w^Kum:K_w^Kum->C_w`.

Write

`N_w^str:=H^1(S_w)`,

`Z_w^str:=H^2(S_w)`.

The local Iwasawa complexes in the protected Nekovář setup have cohomological amplitude at most `[0,2]`. We first identify the lower truncation of `S_w`.

## 2. Vanishing of strict degree zero

### Lemma `BSD-A1-WP46A-H0-001`

`H^0(S_w)=0` at every relevant finite place.

### Proof

At `w|2`, the strict Greenberg source is the ordinary subrepresentation `T_w^+ subset T`. Therefore

`H^0(K_{n,w},T_w^+) subset H^0(K_{n,w},T)`

at every finite layer. The latter group is zero because `E(K_{n,w})[2^infinity]` is finite and hence admits no compatible Tate-module tower. Passing to Iwasawa cohomology preserves degree-zero vanishing.

Away from `2`, the protected strict local condition is unramified. Its degree-zero group is a subgroup of `H^0(K_{n,w},T)`, hence again zero. QED.

Consequently

`tau_{<=1}S_w ~= N_w^str[-1]`.

## 3. Strict degree-one classes lie in the Kummer condition

### Theorem `BSD-A1-WP46A-H1-INCLUSION-002`

The structural map on `H^1` induces a canonical injection

`u_w:N_w^str -> M_w^Kum`.

### Proof

At each finite layer, the protected strict and Kummer local conditions satisfy the usual inclusion.

For `w|2`, the strict Greenberg local condition is

`ker(H^1(K_{n,w},T) -> H^1(K_{n,w},T_w^-))`,

whereas the classical compact Kummer local condition is, by the protected WP39 Nekovář interface,

`ker(H^1(K_{n,w},T) -> H^1(K_{n,w},T_w^-)/tors)`.

The former kernel is contained in the latter.

At odd places, the strict local condition is unramified. The protected semistable local comparison identifies the classical Kummer enlargement as adding only the finite component-group contribution; hence the unramified subgroup is contained in the compact Kummer subgroup.

These finite-layer inclusions are compatible with corestriction/norm. The degree-zero vanishing above identifies Iwasawa `H^1` of the strict local condition with the inverse limit of its finite-layer degree-one groups. Protected WP45A identifies the Kummer inverse limit with `M_w^Kum`. Passing to inverse limits gives the stated canonical injection. QED.

The induced morphism between degree-one truncations is therefore

`u_w[-1]:tau_{<=1}S_w ~= N_w^str[-1]
 -> M_w^Kum[-1] ~= K_w^Kum`.

## 4. The strict Postnikov class

Because `S_w` has amplitude contained in `[1,2]`, there is a canonical truncation triangle

`N_w^str[-1]
 -> S_w
 -> Z_w^str[-2]
 --kappa_w^str--> N_w^str`.

The connecting morphism defines the strict local Postnikov class

`kappa_w^str
 in Hom_{D(Lambda_w)}(Z_w^str[-2],N_w^str)
 = Ext^2_{Lambda_w}(Z_w^str,N_w^str)`.

This class is zero exactly when the strict local condition splits in the derived category as

`N_w^str[-1] direct_sum Z_w^str[-2]`.

WP46A does not assume such a splitting.

## 5. Exact lifting criterion

We seek a derived local-condition morphism

`f_w:S_w -> K_w^Kum`

whose restriction to `tau_{<=1}S_w` is the canonical map `u_w[-1]` and which is compatible with the structural maps to `C_w`.

First ignore the final compatibility with `C_w` and solve the intrinsic extension problem.

### Theorem `BSD-A1-WP46A-OBSTRUCTION-003`

A morphism

`f_w:S_w -> M_w^Kum[-1]`

extending `u_w[-1]` exists if and only if

`o_w:=(u_w)_*(kappa_w^str)=0`

in

`Ext^2_{Lambda_w}(Z_w^str,M_w^Kum)`.

When `o_w=0`, the set of such extensions is a torsor under

`Ext^1_{Lambda_w}(Z_w^str,M_w^Kum)`.

### Proof

Apply the contravariant functor

`Hom_{D(Lambda_w)}(-,M_w^Kum[-1])`

to the truncation triangle

`N_w^str[-1] -> S_w -> Z_w^str[-2] -> N_w^str`.

The resulting exact sequence contains

`Hom(S_w,M_w^Kum[-1])
 -> Hom(N_w^str[-1],M_w^Kum[-1])
 -> Hom(Z_w^str[-2],M_w^Kum)`.

The middle term is

`Hom_{Lambda_w}(N_w^str,M_w^Kum)`,

and the right term is

`Ext^2_{Lambda_w}(Z_w^str,M_w^Kum)`.

The connecting homomorphism sends `u_w` to the pushforward of the Postnikov class, `(u_w)_*(kappa_w^str)`. Exactness proves the existence criterion.

The kernel acting on the fibre of the restriction map is the preceding term

`Hom(Z_w^str[-2],M_w^Kum[-1])
 = Ext^1_{Lambda_w}(Z_w^str,M_w^Kum)`.

Hence, when nonempty, the set of extensions is a torsor under this group. QED.

## 6. Compatibility with the ambient local cochain complex

The two structural morphisms induce the same map on `H^1` after composing with `u_w`, by construction of `u_w` from the finite-layer strict/Kummer inclusions.

A lift `f_w` becomes a morphism of local conditions precisely when

`i_w^Kum o f_w = i_w^str`

in `D(Lambda_w)`.

The difference

`d_w:=i_w^Kum o f_w-i_w^str`

vanishes on `tau_{<=1}S_w`. Therefore it factors through the higher Postnikov quotient `Z_w^str[-2]`.

### Corollary `BSD-A1-WP46A-AMBIENT-004`

After the intrinsic obstruction `o_w` vanishes, the remaining ambient-compatibility defect is a class in

`Hom_{D(Lambda_w)}(Z_w^str[-2],C_w)
 = Hom_{D(Lambda_w)}(Z_w^str,H^2(C_w))`.

Changing the chosen intrinsic lift by an element of

`Ext^1_{Lambda_w}(Z_w^str,M_w^Kum)`

changes this ambient defect by the induced map from the same ambiguity group.

Thus the full strict-to-Kummer local-condition lifting problem is finite-dimensional in the derived sense: it consists only of the Postnikov obstruction, the `Ext^1` lift ambiguity, and the resulting degree-two ambient compatibility class.

No lower-degree ambiguity remains.

## 7. Odd places are unobstructed

At an odd place, the protected strict local condition is unramified. The unramified Galois quotient has cohomological dimension one for the relevant `2`-primary compact coefficient module. Hence

`Z_w^str=H^2(S_w)=0`.

### Corollary `BSD-A1-WP46A-ODD-005`

For every odd relevant place,

`o_w=0`,

`Ext^1_{Lambda_w}(Z_w^str,M_w^Kum)=0`,

and the strict-to-Kummer local comparison lift is canonical.

Therefore every possible derived lifting obstruction and ambiguity is concentrated at the good-ordinary places above `2`.

## 8. Ordinary places above `2`

For `w|2`, protected WP39 identifies the finite-level strict/Kummer enlargement with the torsion ordinary quotient

`H^1(K_w,T_w^-)_tors`

of exact length

`m_2:=ord_2(3-a_2)`.

The protected strict local complex may have nonzero degree-two cohomology; this is exactly why a group-level `H^1` inclusion does not automatically produce a morphism of the full strict complex into the simple Kummer complex.

WP46A deliberately retains

`Z_w^str=H^2(S_w)`

as an exact Iwasawa module rather than replacing it by its finite-level size.

The remaining ordinary local problem is therefore the explicit evaluation of

`(u_w)_*(kappa_w^str)
 in Ext^2_{Lambda_w}(Z_w^str,M_w^Kum)`,

together with the possible lift ambiguity

`Ext^1_{Lambda_w}(Z_w^str,M_w^Kum)`

and the degree-two ambient compatibility class of Corollary `AMBIENT-004`.

## 9. Global consequence

Once compatible local lifts are fixed at the two places above `2`, the canonical odd-place lifts and completed induction yield a global morphism

`C_str,infty -> C_Kum,infty`.

Its cone is then a well-defined strict/Kummer Iwasawa comparison object whose derived augmentation can be compared with WP39/WP40.

Until the ordinary local obstruction is evaluated, no such global comparison morphism is asserted.

## 10. Refined boundary

The prior boundary

`MISSING_P2_STRICT_TO_KUMMER_IWASAWA_COMPARISON_AND_DERIVED_DEFECT_IDENTIFICATION_OVER_K`

is reduced to the ordinary local boundary

`MISSING_P2_ORDINARY_STRICT_POSTNIKOV_PUSHFORWARD_AND_LIFT_CHOICE_AT_2`.

A successor must evaluate, at either place `w|2`,

`Z_w^str`,

`(u_w)_*(kappa_w^str)`,

`Ext^1_{Lambda_w}(Z_w^str,M_w^Kum)`,

and the residual degree-two ambient compatibility class.

Because the two places above `2` are split copies of the same local field/tower, one local calculation transports to the conjugate place.

## 11. Claim firewall

WP46A does not prove:

- that the ordinary Postnikov obstruction vanishes;
- that an ordinary strict-to-Kummer lift exists;
- that such a lift is unique;
- a value or structure theorem for `Z_w^str`;
- `B_w^Kum=0`;
- cancellation of the formal universal-norm term;
- equality of the eventual comparison cone with WP39/WP40 before a lift is fixed;
- that `D_K` is a Bockstein or height defect;
- D1c, D2a, D2c–D2e;
- BSD or certification.