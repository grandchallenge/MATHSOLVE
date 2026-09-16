# HC-R021-P4 — Explicit line-bundle control object on the beta-prime ray

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `20358ac7630b4c9a6033e352a3a9a425f82bd3fb`  
**State:** `EXPLICIT_SAME_RAY_PERFECT_COMPLEX__OBSTRUCTION_RANK_22`  
**Date:** 2026-09-16

## 1. Purpose

Construct an explicit perfect complex with Chern character an integer multiple of

```text
beta' = D - (q/6) H^3,
D := g^*Theta,
H := (g^-1)^*Theta,
```

and compute its ambient Hochschild/Atiyah obstruction map exactly.

The object is a control rather than a solution: its obstruction rank is `22`, so it does not lie in `D20`. The calculation identifies the two mixed directions as the exact extra obstruction beyond the six ordinary simultaneous-polarization directions.

Markman Lemma 11.2.8 applies to any object of `D^b(X)` whose Chern character is an integer multiple of `beta'`; hence this control still has the downstream nonzero-rank, Hodge-persistence, and nonzero-Weil-projection properties after the Orlov construction.

## 2. Integral K-theory identity

For a line bundle with first Chern class `L`, write in `K_0(X)`

```text
Delta(L) := [O_X(L)] - [O_X(-L)].
```

On the fourfold `X`,

```text
ch(Delta(L))
 = exp(L)-exp(-L)
 = 2L + (1/3)L^3.
```

Consequently

```text
ch(Delta(2L)-2Delta(L)) = 2L^3.
```

Set

```text
C3(L) := Delta(2L)-2Delta(L).
```

Then

```text
12 beta'
 = 6 Delta(D) - C3(D) - q C3(H)
 = 8 Delta(D) - Delta(2D) - q Delta(2H) + 2q Delta(H).
```

This is an integral `K_0` identity for every positive integer `q`.

## 3. The split perfect complex

Define bundles

```text
P_plus := O(D)^8
          direct_sum O(-2D)
          direct_sum O(-2H)^q
          direct_sum O(H)^(2q),

P_minus := O(-D)^8
           direct_sum O(2D)
           direct_sum O(2H)^q
           direct_sum O(-H)^(2q).
```

Both have rank `9+3q`. Define the split perfect complex

```text
P_beta := P_plus direct_sum P_minus[1].
```

Its K-class is `[P_plus]-[P_minus]`, hence

```text
ch(P_beta)=12 beta'.
```

No gluing curve, generic translate, or unresolved effectivity multiplier enters this object.

## 4. Characteristic action on a line bundle

Because `X` is abelian, `td(X)=1`, and the HKR decomposition is

```text
HT^2(X)
 = H^2(O_X)
   direct_sum H^1(T_X)
   direct_sum H^0(Lambda^2 T_X).
```

Write an element as

```text
u = (alpha, xi, pi).
```

For a line bundle `L` with first Chern class `ell`, the Atiyah class is `ell`. The degree-two characteristic action is therefore

```text
ev_L(alpha,xi,pi)
 = alpha + xi contraction ell + (1/2) pi contraction ell^2
```

in

```text
Ext^2(L,L)=H^2(O_X).
```

The same formula holds after shifts. The characteristic action on a direct sum is block diagonal, so

```text
ker(ev_P_beta)
```

is the intersection of the kernels for the line-bundle summands occurring in `P_beta`.

## 5. The D-pairs kill the gerby and bivector components

The object contains all four line bundles

```text
O(D), O(-D), O(2D), O(-2D).
```

If `u=(alpha,xi,pi)` annihilates `P_beta`, then the equations for `+D` and `-D` give

```text
xi contraction D = 0,
alpha + (1/2) pi contraction D^2 = 0.
```

The equations for `+2D` and `-2D` give

```text
xi contraction D = 0,
alpha + 2 pi contraction D^2 = 0.
```

Subtracting yields

```text
pi contraction D^2 = 0,
alpha = 0.
```

Since `D` is a polarization, contraction with `D` identifies `T_X` with `H^1(O_X)` and its second exterior power gives an isomorphism

