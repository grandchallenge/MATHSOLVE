# BSD-001 frontier after WP47A

## Protected predecessor

- MATHSOLVE WP46A: `a9fb791a2bb75f2db97ec38c2fcd67e30a9ec27e`.
- MATHFORGE provider/source state: `4306aaeef25ac0923e4442ca1c8c1068ed55b514`.

## WP47A local closure

At each protected place `w|2`, the two exact filtrations of the full universal-norm defect

`U_w=E(K_w)^hat_2/N_w^infinity`

are now reconciled map-by-map.

Protected WP46A gives

`0 -> Z_w^str -> U_w -> R_w -> 0`,

where

`Z_w^str=H^2(U_{w,infty}^{+,str})`,

`R_w=H^1(K_w,T_w^-)_tors`.

Protected WP28 gives

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`,

with quotient map induced by literal reduction.

WP47A constructs the canonical isomorphism

`rho_w:E_tilde(F_2) -> R_w`

from the connecting map of

`0 -> T_w^- -> V_w^- -> A_w^- -> 0`

and proves, by naturality of finite Kummer cocycles under the ordinary etale quotient,

`q_w=rho_w o red_w`

on compact local points. Passing to `U_w` gives

`qbar_w=rho_w o redbar_w`.

Therefore

`Z_w^str=F_w^norm`

as the same subgroup of `U_w`, and the two short exact sequences are the same filtration under `rho_w`.

This is a map-level theorem; it is not inferred from matching cardinalities.

The result applies at both split places over `2`.

## Exact local dictionary now protected after WP47A

With

`m_2:=ord_2(3-a_2)`, one has

`Z_w^str=F_w^norm
 ~= Lambda_w/(2^{m_2},gamma_w-1)`

as the mapped finite subgroup of `U_w`, and

`R_w ~= E_tilde(F_2)`

canonically through the local quotient map.

No hidden power of `2` or unit remains between these local strict/formal descriptions.

## Live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

The local strict/Kummer/formal mismatch is closed. The live boundary is now global/derived:

`MISSING_P2_GLOBAL_STRICT_KUMMER_COMPARISON_CONE_TO_WP40_BOCKSTEIN_DEFECT`.

A successor must:

1. assemble the local reverse comparison morphisms
   `U_{w,infty}^{+,Kum} -> U_{w,infty}^{+,str}`
   into a global morphism of Selmer complexes;
2. compute the global comparison cone and its derived cyclotomic augmentation;
3. identify its finite specialization map-by-map with the protected WP39 strict/Kummer quotient and global image `J_K`;
4. identify the dual finite obstruction with protected WP40's
   `D_K=ann(J_K)`;
5. only then compare that global defect with the protected WP37/WP43A Bockstein/height triangle.

### D2c

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successors

### WP48A — global strict/Kummer comparison cone

Assemble the protected local Kummer-to-strict truncation morphisms by completed induction and Nekovar's mapping-fibre construction. Determine the cone in the global derived category and derive its augmentation. The finite specialized sequence must recover WP39/WP40 maps, not only their lengths.

### WP48B — split semistable bad-prime `Q^ord` factors

Bind and compute the exact normalized split Steinberg/newvector toric factors in Disegni's packet, including Haar measure, local L-factors, denominator pairing, and Tamagawa-sensitive scalars.

## Claim firewall

Do not promote:

- `D_K` to any Bockstein/height defect before WP48A;
- `D_K=0` or `J_K=R_K`;
- fixed-p=2 height nondegeneracy;
- local `Q^ord_2=1` to global `Q^ord=1`;
- D1c, D2d, or D2e;
- BSD-R2-A1;
- MATHCERT certification, novelty, or priority.