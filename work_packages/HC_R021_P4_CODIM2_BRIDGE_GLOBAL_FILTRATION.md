# HC-R021-P4 — Global filtration barrier for a single codimension-two bridge

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `4e0121d565bb9ca6b4f85a95be0664f0cb887f12`  
**State:** `SINGLE_SURFACE_PAIR_CANNOT_REACH_DIVISOR_H2_HOM_COMPONENT__HIGHER_FLAG_REQUIRED_FOR_SCALAR_CHANNEL`  
**Date:** 2026-09-16

## 1. Purpose

Strengthen the local calculation of `HC-R021-L032` to the local-to-global filtration.

`L032` shows that a codimension-two bridge `T` has opposite degree-one channels with a divisor constituent `A`, but their stalkwise/Koszul product on the `A` side is zero because a Cartier-divisor module has no local self-`Ext^2`.

A possible concern is that a **global** `Ext^1` class can carry positive Cech/local-to-global degree and therefore could still have a nonzero product in global `Ext^2(A,A)`.

That concern is real for one of the two divisor self-`Ext^2` graded pieces, but not for the scalar piece. The multiplicative local-to-global filtration proves:

> a single lower-dimensional bridge can contribute pairwise only to positive local-Ext filtration on the divisor side. It cannot reach the `H^2(mathcal End(A))` component.

Thus a scalar/gerby divisor obstruction in filtration zero cannot be removed by one pairwise divisor/surface bridge. A successful construction must use another divisorial constituent or a genuinely higher flag/Massey mechanism.

## 2. Divisorial constituent of ambient projective dimension one

Let `X` be a smooth projective fourfold and let `A` be a coherent sheaf supported on an effective Cartier divisor `S` such that, locally on `X`,

```text
pd_X(A)=1.
```

The basic examples are:

1. `A=i_*L` for a line bundle `L` on a smooth divisor;
2. `i_*F` for a maximal Cohen-Macaulay module `F` on a hypersurface, viewed as an ambient module;
3. the divisor terms occurring in the standard two-term hypersurface resolutions used throughout `L023-L032`.

Then

```text
mathcal Ext^q_X(A,A)=0, q>=2.             (2.1)
```

The local-to-global spectral sequence

```text
E_2^(p,q)=H^p(X, mathcal Ext^q_X(A,A))
  => Ext^(p+q)_X(A,A)
```

therefore gives the degree-two filtration with associated graded pieces

```text
gr_(q=0) Ext^2(A,A) = H^2(mathcal End(A)),
gr_(q=1) Ext^2(A,A) = H^1(mathcal Ext^1(A,A)),   (2.2)
```

up to the usual extension between the two pieces. For `A=i_*L` these are the familiar

```text
H^2(S,O_S),
H^1(S,N_(S/X)).                            (2.3)
```

We call the first piece the **scalar filtration-zero component**.

## 3. A lower-dimensional bridge has no reverse Hom sheaf

Let `T` now be a coherent constituent supported on a proper closed subset

```text
Z subset S
```

of codimension at least one in `S` (hence codimension at least two in `X`). Assume `A` is torsion-free of positive rank on the generic points of `S`, as in the divisor sectors used in the campaign.

Then

```text
mathcal Hom_X(T,A)=0.                     (3.1)
```

Indeed the image of any map `T->A` would be a subsheaf of `A` supported on the proper subset `Z`, hence torsion in the pure/torsion-free divisor module `A`.

Consequently every nonzero local-to-global contribution to

```text
Ext^1_X(T,A)
```

has **positive local Ext degree**:

```text
q>=1.                                     (3.2)
```

For a regular codimension-two bridge the only degree-one contribution is the `H^0(mathcal Ext^1)` piece computed in `L032`; the formulation above also covers singular or more general lower-dimensional bridges as long as (3.1) holds.

## 4. Multiplicativity of the local-to-global filtration

Take opposite degree-one classes

```text
c in Ext^1_X(A,T),
e in Ext^1_X(T,A).
```

Resolve them with respect to the local-to-global filtrations. Every graded summand of `e` has local Ext degree at least `1` by (3.2). Every graded summand of `c` has local Ext degree at least `0`.

The Yoneda product is compatible with the multiplicative spectral sequence, so local Ext degrees add on the associated graded. Therefore every associated-graded component of

```text
e c in Ext^2_X(A,A)                       (4.1)
```

has local Ext degree at least `1`.

It follows immediately that the projection of (4.1) to the local-Ext-degree-zero piece is zero:

```text
proj_[H^2(mathcal End(A))](e c)=0.        (4.2)
```

This conclusion is independent of the shifts used to realize `c,e` as degree-one twisting morphisms: shifts change the underlying Ext degrees but do not manufacture a reverse sheaf-Hom `mathcal Hom(T,A)`.

### HC-R021-L033a — scalar filtration barrier

For a projective-dimension-one torsion-free divisor constituent `A` and a lower-dimensional bridge `T`, every pairwise opposite Yoneda product

```text
Ext^1(A,T_shift) x Ext^1(T_shift,A)
  -> Ext^2(A,A)
```

has zero projection to the filtration-zero component

