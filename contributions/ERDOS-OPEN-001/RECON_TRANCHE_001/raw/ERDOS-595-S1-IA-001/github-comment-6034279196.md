GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-595-S1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-595-S1
assignment: ERDOS-595-S1
disposition: SOURCE_INTERFACE_FOUND
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement

1. Primary Bibliographic Resolution:
The problem originated in joint work of Paul Erdos and Andras Hajnal, published in:
- P. Erdos, "Problems and results on set systems and hypergraphs", Extremal Problems for Finite Sets (Visegrad, 1991), Bolyai Society Mathematical Studies, Vol. 3, Janos Bolyai Mathematical Society, Budapest, 1994, pp. 217-227; Mathematical Reviews MR 95k:05131 (MR1318048).
The problem asks: Does there exist an infinite K_4-free graph that is not the union of countably many triangle-free graphs? This problem is cataloged as Erdos Problem 595 and Prize Problem Ledger PPL 032 ($250 reward, open since 1970).

The finite predecessor theorems are established by two landmark papers:
- J. Folkman, "Graphs with monochromatic complete subgraphs in every edge coloring", SIAM Journal on Applied Mathematics, Vol. 18, No. 1, pp. 19-24 (January 1970); DOI: 10.1137/0118004; MR0268080. (Note: The citation in Lean formalization 595.lean line 27 lists Vol. 19:340-345; the correct primary publication data is Vol. 18, No. 1, pp. 19-24). Folkman proves the existence of a finite K_4-free graph not partitionable into 2 triangle-free graphs.
- J. Nesetril and V. Rodl, "Type theory of partition properties of graphs", Recent Advances in Graph Theory (Proc. Second Czechoslovak Sympos., Prague, 1974), Academia, Prague, 1975, pp. 405-412; MR0409259. Nesetril and Rodl generalize Folkman to all finite n >= 1: for every n >= 1, there exists a finite K_4-free graph not partitionable into n triangle-free graphs.

2. Cardinality and Compactness Audit:
Any counterexample graph G = (V, E) must have uncountable vertex set |V| >= aleph_1. Every countable graph G on V with |V| <= aleph_0 is trivially a countable union of triangle-free graphs because the complete countable graph K_omega decomposes into countably many stars, which are triangle-free (formally verified in Lean 595.lean theorem complete_nat_is_union). Compactness (De Bruijn-Erdos) fails to lift finite Folkman/Nesetril-Rodl graphs to the countable union setting because every finite subgraph is countable and thus trivially countably triangle-free.

3. Consistency Audit:
S. Shelah, "Consistency of positive partition theorems for graphs and models", Set Theory and its Applications (Toronto, ON, 1987), Lecture Notes in Mathematics, Vol. 1401, Springer, Berlin, 1989, pp. 167-193; MR1034564 (Shelah archive Sh:289). Shelah established the consistency with ZFC of the existence of an infinite K_4-free graph not decomposable into countably many triangle-free graphs. Whether such a graph exists in ZFC alone remains an open problem.

4. Definition Reconciliation:
In primary literature, a graph G = (V, E) is the union of countably many triangle-free graphs if E = \bigcup_{i < omega} E_i where each (V, E_i) is K_3-free, which is equivalent to the existence of an edge-coloring c: E -> N without monochromatic triangles. The protected Lean definition Erdos595.IsCountableUnionOfTriangleFree defined via the complete lattice supremum G = \bigsqcup_{i : N} H_i with each H_i clique-free 3 is semantically identical, as proven by Lean theorem reformulation_edge_colouring.

## Derivation

1. Audit of Original Formulation and Finite Theorems:
Erdos and Hajnal formulated the question in the context of infinite partition relations and chromatic numbers of hypergraphs and graphs (Erdos 1994, MR 95k:05131). The finite question is solved:
- Theorem (Folkman 1970, Theorem 1): For every positive integer k, there exists a finite graph G such that G is K_{k+1}-free and in every 2-coloring of the edges of G, there is a monochromatic K_k. For k = 3, G is K_4-free and cannot have its edges partitioned into 2 triangle-free graphs.
- Theorem (Nesetril and Rodl 1975, Section 2): For every finite graph A with clique number omega(A) and any positive integer r, there exists a graph B with omega(B) = omega(A) such that B -> (A)^2_r. For A = K_3 and r = n, this yields a finite K_4-free graph whose edges cannot be colored with n colors without producing a monochromatic triangle.

