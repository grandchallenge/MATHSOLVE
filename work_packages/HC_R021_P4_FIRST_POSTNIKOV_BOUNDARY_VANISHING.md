# HC-R021-P4 — Vanishing of the first Postnikov boundary

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `a71b656d7a53c01ec3c1f452be5cad359e961890`  
**State:** `M_CHANNEL_SURVIVES_FIRST_POSTNIKOV_BOUNDARY__NEXT_K_INVARIANT_OPEN`  
**Date:** 2026-09-17

## 1. Purpose

Continue `HC-R021-L053` from the exact sequence

```text
Ext^2(B,O(-D))
 -> Ext^2(B,E^vee)
 -> Hom(B,G)
 --delta_0--> Ext^3(B,O(-D)),
```

where

```text
B = O_(2D)(D),
E = I_C(D),
G = O_C(H+A),
Hom(B,G) = H^0(C,M),
M = H+A-D.
```

`L053` showed that a genuinely derived second generic residue must first lie in

```text
H^0(C,M)=ker(mu_M).
```

The remaining question at that stage was whether such a class survives the first connecting map `delta_0`.

The answer is exact:

```text
delta_0 = 0.
```

Thus every class in `ker(mu_M)` lifts through the truncation of `E^vee`. The next obstruction is not this first boundary; it is the subsequent Postnikov `k`-invariant / map to `Ext^2(B,E)`.

## 2. The truncation fundamental class

The regular codimension-three embedding

```text
C = D cap H cap A subset X
```

gives the duality triangle

```text
G[-3] -> O(-D) -> E^vee -> G[-2],                   (2.1)
```

where

```text
G=O_C(H+A).
```

Equivalently, after rotation,

```text
O(-D) -> E^vee -> G[-2]
   --epsilon--> O(-D)[1].                            (2.2)
```

The morphism `epsilon` is the twisted fundamental class of the regular embedding.

Applying `RHom(B,-)` produces

```text
delta_0:
Hom(B,G) -> Ext^3(B,O(-D)),                          (2.3)
```

and `delta_0(s)` is Yoneda composition with `epsilon`.

## 3. Serre-dual form of delta_0

Because `X` is an abelian fourfold, `K_X` is trivial. Serre duality identifies the dual of (2.3) with

```text
delta_0^vee:
Ext^1(O(-D),B) -> Ext^4(G,B),                        (3.1)
```

induced by precomposition with the fundamental class map

```text
G[-3] -> O(-D).                                      (3.2)
```

The source is immediate from the double-theta resolution:

```text
Ext^1(O(-D),B)
 = H^1(X,B(D)),
B(D)=O_(2D)(2D).                                     (3.3)
```

For the target, apply `RHom(G,-)` to

```text
0 -> O(-D) --t^2--> O(D) -> B -> 0.                 (3.4)
```

Regular-embedding duality gives

```text
mathcal Ext^3(G,O(-D)) ~= O_C,
mathcal Ext^3(G,O(D))  ~= O_C(2D),
```

and the induced map is multiplication by `t^2|_C=0`. Hence

```text
mathcal Ext^2(G,B) ~= O_C,
mathcal Ext^3(G,B) ~= O_C(2D).                       (3.5)
```

Since `C` is a curve, the local-to-global Ext spectral sequence has only one contribution to total degree four:

```text
Ext^4(G,B) ~= H^1(C,O_C(2D)).                        (3.6)
```

Under (3.3) and (3.6), the naturality of the Koszul fundamental class identifies `delta_0^vee` with the ordinary restriction map

```text
r:
H^1(O_(2D)(2D)) -> H^1(O_C(2D)).                    (3.7)
```

This identification can be checked directly on the top Koszul generator of the regular sequence `(t,h,a_sec)`.

## 4. The restriction map is zero

There is a commutative diagram of quotient sequences

```text
0 -> O --t^2--> O(2D) -> O_(2D)(2D) -> 0
|       |              |
|t^2    |id            |restriction
v       v              v
0 -> I_C(2D) -> O(2D) -> O_C(2D) -> 0.              (4.1)
```

