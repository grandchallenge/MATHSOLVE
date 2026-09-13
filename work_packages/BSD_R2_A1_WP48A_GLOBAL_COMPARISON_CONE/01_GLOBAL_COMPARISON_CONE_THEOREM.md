# WP48A theorem — global strict/Kummer comparison cone and exact finite specialization

## 1. Setup

Retain the protected BSD-001 notation over the WP09 imaginary quadratic field `K`.

Let

`Lambda:=Z_2[[Gamma_K]]`,

with cyclotomic augmentation

`Lambda -> Z_2`.

Protected WP45A constructs the compact Kummer Iwasawa Selmer complex

`C_Kum,infty`.

Protected WP43A and the strict Greenberg formalism give the strict cyclotomic Selmer complex

`C_str,infty`.

Protected WP46A gives, place by place, a canonical reverse morphism of Iwasawa local conditions

`j_w:U_{w,infty}^{+,Kum}
     -> U_{w,infty}^{+,str}`.

At odd places `j_w` is an isomorphism. At each `w|2` there is a canonical exact triangle

`U_{w,infty}^{+,Kum}
 -> U_{w,infty}^{+,str}
 -> Z_w^str[-2]
 ->`,

where

`Z_w^str ~= Lambda_w/(2^{m_2},gamma_w-1)`

and

`m_2:=ord_2(3-a_2)`.

Protected WP47A proves that the mapped subgroup represented by `Z_w^str` is exactly the formal universal-norm subgroup `F_w^norm` inside the full local Kummer augmentation defect `U_w`.

## 2. Global assembly of the reverse comparison

The two global Selmer complexes use the same global Iwasawa cochain complex and the same ambient local Iwasawa cochain complex. They differ only in the local-condition summand.

Use the completed induction convention of protected WP45A:

`Ind_w(C):=Lambda completed_tensor_{Lambda_w} C`.

The direct sum of the induced local maps gives

`j_S:U_{S,infty}^{+,Kum}
     -> U_{S,infty}^{+,str}`.

Functoriality of the Nekovar mapping-fibre construction therefore gives a canonical morphism

`J_infty:C_Kum,infty -> C_str,infty`.

### Theorem `BSD-A1-WP48A-GLOBAL-CONE-001`

There is a canonical exact triangle

`C_Kum,infty
 -> C_str,infty
 -> Q_infty
 -> C_Kum,infty[1]`,

with

`Q_infty
 ~= direct_sum_{w|2} Ind_w(Z_w^str[-2])`.

No odd place contributes to `Q_infty`.

### Proof

Write the two Selmer complexes as fibres

`Fib(C_glob direct_sum U_Kum -> C_loc)`

and

`Fib(C_glob direct_sum U_str -> C_loc)`.

The comparison is the identity on `C_glob` and `C_loc` and is `j_S` on the local-condition summand. For a morphism between two fibres with identity on the common source and target terms, the cone is canonically the cone of the differing local-condition morphism. Hence

`Cone(J_infty) ~= Cone(j_S)`.

Completed induction is exact on the finite free ambient Iwasawa algebra used here, and protected WP46A gives

`Cone(j_w)=0`

at odd places and

`Cone(j_w)=Z_w^str[-2]`

at `w|2`. Taking the induced direct sum gives the displayed formula. QED.

## 3. Derived augmentation of the global comparison cone

Put

`Z_{2,K}^loc:=direct_sum_{w|2} Z_w^str`.

Each `Z_w^str` has trivial local cyclotomic action. For a topological generator `gamma_w`, put

`t_w:=gamma_w-1`.

The augmentation resolution

`0 -> Lambda_w --t_w--> Lambda_w -> Z_2 -> 0`

becomes, after tensoring with `Z_w^str`, the zero differential

`Z_w^str --0--> Z_w^str`.

To record the degree-one copy canonically, write `t_cyc` for the rank-one cyclotomic tangent line `I/I^2` under the protected WP43A convention.

Define

`Q_aug:=Q_infty derived_tensor_Lambda Z_2`.

### Theorem `BSD-A1-WP48A-AUG-CONE-002`

