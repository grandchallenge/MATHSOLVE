# BSD-R2-A1 WP47A — map-level reconciliation of the ordinary local filtrations

## State

`PROVED_BOUNDED_LOCAL_MAP_RECONCILIATION`

## Protected predecessors

- MATHSOLVE WP46A: `a9fb791a2bb75f2db97ec38c2fcd67e30a9ec27e`.
- MATHFORGE provider index/source state: `4306aaeef25ac0923e4442ca1c8c1068ed55b514`.
- WP28/Tan: literal-`p=2` formal/full/reduction universal-norm sequence, with the quotient map induced by literal reduction and exact Pontryagin-dual cohomology sequence.
- WP39/Nekovar-Greenberg: literal-`p=2` compact strict-to-Kummer local comparison, with ordinary target `R_w=H^1(K_w,T_w^-)_tors`.
- WP46A: `B_w^Kum=0` and the canonical derived-control filtration `0 -> Z_w^str -> U_w -> R_w -> 0`.

No new external theorem premise is used.

## Result

Fix either protected split place `w|2`, so `K_w~=Q_2`, and put

`m_2:=ord_2(3-a_2)`.

Let

`0 -> T_w^+ -> T -> T_w^- -> 0`

be the ordinary lattice sequence and set

`A_w^-:=T_w^- tensor (Q_2/Z_2)`,

`V_w^-:=T_w^- tensor Q_2`.

Because `H^0(K_w,V_w^-)=0`, the coefficient sequence

`0 -> T_w^- -> V_w^- -> A_w^- -> 0`

induces a canonical isomorphism

`delta_w:H^0(K_w,A_w^-) -> H^1(K_w,T_w^-)_tors=R_w`.

The ordinary etale quotient identifies

`H^0(K_w,A_w^-) ~= E_tilde(F_2)[2^infinity]`.

On the selected branch `#E_tilde(F_2)=3-a_2 in {2,4}`, so the whole reduction group is `2`-primary. Therefore

`rho_w:E_tilde(F_2) -> R_w`

is a canonical isomorphism.

WP47A proves the map-level identity

`q_w = rho_w o red_w`

on compact Kummer points, where

`red_w:E(K_w)^hat_2 -> E_tilde(F_2)`

is literal reduction and

`q_w:E(K_w)^hat_2 -> R_w`

is the protected finite strict-to-Kummer quotient map. The proof is by naturality of finite Kummer connecting morphisms under the ordinary etale quotient, followed by inverse limit in the exponent.

Both maps kill the stabilized universal norms. Hence on

`U_w=E(K_w)^hat_2/N_w^infinity`

the square

`U_w --qbar_w--> R_w`

` | redbar_w       ^ rho_w`

` v                |`

`E_tilde(F_2) -----`

commutes and `rho_w` is an isomorphism.

Consequently the two protected short exact sequences

`0 -> Z_w^str -> U_w -> R_w -> 0`

and

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`

are the same filtration under the canonical quotient identification. In particular,

`Z_w^str=F_w^norm`

as the same subgroup of `U_w`, not merely as abstract groups of equal order, and

`R_w ~= E_tilde(F_2)`

through `rho_w`.

## Refined D2b boundary

The local map-level filtration discrepancy is closed. The surviving D2b problem is global/derived:

`MISSING_P2_GLOBAL_STRICT_KUMMER_COMPARISON_CONE_TO_WP40_BOCKSTEIN_DEFECT`.

A successor must assemble the protected local reverse comparison triangles into the global strict/Kummer Selmer-complex comparison, derive its augmentation triangle, and identify the resulting finite global defect with the WP39/WP40 pair `J_K,D_K` before any Bockstein/height interpretation is promoted.

## Claim firewall

WP47A does not prove:

- `D_K` is a Bockstein image, kernel, cokernel, or radical;
- fixed-`2` height nondegeneracy;
- the height-one `(2)` analytic determinant generator;
- the remaining Disegni split bad-prime/global `Q^ord` factors;
- classical Gross-Zagier/WP00 normalization;
- final WP06 quadratic descent of normalization;
- `BSD-R2-A1`;
- MATHCERT certification.