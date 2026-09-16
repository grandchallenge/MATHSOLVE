# HC-R021-P4 — q=1 ordinary-secanta kernel alignment and the K-preserving RM plane

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `69d5b830c992aae561e1a7a827bf7b6dc237c8a5`  
**State:** `Q1_STANDARD_SECANT_RAY_CONTAINS_TARGET_EIGHT_KERNEL__OBJECT_LEVEL_VANISHING_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

After `L025-L028` close the natural divisor-block repairs, identify a class whose **cohomological** contraction already annihilates all eight target directions

```text
K_beta := span(k_1,...,k_8)=ker(c_beta').
```

For the source-admissible tranche `q=1`, the ordinary genus-four secant ray of Markman Example 8.2.4 has exactly this property. More precisely, the standard class

```text
beta_1 := Theta-(1/6)Theta^3
```

has

```text
K_beta subset ker(c_beta_1).
```

This does not prove that Markman's object `F_1` has object-level obstruction kernel containing `K_beta`; it identifies `F_1` as the first natural non-divisorial bridge candidate whose Chern character passes the mixed-direction test before any extension engineering.

The package also determines the entire two-dimensional RM degree-(2,6) subspace annihilated by `K_beta` and proves that the ordinary same-polarization secant ray is unique inside it.

## 2. RM coordinates

Use the normal form of `L006`:

```text
D=U+V,
H=aU+bV,
ab=1,
a,b>0,
a!=b,

k_7=pi_1+q a alpha_1,
k_8=pi_2+q b alpha_2,
```

with

```text
alpha_1=y_1 wedge y_2,
alpha_2=y_3 wedge y_4,
pi_1=t_1 wedge t_2,
pi_2=t_3 wedge t_4.
```

Write

```text
tau:=a+b.
```

The six classes `k_1,...,k_6` are the simultaneous first-order Hodge-preserving directions for `D` and `H` by `L013`.

## 3. The complete K_beta-preserving degree-(2,6) plane

Consider an arbitrary class in the RM degree-(2,6) subspace

```text
gamma
 = rU+sV
   + C U^2 V
   + E U V^2.                              (3.1)
```

The six ordinary directions annihilate every such class because they preserve the two RM blocks separately. It remains to impose the two mixed equations.

The contractions are, up to the common fixed exterior-sign convention already used in `L006`,

```text
alpha_1 contraction/cup (rU+sV)
   = s (alpha_1 V),

pi_1 contraction (C U^2V+E UV^2)
   = 2C (alpha_1 V),
```

and similarly

```text
alpha_2 contraction/cup (rU+sV)
   = r (alpha_2 U),

pi_2 contraction (C U^2V+E UV^2)
   = 2E (alpha_2 U).
```

Therefore

```text
k_7 contraction gamma=0
```

if and only if

```text
2C+q a s=0,
```

while

```text
k_8 contraction gamma=0
```

if and only if

```text
2E+q b r=0.
```

Hence the complete RM degree-(2,6) subspace annihilated by all eight target directions is

```text
W_K
 = {
     gamma(r,s)
       = rU+sV
         -(q a s/2) U^2V
         -(q b r/2) UV^2
     : r,s in C
   }.                                      (3.2)
```

It is two-dimensional.

The target class itself is the point `(r,s)=(1,1)`:

```text
beta'
 = D-(q/6)H^3
 = U+V-(q a/2)U^2V-(q b/2)UV^2.
```

Thus `W_K` is the exact cohomological plane in which a useful bridge class must live if it is to be individually compatible with the eight target directions.

## 4. Standard secant classes in W_K

Let

```text
L=rU+sV,
r,s>0,
```

be an ample RM-plane class and consider the ordinary same-polarization secant class

```text
beta_(L,d):=L-(d/6)L^3,
d>0.
```

Since

```text
L^3=3r^2s U^2V+3rs^2 UV^2,
```

membership in `W_K` requires

```text
d r^2 = q a,
d s^2 = q b.                              (4.1)
```

Taking the ratio and using `ab=1` gives

```text
s/r=sqrt(b/a)=b.
```

Consequently the positive polarization ray is uniquely determined:

```text
L proportional to (1+a)U+(1+b)V=D+H.       (4.2)
```

Indeed `(1+b)/(1+a)=b` because `ab=1`.

Write

```text
L=m(D+H).
```

Then (4.1) gives the unique secant parameter

```text
d = q/[m^2(tau+2)],                       (4.3)
```

because

```text
(1+a)^2/a=(1+b)^2/b=tau+2.
```

### HC-R021-L029a — unique standard secant ray

Among positive standard same-polarization classes `L-dL^3/6` in the RM plane, the classes annihilated by all eight target directions are exactly the ray (4.2), with parameter (4.3).

This is a cohomological uniqueness statement; it makes no assertion about the obstruction map of an object realizing the class.

## 5. q=1 gives the ordinary d=1 genus-four secant class

Now specialize to

```text
q=1.
```

Let

```text
lambda=sigma_1(f),
```

so the normal form has

```text
a=lambda^(-4),
b=lambda^4.
```

Because

```text
D=g^*Theta=f^2 · Theta,
H=(g^-1)^*Theta=f^(-2) · Theta,
```

the original principal polarization has RM coordinates

```text
Theta=lambda^(-2)U+lambda^2 V
     =sqrt(a)U+sqrt(b)V.                   (5.1)
```

Set

```text
t:=Tr_F/Q(f^2)=lambda^2+lambda^(-2).
```

Then

```text
D+H=t Theta,                               (5.2)
```

and

```text
t^2=tau+2.                                 (5.3)
```

Take `L=D+H=tTheta`, so `m=1` in (4.3). For `q=1`,

```text
d_L=1/(tau+2)=1/t^2.
```

Therefore

```text
L-(d_L/6)L^3
 = tTheta-(1/(6t^2))t^3Theta^3
 = t[Theta-(1/6)Theta^3]
 = t beta_1.                               (5.4)
```

Since scaling does not change a contraction kernel,

```text
K_beta subset ker(c_beta_1).               (5.5)
```

This can also be seen directly from (5.1): the mixed kernel vectors of the standard `d=1` secant class include

```text
pi_1+a alpha_1=k_7,
pi_2+b alpha_2=k_8,
```

while `k_1,...,k_6` annihilate `Theta` because they annihilate both `D` and `H`.

By `L024`, the full standard-secanta contraction kernel has dimension `16`, so (5.5) is a strict inclusion in general:

```text
dim K_beta=8,
dim ker(c_beta_1)=16.
```

## 6. The explicit source object F_1

Markman Example 8.2.4 supplies, on the genus-four Jacobian, a coherent secant object

```text
F_d
```

with

```text
ch(F_d)=Theta-(d/6)Theta^3.
```

At `d=1`, this gives an explicit non-divisorial coherent object

```text
F_1
```

with

```text
ch(F_1)=beta_1.                            (6.1)
```

Equation (5.5) therefore proves the **cohomological necessary condition**

```text
k_i contraction ch(F_1)=0,
1<=i<=8.                                   (6.2)
```

This is the first natural object encountered in the present search for which both mixed target directions disappear already at the Chern-character level without cancellation between different objects.

It is not yet an object-level solution. Semiregularity compatibility gives only

```text
ob_(F_1)(k_i) in ker(sigma_(F_1));
```

it does not imply

```text
ob_(F_1)(k_i)=0.                           (6.3)
```

The source does not establish semiregularity for this genus-four object.

## 7. Exact next positive obligation

Define

```text
F1-BRIDGE-A1:
  prove or refute
  ob_(F_1)(k_i)=0 for i=1,...,8.
```

A positive result would make `F_1` a **K-compatible bridge object**: any later extension engineering using it would no longer need to cancel a diagonal mixed obstruction internal to the bridge itself.

This still would not put `F_1` on the `beta'` ray, because

```text
rank(c_beta_1)=12 != 20=rank(c_beta').
```

`L024` therefore continues to rule out a direct derived-autoequivalence transport from `beta_1` to `beta'`. The role of `F_1` here is different: it is a potential additional `K_0`-controlled bridge inside a longer non-formal construction.

A negative result at even one `k_i` would eliminate this particular bridge while leaving other classes in `W_K` available for investigation.

## 8. HC-R021-L029 — q=1 standard-secanta kernel alignment

### Statement

For the source-admissible specialization `q=1`:

1. the RM degree-(2,6) classes annihilated by the full target kernel `K_beta` form the two-dimensional plane `W_K` of (3.2);
2. the unique positive ordinary same-polarization secant ray inside `W_K` is the `D+H` ray;
3. because `D+H=Tr(f^2)Theta`, that ray is exactly the ordinary genus-four `d=1` secant ray after scalar normalization;
4. therefore Markman's explicit object `F_1` satisfies

```text
K_beta subset ker(c_ch(F_1)).
```

No object-level vanishing `ob_(F_1)(k_i)=0` is claimed.

### Proof

Sections 3-6.

QED.

## 9. Scope and firewall

`L029` does **not** prove:

- that `F_1` is semiregular;
- that any of the eight object-level classes `ob_(F_1)(k_i)` vanish;
- that `F_1` can be used to construct a `beta'`-ray object;
- second-factor rank `20`;
- all-orders algebraicity transport;
- `HC-R021`;
- the Hodge conjecture.

It identifies a positive cohomological bridge candidate and an exact finite object-level test.

## 10. Current disposition

```text
HC-R021-L029 = proved_in_solve_package_not_certified
q1_K_preserving_RM_plane_dimension = 2
unique_positive_standard_secant_ray_in_plane = D_plus_H
q1_D_plus_H = Tr_f2_times_Theta
q1_beta1_contraction_kernel_contains_target_K = true
F1_object_level_target_eight_relations = open
F1_bridge_candidate = live
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 11. Inputs and sources

- `HC-R021-L006`, `L013`, `L024`, `L028`;
- Eyal Markman, arXiv:2509.23079v1, Corollary 11.2.6 and Example 11.2.7;
- Eyal Markman, arXiv:2502.03415v2, Example 8.2.4;
- standard exterior-algebra contraction in the RM normal form.