The only nonzero cohomology groups of `Q_aug` are

`H^1(Q_aug)
 ~= Z_{2,K}^loc tensor t_cyc`,

`H^2(Q_aug)
 ~= Z_{2,K}^loc`.

The second group is ordinary coinvariant specialization. The first is the augmentation `Tor_1` copy of the same finite local module.

### Proof

By Theorem `GLOBAL-CONE-001` and derived base change for completed induction,

`Q_aug
 ~= direct_sum_{w|2}
    (Z_w^str derived_tensor_{Lambda_w} Z_2)[-2]`.

For a module concentrated in degree zero, the two-term augmentation resolution has

`Tor_1^{Lambda_w}(Z_w^str,Z_2)=Z_w^str[t_w]=Z_w^str`

and

`Z_w^str tensor_{Lambda_w} Z_2=(Z_w^str)_{Gamma_w}=Z_w^str`

because the action is trivial. The shift `[-2]` moves these groups to cohomological degrees `1` and `2`. The tangent factor records the canonical first-order augmentation direction. QED.

## 4. Exact specialization of the strict side

Protected MATHFORGE WP46A admits Nekovar Chapter-8 derived augmentation at literal `p=2`. Applied to the global and local strict Greenberg Iwasawa cochain complexes, and then to their compatible mapping fibre, it gives a canonical isomorphism

`C_str,infty derived_tensor_Lambda Z_2
 ~= C_str,0`.

This is the strict finite-level Selmer complex used in protected WP37-WP40.

Thus derived augmentation of Theorem `GLOBAL-CONE-001` gives a canonical triangle

`C_Kum,infty derived_tensor_Lambda Z_2
 -> C_str,0
 -> Q_aug
 ->`.

For brevity put

`A_Kum:=C_Kum,infty derived_tensor_Lambda Z_2`.

## 5. Factorization of Kummer specialization through the strict base complex

Protected WP45A gives the natural augmentation map

`a_Kum:A_Kum -> C_Kum,0`.

Protected WP46A proves locally that the augmented Kummer degree-one map injects first into the base strict local condition and that its composite with the finite strict-to-Kummer inclusion is the ordinary Kummer base-projection map.

Protected WP47A strengthens the place-`2` statement map-by-map: under the canonical ordinary connecting isomorphism, the finite strict/Kummer quotient is literal reduction, and the Kummer augmentation defect has the exact strict/formal filtration.

At odd bad places the Iwasawa strict and Kummer conditions coincide, while the base strict condition injects into the base Kummer condition through the protected component-group quotient. At odd good places all three maps are isomorphisms.

Because `A_Kum` is built from the same global/ambient cochains and these local factorizations, the global augmentation factors canonically as

`A_Kum
 -> C_str,0
 -> C_Kum,0`.

### Theorem `BSD-A1-WP48A-FACTORIZATION-003`

The natural Kummer augmentation map equals the above composite in `D(Z_2)`.

### Proof

On the global Galois cochain term and ambient local cochain term both maps are the same canonical augmentation. On each local-condition term the assertion is protected WP46A away from the higher ordinary term, and protected WP47A fixes the remaining place-`2` map orientation. The Nekovar mapping-fibre construction is functorial, so equality on all terms gives equality of the induced global morphisms. QED.

## 6. The two specialization cones

Define

`Delta_Kum:=Cone(A_Kum -> C_Kum,0)`

and

`Q_fin:=Cone(C_str,0 -> C_Kum,0)`.

Theorem `FACTORIZATION-003` makes these the cones of two composable arrows

`A_Kum -> C_str,0 -> C_Kum,0`.

The octahedral axiom therefore gives a canonical exact triangle

`Q_aug -> Delta_Kum -> Q_fin -> Q_aug[1]`.

This triangle is the exact derived bridge that earlier work packages deliberately did not assume.

## 7. Cohomology of the Kummer augmentation cone

Protected WP46A proves `B_w^Kum=0` at `w|2`. The same reverse-comparison argument at odd places identifies the augmented Kummer local condition with the exactly augmented strict Iwasawa condition before the finite strict-to-Kummer enlargement. Hence the possible WP45A `Tor_1` and kernel terms vanish at every relevant place.

