# BSD-R2-A1 WP48A — global strict/Kummer comparison cone

## State

`PROVED_BOUNDED_GLOBAL_DERIVED_COMPARISON`

## Protected predecessors

- MATHSOLVE WP47A protected head: `f62436e7d153eab199c7c85a4f7fdc8791d0b959`.
- MATHFORGE provider state: `4306aaeef25ac0923e4442ca1c8c1068ed55b514`.
- WP39: finite strict-Greenberg/classical-Kummer comparison and actual global hit `J_K`.
- WP40: exact Poitou-Tate annihilator `D_K=ann(J_K)`.
- WP43A: source-qualified strict cyclotomic augmentation/Bockstein naturality.
- WP45A: canonical compact Kummer Iwasawa Selmer complex and derived local augmentation defect.
- WP46A: canonical reverse Kummer-to-strict Iwasawa comparison and exact ordinary strict `H^2`.
- WP47A: map-level equality of the ordinary strict-`H^2` and formal universal-norm filtrations.

No new external theorem premise is introduced in WP48A.

## Result

Let

`C_Kum,infty -> C_str,infty`

be the protected reverse Iwasawa comparison. WP48A assembles the local comparison maps through the global Nekovar mapping-fibre construction and proves that its cone is supported only at the two places over `2`:

`Q_infty ~= direct_sum_{w|2} Ind_w(Z_w^str[-2])`.

Derived augmentation gives a two-degree finite complex `Q_aug` with

`H^1(Q_aug)=Z_2,K^loc tensor t_cyc`,

`H^2(Q_aug)=Z_2,K^loc`,

where

`Z_2,K^loc:=direct_sum_{w|2} Z_w^str`.

The natural Kummer augmentation factors through the exactly specialized strict complex. Writing

`Delta_Kum:=Cone(C_Kum,infty tensor^L_Lambda Z_2 -> C_Kum,0)`

and

`Q_fin:=Cone(C_str,0 -> C_Kum,0)`,

the octahedral axiom gives a canonical triangle

`Q_aug -> Delta_Kum -> Q_fin -> Q_aug[1]`.

WP48A computes the finite cohomology of this triangle. Put

`U_K^aug:=direct_sum_w U_w`

over the nonzero local Kummer augmentation defects. Then

`Delta_Kum ~= U_K^aug[-1]`.

Put

`V_K:=H^1(Q_fin)`.

Then

`Q_fin ~= V_K[-1]`

and there is a canonical exact sequence

`0 -> R_K -> V_K -> Z_2,K^loc -> 0`.

The octahedral long exact sequence is

`0 -> Z_2,K^loc -> U_K^aug -> V_K -> Z_2,K^loc -> 0`.

Under protected WP47A, the first map is the direct sum of the actual formal universal-norm embeddings. Hence

`U_K^aug/Z_2,K^loc ~= R_K`

canonically and map-by-map, including the odd bad-prime terms.

Finally, the global map

`H^1(C_Kum,0)=S_2(E/K) -> V_K`

lands in

`ker(V_K -> Z_2,K^loc)=R_K`,

and its image is exactly protected WP39's `J_K`. Thus `J_K` is now recovered inside the specialized derived comparison cone, not merely as an independently named finite subgroup.

By protected WP40,

`D_K=ann_{R_K^dual}(J_K)`.

Therefore the WP40 defect is canonically attached to the derived comparison cone. WP48A does **not** identify it with a Bockstein image, kernel, cokernel, radical, or determinant.

## Refined D2b boundary

The previous boundary

`MISSING_P2_GLOBAL_STRICT_KUMMER_COMPARISON_CONE_TO_WP40_BOCKSTEIN_DEFECT`

is narrowed to

`MISSING_P2_IDENTIFICATION_OF_WP40_ANNIHILATOR_WITH_STRICT_BOCKSTEIN_SUBQUOTIENT`.

A successor must compare the strict cyclotomic Bockstein of WP37/WP43A with the canonical exact sequence above and determine exactly which Bockstein subquotient, if any, is Pontryagin-dual to `D_K`.

## Claim firewall

WP48A does not prove:

- `D_K=0` or `J_K=R_K`;
- `D_K` equals a Bockstein image, kernel, cokernel, radical, or determinant;
- fixed-`2` height nondegeneracy;
- D1c;
- the remaining Disegni `Q^ord` factors;
- classical/WP00 normalization;
- final WP06 descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
