# BSD-R2-A1 WP46A — canonical strict/Kummer Iwasawa truncation comparison

## State

`PROVED_BOUNDED_DERIVED_COMPARISON`

## Protected predecessors

- MATHSOLVE WP45A: `5f7ea71f2d86457575b2bc2f1e8c281f09ce4b87`.
- WP39/WP40: exact finite strict-Greenberg/classical-Kummer comparison over `K` and its Poitou–Tate dual defect.
- WP43A: protected strict Greenberg Iwasawa augmentation/Bockstein naturality.
- MATHFORGE WP46A source admission: `230e449711166e0ad7cf11081cbeec28c553c0ba`, qualifying Nekovář Chapter-8 one-variable Iwasawa descent literally at `p=2`.

## Result

WP46A replaces the noncanonical forward-lifting approach by the canonical direction supplied by the strict Postnikov truncation.

For each relevant local place `w`, let

`S_w:=U_{w,infty}^{+,str}`

be the protected strict Greenberg Iwasawa local-condition complex and let

`K_w^Kum:=U_{w,infty}^{+,Kum}`

be the protected WP45A Kummer local condition.

The strict and Kummer degree-one Iwasawa local conditions coincide canonically:

`H^1(S_w) ~= M_w^Kum`.

Therefore

`K_w^Kum ~= tau_{<=1}S_w`

as local conditions over the ambient local Iwasawa cochain complex. There is a canonical reverse comparison

`K_w^Kum -> S_w`.

At odd places the map is an isomorphism. At `w|2`, put

`m_2:=ord_2(3-a_2)`.

Using the protected WP46A MATHFORGE descent theorem together with finite-layer local Tate duality, WP46A proves

`Z_w^str:=H^2(S_w)
 ~= Lambda_w/(2^{m_2},gamma_w-1)
 ~= Z/2^{m_2}Z`,

with trivial `Gamma_w` action.

Hence the canonical local comparison triangle is

`K_w^Kum
 -> S_w
 -> Z_w^str[-2]
 -> K_w^Kum[1]`.

This route requires no forward Postnikov retraction and no vanishing assumption on the strict Postnikov class.

WP46A also closes the remaining WP45A local kernel at `w|2`:

`B_w^Kum=0`.

Consequently the full Kummer specialization defect satisfies

`0 -> (M_w^Kum)_{Gamma_w}
   -> H^1(U_{w,0}^{+,Kum})
   -> U_w
   -> 0`.

Combining this with strict descent and the protected finite strict/Kummer quotient gives a canonical derived-control filtration

`0 -> Z_w^str
   -> U_w
   -> R_w
   -> 0`,

where

`R_w:=H^1(K_w,T_w^-)_tors`

and

`len Z_w^str=m_2`, `len U_w=2m_2`, `len R_w=m_2`.

Protected WP28 independently gives

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`.

WP46A does not identify these two filtrations merely from equal lengths.

## Refined boundary

The former boundary

`MISSING_P2_STRICT_TO_KUMMER_IWASAWA_COMPARISON_AND_DERIVED_DEFECT_IDENTIFICATION_OVER_K`

is narrowed to

`MISSING_P2_MAP_LEVEL_RECONCILIATION_OF_STRICT_H2_AND_FORMAL_UNIVERSAL_NORM_FILTRATIONS`.

A successor must compare the two exact filtrations of the same `U_w` map-by-map. Only then may one identify

`Z_w^str` with `F_w^norm`

or transport the resulting local correction into WP40's global dual defect/Bockstein normalization.

## Optional forward-retraction algebra

If a forward strict-to-Kummer retraction is nevertheless desired, WP46A computes its obstruction groups explicitly. With

`a=2^{m_2}`, `t=gamma_w-1`,

one has

`Ext^2_{Lambda_w}(Z_w^str,M_w^Kum)
 ~= M_w^Kum/(aM_w^Kum+tM_w^Kum)`

and

`Ext^1_{Lambda_w}(Z_w^str,M_w^Kum)
 ~= ((M_w^Kum)_{Gamma_w})[a]`.

These groups no longer control the canonical comparison route.

## Claim firewall

WP46A does not prove:

- `Z_w^str=F_w^norm` map-by-map;
- `R_w=E_tilde(F_2)` under the exact comparison maps;
- the global WP40 defect `D_K` is a Bockstein or height defect;
- fixed-`2` height nondegeneracy;
- D1c, D2c–D2e;
- BSD or MATHCERT certification.