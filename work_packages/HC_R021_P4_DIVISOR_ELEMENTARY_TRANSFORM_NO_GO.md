# HC-R021-P4 — Characteristic-foliation no-go for the divisor elementary transform

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `988edaeaa36776967ff8291b14a3f88d6192b6dc`  
**State:** `L020_ELEMENTARY_TRANSFORM_REFUTED__LOCALLY_FREE_DIVISOR_LANE_REMAINS`  
**Date:** 2026-09-16

## 1. Purpose

Test the two remaining mixed relations for the divisor-supported elementary-transform candidate `HC-R021-L020`.

They cannot vanish simultaneously.

The obstruction is not the support divisor itself; a hypersurface is coisotropic for a rank-two bivector. The obstruction is the codimension-two singular locus of the torsion-free elementary transform. A module deforming over a first-order Poisson deformation acquires a partial connection along the characteristic foliation of its coisotropic support, and its Fitting ideals are invariant under that connection. The correction curves in `L020` cannot be invariant under both complementary RM characteristic foliations.

## 2. Local form of the elementary transform

Let

```text
i:S -> X
```

be the smooth support divisor of `L020`. At a general smooth point of one irreducible correction curve

```text
C subset S
```

away from the other correction curves, point quotients, and all auxiliary intersections, the quotient has rank one on `C` and the elementary-transform sequence is locally equivalent to

```text
0 -> E -> O_S^R -> O_C -> 0.
```

After changing a local basis of `O_S^R`,

```text
E ~= I_(C/S) direct_sum O_S^(R-1).
```

Thus `C` is an irreducible component of the codimension-two non-locally-free/Fitting locus of `E`.

## 3. Fitting ideals of a first-order Poisson module

### HC-R021-L022a

Let `S` be a smooth coisotropic hypersurface in a smooth variety carrying a first-order deformation with local Poisson bivector `pi`. Let `M` be a torsion-free coherent module on `S`, generically locally free of rank `r`, and suppose `M` lifts to a module over the first-order deformed category.

Then the Fitting ideal defining the codimension-two non-locally-free locus of `M` is preserved by the characteristic distribution

```text
K_pi := pi^sharp(N^*_(S/X)) subset T_S.
```

In particular, at a smooth point of an irreducible curve component `C` of that locus where `K_pi` is nonzero,

```text
K_pi|_C subset T_C.
```

### Proof

Work locally where the gerby part is trivial. A deformation of a coherent module over a first-order Poisson deformation induces, on the special fiber over a coisotropic support, the standard first-order Poisson-module/partial-connection operator along the characteristic distribution. For a local characteristic vector field `v`, this is an operator

```text
nabla_v : M -> M
```

satisfying the Leibniz rule

```text
nabla_v(fm)=v(f)m+f nabla_v(m).
```

Choose a local presentation

```text
O_S^a --A--> O_S^b -> M -> 0.
```

The Leibniz rule implies that applying `v` to the matrix entries of `A` changes the presentation matrix by left and right matrix operations coming from the induced connections on the free modules. Therefore every determinantal/Fitting ideal of `M` is stable under `v`.

The codimension-two singular locus of a torsion-free module on the smooth `S` is defined generically by the appropriate Fitting ideal. Stability of that ideal says that the characteristic vector field is tangent to every smooth irreducible component. Hence `K_pi|_C subset T_C` whenever the characteristic line is nonzero.

QED.

The same statement follows from the standard fact that Fitting ideals of a Poisson module are Poisson/characteristic invariant.

## 4. The two RM characteristic lines

Use the normal form of `HC-R021-L006` and `L019`:

```text
pi_1=t_1 wedge t_2,
pi_2=t_3 wedge t_4,
V_1=span(t_1,t_2),
V_2=span(t_3,t_4),
V_1 intersect V_2=0.
```

For the smooth hypersurface `S`, let `n_p` be a nonzero local conormal at `p`. The characteristic vectors are

```text
v_1(p)=pi_1^sharp(n_p) in V_1,
v_2(p)=pi_2^sharp(n_p) in V_2.
```

The gerby components of `k_7,k_8` are locally trivial and do not change these characteristic directions.

If

```text
ob_E(k_7)=0
```

then `L022a` gives `v_1(p) in T_pC` at every general point where `v_1` is nonzero. Similarly, `ob_E(k_8)=0` gives `v_2(p) in T_pC`.

Because `T_pC` is one-dimensional and `V_1 intersect V_2=0`, the two nonzero characteristic vectors cannot both be tangent to `C` at the same point.

Hence, if both mixed obstructions vanished, every general point of an irreducible correction curve would lie in

