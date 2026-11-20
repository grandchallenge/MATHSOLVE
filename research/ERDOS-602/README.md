# Erdős #602: Lean-checked finite-in-neighbour reduction

**Object:** `ERDOS-602-LIST-CORE-001`  
**Status:** `LOCAL_LEAN_KERNEL_CHECKED__MATHLIB_BRIDGE_AND_INDEPENDENT_CERTIFICATION_OPEN`  
**Source:** [MATH-PROGRAMME admitted unadjudicated handoff](https://github.com/grandchallenge/MATH-PROGRAMME/blob/5a1715bbba62e0184c3cc0a8bd1ce566eec9eceb/docs/handoffs/ERDOS-602-ESSENTIAL-DISJOINTNESS-001.md)  
**Original problem:** [Erdős #602](https://www.erdosproblems.com/602) (open); original paper [Erdős 1987, item 12, printed p. 227](https://www.renyi.hu/~p_erdos/1987-28.pdf).  
**Pinned formal comparator:** `google-deepmind/formal-conjectures@85f863718beeec7b58a3a1926ee92e3472bc2020`, `FormalConjectures/ErdosProblems/602.lean` (blob `9b85fd453afcfa95c6572e2a98d214d50f7e8caa`).

## Exact formal statement

In [EssentialDisjointListCore.lean](EssentialDisjointListCore.lean), the index set `I` and the ground type `X` are arbitrary. Every indexed predicate `A i : X → Prop` satisfies `EscapesEveryList`: for each finite `List X`, there is a point of `A i` absent from the list.

The input includes a relation `R : I → I → Prop` choosing at least one direction for every distinct pair. The function `P i : List I` gives a finite list of incoming neighbours: if `R j i` and the two sets share a point, `j` is in `P i`. The function `W i j : List X` covers every point of each distinct pairwise intersection. These are *actual finite-list witnesses*, not axiomatic claims of finiteness or hidden cardinality assumptions.

Two theorems are kernel checked:

1. `essentialDisjoint_of_finiteInNeighbours`: deleting `(P i).flatMap (fun j => W i j)` from each set leaves pairwise disjoint predicates still escaping every finite list.
2. `propertyB_of_finiteInNeighbours`: there is a binary `Fin 2` colouring such that none of the original `A i` is monochromatic.

The relation may contain directed cycles. **No acyclicity or well-order assumption is used.** The prohibition on singleton intersections is also not used. This strengthens the presentation of the finite-backward-neighbour method, but it is only a *sufficient* hypothesis, not a characterization of arbitrary Erdős #602 families.

## Pinned local replay

MATHSOLVE toolchain: `leanprover/lean4:v4.29.1` (pinned by `lean-toolchain`). The only import is `Init.Data.List.Lemmas`, so no compiled Mathlib or network cache is necessary.

Run from a clone with the matching installed toolchain:

```sh
elan run leanprover/lean4:v4.29.1 lean research/ERDOS-602/EssentialDisjointListCore.lean
```

**Exact source SHA-256:** `0aa8a514901fd301f0abd21da1e21c90c31d5f198694cd9924d53a1fdd05dbc1`.

Observed direct pinned-toolchain local replay on CHAD (exit 0, exact source bytes re-fetched from GitHub and compared to the initial checked file):

```text
'Erdos602ListCore.essentialDisjoint_of_finiteInNeighbours' depends on axioms: [propext, Quot.sound]
'Erdos602ListCore.propertyB_of_finiteInNeighbours' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The complete source contains no `sorry` or `admit`. Compiler proof checking was performed locally on an authenticated OS transport; it is **not** an independently authenticated or MATHCERT-certified replay. Local execution-capture ID: `b656ab3dfaa8419da3a7d75656f4ea5c`, which is supporting operator evidence, not a substitute for protected CI.

## Limitations and adversarial review

- Finite pairwise intersections by themselves do **not** produce finite incoming-neighbour lists. Constructing `P` remains an additional obligation.
- The unrestricted binary-prefix family in the source handoff has Property B but is not essentially disjoint. Therefore the stronger conclusion is not an admissible blanket strategy for Erdős #602.
- `EscapesEveryList` formalizes list-finitary infinitude, which agrees with ordinary infinitude in the usual classical setting. The explicit equivalence to Mathlib `Set.Infinite`, as well as conversion of `Set.Finite` to `List` witnesses `W` and `P`, is **not formalized in this file**.
- The `IsMonochromatic` predicate is structurally identical to the pinned formal provider's pointwise definition, but a Mathlib import and exact-provider theorem bridge have not been compiled.
- The theorem proves non-monochromaticity, **not** the stronger claim that each colour occurs infinitely often. The latter remains a written extension in the admitted handoff.
- No attempt is made to prove the provider's open `erdos_602` theorem or its separate `countable_index` `sorry`. No priority, originality, universality, external validity, or certification is claimed.

## Next bounded obligation

Produce a pinned-Mathlib theorem whose hypotheses use `Set.Infinite`, `Set.Finite`, finite incoming overlap-neighbour sets, and the **exact** pinned `Erdos602.HasPropertyB` predicate; prove the finite-list bridges without axioms beyond the declared classical Lean baseline; replay independently on the source-locked toolchain with no `sorry`, inspect `#print axioms`, and obtain source-semantic review. Then formalize the binary-prefix non-equivalence example. The unrestricted conjecture remains open.
