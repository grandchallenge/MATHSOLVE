# HC-R021-P4 — The q=1 ordinary genus-four secant object is not a mixed bridge

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `76dfe80141828a57cc634a34a69ba87d85a3c9c8`  
**State:** `Q1_F1_COHOMOLOGICALLY_ALIGNED__OBJECT_LEVEL_MIXED_PAIR_CANNOT_BOTH_VANISH`  
**Date:** 2026-09-16

## 1. Purpose

Decide the object-level test left open by `HC-R021-L029`.

For `q=1`, `L029` proves that the eight-dimensional target contraction kernel

```text
K_beta := span(k_1,...,k_8)
```

is contained in the contraction kernel of the ordinary genus-four secant class

```text
beta_1=Theta-(1/6)Theta^3.
```

Markman Example 8.2.4 supplies the explicit coherent secant sheaf

```text
F_1=e_* I_(Z_1/Theta)(Theta),
ch(F_1)=beta_1.
```

Thus `F_1` is cohomologically compatible with both mixed target directions `k_7,k_8`. The remaining question was whether

```text
ob_(F_1)(k_7)=ob_(F_1)(k_8)=0
```

objectwise.

The answer is negative. The Abel-Jacobi correction curve in the non-locally-free locus of `F_1` would have to be invariant under the characteristic foliation of both mixed Poisson directions. At every smooth theta point at least one of the two characteristic lines is nonzero, and each lies in one of the fixed complementary RM planes `V_1,V_2`. This would force the tangent directions of the Abel-Jacobi curve generically into a fixed two-plane, contradicting the nondegeneracy of the canonical genus-four curve in `P^3`.

This closes the `F_1` bridge candidate without asserting anything about the full semiregularity map of `F_1`.

## 2. Source geometry of F_1

Use Markman, arXiv:2502.03415v2, Example 8.2.4.

Let `C` be a non-hyperelliptic genus-four curve with two `g^1_3`'s and

```text
X=Pic^3(C),
Theta=W_3,
e:Theta -> X.
```

Markman chooses a translate

```text
W_(2,p) subset Theta
```

and, for each secant parameter, translates

```text
C_i={p+p_i+q_i : p in C}
```

of the Abel-Jacobi curve `W_1=AJ(C)`. The source explicitly states that each `C_i` is contained in the smooth locus of `Theta`, and that

```text
Z_d=W_(2,p) union C_1 union ... union C_d,
F_d=e_* I_(Z_d/Theta)(Theta),
ch(F_d)=Theta-(d/6)Theta^3.
```

For `d=1`, choose a generic point

```text
x in C_1 \ W_(2,p).
```

Near `x`, `Theta` is smooth and the only component of `Z_1` present is the smooth curve `C_1`. Up to the harmless line-bundle twist `O_Theta(Theta)`, the local module underlying `F_1` is therefore

```text
I_(C_1/Theta).
```

This is a rank-one torsion-free module on the smooth threefold `Theta`, non-locally-free precisely along `C_1` near `x`.

## 3. Fitting loci are invariant under a partial connection

We use the local mechanism already underlying the curve argument in `L022`, and record it explicitly here.

Let `S` be a smooth local algebra, `M` a finitely presented `S`-module, and

```text
delta:S->S
```

a derivation. Suppose `M` has a `delta`-connection

```text
nabla_delta:M->M,

nabla_delta(sm)=delta(s)m+s nabla_delta(m).
```

Choose a finite presentation

```text
S^m --P--> S^n -> M -> 0.
```

After choosing lifts of the connection to the free modules, compatibility has the matrix form

```text
delta(P)=A P-P B
```

for suitable matrices `A,B`. Applying `delta` to any determinantal minor of `P` and using the Leibniz rule expresses the result as an `S`-linear combination of minors of the same size. Therefore every Fitting ideal of `M` is `delta`-stable.

### HC-R021-L030a — singular-locus invariance

If a coherent module on a smooth support admits a partial connection along a line distribution `K`, every Fitting stratum, in particular the non-locally-free locus, is invariant under `K`.

At a smooth point of an irreducible curve which is a generically reduced component of that locus, a nonzero characteristic line must therefore be contained in the tangent line of the curve.

## 4. Mixed Hochschild lifting induces the characteristic partial connection

Use the RM normal form of `L006`:

```text
k_7=pi_1+q a alpha_1,
pi_1=t_1 wedge t_2,
V_1=span(t_1,t_2),

k_8=pi_2+q b alpha_2,
pi_2=t_3 wedge t_4,
V_2=span(t_3,t_4),

V_1 intersect V_2=0,
V_1 direct_sum V_2=T_0X.
```

For the present package `q=1`, but the local characteristic argument is independent of that scalar.

Assume

```text
ob_(F_1)(k_i)=0
```

for one of `i=7,8`. By the characteristic obstruction/deformation correspondence used in `L019` and `L022`, the object lifts to the first-order category deformation defined by `k_i`.

Restrict to a sufficiently small affine/analytic neighborhood of a generic point of `C_1`. The `H^2(O_X)` gerby component is locally trivial, while the noncommutative part is the first-order Poisson deformation defined by `pi_i`. For a coherent module generically of positive rank on the smooth hypersurface `Theta`, such a lift induces the standard partial connection along the characteristic distribution

```text
K_i := im[N^*_(Theta/X) --pi_i^sharp--> T_Theta].
```

The gerby term changes only scalar gluing and does not change this characteristic distribution or the Fitting-locus argument.

Since `N^*_(Theta/X)` is a line bundle,

```text
rank K_i <=1,
```

and whenever nonzero,

```text
K_1 subset V_1 tensor O_Theta,
K_2 subset V_2 tensor O_Theta.             (4.1)
```

