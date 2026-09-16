# HC-R021-P4 — Partial-normalization full-support secant object still fails the RM mixed directions

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `6876c474766a5add3e22e9713898276fc6e59d71`  
**State:** `PARTIAL_NORMALIZATION_SECANT_OBJECT_GENERIC_W2_FITTING_LOCUS_BLOCKS_EACH_MIXED_DIRECTION`  
**Date:** 2026-09-16

## 1. Purpose

Test the genuinely derived full-support secant object introduced by Markman in arXiv:2502.03415, Example 8.2.3, after the coherent and line-bundle companion routes were narrowed by `L035-L037`.

For a genus-four Jacobian, Markman constructs a union `Z` of translates of `W_2`, partially normalizes selected pairwise intersection points, and forms

```text
F' := [ O_X -> nu_* O_(Z_tilde) ].
```

After twisting by `Theta`, this object has the same Chern character as the corresponding secant ideal sheaf. Because `F'` is genuinely derived and has full support, it is not covered by the divisor-support no-go lemmas.

Nevertheless it still fails the two selected RM mixed directions for a generic local reason. Away from the finite normalization/intersection set, it is locally just the ideal sheaf of one smooth `W_2` component. A first-order Poisson lift would force that codimension-two Fitting locus to be invariant under the full rank-two Poisson image plane. The tangent planes of `W_2=C^(2)` vary with the canonical secant line and therefore cannot equal either fixed RM plane.

The partial-normalization correction occurs only at finitely many points and cannot repair this generic obstruction.

## 2. Source construction

Use Markman, arXiv:2502.03415, Example 8.2.3 in dimension `n=4`.

Let `C` be a Brill-Noether generic genus-four curve, `X=Pic^3(C)`, and let `W_2` denote the Abel-Jacobi image of `C^(2)` translated into `X`. For the secant parameter `d>0`, choose a cyclic subgroup `G` of order `d+1` and translates

```text
S_i := tau_(t_i)(W_2),
0 <= i <= d,
```

such that every pair intersects in six distinct points and all pairwise intersection sets are mutually disjoint.

Set

```text
Z := union_i S_i.
```

For each pair choose four of the six intersection points and partially normalize those crossings:

```text
nu : Z_tilde -> Z subset X.
```

Markman's object is

```text
F' := [ O_X -> nu_* O_(Z_tilde) ].          (2.1)
```

The chosen normalization data can be made `G`-invariant, and the source records

```text
ch(F'(Theta)) = ch(F_d),                   (2.2)
```

where `F_d` is the corresponding genus-four secant ideal object of Example 8.2.3.

No semiregularity or mixed-obstruction vanishing is asserted for `F'` in the source.

## 3. Generic local form

Fix one irreducible component

```text
S := S_i = tau_(t_i)(W_2).
```

Choose a general point

```text
x in S
```

away from:

- every other `S_j`;
- all pairwise intersection points;
- all points at which the partial normalization differs from the identity.

On a sufficiently small neighborhood `U` of `x`, the finite map `nu` is the identity over `S cap U`, and no other component of `Z` is present. Thus (2.1) restricts to

```text
[ O_U -> O_(S cap U) ].                    (3.1)
```

With the standard convention in which the first term is in degree zero, (3.1) is quasi-isomorphic to

```text
I_(S/U).                                   (3.2)
```

The twist by `O_X(Theta)` is locally invertible and does not alter the singular/Fitting locus or the Poisson-invariance argument.

Consequently every object-level deformation of `F'(Theta)` restricts near `x` to a deformation of the rank-one torsion-free module `I_(S/U)`.

## 4. Fitting invariance for a full-support Poisson module

Let `U` be smooth and let `M` be a finitely presented module which is locally free on a dense open. Suppose `M` lifts to a module over a first-order Poisson deformation of `O_U` with bivector `pi`.

After locally trivializing the gerby part, the first-order module structure induces the usual contravariant/Poisson connection

```text
nabla_alpha : M -> M,
alpha in Omega^1_U,
```

with anchor `pi^sharp(alpha)` and Leibniz rule

```text
nabla_alpha(fm)
 = pi^sharp(alpha)(f)m + f nabla_alpha(m).  (4.1)
```

Exactly as in `L022/L030`, choose a local presentation of `M`. Equation (4.1) implies that every determinantal/Fitting ideal is stable under every anchored derivation `pi^sharp(alpha)`. Therefore every irreducible component of the non-locally-free locus is invariant under the distribution

```text
im(pi^sharp) subset T_U.                   (4.2)
```

### HC-R021-L038a — full-support Fitting invariance

For a full-support torsion-free module admitting a first-order Poisson lift, the generic tangent space of every reduced irreducible component of its non-locally-free locus contains the Poisson image distribution.

For the local complete-intersection ideal `I_(S/U)` with `codim_U S=2`, its non-locally-free Fitting locus is precisely `S`. Thus

