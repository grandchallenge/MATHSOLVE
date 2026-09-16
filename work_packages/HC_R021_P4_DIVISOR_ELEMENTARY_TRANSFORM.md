# HC-R021-P4 — Divisor-supported elementary-transform candidate on the beta-prime ray

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `20358ac7630b4c9a6033e352a3a9a425f82bd3fb`  
**State:** `SAME_RAY_SIMPLE_COHERENT_CANDIDATE__SIX_ORDINARY_DIRECTIONS_LIFT__TWO_MIXED_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Replace the Example 11.2.7 correction-curve gluing refuted by `HC-R021-L019` with a coherent second-factor construction whose generic support is a single smooth divisor.

The construction produces a simple coherent sheaf `E_div` with

```text
ch(E_div) = M beta',
beta' = D - (q/6)H^3,
```

for an explicit positive integer `M`, and it is relative over the six-dimensional simultaneous `D,H` Hodge locus. Consequently

```text
ob_E_div(k_i)=0,  i=1,...,6.
```

The two mixed relations `k_7,k_8` remain open. Thus this package supplies a new exact rank-20 candidate with only the genuinely generalized-deformation half left to test; it does not assert that the candidate lies in `D20`.

## 2. RM recurrence and a third principal polarization

Use the source assumptions of Markman Example 11.2.7:

```text
Nm(f)=1,
f^2 != 1,
hat_eta(f)=g^*,
g in Aut(X).
```

Set

```text
D := g^*Theta = f^2 · Theta,
H := (g^-1)^*Theta = f^-2 · Theta.
```

Because `g^*` preserves the integral first-cohomology lattice, the eigenvalue `f` is an algebraic integer; `Nm(f)=1` makes it a unit. Hence

```text
tau := Tr_F/Q(f^4)
```

is an integer. The two real embeddings of `f^4` are positive reciprocal numbers, and `f^2 != 1`, so

```text
tau > 2.
```

Define

```text
A := tau H - D.
```

Using `tau=f^4+f^-4` in the quadratic RM algebra,

```text
tau f^-2 - f^2 = f^-6.
```

Therefore

```text
A = f^-6 · Theta = (g^-3)^*Theta.
```

Thus `D,H,A` are all integral principal-polarization classes.

## 3. Curve-class identity

### HC-R021-L020a

In `H^6(X,Q)`,

```text
D H A = ((tau^2-1)/3) H^3.
```

### Proof

Write the real-multiplication decomposition

```text
Theta = U + V,
```

where the two two-dimensional RM blocks are `U,V`, and let the first embedding of `f` be `lambda`; the second is `lambda^-1`. Then

```text
D = lambda^2 U + lambda^-2 V,
H = lambda^-2 U + lambda^2 V,
A = lambda^-6 U + lambda^6 V,
tau = lambda^4 + lambda^-4.
```

Since `U^3=V^3=0`, both `DHA` and `H^3` are linear combinations of `U^2V` and `UV^2`. Direct multiplication gives the same scalar ratio on both basis classes:

```text
DHA / H^3 = (tau^2-1)/3.
```

QED.

In particular

```text
2 D H A = 4(tau^2-1) (H^3/6).
```

This is an integral curve class because the left side is an intersection of integral divisor classes.

## 4. A smooth divisor with a clean Chern character

Choose a smooth member

```text
S in |2D tensor P|
```

for a suitable degree-zero twist `P`; `2D` is globally generated on an abelian variety and a general member is smooth. Let

```text
i:S -> X.
```

Set

```text
B_P := i_* O_S(D) tensor P'.
```

where `P'` is any degree-zero line bundle (absorbed into the notation below). Degree-zero twists do not change the rational Chern character. The standard divisor resolution gives

```text
ch(B_P)
 = exp(D)(1-exp(-2D))
 = exp(D)-exp(-D)
 = 2D + (1/3)D^3.
```

There are no degree-four or degree-eight terms.

## 5. Complete-intersection correction curves inside S

Write the positive rational source parameter in lowest terms as

```text
q = p/s,
p,s positive integers.
```

Choose an auxiliary positive integer `L` and set

```text
R := 6 s (tau^2-1) L,
M := 2R,
n_D := R/6 = s(tau^2-1)L,
n_H := Rq/[2(tau^2-1)] = 3pL.
```

