# HC-R021-P4 — Exact decomposition into the two quadratic RM secant sectors

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `d0eb7c868d75e5e989c043dff57807bda8620e73`  
**State:** `BETA_PRIME_MIXES_TWO_RANK12_QUADRATIC_SECANT_SECTORS__NONAMPLE_COMPANION_OBJECT_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Re-express the rank-20 RM target using the intrinsic decomposition of Markman's four-dimensional secant space

```text
B_(sqrt(-q) Theta)=P_(K0) direct_sum P_(K1)
```

from Section 11.2.1 of arXiv:2509.23079.

This reveals a construction route that is invisible in the divisor-block identities `L025-L034`:

> `beta'` is the sum of two nonzero classes lying on two different quadratic secant planes, each of contraction rank `12`.

The first is the ordinary ample secant sector. The second is a rational but non-ample real-multiplication companion sector. The unresolved categorical problem is therefore not to discover a third cohomological direction; it is to realize and couple the non-ample companion sector at object level.

## 2. Markman's basis of B

Let

```text
F=Q(sqrt(t)),
t>0 not a square,
Theta=Theta_1+Theta_2,
tildeTheta=Theta_1-Theta_2.
```

Markman defines

```text
alpha = 1-(q/2)Theta^2+(q^2/4!)Theta^4,
beta  = Theta-(q/3!)Theta^3,
```

and the analogous classes `tildeAlpha,tildeBeta` formed from `tildeTheta`. His Section 11.2.1 gives the rational basis

```text
{alpha, beta, tildeAlpha, sqrt(t) tildeBeta}
```

of `B_(sqrt(-q)Theta)`.

The degree `(2,6)` intersection is the graph

```text
r . Theta
  |->
-(q/2) Theta_1 Theta_2 gamma(r) . Theta,   (2.1)
```

where

```text
r in F,
gamma(a+b sqrt(t))=a-b sqrt(t).
```

Here `.` denotes the `F`-scalar structure on the RM Hodge subspace, not ordinary scalar multiplication in complex cohomology.

## 3. beta-prime is the graph point r=f^2

In the selected source datum

```text
Nm_F/Q(f)=1,
g^*Theta=f^2 . Theta.
```

Hence

```text
(g^-1)^*Theta=f^-2 . Theta=gamma(f^2) . Theta.
```

The target class

```text
beta'
 = g^*Theta-(q/6)(g^-1)^*(Theta^3)
```

is exactly the graph point (2.1) with

```text
r=f^2.                                     (3.1)
```

Write uniquely

```text
f^2=u+v sqrt(t),
u,v in Q.                                (3.2)
```

Linearity of the graph in `r`, together with the basis in Section 2, gives

```text
boxed[
 beta' = u beta + v sqrt(t) tildeBeta
].                                             (3.3)
```

This is an identity in rational even cohomology.

## 4. Both components are genuinely present

Because

```text
Nm(f^2)=1,
f^2 !=1,
```

neither coefficient in (3.2) can vanish.

If `v=0`, then `f^2=u in Q` and

```text
1=Nm(f^2)=u^2.
```

The two real embeddings of the square `f^2` are positive, so `u=1`, contrary to `f^2!=1`.

If `u=0`, then

```text
f^2=v sqrt(t)
```

has norm

```text
-v^2 t<0,
```

contrary to `Nm(f^2)=1`.

Thus

```text
u!=0,
v!=0.                                      (4.1)
```

This recovers geometrically Markman's observation that `beta'` belongs to neither quadratic secant plane `P_(K0)` nor `P_(K1)`.

## 5. The companion is a rational index-two divisor class

Set

```text
L_tilde := sqrt(t) tildeTheta.
```

Markman proves that `L_tilde` is rational and that neither `L_tilde` nor `-L_tilde` is ample. In the two RM blocks its eigenvalues have opposite signs, so it is nondegenerate of index two.

The companion class can be written

```text
sqrt(t) tildeBeta
 = L_tilde - [q/(6t)] L_tilde^3.           (5.1)