```text
H^2(mathcal End(A)).
```

A nonzero scalar divisor obstruction in this component cannot be killed by one direct pairwise lower-dimensional bridge.

## 5. What a surface bridge can still hit

`L033a` does **not** force the whole product to vanish.

For a smooth divisor/surface flag, the nontrivial global pattern isolated in `L032` is

```text
H^1(mathcal Hom(A,T))
   x
H^0(mathcal Ext^1(T,A))
   ->
H^1(mathcal Ext^1(A,A)).                  (5.1)
```

Thus a codimension-two bridge may genuinely contribute to the second piece in (2.2), geometrically the `H^1(N_(S/X))` channel for a divisor line bundle.

This is the exact distinction needed for route design:

```text
single surface pair:
  H^2(mathcal End A)      [cannot hit]
  H^1(mathcal Ext^1 A,A) [can in principle hit].
```

So the surface bridge is not discarded. Its role is more specific than `L031` initially suggested.

## 6. The natural W_2 bridge

Markman Example 8.2.4 supplies the natural codimension-two surface

```text
W_(2,p) subset Theta subset X.
```

For a non-hyperelliptic genus-four curve, `W_2` is smooth (isomorphic to `C^(2)`) and has

```text
h^(0,1)(W_2)=4,
h^(0,2)(W_2)=6,
```

as used in Markman's Chern-character calculation. Hence positive local-to-global cohomological filtration is genuinely available on this bridge.

The theta divisor has two singular points (the two `g^1_3` points in the source construction), and `W_(2,p)` passes through them. These singular points require a separate local audit before identifying the entire cross-Ext spectral sequence with the smooth-flag model.

However, they do not invalidate the filtration-zero conclusion for any divisor constituent `A` satisfying the hypotheses of Section 2-3: the absence of a reverse sheaf-Hom `mathcal Hom(T,A)` still prevents a pairwise product from acquiring local Ext degree zero.

Thus the `W_2` bridge can only be useful pairwise through the positive-local-Ext part, or through a genuinely higher composition involving further constituents.

## 7. Consequence for the nested-secanta architecture

The current exact virtual identity is

```text
beta'=ch(F_1^D)+ch(Q_D)-ch(Q_H)            [L031].
```

The genus-four construction also contains the exact sequence

```text
0 -> F_1^D
   -> G_D
   -> Q_D
   -> 0,
```

where, before pullback by the RM automorphism,

```text
G := e_* I_(W_(2,p)/Theta)(Theta),
ch(G)=Theta.
```

Equivalently,

```text
beta' = ch(G_D)-ch(Q_H).                  (7.1)
```

The object `G_D` itself is represented inside Markman's geometry by a divisor term corrected by the codimension-two `W_2` surface. `L033a` says that this surface correction cannot, by one pairwise opposite product, remove a scalar filtration-zero obstruction of the divisor term.

Therefore a positive realization of (7.1) must use at least one of:

1. a second divisorial constituent carrying an opposite scalar channel;
2. the full divisor/surface/curve flag with a nonzero higher product;
3. a global derived extension whose obstruction class lies entirely in the `H^1(mathcal Ext^1)` channel after an independently proved cancellation of the scalar part.

This replaces the vague instruction “add a codimension-two bridge” with three exact mechanisms.

## 8. HC-R021-L033 — global pairwise surface-bridge boundary

### Statement

Let `A` be a torsion-free divisorial constituent of ambient projective dimension one and `T` a constituent supported in codimension at least two. Then every direct opposite degree-one Yoneda pair through `T` has zero projection to

```text
H^2(mathcal End(A))
```

inside the local-to-global filtration of `Ext^2(A,A)`.

A surface bridge may still hit the `H^1(mathcal Ext^1(A,A))` component and may participate in nontrivial higher products. In particular the natural `W_2` surface of Markman Example 8.2.4 remains live only through those mechanisms.

### Proof

Sections 2-6.

QED.

## 9. Scope and firewall

`L033` does **not** prove:

- that the mixed obstruction of every divisor constituent has a nonzero scalar filtration-zero component;
- that the `W_2` bridge cannot contribute to `H^1(mathcal Ext^1)`;
- that all higher Massey products vanish;
- that a second divisorial constituent cannot cancel the scalar component;
- second-factor rank `20`;
- all-orders algebraicity transport;
- `HC-R021`;
- the Hodge conjecture.

It is a filtration theorem for direct pairwise lower-dimensional bridges.

## 10. Current disposition

```text
HC-R021-L033 = proved_in_solve_package_not_certified
single_lower_support_pair_hits_H2_End_divisor = false
single_surface_pair_may_hit_H1_Ext1_divisor = true
W2_pairwise_scalar_bridge = impossible
W2_positive_filtration_bridge = open
higher_divisor_surface_curve_product = open
second_divisor_scalar_bridge = open
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 11. Inputs

- `HC-R021-L021`, `L023`, `L030-L032`;
- multiplicative local-to-global Ext spectral sequence;
- purity/torsion-freeness of the divisorial constituent;
- Eyal Markman, arXiv:2502.03415v2, Example 8.2.4 and the `W_2` cohomology calculation used in Example 8.2.3.