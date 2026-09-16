# HC-R021-P4 — Normal-bundle correction and the genus-four W2 Schottky obstruction

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `e8bdfccb3600f89a13cff4a3b75656ebe85f6e27`  
**State:** `W2_IDEAL_HAS_ONE_EXTRA_PPAV_SCHOTTKY_OBSTRUCTION__PARTIAL_NORMALIZATION_POINT_CANCELLATION_REDUCED`  
**Date:** 2026-09-16

## 1. Purpose

Refine the reopened full-support lane after `L039-L040`.

There are two tasks.

First, correct the globalization of the affine self-Ext calculation in `L039`: for a smooth codimension-two embedding the local rank-two module written as `I/I^2` globalizes as the **normal bundle**, not the conormal bundle.

Second, identify a concrete genus-four obstruction which is invisible to the Chern-character contraction. For the Abel-Jacobi surface `W_2(C)` in a non-hyperelliptic genus-four Jacobian, a polarization-preserving deformation of the ppav which is transverse to the Jacobian locus preserves the Hodge class of the principal polarization but cannot carry `W_2`. Hence the corresponding ideal sheaf has a nonzero object obstruction in a contraction-kernel direction.

This is the one-dimensional infinitesimal Schottky defect absent from the genus-three secant proof.

## 2. Correct global self-Ext sheaves for a codimension-two ideal

Let

```text
i:S -> X
```

be a smooth regular embedding of codimension two and let

```text
I:=I_S.
```

Locally `I=(f,g)` and has the free resolution used in `L039`:

```text
0 -> O_X -> O_X^2 -> I -> 0.               (2.1)
```

The affine calculation gives a rank-two `O_S`-module in `Ext^1`. Under a change of local generators of the ideal, however, this module transforms contragrediently to `I/I^2`. The invariant global identification is

```text
mathcal Ext^1_X(I,I) ~= N_(S/X),            (2.2)
```

where

```text
N_(S/X):=Hom(I/I^2,O_S).
```

Moreover

```text
mathcal Hom_X(I,I) ~= O_X,
mathcal Ext^j_X(I,I)=0, j>=2.               (2.3)
```

Thus the local-to-global spectral sequence for total degree two has only the two potentially nonzero associated-graded pieces

```text
H^2(X,O_X),
H^1(S,N_(S/X)).                             (2.4)
```

### HC-R021-L041a — correction to L039

Where `L039` wrote `mathcal Ext^1(I,I)=I/I^2` and `H^1(I/I^2)`, replace those global expressions by

```text
mathcal Ext^1(I,I)=N_(S/X),
H^1(S,N_(S/X)).                             (2.5)
```

The local statement `Ext^2_R(I,I)=0`, the withdrawal of `L038`, and the reopening of the full-support route are unchanged.

## 3. The single W2 ideal has pure-spinor Chern character

Let `C` be a smooth non-hyperelliptic genus-four curve,

```text
X=J(C),
S=W_2(C) subset X,
Theta = principal polarization.
```

Markman records

```text
ch(O_S)
 = Theta^2/2 - Theta^3/3 + 3[pt],           (3.1)
```

with

```text
[pt]=Theta^4/24.
```

Multiplying

```text
ch(I_S(Theta))=(1-ch(O_S)) exp(Theta)
```

and truncating in complex dimension four gives the exact cancellation

```text
boxed[ ch(I_S(Theta)) = 1+Theta ].           (3.2)
```

This is an even pure-spinor class. In particular every first-order commutative deformation preserving the principal polarization lies in the contraction kernel of (3.2).

## 4. The ten-dimensional ppav tangent kernel

For a principally polarized abelian fourfold, the tangent space to the moduli of ppavs has dimension

```text
dim A_4 = 4*5/2 = 10.                      (4.1)
```

Inside the commutative Hochschild sector

```text
H^1(X,T_X),
```

these are precisely the first-order complex-structure deformations for which the fixed principal-polarization class remains of type `(1,1)`.

Because (3.2) depends only on `1` and `Theta`, all ten directions annihilate the Chern character:

```text
T_(X,Theta) A_4
 subset ker(c_(1+Theta)).                   (4.2)
```

## 5. W2 deforms only along the Jacobian locus

Use Lombardi-Tirabassi, *Deformations of minimal cohomology classes on abelian varieties*, arXiv:1410.7986.

For a smooth non-hyperelliptic curve of genus `g>=3` and `1<=d<g-1`, their Theorem 1.1 identifies the deformation functor of `W_d` with that of the curve. Their Theorem 1.4 and Corollary 1.5 identify simultaneous infinitesimal deformations of the embedding

```text
W_d -> J(C)
```

with deformations of `C`; in particular, an infinitesimal deformation of the Jacobian together with `W_d` remains tangent to the Jacobian locus.

For

```text
g=4,
d=2,
```

the deformation space has dimension

```text
3g-3=9.                                    (5.1)
```

The Jacobian locus in `A_4` is therefore infinitesimally codimension one at the selected non-hyperelliptic Jacobian:

```text
dim T_J J_4 = 9,
dim T_J A_4 = 10.                           (5.2)
```

Choose a polarization-preserving first-order deformation

```text
xi_Sch in T_J A_4 \ T_J J_4.               (5.3)
```

Then `W_2` does not admit a simultaneous embedded deformation in direction `xi_Sch`.

