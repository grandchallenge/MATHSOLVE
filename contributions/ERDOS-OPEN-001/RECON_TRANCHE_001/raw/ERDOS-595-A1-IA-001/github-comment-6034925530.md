GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-595-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-595-A1
assignment: ERDOS-595-A1
disposition: COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

The protected finite theorem does not imply the registered infinite target by disjoint union, direct limit, ordinary first-order compactness, or merely by obtaining one graph whose triangle-free cover number exceeds every finite integer.

Write tau_triangle(G) for the least cardinality of a family of triangle-free subgraphs whose edge sets cover E(G).

Using the protected fact, choose for every positive integer n a finite K4-free graph H_n with tau_triangle(H_n) > n. Let

G = bigsqcup_{n >= 1} H_n.

Then:

1. G is K4-free.
2. tau_triangle(G) > n for every finite n.
3. Nevertheless tau_triangle(G) = aleph_0, so G is the union of countably many triangle-free graphs.

Thus even a single graph simultaneously witnessing failure of every finite cover bound need not witness failure of countable coverability. The missing step is exactly the jump from requiring arbitrarily many finite colors to failing countable coverability.

The same example can be made into a coherent direct system: set G_N = bigsqcup_{1 <= n <= N} H_n. Then G_1 subseteq G_2 subseteq ..., each G_N is finite and K4-free, tau_triangle(G_N) > N, and the direct limit bigcup_N G_N still has cover number exactly aleph_0. Therefore finite-stage coherence by inclusion is not enough.

## Derivation

For (1), every K4 in a disjoint union lies inside one connected component, but each H_n is K4-free.

For (2), suppose G were covered by k < infty triangle-free subgraphs. Restrict those subgraphs to the component H_k. Restriction preserves triangle-freeness and gives a cover of H_k by at most k triangle-free subgraphs, contradicting tau_triangle(H_k) > k.

For (3), G is a countable disjoint union of finite graphs, so E(G) is countable. Enumerate its edges e_0, e_1, ... Each one-edge subgraph is triangle-free, and these countably many subgraphs cover E(G). Hence tau_triangle(G) <= aleph_0. By (2), tau_triangle(G) is not finite, so tau_triangle(G) = aleph_0.

This also identifies the compactness boundary.

For a fixed finite k, coverability by k triangle-free subgraphs is equivalent to an edge-coloring by k colors with no monochromatic triangle: from a cover, choose one containing cover member for each edge; conversely, the color classes are triangle-free. In the pure graph language this quantifies over edge subsets or colorings, so it is not an ordinary first-order graph formula. It can be represented in a finite relational expansion using k binary color predicates, but the existence of such an expansion is an existential second-order property of the underlying graph.

K4-freeness itself is first-order and therefore survives ordinary ultraproducts by Los. The finite-cover obstruction does not transfer so directly in the pure graph language. More importantly, even if an ultraproduct or another limit construction could be shown to satisfy tau_triangle(G) > k for every finite k, that yields only tau_triangle(G) >= aleph_0, not tau_triangle(G) > aleph_0.

Countable coverability is genuinely different. If one introduces predicates C_0, C_1, ... for countably many triangle-free cover classes, the assertion that every edge belongs to some C_i requires a countable disjunction E(x,y) -> bigvee_{i < omega} C_i(x,y), which is not an ordinary first-order formula. Moving to an infinitary language admits such a formula but forfeits the ordinary compactness theorem that the naive argument needs.

There is also a model-theoretic obstruction to any proposed ordinary first-order route: a satisfiable first-order theory in a countable language with an infinite graph model has a countable elementary submodel by downward Lowenheim-Skolem. Every countable graph is trivially a countable union of one-edge triangle-free subgraphs. Hence ordinary first-order compactness alone cannot force the target property of not being a countable union of triangle-free graphs.

## Assumptions beyond bootstrap

None beyond standard graph-theoretic semantics for union or cover by triangle-free subgraphs: their edge sets cover the ambient edge set.

No external literature, sibling return, campaign discussion, or later repository state was used.

## Verification / falsification hooks

1. Verify directly that restriction of a triangle-free cover of G to a component H_n is a triangle-free cover of H_n.
2. Verify that E(bigsqcup_n H_n) is countable because each H_n is finite.
3. Formalize the fixed-k equivalence: tau_triangle(G) <= k if and only if there exists c : E(G) -> {0, ..., k-1} with no monochromatic triangle.
4. Any proposed compactness proof should identify the exact formal sentence that is supposed to express not countably coverable; if it uses countably many color predicates, check where the required infinite disjunction enters.
5. A purported implication that unbounded finite cover numbers force the Erdős target is falsified by the explicit disjoint-union construction above.

## Claim boundary

This is a counterexample to the naive finite-to-countable bridge, not a counterexample to Erdős problem 595 itself.

It does not show that the desired infinite K4-free graph does or does not exist. It shows that the protected finite Folkman or Nesetril-Rodl phenomenon, even assembled coherently into one graph with unbounded finite triangle-free cover number, does not by itself cross the cardinal threshold required by the target.

## Next residual

Construct a K4-free graph that diagonalizes against all countable edge-colorings rather than merely unbounded finite covers. Successor routes must use genuinely infinitary set-theoretic structure since finite compactness and unbounded finite cover number are insufficient.
