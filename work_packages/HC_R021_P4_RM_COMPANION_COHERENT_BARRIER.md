# HC-R021-P4 — Coherent positivity barrier for the non-ample RM companion sector

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `ae855baa8e4a8ad1a123b712ba57772b58adf779`  
**State:** `COMPANION_RANK1_AND_SEMISTABLE_POSITIVE_RANK_REALIZATIONS_IMPOSSIBLE__DERIVED_OR_UNSTABLE_REQUIRED`  
**Date:** 2026-09-16

## 1. Purpose

Test whether the non-ample companion sector isolated in `HC-R021-L035` can be realized by the same coherent templates that produce the ordinary ample secant sector.

The answer is negative for the two most natural classes:

1. no rank-one torsion-free sheaf can have the full companion secant Chern character;
2. more generally, no positive-rank `Theta`-slope-semistable torsion-free sheaf can have a nonzero multiple of that full companion secant Chern character.

The obstruction is elementary positivity. The companion divisor has index two, and its square has **negative** degree against `Theta^2`. The desired secant Chern character forces the codimension-two defect/discriminant to be a positive multiple of that square.

This does not rule out an unstable coherent sheaf or a genuinely derived object.

## 2. The rational companion divisor

Use `L035`:

```text
Theta=Theta_1+Theta_2,
tildeTheta=Theta_1-Theta_2,
L_tilde:=sqrt(t) tildeTheta.
```

The class `L_tilde` is rational and nondegenerate of index two. After multiplying by one fixed positive integer if necessary, treat it as the first Chern class of a line bundle; all arguments below are homogeneous and unaffected by this denominator clearing.

Since each RM block has complex rank two,

```text
Theta_1^3=Theta_2^3=0.
```

A direct expansion gives

```text
L_tilde^2 Theta^2
 = t(Theta_1-Theta_2)^2(Theta_1+Theta_2)^2
 = -2t Theta_1^2 Theta_2^2.                (2.1)
```

The top intersection

```text
integral_X Theta_1^2 Theta_2^2
```

is positive in the principal-polarization normalization. Hence

```text
integral_X L_tilde^2 Theta^2 <0.           (2.2)
```

## 3. Full companion secant class

The quadratic companion plane `P_(K1)` is spanned by the real/imaginary parts formed from `tildeTheta`. In rational coordinates use

```text
L:=L_tilde=sqrt(t)tildeTheta.
```

Then

```text
sqrt(t)tildeBeta
 = L-[q/(6t)]L^3,
```

and the even companion is

```text
tildeAlpha
 = 1-[q/(2t)]L^2+[q^2/(24t^2)]L^4.
```

Thus the full rational companion secant class with rank one and first Chern class `L` is

```text
w_tilde
 := tildeAlpha+sqrt(t)tildeBeta
 = 1+L-[q/(2t)]L^2-[q/(6t)]L^3
   +[q^2/(24t^2)]L^4.                     (3.1)
```

Only the rank, first Chern class, and degree-four component are needed below.

## 4. Rank-one torsion-free realization is impossible

Suppose a rank-one torsion-free sheaf `E` had

```text
ch(E)=w_tilde.
```

Write its reflexive hull as a line bundle with first Chern class `L`; then

```text
E = I_Z tensor O_X(L)
```

away from codimension at least three, with an effective codimension-two cycle `[Z]_2` recording the degree-four defect. Consequently

```text
ch_2(E)=L^2/2-[Z]_2.                       (4.1)
```

Comparing with (3.1),

```text
L^2/2-[Z]_2 = -[q/(2t)]L^2,
```

so

```text
[Z]_2 = [(t+q)/(2t)] L^2.                 (4.2)
```

Cup with the ample class `Theta^2` and integrate. By (2.2), the right-hand side has strictly negative degree:

```text
integral_X [Z]_2 Theta^2 <0.               (4.3)
```

But a nonzero effective codimension-two cycle has strictly positive degree against `Theta^2`, while the zero cycle has degree zero. Contradiction.

### HC-R021-L037a — rank-one companion no-go

