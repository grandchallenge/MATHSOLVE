# HC-R021-P4 — Direct beta-prime perfect complex from RM theta-square cones

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `1dfb41a54187b7dba225623a8db2b9d009992c77`  
**State:** `EXPLICIT_NON_SPLIT_PERFECT_COMPLEX_ON_BETA_PRIME_RAY__OBSTRUCTION_RANK_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Use the positive-secanta cone mechanism of `HC-R021-L046` together with the exact RM complete-intersection identity of `HC-R021-L020a` to construct an explicit perfect complex directly on the required source ray

```text
beta' = D - (q/6) H^3.
```

This avoids the non-ample companion decomposition and the three-divisor K-theory identities of `L025-L028`.

The construction is object-level and genuinely non-formal inside each block. It does not yet establish the required eight Hochschild nullhomotopies or obstruction rank `20`.

## 2. RM data

Retain the source notation of `L020`:

```text
D := g^* Theta = f^2 . Theta,
H := (g^-1)^* Theta = f^-2 . Theta,
tau := Tr_F/Q(f^4) in Z,
A := tau H - D = (g^-3)^* Theta.
```

The source assumptions imply

```text
tau > 2,
```

and `D,H,A` are integral principal-polarization classes.

The exact curve-class identity `HC-R021-L020a` is

```text
D H A = ((tau^2-1)/3) H^3.                  (2.1)
```

Write the positive rational source parameter in lowest terms as

```text
q = p/s,
p,s positive integers.                     (2.2)
```

The source-relevant integral case is `s=1`; keeping `s` makes the arithmetic transparent.

## 3. A D-theta block with arbitrary curve multiplicity

Because `D=g^*Theta` is a principal polarization obtained from the original Jacobian theta class by an automorphism, the standard genus-four theta/W2 geometry transports to `D`.

Choose a theta translate

```text
Delta_j in |D tensor P_j|
```

and a transported/translated Abel-Jacobi surface

```text
T_j subset Delta_j
```

with the standard Chern character

```text
ch(O_(T_j))
 = D^2/2 - D^3/3 + degree_8.                (3.1)
```

For an integer `r_j >= 0`, choose sufficiently general pairs of translated theta divisors

```text
H_(j,l) of class H,
A_(j,l) of class A,
1 <= l <= r_j,
```

and define complete-intersection curves

```text
C_(j,l)
 := Delta_j cap H_(j,l) cap A_(j,l).         (3.2)
```

For general choices these are local complete-intersection curves, no curve is contained in `T_j`, and all intersections among `T_j` and the `C_(j,l)` which are not forced to be positive-dimensional are zero-dimensional.

Their one-cycle classes are

```text
[C_(j,l)]
 = D H A
 = ((tau^2-1)/3) H^3.                       (3.3)
```

Set

```text
Z_j
 := T_j union C_(j,1) union ... union C_(j,r_j).
```

Every component of `Z_j` is contained in `Delta_j`.

Let

```text
L_j := O_X(Delta_j),
E_j := I_(Z_j) tensor L_j.                  (3.4)
```

Since `X` is smooth, `E_j` is perfect.

## 4. Exact odd Chern character of a block

The zero-dimensional intersections among the components of `Z_j` affect only degree eight. Therefore, through degree six,

```text
ch(O_(Z_j))
 = D^2/2 - D^3/3
   + sum_l [C_(j,l)]
   + degree_8.                               (4.1)
```

Hence

```text
ch(I_(Z_j))
 = 1 - D^2/2 + D^3/3
   - sum_l [C_(j,l)]
   + degree_8.                               (4.2)
```

Since `c_1(L_j)=D`, multiplication by `exp(D)` gives

```text
ch_1(E_j)=D,                                (4.3)
```

and

```text
ch_3(E_j)
 = D^3/6 - D^3/2 + D^3/3
   - sum_l [C_(j,l)]
 = - sum_l [C_(j,l)].                        (4.4)
```

Thus

```text
odd(ch(E_j))
 = D - r_j D H A.                            (4.5)
```

Using (2.1),

```text
odd(ch(E_j))
 = D - r_j ((tau^2-1)/3) H^3.               (4.6)
```

The `D^3` contribution of the Abel-Jacobi surface cancels exactly, as in `L045`.

## 5. Canonical non-split dual cone in each block

Let

```text
t_j in H^0(X,L_j)
```

be the theta section cutting out `Delta_j`.

Because `Z_j subset Delta_j`,

```text
t_j in H^0(I_(Z_j) tensor L_j).
```

Therefore

```text
t_j^2
 in H^0(I_(Z_j)^2 tensor L_j^2)             (5.1)
```

gives a degree-zero class in

```text
H^0(E_j tensor^L E_j)
 ~= Hom_D(E_j^vee,E_j).                      (5.2)
```

Let

```text
e_j:E_j^vee -> E_j                           (5.3)
```

be the corresponding morphism and define

```text
C_j := Cone(e_j).                             (5.4)
```

The map is not nullhomotopic: on the dense open complement of `Z_j`, it is multiplication by the nonzero section `t_j^2`.

Thus every `C_j` is a genuinely non-split perfect complex.

Perfect duality gives

```text
ch(C_j)
 = ch(E_j)-ch(E_j^vee)
 = 2 odd(ch(E_j))
 = 2D - 2 r_j D H A.                         (5.5)
