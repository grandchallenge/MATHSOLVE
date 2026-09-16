# HC-R021-P4-A0 — Determinantal formulation of the rank-20 gluing locus

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `09f63de8ec7a6833bdea0c3d007a76a55ee00a72`  
**State:** `RANK20_LOCUS_DETERMINANTAL__PARAMETER_SPACE_AND_NONEMPTINESS_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Refine `HC-R021-P4-A0` after `HC-R021-L008` showed that Markman Example 11.2.7 defines a family of admissible glued sheaves rather than one canonical object.

The correct next object is therefore the **rank-20 locus in the gluing family**, not a numerical rank attached to an unspecified `E'`.

This package proves that, once the admissible gluing data are organized into an algebraic parameter family carrying a universal perfect object, the desired condition

```text
rank(ob_E)=20
```

is determinantal. Because `HC-R021-L006` supplies the pointwise lower bound `rank(ob_E)>=20`, the desired locus is exactly the rank-`<=20` degeneracy locus.

## 2. Relative setup

Let `S` be a finite-type complex scheme or algebraic stack parametrizing a family of admissible Example 11.2.7 gluing data on the fixed abelian fourfold `X`. Assume a universal perfect complex

```text
E in Dperf(X x S)
```

is given and that every geometric fiber `E_s` has

```text
ch(E_s) = N beta'
```

for the same nonzero integer `N` and fixed class `beta'`.

The constant Hochschild source is

```text
H := HT^2(X) tensor O_S,
rank(H)=28.
```

The universal Atiyah class defines a relative evaluation/obstruction morphism in the derived category. On any locally closed flattening stratum `S_alpha` on which

```text
Ext^2_p(E,E)
```

is represented by a locally free sheaf and commutes with base change, taking degree two gives a morphism of vector bundles

```text
ob_E/S : H|S_alpha -> Ext^2_p(E,E)|S_alpha.
```

Here `p:X x S -> S`.

## 3. HC-R021-L009 — the desired locus is determinantal closed

### Statement

On every such flattening stratum, define

```text
D_20 := { s in S_alpha : rank(ob_E_s) <= 20 }.
```

Then:

1. `D_20` is a Zariski-closed determinantal subspace of `S_alpha`;
2. semiregularity compatibility and `HC-R021-L006` imply `rank(ob_E_s)>=20` for every admissible fiber;
3. consequently

```text
D_20 = { s : rank(ob_E_s)=20 }
     = { s : ker(ob_E_s)=ker(c_beta') };
```

4. by `HC-R021-L007`, `D_20` is exactly the simultaneous zero locus of the eight objectwise Yoneda classes

```text
ev_E_s(k_1),...,ev_E_s(k_8).
```

Thus Markman's restricted first-order semiregularity question for the Example 11.2.7 construction reduces to proving

```text
D_20 != empty
```

for one admissible algebraic gluing family.

### Proof

For a morphism of vector bundles, the locus where rank is at most `20` is cut out by the `21 x 21` minors of a local matrix for the morphism. Hence `D_20` is determinantal and Zariski closed.

For every fiber, Buchweitz-Flenner/HKR compatibility gives

```text
ker(ob_E_s) subset ker(c_ch(E_s)).
```

Since `ch(E_s)=N beta'` with `N!=0`, scaling does not change the contraction kernel. `HC-R021-L006` proves

```text
dim ker(c_beta')=8,
rank(c_beta')=20.
```

Therefore

```text
dim ker(ob_E_s) <= 8,
rank(ob_E_s) >= 20.
```

On `D_20`, the two inequalities force `rank(ob_E_s)=20` and equality of the two eight-dimensional kernels. Conversely equality of kernels gives rank `20`, hence membership in `D_20`.

The equivalence with the simultaneous vanishing of the eight `L007` classes follows because `k_1,...,k_8` form a basis of `ker(c_beta')`.

QED.

## 4. Correction to the generic-locus heuristic

The minimal-rank condition is **not generically open** in an arbitrary gluing family.

For a matrix of regular functions, rank can drop on specialization; the condition

```text
rank <= 20
```

is closed, while `rank >= 20` is open. Since rank `20` is the minimum allowed by semiregularity compatibility, the desired objects naturally lie on a determinantal closed locus.

A proof that the eight relations vanish on a nonempty open subset would be stronger: on an irreducible parameter component it would force the relevant minors to vanish identically after closure. But openness must not be assumed.

## 5. Refined Route A0

The shortest direct route is now:

```text
P4-A0a  construct an algebraic parameter space/stack S for admissible
        Example 11.2.7 gluing data and a universal perfect object        [OPEN]
   |
   +--> P4-A0b  pass to explicit flattening strata where Ext^2 is
   |            locally free and base change holds                       [STANDARD INTERFACE]
   |
   +--> P4-A0c  form the rank-20 determinantal locus D_20                [L009]
   |
   +--> P4-A0d  prove D_20 is nonempty                                   [OPEN]
   |
   +--> P4-A1   choose s in D_20; restricted first-order
                semiregularity is then proved for E_s                    [CONDITIONAL]
```

The representative path from `HC-R021-L008` is the special case where one constructs a point of `D_20` directly.

## 6. What remains genuinely hard

`L009` removes an ambiguity but does not establish nonemptiness.

A nonemptiness proof can come from any of the following:

1. construct one symmetric or otherwise tractable gluing datum and verify the eight `L007` relations;
2. exhibit a specialization from the admissible family to a point where the eight relations can be calculated and which remains inside the admissible/simple locus;
3. prove the eight relative Yoneda sections vanish identically on a parameter component;
4. relate the determinantal equations to a finite group symmetry strong enough to force the required relations, thereby connecting Route A to Route G.

Chern-character identities alone cannot prove nonemptiness of `D_20`.

## 7. Current disposition

```text
HC-R021-L009 = proved_in_solve_package_not_certified
rank20_condition = determinantal_closed_on_flattening_strata
rank20_locus = simultaneous_zero_locus_of_eight_L007_relations
P4_A0_parameter_space = open
P4_A0_rank20_nonemptiness = open
P4_A1 = conditional_on_point_in_D20
P4_A2 = conditional_on_A1
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 8. Sources

- Eyal Markman, arXiv:2509.23079, Example 11.2.7 and Question 11.2.2.
- Eyal Markman, arXiv:2502.03415, Section 8.3.
- `work_packages/HC_R021_P4_CONTRACTION_RANK.md` (`HC-R021-L006`).
- `work_packages/HC_R021_P4_ATIYAH_RANK_REDUCTION.md` (`HC-R021-L007`).
- `work_packages/HC_R021_P4_ATIYAH_DATUM_BOUNDARY.md` (`HC-R021-L008`).
