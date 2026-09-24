# WP08 Proof Debt Register

Date: 2026-09-24

| Debt ID | Obligation | Status | Evidence / next gate |
|---|---|---|---|
| WP08-D001 | Decide whether arbitrary finite union-closed families admit exact D003-complement representation. | Closed negative | `p04_no_universal_exact_functionalPreorder_representation`; explicit three-point obstruction. |
| WP08-D002 | Extend the Frankl-facing result from functional preorders to arbitrary finite partial orders. | Closed locally | `posetIdealFamily_exists_rare`, `posetIdeal_complement_frankl`; maximal-element erasure injection. |
| WP08-D003A | Extend the erasure mechanism beyond posets using finite Horn implications. | Candidate closed | `hornModel_complement_frankl_of_conclusionFree`. |
| WP08-D003B | Determine whether single-element erasure can cover arbitrary pointed closure systems. | Candidate closed negative | `not_every_pointedClosureSystem_has_erasable`; cyclic binary Horn fixture. |
| WP08-D003C | Replace erasure by a more general matching/charging mechanism for cyclic multi-premise closure systems. | Open | Begin from the three-point cyclic fixture and formulate an incidence-preserving finite matching criterion. |
| WP08-D004 | Build an incidence-preserving interface to the WP05 minimum-counterexample lattice spine. | Open | Abstract lattice structure alone does not preserve concrete ground-element frequency data. |

## Current frontier

The exact representation route is false; the poset theorem is broader than
WP07; and the single-erasure proof has now reached its exact structural limit.

The next useful object is not another equality representation. It is a
certificate of the cardinal inequality

```text
# closed sets containing x <= # closed sets omitting x
```

that can use a nontrivial matching or charging map rather than literal
`I |-> I \ {x}`.

Such a certificate retains the incidence information needed by Frankl and can
be compared directly with WP05's minimum-counterexample constraints.

```text
UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
```
