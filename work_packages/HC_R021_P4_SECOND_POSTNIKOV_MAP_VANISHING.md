# HC-R021-P4 — Vanishing of the second Postnikov obstruction

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `7e691c7d84604469437f25df2e6a92d7ec3d6ab4`  
**State:** `SECOND_POSTNIKOV_MAP_ZERO__M_CHANNEL_SURVIVAL_REDUCED_EXACTLY_TO_KERNEL_MU_M`  
**Date:** 2026-09-17

## 1. Purpose

Continue `HC-R021-L054`.

There the genuinely derived second residue was reduced to

```text
s in H^0(C,M)=ker(mu_M)
```

and the remaining obstruction was the canonical map

```text
psi:
H^0(C,M) -> V_next,

V_next
 := Coker[
      Ext^2(B,O(-D)) -> Ext^2(B,E)
    ],
```

induced by the theta-square morphism

```text
e:E^vee -> E.
```

The present package proves that this map vanishes identically.

## 2. Setup

Retain

```text
C = D cap H cap A,
E = I_C(D),
B = O_(2D)(D),
M = H+A-D.
```

The corrected cone is

```text
C_corr = Cone(e:E^vee -> E).
```

From `L047-L048`, the theta-square morphism is not an arbitrary lift of the section `t^2`. Let

```text
s:O_X -> E,
1 |-> t,
```

where `t` is the theta section cutting out `D`. Then

```text
e = s o s^vee.                                      (2.1)
```

Equivalently,

```text
E^vee --s^vee--> O_X --s--> E.                     (2.2)
```

This factorization is global.

## 3. The induced Ext^2 map factors through Ext^2(B,O_X)

Apply `Ext^2(B,-)` to (2.2). The map appearing after `L054` factors as

```text
Ext^2(B,E^vee)
  -> Ext^2(B,O_X)
  -> Ext^2(B,E).                                     (3.1)
```

Thus it is enough to compute the middle group.

## 4. Exact vanishing of Ext^2(B,O_X)

The ordinary double-theta block has the locally free resolution

```text
0 -> O(-D) --t^2--> O(D) -> B -> 0.                (4.1)
```

Dualizing gives

```text
RHom(B,O_X)
 ~= [ O(-D) --t^2--> O(D) ]
```

with the two displayed terms in cohomological degrees `0,1`. Equivalently,

```text
RHom(B,O_X) ~= B[-1].                                (4.2)
```

Therefore

```text
Ext^2(B,O_X) ~= H^1(X,B).                            (4.3)
```

Now use (4.1). Since `D` is a principal polarization on the abelian fourfold,

```text
H^i(X,O(D))=0 for i>0,
H^i(X,O(-D))=0 for i<4.                              (4.4)
```

The long exact sequence of cohomology of (4.1) gives

```text
H^1(X,B)=0.                                          (4.5)
```

Hence

```text
boxed:
Ext^2_X(B,O_X)=0.                                    (4.6)
```

## 5. HC-R021-L055 — the second Postnikov map vanishes

By (3.1) and (4.6),

```text
Ext^2(B,E^vee) -> Ext^2(B,E)
```

is the zero map. Consequently its induced quotient map from `L054` is also zero:

```text
boxed:
psi = 0.                                             (5.1)
```

Thus

```text
ker(mu_M) cap ker(psi)
 = ker(mu_M).                                        (5.2)
```

There is no second Postnikov obstruction beyond the fixed-scale matrix `mu_M`.

## 6. Exact consequence for the global extension channel

From `L054` there is a localizable surjection

```text
Ext^2(B,E^vee) ->> H^0(C,M)=ker(mu_M).
```

From the long exact sequence associated to

```text
E^vee -> E -> C_corr -> E^vee[1],
```

and the vanishing established above, every class of `Ext^2(B,E^vee)` lifts to

```text
Ext^1(B,C_corr).
```

Therefore

```text
ker(mu_M)=0
=> no genuinely derived second residue
=> co-supported escape closes;

ker(mu_M)!=0
=> a genuinely derived global extension class with nonzero generic residue exists.
                                                               (6.1)
```

The remaining rank-two question is therefore no longer a Postnikov-survival problem. It is exactly whether `mu_M` has nonzero kernel, followed by comparison of the resulting residue with the ordinary theta-square residue and construction of the required opposite extension/homotopy.

## 7. Next smallest obligation

The unique next algebraic gate is

```text
mu_M:
H^2(A-2D) direct_sum H^2(H-2D)
 ->
H^2(H+A-2D) direct_sum H^2(A-D) direct_sum H^2(H-D),

mu_M(x,y)
 = (-h cup x - a_sec cup y,
     t cup x,
     t cup y).
```

By `L053`,

```text
H^0(C,M)=ker(mu_M).
```

Hence the co-supported lane now has the exact dichotomy

```text
mu_M injective
=> co-supported escape closes;

ker(mu_M) != 0
=> the derived second channel globalizes through both Postnikov stages.
                                                               (7.1)
```

No maximal-rank statement for `mu_M` is asserted here.

## 8. Claim boundary

```text
HC-R021-L055 = proved_in_solve_package_not_certified
theta_square_factorization = Edual_to_O_to_E
Ext2_B_O = zero
Ext2_B_Edual_to_Ext2_B_E = zero
second_postnikov_map_psi = zero
postnikov_survival_condition = exactly_ker_mu_M_nonzero
mu_M_rank = open
generic_residue_independence_from_ordinary_channel = open
opposite_extension_factorization = open
global_Ext1_residue_rank = open
cosupported_global_extension_rank2 = open
second_factor_rank20 = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

This is a Solve-package result and not a MATHCERT disposition.

## 9. Inputs

- `HC-R021-L047`: canonical theta-square morphism;
- `HC-R021-L048`: exact global factorization `e=s o s^vee`;
- `HC-R021-L053`: `H^0(C,M)=ker(mu_M)`;
- `HC-R021-L054`: first Postnikov boundary `delta_0=0` and definition of `psi`;
- the index theorem for the principal polarization `D` on the abelian fourfold.
