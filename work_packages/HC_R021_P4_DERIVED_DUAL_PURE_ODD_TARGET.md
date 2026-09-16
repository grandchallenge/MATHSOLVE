# HC-R021-P4 — Derived-dual extraction gives an explicit full-support perfect object on the beta-prime ray

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `469d40decf7ec2b9f1423e903f5188b08dac4538`  
**State:** `EXPLICIT_FULL_SUPPORT_PERFECT_OBJECT_ON_2_BETA_PRIME_RAY__RANK20_OBSTRUCTION_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Exploit the full-support secant objects after the correction `L039`.

The key observation is elementary but structural: on a fourfold, derived duality preserves the Chern-character components in cohomological degrees `0,4,8` and negates those in degrees `2,6`. Markman's full-support secant objects contain both parity sectors. Taking the virtual difference with the derived dual therefore extracts the pure odd secant class as the Chern character of an actual perfect complex.

Combining these pure-odd blocks with the four-secanta identity of `L031` gives an explicit perfect object whose Chern character is exactly `2 beta'`.

Thus the remaining first-order problem is not existence of a perfect representative on the target ray. It is whether one can choose/nontrivially couple such a representative so that its obstruction map has the minimum possible rank `20`.

## 2. Full-support secant object

Use Markman's genus-four full-support construction from arXiv:2502.03415, Example 8.2.3. After the theta twist write the resulting perfect object as

```text
E_d.
```

The source computes its Chern character in the form

```text
ch(E_d)=alpha_d+beta_d,                    (2.1)
```

where

```text
alpha_d in H^0(X) + H^4(X) + H^8(X),
beta_d  in H^2(X) + H^6(X),                (2.2)
```

and the odd secant part is

```text
beta_d=Theta-(d/6)Theta^3.                 (2.3)
```

Because `X` is smooth, every bounded coherent complex is perfect; hence the derived dual

```text
E_d^vee := RHom(E_d,O_X)
```

is again perfect.

## 3. Derived dual extracts the odd sector

For any perfect object on a smooth variety,

```text
ch_j(E^vee)=(-1)^j ch_j(E).                (3.1)
```

On a fourfold, the components of `alpha_d` have even `j=0,2,4`, whereas those of `beta_d` have odd `j=1,3`. Thus

```text
ch(E_d^vee)=alpha_d-beta_d.                (3.2)
```

Define the honest perfect complex

```text
P_d := E_d direct_sum E_d^vee[1].          (3.3)
```

A shift by one negates the `K_0` class, so

```text
ch(P_d)
 = ch(E_d)-ch(E_d^vee)
 = 2 beta_d.                               (3.4)
```

### HC-R021-L040a — pure-odd derived-dual extraction

Every full-support secant object `E_d` of Example 8.2.3 therefore gives an explicit perfect representative

```text
P_d
```

of the pure odd ray `2 beta_d`.

No semiregularity assertion is required for this identity.

## 4. Pullback to the two RM polarizations

As in `L031`, let

```text
D=g^*Theta,
H=(g^-1)^*Theta.
```

Set

```text
E_d^D := g^*E_d,
E_d^H := (g^-1)^*E_d
```

and

```text
P_d^D := E_d^D direct_sum (E_d^D)^vee[1],
P_d^H := E_d^H direct_sum (E_d^H)^vee[1].
```

Then

```text
ch(P_d^D)=2 beta_d^D,
ch(P_d^H)=2 beta_d^H,                       (4.1)
```

where

```text
beta_d^D=D-(d/6)D^3,
beta_d^H=H-(d/6)H^3.                       (4.2)
```

## 5. Exact target-ray object

`L031` established

```text
beta'
 = 2 beta_1^D - beta_2^D
   + beta_(q+1)^H - beta_1^H.              (5.1)
```

Multiplying by two and using (4.1) gives

```text
2 beta'
 = 2 ch(P_1^D)
   - ch(P_2^D)
   + ch(P_(q+1)^H)
   - ch(P_1^H).                             (5.2)
```

Therefore the direct sum with shifts

```text
T_split :=
  (P_1^D)^(direct_sum 2)
  direct_sum P_2^D[1]
  direct_sum P_(q+1)^H
  direct_sum P_1^H[1]                      (5.3)
```

is an explicit perfect object satisfying

```text
boxed[ ch(T_split)=2 beta' ].               (5.4)
```

Since multiplication of the target class by a nonzero scalar does not change its contraction kernel,

```text
rank(c_(ch(T_split)))=20,
ker(c_(ch(T_split)))=K_beta.                (5.5)
```

By semiregularity compatibility already used in `L007`,

```text
ker(ob_(T_split)) subset K_beta,
rank(ob_(T_split)) >=20.                   (5.6)
```

## 6. What is and is not solved

Equation (5.4) changes the status of the construction problem.

The campaign no longer needs to search for an abstract perfect object with Chern character on the `beta'` ray: such an object is explicit.

What is not known is whether the split representative `T_split` has the minimum obstruction rank. Because it is a direct sum, its obstruction kernel is the intersection of the obstruction kernels of its secant/dual summands. The source does not establish those kernels, and the semiregularity question for the genus-four secant objects remains open.

Thus the decisive target becomes

```text
rank(ob_T)=20
```

for either:

1. `T_split` itself; or
2. a non-split twisted complex with the same associated graded and hence the same `K_0` class.

The latter can use cross-Ext differential data to make diagonal obstruction classes boundaries, exactly in the sense of `L021`.

## 7. Why the derived dual is structurally useful

At the generic codimension-two surface point, `L039` computes for

```text
I=(f,g),
D=RHom(I,R)
```

that

```text
H^0(D)=R,
H^1(D)=R/I,
Ext^2_R(I,I)=0,
Ext^2_R(I,D)=R/I.                           (7.1)
```

Thus `E_d^vee[1]` is not merely a formal negative copy of `E_d`. It introduces a surface-supported cohomological term and nontrivial opposite channels in exactly the same support geometry. This is outside the line-bundle no-go `L036` and the distinct-support filtration no-go `L034`.

The remaining obstruction is global: one must compute the products into the `H^2(O_X)` and `H^1(I/I^2)` pieces isolated by `L039`.

## 8. HC-R021-L040 — explicit target-ray representative

### Statement

There exists an explicit perfect object `T_split` constructed from Markman's full-support secant objects and their derived duals such that

```text
ch(T_split)=2 beta'.
```

Its cohomological contraction map has rank exactly `20`. Its object obstruction map has rank at least `20`; equality is open.

### Proof

Sections 2-5.

QED.

## 9. Next finite obligation

Define

```text
DUAL-PAIR-A1:
  compute the global two-way Yoneda pairing for
  E_d and E_d^vee[1]
  on the H^2(O_X) and H^1(I/I^2) obstruction filtrations.
```

A positive factorization result would give a canonical way to replace the split `P_d` by a non-split pure-odd block with smaller obstruction kernel defect. A negative result would close the simplest full-support hyperbolic repair while leaving multi-block couplings in (5.3).

## 10. Claim boundary

```text
HC-R021-L040 = proved_in_solve_package_not_certified
explicit_perfect_object_on_2_beta_prime_ray = true
contraction_rank_of_T_split = 20
obstruction_rank_of_T_split = unknown_at_least_20
rank20_second_factor_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 11. Inputs

- Markman, arXiv:2502.03415, Example 8.2.3;
- `HC-R021-L007`, `L031`, `L039`;
- standard identity `ch_j(E^vee)=(-1)^j ch_j(E)` for perfect complexes;
- invariance of the contraction kernel under nonzero scalar multiplication.
