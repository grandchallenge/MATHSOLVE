# HC-R021-P4-A0 — Algebraic parameter stack for the Example 11.2.7 gluings

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `09f63de8ec7a6833bdea0c3d007a76a55ee00a72`  
**State:** `PARAMETER_STACK_EXISTS__RANK20_NONEMPTINESS_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Discharge the parameter-space part of `HC-R021-P4-A0` without pretending that Markman Example 11.2.7 selects a canonical sheaf.

The source construction is existential but algebraic. After fixing one admissible discrete/source datum, its remaining curve/translation/line-bundle/gluing choices can be organized into a finite-type algebraic stack carrying a universal glued object. This supplies the base required by `HC-R021-L009`.

The result does **not** prove that the rank-20 determinantal locus is nonempty.

## 2. Fixed source datum

Fix the genus-four Jacobian `X`, principal polarization `Theta`, real-quadratic action, norm-one element `f`, automorphism `g`, and positive parameter `q` used in Markman Example 11.2.7.

Choose source-admissible integers `d,N>0` for which the curve class

```text
Gamma := (N/6)(d g^*(Theta^3) - q (g^-1)^*(Theta^3))
```

is represented by a curve on `X`.

Fix one simple secant sheaf `F'` supplied by Markman arXiv:2502.03415, Example 8.2.4, with

```text
ch(F') = Theta - (d/6)Theta^3.
```

No uniqueness is claimed. Fixing these choices only selects one nonempty source tranche in which to search for a successful `E'`.

## 3. Curve parameter

Choose one source-admissible curve `C'_0` of class `Gamma` and let `P` be its Hilbert polynomial with respect to a fixed ample line bundle on `X`.

Let

```text
H := Hilb_P(X)_Gamma
```

denote the union of Hilbert-scheme components containing curves with the required cohomology class, restricted to the component containing `C'_0` if desired.

Then `H` is finite type and nonempty, and it carries the universal subscheme

```text
C_univ subset X x H.
```

Retain a nonempty locally closed locus on which the fibers have the geometric properties needed for the gluing construction.

## 4. Translation parameter and labeled incidence

Let

```text
T := X^N.
```

For `t=(t_1,...,t_N) in T`, set

```text
T_j(t) := tau_(t_j)^* g^*F',
A_t := direct_sum_(j=1)^N T_j(t).
```

The action map and pullback of the fixed coherent sheaf give universal constituent families

```text
T_j,univ
```

and their direct sum `A_univ` on `X x H x T`.

For each `j`, let `Z_j` be the incidence scheme between the universal curve and `Supp(T_j,univ)`. Pass to a common locally closed flattening stratum `U_inc subset H x T` on which every `Z_j -> U_inc` is finite and the restriction of `T_j,univ` to `Z_j` is a line bundle. This is the constituent-wise form of Markman's condition that the curve meet each translated support only where that sheaf is a line bundle on its support.

No disjointness among the `Z_j` is required for the construction below: use the labeled disjoint union

```text
Z_lab := disjoint_union_(j=1)^N Z_j.
```

Markman's instruction to choose generic translates with the required local-freeness condition implies that at least one such incidence stratum is nonempty for the fixed source datum.

## 5. Relative line-bundle parameter

Over the universal curve on `U_inc`, use the relative Picard **stack** rather than assuming a global Poincare bundle on a coarse Picard scheme.

Fix the Euler-characteristic/degree condition required in Example 11.2.7 and let

```text
Pic^ell(C/U_inc)
```

be the corresponding finite-type component of the relative Picard stack.

By definition this stack carries a universal line bundle `L_univ` on the pulled-back universal curve. Its degree can be chosen so that the resulting glued sheaf has `chi(E')=0`, as in the source construction.

## 6. Constituent-wise gluing-isomorphism parameter

Pull all incidence schemes to the relative Picard stack. On each `Z_j`, both

```text
T_j,univ|Z_j
```

and

```text
L_univ|Z_j
```

are line bundles. The fiber identifications required by Markman form the product relative isomorphism torsor

```text
Glu := product_(j=1)^N Isom_(Z_j)(T_j,univ|Z_j, L_univ|Z_j).
```

After an etale cover that labels the geometric points of the finite `Z_j`, each factor is a product of `G_m`-torsors. Hence `Glu` is algebraic and finite type over the incidence/Picard parameter stack.

