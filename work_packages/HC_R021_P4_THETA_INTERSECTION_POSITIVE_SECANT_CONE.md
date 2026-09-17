# HC-R021-P4 — Explicit non-split positive-secanta cone from a theta-intersection flag

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `eccec1fe4b529890ac50a3029320336c77a3e6a7`  
**State:** `POSITIVE_SECANT_NON_SPLIT_PERFECT_COMPLEX_EXPLICIT__OBSTRUCTION_RANK_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Construct an actual non-split perfect complex on the positive genus-four secant ray

```text
2 beta_d = 2 Theta - (d/3) Theta^3,
```

for every positive integer `d`, rather than merely a split K-theory representative.

The construction combines:

1. the theta-intersection decomposition recorded by Markman in Example 8.2.4;
2. a surface-plus-curves flag contained in that complete intersection;
3. a square root of the sum of the two theta translates;
4. the product of the two theta equations, which gives a genuine derived-dual pairing.

The result settles existence of a non-split positive-secanta perfect complex. It does not yet settle its object-specific Hochschild obstruction rank or `Ext^{<0}` condition.

## 2. Theta-intersection geometry

Let `C` be a non-hyperelliptic genus-four curve with two `g^1_3`'s and set

```text
X = Pic^3(C).
```

Let

```text
D_1 = Theta,
D_2 = tau_(p'-p)(Theta)
```

for distinct points `p,p' in C` as in the footnote to Markman Example 8.2.4. Markman records the scheme-theoretic equality

```text
D_1 cap D_2
 = W_(2,p) union iota(W_(2,p')).                 (2.1)
```

Write

```text
S  := W_(2,p),
S' := iota(W_(2,p')).
```

Thus both theta equations vanish on both `S` and `S'`.

The surface `S'` contains a one-parameter family of Abel-Jacobi curves. Choose distinct curves

```text
C_1,...,C_d subset S'
```

so that:

- no `C_i` is an irreducible component of `S cap S'`;
- all intersections `C_i cap S` are zero-dimensional;
- all intersections `C_i cap C_j`, `i != j`, are zero-dimensional;
- no higher-dimensional common component occurs.

This is possible for any fixed finite `d` by choosing the curve parameters generically in the family on `S'`.

Set the reduced union

```text
Z_d := S union C_1 union ... union C_d.          (2.2)
```

Every irreducible component of `Z_d` is contained in both `D_1` and `D_2`.

## 3. The square-root line bundle

The line bundle of the sum of the two theta translates satisfies

```text
O_X(D_1+D_2) = O_X(2Theta) tensor P
```

for some `P in Pic^0(X)`.

Multiplication by `2` on `Pic^0(X)` is surjective. Choose `M in Pic^0(X)` with

```text
M^2 = P
```

and put

```text
L := O_X(Theta) tensor M.                       (3.1)
```

Then

```text
L^2 ~= O_X(D_1+D_2),                            (3.2)
```

and cohomologically

```text
c_1(L)=Theta.                                   (3.3)
```

Define the rank-one torsion-free sheaf

```text
E_d := I_(Z_d) tensor L.                        (3.4)
```

Since `X` is smooth, `E_d` is perfect.

## 4. Exact odd Chern character

Only the degree-two and degree-six parts of `ch(O_(Z_d))` affect the odd Chern character after twisting by `L`.

For the Abel-Jacobi surface in genus four, Markman Lemma 8.2.5 gives

```text
ch(O_S)
 = Theta^2/2 - Theta^3/3 + 3[pt].              (4.1)
```

For an Abel-Jacobi curve in a genus-four Jacobian,

```text
ch(O_(C_i))
 = Theta^3/6 - 3[pt].                           (4.2)
```

All intersections among the components in (2.2) are zero-dimensional by construction. Inclusion-exclusion therefore changes only the degree-eight term. Hence, modulo `H^8(X)` terms,

```text
ch(O_(Z_d))
 = Theta^2/2
   + (-1/3 + d/6) Theta^3
   + degree_8.                                  (4.3)
```

Thus

```text
ch(I_(Z_d))
 = 1 - Theta^2/2
   + (1/3 - d/6) Theta^3
   + degree_8.                                  (4.4)
```

Twisting by `L` multiplies by `exp(Theta)` in rational cohomology. The odd terms are therefore

```text
ch_1(E_d)=Theta,                                (4.5)
```

and

```text
ch_3(E_d)
 = Theta^3/6
   - Theta^3/2
   + (1/3-d/6)Theta^3
 = -(d/6)Theta^3.                               (4.6)
```

Consequently

```text
odd(ch(E_d))
 = Theta - (d/6)Theta^3
 = beta_d.                                      (4.7)
```

This calculation is insensitive to the zero-dimensional intersection corrections.

## 5. Canonical derived-dual pairing

Let

```text
s_i in H^0(X,O_X(D_i)),  i=1,2,
```

be the defining theta sections.

Because every component of `Z_d` is contained in both divisors,

```text
s_1 in H^0(I_(Z_d) tensor O_X(D_1)),
s_2 in H^0(I_(Z_d) tensor O_X(D_2)).           (5.1)
```

Their tensor product gives a nonzero class

```text
s_1 tensor s_2
 in H^0(
      I_(Z_d) tensor I_(Z_d)
      tensor O_X(D_1+D_2)
    ).                                          (5.2)
```

Via (3.2), this is a degree-zero class in

```text
H^0(E_d tensor^L E_d).                         (5.3)
```

The ordinary tensor class maps canonically into the derived tensor product; on the dense open complement of `Z_d`, it is simply the nonzero product section `s_1 s_2`.

Since `E_d` is perfect, perfect duality identifies (5.3) with

```text
Hom_D(E_d^vee,E_d).                            (5.4)
```

Let

```text
e_d : E_d^vee -> E_d                            (5.5)
```

be the corresponding morphism and define

```text
C_d := Cone(e_d).                               (5.6)
```

The morphism is not nullhomotopic: its restriction to the open set where `E_d` is the line bundle `L` is multiplication by the nonzero section `s_1s_2` of `L^2`.

Therefore `C_d` is a genuinely non-split perfect complex.

## 6. Chern character of the cone

For every perfect complex `E`,

```text
ch(E^vee) = sum_j (-1)^j ch_j(E).
```

Hence

```text
ch(C_d)
 = ch(E_d) - ch(E_d^vee)
 = 2 odd(ch(E_d)).                              (6.1)
```

Using (4.7),

```text
boxed:
ch(C_d)
 = 2Theta - (d/3)Theta^3
 = 2 beta_d.                                    (6.2)
```

Thus `C_d` is an explicit non-split perfect complex on the positive secant ray for every integer `d>0`.

## 7. Relation to the earlier d=0 cone

`L045` used a single `W_2` surface and a theta-square pairing and obtained

```text
ch = 2Theta.
```

The present construction explains exactly what was missing there. Each additional Abel-Jacobi curve contributes

```text
-Theta^3/6
```

to the odd Chern character of `E_d`, while the zero-dimensional intersections only modify even degree. The dual cone doubles this odd contribution.

Hence the cubic secant correction is carried by the curve flag inside the second `W_2` component of the theta intersection.

## 8. Why this is not yet the rank-20 solution

The construction settles a previously open existence subproblem but not the decisive obstruction-map calculation.

Still open for `C_d` are:

1. compute `ob_(C_d):HH^2(X)->Ext^2(C_d,C_d)`;
2. determine whether its kernel equals the contraction kernel of `beta_d` in the ordinary sector;
3. determine `Ext^{<0}(C_d,C_d)` and, if necessary, replace `C_d` by an equivalent connective/coherent realization;
4. transport/pull back the construction to the RM divisor classes used in the `beta'` decomposition;
5. couple the resulting quadratic sectors so that the final `beta'` object kills exactly `k_1,...,k_8` and has obstruction rank `20`.

In particular, this package does not infer semiregularity from the Chern character.

## 9. HC-R021-L046 — positive-secanta cone

### Statement

For every positive integer `d`, on a genus-four Jacobian in the source geometry there exists an explicit morphism

```text
e_d:E_d^vee -> E_d
```

such that the cone

```text
C_d=Cone(e_d)
```

is non-split and satisfies

```text
ch(C_d)=2 beta_d
       =2Theta-(d/3)Theta^3.
```

### Proof

Sections 2-6.

QED.

## 10. Disposition

```text
HC-R021-L046 = proved_in_solve_package_not_certified
positive_secant_non_split_perfect_complex_exists = true
positive_secant_cone_ch = 2 beta_d
positive_secant_cone_obstruction_rank = open
positive_secant_cone_Ext_negative = open
RM_QUADRIC_A1 = open_with_L044_numerical_evidence
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

This is a Solve-package construction and not a MATHCERT disposition.

## 11. Sources and prior inputs

- Eyal Markman, arXiv:2502.03415, Example 8.2.4, especially the scheme-theoretic theta-intersection identity in footnote 20;
- Markman Lemma 8.2.5 for `ch(O_(W_2))`;
- Poincare's formula for the Abel-Jacobi curve class;
- `HC-R021-L039`, `L040`, and `L045`.