By `L030a`, if `ob_(F_1)(k_i)=0` and `K_i` is nonzero at a generic point of `C_1`, then

```text
T C_1 = K_i subset V_i                     (4.2)
```

generically along the curve.

## 5. The two characteristic lines cannot both vanish

Let `x` be a smooth point of `Theta` and let

```text
0 != n_x in N^*_(Theta/X,x) subset T_x^*X
```

be a conormal generator.

For the rank-two bivector `pi_1` with image `V_1`,

```text
pi_1^sharp(n_x)=0
```

if and only if `n_x` annihilates `V_1`. Likewise

```text
pi_2^sharp(n_x)=0
```

if and only if `n_x` annihilates `V_2`.

If both characteristic vectors vanished, `n_x` would annihilate

```text
V_1 direct_sum V_2=T_xX,
```

hence `n_x=0`, contradiction.

Therefore at every smooth theta point,

```text
K_1(x) !=0  or  K_2(x) !=0.               (5.1)
```

Since `C_1` is irreducible, at its generic point at least one fixed `K_i` is nonzero. If both object-level mixed obstructions vanished, (4.2) for that index would force

```text
T_x C_1 subset V_i
```

on a dense open subset of `C_1`.

## 6. Abel-Jacobi tangent directions are not contained in a fixed RM plane

The curve `C_1` is a translate of the Abel-Jacobi embedding of the non-hyperelliptic genus-four curve `C` into its Jacobian.

Translation identifies all tangent spaces of `X` with `T_0X`. Under the standard identification

```text
P(T_0X) = P(H^0(C,K_C)^*),
```

the projectivized tangent direction of the Abel-Jacobi curve at `p` is the canonical image of `p`.

Thus the tangent Gauss map of `C_1` is the canonical map

```text
C -> P^3.
```

Because `C` is non-hyperelliptic of genus four, the canonical map is an embedding and its image is nondegenerate in `P^3`. In particular it is not contained in either projective line

```text
P(V_1),
P(V_2).
```

Hence the generic containment (4.2) is impossible for either `i`.

## 7. HC-R021-L030 — F_1 mixed bridge no-go

### Statement

For Markman's genus-four object

```text
F_1=e_* I_(Z_1/Theta)(Theta)
```

of Example 8.2.4, in the `q=1` RM target setting of `L029`, the two mixed target obstructions cannot both vanish:

```text
not [ ob_(F_1)(k_7)=0 and ob_(F_1)(k_8)=0 ].
```

Consequently `F_1` cannot serve as a bridge object individually compatible with the full target kernel `K_beta`, despite the cohomological inclusion

```text
K_beta subset ker(c_ch(F_1))
```

proved in `L029`.

### Proof

Assume both obstruction classes vanish. Sections 4 and 5 imply that at the generic point of the Abel-Jacobi component `C_1`, one of the two nonzero characteristic lines forces the tangent line of `C_1` into the fixed plane `V_1` or `V_2`. Section 6 shows that the Abel-Jacobi tangent Gauss image is the nondegenerate canonical genus-four curve and cannot lie in either projective line. Contradiction.

QED.

## 8. Extension to every d>0 in Example 8.2.4

The same argument applies to every `F_d` of Example 8.2.4. Each `Z_d` contains at least one Abel-Jacobi component `C_i` lying in the smooth locus of `Theta`. At a generic point of `C_i` away from the other components, the local module is `I_(C_i/Theta)` up to line-bundle twist. Therefore simultaneous mixed lifting in the two complementary rank-two Poisson directions is impossible for every `d>0`.

This statement concerns the selected pair of RM mixed directions. It does not assert that `F_d` has no other deformations or determine its full obstruction rank.

## 9. Consequence for the search

The positive cohomological alignment of `L029` was real but insufficient. It shows exactly why trace/Chern-character cancellation can conceal a surviving object-level obstruction even for a geometrically natural non-divisorial sheaf.

The following candidate is now closed:

```text
q=1 ordinary beta_1 secant object F_1
   cohomological target-eight compatibility     [L029]
   object-level simultaneous mixed compatibility [REFUTED L030]
```

The next bridge must therefore avoid a one-dimensional non-locally-free locus whose tangent Gauss image is incompatible with the mixed characteristic distributions. High-value surviving mechanisms are:

1. a genuinely derived bridge whose cancellation happens between cohomological degrees rather than through a torsion-free ideal sheaf;
2. codimension-two intersection-supported objects with a rank-two normal Koszul algebra and enough opposite Yoneda products;
3. higher-rank/semihomogeneous objects with non-scalar Atiyah action but not covered by the smooth-divisor bundle no-go `L023`;
4. a longer `K_0`-zero bridge complex engineered so its reverse Hom has the required degree-two cohomology.

## 10. Scope and firewall

`L030` does **not** prove:

- that every object on the ordinary secant ray fails the selected mixed directions;
- that a different perfect complex with the same `beta_1` Chern character cannot be a useful bridge;
- that every codimension-two bridge fails;
- second-factor rank `20`;
- all-orders algebraicity transport;
- `HC-R021`;
- the Hodge conjecture.

It refutes the explicit Example 8.2.4 coherent sheaves `F_d` as simultaneous bridges for the selected complementary mixed directions.

## 11. Sources and inputs

- Eyal Markman, arXiv:2502.03415v2, Example 8.2.4, especially the construction of `C_i`, `Z_d`, `F_d`, and the Chern-character calculation;
- `HC-R021-L006`, `L019`, `L022`, `L029`;
- standard identification of the tangent Gauss map of an Abel-Jacobi curve with the canonical map;
- elementary invariance of Fitting ideals under a derivation-compatible partial connection.
