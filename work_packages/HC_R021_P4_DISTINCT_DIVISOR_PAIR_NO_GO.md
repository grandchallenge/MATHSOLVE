# HC-R021-P4 — Distinct divisors cannot provide a pairwise scalar bridge

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `34be5e32df8767d9463c2ceae3bd481547e5bb82`  
**State:** `DISTINCT_PURE_DIVISOR_PAIRWISE_YONEDA_PRODUCT_ZERO__SAME_SUPPORT_OR_HIGHER_BRIDGE_REQUIRED`  
**Date:** 2026-09-16

## 1. Purpose

Continue the scalar-channel analysis after `HC-R021-L033`.

`L033` proves that a lower-dimensional bridge cannot hit the filtration-zero `H^2(mathcal End A)` part of the self-`Ext^2` of a projective-dimension-one divisor constituent. The next natural possibility is a second divisor constituent, because a same-dimensional object can in principle have sheaf-Hom in both directions and hence contribute Cech degree to a scalar `H^2` product.

This package separates two cases.

- If the two divisor supports are distinct, purity forces both cross sheaf-Hom groups to vanish. The two opposite `Ext^1` classes are then forced into local-Ext degree one, and their Yoneda product is globally zero by the multiplicative filtration.
- If the supports coincide, cross sheaf-Hom can survive and the argument below no longer applies. This same-support case is the only remaining direct two-divisor scalar mechanism.

## 2. Setup

Let `X` be a smooth projective fourfold. Let

```text
A,
B
```

be coherent sheaves satisfying:

1. `A` is pure/torsion-free of positive rank on an effective Cartier divisor `S`;
2. `B` is pure/torsion-free of positive rank on an effective Cartier divisor `T`;
3. `S` and `T` are distinct irreducible divisors;
4. both objects have ambient projective dimension one at the generic points relevant to the product calculation.

The standard smooth-divisor line bundles and maximal Cohen-Macaulay hypersurface modules used in the current campaign satisfy these hypotheses on the required open sets.

## 3. Cross sheaf-Hom vanishes in both directions

Any morphism

```text
A -> B
```

has image supported on

```text
S intersect T,
```

which is a proper closed subset of `T`. Since `B` is pure of dimension three, it has no nonzero subsheaf supported in dimension at most two. Hence

```text
mathcal Hom_X(A,B)=0.                     (3.1)
```

Interchanging `A,B` gives

```text
mathcal Hom_X(B,A)=0.                     (3.2)
```

This is the key difference from two objects on the same divisor support.

## 4. Cross Ext1 is forced into local-Ext degree one

The local-to-global spectral sequence for `Ext^1_X(A,B)` has possible total-degree-one pieces

```text
H^1(mathcal Hom(A,B)),
H^0(mathcal Ext^1(A,B)).
```

The first vanishes by (3.1), so every class in

```text
Ext^1_X(A,B)
```

has local-Ext filtration at least one. Under the projective-dimension-one hypothesis there is no higher sheaf-Ext contribution to total degree one, so the associated graded is entirely

```text
H^0(mathcal Ext^1(A,B)).                  (4.1)
```

Likewise every class in

```text
Ext^1_X(B,A)
```

has local-Ext filtration at least one.      (4.2)

Geometrically these classes live on the codimension-two intersection `S cap T`.

## 5. The opposite Yoneda products vanish globally

Take

```text
e in Ext^1_X(B,A),
c in Ext^1_X(A,B).
```

The local-to-global spectral sequence is multiplicative. By Section 4, both classes have local-Ext filtration at least one. Hence their product has filtration at least two:

```text
F^2_local (e c) = e c
```

inside

```text
Ext^2_X(A,A).                              (5.1)
```

But `A` has ambient projective dimension one, so

```text
mathcal Ext^q_X(A,A)=0, q>=2.
```

Therefore the local-Ext filtration on `Ext^2_X(A,A)` has only the pieces