Because `2D` is ample on the abelian fourfold,

```text
H^i(X,O(2D))=0, i>0.                                 (4.2)
```

The connecting maps in (4.1) therefore identify

```text
H^1(O_(2D)(2D)) ~= H^2(O_X),
H^1(O_C(2D))    ~= H^2(I_C(2D)).                     (4.3)
```

Under these identifications, the restriction map (3.7) is exactly

```text
H^2(t^2):
H^2(O_X) -> H^2(I_C(2D)).                            (4.4)
```

But the sheaf map in (4.4) factors as

```text
O_X --t--> O(D) --t--> I_C(2D).                     (4.5)
```

Since `D` is a principal polarization,

```text
H^2(X,O(D))=0.                                       (4.6)
```

Therefore

```text
H^2(t^2)=0,
r=0,
delta_0^vee=0,
delta_0=0.                                            (4.7)
```

QED.

## 5. HC-R021-L054 — exact consequence

The exact sequence of `L053` now shortens on the localizable quotient to a surjection

```text
Ext^2(B,E^vee) ->> Hom(B,G)
                         ~= H^0(C,M).                (5.1)
```

Modulo the positive-Cech-degree ambiguity from `Ext^2(B,O(-D))`, every section

```text
s in H^0(C,M)=ker(mu_M)
```

therefore has a lift to `Ext^2(B,E^vee)` carrying the same nonzero generic residue.

Thus:

```text
ker(mu_M)=0
=> no second generic residue
=> co-supported escape closes;

ker(mu_M)!=0
=> the M-channel survives the first Postnikov boundary,
   but must still survive the next map to Ext^2(B,E). (5.2)
```

The first Postnikov boundary cannot close a nonzero `M`-channel.

## 6. Canonical next obstruction

A lift in (5.1) is not unique: two lifts differ by the image of

```text
Ext^2(B,O(-D)).                                      (6.1)
```

The subsequent map induced by `E^vee -> E` therefore defines a canonical obstruction only after quotienting by the corresponding ambiguity in `Ext^2(B,E)`.

Set

```text
V_next
 := Coker[
      Ext^2(B,O(-D)) -> Ext^2(B,E)
    ].                                                (6.2)
```

Then the next residue-survival map is a well-defined linear map

```text
psi:
H^0(C,M)=ker(mu_M) -> V_next.                        (6.3)
```

Equivalently, using the Postnikov triangle

```text
F -> C_corr -> G[-1] -> F[1],
F=I_C(D)/t^2 O(-D),
```

`psi` is the `k`-invariant action

```text
Hom(B,G) -> Ext^2(B,F)                               (6.4)
```

viewed in the subquotient determined by (6.2).

A second global extension residue exists precisely when there is a nonzero

```text
s in ker(mu_M) cap ker(psi).                         (6.5)
```

After that, one must still verify that its actual generic residue is independent of the ordinary theta-square channel and then construct the opposite extension/homotopy required by `L049b`.

## 7. Claim boundary

```text
HC-R021-L054 = proved_in_solve_package_not_certified
first_postnikov_boundary_delta0 = zero
M_channel_lifts_to_Ext2_B_Edual = true_if_H0M_nonzero
H0M = ker(mu_M)
next_obstruction = psi_from_H0M_to_V_next
V_next = coker(Ext2(B,O(-D))->Ext2(B,E))
mu_M_rank = open
psi_rank_on_ker_mu_M = open
global_Ext1_residue_rank = open
cosupported_global_extension = open
second_factor_rank20 = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

This is a Solve-package result and not a MATHCERT disposition.

## 8. Inputs

- `HC-R021-L049`: explicit local two-channel co-supported repair;
- `HC-R021-L050`: global hyper-Ext reduction;
- `HC-R021-L053`: `M`-channel and exact fixed-scale matrix `mu_M`;
- standard regular-embedding duality, Serre duality on an abelian fourfold, and naturality of the Koszul fundamental class.
