# HC-WP00 statement lattice and proof-obligation DAG

## Purpose

This document prevents a proof route from acquiring algebraicity by semantic drift. Every arrow states what is genuinely known, what is conjectural, and where an algebraic-cycle construction is still missing.

## Canonical objects

```text
X              smooth projective variety over C
n              complex dimension of X
p              codimension
Z^p(X)         free abelian group on irreducible codimension-p subvarieties
CH^p(X)        Z^p(X) modulo rational equivalence
Hdg^(2p)(X,Q)  H^(2p)(X,Q) intersect H^(p,p)(X)
cl_Q^p         CH^p(X) tensor Q -> Hdg^(2p)(X,Q)
```

## Theorem spine

```text
HC-D000  Smooth projective varieties over C; dimension and codimension conventions
HC-D001  Hodge decomposition and rational Hodge classes
HC-D002  Algebraic cycles, Chow groups, rational equivalence, and cycle classes
HC-L003  Algebraic codimension-p cycle classes have type (p,p)
HC-T004  Surjectivity of cl_Q^p
HC-B005  Equivalence with rational generation by irreducible subvariety classes
HC-K006  Boundary cases p=0,1,n-1,n
HC-K007  Full conjecture in dimension at most three
HC-K008  Selected special higher-dimensional cases, source-indexed
HC-O009  Naive integral formulation is false
HC-O010  Unrestricted compact-Kahler analogue is false
HC-O011  Algebraicity of Kunneth projectors and inverse Lefschetz is not automatic
HC-O012  Hodge-locus algebraicity does not imply cycle algebraicity
HC-O013  Deformation transport requires a variational/relative-cycle bridge
HC-O014  Numerical period recognition is not exact algebraicity
HC-O015  Tate reduction requires comparison, specialization, and lifting
HC-O016  Topological Chern-character generation is not algebraic cycle generation
HC-O017  Abel-Jacobi/normal-function tests are not complete general detectors
HC-O018  Absolute or motivated does not mean algebraic
HC-O019  Very-general-fiber results do not automatically cover every fiber
HC-T020  Full classical Hodge conjecture [OPEN]
HC-R021  First restricted theorem target [UNSELECTED]
```

## Dependency graph

```text
D000 ─┬─> D001 ──────────────┐
      └─> D002 ─> L003 ──────┼─> T004 <─> B005 ─> T020
                              │
K006 ─> K007 ─────────────────┘

D001 + D002 ─> O009  integral drift blocked
D000 + D001 ─> O010  Kahler drift blocked
D001 ─> O012          locus/class distinction
D001 + family data ─> O013
D001 + exact arithmetic debt ─> O014
Tate interfaces ─> O015
K-theory interfaces ─> O016
cycle-filtration interfaces ─> O017
absolute/motivated interfaces ─> O018
family quantifiers ─> O019

WP00 + WP01 + WP02 ─> R021 selection gate
```

## Node obligations

### HC-D000 — domain

Discharge criterion: every claim states smoothness, projectivity, base field, dimension, and codimension. Compact Kahler, singular, quasi-projective, arithmetic, or positive-characteristic variants receive separate profiles.

### HC-D001 — rational Hodge class

Discharge criterion: `alpha` is both rational and of complex type `(p,p)`. A calculation in `H^(p,p)(X)` alone is insufficient.

### HC-D002 — cycle object

Discharge criterion: specify whether the domain is `Z^p`, `CH^p`, algebraic K-theory, numerical cycles, or another correspondence class. The canonical image in cohomology factors through `CH^p`, but injectivity is not asserted.

### HC-L003 — necessary direction

Discharge criterion: the cycle class of each codimension-`p` algebraic subvariety lies in `H^(p,p)` and is rational/integral under the chosen convention. This is only the easy direction.

### HC-T004 — target

Discharge criterion: for arbitrary `alpha in Hdg^(2p)(X,Q)`, construct a rational algebraic cycle with exactly that cohomology class.

### HC-B005 — equivalence

Discharge criterion: explicitly use generation of `Z^p` by irreducible subvarieties and factorization through rational equivalence. Do not add effectivity.

### HC-K006/HC-K007 — boundary

Discharge criterion: record the Lefschetz `(1,1)` input and the hard-Lefschetz/Hodge-structure argument for codimension `n-1`. No algebraicity of the inverse Lefschetz correspondence is required for this cohomological preimage argument; the produced class is made algebraic after the preimage is identified as a divisor.

### HC-O011 — projector circularity

Discharge criterion: any use of algebraic Kunneth projectors, Lefschetz-star operators, or inverse Lefschetz correspondences cites an independent theorem for the selected variety class. Cohomological existence alone does not make the correspondence algebraic.

### HC-O012 — Hodge locus

Discharge criterion: distinguish

```text
parameter locus where alpha remains (p,p)
```

from

```text
relative algebraic cycle whose class is alpha.
```

The first may be algebraic without supplying the second.

### HC-O013 — variational bridge

Discharge criterion: a flat Hodge class with one algebraic specialization requires an explicit relative-cycle or variational theorem to move algebraicity.

### HC-O015 — Tate bridge

Discharge criterion: state good reduction, cohomological comparison, invariance, field extension, specialization of cycles, and lifting back to characteristic zero. Each arrow is independently audited.

## Implication ledger

### Proven implications

```text
algebraic class -> rational Hodge class
classical Hodge for X -> every rational Hodge class on X is absolute
classical Hodge for X x X -> algebraicity of its Hodge Kunneth components
classical Hodge for appropriate products -> relevant inverse-Lefschetz correspondence is algebraic
Lefschetz (1,1) + hard Lefschetz -> p=n-1 boundary case
```

The middle implications require the correspondence to be represented as a Hodge class on a product with the correct Tate twist and degree.

### Conjectural or non-implications

```text
rational Hodge -/-> algebraic                  [the open target]
absolute Hodge -/-> algebraic                  [not known generally]
motivated -/-> algebraic                       [definition deliberately broader]
algebraic Hodge locus -/-> algebraic class     [different object]
Tate class in a reduction -/-> lifted cycle    [missing bridges]
cohomological inverse Lefschetz -/-> algebraic correspondence
very general fiber theorem -/-> every fiber theorem
numerical period relation -/-> exact rational class or cycle
```

## Restricted-target admission rubric

No target is selected in WP00. A candidate receives a score only after the source and false-proof ledgers are complete. Required dimensions:

1. exact variety class and codimension;
2. nontriviality beyond `p=1,n-1`;
3. source-defined unsolved boundary;
4. independent cycle-construction mechanism;
5. resistance to all WP01 fixtures;
6. exact cohomology comparison route;
7. tractable quantifiers and deformation/specialization control;
8. prior-art distance;
9. formalizable finite or algebraic sub-obligations;
10. information value if false or if the route terminates.

## First executable obligations after WP00

### WP01 — false-proof atlas

Turn each obstruction node into a minimized fixture with a tempting argument, exact failure, scope of rejection, and surviving route.

### WP02 — known-case and construction ledger

For each admitted known family, reconstruct the actual cycle-producing mechanism rather than listing theorem names. The ledger must distinguish:

- generation of all rational Hodge classes;
- construction of selected classes;
- deformation or monodromy reduction;
- motivated/absolute status only;
- conditional results;
- necessary detection criteria.

## Claim boundary

This DAG certifies logical bookkeeping only. It does not certify the imported geometry and does not convert an abstract implication theorem into a proof of cycle-class surjectivity.