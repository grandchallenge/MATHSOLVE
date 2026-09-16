# HC-R021-P4 — Nested standard-secanta identity and curve/divisor two-step no-go

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `9dedde7523b493ff2e731c40825c507301c3535f`  
**State:** `EXPLICIT_SECANT_QUOTIENT_IDENTITY__NATURAL_TWO_STEP_CURVE_DIVISOR_REPAIR_PRUNED`  
**Date:** 2026-09-16

## 1. Purpose

Exploit the fact that Markman Example 8.2.4 supplies an explicit genus-four secant sheaf on every ordinary secant ray

```text
beta_d^L := L-(d/6)L^3,
d in Z_(>0),
```

for a principal polarization `L` obtained from `Theta` by an automorphism.

There is an exact four-secanta identity on the RM target ray:

```text
beta'
 = 2 beta_1^D - beta_2^D
   + beta_(q+1)^H - beta_1^H.              (1.1)
```

Moreover the `F_d` of Example 8.2.4 can be chosen from nested ideal data, so each difference `beta_d^L-beta_(d+1)^L=L^3/6` is represented by an actual curve-supported quotient.

This gives a much more geometric same-ray realization than the three-divisor identity of `L025-L028`:

```text
beta' = ch(F_1^D)+ch(Q_D)-ch(Q_H),          (1.2)
```

where `Q_D` is one curve quotient of class `D^3/6` and `Q_H` is a union/successive extension of `q` curve quotients of total class `qH^3/6`.

The package determines the exact two-step obstruction geometry. If a negative curve is not contained in the positive divisor support, the mixed deformation already fails on a dense open of that curve. If it is contained, the required opposite degree-one channels exist after the parity shift, but their Yoneda product into the divisor self-`Ext^2` is zero for local complete-intersection reasons. Hence the natural two-step curve/divisor repair still cannot kill a nonzero mixed obstruction on the divisor block.

Longer complexes with more than one bridge remain open.

## 2. Standard secant blocks on D and H

Let `F_d` be Markman's Example 8.2.4 sheaf on the principally polarized genus-four Jacobian `(X,Theta)`:

```text
ch(F_d)=Theta-(d/6)Theta^3.
```

Because `g` is an automorphism and

```text
D=g^*Theta,
H=(g^-1)^*Theta,
```

define

```text
F_d^D := g^*F_d,
F_d^H := (g^-1)^*F_d.
```

Then

```text
ch(F_d^D)=D-(d/6)D^3=:beta_d^D,
ch(F_d^H)=H-(d/6)H^3=:beta_d^H.            (2.1)
```

## 3. HC-R021-L031a — exact four-secanta identity

The identities

```text
2 beta_1^D-beta_2^D=D,

beta_(q+1)^H-beta_1^H=-(q/6)H^3
```

are immediate. Therefore

```text
boxed[
 beta'
 =2 beta_1^D-beta_2^D
  +beta_(q+1)^H-beta_1^H
].                                             (3.1)
```

Thus the RM target ray admits an integral `K_0` presentation using only explicit genus-four secant sheaves from the earlier Markman construction.

This identity does not contradict `L024`: it is not an autoequivalence from a single standard secant ray. It is a virtual combination of four standard secant classes.

## 4. Nested ideal data produce actual curve quotients

In Example 8.2.4, Markman writes

```text
Z_d=W_(2,p) union C_1 union ... union C_d,
F_d=e_* I_(Z_d/Theta)(Theta),              (4.1)
```

where each `C_i` is a translate of the Abel-Jacobi curve and lies in the smooth locus of `Theta`.

Choose the data for `d=1,...,q+1` compatibly, so that the first `d` curves used for `Z_d` are retained when passing to `Z_(d+1)`. Then

```text
I_(Z_(d+1)/Theta) subset I_(Z_d/Theta),
```

hence there is an exact sequence

```text
0 -> F_(d+1) -> F_d -> Q_(d+1) -> 0.       (4.2)
```

The quotient `Q_(d+1)` is supported on the new Abel-Jacobi component `C_(d+1)` (with the finite incidence correction inherited from the other components). Its Chern character is determined by (2.1):

```text
ch(Q_(d+1))
 = ch(F_d)-ch(F_(d+1))
 = Theta^3/6.                               (4.3)
```

After pullback by `g` or `g^-1`, obtain quotient sheaves

