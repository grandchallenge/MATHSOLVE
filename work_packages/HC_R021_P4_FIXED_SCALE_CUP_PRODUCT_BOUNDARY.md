# HC-R021-P4 — Fixed-scale RM cup-product evidentiary boundary

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `f4fda129f446f3e79d49fb29377a29cb2df42048`  
**State:** `MISSING_FIXED_SCALE_RM_THETA_CUP_PRODUCT_MATRIX`  
**Date:** 2026-09-16

## 1. Purpose

Record the exact evidentiary boundary reached after `HC-R021-L050` reduced the co-supported globalization problem to finite-dimensional index-two cup-product/hypercohomology maps.

This package does not close the co-supported extension lane. It prevents an unsupported promotion from index-theoretic dimension counts to a fixed-scale rank statement.

## 2. What is already exact

`L049b` constructs two local co-supported extension channels and gives explicit nullhomotopies for every local constant bivector.

`L050` proves:

```text
Ext_X^1(B_D,E) ~= C,
E=I_C(D),
```

so ordinary global chain maps provide only the theta-square channel and cannot supply the required two independent residues.

The second channel must therefore come from the derived term

```text
Ext_X^2(B_D,E^vee) ~= H^2(X,Q)^*,
Q=I_C(2D)/t^2 I_C.
```

All line-bundle classes carrying the local residues and terminal compatibility have index `2`, with

```text
h^2(2D-H)       = (2 tau-5)^2,
h^2(2D-A)       = (2 tau^2-9)^2,
h^2(H+A-D)      = (tau^2-5)^2.
```

Thus there is ample cohomological room, but dimensions alone do not determine the residue-map rank.

## 3. Literature audit

Nathan Grieve, *Index conditions and cup-product maps on abelian varieties* (arXiv:1308.1970; International Journal of Mathematics 25 (2014)) is directly relevant because it studies cup products between nondegenerate line bundles of nonzero index.

The paper itself distinguishes two levels:

1. at fixed scale, for line bundles `L,M` satisfying

```text
chi(L), chi(M), chi(L tensor M) != 0,
i(L tensor M)=i(L)+i(M),
```

the image and even nonvanishing of the cup-product map are posed as `Problem 1.1`;

2. Theorem 3.3 proves nonzero/surjective cup products only in an asymptotic family after replacing the line bundles by sufficiently high tensor powers (`n >> 0`) and allowing translation.

Therefore that theorem does **not** imply that the fixed `n=1` cup-product matrices occurring in `L050` are nonzero, injective, surjective, or maximal rank.

Using the asymptotic theorem to assert rank two here would cross the proof firewall.

## 4. Repository audit

An accessible repository search of `grandchallenge/MATHSOLVE` and `grandchallenge/MATHFORGE` did not surface an existing exact theta-group / finite-Heisenberg implementation that evaluates the required fixed-scale RM cup products or their structure constants.

This is a search result, not a claim that no such code can exist elsewhere.

## 5. Exact missing object

The remaining mathematical datum is the fixed-scale cup-product/hypercohomology matrix obtained by expanding `Q` through the Koszul resolution of

```text
C=D cap H cap A
```

and taking the unique nonzero `H^2` groups of the index-two line bundles.

At minimum one needs exact linear maps induced by multiplication by the selected theta sections of `D`, `H`, and `A` between the relevant spaces, including the summands with numerical classes

```text
2D-H,
2D-A,
H+A-D,
```

and the neighboring Koszul classes appearing in `HC-R021-L050`.

The decisive invariant is the generic-residue rank

```text
rank( Ext_X^1(B_D,C_corr)
      -> Ext_R^1(B,C) )
```

on the two local residue coordinates of `L049`.

Required disposition:

```text
rank = 2  -> co-supported globalization remains viable;
rank < 2  -> co-supported escape closes.
```

## 6. Admissible ways to cross the boundary

Any one of the following would supply the missing evidence:

1. an exact theta-group / finite-Heisenberg model for the relevant RM line bundles and chosen theta sections, yielding the cup-product matrices directly;
2. a theorem specialized to these fixed RM numerical classes that proves the needed fixed-scale rank;
3. an exact algebraic model of the chosen RM abelian fourfold and theta sections from which the same matrices can be computed and certified;
4. a source theorem identifying these particular cup products with an already certified representation-theoretic map of known rank.

Pure dimension counts, generic-rank heuristics, numerical period evaluations without certification, and the `n >> 0` theorem are insufficient.

## 7. Boundary

```text
HC-R021-L051 = evidentiary_boundary_not_theorem
boundary_name = MISSING_FIXED_SCALE_RM_THETA_CUP_PRODUCT_MATRIX
local_two_channel_repair = proved_in_solve_package_not_certified
ordinary_global_channel_rank = 1
derived_index2_channel = nonempty_in_dimension_but_rank_unknown
global_Ext1_residue_rank = open
cosupported_global_extension = open
second_factor_rank20 = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

This package records an evidentiary boundary only. It is not a MATHCERT disposition.

## 8. Sources

- `HC-R021-L049`: co-supported local extension repair;
- `HC-R021-L050`: global residue hyper-Ext reduction;
- Nathan Grieve, arXiv:1308.1970v3, especially Problem 1.1 and the asymptotic statements summarized around Theorems 3.2 and 3.3;
- Mumford index theorem for nondegenerate line bundles on abelian varieties.