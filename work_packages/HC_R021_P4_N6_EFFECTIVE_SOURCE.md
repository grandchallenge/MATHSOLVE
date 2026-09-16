# HC-R021-P4 — Explicit N=6 correction-curve tranche

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `20358ac7630b4c9a6033e352a3a9a425f82bd3fb`  
**State:** `CURVE_EFFECTIVITY_CONSTRUCTIVE_AT_N6__D20_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Make the curve-effectivity step in Markman Example 11.2.7 constructive for one bounded source tranche.

Markman chooses `d` sufficiently large and then asserts the existence of some positive integer `N` such that

```text
(N/6)(d D^3 - q H^3)
```

is the class of a curve, where

```text
D := g^*Theta,
H := (g^-1)^*Theta,
q > 0
```

and `q` is an integer in the genus-four CM4 example.

The present lemma gives an explicit choice

```text
N = 6
```

for infinitely many sufficiently large `d`.

It does not prove that the corresponding glued sheaf lies in `D20`.

## 2. Ample classes

Both `D` and `H` are integral ample divisor classes: they are pullbacks of the principal polarization `Theta` by automorphisms of `X`.

Fix an integer `m>>0` and set

```text
A := mD - H.
```

The ample cone is open in `NS(X)_R`, and

```text
A/m = D - (1/m)H -> D
```

as `m -> infinity`. Hence `A` is ample for all sufficiently large `m`. It is integral because `D,H` are integral.

Set

```text
d := q m^3.
```

Then `d` is a positive integer and can be made arbitrarily large.

## 3. Factorization of the correction class

We have the exact identity

```text
d D^3 - q H^3
 = q(m^3 D^3 - H^3)
 = q(mD-H)(m^2 D^2 + m D H + H^2)
 = q[m^2 A D^2 + m A D H + A H^2].
```

Thus for `N=6` Markman's desired curve class becomes

```text
Gamma_6
 := (6/6)(dD^3-qH^3)
  = q[m^2 A D^2 + m A D H + A H^2].
```

Every coefficient is a positive integer.

## 4. Effective curve representatives

For any three ample divisor classes on an abelian fourfold, general effective divisors in suitable translates of the corresponding ample line bundles meet properly in an effective one-dimensional complete-intersection cycle with the cup-product class of the three divisors.

Translations do not change cohomology classes. Therefore we may choose effective curves with classes

```text
A D^2,
A D H,
A H^2.
```

Taking respectively

```text
q m^2,
q m,
q
```

general translated copies and taking their scheme-theoretic union with reduced structure gives an effective pure one-dimensional subscheme `C'_6` whose fundamental cycle has class

```text
[C'_6] = Gamma_6.
```

If desired, the translated components can be chosen in incidence chains rather than independently so that the support is connected; connectedness is not used in the cohomology calculation below.

Hence the curve-class existence step of Example 11.2.7 can be satisfied with

```text
N=6,
d=q m^3
```

for every sufficiently large `m`.

## 5. HC-R021-L012 — bounded effectivity multiplier

### Statement

In the exact CM4 source datum of Example 11.2.7, for every positive integer `q` and all sufficiently large integers `m`, the choice

```text
N=6,
d=q m^3
```

admits an explicit effective curve representative of

```text
(N/6)(d g^*(Theta^3)-q(g^-1)^*(Theta^3)).
```

### Proof

Sections 2-4.

QED.

## 6. Consequences and non-consequences

This closes only the numerical/effectivity ambiguity in one source tranche.

It gives a bounded concrete search family:

```text
N = 6,
d = q m^3,
m sufficiently large.
```

It does **not** prove:

- that a selected gluing in this tranche lies in the rank-20 locus `D20`;
- that all eight `HC-R021-L007` Yoneda relations vanish;
- weak equivariant semiregularity;
- all-orders deformation transport.

It also shows why the exceptional numerical possibility left by `HC-R021-L011` must not be promoted into an existence claim. Markman's published effectivity argument supplies only some positive `N`; the constructive tranche here has `N=6`, so

```text
qN = 6q >= 6.
```

Consequently the naive transitive pure-translation dimension argument of `L011` is unavailable on this explicit tranche.

## 7. Exact next use

Use `C'_6` as the correction curve in the universal gluing construction of `HC-R021-L010`; choose six generic translated secant constituents and constituent-wise fiber gluings. The resulting finite-type subfamily of `S_adm` has no unspecified curve-effectivity multiplier.

The remaining direct obligation on that subfamily is still

```text
D20 != empty.
```

## 8. Claim boundary

```text
HC-R021-L012 = proved_in_solve_package_not_certified
explicit_effectivity_multiplier = 6
explicit_d_family = q*m^3
D20_nonempty = open
P4_A1 = open_conditional_on_D20
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 9. Sources

- Eyal Markman, arXiv:2509.23079, Corollary 11.2.6 and Example 11.2.7.
- `work_packages/HC_R021_P4_GLUE_PARAMETER_STACK.md` for the admissible gluing-family interface.