```text
Q_D,
Q_(H,2),...,Q_(H,q+1)
```

with

```text
ch(Q_D)=D^3/6,
ch(Q_(H,j))=H^3/6.
```

Let `Q_H` denote the successive quotient `F_1^H/F_(q+1)^H`; it has a filtration with these `q` curve-supported graded pieces and

```text
ch(Q_H)=qH^3/6.                             (4.4)
```

Consequently (3.1) becomes

```text
boxed[
 beta'=ch(F_1^D)+ch(Q_D)-ch(Q_H)
].                                             (4.5)
```

This is the minimal nested-secanta form of the identity.

## 5. Mixed obstruction on the positive divisor block

The local Fitting argument of `L030` is invariant under pullback by the RM automorphism `g`: the rank-two Poisson images remain the two complementary RM planes `V_1,V_2`, and an invertible RM scaling does not make the canonical tangent curve lie in either plane.

Therefore the `D`-secant sheaf `F_1^D` cannot lift simultaneously in the two target mixed directions:

```text
not [
 ob_(F_1^D)(k_7)=0
 and
 ob_(F_1^D)(k_8)=0
].                                             (5.1)
```

Fix a nonzero mixed direction

```text
k in span(k_7,k_8)
```

for which

```text
o_D:=ob_(F_1^D)(k) !=0.                    (5.2)
```

Any extension engineering based on (4.5) must make this class a boundary.

## 6. If a negative curve is not contained in the positive divisor, local failure is immediate

Let `C` be an irreducible curve component of the support of `Q_H`. Suppose

```text
C not_subset Supp(F_1^D).
```

Then on a dense open subset of `C`, the positive divisor-supported terms `F_1^D` and `Q_D` vanish. Any perfect complex whose associated graded uses the three terms of (4.5), with the `Q_H` sector in odd `K`-parity, restricts there to a shift of the curve-supported object.

For a line bundle/torsion-free rank-one module on a smooth curve, lifting in a Poisson direction requires the curve to be coisotropic for that bivector, equivalently its tangent line to lie in the image plane of the rank-two bivector, exactly as in `L019b`.

The Abel-Jacobi tangent Gauss image is the nondegenerate canonical genus-four curve, as used in `L030`. Hence simultaneous lifting for `k_7,k_8` is impossible on this dense open.

Thus a necessary condition for a nested-secanta mixed cancellation is:

```text
every negative H-curve component must be contained
in the positive D-divisor support.            (6.1)
```

## 7. Local Ext algebra when the curve is contained in the divisor

Assume now that a smooth negative curve `C` is contained in a smooth open subset of the positive divisor `S` and avoids the singular locus of the positive secant sheaf. Near its generic point the positive sheaf is a line bundle on `S`, so line-bundle twists can be discarded from the local Ext calculation.

Let

```text
R=k[[f,g,h,w]]
```

be a regular local model for the fourfold, with

```text
A=R/(f)                         [divisor module],
B=R/(f,g,h)                     [curve module].     (7.1)
```

The negative `K`-parity of the curve can be represented by the odd shift `B[-1]`.

### 7.1 Ext from the divisor to the curve

Resolve `A` by

```text
0 -> R --f--> R -> A -> 0.
```

Because `f=0` on `B`, applying `Hom_R(-,B)` gives zero differential. Hence

```text
Ext^0_R(A,B)=B,
Ext^1_R(A,B)=B,
Ext^j_R(A,B)=0, j>=2.                    (7.2)
```

### 7.2 Ext from the curve to the divisor

Resolve `B` by the Koszul complex on `(f,g,h)`. After applying `Hom_R(-,A)`, the `f`-Koszul differential is zero while `(g,h)` remains a regular sequence on `A`. Therefore

```text
Ext^2_R(B,A)=B,
Ext^3_R(B,A)=B,
Ext^j_R(B,A)=0 for j notin {2,3}.         (7.3)
```

### 7.3 The shifted degree-one channels

For `B[-1]`, the two opposite degree-one morphism spaces include

```text
Hom^1(A,B[-1]) = Ext^0_R(A,B)=B,
Hom^1(B[-1],A) = Ext^2_R(B,A)=B.          (7.4)
```

Thus containment really does create the opposite twisting channels that were absent in the definite divisor-block calculation of `L026`.

## 8. The opposite product cannot hit the divisor obstruction