## 6. From a rank-one ideal-sheaf lift to an embedded support deformation

Let

```text
F:=I_S(Theta).
```

Suppose, for contradiction, that the object obstruction vanishes:

```text
ob_F(xi_Sch)=0.                             (6.1)
```

Then `F` has a flat first-order coherent lift `F_A` on the corresponding commutative deformation `X_A` of `X`.

Because `xi_Sch` is a ppav direction, `Theta` has a line-bundle lift `Theta_A`. Untwist:

```text
G_A:=F_A tensor Theta_A^(-1).               (6.2)
```

The special fiber is the rank-one torsion-free sheaf `I_S` with trivial determinant.

For a rank-one torsion-free sheaf on a smooth family, the reflexive hull is a line bundle. Let

```text
L_A:=G_A^{**}.
```

It specializes to `O_X`. After tensoring by `L_A^{-1}`, we may assume the reflexive hull is `O_(X_A)`. The canonical map to the double dual then gives

```text
0 -> G_A -> O_(X_A) -> O_(S_A) -> 0.       (6.3)
```

The first two terms are flat over the dual numbers and the special-fiber map is injective, so the quotient is flat by the local flatness criterion. Hence `S_A` is an embedded first-order deformation of `S=W_2` inside `X_A`.

This contradicts (5.3) and Lombardi-Tirabassi.

Therefore

```text
boxed[ ob_F(xi_Sch) != 0 ].                 (6.4)
```

## 7. HC-R021-L041 — the one-dimensional Schottky defect

### Statement

For

```text
F=I_(W_2)(Theta)
```

on the selected non-hyperelliptic genus-four Jacobian:

1. the ten-dimensional ppav tangent space lies in the commutative contraction kernel of `ch(F)=1+Theta`;
2. only the nine-dimensional Jacobian tangent subspace can deform the pair `(X,W_2)`;
3. every ppav direction transverse to the Jacobian locus has nonzero object obstruction for `F`.

Hence the object obstruction map of `F` has at least one additional commutative obstruction direction which is invisible to its Chern-character contraction.

This is the infinitesimal genus-four Schottky defect.

### Proof

Sections 3-6.

QED.

## 8. Why this matters for Markman's genus-four secant ideal

Example 8.2.3 constructs the coherent secant ideal

```text
F_d=I_Z(Theta)
```

from `d+1` translates of `W_2` plus zero-dimensional corrections. Markman explicitly notes that these sheaves are unlikely to be semiregular.

`L041` identifies the geometric source of a defect which is absent from the genus-three proof: already one `W_2` building block cannot follow the unique ppav-normal Schottky direction while its Chern character can.

A separate argument is still required to show that the same one-dimensional obstruction survives unchanged for the *union* ideal `I_Z(Theta)`. Intersections and point corrections may affect the global `Ext^2` class. We therefore do not yet assert

```text
rank(ob_(F_d)) >= 13.
```

for every `d`.

## 9. Reduction for the partial-normalization object

Markman's alternative object

```text
F'=[O_X -> nu_*O_(Z_tilde)]
```

has the same Chern character as `F_d`, but its cohomology differs at the finitely many partial-normalization points. With `O_X` in degree zero, there is a truncation triangle

```text
I_Z -> F' -> Q[-1] -> I_Z[1],              (9.1)
```

where

```text
Q:=nu_*O_(Z_tilde)/O_Z
```

is finite-length and supported exactly at the normalized intersection points.

Consequently the only way in which `F'` can cancel a Schottky obstruction present on the coherent ideal sector is through the extension/conductor data of (9.1).

Writing the triangle as a two-step filtered object, the extension class has type

```text
e in Ext^2_X(Q,I_Z).                        (9.2)
```

The opposite degree-one class in the shifted two-step formalism is equivalently

```text
c in Hom_X(I_Z,Q).                          (9.3)
```

The `I_Z` diagonal obstruction can be killed only if the corresponding Yoneda composition satisfies

```text
e c = o_Sch                                (9.4)
```

up to the enhancement sign convention; the `Q`-side composition must match the point-sector obstruction.

Thus the broad semiregularity question has a finite next target:

```text
PN-SCHOTTKY-A1:
  compute the conductor pairing
  Ext^2(Q,I_Z) x Hom(I_Z,Q) -> Ext^2(I_Z,I_Z)
  on the Schottky-normal obstruction line.
```

## 10. Current disposition

```text
HC-R021-L041 = proved_in_solve_package_not_certified
L039_global_Ext1_conormal_notation = corrected_to_normal_bundle
single_W2_ppav_kernel_dimension = 10
single_W2_embedded_pair_deformation_dimension = 9
single_W2_Schottky_extra_obstruction = nonzero
coherent_union_Fd_rank_at_least_13 = open
partial_normalization_Schottky_cancellation = open
PN-SCHOTTKY-A1 = next_finite_calculation
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 11. Sources and inputs

- `HC-R021-L039`, `L040`;
- Eyal Markman, arXiv:2502.03415v2, Example 8.2.3 and Lemma 8.2.5;
- Luigi Lombardi and Sofia Tirabassi, arXiv:1410.7986, Theorem 1.1, Theorem 1.4, Corollary 1.5;
- standard deformation theory of rank-one torsion-free sheaves with fixed determinant and ideal sheaves;
- local-to-global Ext spectral sequence for a regular codimension-two embedding.