```text
q=0: H^2(mathcal End A),
q=1: H^1(mathcal Ext^1(A,A)),
```

and

```text
F^2_local Ext^2_X(A,A)=0.                 (5.2)
```

Combining (5.1)-(5.2),

```text
e c=0.                                    (5.3)
```

The reverse product is identical:

```text
c e=0 in Ext^2_X(B,B).                    (5.4)
```

Thus the vanishing is global. It does not rely on choosing a transverse local coordinate model and is not repaired by Cech degree.

### HC-R021-L034a — distinct-divisor pairwise product no-go

For pure projective-dimension-one sheaves on distinct irreducible Cartier divisors, every pair of opposite degree-one extension classes has zero diagonal Yoneda products in both directions.

## 6. Consequence for the L021 factorization criterion

`HC-R021-L021` gives the necessary condition for a two-step filtered object to kill nonzero diagonal degree-two obstructions:

```text
e c=o_A,
c e=o_B
```

up to the fixed enhancement signs.

For distinct divisor supports, `L034a` gives

```text
e c=c e=0
```

for every possible opposite degree-one pair. Therefore a two-step extension between such constituents cannot kill any nonzero diagonal obstruction on either graded divisor block.

This closes the direct second-**distinct-divisor** scalar bridge.

## 7. The same-support case is genuinely different

If `A` and `B` are supported on the same divisor `S`, equations (3.1)-(3.2) need not hold. Cross sheaf-Hom can be nonzero, and the local-to-global products can have the bidegree pattern

```text
H^1(mathcal Hom(A,B))
 x
H^1(mathcal Hom(B,A))
 ->
H^2(mathcal End(A)).                      (7.1)
```

This is precisely the scalar filtration-zero channel excluded in `L033-L034` for lower-dimensional or distinct-support bridges.

`HC-R021-L021` already prunes generic Picard-zero line-bundle extensions and identical self-extensions on one smooth divisor. It does **not** rule out general same-support higher-rank or non-isomorphic graded pieces whose cross-Hom cohomology and composition pairing are nontrivial.

Thus the only surviving direct pairwise scalar mechanism is:

```text
same divisor support
+ nontrivial cross sheaf-Hom in both directions
+ H^1 x H^1 -> H^2 composition capable of matching the mixed scalar classes.
```

## 8. HC-R021-L034 — distinct-divisor bridge closure

### Statement

Let `A,B` be pure positive-rank projective-dimension-one constituents on distinct irreducible Cartier divisors of the source fourfold. Then every direct opposite degree-one Yoneda pair satisfies

```text
e c=0,
c e=0.
```

Hence no two-step extension between distinct divisor supports can factor a nonzero diagonal ambient obstruction as required by `L021`.

The surviving direct scalar lane is restricted to same-support divisorial data; otherwise one needs a genuinely higher filtered/Massey mechanism.

### Proof

Sections 3-7.

QED.

## 9. Scope and firewall

`L034` does **not** rule out:

- two non-isomorphic constituents on the same divisor support;
- higher-rank same-support bundles;
- a longer complex using multiple divisor supports and higher products;
- a divisor/surface/curve Massey mechanism;
- a constituent of ambient projective dimension greater than one;
- second-factor rank `20`;
- all-orders algebraicity transport;
- `HC-R021`;
- the Hodge conjecture.

## 10. Current disposition

```text
HC-R021-L034 = proved_in_solve_package_not_certified
distinct_divisor_cross_Hom = zero
distinct_divisor_opposite_Ext1_product = zero
distinct_divisor_two_step_scalar_bridge = impossible
same_support_divisor_scalar_bridge = open
higher_filtered_bridge = open
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 11. Inputs

- `HC-R021-L021`, `L023`, `L033`;
- purity of torsion-free sheaves on irreducible divisors;
- multiplicative local-to-global Ext spectral sequence;
- ambient projective-dimension-one property for hypersurface modules.