```text
Z_1 union Z_2,
Z_i := {p in C : v_i(p)=0}.
```

Each `Z_i` is Zariski/analytic closed on the smooth locus of `C`. Since `C` is irreducible, one of them contains a dense open set and therefore the whole curve. Without loss of generality,

```text
v_1 identically 0 along C.
```

Then `V_1 subset T_pS` along `C`. The other characteristic vector cannot also vanish generically, because that would give

```text
V_1 direct_sum V_2 subset T_pS=T_pX,
```

contradicting `dim T_pS=3`. Thus `v_2` is nonzero generically and

```text
T_pC subset V_2
```

on a dense open subset.

The alternative case interchanges `V_1,V_2`.

## 5. The correction curves can be chosen to generate X

The `D`-type curves of `L020` are general complete intersections

```text
S intersect D_1 intersect D_2,
```

and the `H`-type curves are general complete intersections

```text
S intersect H_1 intersect A_1,
```

where every divisor class involved is ample. The translates can be chosen generally enough that each irreducible correction curve generates `X` as an abelian variety: equivalently, it is not contained in a translate of any proper abelian subvariety. This is an open general-position condition; proper abelian subvarieties form a countable collection of algebraic subgroup types, and a general ample complete intersection is not contained in any of their translates.

On the other hand, if the tangent of a complete algebraic curve `C` lies everywhere in a fixed complex vector subspace

```text
V_i subset T_0X
```

of dimension two, then the abelian subvariety generated by `C-C` has tangent space contained in `V_i`. It therefore has dimension at most two. Thus `C` is contained in a translate of a proper abelian subvariety and cannot generate the fourfold `X`.

Consequently no generating correction curve can have its tangent contained in `V_1` or `V_2` on a dense open set.

## 6. HC-R021-L022 — L020 cannot have both mixed relations

### Statement

Choose the complete-intersection correction curves in `HC-R021-L020` generally so that each generates `X`. Then the elementary-transform sheaf `E_div` cannot satisfy both

```text
ob_E_div(k_7)=0,
ob_E_div(k_8)=0.
```

Hence

```text
rank(ob_E_div)>20.
```

The `L020` divisor elementary-transform candidate is not a rank-20 second factor.

### Proof

At a generic point of every correction curve the local form is `I_(C/S) direct_sum O_S^(R-1)`. If both mixed obstructions vanished, `L022a` would make `C` invariant under both RM characteristic lines. Section 4 reduces this to the statement that `T_C` lies generically in one fixed RM plane `V_i`. Section 5 excludes that for the chosen generating ample complete-intersection curves.

QED.

## 7. Scope

This result refutes the specific elementary-transform construction of `L020` and, more generally, any analogous torsion-free sheaf on a smooth hypersurface whose codimension-two singular locus contains a generating curve and which is required to deform in both mixed RM directions.

It does **not** rule out:

1. a locally free vector bundle on a smooth divisor, because it has no codimension-two Fitting curve to which `L022a` can be applied;
2. a perfect complex with no torsion-free-sheaf singular locus;
3. a coherent object supported in higher codimension with a different characteristic distribution;
4. a construction whose singular locus is deliberately contained in a non-generating invariant subtorus, if such a construction can still realize the exact `beta-prime` Chern character and downstream Markman criterion.

## 8. Updated first-order frontier

The successive second-factor candidates now behave as follows:

```text
Example 11.2.7 divisor-plus-curve gluing     refuted by L019
split line-bundle perfect complex             rank 22 by L015/L016
same-divisor two-step extensions              pruned by L021
divisor elementary transform                  refuted by L022
locally free bundle on smooth divisor         OPEN
other genuinely non-formal perfect complex    OPEN
```

The next highest-value route is a locally free bundle on a smooth divisor with Chern character pushing forward to a nonzero multiple of `beta-prime`, followed by an exact computation of its two mixed characteristic actions.

## 9. Claim boundary

```text
HC-R021-L022 = proved_in_solve_package_not_certified
L020_elementary_transform_rank20 = false_for_general_generating_corrections
L020_mixed_pair_simultaneous_vanishing = false
locally_free_divisor_bundle_rank20 = open
second_factor_rank20 = open
G3 = downstream_of_second_factor_rank20_by_L018
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 10. Sources and inputs

- Wendy Lowen, characteristic morphism / first-order object obstruction framework.
- Yukinobu Toda, gerby/commutative/noncommutative first-order deformation framework.
- standard Poisson-module fact that Fitting ideals are preserved by the induced characteristic/Poisson connection.
- `HC-R021-L006`, `L019`, `L020`, and `L021`.
