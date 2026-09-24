# WP08 Proof Debt Register

Date: 2026-09-24

| Debt ID | Obligation | Status | Evidence / next gate |
|---|---|---|---|
| WP08-D001 | Decide whether arbitrary finite union-closed families admit exact D003-complement representation. | Closed negative | `p04_no_universal_exact_functionalPreorder_representation`; explicit three-point obstruction. |
| WP08-D002 | Extend the Frankl-facing result from functional preorders to arbitrary finite partial orders. | Closed locally | `posetIdealFamily_exists_rare` and `posetIdeal_complement_frankl`; maximal-element erasure injection. |
| WP08-D003 | Express arbitrary closure systems by closure operators / implication bases and isolate the first non-poset obstruction. | Open | Build the closure/implication layer and identify a bounded extension beyond unary order implications. |
| WP08-D004 | Build an incidence-preserving interface to the WP05 minimum-counterexample lattice spine. | Open | Abstract lattice structure alone does not preserve concrete ground-element frequency data. |

## D002 movement

The functional restriction is unnecessary for the existence-of-a-rare-element
conclusion.

For a nonempty finite carrier `U` in any partial order:

1. choose a maximal `m ∈ U`;
2. erase `m` from every ideal containing it;
3. maximality preserves downward closure;
4. erasure is injective on sets containing `m`;
5. the image omits `m`;
6. therefore at most half of all ideals contain `m`;
7. complement duality makes `m` abundant.

This does not claim the stronger WP07 average-rarity inequality for arbitrary
posets.

## Current frontier

The remaining jump is from poset-ideal closure systems to arbitrary finite
closure systems.  That requires a representation richer than a binary order:
closure operators / finite implication bases are the next exact interface.

```text
UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
```