All are positive integers.

Inside the smooth threefold `S`, choose sufficiently general translated complete intersections of the following two types.

### D-type

```text
C_D = S intersect D_1 intersect D_2,
```

with `D_1,D_2` translates of theta divisors of class `D`. Then

```text
[C_D]=2D^3.
```

### H-type

```text
C_H = S intersect H_1 intersect A_1,
```

where `H_1,A_1` are general translates with classes `H,A`. By `L020a`,

```text
[C_H]
 = 2DHA
 = 2(tau^2-1)H^3/3.
```

Take `n_D` D-type and `n_H` H-type curves in sufficiently general position; their one-cycle class is

```text
[C]
 = n_D (2D^3) + n_H (2(tau^2-1)H^3/3)
 = (R/3)D^3 + (Rq/3)H^3.
```

Pairwise zero-dimensional intersections, if retained rather than avoided, affect only the degree-eight bookkeeping and can be absorbed in the point correction of Section 7. The degree-six identity is exact.

## 6. Quotient line bundles and Euler characteristics

Take `R` generic degree-zero twists

```text
B_j := i_* (O_S(D) tensor P_j),
j=1,...,R.
```

All have the same Chern character `2D+D^3/3`.

The quotient along the D-type curves uses line bundles numerically equivalent to

```text
L_D := O_C(2D).
```

Adjunction for `C_D=S cap D_1 cap D_2` gives

```text
K_C_D = O_C(4D),
g(C_D)-1 = 2 D.C_D.
```

Hence

```text
chi(L_D)=deg(2D|C_D)+1-g(C_D)=0.
```

The difference between `L_D` and a source restriction `O_C(D) tensor P_j` is a degree-zero twist of the principal polarization `D`. By varying `P_j`, the unique theta sections give maps whose restrictions generate `L_D` pointwise; after increasing `L` if needed, a finite generating subcollection exists.

For an H-type curve use line bundles numerically equivalent to

```text
L_H := O_C(D+H).
```

The RM identity also gives

```text
D.C_H = (tau/2) H.C_H.
```

Adjunction gives

```text
K_C_H = O_C(D+(tau+1)H).
```

Therefore

```text
chi(L_H)
 = (D+H).C_H - (g(C_H)-1)
 = ((2-tau)/4) H.C_H
 < 0.
```

Again the difference between `L_H` and a source restriction is a degree-zero twist of the principal polarization `H`; varying the `P_j` supplies theta sections, and sufficiently many source summands generate the quotient along each curve.

## 7. Point correction and elementary transform

Let `Q_C` be the direct sum of the selected D-type `L_D` and H-type `L_H` quotient sheaves, with the finite-intersection corrections included if the chosen curves are not disjoint.

Its degree-six Chern character is exactly `[C]`. Let

```text
chi_C := chi(Q_C).
```

The D-type contribution is zero and the H-type contribution is negative; after the harmless finite-intersection corrections, choose the curves/generators and, if necessary, increase `L` so that the resulting Euler discrepancy is nonpositive. Choose a zero-dimensional quotient `Q_0` of total length

```text
-length(chi_C) = -chi_C >= 0
```

at points of the smooth support away from the curves. Then

```text
ch(Q_C direct_sum Q_0) = [C]
```

with no degree-eight term.

Choose the degree-zero twists and theta-section maps generically so that there is a surjection

```text
rho : direct_sum_(j=1)^R B_j -> Q_C direct_sum Q_0.
```

Define the elementary transform

```text
0 -> E_div -> direct_sum_(j=1)^R B_j
   -> Q_C direct_sum Q_0 -> 0.
```

Then

```text
ch(E_div)
 = R(2D+D^3/3) - [(R/3)D^3+(Rq/3)H^3]
 = 2R D - (Rq/3)H^3
 = M[D-(q/6)H^3]
 = M beta'.
```

Thus the Chern character lies on exactly the required source ray, with no degree-zero, degree-four, or degree-eight contamination.

## 8. Simplicity can be imposed generically

On `S`, let

```text
V := direct_sum_j O_S(D) tensor P_j.
```

Choose the `P_j` pairwise generic. For distinct generic degree-zero differences, the corresponding Hom spaces on the ample divisor vanish, so