The only surviving Kummer augmentation defect is the protected finite cokernel `U_w`.

Put

`U_K^aug:=direct_sum_w U_w`,

where the direct sum is over places with nonzero local defect. Explicitly:

- at each `w|2`, `U_w` is the full universal-norm quotient with exact WP47A filtration;
- at each odd bad split place, `U_w` is the protected `2`-primary component-group quotient;
- at odd good places `U_w=0`.

### Theorem `BSD-A1-WP48A-KUMMER-DEFECT-004`

`Delta_Kum ~= U_K^aug[-1]`.

Equivalently,

`H^1(Delta_Kum)=U_K^aug`

and all other cohomology vanishes.

### Proof

The global and ambient local Iwasawa cochain terms specialize exactly. Therefore the cone of global Kummer augmentation is the direct sum of the local-condition augmentation cones. Protected WP45A computes each local cone. The kernel and `Tor_1` terms vanish by the protected reverse comparison and strict descent just recalled, leaving only `H^1=U_w`. QED.

## 8. Cohomology of the finite strict-to-Kummer comparison cone

Put

`V_K:=H^1(Q_fin)`.

At an odd bad place, the finite strict local complex has no ordinary higher term, so the local cone is simply the finite strict/Kummer quotient in degree one. This is the same component-group module as the corresponding `U_w`.

At each `w|2`, the finite strict local complex has

`H^1=H^1(U_{w,0}^{+,str})`,

`H^2=Z_w^str`,

while the simple Kummer local complex has only

`H^1=E(K_w)^hat_2`.

The finite strict-to-Kummer injection has degree-one quotient

`R_w`.

The local cone long exact sequence therefore gives

`0 -> R_w -> V_w -> Z_w^str -> 0`,

where `V_w` denotes the place-`2` contribution to `V_K`.

Summing all places yields:

### Theorem `BSD-A1-WP48A-FINITE-CONE-005`

`Q_fin ~= V_K[-1]`,

and there is a canonical exact sequence

`0 -> R_K -> V_K -> Z_{2,K}^loc -> 0`.

Here `R_K` is exactly the protected WP39 finite ambient strict/Kummer quotient, including both split places over `2` and all split bad-prime terms.

## 9. The octahedral five-term sequence

Take cohomology of

`Q_aug -> Delta_Kum -> Q_fin -> Q_aug[1]`.

Theorem `AUG-CONE-002`, Theorem `KUMMER-DEFECT-004`, and Theorem `FINITE-CONE-005` give:

### Theorem `BSD-A1-WP48A-OCTAHEDRAL-006`

There is a canonical exact sequence

`0
 -> Z_{2,K}^loc tensor t_cyc
 -> U_K^aug
 -> V_K
 -> Z_{2,K}^loc
 -> 0`.

After the fixed protected identification of the rank-one tangent line, the first term is the same finite module as `Z_{2,K}^loc`; the displayed tangent factor is retained to record its derived origin.

At `w|2`, the first map is exactly the mapped subgroup

`Z_w^str=F_w^norm -> U_w`

of protected WP47A. At odd places the first term is zero.

Consequently the induced quotient map gives a canonical isomorphism

`U_K^aug/(Z_{2,K}^loc tensor t_cyc)
 ~= R_K`,

where the place-`2` component is literal reduction under the protected `rho_w`, and the odd bad-prime components are the protected component-group quotients.

### Proof

The long exact sequence begins in degree zero with zero groups, so the degree-one map from `H^1(Q_aug)` is injective. Its place-`2` component is the map produced by the local octahedron. Protected WP47A identifies this map with the actual formal universal-norm embedding into `U_w` rather than an abstract subgroup of equal order.

The cokernel at each place over `2` is therefore `R_w`; at odd bad places `Q_aug` contributes nothing and `U_w=R_w` by the protected component-group comparison. Summing gives the displayed global quotient `R_K`.

Exactness then identifies the image of `U_K^aug -> V_K` with

`ker(V_K -> Z_{2,K}^loc)=R_K`,

