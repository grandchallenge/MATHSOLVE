# HC-R021-P4 — Traceless-Atiyah no-go for locally free bundles on a smooth divisor

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `e76c43ac107c50f24f5acf6c597560e15a218246`  
**State:** `LOCALLY_FREE_SMOOTH_DIVISOR_LANE_REFUTED__PERFECT_COMPLEX_FRONTIER_REMAINS`  
**Date:** 2026-09-16

## 1. Purpose

Decide the remaining smooth-divisor route after `HC-R021-L022` refuted the torsion-free elementary transform with codimension-two singular curves.

The result is negative in full generality for a **locally free vector bundle on a smooth divisor**.

If a pushforward `i_*F` deforms in both mixed kernel directions `k_7,k_8`, then the two rank-one characteristic distributions force the traceless Atiyah class of `F` to factor through a rank-one cotangent subsheaf. Its square therefore vanishes, so the normalized second Chern character of `F` is zero. Grothendieck-Riemann-Roch for the required `beta-prime` Chern character forces that normalized second Chern character to have nonzero pushforward. Contradiction.

Thus no locally free bundle on a smooth divisor can supply the missing rank-20 second factor.

## 2. Setup

Let `X` be the source abelian fourfold and use the real-multiplication normal form of `HC-R021-L006`:

```text
beta' = D - (q/6)H^3,
q>0,

k_7 = pi_1 + q a alpha_1,
k_8 = pi_2 + q b alpha_2,

pi_1=t_1 wedge t_2,
pi_2=t_3 wedge t_4,

V_1=span(t_1,t_2),
V_2=span(t_3,t_4),
V_1 intersect V_2=0.
```

Let

```text
i:S -> X
```

be a smooth connected divisor and let `F` be a vector bundle of rank `r>0` on `S`. Assume

```text
ch(i_*F)=M beta'
```

for some nonzero rational/integer scalar `M`; replacing the object by its shift changes the sign, so for the coherent pushforward case we take `M>0`.

Assume for contradiction that

```text
ob_(i_*F)(k_7)=ob_(i_*F)(k_8)=0.
```

## 3. GRR forces half-normal first Chern class

Let

```text
s := c_1(N_(S/X)) = i^*[S].
```

Grothendieck-Riemann-Roch for a smooth divisor gives

```text
ch(i_*F)
 = i_*[ch(F) td(N_(S/X))^(-1)],

td(N)^(-1)
 = (1-exp(-s))/s
 = 1 - s/2 + s^2/6 + ... .
```

### Degree two

The degree-two component is

```text
r [S] = M D.
```

Hence `[S]` is a positive rational multiple of the ample class `D`.

### Degree four

The target `M beta'` has no degree-four component, so

```text
i_*[c_1(F)-r s/2]=0.
```

For a smooth ample divisor in a fourfold, weak Lefschetz identifies `H^2(S,Q)` with `H^2(X,Q)` and the Gysin map on this group is injective: under the identification it is cup product with the ample class `[S]`, which is injective by hard Lefschetz/Lefschetz decomposition.

Therefore

```text
c_1(F)=r s/2
```

in `H^2(S,Q)`.

Define the normalized second Chern-character component

```text
kappa_2(F)
 := ch_2(F) - c_1(F)^2/(2r).
```

Equivalently, this is the degree-four part of

```text
ch(F) exp(-c_1(F)/r).
```

## 4. GRR forces kappa_2(F) to be nonzero

The degree-six component of GRR is

```text
i_*[ch_2(F) - (s/2)c_1(F) + r s^2/6].
```

Substituting `c_1(F)=rs/2` and

```text
ch_2(F)=kappa_2(F)+r s^2/8
```

gives

```text
ch_3(i_*F)
 = i_*kappa_2(F) + r [S]^3/24.
```

The required ray has degree-six component

```text
-(M q/6) H^3.
```

Hence

```text
i_*kappa_2(F)
 = -(M q/6) H^3 - r [S]^3/24.      (4.1)
```

This class is nonzero. Indeed, cup with any ample divisor, for example `D`, and integrate over `X`. Both `D H^3` and `D[S]^3` have strictly positive degree, while both coefficients on the right are strictly negative. Therefore

```text
i_*kappa_2(F) != 0,
```

and in particular

```text
kappa_2(F) != 0.
```

## 5. Mixed deformation directions give projective partial connections

The local noncommutative parts of `k_7,k_8` are `pi_1,pi_2`. The `H^2(O_X)` components are gerby/scalar data. They affect the scalar gluing of a lifted module but disappear after passing to the projective bundle or, equivalently, to the traceless Atiyah class.

For a smooth coisotropic support, first-order deformation of a vector bundle over a Poisson/algebroid deformation induces a partial connection along the characteristic distribution. In the Atiyah-class formulation this says that the traceless Atiyah class is zero after contraction with the characteristic distribution. This is the projective part of the standard `(1/2,1)`-connection criterion of Pecharich; scalar line/gerbe twists alter only the trace.

Let

```text
N^* := N^*_(S/X).
```

The two characteristic morphisms are

