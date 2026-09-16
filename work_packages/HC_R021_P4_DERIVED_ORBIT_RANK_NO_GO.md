# HC-R021-P4 — Hochschild-contraction rank separates the standard secant and RM beta-prime derived orbits

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `5d579b3ee73d5ec6563efe3d7db6e2161ef57adf`  
**State:** `STANDARD_GENUS4_SECANT_AUTOEQUIVALENCE_SHORTCUT_REFUTED`  
**Date:** 2026-09-16

## 1. Purpose

Test whether the unresolved RM second-factor class

```text
beta' = D - (q/6) H^3,
D=g^*Theta,
H=(g^-1)^*Theta,
```

can be obtained from the simpler genus-four secant class

```text
beta_d = Theta - (d/6) Theta^3
```

of Markman Example 8.2.4 by an actual derived autoequivalence of `X`.

It cannot.

The obstruction is stronger than Mukai-norm arithmetic: the rank of the Hochschild/Chern-character contraction map is invariant under derived equivalence. The standard secant class has contraction rank `12`; the RM class has contraction rank `20` by `HC-R021-L006`.

## 2. Derived invariance of the contraction rank

Let

```text
Phi : D^b(X) -> D^b(X)
```

be an exact Fourier-Mukai autoequivalence. It induces isomorphisms

```text
Phi^HH : HH^2(X) -> HH^2(X),
Phi_HH : HH_(-2)(X) -> HH_(-2)(X),
```

compatible with the Hochschild action and the Chern character. In HKR coordinates, after the standard Todd correction (trivial for an abelian variety), the square

```text
HT^2(X)  -- c_ch(E) -->  H_Omega^(-2)(X)
   |                         |
   | Phi^HH                  | Phi_HH
   v                         v
HT^2(X)  -- c_ch(Phi(E)) --> H_Omega^(-2)(X)
```

commutes.

Consequently

```text
rank(c_ch(Phi(E))) = rank(c_ch(E)).
```

This is the cohomological side of the usual derived invariance/functoriality of the Atiyah/Hochschild obstruction and semiregularity diagrams.

Markman recalls that every integral Hodge-spin action arising from an autoequivalence is realized in this manner; conversely the cohomological action of an autoequivalence lies in `Spin_Hdg(V_X)`.

## 3. Standard genus-four secant class

Let

```text
beta_d := Theta - (d/6) Theta^3,
d>0,
```

on a principally polarized abelian fourfold. This is exactly the class occurring in Markman Example 8.2.4.

Choose holomorphic/anti-holomorphic bases so that

```text
Theta = sum_(i=1)^4 x_i y_i.
```

The HKR source is

```text
HT^2(X)
 = H^2(O_X)
   direct_sum H^1(T_X)
   direct_sum H^0(Lambda^2 T_X)
```

of dimension `6+16+6=28`.

As in `L006`, contraction splits into the commutative block and the gerby/bivector block.

### 3.1 H^1(T) block

For

```text
xi in H^1(T_X),
```

we have

```text
xi contraction beta_d
 = (xi contraction Theta)
   - (d/6)(xi contraction Theta^3).
```

The two target components have different Hodge degree. Moreover

```text
xi contraction Theta^3
 = 3 (xi contraction Theta) Theta^2.
```

Hard Lefschetz makes cup product with `Theta^2` injective on `H^2(O_X)`. Hence the two components have the same kernel:

```text
ker = {xi : xi contraction Theta=0}.
```

The map

```text
H^1(T_X) -> H^2(O_X),
xi |-> xi contraction Theta
```

is the skew-symmetrization map after using the polarization to identify `T_X` with `Omega^1_X`; it is surjective of rank `6`. Therefore

```text
rank(C_B(beta_d))=6,
dim ker(C_B(beta_d))=10.
```

### 3.2 H^2(O) plus Lambda^2 T block

The remaining block is

```text
C_AC(beta_d):
H^2(O_X) direct_sum H^0(Lambda^2 T_X)
 -> H^3(Omega^1_X),
(alpha,pi) |-> alpha cup Theta -(d/6)(pi contraction Theta^3).
```