Despite (7.4), the two-step factorization required by `L021` still fails.

The divisor module `A=R/(f)` has projective dimension one. Therefore

```text
Ext^j_R(A,A)=0 for j>=2                  (8.1)
```

as a local/sheaf-Ext statement.

Take

```text
e in Hom^1(B[-1],A)=Ext^2(B,A),
c in Hom^1(A,B[-1])=Hom(A,B).
```

Their composition on the divisor side is a degree-two class

```text
e c in Ext^2_R(A,A).
```

By (8.1),

```text
e c=0.                                   (8.2)
```

The same conclusion holds sheaf-theoretically along the generic curve: `e` lies in the local `mathcal Ext^2(B,A)` piece and multiplication by the filtration-zero morphism `c` maps to `mathcal Ext^2(A,A)=0`.

Consequently these opposite channels cannot reproduce a nonzero diagonal divisor obstruction such as (5.2).

### HC-R021-L031b — contained curve/divisor factorization no-go

For a smooth curve contained in the smooth locus of a divisor, with the curve placed in the odd shift required by a negative `K`-class, the natural opposite degree-one channels exist but their Yoneda product into the divisor self-`Ext^2` is zero. Hence they cannot satisfy the `L021` factorization condition for a nonzero divisor obstruction.

## 9. HC-R021-L031 — natural nested-secanta two-step lane is pruned

### Statement

The target class admits the explicit nested-secanta presentation

```text
beta'=ch(F_1^D)+ch(Q_D)-ch(Q_H).
```

However, no **two-step** repair in which the negative `Q_H` curve sector is used directly to cancel the nonzero mixed obstruction of the positive divisor-supported secant block can succeed:

1. if a negative curve component is not contained in the positive divisor, mixed lifting fails locally on a dense open of that curve;
2. if it is contained, the required opposite shifted degree-one channels exist but their product into the divisor self-`Ext^2` vanishes locally and cannot factor the nonzero diagonal divisor obstruction.

Therefore the first viable use of the identity (4.5) must be genuinely longer than a single curve/divisor extension. It must introduce at least one additional bridge through which a degree-two divisor obstruction can be represented by a nonzero composite.

### Proof

Sections 3-8.

QED.

## 10. Structural lesson

`L025-L028` showed that same-parity divisor geometry lacks the needed index-two bridge. `L031` shows the complementary failure mode:

```text
curve in odd parity + divisor in even parity
```

can expose an `Ext^2(B,A)` / `Hom(A,B)` pair, but the divisor's codimension-one projective dimension forces their direct product to zero.

A successful complex must therefore contain a **third object** `T` which changes the local Ext amplitude. Schematically the mixed nullhomotopy must be able to use a path such as

```text
A -> T -> B[-1] -> A
```

or the reverse, rather than a direct two-object factorization.

The shortest promising choices for `T` are codimension-two complete-intersection objects: their self and cross Koszul algebras possess genuine degree-two wedge products unavailable for a Cartier divisor alone.

## 11. Scope and firewall

`L031` does **not** rule out:

- a three-step or longer complex built from the nested secant quotients;
- a codimension-two bridge object;
- a higher-rank bridge;
- a perfect complex on the same virtual class with different cohomology sheaves;
- second-factor rank `20`;
- all-orders algebraicity transport;
- `HC-R021`;
- the Hodge conjecture.

It closes the natural two-step realization of the exact standard-secanta identity.

## 12. Current disposition

```text
HC-R021-L031 = proved_in_solve_package_not_certified
four_standard_secant_beta_prime_identity = proved
nested_secant_curve_quotients = available
beta_prime_nested_form = F1_D_plus_QD_minus_QH
negative_curve_outside_D_support = local_mixed_failure
negative_curve_inside_D_support = opposite_shifted_channels_exist
contained_curve_to_divisor_Yoneda_product = zero
natural_two_step_nested_secant_rank20 = impossible
minimum_new_bridge_length = at_least_three_objects
codimension2_bridge = highest_value_next_lane
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 13. Inputs and sources

- Eyal Markman, arXiv:2502.03415v2, Example 8.2.4;
- `HC-R021-L006`, `L019`, `L021`, `L024`, `L030`;
- Koszul resolutions of a Cartier divisor and a codimension-three complete-intersection curve in a smooth fourfold;
- standard local-to-global/sheaf-Ext multiplicative filtration.