This constituent-wise definition is essential: at a point lying on one translated support, the gluing identifies the fiber of that specific `T_j` with the fiber of `L`; it does not identify the full direct-sum fiber `A_t` with a rank-one line.

## 7. Universal glued object

Over

```text
S_glue := Glu -> Pic^ell(C/U_inc) -> U_inc,
```

the universal isomorphisms define a difference morphism

```text
rho_univ : A_univ direct_sum i_*L_univ -> Q_univ,
```

where, using the labeled incidence branches,

```text
Q_univ := direct_sum_(j=1)^N (i_j)_*(L_univ|Z_j)
```

and the `j`-th component of `rho_univ` is the difference between the restriction of the `j`-th constituent and the line-bundle restriction under the chosen fiber isomorphism.

Define

```text
E_univ := ker(rho_univ).
```

Equivalently,

```text
E_univ -> A_univ direct_sum i_*L_univ -> Q_univ -> E_univ[1]
```

is the universal gluing triangle.

After flattening stratification, `E_univ` is an `S_glue`-flat coherent family; over the fixed smooth projective fourfold it is relatively perfect. Every geometric fiber has

```text
ch(E_s) = N beta'
```

by the same K-theory calculation as Example 11.2.7.

## 8. Simple/admissible locus

For a flat proper family of coherent sheaves, the function

```text
s |-> dim Hom(E_s,E_s)
```

is upper semicontinuous. Hence the locus where this dimension takes its minimum value `1` is open.

Markman states that the construction yields a simple coherent sheaf after suitable generic choices. Therefore, after restricting to a suitable source-admissible stratum, the simple locus

```text
S_adm subset S_glue
```

is nonempty.

## 9. HC-R021-L010 — existence of a nonempty algebraic gluing family

### Statement

There exists a nonempty finite-type complex algebraic stack `S_adm` and a universal relatively perfect object

```text
E_univ on X x S_adm
```

such that every geometric fiber is an admissible simple Example 11.2.7 gluing with Chern character `N beta'`.

After a flattening/base-change stratification of `S_adm`, relative `Ext^2` is locally free and commutes with base change on each stratum, so `HC-R021-L009` applies and defines the closed rank-20 determinantal locus `D_20`.

### Proof

Sections 3-8 construct the stack as a tower of standard finite-type algebraic parameter objects: a Hilbert-scheme stratum, translation parameters, relative Picard stack, and constituent-wise relative isomorphism torsors. The universal difference morphism gives `E_univ`. Nonemptiness follows from the source existence of a curve in class `Gamma`, generic translates satisfying the local-freeness incidence condition, a suitable-degree line bundle, fiber identifications, and a simple resulting sheaf.

Flattening stratification and cohomology-and-base-change for the relative self-Hom complex produce the required strata for `L009`.

QED.

## 10. Exact remaining A0 obligation

The parameter ambiguity is now removed. The direct route is:

```text
L010  nonempty admissible algebraic gluing stack S_adm          [SOLVE-PROVED]
   |
   +--> L009  closed determinantal rank-20 locus D_20           [SOLVE-PROVED]
            |
            +--> P4-A0d  prove D_20 is nonempty                 [OPEN]
                     |
                     +--> P4-A1  choose E in D_20;
                                  rank(ob_E)=20                  [CONDITIONAL]
```

No explicit coordinate equation for `X` is needed merely to define this frontier. Explicit RM/Jacobian equations become relevant only if they provide a tractable point at which the eight `L007` relations can be evaluated.

## 11. Current disposition

```text
HC-R021-L010 = proved_in_solve_package_not_certified
admissible_gluing_parameter_stack = nonempty_finite_type
universal_relative_perfect_gluing_family = available_after_stratification
rank20_determinantal_locus = defined
rank20_determinantal_locus_nonempty = open
P4_A0_remaining = nonemptiness_of_D20
P4_A1 = conditional_on_D20_nonempty
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 12. Sources

- Eyal Markman, arXiv:2509.23079, Example 11.2.7.
- Eyal Markman, arXiv:2502.03415, Example 8.2.4.
- `work_packages/HC_R021_P4_ATIYAH_DATUM_BOUNDARY.md` (`HC-R021-L008`).
- `work_packages/HC_R021_P4_ATIYAH_DETERMINANTAL_LOCUS.md` (`HC-R021-L009`).