```text
H^0(Lambda^2 T_X) -> H^2(O_X),
pi |-> pi contraction D^2
```

up to a nonzero scalar. Hence

```text
pi=0,
alpha=0.
```

Thus no nonzero gerby or bivector component lies in the obstruction kernel of the split control object.

## 6. The H-pairs impose the second polarization condition

The object also contains `O(H)` and `O(-H)` because `q>0`. With `alpha=pi=0`, their two equations reduce to

```text
xi contraction H = 0.
```

Therefore

```text
ker(ev_P_beta)
 = {xi in H^1(T_X) : xi contraction D=0 and xi contraction H=0}.
```

By `HC-R021-L013`, this is exactly

```text
span(k_1,...,k_6)
```

and has dimension `6`.

Since `dim HT^2(X)=28`, we obtain

```text
rank(ob_P_beta) = 28-6 = 22.
```

## 7. HC-R021-L015 — exact rank-22 control

### Statement

The explicit split perfect complex `P_beta` above satisfies

```text
ch(P_beta)=12 beta',
ker(ob_P_beta)=span(k_1,...,k_6),
rank(ob_P_beta)=22.
```

In particular

```text
ob_P_beta(k_7) != 0,
ob_P_beta(k_8) != 0,
```

because `k_7,k_8` complete `k_1,...,k_6` to a basis of the eight-dimensional contraction kernel.

### Proof

Sections 2-6.

QED.

## 8. Downstream Markman interface

Markman Lemma 11.2.8 begins with an object `E' in D^b(X)` whose Chern character is an integer multiple of `beta'`; it does not require that object to be the coherent sheaf constructed immediately before the lemma.

Therefore `P_beta` satisfies the cohomological input to that lemma. If `E_0` is Markman's first secant factor, then

```text
Phi(E_0 boxtimes P_beta)
```

has nonzero rank, its normalized class remains Hodge under the selected Weil-type deformations, and its degree-four normalized component has nonzero projection to the Weil summand.

This confirms that the failure `rank=22` is genuinely a semiregularity/deformation failure, not a failure of the Weil-projection construction.

## 9. Interpretation for D20

The line-bundle control has exactly the six ordinary kernel directions of `HC-R021-L013` and misses exactly the two mixed directions.

Thus a successful same-ray object must introduce nontrivial extension/gluing data which supplies nullhomotopies for

```text
k_7,
k_8
```

without losing the six ordinary directions.

This gives a sharper engineering target than the original eight-relation problem:

```text
split same-ray K-theory representative      rank 22
          |
          +--> extension/gluing correction
                 must kill exactly two
                 mixed obstruction classes
          |
          +--> desired D20 object            rank 20
```

The coherent Example 11.2.7 construction is one possible mechanism for such a two-rank drop, but no such drop is proved here.

## 10. Scope

`P_beta` is not a solution to Markman's Question 11.2.2:

- it is a split perfect complex rather than the desired coherent second-factor sheaf;
- it has obstruction rank `22`, not `20`;
- its mixed relations are nonzero;
- no weak equivariant semiregularity is claimed;
- no Perry conclusion follows from this object.

## 11. Current disposition

```text
HC-R021-L015 = proved_in_solve_package_not_certified
explicit_same_ray_Db_object = P_beta
ch_P_beta = 12_beta_prime
rank_ob_P_beta = 22
kernel_ob_P_beta = span(k1,...,k6)
mixed_k7_k8_for_P_beta = nonzero
D20_nonempty = open
P4_G3 = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 12. Sources

- Eyal Markman, arXiv:2509.23079, Corollary 11.2.6 and Lemma 11.2.8.
- standard Atiyah-class/characteristic-action formula for a line bundle under HKR; `td(X)=1` for an abelian variety.
- `work_packages/HC_R021_P4_CONTRACTION_RANK.md` (`HC-R021-L006`).
- `work_packages/HC_R021_P4_SIX_COMMUTATIVE_DIRECTIONS.md` (`HC-R021-L013`).