agreeing with Theorem `FINITE-CONE-005`. QED.

## 10. Recovery of the actual global hit `J_K`

Protected WP39 defines

`J_K
 := im(S_2(E/K) -> R_K)`

under the finite strict-to-Kummer quotient map.

Now

`H^1(C_Kum,0)=S_2(E/K)`.

The comparison triangle

`C_str,0 -> C_Kum,0 -> Q_fin ->`

gives a canonical map

`S_2(E/K) -> V_K`.

By the local long exact sequence, its image lies in the submodule

`R_K=ker(V_K -> Z_{2,K}^loc)`:

the subsequent map to the finite strict `H^2` term is zero on a class represented by an actual Kummer Selmer cocycle, and the preceding quotient coordinate is exactly its strict/Kummer local class.

### Theorem `BSD-A1-WP48A-JK-RECOVERY-007`

Under the canonical inclusion

`R_K -> V_K`,

the image of

`H^1(C_Kum,0) -> V_K`

is exactly protected WP39's subgroup `J_K`.

Thus `J_K` is recovered map-by-map as the global image inside the specialized derived comparison cone.

### Proof

At each place the map from base Kummer degree-one cohomology to the local finite comparison cone first records the degree-one quotient by the strict condition. This is precisely the WP39 local quotient map. The global mapping-fibre map is induced by localization, so its product over all places is precisely the global localization map used to define `J_K`. The additional quotient `V_K -> Z_{2,K}^loc` comes from the degree-two strict term and vanishes on this degree-one quotient image by exactness. Therefore the image is the same subgroup `J_K subset R_K`. QED.

## 11. Exact placement of the WP40 defect

Protected WP40 gives a perfect pairing

`R_K x R_K^dual -> Q_2/Z_2`

and proves

`D_K=ann_{R_K^dual}(J_K)`.

Theorem `JK-RECOVERY-007` now makes both `R_K` and `J_K` canonical subobjects of the specialized comparison cone. Therefore `D_K` is no longer external to the derived strict/Kummer comparison: it is the exact annihilator of the global degree-one image in the canonical kernel

`R_K=ker(V_K -> Z_{2,K}^loc)`.

### Corollary `BSD-A1-WP48A-DK-DERIVED-008`

`D_K` is canonically determined by the WP48A derived comparison cone and the protected local Tate pairing.

This corollary is a placement theorem only. It does not identify `D_K` with the strict cyclotomic Bockstein.

## 12. What remains for the Bockstein bridge

Protected WP43A identifies the strict first-order cyclotomic augmentation connecting morphism with the WP37 Bockstein

`beta_str:H~^1_f(K,T)
          -> H~^2_f(K,T) tensor t_cyc`.

WP48A shows that the strict/Kummer comparison produces a canonical local tangent defect

`Z_{2,K}^loc tensor t_cyc = H^1(Q_aug)`

and embeds `J_K`/`D_K` into the same global derived comparison diagram.

What is **not** yet proved is the exact map from the global strict Bockstein target to this local tangent defect, or equivalently the precise Bockstein subquotient whose Pontryagin dual is `D_K`.

The surviving minimal D2b boundary is therefore

`MISSING_P2_IDENTIFICATION_OF_WP40_ANNIHILATOR_WITH_STRICT_BOCKSTEIN_SUBQUOTIENT`.

A successor must construct the morphism of first-order triangles and prove which of

- a Bockstein image,
- a Bockstein cokernel,
- a localized Bockstein image modulo the Kummer-global image,
- or another explicitly derived subquotient

is canonically dual to `D_K`.

No equality may be inferred merely from complementary lengths.

## 13. Claim firewall

WP48A does not prove:

- `D_K=0`;
- `J_K=R_K`;
- `D_K` equals any Bockstein image, kernel, cokernel, radical, or determinant;
- the first cyclotomic height is nondegenerate at fixed `p=2`;
- D1c;
- the remaining Disegni bad-prime/global normalization factors;
- equality of p-adic and Neron-Tate regulators;
- classical/WP00 normalization;
- final WP06 descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