No rank-one torsion-free coherent sheaf on `X` has Chern character `w_tilde`, nor any positive scalar multiple realized with the corresponding rank and first Chern scaling.

## 5. Bogomolov obstruction for semistable positive rank

More generally suppose a torsion-free sheaf `E` of rank `r>0` has

```text
ch(E)=r w_tilde.
```

Then

```text
c1(E)=rL,
ch_2(E)=-[rq/(2t)]L^2.
```

Using

```text
ch_2(E)=c1(E)^2/2-c2(E),
```

we get

```text
c2(E)
 = [r^2/2+rq/(2t)]L^2.
```

The Bogomolov discriminant is

```text
Delta(E)
 :=2r c2(E)-(r-1)c1(E)^2
 =r^2(1+q/t)L^2.                          (5.1)
```

Hence, by (2.2),

```text
integral_X Delta(E) Theta^2 <0.            (5.2)
```

But every `mu_Theta`-semistable torsion-free sheaf in characteristic zero satisfies the Bogomolov inequality

```text
integral_X Delta(E) Theta^2 >=0.
```

Contradiction.

### HC-R021-L037b — semistable companion no-go

No positive-rank `mu_Theta`-semistable torsion-free sheaf can have Chern character `r w_tilde` for `r>0`.

The same conclusion holds after a common positive integral scaling used to clear the rational divisor lattice.

## 6. Relation to Markman's ordinary secant construction

For the ordinary ample sector, Markman's genus-four constructions start from a theta polarization and correct the positive line-bundle exponential by effective `W_2`, curve, and point loci.

Equation (4.2) shows why this template cannot simply be repeated with the companion divisor: the required codimension-two correction would have a negative degree with respect to the ambient principal polarization.

Thus the absence of an effective theta-type companion is structural, not a missing choice of translate.

## 7. Consequence for route design

Combine `L035-L037`:

```text
beta' = ordinary rank-12 sector
        + non-ample companion rank-12 sector.
```

For the companion sector:

- line-bundle-only twisted complexes are pruned by `L036`;
- rank-one torsion-free sheaves are impossible by `L037a`;
- semistable positive-rank torsion-free sheaves are impossible by `L037b`.

Therefore a successful companion object must be at least one of:

1. a genuinely derived non-line-bundle complex;
2. an unstable higher-rank coherent object with carefully controlled Harder-Narasimhan data;
3. a transform/correspondence construction whose individual cohomology sheaves do not themselves carry the full companion Chern character.

The first and third are now substantially more natural than trying to force an effective support model.

## 8. HC-R021-L037 — coherent companion positivity barrier

### Statement

The full non-ample RM companion secant class `w_tilde` admits neither a rank-one torsion-free coherent realization nor a positive-rank `Theta`-slope-semistable torsion-free realization.

The proof is the negative intersection

```text
L_tilde^2 Theta^2<0,
```

which contradicts respectively effectivity of the codimension-two defect and the Bogomolov inequality.

### Proof

Sections 2-5.

QED.

## 9. Scope and firewall

`L037` does **not** rule out:

- unstable higher-rank coherent sheaves;
- complexes with several cohomology sheaves;
- Fourier-Mukai/correspondence constructions;
- a companion object whose Chern character is only the pure odd class rather than the full rank-one secant class;
- a successful two-sector coupling;
- second-factor rank `20`;
- all-orders algebraicity transport;
- `HC-R021`;
- the Hodge conjecture.

## 10. Current disposition

```text
HC-R021-L037 = proved_in_solve_package_not_certified
companion_rank1_torsionfree = impossible
companion_semistable_positive_rank = impossible
companion_line_bundle_complex = impossible_by_L036
companion_genuinely_derived = live
companion_unstable_coherent = live
companion_transform_route = live
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 11. Inputs and sources

- `HC-R021-L035-L036`;
- Markman arXiv:2509.23079v1, Section 11.2.1 for `tildeTheta`, `tildeAlpha`, `tildeBeta`, and non-ampleness of `+-sqrt(t)tildeTheta`;
- positivity of intersections of effective cycles with powers of an ample divisor;
- Bogomolov inequality for slope-semistable torsion-free sheaves on a smooth projective variety in characteristic zero.