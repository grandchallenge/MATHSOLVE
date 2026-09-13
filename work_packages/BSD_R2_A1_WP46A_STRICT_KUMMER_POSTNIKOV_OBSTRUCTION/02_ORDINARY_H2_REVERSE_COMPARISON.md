# WP46A strengthening — ordinary strict `H^2` and the canonical reverse comparison

## 1. New protected source input

MATHFORGE protected commit

`230e449711166e0ad7cf11081cbeec28c553c0ba`

admits Nekovář's Chapter-8 one-variable Iwasawa descent literally at `p=2`. In particular, for a local cyclotomic `Z_2`-tower and a finite free `Z_2` lattice `T'`, one has exact finite-layer descent

`0 -> H_Iw^j(T')_{Gamma_n}
   -> H^j(F_n,T')
   -> H_Iw^{j+1}(T')^{Gamma_n}
   -> 0`.

For local cohomology there is no degree `3`, so

`H_Iw^2(T')_{Gamma_n} ~= H^2(F_n,T')`.

We apply this at a protected ordinary place `w|2` with `T'=T_w^+`.

Put

`m_2:=ord_2(3-a_2)`.

## 2. Finite-layer ordinary `H^2`

Let `F_n/K_w` be the local cyclotomic layer of degree `2^n`.

Protected local Tate duality identifies

`H^2(F_n,T_w^+)`

with the Pontryagin dual of

`H^0(F_n,A_w^-)`,

where `A_w^-` is the discrete ordinary quotient dual to `T_w^+`.

The representation `A_w^-` is unramified. The local cyclotomic extension at `2` is totally ramified, so every `F_n` has the same residue field as `K_w`. Therefore

`H^0(F_n,A_w^-)=H^0(K_w,A_w^-)`

for all `n`.

Protected WP39 gives

`H^1(K_w,T_w^-)_tors
 ~= H^0(K_w,A_w^-)/div`

and the protected Greenberg local theorem gives this finite group exact order

`#E_tilde(F_2)=3-a_2=2^{m_2}`.

Protected WP39 also gives `H^0(K_w,V_w^-)=0`, so `H^0(K_w,A_w^-)` is finite and has no divisible subgroup. Since `A_w^-` is a one-dimensional `Q_2/Z_2`-type module, its finite invariant subgroup is cyclic.

### Theorem `BSD-A1-WP46A-FINITE-H2-006`

For every finite local cyclotomic layer,

`H^2(F_n,T_w^+) ~= Z/2^{m_2}Z`

as an abstract finite `Z_2`-module.

In particular its order is independent of `n`.

## 3. A bounded-coinvariant algebra lemma

Let

`Lambda_w=Z_2[[Gamma_w]] ~= Z_2[[t]]`,

with `t=gamma-1`, and put

`omega_n:=gamma^{2^n}-1`.

### Lemma `BSD-A1-WP46A-BOUNDED-COINV-007`

Let `M` be a finitely generated compact `Lambda_w`-module. Suppose every

`M/omega_n M`

is finite, cyclic, and has the same order `2^m`. Then

`M ~= Z/2^m Z`

and `Gamma_w` acts trivially on `M`.

### Proof

First reduce modulo `2`. Since

`omega_n == t^{2^n} (mod 2)`,

the quotients

`(M/2M)/t^{2^n}(M/2M)`

have uniformly bounded `F_2`-dimension. A finitely generated module over the PID `F_2[[t]]` can have uniformly bounded `t^{2^n}`-coinvariants only if it is torsion; hence `M/2M` has finite `F_2`-dimension.

Choose `r` with

`t^r M subset 2M`.

If `e_1,...,e_d` generate `M` over `Lambda_w`, then every higher power `t^{qr+s}e_i`, with `0<=s<r`, lies in `2^q M`. Completeness therefore shows that the finite set

`{t^s e_i : 1<=i<=d, 0<=s<r}`

topologically generates `M` over `Z_2`. Thus `M` is finitely generated as a `Z_2`-module.

If `M` had positive `Z_2`-rank, continuity of the pro-`2` action would imply: for every `k` there is `n` such that

`omega_n M subset 2^k M`.

Then `M/omega_n M` surjects onto `M/2^kM`, whose order grows without bound with `k`, contradiction. Hence `M` is finite.

A continuous action of the pro-`2` group `Gamma_w` on the finite module `M` has an open kernel. For sufficiently large `n`, `Gamma_n` acts trivially, so

`M/omega_nM=M`.

Therefore `#M=2^m`, and the assumed cyclicity of the finite-layer coinvariant makes `M` cyclic.

At `n=0`, `M/tM` also has order `2^m=#M`. Hence `tM=0`; the full `Gamma_w` action is trivial. QED.

## 4. Exact ordinary strict `H^2` module

Put

`Z_w^str:=H^2(U_{w,infty}^{+,str})`.

At an ordinary place the protected strict local complex is the Iwasawa local cohomology complex for `T_w^+`, so

`Z_w^str=H_Iw^2(K_w,T_w^+)`.

Protected Chapter-8 descent gives

`(Z_w^str)_{Gamma_n} ~= H^2(F_n,T_w^+)`.

Apply Theorem `FINITE-H2-006` and Lemma `BOUNDED-COINV-007`.

### Theorem `BSD-A1-WP46A-ORDINARY-H2-008`

At each `w|2`,

`Z_w^str ~= Lambda_w/(2^{m_2},gamma_w-1)
          ~= Z/2^{m_2}Z`,

with trivial `Gamma_w` action.

Thus the higher strict Iwasawa local term is finite cyclic of exact length `m_2`.

This is a module-level identification; it does not yet identify `Z_w^str` with the protected formal universal-norm subgroup `F_w^norm` merely because their orders agree.

## 5. Strict and Kummer `H^1` coincide at Iwasawa level

Protected Greenberg Proposition 2.4, admitted literally at `p=2`, proves that at infinite cyclotomic level the classical Kummer condition equals the connected ordinary condition. Under the protected local duality between the discrete and compact formulations, this gives equality of the compact Iwasawa degree-one local conditions at `w|2`.

Equivalently, with the notation of WP46A,

`N_w^str=H^1(U_{w,infty}^{+,str})
 ~= M_w^Kum`.

At an odd bad place the same conclusion follows directly from the protected component-group calculation: the finite strict/Kummer quotient is supported on the finite `2`-primary component group, while the transition norm in the unramified `Z_2`-tower is eventually multiplication by `2` (and is already zero on the first nonsplit transition when relevant). Its inverse limit is therefore zero. At odd good places the finite quotient is already zero.

### Theorem `BSD-A1-WP46A-IW-H1-EQUALITY-009`

For every relevant local place,

`N_w^str ~= M_w^Kum`

canonically inside `H^1_Iw(K_w,T)`.

## 6. The Kummer local complex is the lower truncation of the strict complex

Protected WP45A constructs `U_{w,infty}^{+,Kum}` as the canonical simple local condition having exactly the submodule

`M_w^Kum subset H^1_Iw(K_w,T)`

in degree one.

By Theorem `IW-H1-EQUALITY-009`, the lower truncation of the strict local condition has the same canonical image:

`tau_{<=1}U_{w,infty}^{+,str}
 ~= M_w^Kum[-1]
 ~= U_{w,infty}^{+,Kum}`.

The identification is over the ambient local Iwasawa cochain complex, by the universal property of the fibre defining the WP45A simple local condition.

### Theorem `BSD-A1-WP46A-REVERSE-COMPARISON-010`

There is a canonical morphism of local conditions

`j_w:U_{w,infty}^{+,Kum}
     -> U_{w,infty}^{+,str}`

and an exact triangle

`U_{w,infty}^{+,Kum}
 -> U_{w,infty}^{+,str}
 -> Z_w^str[-2]
 -> U_{w,infty}^{+,Kum}[1]`.

At odd places `Z_w^str=0`, so `j_w` is an isomorphism. At `w|2` the cone is exactly the cyclic module

`Lambda_w/(2^{m_2},gamma_w-1)[-2]`.

This canonical **reverse** comparison replaces the noncanonical forward-lifting route of `01_POSTNIKOV_OBSTRUCTION_THEOREM.md`. No vanishing of the strict Postnikov class is needed to obtain it.

## 7. Vanishing of the WP45A kernel `B_w^Kum` at `w|2`

At `w|2`, apply protected Chapter-8 descent in degree one to the strict local condition. Since `Z_w^str` is `Gamma_w`-trivial, one has

`0 -> (M_w^Kum)_{Gamma_w}
   -> H^1(U_{w,0}^{+,str})
   -> Z_w^str
   -> 0`.

The first map is injective.

The WP45A map

`(M_w^Kum)_{Gamma_w}
 -> H^1(U_{w,0}^{+,Kum})=E(K_w)^hat_2`

is compatible with the finite strict-to-Kummer inclusion. Since

`H^1(U_{w,0}^{+,str}) -> H^1(U_{w,0}^{+,Kum})`

is injective by protected WP39, the composite from `(M_w^Kum)_{Gamma_w}` is injective.

### Theorem `BSD-A1-WP46A-BVANISH-011`

At each `w|2`,

`B_w^Kum=0`.

Combined with protected WP45A, the local Kummer derived-specialization sequence is therefore

`0 -> (M_w^Kum)_{Gamma_w}
   -> H^1(U_{w,0}^{+,Kum})
   -> U_w
   -> 0`.

## 8. The exact derived/control filtration of `U_w`

Protected WP39 gives the finite strict/Kummer exact sequence

`0 -> H^1(U_{w,0}^{+,str})
   -> H^1(U_{w,0}^{+,Kum})
   -> R_w
   -> 0`,

where

`R_w:=H^1(K_w,T_w^-)_tors`

has length `m_2`.

Combine this with the two exact sequences of Section 7. The identity on `(M_w^Kum)_{Gamma_w}` and the strict/Kummer inclusion give a commutative diagram with exact rows. The snake/3-by-3 lemma yields:

### Theorem `BSD-A1-WP46A-U-FILTRATION-012`

At each `w|2` there is a canonical short exact sequence

`0 -> Z_w^str
   -> U_w
   -> R_w
   -> 0`.

Every term is exact integral `2`-primary data:

`len_Z2 Z_w^str=m_2`,

`len_Z2 U_w=2m_2`,

`len_Z2 R_w=m_2`.

This is the derived-control filtration of the full universal-norm specialization defect.

Protected WP28 independently supplies

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`.

The two filtrations have matching term lengths, but WP46A does **not** identify

`Z_w^str=F_w^norm`

or

`R_w=E_tilde(F_2)`

merely from those lengths. A map-level reconciliation of the two filtrations is a separate, now very narrow obligation.

## 9. Explicit forward-lift obstruction groups, if desired

Although the canonical reverse comparison makes a forward retraction unnecessary, the obstruction groups of `01_POSTNIKOV_OBSTRUCTION_THEOREM.md` are now explicit.

Write

`a:=2^{m_2}`, `t:=gamma_w-1`,

so

`Z_w^str=Lambda_w/(a,t)`.

Protected WP45A proves `t` is injective on `M_w^Kum`.

The Koszul resolution for `(a,t)` gives

`Ext^2_{Lambda_w}(Z_w^str,M_w^Kum)
 ~= M_w^Kum/(aM_w^Kum+tM_w^Kum)`,

and

`Ext^1_{Lambda_w}(Z_w^str,M_w^Kum)
 ~= ((M_w^Kum)_{Gamma_w})[a]`.

Thus any forward strict-to-Kummer retraction would be controlled by completely explicit residue/torsion groups. No such retraction is needed for the canonical reverse triangle.

## 10. Refined D2b boundary

The abstract strict-to-Kummer Iwasawa comparison problem is closed by the canonical reverse truncation triangle. The surviving local compatibility problem is strictly narrower:

`MISSING_P2_MAP_LEVEL_RECONCILIATION_OF_STRICT_H2_AND_FORMAL_UNIVERSAL_NORM_FILTRATIONS`.

A successor must compare the two canonical short exact sequences inside the same group `U_w`:

`0 -> Z_w^str -> U_w -> R_w -> 0`

and

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`.

Only after the maps are matched may one identify the strict higher-cohomology defect with the formal universal-norm term and propagate the comparison into the global WP40/Bockstein normalization.

## Claim firewall

This strengthening does not prove:

- `Z_w^str=F_w^norm`;
- `R_w=E_tilde(F_2)` as canonically mapped groups;
- the global WP40 defect `D_K` is a Bockstein defect;
- fixed-`2` height nondegeneracy;
- D1c, D2c–D2e;
- BSD or certification.