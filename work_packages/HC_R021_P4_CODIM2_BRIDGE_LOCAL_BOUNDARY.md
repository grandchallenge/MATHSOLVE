# HC-R021-P4 — Codimension-two bridge: local Yoneda boundary

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `04d5c4b1f3f3dc46bba0cf87e94a114e47b71f94`  
**State:** `CODIM2_LOCAL_CHANNELS_EXIST__DIVISOR_SIDE_PAIRWISE_PRODUCT_ZERO__GLOBAL_OR_HIGHER_DATA_REQUIRED`  
**Date:** 2026-09-16

## 1. Purpose

Continue the bridge analysis after `HC-R021-L031`.

`L031` proves that a direct divisor/curve two-step extension cannot kill the nonzero mixed obstruction carried by the positive divisor sector. It identifies a codimension-two bridge as the shortest next candidate because a codimension-two complete-intersection object has a genuine degree-two self-Ext wedge.

The present package computes the exact local Ext category of the first flag

```text
divisor  A
   |
   v
surface  T
```

and determines what that extra Ext amplitude can and cannot do.

The conclusion is sharp:

> a codimension-two bridge does create opposite degree-one channels, and its own self-Ext algebra has a nonzero degree-two wedge, but **every direct opposite pair still has zero Yoneda product on the divisor side**.

Thus simply inserting a surface between the divisor and curve does not repair the `L021` factorization at the pointwise/Koszul level. Any successful use of a codimension-two bridge must use either:

1. genuinely global local-to-global cohomology in one of the extension classes; or
2. a higher filtered/Massey differential involving at least one additional constituent.

This is a boundary lemma, not a no-go for all codimension-two bridges.

## 2. Local regular flag

Let

```text
R = k[[f,g,h,w]]
```

be a regular local ring of dimension four. Model a smooth divisor and a smooth codimension-two complete intersection contained in it by

```text
A := R/(f),
T := R/(f,g).
```

Line-bundle twists do not change the local Ext-amplitude statements below and are suppressed.

The standard free resolutions are

```text
K_A : 0 -> R --f--> R -> A -> 0,
```

and

```text
K_T : 0 -> R --(-g,f)^t--> R^2 --(f,g)--> R -> T -> 0.
```

## 3. Exact cross-Ext groups

### 3.1 `Ext(A,T)`

Apply `Hom_R(K_A,T)`. Since `f` acts by zero on `T`, the differential vanishes. Hence

```text
Ext^0_R(A,T) = T,
Ext^1_R(A,T) = T,
Ext^j_R(A,T) = 0,  j>=2.                 (3.1)
```

### 3.2 `Ext(T,A)`

Apply `Hom_R(K_T,A)`. Since `f=0` in `A` and `g` is a non-zero-divisor on `A`, the resulting cochain Koszul complex is the complex for the sequence `(0,g)`.

Its cohomology is

```text
Ext^0_R(T,A) = 0,
Ext^1_R(T,A) = T,
Ext^2_R(T,A) = T,
Ext^j_R(T,A) = 0,  j>=3.                 (3.2)
```

Equivalently, the zero normal equation `f` contributes an exterior generator, while the regular equation `g` contributes the usual top Koszul class.

### 3.3 Self-Ext of the divisor

Applying `Hom_R(K_A,A)` again gives zero differential and

```text
Ext^0_R(A,A)=A,
Ext^1_R(A,A)=A,
Ext^j_R(A,A)=0,  j>=2.                   (3.3)
```

### 3.4 Self-Ext of the surface

Both defining equations vanish on `T`, so

```text
Ext^*_R(T,T)
  = T tensor Lambda^*(epsilon_f,epsilon_g).   (3.4)
```

In particular

```text
Ext^2_R(T,T)=T (epsilon_f wedge epsilon_g)
```

is nonzero. This is the extra degree-two local wedge absent from a Cartier divisor.

## 4. All opposite degree-one shift patterns

Let the divisor and surface constituents be shifted by integers `r,s`:

```text
A[r],
T[s].
```

A degree-one morphism

```text
A[r] -> T[s]
```

is an element of

```text
Ext^p_R(A,T),
p := 1+s-r,
```

while a degree-one morphism in the opposite direction lies in

```text
Ext^q_R(T,A),
q := 1+r-s.
```

Necessarily

```text
p+q=2.                                    (4.1)
```

Using (3.1)-(3.2), the only possibilities in which **both** opposite degree-one spaces are nonzero are

```text
(p,q)=(0,2)
or
(p,q)=(1,1).                              (4.2)
```

Thus a codimension-two bridge genuinely improves on the definite divisor-block situation of `L026`: opposite degree-one channels can exist in either adjacent shift parity.

## 5. The divisor-side product is always zero locally

Take any pair of opposite degree-one classes

```text
c in Ext^p_R(A,T),
e in Ext^q_R(T,A),
```

with `(p,q)` one of the two possibilities (4.2).

Their Yoneda composition on the divisor side is

```text
e c in Ext^(p+q)_R(A,A)=Ext^2_R(A,A).
```

By (3.3),

```text
Ext^2_R(A,A)=0.
```

Hence

```text
e c = 0                                    (5.1)
```

for **every** opposite degree-one pair and every shift choice.

This is not a dimension-counting statement and does not depend on genericity. It is forced by the codimension-one projective dimension of the divisor module.

### HC-R021-L032a — local codimension-two pairwise factorization no-go

For a smooth divisor module `A` and a smooth codimension-two complete-intersection module `T` contained in it, no pair of opposite degree-one morphisms between arbitrary shifts of `A` and `T` can have a nonzero Yoneda product in the divisor self-`Ext^2`.

