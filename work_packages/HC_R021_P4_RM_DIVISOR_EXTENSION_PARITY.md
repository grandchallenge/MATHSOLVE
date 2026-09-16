# HC-R021-P4 — RM divisor divisibility and two-step extension parity no-go

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `82917d7be34069c9d277ae73a42b3fa1f0e509aa`  
**State:** `PROPER_J_DIVISORS_CAN_CREATE_INDEX2_EXT2__BUT_TWO_STEP_MIXED_FACTORIZATION_STILL_ZERO`  
**Date:** 2026-09-16

## 1. Purpose

Continue `HC-R021-L027` at the only residual three-divisor arithmetic branch.

`L027` proves that every third RM-plane divisor occurring in a nonzero three-block Chern identity on the `beta'` ray is of the form

```text
L=mJ,
J=D+qH.
```

For `m>=1`, `L026` already closes the corresponding three-block twisted-complex lane by definite-difference Ext parity. The only remaining possibility is a proper integral divisor

```text
L=J/d,
d>1.
```

Such a divisor can change the Ext geometry: the differences `L-D` or `L-H` may have Mumford index `2`, and then an `Ext^2` group appears. This package determines that arithmetic exactly and proves that the new `Ext^2` does **not** repair the two-step mixed obstruction. The opposite `Ext^1` products required by `L021` are still identically zero.

The result does not rule out a longer complex with additional `K_0`-zero bridge objects or non-divisorial geometry.

## 2. Divisibility of J in the RM Neron-Severi lattice

Use the source datum

```text
D=g^*Theta,
H=(g^-1)^*Theta,
Nm(f)=1,
g^*Theta=f^2 · Theta.
```

Under the principal-polarization identification of the RM part of `NS(X)` with the Rosati-symmetric order in `F`, the class `J=D+qH` corresponds to

```text
u := f^2 + q f^(-2)
    = f^(-2)(f^4+q).
```

Since `g` is an automorphism, `f` is a unit in the relevant integral endomorphism order. Hence multiplication by `f^(-2)` does not change integer divisibility.

### HC-R021-L028a — exact divisibility criterion

For an integer `d>0`,

```text
J in d NS(X)
```

if and only if

```text
f^4+q in d O_RM,
```

where `O_RM` is the integral RM order acting on `X`.

In particular, if `d` divides `J`, then

```text
 d^2 | Nm_F/Q(f^4+q).
```

Because `Nm(f)=1`,

```text
Nm(f^4+q)
 = 1 + q Tr_F/Q(f^4) + q^2
 = A.
```

Therefore every proper divisor satisfies

```text
d^2 | A.                                      (2.1)
```

The exceptional value `d^2=A` is exactly the excluded `m^2A=1` branch of `L027`, which gives zero `beta'` coefficient. Hence every nontrivial residual identity has

```text
d^2 < A,
d < sqrt(A).                                  (2.2)
```

### q=1 specialization

If `q=1`, then

```text
nu=f^2+f^(-2)=Tr_F/Q(f^2) in Z,
```

so

```text
J=Tr_F/Q(f^2) Theta.
```

Thus the residual search is literally over the positive divisors of the integer `Tr(f^2)`; the maximal divisor is the excluded `d^2=A` case.

## 3. RM index of a proper divisor difference

Use the normal form

```text
D=U+V,
H=aU+bV,
ab=1,
0<a<b,
A=(1+qa)(1+qb)=(q+a)(q+b).
```

Let

```text
L=J/d
 =(1/d)[(1+qa)U+(1+qb)V].
```

By (2.2), `d<sqrt(A)`.

### Difference from D

```text
L-D
 = [(1+qa-d)/d] U
   +[(1+qb-d)/d] V.                         (3.1)
```

Since

```text
1+qa < sqrt(A) < 1+qb,
```

the second coefficient in (3.1) is positive. The first is positive or negative according as

```text
d < 1+qa
```

or

```text
d > 1+qa.
```

Equality cannot occur: `a` is irrational because `f^2 != 1` and `Nm(f)=1`.

Therefore `L-D` is either ample or nondegenerate of index `2`.

### Difference from H

Using `ab=1`,

```text
L-H
 = [a(q+b-d)/d] U
   +[b(q+a-d)/d] V.                         (3.2)
```

