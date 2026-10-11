# Two exact elementary boundaries for the Erdős catalogue

STATUS: PROOF_CANDIDATE_WITH_FINITE_ADVERSARIAL_REPLAY
MATHEMATICAL_SCOPE: LOCAL_THEOREM_NOT_PARENT_PROBLEM
SOURCE_SEMANTIC_AUTHORITY: PENDING_CRITICAL_REVIEW
LEAN_KERNEL_COMPLETION: NOT_CLAIMED
DISTINCT_AGENT_INDEPENDENCE: NOT_ATTESTED
MATHSOLVE_DISPATCH_OR_MATHCERT_AUTHORITY: NONE

This note extends the return and critical review on Erdős 241 and 595.
It is a complete **ordinary mathematical proof** of two conditional,
finite/combinatorial theorem families, with independently specified
exhaustive **finite tests**. It is **not** a solution, originality claim,
source-acceptance act, formal kernel proof, or authorized new work package.

Source surfaces:
- Erdős 241: MATH-PROGRAMME #1510, RESULT/1 6098842021,
  critical source/replay review #2509.
- Erdős 595: MATH-PROGRAMME #1866, RESULT/1 6098889544,
  critical source/replay review #2511.
- Existing replay-only prior: MATHSOLVE
  `contributions/ERDOS-OPEN-001/CATALOGUE_LOCAL_REPLAY_001/REVIEW_HANDOFF.md`.
- This tranche: `python ci/erdos_241_595_theorem_boundaries.py`.
  No external libraries, calls, mutable online data or Mathlib required.

## Pinned formal statement semantics checked directly

The underlying original provider files were fetched through GitHub at
`google-deepmind/formal-conjectures@85f863718beeec7b58a3a1926ee92e3472bc2020`.
These are **statement/source checks** only, not Lean builds or acceptance.

- Erdős 241, `FormalConjectures/ErdosProblems/241.lean`,
  blob `8e462d92fcd1e87cb8b211bc8ceaee42ae60a089`, defines
  `f N r` using `Multiset ℕ`, `m.card = r`,
  `m.sum` equality and `m₁=m₂` for finite subsets of
  `Finset.Icc 1 N`. This exactly matches repeated summands
  modulo permutation in the integer B_h theorem when restricted
  to A⊆[1,N]. The generalized theorem herein permits arbitrary
  integer A; no claim of an existing Lean `ZMod` lift is made.
  The formalized asymptotic theorem bodies contain `sorry`.
- Erdős 595, `FormalConjectures/ErdosProblems/595.lean`,
  blob `c7ae92d69247ed107099978b9c7bce2cc319af76`,
  defines `IsCountableUnionOfTriangleFree G` as existence of
  `H : ℕ → SimpleGraph V`, each `CliqueFree 3`,
  with `G = ⨆ i, H i`; the main question also requires
  `CliqueFree 4`. The theorem B proof uses the **stronger**
  hypothesis that every H_i is bipartite. Thus its conclusion
  *implies* a triangle-free decomposition, but cannot be used
  in reverse to characterize arbitrary triangle-free covers.
  The main conjectural assertion remains `sorry`.

Both semantic distinctions are required for any promoted
mathematical statement. They do not imply originality, correctness
of the historical paper references or completion of external
source-semantic referee review.

## Theorem A · arbitrary-order strong B_h, exact safe modulus

Fix an integer h≥1 and finite A⊆ℤ, with h-element *multisets*
(repetition permitted, order ignored). Write S_h(A) for the multiset
family and `s(T)=sum(T)`. Define the *integer strong B_h* property:
s(T)=s(U) implies T=U for all T,U∈S_h(A).

For integer modulus M≥1, the **modular** strong B_h property requires
s(T)≡s(U) (mod M) to imply T=U. This explicitly uses original labelled
integer summands; modular collisions are never silently discarded.

**(A1, exact criterion)** If A is not strong B_h in ℤ, it is not
strong B_h modulo *any* M≥1. If it is strong B_h in ℤ, form the finite
set of positive nonzero differences

`D_h(A) = {|s(T)-s(U)| : T,U∈S_h(A), T≠U}`.

Then A is strong B_h modulo M **if and only if**
`M ∤ d` for every `d∈D_h(A)`.

*Proof.* Integer equality is a modular equality for every M.
Conversely, for an integer-B_h set, each pair of distinct multisets
has a **nonzero** integer sum difference d. Such a pair collides mod M
exactly when M divides d. The finite pairwise condition is therefore
necessary and sufficient. If distinct elements a,b in A were
identified mod M, adjoining h−1 copies of any fixed element gives a
collision among h-multisets, so no extra injectivity assumption on
A→ℤ/Mℤ has been silently omitted. QED.

**(A2, diameter bound)** If A is nonempty and
`d=max(A)-min(A)`, then for every `M>h*d` integer and modular
strong B_h are equivalent.

*Proof.* Every h-term sum lies in
`[h*min(A),h*max(A)]`. Any two such sums differ by at most h*d.
When M>h*d a congruence between sums forces integer equality:
a nonzero multiple of M cannot have magnitude <M. In the other
direction integer-equal sums always remain congruent, so the two
strong-B_h properties are equivalent. QED.

**(A3, universal sharpness)** For every h≥1 and d≥1, take
A={a,a+d}. Its h-multiset sums are exactly
`h*a + k*d`, k=0,...,h, all distinct, so A is integer strong B_h.
At `M=h*d`, the 0- and h-copy sums differ by exactly M and collide.
Thus one cannot replace the *uniform* strict bound `M>h*d` by
`M≥h*d` for all A.