```text
p_i : N^* -> T_S,
p_i(n)=pi_i^sharp(n),
i=1,2.
```

Denote their image subsheaves by

```text
K_i := im(p_i) subset T_S.
```

Each `p_i` is generically nonzero. Since `N^*` is a line bundle and `T_S` is torsion-free, each nonzero `p_i` is injective as a morphism of sheaves, so `K_i` is a torsion-free rank-one subsheaf.

Moreover

```text
K_1 subset V_1 tensor O_S,
K_2 subset V_2 tensor O_S,
```

and `V_1 intersect V_2=0`. Therefore

```text
K_1 intersect K_2=0
```

as subsheaves and

```text
K:=K_1 direct_sum K_2 subset T_S
```

is torsion-free of rank two.

The assumed vanishing of both mixed object obstructions supplies projective partial connections along both `K_i`. Because their intersection is zero, the two splittings combine to a projective partial connection along `K`.

## 6. The traceless Atiyah class factors through a rank-one cotangent subsheaf

Let

```text
At_0(F)
 in Ext^1_S(F,F tensor Omega^1_S)
```

be the traceless Atiyah class.

A projective partial connection along `K` is exactly a splitting of the traceless Atiyah extension after restriction to `K`. Equivalently, `At_0(F)` is represented through the annihilator of `K` in `Omega^1_S`.

Set

```text
A_K := ker[Omega^1_S -> Hom(K,O_S)].
```

Since `Omega^1_S` has rank three and `K` has generic rank two,

```text
A_K
```

is a torsion-free rank-one subsheaf of `Omega^1_S`.

Thus the traceless Atiyah class factors as

```text
F -> F tensor A_K[1]
     -> F tensor Omega^1_S[1].
```

The wedge map

```text
A_K tensor A_K -> Omega^2_S
```

is identically zero: it vanishes on the dense open set where `A_K` is a line subbundle, and its target `Omega^2_S` is torsion-free, so a morphism vanishing generically vanishes globally.

Consequently

```text
At_0(F) wedge At_0(F)=0
```

in

```text
Ext^2_S(F,F tensor Omega^2_S).
```

Taking the trace gives

```text
kappa_2(F)
 = (1/2) Tr(At_0(F)^2)
 = 0.                                      (6.1)
```

The identity between the normalized second Chern character and the square of the traceless Atiyah class is the standard Atiyah-class expression for Chern characters.

## 7. Contradiction

Equation (6.1) contradicts the nonzero GRR requirement (4.1).

Therefore a locally free bundle on a smooth divisor with Chern character on the nonzero `beta'` ray cannot deform in both mixed directions.

## 8. HC-R021-L023 — smooth-divisor locally-free no-go

### Statement

There is no smooth divisor `i:S->X` and vector bundle `F` on `S` such that simultaneously

```text
ch(i_*F)=M beta',  M!=0,
ob_(i_*F)(k_7)=0,
ob_(i_*F)(k_8)=0.
```

In particular no locally free smooth-divisor representative of the `beta'` ray has second-factor obstruction rank `20`.

### Proof

Sections 3-7.

QED.

## 9. Consequences

The sequence of divisor-based attempts is now exhausted at first order:

```text
Example 11.2.7 divisor-plus-curve gluing     refuted by L019
split line-bundle perfect complex             rank 22 by L015/L016
same-divisor Pic0 two-step extensions          pruned by L021
divisor elementary transform                  refuted by L022
locally free bundle on a smooth divisor       refuted by L023
```

The Pell/Diophantine constructions for rank-two bundles on a smooth divisor are therefore irrelevant to the rank-20 problem even when their Chern-character equations have integral solutions: `L023` rules them out uniformly.

The surviving second-factor frontier is genuinely derived/non-divisorial:

1. a non-formal perfect complex whose cohomology is not a vector bundle/torsion-free sheaf on one smooth divisor;
2. a coherent sheaf with different support geometry not covered by `L019`, `L022`, or `L023`;
3. an object obtained by a derived autoequivalence from a simpler rank-20 object, if an actual categorical transform producing the `beta'` ray can be found.

By `HC-R021-L018`, any Perry equivariant route remains downstream of such a rank-20 second factor.

## 10. Claim boundary

```text
HC-R021-L023 = proved_in_solve_package_not_certified
locally_free_smooth_divisor_rank20 = impossible
Pell_rank2_divisor_lane = pruned
second_factor_rank20_exists = open
nondivisorial_nonformal_perfect_lane = open
G3 = downstream_of_second_factor_rank20
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 11. Sources and inputs

- Jeremy Pecharich, *Deformations of vector bundles on coisotropic subvarieties via the Atiyah class*, arXiv:1010.3671, especially Theorem 1.1 and the `(1/2,1)`-connection description of first-order module deformations.
- Yukinobu Toda, *Deformations and Fourier-Mukai transforms*, for the decomposition of first-order category deformations into gerby, commutative, and Poisson parts.
- standard Grothendieck-Riemann-Roch for a smooth divisor;
- standard Atiyah-class formula for Chern characters;
- `HC-R021-L006`, `L013`, `L018`, and `L022`.
