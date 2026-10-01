# OM26-H7 formalization status review

**Hill:** `ottogin/erdos-3`  
**Freeze-date review:** 2026-10-01  
**Pinned environment:** Lean 4.33.1, `ghcr.io/ottogin/lean-mathlib@sha256:964547ad81e109c78545512867bae70b710c55d833078674878faad7de0ebb85`

## Formally closed event-window contribution

Two theorems now compile with no proof holes under the exact organizer-pinned environment:

1. `Erdos3.ap_subprogression_of_le`:
   if (S \subseteq A) is an arithmetic progression of length (k) and (m \le k), then (A) contains an arithmetic progression of length (m).

2. `Erdos3.ap_frequently_iff_every_length`:
   the protected conclusion
   [
   \exists^\mathrm{frequently} k\to\infty,\; \exists S\subseteq A,\; S.\mathrm{IsAPOfLength}(k)
   ]
   is equivalent to
   [
   \forall m,\; \exists T\subseteq A,\; T.\mathrm{IsAPOfLength}(m).
   ]

Exact pinned run `36879690920`, job `110427986166`, passed. Both theorems print exactly the evaluator-allowed axioms:

`[propext, Classical.choice, Quot.sound]`.

No `sorry`, custom axiom, or unpinned environment is used.

## Relation to the canonical target

These theorems do **not** prove Erdős Problem 3. They close a formal representational bridge on the conclusion side: the filter-based protected statement is now formally interchangeable with the customary "arithmetic progressions of every finite length" formulation.

The hard implication from nonsummability of reciprocal mass to arithmetic progressions remains untouched.

## Freeze-date formal-library review

Scoped searches of the pinned FormalConjectures/Mathlib ecosystem and public GitHub did not locate an exact existing theorem matching `ap_subprogression_of_le` or `ap_frequently_iff_every_length`. Public formal-conjectures projects do use `Set.IsAPOfLength` and manually unfold its representation in other arithmetic-progression work, confirming that this is shared formal vocabulary.

Absence of an exact search hit is not proof of novelty. Mathematically, D3 is elementary; its plausible competition value is as a new, reusable **formalization/reduction**, not as a new combinatorial theorem.

## Competition disposition

- Parent Erdős-3 solution: **NO**.
- Formal correctness: **PASS**.
- Pinned environment/axiom gate: **PASS**.
- Direct correspondence to canonical target: **PASS**.
- Mathematical novelty: **not claimed**.
- New formalization/reduction novelty: **plausible but requires competition review**.
- Recommended modality: **M2 / narrow formalized partial**, unless the competition workflow assigns a different formalized-partial code.

## Sources checked

- Google DeepMind `formal-conjectures` AP vocabulary and Erdős statements.
- Mathlib pinned revision `0df444a360eaa60ab8c11dca51a86af692955474`.
- Scoped public GitHub/web searches for the exact theorem names and equivalent AP-truncation statements.

## Remaining gates

1. Section 8 human roster/class/resource/publication-authority fields;
2. competition submission ID/workflow and final evaluator report;
3. organizer novelty/usefulness determination for M2 credit.

## Claim boundary

This is a formalization/reduction contribution only. It does not establish the reciprocal-divergence implication, solve Erdős Problem 3, or independently determine competition novelty or score.