Since

```text
q+a < sqrt(A) < q+b,
```

the first coefficient is positive, while the second changes sign at `d=q+a`. Again equality is impossible.

Therefore `L-H` is also either ample or nondegenerate of index `2`.

Thus every residual proper divisor has only the following pairwise difference indices:

```text
ind(L-D) in {0,2},
ind(L-H) in {0,2}.                          (3.3)
```

The `q=1` case is especially clean: both thresholds coincide at `1+a`, so every integer `d>1` below the exceptional maximum lies in the index-two regime for both differences.

## 4. RHom of two symmetric divisor blocks

For an ample integral divisor class `R`, choose an effective Cartier divisor in `|2R|` and write

```text
B_R := O_(2R)(R).
```

It has the two-term locally free resolution

```text
0 -> O_X(-R) -> O_X(R) -> B_R -> 0.        (4.1)
```

Let `R,S` be distinct ample classes such that `S-R` is nondegenerate of even index `0`, `2`, or `4`.

Resolving both objects, the sheaf-Hom complex for `RHom(B_S,B_R)` has internal degrees

```text
p=-1 : O_X(-R-S),

p= 0 : O_X(S-R) direct_sum O_X(R-S),

p= 1 : O_X(R+S).                            (4.2)
```

On the abelian fourfold, a nondegenerate line bundle has cohomology in exactly its Mumford index.

The sum `R+S` is ample and `-(R+S)` is anti-ample. Hence the extreme terms of (4.2) contribute only in `(p,q)=(1,0)` and `(-1,4)`.

### Index-two case

If `ind(S-R)=2`, then both middle line bundles have cohomology only in degree `2`. Therefore the only first-page terms occur in total degrees

```text
1,2,3.
```

In particular,

```text
Hom(B_S,B_R)=0=Hom(B_R,B_S),               (4.3)
```

and

```text
Ext^2(B_S,B_R)
 ~= H^2(O_X(S-R)) direct_sum H^2(O_X(R-S))
```

is generally nonzero.

Moreover every `Ext^1(B_S,B_R)` class is represented by the internal-degree `+1` component

```text
O_X(-S) -> O_X(R),
```

i.e. by a section of `O_X(R+S)`. The same holds in the opposite direction.

If

```text
e in Ext^1(B_S,B_R),
c in Ext^1(B_R,B_S),
```

then their cochain representatives both have internal degree `+1`. Their composition would have internal degree `+2`, but the two-term endomorphism complexes have no such component. Hence

```text
e c = 0,
c e = 0.                                   (4.4)
```

### Definite-difference case

If `S-R` is ample or anti-ample, `L026` already proves

```text
Ext^even(B_S,B_R)=Ext^even(B_R,B_S)=0.
```

The degree-one classes which remain are again represented by the top internal-degree `+1` maps after quotienting by the horizontal boundary from the degree-zero term. Their opposite Yoneda products are therefore also zero for the same internal-degree reason:

```text
Ext^1(B_S,B_R) Ext^1(B_R,B_S) -> Ext^2(B_R,B_R)
```

and its reverse are the zero maps.                 (4.5)

### HC-R021-L028b — cross-divisor Ext-one products vanish

For any two distinct symmetric divisor blocks `B_R,B_S` whose RM difference is nondegenerate of even index, every pair of opposite degree-one classes has zero Yoneda products in both orders.

This includes the pairs

```text
(B_D,B_H),
(B_D,B_(J/d)),
(B_H,B_(J/d))
```

for every proper integral divisor `J/d` allowed by `L027`.

## 5. The mixed obstruction is nonzero on every block

Let

```text
R=rU+sV,
r,s>0.
```

The two-term edge calculation of `L025`, together with the line-bundle characteristic formula of `L016`, gives nonzero diagonal degree-two components

```text
ob_(B_R)(k_7):  (qa+r^2) y_1 wedge y_2,
ob_(B_R)(k_8):  (qb+s^2) y_3 wedge y_4.    (5.1)
```

Both coefficients are strictly positive.

More generally, for

```text
k=lambda k_7+mu k_8,
```

the two displayed components are independent, so

```text
ob_(B_R)(k)=0
```

implies