```

After clearing the fixed denominators needed to make `L_tilde` integral, (5.1) is an algebraic rational K-theory class built entirely from divisor powers. What is missing is a rank-minimal **object**, not algebraicity of the cohomology class itself.

In particular the obstruction encountered here is not the Hodge conjecture in disguise: an explicit split perfect complex with a multiple of (5.1) can be written by finite-difference identities among line bundles. The problem is to supply non-formal differential data with the correct Hochschild kernel.

## 6. Each quadratic sector has contraction rank 12

`HC-R021-L024` proves

```text
rank(c_beta)=12
```

for the ordinary secant class `beta`.

The same exterior-linear calculation applies to `sqrt(t)tildeBeta`. Positivity of the degree-two form is not used in the rank calculation; only nondegeneracy is needed. Since `L_tilde^4 !=0`, wedge/contraction by `L_tilde` gives the symplectic Lefschetz isomorphisms on the exterior algebra, and for every nonzero coefficient in (5.1)

```text
rank(c_(sqrt(t)tildeBeta))=12,
dim ker(c_(sqrt(t)tildeBeta))=16.          (6.1)
```

By contrast `L006` gives

```text
rank(c_beta')=20,
dim ker(c_beta')=8.                        (6.2)
```

Thus the rank-20 target is produced by a genuine mixing of two rank-12 quadratic secant sectors.

## 7. Why this does not contradict L024

`L024` proves that no derived autoequivalence can carry a **single** standard genus-four secant ray to `beta'`, because contraction rank is derived invariant.

Equation (3.3) is different. It writes `beta'` as a nontrivial linear combination of two rank-12 sectors. No single rank-12 class is being transported to rank `20`.

Accordingly the surviving categorical architecture is

```text
rank-12 K0 sector beta
          \
           >-- non-split coupling --> beta' rank 20 object
          /
rank-12 K1 companion sqrt(t)tildeBeta
```

rather than an autoequivalence shortcut.

## 8. Exact next obligations

### COMP-A — companion realization

Construct an object `T_tilde in D^b(X)` with

```text
ch(T_tilde)=m sqrt(t)tildeBeta,
m!=0,
```

whose degree-two obstruction kernel equals its 16-dimensional contraction kernel, or at minimum contains the eight target directions needed after coupling.

The ordinary theta-divisor construction does not apply directly because `L_tilde` is non-ample.

### COMP-B — coupling

Given a rank-minimal ordinary-sector object and a rank-minimal companion-sector object, determine whether a non-split filtered object can realize (3.3) and reduce the common kernel to exactly the eight-dimensional `ker(c_beta')`.

A split direct sum is generally insufficient: contraction with the two summands can cancel in (3.3), whereas a block-diagonal obstruction map requires termwise vanishing. The coupling has to categorify the graph cancellation.

### COMP-C — integral lattice

Bind the smallest integer `m` clearing the divisor and coefficient denominators in (5.1) for the exact source RM order. This is arithmetic bookkeeping, not the mathematical obstruction.

## 9. HC-R021-L035 — two-sector RM decomposition

### Statement

For the selected real-quadratic source datum, writing `f^2=u+v sqrt(t)` gives the exact decomposition

```text
beta'=u beta+v sqrt(t)tildeBeta,
u v !=0.
```

The two summands belong to the two different quadratic secant planes `P_(K0)` and `P_(K1)` and each has Hochschild-contraction rank `12`. The companion degree-two class `sqrt(t)tildeTheta` is rational, nondegenerate, and non-ample.

Therefore the rank-20 problem admits a new exact formulation: categorify the mixing of the ordinary ample rank-12 sector with the non-ample RM rank-12 companion sector.

### Proof

Sections 2-6.

QED.

## 10. Scope and firewall

`L035` does **not** prove:

- existence of a rank-minimal object on the companion ray;
- that the explicit genus-four ordinary secant sheaf is rank-minimal;
- that a split sum of the two sectors works;
- existence of a successful coupling;
- second-factor rank `20`;
- all-orders algebraicity transport;
- `HC-R021`;
- the Hodge conjecture.

## 11. Current disposition

```text
HC-R021-L035 = proved_in_solve_package_not_certified
beta_prime_two_quadratic_sector_decomposition = exact
both_sector_coefficients_nonzero = true
ordinary_sector_contraction_rank = 12
companion_sector_contraction_rank = 12
companion_divisor_class = rational_nondegenerate_index2_nonample
companion_rank_minimal_object = open
two_sector_nonsplit_coupling = open
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 12. Sources and inputs

- Eyal Markman, arXiv:2509.23079v1, Section 11.2.1, especially the decomposition `B=P_(K0) direct_sum P_(K1)`, equations (11.2.1), the basis `{alpha,beta,tildeAlpha,sqrt(t)tildeBeta}`, and Lemmas 11.2.3-11.2.4;
- `HC-R021-L006` and `L024`;
- exterior symplectic linear algebra for a nondegenerate two-form on an eight-dimensional real/four-dimensional complex vector space.