Both source summands have dimension `6`. Polarization identifies `Lambda^2 T_X` with `Lambda^2 Omega^1_X`; under this identification the two displayed maps have the same six-dimensional image in `H^3(Omega^1_X)`, up to a nonzero scalar and the natural Hodge-star identification. Equivalently, in the exterior basis `x_i,y_i`, each basis vector `y_i wedge y_j` maps to the same two-term basis pattern as the complementary bivector `t_k wedge t_l`, where `{i,j,k,l}={1,2,3,4}`.

Each summand map is injective. Thus

```text
rank(C_AC(beta_d))=6,
dim ker(C_AC(beta_d))=6.
```

### 3.3 Exact standard rank

The two target Hodge-degree blocks are independent, so

```text
rank(c_beta_d)=6+6=12,
dim ker(c_beta_d)=16.
```

This rank is independent of the positive scalar `d`.

## 4. Compare with the RM target

`HC-R021-L006` proves for

```text
beta' = g^*Theta - (q/6)(g^-1)^*(Theta^3),
```

with `Nm(f)=1` and `f^2 != 1`, that

```text
rank(c_beta')=20,
dim ker(c_beta')=8.
```

Therefore

```text
rank(c_beta_d) != rank(c_beta').
```

By Section 2 no Fourier-Mukai autoequivalence can map a nonzero multiple of `beta_d` to a nonzero multiple of `beta'`.

Scaling either class does not change contraction rank.

## 5. HC-R021-L024 — standard secant derived-orbit no-go

### Statement

For every positive `d`, the standard genus-four secant ray

```text
Q^x beta_d,
beta_d=Theta-(d/6)Theta^3,
```

and the RM target ray

```text
Q^x beta',
beta'=g^*Theta-(q/6)(g^-1)^*(Theta^3),
```

belong to distinct derived-autoequivalence orbits of `H^ev(X,Q)`.

In particular a semiregular/rank-minimal object on a standard `beta_d` ray, if available, cannot be transported to the RM second-factor ray by an autoequivalence of `D^b(X)`.

### Proof

Sections 2-4.

QED.

## 6. Relation to Mukai norm

The Mukai pairing supplies a weaker necessary test. For a principal polarization,

```text
(beta_d,beta_d)=8d.
```

For the RM class one obtains

```text
(beta',beta')=(q/3) integral_X D H^3,
```

which in the two-block RM normalization equals `4 q tau`, with

```text
tau = Tr_F/Q(f^4).
```

Thus norm matching would require

```text
d = q tau/2.
```

Even when this arithmetic condition is integral, `L024` shows that it is insufficient: contraction rank separates the orbits.

## 7. Consequence for the live frontier

The following categorical shortcut is closed:

```text
known/simpler standard genus-four beta_d object
       |
       +--> derived autoequivalence
       v
RM beta-prime rank-20 object
```

A surviving derived construction must therefore start from a class with the same contraction rank `20`, not from the standard one-polarization secant ray.

The live second-factor possibilities are now:

1. a genuinely non-formal perfect complex constructed directly on the `beta'` ray;
2. a coherent object with support geometry not covered by `L019`, `L022`, `L023`;
3. an autoequivalence image of some *other* class whose contraction rank is already `20` and whose object-level rank-minimality is independently established.

## 8. Claim boundary

```text
HC-R021-L024 = proved_in_solve_package_not_certified
rank_contraction_standard_beta_d = 12
rank_contraction_RM_beta_prime = 20
standard_beta_d_autoequivalence_to_beta_prime = impossible
second_factor_rank20_exists = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 9. Sources and inputs

- Eyal Markman, arXiv:2502.03415v2, Example 8.2.4 for `beta_d`, Section 5.1 for the cohomological action of autoequivalences and `Spin_Hdg(V_X)`.
- Eyal Markman, arXiv:2509.23079, Corollary 11.2.6 and Lemma 11.2.8 for `beta'`.
- derived invariance of Hochschild cohomology/homology and compatibility of the Chern character action;
- `HC-R021-L006`.