Consequently a nonzero degree-two obstruction on the divisor graded piece cannot be killed by the first filtered differential using only one direct `A <-> T` pair.

## 6. What the nonzero `Ext^2(T,T)` can do

The result does **not** say that the surface bridge is useless.

The reverse composition

```text
c e in Ext^2_R(T,T)
```

can be nonzero because of (3.4). In the `(1,1)` shift pattern it is the ordinary exterior/Koszul product of the two normal degree-one generators; in the `(0,2)` pattern it can represent the corresponding top Koszul class after the shift identification.

Thus a surface can absorb or redistribute a diagonal obstruction **on its own graded piece**. What it cannot do directly is reproduce a nonzero divisor diagonal obstruction through one opposite pair.

This distinction is the exact local boundary needed before attempting a longer bridge.

## 7. Local-to-global qualification

For a global smooth flag

```text
T -> S -> X
```

with `S` a divisor and `T` codimension two in `X`, the local-to-global spectral sequences contain more than the stalkwise groups above.

For example, globally

```text
Ext^1_X(i_*L,j_*M)
```

can contain a contribution from

```text
H^1(T, mathcal Hom_X(i_*L,j_*M)),
```

and global divisor self-`Ext^2` has the standard pieces

```text
H^2(S,O_S)
and
H^1(S,N_(S/X))
```

(up to line-bundle identifications).

Therefore (5.1) does **not** imply that every global Yoneda product involving a codimension-two bridge is zero. A global extension class carrying positive Cech degree can, in principle, contribute to the `H^1(mathcal Ext^1)` or `H^2(mathcal Hom)` pieces of the divisor self-Ext.

The correct conclusion is narrower:

```text
pointwise/Koszul opposite channels alone are insufficient;
any successful two-way surface bridge must use nonlocal cohomology,
or a higher filtered/Massey differential.              (7.1)
```

This is precisely where the next calculation must occur. Treating the local nonzero `Ext^2(T,T)` as if it automatically supplied the missing divisor factorization would repeat the local/global mistake that the campaign is designed to avoid.

## 8. Consequence for the nested-secanta lane

Combine `L031` and `L032a`.

The exact target presentation remains

```text
beta' = ch(F_1^D)+ch(Q_D)-ch(Q_H).
```

A direct negative curve cannot repair the positive divisor obstruction (`L031`). Adding one ordinary codimension-two complete-intersection object does create the missing opposite degree-one **spaces**, but its direct pairwise product into the divisor diagonal is still zero (`L032a`).

Hence the next positive calculation is no longer merely

```text
find T with Ext^2(T,T) != 0.
```

It is one of the following exact problems:

### L032-B1 — global surface bridge

Find a concrete surface `T` and line-bundle data for which one of the opposite degree-one classes necessarily lives in a positive local-to-global cohomological filtration and compute the resulting product

```text
Ext^1(A,T_shift) tensor Ext^1(T_shift,A)
  -> Ext^2(A,A)
```

on the `H^2(O_S)` / `H^1(N)` decomposition.

### L032-B2 — higher flag bridge

Use a flag

```text
A (divisor) -> T (surface) -> B (curve)
```

and compute the first nonzero higher differential/Massey product in the endomorphism filtration. The target is an actual degree-two class on `A`, not merely a nonzero self-class on `T`.

The existing Markman geometry already contains a natural surface candidate: the `W_2` component in Example 8.2.4. Its irregularity is nonzero (`h^{0,1}(W_2)=4` in the source calculation), so it is a serious `L032-B1` candidate rather than a formal placeholder.

## 9. HC-R021-L032 — codimension-two local boundary

### Statement

For the regular local divisor/surface flag

```text
A=R/(f),
T=R/(f,g),
```

all opposite degree-one shift patterns are explicitly given by (4.2), but every divisor-side pairwise Yoneda product is zero:

```text
Ext^1(A[r],T[s]) x Ext^1(T[s],A[r])
  -> Ext^2(A[r],A[r])
```

vanishes for every `r,s` for which both source factors are nonzero.

The surface self-`Ext^2` is nevertheless nonzero. Therefore a codimension-two bridge can contribute only through genuinely global local-to-global extension data or through a higher filtered/Massey mechanism if it is to cancel the nonzero mixed obstruction on the divisor sector.

### Proof

Sections 2-7.

QED.

## 10. Scope and firewall

`L032` does **not** rule out:

- a global surface bridge using `H^1` or higher cohomology;
- the `W_2` surface of Markman Example 8.2.4;
- a divisor/surface/curve higher Massey product;
- a longer non-formal perfect complex;
- second-factor rank `20`;
- all-orders algebraicity transport;
- `HC-R021`;
- the Hodge conjecture.

It rules out only the naive inference that the local `Ext^2(T,T)` wedge by itself repairs the divisor diagonal obstruction.

## 11. Current disposition

```text
HC-R021-L032 = proved_in_solve_package_not_certified
codim2_opposite_degree1_channels = exist
codim2_surface_self_Ext2 = nonzero
divisor_side_local_pairwise_product = zero
pure_local_Koszul_surface_bridge = insufficient
global_surface_bridge = open
higher_flag_Massey_bridge = open
W2_surface_bridge = highest_value_concrete_B1_candidate
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 12. Inputs

- `HC-R021-L021`, `L025-L028`, `L030-L031`;
- Koszul resolutions for regular immersions of codimension one and two;
- standard local-to-global Ext spectral sequence;
- Eyal Markman, arXiv:2502.03415v2, Example 8.2.4 and the cohomology calculation of `W_2` used there.