**(A4, improvement for particular sets)** The bound is sufficient,
not individually necessary. For h=3, A={1,4}, the four unordered
triple sums are {3,6,9,12}; modulo M=4 they are {3,2,1,0},
all distinct, even though `4<3*(4-1)+1=10`.
Criterion A1, not the diameter bound, identifies exactly which
smaller moduli are safe.

**Consequences for Erdős 241.** For A⊆{1,...,N}, h=3,
M≥3N−2 is a sharp *uniform* sufficient threshold. More generally
modular strong-B_h always implies integer strong-B_h for any
chosen integer representatives (since integer equality implies
modular equality). The converse needs A1 or A2. A cyclic B3
construction may be lifted to its integer representatives in that
direction; an integer B3 set cannot be reduced modulo an arbitrary
small modulus without a collision check. Neither assertion settles
`f(N) / N^(1/3)→1`.

## Theorem B · exact bipartite edge-cover number

Let G=(V,E) be a simple undirected graph with finite nonempty
vertex set. Let `b(G)` be the least integer t≥0 for which G has
t *spanning*, bipartite edge-subgraphs whose edge sets cover E.
Overlapping edge sets are allowed. Let `χ(G)` be its usual positive
chromatic number.

**(B1, finite exact characterization)** For every t≥0,

`b(G)≤t` if and only if `χ(G)≤2^t`.

*Forward proof.* For each of the t bipartite subgraphs H_i choose
a proper 2-colouring `c_i:V→{0,1}` (isolated vertices can be
assigned arbitrarily). Give each vertex its bit vector
`c(v)=(c_1(v),...,c_t(v))`.
Every edge uv of G belongs to some H_i, so
`c_i(u)≠c_i(v)`, hence `c(u)≠c(v)`. This is a proper colouring
using ≤2^t bit vectors. If t=0, there can be no edges and the
empty bit-vector yields a proper one-colouring.

*Reverse proof.* Choose a proper colouring of G into at most 2^t
colours, and inject its used colours into `{0,1}^t`.
For each bit i define H_i to contain precisely those G-edges
whose endpoint colour-codes have different i-th bits. Each H_i
is bipartite, split by that bit. Each G-edge joins different
codes and therefore differs in at least one bit: it lies in
some H_i. This gives the required cover. QED.

In particular `b(G)=ceil(log_2 χ(G))` for nonempty finite
graphs, with `b(G)=0` when χ(G)=1.
For K_m, `b(K_m)=ceil(log_2 m)`: the finite sharpness is exact,
not merely a construction for complete graphs.

**(B2, countable analogue, in ZFC).** A graph admits a countable
family of bipartite spanning subgraphs covering its edges if and
only if it admits a proper vertex colouring into
`{0,1}^ℕ`, i.e. chromatic cardinal ≤`2^aleph_0`.

The same proofs as B1 apply with countable bit vectors. The
forward direction chooses a 2-colouring of each bipartite
subgraph; ordinary choice is available in ZFC. For the reverse
direction, an edge differs in at least one coordinate, so it is
in at least one coordinate-cut graph.

**(B3, precise relevance to Erdős 595)** Every graph on at most
continuum many vertices has a countable bipartite cover (inject
its vertices into binary sequences), hence a countable cover by
triangle-free spanning subgraphs. Therefore any counterexample
to Erdős 595 (a K4-free graph *not* covered by countably many
triangle-free graphs) must in particular have χ(G)>continuum
(and therefore |V|>continuum).

The converse DOES NOT follow: a triangle-free graph may itself
have arbitrarily high chromatic number, so failure of a
countable **bipartite** cover does *not* imply failure of a
countable **triangle-free** cover. B1–B3 give a **necessary
cardinal barrier**, not a solution of Erdős 595.

## Hostile finite regression

The committed independent script exhausts:
- 1,008 A⊆[1,N] choices with 1≤h≤4 and 2≤N≤7,
  checking 14,856 set/modulus conditions against both A1 and A2;
- 99 two-point sharpness instances for 1≤h≤9 and 1≤d≤11;
- 1,099 *all* labelled simple graphs on 1≤|V|≤5,
  checking 4,396 graph/layer decisions independently by (i)
  brute-force vertex colouring and (ii) all unions of vertex
  bipartition cuts, t=0,1,2,3.

Finite enumeration checks examples and hostile boundaries.
The universally quantified proofs above rest on their elementary
integer/arithmetic and graph-colouring arguments, not on finite
testing. None of these proofs has been checked by Lean.

## Separate claim and acceptance boundaries

1. The exact theorem families are eligible for ordinary critical
   review and, if useful, later formalization of A1–A3 or B1.
2. Verify exact original/source definitions from the pinned
   Formal Conjectures versions, especially unordered multisets and
   bipartite vs merely triangle-free covers, before SOURCE_ACCEPTED.
3. Do not infer mathematical novelty, a solved Erdős problem,
   independent external-worker proof provenance, publication,
   MATHFORGE claim admission, protected MATHSOLVE worker launch, or
   MATHCERT certification from this note or the CI run.
4. The existing native Erdős 241 and 595 work packages and their
   prior findings remain unchanged. Never create a duplicate
   dispatch or assert that this replaces the asymptotic and
   infinite-cardinal unresolved boundaries.
