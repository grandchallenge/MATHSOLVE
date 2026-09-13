# BSD-001 frontier after WP48A

## Protected predecessor

- MATHSOLVE WP47A: `f62436e7d153eab199c7c85a4f7fdc8791d0b959`.
- MATHFORGE provider/source state: `4306aaeef25ac0923e4442ca1c8c1068ed55b514`.

## WP48A global closure

WP48A globalizes the protected reverse local comparison

`U_{w,infty}^{+,Kum} -> U_{w,infty}^{+,str}`

and proves

`C_Kum,infty -> C_str,infty -> Q_infty ->`

with

`Q_infty ~= direct_sum_{w|2} Ind_w(Z_w^str[-2])`.

Derived augmentation gives

`H^1(Q_aug)=Z_2,K^loc tensor t_cyc`,

`H^2(Q_aug)=Z_2,K^loc`,

where

`Z_2,K^loc:=direct_sum_{w|2} Z_w^str`.

The natural Kummer augmentation factors through the exactly specialized strict complex, producing the canonical octahedral triangle

`Q_aug -> Delta_Kum -> Q_fin -> Q_aug[1]`.

Write

`U_K^aug:=direct_sum_w U_w`,

`V_K:=H^1(Q_fin)`.

Then

`Delta_Kum ~= U_K^aug[-1]`,

`Q_fin ~= V_K[-1]`,

and the octahedron gives

`0 -> Z_2,K^loc tensor t_cyc
   -> U_K^aug
   -> V_K
   -> Z_2,K^loc
   -> 0`.

The first map is the actual direct sum of the WP47A formal universal-norm embeddings. Therefore

`U_K^aug/(Z_2,K^loc tensor t_cyc) ~= R_K`

canonically and map-by-map.

The finite comparison cone satisfies

`0 -> R_K -> V_K -> Z_2,K^loc -> 0`.

Most importantly, the image of

`H^1(C_Kum,0)=S_2(E/K) -> V_K`

lands in

`R_K=ker(V_K -> Z_2,K^loc)`

and is exactly the protected WP39 subgroup

`J_K`.

Protected WP40 then places

`D_K=ann(J_K)`

canonically on this derived comparison surface.

WP48A does not identify `D_K` with any Bockstein subquotient.

## Live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

The global strict/Kummer cone and the exact recovery of `J_K,D_K` are closed.

The live boundary is now

`MISSING_P2_IDENTIFICATION_OF_WP40_ANNIHILATOR_WITH_STRICT_BOCKSTEIN_SUBQUOTIENT`.

A successor must compare the protected WP37/WP43A strict cyclotomic Bockstein

`beta_str:H~^1_f(K,T) -> H~^2_f(K,T) tensor t_cyc`

with the canonical WP48A tangent term

`Z_2,K^loc tensor t_cyc = H^1(Q_aug)`.

The target is an exact map-level theorem identifying which Bockstein subquotient, if any, is Pontryagin-dual to `D_K`. Complementary lengths are not enough.

### D2c

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successors

### WP49A — strict Bockstein / WP40 annihilator comparison

Construct the morphism between:

1. Nekovar's protected first-order strict augmentation triangle;
2. the WP48A reverse strict/Kummer comparison triangle after derived augmentation.

Track the global-to-local map on `H~^2_f(K,T)` and determine the exact subquotient controlling the finite tangent module `Z_2,K^loc tensor t_cyc`. Then use the protected local Tate pairing to compare its annihilator with `D_K`.

Do not assume height nondegeneracy and do not replace a map-level comparison by a length identity.

### WP49B — split semistable bad-prime `Q^ord` factors

Bind and compute the exact normalized split Steinberg/newvector toric factors in Disegni's packet, retaining Haar measure, local L-factors, denominator pairing, and Tamagawa-sensitive scalars.

Any new external theorem premise must first be admitted through MATHFORGE.

## Claim firewall

Do not promote:

- `D_K` to a Bockstein image/kernel/cokernel/radical before WP49A;
- `D_K=0` or `J_K=R_K`;
- fixed-`2` height nondegeneracy;
- D1c, D2c, D2d, or D2e;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