```

## 6. Assemble the exact beta-prime ray

Set

```text
N := 2 s (tau^2-1).                          (6.1)
```

Choose nonnegative integers

```text
r_1,...,r_N
```

with

```text
sum_j r_j = p.                               (6.2)
```

There is no restriction requiring `r_j <= 1`; for any fixed finite multiplicity the complete-intersection curves in a block can be chosen generically.

Define

```text
C_beta'
 := direct_sum_(j=1)^N C_j.                 (6.3)
```

Summing (5.5) and using (6.2),

```text
ch(C_beta')
 = 2N D - 2p D H A
 = 2N D - 2p ((tau^2-1)/3) H^3.             (6.4)
```

On the other hand, from `q=p/s` and `N=2s(tau^2-1)`,

```text
2N beta'
 = 2N D - (Nq/3) H^3
 = 2N D - 2p ((tau^2-1)/3) H^3.             (6.5)
```

Therefore

```text
boxed:
ch(C_beta') = 2N beta'
            = 4s(tau^2-1) beta'.             (6.6)
```

This is the required nonzero integer multiple of the exact source class.

In the source-relevant integral case `q in Z_(>0)`, take simply

```text
s=1,
N=2(tau^2-1),
sum_j r_j=q.
```

## 7. What this construction changes

Before this package, explicit objects on the `beta'` ray were available in three forms:

1. the coherent elementary-transform candidate `L020`, with six ordinary relations already lifted but mixed actions open;
2. split perfect representatives such as `L015/L040`, whose object obstruction is too large;
3. K-theory identities from `L025-L028`, whose natural differentials were pruned.

The present object is different:

- its Chern character is directly on `beta'`;
- every summand is internally non-split;
- the cubic `H^3` correction is carried geometrically by explicit `D-H-A` complete-intersection curves;
- no non-ample companion polarization is required;
- no formal subtraction of a `J=D+qH` divisor block is required.

Thus the existence of a genuinely non-formal target-ray perfect object is no longer an open subproblem.

## 8. Local form along a correction curve

At a general point of a correction curve away from `T_j` and all other curves, choose regular parameters so that

```text
Delta_j=(t=0),
C_(j,l)=(t,u,v)=0.
```

Then locally

```text
I_(Z_j)=(t,u,v),
```

and `e_j` is represented by the tensor-square class `t^2`.

This is materially different from the divisor-supported coherent elementary transform of `L020`: the cone contains a curve-supported higher-cohomology correction arising from the derived dual of the codimension-three ideal. Hence the characteristic-foliation no-go for an ordinary quotient on a divisor cannot simply be imported as an obstruction to `C_j`.

The selected mixed Hochschild actions must be computed on this local/global cone itself.

## 9. Remaining exact obligations

The construction does not establish semiregularity. The next obligations are now concrete:

1. compute `Ext^{<0}(C_beta',C_beta')` or show it is irrelevant to the exact Markman/Perry interface used downstream;
2. compute the selected characteristic actions

```text
ob_(C_beta')(k_i), i=1,...,8;
```

3. determine whether the six ordinary directions lift object-level for the chosen theta/surface/curve data;
4. compute the two mixed actions on the local model `(t,u,v; t^2)` and globalize them;
5. if the direct sum still has excess obstruction rank, introduce cross-block extension data while preserving (6.6).

The exact cohomological lower bound remains

```text
rank(ob_(C_beta')) >= 20
```

by the semiregularity/contraction compatibility already established in `L006-L007`.

## 10. HC-R021-L047 — direct beta-prime cone construction

### Statement

For every positive rational source parameter `q=p/s` satisfying the source RM hypotheses, there exists an explicit perfect complex `C_beta'` on the source abelian fourfold such that

```text
ch(C_beta')
 = 4s(tau^2-1) beta',
```

and `C_beta'` is a finite direct sum of genuinely non-split derived-dual cones whose curve corrections are explicit complete intersections of the three principal polarizations `D,H,A`.

### Proof

Sections 2-6.

QED.

## 11. Claim boundary

```text
HC-R021-L047 = proved_in_solve_package_not_certified
explicit_nonformal_beta_prime_perfect_complex = constructed
ch = 4s(tau^2-1) beta_prime
object_obstruction_rank = open
ordinary_k1_to_k6_for_L047 = open
mixed_k7_k8_for_L047 = open
Ext_negative_for_L047 = open
second_factor_rank20 = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

This is a Solve-package construction and not a MATHCERT disposition.

## 12. Inputs

- `HC-R021-L020a`: `D H A=((tau^2-1)/3)H^3`, with `D,H,A` principal polarizations;
- `HC-R021-L045`: theta-square dual-cone local model;
- `HC-R021-L046`: positive-secanta derived-dual cone mechanism;
- Markman, arXiv:2502.03415, Example 8.2.4 and Lemma 8.2.5 for the transported genus-four theta/W2 Chern-character identity.
