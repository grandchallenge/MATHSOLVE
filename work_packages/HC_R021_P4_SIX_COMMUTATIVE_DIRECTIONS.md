# HC-R021-P4 — Six ordinary simultaneous-polarization directions

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `20358ac7630b4c9a6033e352a3a9a425f82bd3fb`  
**State:** `SIX_COMMUTATIVE_DIRECTIONS_IDENTIFIED__OBJECT_LIFTING_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Give a geometric interpretation of the six `H^1(T_X)` generators `k_1,...,k_6` in the eight-dimensional contraction kernel computed by `HC-R021-L006`.

The result separates the `D20` problem into:

- six ordinary commutative deformation directions preserving two polarization classes simultaneously; and
- two genuinely mixed `H^2(O_X) + H^0(Lambda^2 T_X)` directions.

The identification does not by itself prove that an admissible gluing deforms in those six directions.

## 2. First-order Hodge locus of an ample class

Let `L` be an ample `(1,1)` class on the abelian fourfold `X`.

For a Kodaira-Spencer class

```text
xi in H^1(T_X),
```

the first-order variation of the `(1,1)` condition for `L` is represented by

```text
xi contraction L in H^2(O_X).
```

Hence the tangent space to the local Hodge locus of `L` is

```text
T_Hdg(L) = ker[H^1(T_X) -> H^2(O_X), xi |-> xi contraction L].
```

Because `L` is a polarization on a fourfold, this kernel has dimension `10`.

## 3. Degree-six contraction has the same kernel

For `xi in H^1(T_X)`, the derivation rule gives

```text
xi contraction L^3 = 3 (xi contraction L) L^2.
```

Hard Lefschetz for the ample class `L` gives an isomorphism

```text
L^2 cup (bullet) : H^2(O_X) -> H^4(Omega_X^2).
```

Therefore

```text
ker(xi |-> xi contraction L^3)
 = ker(xi |-> xi contraction L)
 = T_Hdg(L).
```

Thus no extra first-order directions are introduced by using the complementary-degree class `L^3` instead of `L`.

## 4. Apply to the CM4 secant class

Set

```text
D := g^*Theta,
H := (g^-1)^*Theta,
beta' := D - (q/6)H^3.
```

On the summand `H^1(T_X)` of `HT^2(X)`, contraction with `beta'` lands in the direct sum of two distinct Hodge-degree targets:

```text
H^2(O_X) direct_sum H^4(Omega_X^2).
```

Consequently

```text
xi contraction beta' = 0
```

if and only if both

```text
xi contraction D = 0
```

and

```text
xi contraction H^3 = 0.
```

By Section 3 this is equivalent to

```text
xi contraction D = 0,
xi contraction H = 0.
```

Hence

```text
ker(c_beta' | H^1(T_X))
 = T_Hdg(D) intersect T_Hdg(H).
```

`HC-R021-L006` computes this intersection explicitly and proves that it is six-dimensional, with basis

```text
k_1 = y_1 wedge t_1,
k_2 = y_2 wedge t_2,
k_3 = y_1 wedge t_2 + y_2 wedge t_1,
k_4 = y_3 wedge t_3,
k_5 = y_4 wedge t_4,
k_6 = y_3 wedge t_4 + y_4 wedge t_3.
```

## 5. HC-R021-L013 — geometric meaning of k1,...,k6

### Statement

The six-dimensional `H^1(T_X)` part of `ker(c_beta')` is exactly the simultaneous first-order Hodge locus of the two integral ample classes `D` and `H`:

```text
span(k_1,...,k_6)
 = T_Hdg(D) intersect T_Hdg(H).
```

In particular these six directions are ordinary commutative deformations of the abelian variety along which both polarization classes remain of type `(1,1)` to first order.

### Proof

Sections 2-4, together with the explicit kernel computation of `HC-R021-L006`.

QED.

## 6. Relation to the real-multiplication deformation space

The source datum satisfies

```text
D = g^*Theta,
H = (g^-1)^*Theta
```

with `g` induced by a norm-one unit in the real-quadratic multiplication algebra. The dimension-six simultaneous-polarization tangent space is therefore the expected local commutative deformation space compatible with the two RM-related polarization classes.

This observation is used only as geometric guidance here. A later package must bind the exact PEL/moduli carrier before identifying this tangent space globally with a named RM moduli space.

## 7. What remains object-specific

For an admissible gluing `E`, `HC-R021-L007` still requires

```text
ev_E(k_i)=0,  i=1,...,6.
```

The fact that `D` and `H` stay Hodge does not imply that the sheaf `E` deforms: its secant constituents, correction curve, line bundle, and gluing maps must deform compatibly.

Accordingly `L013` is not a proof of six of the eight Yoneda relations. It identifies the precise relative-geometric construction that would prove them:

> construct the admissible gluing family relatively over the simultaneous `D,H` Hodge locus and show the chosen point admits liftings in all six tangent directions.

The remaining two kernel generators

```text
k_7,
k_8
```

mix `H^2(O_X)` with `H^0(Lambda^2 T_X)` and are not ordinary Kodaira-Spencer directions. They require the genuinely gerby/noncommutative part of the Hochschild deformation theory.

## 8. Refined D20 attack

A positive direct-route proof can now be divided into two independent tests:

```text
A0d-COMM:
  prove ev_E(k_1)=...=ev_E(k_6)=0
  by a relative commutative construction over T_Hdg(D) intersect T_Hdg(H);

A0d-MIXED:
  prove ev_E(k_7)=ev_E(k_8)=0
  by an object-level generalized-deformation calculation.
```

A failure in either tranche refutes the chosen object as a point of `D20`.

## 9. Claim boundary

```text
HC-R021-L013 = proved_in_solve_package_not_certified
commutative_contraction_kernel_dimension = 6
commutative_kernel = simultaneous_D_H_Hodge_tangent
six_object_level_Yoneda_relations = open
two_mixed_Yoneda_relations = open
D20_nonempty = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 10. Sources

- Eyal Markman, arXiv:2509.23079, Corollary 11.2.6 and Example 11.2.7.
- `work_packages/HC_R021_P4_CONTRACTION_RANK.md` (`HC-R021-L006`).
- standard first-order variation of Hodge type and Hard Lefschetz for ample classes on abelian varieties.
