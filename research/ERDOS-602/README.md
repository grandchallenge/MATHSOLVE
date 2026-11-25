# Erdős #602: Lean-checked finite-in-neighbour reduction

**Object:** `ERDOS-602-LIST-CORE-001`  
**Status:** `BINARY_PREFIX_KERNEL_REPLAYED__LOCAL_COUNTABLE_GRAPH_KERNEL_CHECKED__SOURCE_PROVIDER_IMPORT_AND_MATHCERT_OPEN`  
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

**Remaining mathematical obligations at the original 2026-11-21 bridge intake:** the locally countable intersection-graph corollary and binary-prefix counterexample. Both have since been kernel-replayed in later sections. Direct pinned FormalConjectures source identity, any independent MATHCERT promotion and the unrestricted Erdős #602 question remain **OPEN**.

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

**Evidence update:** this tranche was protected-merged in [PR #1278](https://github.com/grandchallenge/MATHSOLVE/pull/1278) after pinned Lean exact-head checks and readback; not MATHCERT-certified.

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

**Boundary at PR #1279:** the countable-neighbourhood-to-component proof was still open. It was discharged in protected-merged [PR #1280](https://github.com/grandchallenge/MATHSOLVE/pull/1280).

Source identity with pinned upstream formal-conjectures, global
Erdős #602, and MATHCERT certification remain unresolved.
The componentwise theorem subsequently passed exact-head CI and was protected-merged in PR #1279.

## Locally countable overlap graph — 2026-11-21

**Candidate declaration:** `MathSolve.Erdos602.propertyB_of_locallyCountableOverlaps`
in [E602SetBridge.lean](../../MathSolve/Erdos/E602SetBridge.lean).

Given a family `A : I → Set X` where every member is infinite,
distinct pairwise intersections are finite, and **each indexed member
meets only countably many distinct other indexed members**, the whole
family has Property B. The index type `I` and ground type `X` need
not be countable. The prohibition on singleton intersections is not
used by this sufficient theorem.

**Graph calculation:** define a simple graph on indices by adjacency
`i ≠ j ∧ (A i ∩ A j).Nonempty`. Each neighbor set is countable by
hypothesis. The new private general-purpose graph lemma proves that
each connected-component support is countable: vertices reachable
in `n` steps form a countable set by induction, and the union over
`n : ℕ` remains countable. The previously proved componentwise rank
theorem supplies a global binary coloring. This closes the
*graph-to-countable-component* implication that was explicitly
open after PR #1279.

**Scope:** This is the locally countable overlap-graph corollary from
the admitted MATH-PROGRAMME research handoff, not the unrestricted
Erdős #602 theorem. In particular, the original finite-intersection
and no-singleton conditions do not impose a countability bound on
the number of *different members* meeting a given member.

The graph theorem passed exact-head pinned Lean CI and was protected-merged in PR #1280. Direct source-provider identity and MATHCERT remain separate. The stronger classical Bernstein lemma for families with arbitrary intersections is not established.

## Binary-prefix sharpness obstruction — 2026-11-21

**Candidate formalization:** `MathSolve.Erdos602.BinaryPrefix.binaryPrefix_sharpness`
in [E602SetBridge.lean](../../MathSolve/Erdos/E602SetBridge.lean).
This is the concrete example called **Counterexample C** in the admitted
[essential-disjointness handoff](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/docs/handoffs/ERDOS-602-ESSENTIAL-DISJOINTNESS-001.md).

Take the index type `ℕ → Bool` (all infinite binary streams) and the
countable ground type `List Bool ⊕ Fin 2` (all finite binary strings
plus two separate marker points). Each indexed member consists of all
finite prefixes of its stream together with the same two markers.
The formal proof obligations are:

- All members are countably infinite. The prefixes have different
  lengths, providing an injective infinite subset.
- For distinct streams, their first differing bit bounds the length of
  all common prefixes. Hence intersections are finite.
- Each pairwise intersection contains both marker points, so its
  `Set.ncard` cannot be one.
- Colour the two markers differently; every indexed member receives
  both colours, so the family has Property B.
- The streams are uncountable by Cantor diagonalization, while the
  ground type is countable. Infinite, mutually disjoint residuals after
  finite deletions would give an injection from streams to the ground
  type, a contradiction.

The formal conclusion is **not** a counterexample to Property B or
a resolution of Erdős #602. It refutes the proposed *stronger*
universal finite-deletion essential-disjointness lemma within the
exact original hypothesis class. The earlier locally-countable-overlap
theorem is not contradicted: in this example each member overlaps
every other member through the common markers, and there are
uncountably many members.

**Evidence:** exact-source pinned Lean replay in [PR #1281](https://github.com/grandchallenge/MATHSOLVE/pull/1281), GitHub Actions [run 44958812891, formal-targets job 137012797695](https://github.com/grandchallenge/MATHSOLVE/actions/runs/44958812891/job/137012797695), at source head `0941054572c75f827a066f4e7c07a7c9f231a17b`. All ten exact-head checks succeeded; six new declarations printed their expected axiom reports, with only standard `propext`, `Classical.choice` and `Quot.sound` collectively, and no `sorryAx` or compiler diagnostics. Protected admission requires its own final exact-head replay and readback if the PR head changes. Upstream FormalConjectures provider identity and MATHCERT certification remain open.

## Pinned provider extraction and full Bernstein lemma — 2026-11-23

The original upstream `FormalConjectures/ErdosProblems/602.lean` is
preserved byte-for-byte as `upstream-602.lean.txt` with its Apache
license, at provider commit `85f863718beeec7b58a3a1926ee92e3472bc2020`,
Git blob `9b85fd453afcfa95c6572e2a98d214d50f7e8caa`.
`ci/validate_erdos602_source.py` checks the original Git blob and the
entire deterministic source extract (with three negative controls).
`MathSolve/FormalConjectures/E602SourceExtract.lean` preserves the
upstream predicate declarations and right-hand-side propositions. Its
import and wrappers are adapted, with no upstream proof holes imported.
`E602Correspondence.lean` imports this extract and the existing
MATHSOLVE proof module; it proves definitional equality of both
predicates and the unrestricted target, and supplies a proof of the
exact extracted countable-index proposition and its True-iff wrapper.

This is a **source-locked extracted-declaration bridge**, not a build
of the entire upstream FormalConjectures package or its answer
elaborator. The provider pins Lean/Mathlib 4.27.0, while MATHSOLVE pins
Lean 4.29.1 and Mathlib 5e932f97dd25535344f80f9dd8da3aab83df0fe6.
Neither dependency pin is changed. The actual upstream `sorry` is
not modified. Full native-provider integration remains a separate
compatibility obligation.

The new `bernstein_nat` and `bernstein_countable` proofs establish
Bernstein's lemma for any countable family of infinite sets, without
requiring finite intersections, countability of the members, or the
no-singleton restriction. At each natural-number stage, choose two
distinct points of the current infinite set outside the finite set of
all previous witnesses; the used sets grow monotonically, so no red
witness can equal any blue witness. Colour blue witnesses 1 and every
other point 0. A surjective natural-number enumeration covers every
nonempty countable index type, and the empty case is vacuous.

The original unrestricted conjecture remains open. No mathematical
certification or external promotion is claimed. Admission evidence
must be tied to the final exact candidate head, checked Lean logs,
and protected-main readback.

## Minimal-transversal route — 2026-11-24

This tranche changes proof strategy: instead of seeking disjoint
residuals, exploit the forbidden singleton intersection directly.
A vertex cover T meets every member of the family. It is
inclusion-minimal exactly when each x in T has a private witness
edge B with B intersect T = {x}.

**Reduction:** suppose A is an edge contained in a minimal cover T.
Choose x in A and its private witness B. Then A intersect B = {x}.
If B = A, this contradicts the two-point minimum for every edge;
otherwise it contradicts the forbidden singleton intersection.
Thus every edge meets both T and its complement. This is the
classical minimal-transversal/Lovasz argument, not a novelty claim.

**Construction under a sufficient hypothesis:** if a cover T meets
each edge in a nonempty finite trace, the covers contained in T
have an inclusion-minimal member by Zorn's lemma. For any nonempty
chain of such covers, fix an edge A and choose a chain member V
minimizing the natural cardinality of A intersect V. The trace of V
is nonempty and finite. If another member W is contained in V,
its trace is contained in V's and by minimal cardinality equal to it.
If V is contained in W, V's trace is contained in W's. Thus any point
of the minimizing trace survives the entire chain. The intersection
of the chain is still a cover. This argument permits uncountably many
members and unbounded finite intersection sizes.

The new Lean declarations are `minimalCover_iff_privateWitnesses`,
`propertyB_of_minimalCover`, `minimalCover_of_finiteTraces`,
and `propertyB_of_finiteTraceCover`. The latter uses the original
ncard != 1 hypothesis, plus infinitude and a finite-trace cover.
In fact finite trace plus infinite edges already gives Property B
by the indicator of T; the significant new route is the general
minimal-cover reduction, which permits infinite traces. The
finite-trace existence theorem is a baseline, not a solution.

**Literature:** Csernak and Soukup, *Minimal vertex covers in infinite
hypergraphs*, Discrete Mathematics 346 (2023), 113280,
https://doi.org/10.1016/j.disc.2022.113280
(preprint https://arxiv.org/abs/2103.10340, Observation 1.6 and
Theorem 1.4 in the preprint). They prove minimal-cover existence
for countably infinite edges under a uniform finite bound on the
intersection of a fixed finite number of distinct edges.
This is a useful known regime beyond pairwise bounds. The present
Lean work does not formalize their existence theorem.

**Frontier:** The original assumptions do not immediately give a
finite-trace cover or a minimal cover. A finite-trace-cover strategy
cannot be universal: take a maximal almost-disjoint family on
the naturals extending a countable partition into infinite sets
(Zorn), and replace every point by two copies. Every edge is countably
infinite; pair intersections are finite and even; the two-copy
colouring gives Property B. Any cover projects to an infinite subset
because it must meet every partition member. Maximality guarantees
that some original edge has infinite intersection with the projection,
hence its doubled edge has infinite intersection with the cover.
This obstruction is a paper argument, not yet Lean-checked.
The next substantive issue is minimal-cover existence with arbitrary
finite pairwise intersections and no singleton intersections, or
a weaker witnessed-cover construction that suffices for splitting.
No claim of unrestricted closure or MATHCERT certification.

## Conditional obstruction to universal minimal covers — 2026-11-24

**Result (paper proof under CH; local lemmas submitted for Lean replay):**
assuming the Continuum Hypothesis, there exists a family satisfying all
original Erdos #602 premises which has Property B but no inclusion-minimal
vertex cover. Thus a general ZFC proof of minimal-cover existence from
those premises would imply the negation of CH. This is not an obstruction
to Property B itself. No novelty or independence claim is made.

### Construction before doubling

Assume CH and enumerate all subsets of N as (T_alpha : alpha < omega_1).
Start with a countably infinite partition P of N into infinite sets
(for instance, the fibers of the first coordinate under a bijection
N with N x N). Construct an increasing almost-disjoint family F_alpha
of infinite subsets of N, starting with P, by transfinite recursion.
At limit stages take unions. Every stage below omega_1 contains only
countably many edges because alpha is countable and at most one edge
is added at each successor stage.

At stage alpha put D = N minus T_alpha. Consider the dichotomy:

1. If D is contained modulo finitely many points in a finite union
   of members of F_alpha, do not add an edge.
2. Otherwise enumerate the countably infinite F_alpha as (B_n : n in N).
   For every n the set D minus (B_0 union ... union B_n) is infinite.
   Choose distinct d_n in that set, also avoiding all previously
   chosen d_m. Add B = {d_n : n in N}. This is an infinite subset of D;
   for each m, only d_0,...,d_(m-1) could belong to B_m.
   Consequently the new edge has finite intersection with every old
   edge, including every partition cell, and is not an old edge.

Let F be the union of the construction. Every member is countably
infinite and distinct members intersect finitely. Any vertex cover T
of F must be infinite, since it meets every cell of P.

To exclude minimality, locate the stage enumerating T. Case 2 would
have added an edge disjoint from T, contradicting coverage. Thus case 1
held: D is almost contained in the union of some finite K subset F.
For any B in F outside K, its intersection with each member of K
is finite, as is D minus the union of K. Hence B minus T is finite.
Since B is infinite, B intersect T is infinite. Therefore all singleton
private-witness edges for T must belong to K. Each such edge witnesses
at most one point of T. An infinite T cannot have a private witness
for every point, so T is not minimal.

This is a complete conditional paper construction using CH and ordinary
transfinite recursion; the enumeration and recursion themselves have
not been formalized in Lean. The proof does not require a maximal
almost-disjoint family or any additional saturation assumption.

### Doubling to enforce the original restriction

On N x {0,1} replace each B in F by B x {0,1}. All members are
countably infinite; for distinct B,C the intersection has size
2|B intersect C|, finite and never one. The second-coordinate coloring
splits every member. If S were a minimal cover of the doubled family,
its projection T onto N would cover F. For every x in T choose a
representative (x,b) in S and a private witness B x {0,1} whose
intersection with S is precisely {(x,b)}. Projecting this identity
gives B intersect T = {x}: if y lies in B intersect T, some (y,c)
belongs to S and must equal (x,b). Thus T would be a minimal cover
of F, impossible. This yields the promised CH counterexample to
universal minimal-cover existence, not a counterexample to Erdos #602.

### Formal scope

The candidate Lean declarations are:
- `not_minimalCover_of_finitePrivateEdges`: an infinite cover with
  finitely many possible private-witness edges is not minimal.
- `not_minimalCover_of_almostCoveredCompl`: the preceding obstruction
  for almost-disjoint families and a complement almost covered by a
  finite union of edges.
- `minimalCover_doubled_projects`: a minimal cover of the doubled family
  projects to a minimal cover of the original.
- `doubled_propertyB_and_noSingleton`: the doubled family is explicitly
  two-colorable when the members are nonempty and its pairwise
  intersection cardinalities are never one.

No CH assumption is introduced as a global Lean axiom. The separate
transfinite construction and its exact CH hypothesis remain a formal
obligation. Admission of the local reductions requires exact-head
compiler replay and protected readback.

### Consequence for the research programme

The minimal-transversal implication remains sound, but universal
existence is too strong at least consistently with ZFC (relative to
the consistency of ZFC+CH). This obstruction is stronger than the
earlier finite-trace-cover obstruction. The next mathematical route
must allow covers with redundant points and establish splitting
directly; for example, preserve a two-color witness condition rather
than insist on a private singleton witness for every selected point.
The original unrestricted conjecture remains open.

Literature comparator: Csernak and Soukup, arXiv:2103.10340v1,
Theorem 1.4 (countably infinite edges, a uniform finite bound on
r-wise intersections), Observation 1.6 (private witness criterion).
Their theorem concerns a stronger uniform-bound hypothesis and does
not prove or refute this CH construction. See
https://arxiv.org/abs/2103.10340. The argument above is supplied
explicitly, not attributed to that paper.
