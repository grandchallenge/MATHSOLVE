# Erdős #602: Lean-checked finite-in-neighbour reduction

**Object:** `ERDOS-602-LIST-CORE-001`  
**Status:** `LIST_CORE_KERNEL_CHECKED__SET_BRIDGE_CI_REPLAYED__SOURCE_PROVIDER_IMPORT_AND_MATHCERT_OPEN`  
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

There are no `sorry` or `admit` proof tactics in the list-core declarations. Compiler proof checking was performed locally on an authenticated OS transport, then replayed in protected GitHub CI; this is **not** MATHCERT certification. Local execution-capture ID: `b656ab3dfaa8419da3a7d75656f4ea5c`, which is supporting operator evidence, not a substitute for protected CI.

## Limitations and adversarial review

- Finite pairwise intersections by themselves do **not** produce finite incoming-neighbour lists. Constructing `P` remains an additional obligation.
- The unrestricted binary-prefix family in the source handoff has Property B but is not essentially disjoint. Therefore the stronger conclusion is not an admissible blanket strategy for Erdős #602.
- `EscapesEveryList` formalizes list-finitary infinitude, which agrees with ordinary infinitude in the usual classical setting. The explicit equivalence to Mathlib `Set.Infinite`, as well as conversion of `Set.Finite` to `List` witnesses `W` and `P`, is **not formalized in this file**.
- The `IsMonochromatic` predicate is structurally identical to the pinned formal provider's pointwise definition, but a Mathlib import and exact-provider theorem bridge have not been compiled.
- The theorem proves non-monochromaticity, **not** the stronger claim that each colour occurs infinitely often. The latter remains a written extension in the admitted handoff.
- No attempt is made to prove the provider's open `erdos_602` theorem or its separate `countable_index` `sorry`. No priority, originality, universality, external validity, or certification is claimed.

## Mathlib set-theoretic bridge — 2026-11-21

Source: [MathSolve/Erdos/E602SetBridge.lean](../../MathSolve/Erdos/E602SetBridge.lean), introduced in [MATHSOLVE PR #1272](https://github.com/grandchallenge/MATHSOLVE/pull/1272).

This new, independently formulated Mathlib theorem uses `Set.Finite` and `Set.Infinite`, rather than requiring callers to provide the list-core witness objects directly. It formally proves:

1. A Mathlib finite set admits a finite list cover, and conversely; `EscapesEveryList` is equivalent to `Set.Infinite`.
2. If every distinct pairwise intersection is finite and each index has a finite set of **incoming overlap-neighbours**, then deleting their shared points (with the diagonal excluded) leaves the family infinite and pairwise disjoint.
3. That family admits Property B. Only intersecting pairs must be orientable, and oriented cycles are allowed. The no-singleton-intersection requirement is not used.

The Mathlib theorem uses a local source-parallel `HasPropertyB` definition structurally matching the pinned FormalConjectures provider; **the actual pinned provider declaration has not been imported**. Exact upstream source-identity concordance is therefore still an independent obligation.

**First source-checked replay:** GitHub Actions [formal-targets, run 44901703595](https://github.com/grandchallenge/MATHSOLVE/actions/runs/44901703595/job/136838832657) at candidate `9537b0883f241751f8942f85aa1349b12bdcd2ce`. Lean 4.29.1 and pinned Mathlib commit `5e932f97dd25535344f80f9dd8da3aab83df0fe6` reported for all four bridge theorems only `[propext, Classical.choice, Quot.sound]`. Actual compiler output was independently inspected, not inferred from a green job status.

**Compiler gate correction:** The first run of PR #1272 (job `136838207884`) had two unresolved equality-direction goals yet reported success because a shell pipe to `tee` masked the Lean exit status; the original error scanner also anchored to the start of the line. The same PR now sets `set -euo pipefail` and rejects `sorryAx`, `error:`, and `warning:` in the new Lean output, including indented messages. Three bounded negative shell controls correctly failed: a failing process piped to `tee`, an indented `sorryAx`, and a file-prefixed `error:`. The valid replay is **the repaired exact-head run**, not the earlier false-green run.

**Remaining mathematical obligations:** formalize the locally countable intersection-graph corollary and the binary-prefix example showing that Property B need not entail essential disjointness; then directly bind to the pinned FormalConjectures source or record precise semantic limitations, and independently review any claim before MATHCERT promotion. The unrestricted Erdős #602 problem remains **OPEN**. No MATHCERT certificate is issued by this handoff.

## Countable-index source-parallel theorem — 2026-11-21

**New candidate:** `MathSolve/Erdos/E602SetBridge.lean`, theorem
`propertyB_of_countableIndex`, with companion
`countable_index_source_parallel`.

If the *index type* is countable, each member `A i` is infinite, and
each pairwise intersection is finite, then the family has Property B.
The proof chooses an injective rank `I → ℕ`; each index has finitely
many smaller ranks. Its incoming-overlap predecessors therefore satisfy
the already kernel-checked `propertyB_of_finiteIncoming` theorem.

This result needs **neither** member-wise countability **nor** the
no-singleton-intersection restriction. The source-parallel wrapper has
the precise hypotheses/conclusion shape of the pinned
`erdos_602.variants.countable_index` mathematical proposition, except
that it refers to MATHSOLVE's *local* definition of `HasPropertyB`.
The actual pinned formal-conjectures declaration is **not imported**.
The stronger classical Bernstein lemma for a countable family without
any pairwise-intersection restriction is **not proved by this argument**.

The locally countable intersection-graph corollary for an arbitrary,
possibly uncountable index type and the binary-prefix obstruction
remain separate formal obligations. No unrestricted theorem or
MATHCERT promotion is claimed.

**Evidence status:** proof candidate until exact-head pinned Mathlib
compilation, axiom report, operational review and protected merge
readback establish the result.

## Componentwise countable-overlap extension — 2026-11-21

**Candidate declaration:** `MathSolve.Erdos602.propertyB_of_countableOverlapComponents`
in [E602SetBridge.lean](../../MathSolve/Erdos/E602SetBridge.lean).

Let `part : I → C` label components, where `I` and `C` may both be
uncountable. Suppose each fiber `{i | part i = c}` is countable and
any two intersecting distinct family members have the same label.
If every member is infinite and distinct pairwise intersections are
finite, then the whole family has Property B.

**Proof construction:** choose an injective rank into `ℕ` separately
for every fiber, with no global countability requirement. For each
`i`, only finitely many same-fiber indices have smaller ranks. These
supply the finite predecessor sets required by
`propertyB_of_finiteIncoming`. Different fibers cannot have
intersections, so their independent rankings do not conflict.

**Boundary:** this is *not yet* the complete local-countability-of-overlap
theorem. That theorem additionally requires a formal proof that a graph
with countable vertex neighborhoods has countable connected
components, followed by a component-label construction for the
overlap relation. Neither has been discharged here.

Source identity with pinned upstream formal-conjectures, global
Erdős #602, and MATHCERT certification remain unresolved.
This addition is a candidate until exact-head CI, axiom audit,
protected merge and readback complete.