2. Uncountable Cardinality Necessity:
Let G = (V, E) be any graph with |V| <= aleph_0. Identify V with a subset of N. The complete graph K_omega on N decomposes into stars:
E(K_omega) = \bigcup_{m \in N} { {m, v} : v \ne m }.
Each star graph H_m is triangle-free: if {a, b, c} formed a triangle in H_m, then each edge {a, b}, {a, c}, {b, c} must contain the center m, forcing at least two of {a, b, c} to equal m, contradicting distinctness of vertices.
Since G is a subgraph of K_omega, E(G) = \bigcup_{m \in N} (E(G) \cap E(H_m)), decomposing G into countably many triangle-free subgraphs. Hence, no countable graph can be a counterexample. Any counterexample must satisfy |V| >= aleph_1.

3. Failure of Compactness:
The De Bruijn-Erdos compactness theorem asserts that an infinite graph has chromatic number <= k if and only if all its finite subgraphs have chromatic number <= k. However, for decomposition into countably many triangle-free graphs, every finite subgraph H of any graph G has |V(H)| finite, so H trivially decomposes into |V(H)| <= aleph_0 triangle-free stars. Thus, every finite subgraph of any graph satisfies the condition, so compactness cannot establish or refute the infinite property.

4. Dependency Table:
Source Claim -> Exact Hypotheses -> Relevance to Protected Target -> Semantic Match/Conflict -> Confidence
- Folkman (SIAM J. Appl. Math. 18:19-24, 1970) -> Finite graphs, 2 edge colors, forbidden K_{k+1} -> Establishes base case n = 2 for finite analogue -> Perfect semantic match -> High
- Nesetril-Rodl (Academia Prague, 1975, pp. 405-412) -> Finite graphs, arbitrary n edge colors, forbidden K_{p} -> Establishes full finite analogue (variants.folkman_finite) -> Perfect semantic match -> High
- Erdos-Hajnal (Bolyai Soc. Math. Stud. 3, 1994, pp. 217-227) -> Infinite graphs, forbidden K_4, countable decomposition -> Definitional source of Problem 595 -> Perfect semantic match -> High
- Shelah (Springer LNM 1401, 1989, pp. 167-193, Sh:289) -> Set-theoretic forcing models, partition relations -> Establishes consistency of non-decomposable K_4-free graph -> Compatible extension -> High
- Lean formalization (595.lean) -> Lattice supremum ⨆ i, H i and edge-coloring equivalence -> Formal target representation -> Isomorphic match -> High

## Assumptions beyond bootstrap

None. All derivations and audits rely strictly on standard ZFC set theory, finite Ramsey theory, and the cited primary literature.

## Verification / falsification hooks

1. Bibliographic Verification:
- Folkman (1970): DOI: 10.1137/0118004; MR0268080.
- Nesetril-Rodl (1975): MR0409259.
- Erdos (1994): MR1318048 / MR 95k:05131.
- Shelah (1989): MR1034564.
2. Formalization Hooks:
- Formal definition: Erdos595.IsCountableUnionOfTriangleFree in FormalConjectures/ErdosProblems/595.lean.
- Monotonicity theorem: erdos_595.variants.subgraph_of_countable_union.
- Star decomposition of K_omega: erdos_595.variants.complete_nat_is_union.
- Edge-coloring equivalence: erdos_595.variants.reformulation_edge_colouring.

## Claim boundary

This audit establishes the primary bibliographic identities, verifies the mathematical equivalence between the primary literature and the Lean formalization, and details the structural gap between finite Folkman/Nesetril-Rodl graphs and the infinite problem. It documents that the problem is open in ZFC and consistent via Shelah Sh:289, without asserting a mathematical resolution of the conjecture in ZFC.

## Next residual

Determine whether the existence of an uncountable K_4-free graph that is not the union of countably many triangle-free graphs is provable in ZFC or independent via forcing models. Formally verify in Lean the finite Folkman-Nesetril-Rodl theorem for general n >= 1. Extend the formalization to capture Shelah's consistency result in an axiomatic extension of ZFC.