```text
lambda=mu=0.                                (5.2)
```

Thus every nonzero mixed combination is a nonzero diagonal obstruction on each `B_D`, `B_H`, and `B_(J/d)` block.

## 6. HC-R021-L028 — two-step divisor-block repair remains impossible

### Statement

Let `R,S` be any two distinct divisor classes among

```text
D,
H,
J/d
```

with `d` a proper integral divisor allowed by `L027`. Let

```text
e in Ext^1(B_S,B_R)
```

define a two-step extension of `B_S` by `B_R`.

Then no nonzero mixed direction

```text
k in span(k_7,k_8)
```

can become unobstructed on that extension.

### Proof

By (5.2), the diagonal obstruction classes

```text
o_R=ob_(B_R)(k),
o_S=ob_(B_S)(k)
```

are both nonzero.

`HC-R021-L021a` gives the exact necessary factorization condition for a two-step extension: if the obstruction on the extension vanished, there would have to exist

```text
c in Ext^1(B_R,B_S)
```

such that, up to the fixed enhancement sign convention,

```text
e c=o_R,
c e=o_S.                                  (6.1)
```

But `L028b` gives

```text
e c=0=c e
```

for every such pair. This contradicts the nonzero diagonal classes.

Therefore no two-step extension between any two of the RM symmetric divisor blocks can kill a nonzero mixed obstruction.

QED.

## 7. Consequence for the residual J-divisibility route

The proper-divisor escape now has the following exact status:

```text
J divisible by d>1
    |
    +--> d^2 | A                                  [L028a]
    |
    +--> L=J/d has D/H differences of index 0 or 2
    |
    +--> index 2 may create Ext^2                  [NEW]
    |
    +--> opposite Ext^1 products are still zero   [L028b]
    |
    +--> any two-step divisor-block repair fails   [L028]
```

Thus the first genuinely new positive mechanism cannot be merely an extension between two symmetric divisor blocks, even in the index-two regime.

The next possible mechanisms are narrower:

1. a longer complex with additional `K_0`-zero bridge terms whose Yoneda products do not factor through the top internal degree of two divisor resolutions;
2. a codimension-two/intersection-supported bridge with a rank-two normal Koszul algebra;
3. a higher-rank/semihomogeneous object with non-scalar Atiyah action;
4. an independently rank-20 class followed by a genuine categorical transform.

The appearance of `Ext^2` in the proper-divisor case is therefore diagnostic rather than sufficient: it identifies the cohomological degree a successful bridge must access, while `L028` proves that the direct two-step factorization channel remains closed.

## 8. Scope and firewall

`L028` does **not** prove:

- that every longer twisted complex generated by `B_D,B_H,B_(J/d)` fails;
- that added `K_0`-zero bridge objects cannot work;
- that codimension-two or higher-rank bridges cannot work;
- that every divisible `J` is irrelevant;
- second-factor rank `20`;
- all-orders algebraicity transport;
- `HC-R021`;
- the Hodge conjecture.

It closes exactly the divisibility arithmetic and the entire **two-step** extension repair among the natural RM symmetric divisor blocks.

## 9. Current disposition

```text
HC-R021-L028 = proved_in_solve_package_not_certified
J_divisibility_criterion = f^4_plus_q_divisible_in_RM_order
proper_divisor_implies_d2_divides_A = true
proper_J_divisor_difference_index = 0_or_2
index2_Ext2_bridge_group = can_be_nonzero
opposite_cross_Ext1_products = zero
proper_J_two_step_divisor_extension_rank20 = impossible
longer_K0_zero_bridge = open
codimension2_bridge = open
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 10. Inputs and sources

- `HC-R021-L006`, `L007`, `L016`, `L021`, `L025`, `L026`, `L027`;
- Eyal Markman, arXiv:2509.23079v1, Corollary 11.2.6, Example 11.2.7, Lemma 11.2.8;
- principal-polarization identification of the RM Neron-Severi lattice with the Rosati-symmetric endomorphism order;
- the divisor resolution `0 -> O(-R) -> O(R) -> B_R -> 0`;
- Mumford's index theorem for nondegenerate line bundles on an abelian variety;
- standard Yoneda composition in the Hom complex of two-term resolutions.
