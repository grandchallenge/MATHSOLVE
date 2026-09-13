# BSD-001 frontier after WP49A

## Protected predecessor and provider state

- MATHSOLVE WP48A: `05a45bd103d33ee828df9f3ff6050a895635a6d7`.
- MATHFORGE provider/source state: `79f7c88cf4e59886902c2f12d29d7c73afced379`.

## WP49A closure

Protected WP48A supplies

`A_Kum -> C_str,0 -> Q_aug ->`

with

`H^1(Q_aug)=Zloc tensor t_cyc`,

`H^2(Q_aug)=Zloc`,

where

`Zloc:=direct_sum_{w|2} Z_w^str`.

WP49A proves that the comparison boundary

`lambda_K:H^1(C_str,0) -> Zloc tensor t_cyc`

is exactly the ordinary-local projection of the protected strict cyclotomic Bockstein

`beta_str:H^1(C_str,0) -> H^2(C_str,0) tensor t_cyc`.

Define the full global Kummer-control image

`C_K^ctrl
 := im(S_2(E/K) -> U_K^aug)`.

Then

`C_K^ctrl intersect (Zloc tensor t_cyc)
 = im(lambda_K)`

and

`0 -> im(lambda_K)
   -> C_K^ctrl
   -> J_K
   -> 0`.

Hence

`R_K/J_K
 ~= U_K^aug / ((Zloc tensor t_cyc)+C_K^ctrl)`

and protected WP40 gives

`D_K
 ~= (U_K^aug / ((Zloc tensor t_cyc)+C_K^ctrl))^vee`.

Therefore the strict Bockstein controls exactly the tangent intersection of the global Kummer-control image. It does not determine the full image `C_K^ctrl`, and so it does not by itself determine `D_K`.

## Source result

Protected MATHFORGE WP49 records Macias Castillo–Sano 2026 as

`QUALIFIED_ODD_PRIME_COMPARATOR_NOT_LITERAL_P2`.

Its Selmer-complex/Poitou–Tate and derived-height comparison is structurally close to the missing theorem, but the article assumes `p` odd throughout. It cannot be specialized mechanically to this `p=2` branch.

## Live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

The localized strict Bockstein and the exact placement of `J_K,D_K` are closed.

The live boundary is

`MISSING_P2_GLOBAL_KUMMER_CONTROL_IMAGE_TO_STRICT_BOCKSTEIN_DUALITY`.

A successor must characterize the full subgroup

`C_K^ctrl subset U_K^aug`

through a literal-`p=2` global Poitou–Tate/Selmer-complex duality theorem compatible with the strict Bockstein/height construction. It must retain finite `2`-primary terms exactly.

### D2c

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successors

### WP50A — literal-p=2 control-image duality

Search first for a literal-`p=2` theorem identifying the global Kummer-control image or its quotient through Poitou–Tate/Selmer-complex duality and the strict cyclotomic Bockstein. If no source applies, attempt a direct theorem from the already-protected compact/discrete duality diagrams. The target is `C_K^ctrl`, not merely `im(lambda_K)`.

### WP50B — split semistable bad-prime `Q^ord` factors

Bind and compute the exact normalized split Steinberg/newvector toric factors in Disegni's packet, retaining Haar measure, local L-factors, denominator pairing, and Tamagawa-sensitive scalars.

## Claim firewall

Do not promote:

- `D_K` to a pure Bockstein image/kernel/cokernel/radical;
- `D_K=0` or `J_K=R_K`;
- height existence to height nondegeneracy;
- D1c, D2c, D2d, or D2e;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
