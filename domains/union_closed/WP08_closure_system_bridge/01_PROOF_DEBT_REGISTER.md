# WP08 Proof Debt Register

Date: 2026-09-24

| Debt ID | Obligation | Status | Evidence / next gate |
|---|---|---|---|
| WP08-D001 | Decide whether arbitrary finite union-closed families admit exact D003-complement representation. | Closed negative | `p04_no_universal_exact_functionalPreorder_representation`; explicit three-point obstruction. |
| WP08-D002 | Extend from functional preorders to arbitrary finite preorders/posets. | Open | Build a general order-ideal family interface and seek a rare-element theorem independent of the functional restriction. |
| WP08-D003 | Express arbitrary closure systems by closure operators / Horn implications and isolate the first non-unary obstruction. | Open | Formal closure-system duality is available; implication-normal-form layer not yet implemented. |
| WP08-D004 | Build an incidence-preserving interface to the WP05 minimum-counterexample lattice spine. | Open | Abstract lattice structure alone does not preserve the concrete ground-element frequency data. |

## Exact negative result

The family

```text
{ ∅, {a,b}, {b,c}, {a,b,c} }
```

is union-closed but not intersection-closed. Exact D003 complements are both.
Therefore exact D003 representation cannot be universal.

This is a refutation of one proposed UC-P04 route, not a refutation or proof of
Frankl's conjecture.

## Current frontier

The universal complement of a union-closed family is an intersection-closed
finite closure system. The next constructive route is to enlarge the WP07
theorem from functional-preorder closure systems toward arbitrary finite closure
systems in controlled stages.