```text
End(V) = direct_sum_j C.
```

The elementary-transform kernel is torsion-free on the smooth threefold `S`, with double dual `V`; hence any endomorphism of the kernel extends to an endomorphism of `V`.

Choose the quotient maps so that the incidence graph connecting source summands through the curve and point quotients is connected and every chosen source summand occurs nontrivially. Preservation of the kernel then forces all diagonal scalars in `End(V)` to be equal. Therefore, for a generic such quotient,

```text
End(E_div)=C.
```

So the candidate can be chosen simple.

This simplicity statement is useful but not required by Markman Lemma 11.2.8; the exact Chern character is the downstream cohomological input.

## 9. HC-R021-L020b — the six ordinary relations vanish

### Statement

The construction can be made relative over a local algebraic/analytic carrier whose tangent space at the source contains

```text
T_Hdg(D) intersect T_Hdg(H)
 = span(k_1,...,k_6).
```

Consequently

```text
ob_E_div(k_i)=0,
i=1,...,6.
```

### Proof

Along the simultaneous `D,H` Hodge locus, both integral polarization classes extend as relative line bundles after a local level/base change. Since

```text
A=tau H-D,
```
`A` extends as well.

The support `S` is cut out by a relative section of `2D`. The D-type and H-type curves are relative complete intersections of the relative `D,H,A` line bundles. Degree-zero twists and points extend in the relative Picard/abelian schemes. The quotient maps are supplied by theta sections of relative ample line bundles; higher cohomology of ample line bundles on abelian fibers vanishes, so after shrinking the base the relevant spaces of sections are locally free and the chosen generating maps extend. Surjectivity is open.

Thus the entire elementary-transform exact sequence extends to first order in every tangent direction preserving `D` and `H`. By the characteristic-obstruction theorem, its ambient obstruction vanishes on those directions. `HC-R021-L013` identifies them exactly with `k_1,...,k_6`.

QED.

## 10. HC-R021-L020 — new second-factor frontier

There exists a simple coherent sheaf `E_div` on `X` with

```text
ch(E_div)=M beta'
```

for an explicit positive integer `M`, and

```text
span(k_1,...,k_6) subset ker(ob_E_div).
```

Therefore

```text
20 <= rank(ob_E_div) <= 22.
```

The candidate lies in `D20` exactly when the two remaining mixed actions vanish:

```text
ob_E_div(k_7)=0,
ob_E_div(k_8)=0.
```

Unlike the Example 11.2.7 gluing, `E_div` has no open curve-supported component: generically it is a rank-`R` torsion-free sheaf on the single smooth divisor `S`. Hence `HC-R021-L019` does not apply.

## 11. Exact next calculation

Compute the two mixed characteristic actions on the elementary-transform triangle

```text
E_div -> V -> Q_C direct_sum Q_0 -> E_div[1].
```

The support `S` is a hypersurface and is automatically coisotropic for each rank-two bivector `pi_1,pi_2`; consequently there is no support-level local obstruction analogous to the correction curve. The remaining question is the global module/extension obstruction.

A positive result for both mixed classes proves

```text
rank(ob_E_div)=20
```

and supplies the second-factor first-order condition required by every surviving route after `L018`.

## 12. Claim boundary

```text
HC-R021-L020 = proved_in_solve_package_not_certified
new_same_ray_simple_coherent_candidate = constructed
ch_E_div = M_beta_prime
ordinary_k1_to_k6 = zero
mixed_k7_k8 = open
rank_ob_E_div = in_[20,22]
Example_11_2_7_D20 = empty_by_L019
second_factor_rank20 = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 13. Sources

- Eyal Markman, arXiv:2509.23079, Corollary 11.2.6 and Lemma 11.2.8 for the beta-prime ray and downstream Weil-projection interface.
- Eyal Markman, arXiv:2502.03415, Example 8.2.4, especially the clean genus-four identity `ch(e_*I_{W_2,p}(Theta))=Theta`, which motivates divisor-supported representatives.
- Standard global generation of `2L` for ample line bundles on abelian varieties, Bertini/Kleiman transversality for general translated complete intersections, and the characteristic-obstruction interpretation of first-order object deformations.
