# HC-R021-P4-A1 — Atiyah-rank reduction for the explicit CM4 second factor

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `09f63de8ec7a6833bdea0c3d007a76a55ee00a72`  
**State:** `ATIYAH_RANK_REDUCED_TO_EIGHT_EXPLICIT_YONEDA_RELATIONS`  
**Date:** 2026-09-16

## 1. Purpose

Continue the direct obstruction route `HC-R021-P4-A1` after `HC-R021-L006` fixed the cohomological contraction rank.

The input is Markman's explicit simple coherent sheaf `E'` from arXiv:2509.23079, Example 11.2.7, with

```text
ch(E') = N beta',
beta' = g^*Theta - (q/6)(g^-1)^*(Theta^3),
N != 0.
```

The parent result proves

```text
rank(c_beta') = 20,
dim ker(c_beta') = 8,
```

for the HKR contraction map

```text
c_beta' : HT^2(X) -> H_Omega^{-2}(X).
```

By semiregularity compatibility,

```text
ker(ob_E') subset ker(c_beta').
```

Hence `rank(ob_E') >= 20`; Markman's restricted semiregularity condition holds for this explicit sheaf exactly when all eight cohomological annihilator directions also lie in `ker(ob_E')`.

This package rewrites that statement as eight explicit Yoneda-product identities and records the exact gluing triangle on which they must be checked.

## 2. Degree-one presentation of the obstruction map

Set

```text
V := H^1(O_X) direct_sum H^0(T_X).
```

For an abelian variety the tangent bundle is trivial and `td(X)=1`. Under HKR,

```text
HT^*(X) ~= Lambda^* V
```

as a graded algebra. For every perfect/coherent object `E`, the action induced by `exp(at_E)` is an algebra homomorphism

```text
ev_E : HT^*(X) -> Ext^*(E,E).
```

Its restriction to degree two is the ambient obstruction map:

```text
ob_E = ev_E | HT^2(X).
```

This is the mechanism used by Markman in arXiv:2502.03415, Section 8.3, where the obstruction map is computed from the degree-one action and the Yoneda algebra.

Therefore, for `E'`, `HC-R021-P4-A1` is a finite quadratic problem:

> compute the Yoneda-product map on `Lambda^2 V`, or equivalently determine which degree-two exterior relations among the eight translation/twist generators vanish in `Ext^2(E',E')`.

No separate 28-dimensional Atiyah-class matrix is required.

## 3. Real-multiplication basis

Use the same Hodge basis as `HC-R021-L006`.

Let

```text
y_1,...,y_4
```

be the basis of `H^1(O_X)` dual to the holomorphic basis adapted to the two real-multiplication blocks, and let

```text
t_1,...,t_4
```

be the corresponding basis of `H^0(T_X)`.

Write

```text
a = lambda^(-4),
b = lambda^4,
c = -q/6,
```

so `a,b,c` are nonzero and `a != b`.

Under

```text
HT^2(X) = Lambda^2 H^1(O_X)
          direct_sum H^1(T_X)
          direct_sum Lambda^2 H^0(T_X),
```

the eight-dimensional kernel computed in `HC-R021-L006` has the following basis.

### Block `sigma_1`

```text
k_1 = y_1 wedge t_1,
k_2 = y_2 wedge t_2,
k_3 = y_1 wedge t_2 + y_2 wedge t_1,
k_7 = t_1 wedge t_2 - 6 c a^2 b (y_1 wedge y_2).
```

### Block `sigma_2`

```text
k_4 = y_3 wedge t_3,
k_5 = y_4 wedge t_4,
k_6 = y_3 wedge t_4 + y_4 wedge t_3,
k_8 = t_3 wedge t_4 - 6 c a b^2 (y_3 wedge y_4).
```

The first six are the symmetric endomorphism directions inside the two real-multiplication blocks. The final two are the mixed `H^2(O_X) + Lambda^2 T_X` annihilator directions forced by the secant relation between the degree-two and degree-six terms of `beta'`.

## 4. HC-R021-L007 — exact eight-relation criterion

### Statement

For Markman's explicit `E'`, the following are equivalent:

1. `rank(ob_E') = 20`;
2. `ker(ob_E') = ker(c_beta')`;
3. `ev_E'(k_i)=0` in `Ext^2(E',E')` for every `1 <= i <= 8`.

Equivalently, the first-order part of Markman's Question 11.2.2 for the explicit sheaf closes if and only if the eight displayed quadratic Yoneda relations vanish.

### Proof

Compatibility of the semiregularity diagram gives

```text
ker(ob_E') subset ker(c_beta').
```

`HC-R021-L006` proves that the latter space is exactly the eight-dimensional span of `k_1,...,k_8`.

If all eight `k_i` lie in `ker(ob_E')`, then the inclusion of kernels is an equality. Since `dim HT^2(X)=28`, the common kernel has dimension `8` and

```text
rank(ob_E') = 28 - 8 = 20.
```

Conversely, if `rank(ob_E')=20`, then `dim ker(ob_E')=8`. An eight-dimensional subspace contained in the eight-dimensional `ker(c_beta')` must equal it, so all `k_i` vanish under `ev_E'`.

QED.

### Falsification form

A single nonzero class

```text
ev_E'(k_i) != 0
```

for any one of the eight displayed elements proves

```text
rank(ob_E') > 20
```

and refutes the explicit Example 11.2.7 sheaf as a solution to Markman's restricted semiregularity question.

There can be no obstruction-map rank below `20` and no ninth independent kernel relation.

## 5. Exact gluing model for `E'`

Markman constructs `E'` as follows.

- Let `F'` be the simple secant sheaf from arXiv:2502.03415, Example 8.2.4, with

```text
ch(F') = Theta - (d/6) Theta^3.
```

- Choose `N` generic translates `T_j` of `g^*F'`.
- Choose a curve `C'` with the prescribed class correcting the degree-six Chern character.
- Choose a line bundle `L` on `C'`.
- At each transverse point where `C'` meets the support of `T_j` in the locus where `T_j` is a line bundle on its support, identify the two one-dimensional fibers.

Let

```text
A := direct_sum_(j=1)^N T_j,
B := i_* L,
```

where `i:C' -> X`, and let `S` be the finite set of gluing points. The fiber identifications give a difference map

```text
rho : A direct_sum B -> Q,
Q := direct_sum_(p in S) k_p,
```

and the glued sheaf is the kernel:

```text
0 -> E' -> A direct_sum B -> Q -> 0.
```

Equivalently, in `D^b(X)`,

```text
E' -> A direct_sum B -> Q -> E'[1]
```

is a distinguished triangle.

This is the standard local model of gluing line-bundle fibers over transverse zero-dimensional intersections. The Hochschild action is natural on this triangle, so each `ev_E'(k_i)` must be computed together with the induced actions on `A`, `B`, `Q`, and the gluing morphism `rho`.

## 6. Why Chern-character cancellation is insufficient

The two mixed relations `k_7,k_8` are especially important.

Their cohomological vanishing comes from cancellation between:

- the `H^2(O_X)` action on the divisor-class part of `ch(E')`; and
- the bivector action on the curve-class part of `ch(E')`.

The construction of `E'` mirrors this split geometrically: `A` supplies the divisorial contribution and `B` supplies the curve correction, with `Q` enforcing the fiber gluing.

But

```text
k_i contraction ch(E') = 0
```

does **not** imply

```text
ev_E'(k_i)=0.
```

The latter requires an actual nullhomotopy in the self-Ext algebra compatible with the triangle. K-theory additivity or cancellation of traces is not enough.

This is precisely the remaining content of `P4-A1`.

## 7. Exact next calculations

The 28-column obstruction computation is reduced to the following eight tests.

### A1a — six block-symmetric relations

Compute

```text
ev_E'(k_i),  1 <= i <= 6.
```

These classes lie in the `H^1(T_X)` summand and preserve both degree components of `beta'` separately at the cohomological level. They are the shortest candidates for geometric first-order deformations.

### A1b — two mixed secant relations

Compute

```text
ev_E'(k_7),
ev_E'(k_8).
```

These require cancellation between twist and bivector effects and are the more delicate test of the gluing triangle.

### A1c — use the gluing triangle, not a surrogate object

For each `k_i`, compute the natural Hochschild action on

```text
E' -> A direct_sum B -> Q -> E'[1].
```

A positive proof must produce a compatible nullhomotopy for the action on the cone. A negative proof needs only one gluing-compatible local component detecting a nonzero class.

### A1d — do not import the threefold rank-six calculation

Markman's arXiv:2502.03415, Proposition 8.3.9, proves a rank-six obstruction map for an ideal sheaf of disjoint Abel-Jacobi curves on an abelian threefold by exploiting a very specific direct-sum decomposition of `Ext^2` and vanishing of cross-component Yoneda products.

Those hypotheses are not established for the fourfold pushout `E'`. That result is a template for the method, not evidence that the eight relations above vanish.

## 8. Current disposition

```text
HC-R021-L007 = proved_in_solve_package_not_certified
rank_contraction_beta_prime = 20
possible_kernel_of_ob_E_prime = span(k_1,...,k_8)
rank_ob_E_prime = open_in_[20,28]
P4_A1_positive_criterion = all_eight_Yoneda_relations_vanish
P4_A1_falsification_criterion = any_one_Yoneda_relation_nonzero
Markman_Question_11_2_2_for_explicit_E_prime = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 9. Sources

- Eyal Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079; Question 11.2.2, Example 11.2.7, Lemma 11.2.8.
- Eyal Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*, arXiv:2502.03415; Lemma 8.3.4, Remark 8.3.5, Proposition 8.3.9, and the degree-one/Yoneda obstruction calculation in Section 8.3.
- `work_packages/HC_R021_P4_CONTRACTION_RANK.md` for the explicit rank-20 calculation and basis of the eight-dimensional annihilator.