```text
im(pi^sharp)|_S subset T_S.                (4.3)
```

## 5. Apply the two RM mixed directions

Use the RM normal form of `L006`:

```text
k_7 = pi_1 + q a alpha_1,
pi_1 = t_1 wedge t_2,
V_1 = span(t_1,t_2),

k_8 = pi_2 + q b alpha_2,
pi_2 = t_3 wedge t_4,
V_2 = span(t_3,t_4).
```

The two bivectors have constant rank two and

```text
im(pi_i^sharp)=V_i tensor O_X.             (5.1)
```

The gerby terms `alpha_i` are locally trivial and do not change the anchored distribution.

If

```text
ob_(F'(Theta))(k_i)=0,
```

then the local object (3.2) lifts over the corresponding first-order Poisson deformation. By (4.3),

```text
V_i subset T_x S
```

for general `x in S`. Since both spaces are two-dimensional,

```text
T_x S = V_i                                (5.2)
```

on a dense open subset of `S`.

Thus vanishing of even one selected mixed obstruction would force the tangent Gauss map of the `W_2` component to be constant.

## 6. The tangent planes of W_2 are not constant

For a non-hyperelliptic genus-four curve, the Abel-Jacobi map identifies `W_2` generically with `C^(2)`. At a reduced divisor

```text
p+q in C^(2),
```

the projectivized tangent plane to `W_2` inside the Jacobian is the secant line

```text
< kappa(p), kappa(q) > subset P(H^0(C,K_C)^*),
```

where `kappa:C->P^3` is the canonical embedding.

As `p,q` vary, these secant lines vary. A nondegenerate canonical genus-four curve is not contained in a single projective line, and its secant-line family is two-dimensional. Therefore the Gauss map of `W_2` is nonconstant.

In particular there is no fixed two-dimensional vector subspace

```text
V subset T_0 X
```

such that

```text
T_x W_2 = V
```

on a dense open subset.

This contradicts (5.2) for both `V_1` and `V_2`.

## 7. HC-R021-L038 — partial-normalization secant no-go

### Statement

For Markman's genus-four partial-normalization secant object `F'` of Example 8.2.3, and for either selected RM mixed direction,

```text
ob_(F'(Theta))(k_7) != 0,
ob_(F'(Theta))(k_8) != 0.                  (7.1)
```

The conclusion is object-level and does not rely on semiregularity. It follows from the generic `W_2` Fitting locus, where the partial normalization is invisible.

Thus the partial-normalization/full-support realization does not itself furnish a mixed-compatible rank-12 bridge or a rank-20 second factor.

### Proof

Sections 3-6.

QED.

## 8. Exposure principle for later complexes

The proof gives a reusable local constraint.

Suppose a filtered/perfect complex has an irreducible `W_2`-type surface `S` such that, on a dense open subset of `S`, all other graded pieces vanish or are locally free and the complex reduces to a shift of `I_S`. Then vanishing of a mixed obstruction forces `S` to be invariant under the corresponding RM plane. Hence it fails for a generic Abel-Jacobi `W_2` component.

Therefore any future construction using these secant objects must **pair every exposed W_2 component on the same generic support** with other nontrivial local terms. Merely adding point-level partial-normalization corrections, or placing unrelated secant components elsewhere, cannot cancel the mixed obstruction.

This is stronger than saying that `F'` itself fails: it constrains how the object may appear inside a longer non-formal complex.

## 9. Scope and firewall

`L038` does **not** rule out:

- a complex in which every `W_2` component is overlapped by another nontrivial constituent on the same support;
- same-support secant pairs with cross-Ext cancellation;
- higher-rank modules whose generic singularity along the surface is not an ideal module;
- a Fourier-Mukai/isogeny transform producing the companion sector;
- an unstable coherent companion object;
- second-factor rank `20`;
- all-orders algebraicity transport;
- `HC-R021`;
- the Hodge conjecture.

## 10. Current disposition

```text
HC-R021-L038 = proved_in_solve_package_not_certified
partial_normalization_secant_k7 = obstructed
partial_normalization_secant_k8 = obstructed
finite_normalization_point_corrections_repair_generic_W2_obstruction = false
exposed_W2_component_in_longer_complex = forbidden_for_mixed_lift
same_support_surface_cancellation = live
companion_transform_route = live
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 11. Inputs and sources

- `HC-R021-L006`, `L022`, `L030`, `L035-L037`;
- Eyal Markman, arXiv:2502.03415, Example 8.2.3, especially Equation (8.2.6) and the partial-normalization construction;
- standard Poisson-module/contravariant-connection interpretation of first-order module lifts;
- invariance of Fitting ideals under derivation-compatible connections;
- standard tangent-space description of `W_2=C^(2)` in a Jacobian via secant lines to the canonical curve.
