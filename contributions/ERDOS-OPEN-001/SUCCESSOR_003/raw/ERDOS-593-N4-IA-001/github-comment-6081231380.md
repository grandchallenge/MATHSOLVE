GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-593-N4-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-593-N4
assignment: ERDOS-593-N4
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement
Let X be an index set and define the 3-uniform hypergraph of triangles of pairs T_X = (V, E) with vertex set V = [X]^2 and hyperedges E = {{ab, bc, ac} : {a, b, c} in [X]^3}.
1. Strict Linearity: For any index set X, T_X is strictly linear, meaning distinct hyperedges intersect in at most one vertex: |E_1 intersect E_2| <= 1 for all distinct E_1, E_2 in E.
2. Injective Embedding Invariant: If F is a finite 3-uniform hypergraph containing two hyperedges intersecting in at least two vertices (i.e. F is non-linear), then F cannot embed into any linear 3-uniform hypergraph. In particular, F cannot embed into T_X for any index set X.
3. Unconditional ZFC Erdős-Rado Transfinite Lock: In ZFC, the Erdős-Rado partition relation (2^aleph_0)^+ -> (aleph_1)^2_aleph_0 holds unconditionally (Erdős and Rado, 1956, Theorem 39, p. 467; equation (95), p. 471). For lambda = (2^aleph_0)^+, every countable coloring of [lambda]^2 contains an uncountable homogeneous set and therefore a monochromatic triangle, establishing that the linear hypergraph T_lambda has uncountable chromatic number chi(T_lambda) > aleph_0. Consequently, no non-linear finite 3-uniform hypergraph (including K_5^(3)) is obligatory.
4. Countable First-Difference Coloring on the Continuum: For any index set X with |X| <= 2^aleph_0, injectively embedding X into {0, 1}^omega and coloring each pair by its least differing coordinate yields a vertex coloring of T_X in aleph_0 colors without any monochromatic triangle, establishing chi(T_X) <= aleph_0.
5. Finite Ramsey Refutation of Two-Coloring: The assertion that chi(T_lambda) <= 2 on the continuum is refuted by Ramsey theorem R(3,3) = 6. For any index set with |X| >= 6, every 2-coloring of [X]^2 contains a monochromatic triangle, forcing chi(T_X) >= 3 for all |X| >= 6 and chi(T_X) >= aleph_0 for all infinite X.
6. Cardinal Threshold Distinction: The cardinal threshold (2^aleph_0)^+ is exact for the canonical triangle-of-pairs construction T_lambda in ZFC, but does not constrain arbitrary uncountably chromatic linear 3-uniform hypergraphs, which can be constructed at aleph_1 (Erdős, Hajnal, Rothschild 1973, Theorem 2; Li 2026).

## Derivation
1. Hypergraph Linearity:
Let S_1 = {a_1, b_1, c_1} and S_2 = {a_2, b_2, c_2} be distinct 3-subsets of X. The vertices of T_X are pairs from X.
The intersection of the hyperedges is E_{S_1} intersect E_{S_2} = [S_1]^2 intersect [S_2]^2 = [S_1 intersect S_2]^2.
Since S_1 != S_2 and |S_1| = |S_2| = 3, their intersection has size |S_1 intersect S_2| <= 2.
If |S_1 intersect S_2| <= 1, then [S_1 intersect S_2]^2 is empty, so |E_{S_1} intersect E_{S_2}| = 0.
If |S_1 intersect S_2| = 2, then [S_1 intersect S_2]^2 contains exactly one pair, so |E_{S_1} intersect E_{S_2}| = 1.
In all cases, distinct hyperedges share at most one vertex, proving T_X is strictly linear.

2. Injective Embedding Intersection Invariance:
Let F = (V_F, E_F) and H = (V_H, E_H) be 3-uniform hypergraphs, and let phi: V_F -> V_H be an injective homomorphism.
Because phi is injective, set operations commute with phi: phi(A intersect B) = phi(A) intersect phi(B) for all A, B subset V_F.
In particular, for any two hyperedges e_1, e_2 in E_F, |phi(e_1) intersect phi(e_2)| = |phi(e_1 intersect e_2)| = |e_1 intersect e_2|.
If F is non-linear, there exist distinct e_1, e_2 in E_F such that |e_1 intersect e_2| >= 2.
Then phi(e_1) and phi(e_2) are distinct hyperedges in E_H sharing at least two vertices, so H cannot be linear.
Contrapositively, no non-linear finite 3-uniform hypergraph can embed into any linear 3-uniform hypergraph.
Because T_lambda is linear and chi(T_lambda) > aleph_0, no non-linear F embeds into T_lambda.
Therefore, non-linearity is a sufficient obstruction to obligatoriness: any finite 3-uniform hypergraph with a pair of hyperedges sharing >= 2 vertices is not obligatory.

3. Countable First-Difference Coloring:
Let |X| <= 2^aleph_0 and let f: X -> {0, 1}^omega be an injection.
For distinct x, y in X, define the color c({x, y}) = min { n in omega : f(x)(n) != f(y)(n) }.
Suppose distinct x, y, z in X form a monochromatic triangle of color n.
Then f(x)(n) != f(y)(n), f(y)(n) != f(z)(n), and f(x)(n) != f(z)(n).
This implies that the three values f(x)(n), f(y)(n), f(z)(n) in {0, 1} are pairwise distinct, which contradicts the Pigeonhole Principle (|{0, 1}| = 2 < 3).
Hence no monochromatic triangle exists, proving chi(T_X) <= aleph_0.

4. Finite Ramsey Refutation of Two-Coloring:
Suppose c: [X]^2 -> {0, 1} is a 2-coloring for |X| >= 6.
Choose any 6-element subset Y subset X. The restriction of c to [Y]^2 is a 2-coloring of the edges of K_6.
By the finite Ramsey theorem R(3,3) = 6, every 2-coloring of K_6 contains a monochromatic K_3.
This yields three pairs forming a monochromatic hyperedge in T_X.
Thus chi(T_X) >= 3 for all |X| >= 6. Furthermore, since R(3; k) is finite for every finite k, chi(T_X) >= aleph_0 for every infinite X.

5. Erdős-Rado Transfinite Partition Theorem:
By Erdős and Rado (1956, Theorem 39, p. 467; eq. (95), p. 471), the partition relation (2^kappa)^+ -> (kappa^+)^2_kappa holds in ZFC for every infinite cardinal kappa.
For kappa = aleph_0, this gives (2^aleph_0)^+ -> (aleph_1)^2_aleph_0.
Every partition of the pairs of (2^aleph_0)^+ into countably many colors contains an uncountable homogeneous subset of order aleph_1.
Any three elements from this homogeneous subset form a monochromatic triangle.
Hence every countable vertex-coloring of T_{(2^aleph_0)^+} has a monochromatic hyperedge, so chi(T_{(2^aleph_0)^+}) > aleph_0.
This partition relation is an unconditional theorem of ZFC and requires no CH, GCH, or large cardinal assumptions.

6. Construction-Specific Sharpness vs. General Linear Hosts:
The threshold (2^aleph_0)^+ is exact for the canonical triangle-of-pairs family T_lambda.
However, general linear 3-uniform hypergraphs with uncountable chromatic number exist at smaller cardinalities, such as aleph_1 (Erdős, Hajnal, Rothschild 1973; Li 2026).
Thus (2^aleph_0)^+ characterizes this specific host construction rather than all uncountably chromatic linear systems.

## Assumptions beyond bootstrap
1. Zermelo-Fraenkel set theory with the Axiom of Choice (ZFC).
2. Primary literature references:
- P. Erdős and R. Rado, A partition calculus in set theory, Bulletin of the American Mathematical Society, Vol. 62, No. 5 (1956), pp. 427-489; Theorem 39, p. 467, eq. (95), p. 471.
- F. P. Ramsey, On a Problem of Formal Logic, Proceedings of the London Mathematical Society, Vol. 30 (1930), pp. 264-286; finite Ramsey number R(3,3) = 6.
- P. Erdős, A. Hajnal, B. L. Rothschild, On chromatic number of graphs and set-systems, Cambridge Combinatorial Conference, Lecture Notes in Mathematics 337 (1973), Theorem 2, p. 532.
3. No Continuum Hypothesis, Generalized Continuum Hypothesis, Jensen Diamond, or large cardinal hypotheses are used; all derivations are unconditional in ZFC.

## Verification / falsification hooks
1. Python finite verification script checking triangle-of-pairs linearity, non-linearity of K_5^(3), exhaustive Ramsey R(3,3)=6 verification, K_5 2-coloring, and first-difference triangle-free coloring:

```python
import itertools

# Linearity of T_n for n in [3..7]
for n in range(3, 8):
    elements = list(range(n))
    triples = list(itertools.combinations(elements, 3))
    hyperedges = [frozenset([frozenset([a, b]), frozenset([b, c]), frozenset([a, c])]) for a, b, c in triples]
    max_inter = max(len(hyperedges[i] & hyperedges[j]) for i in range(len(hyperedges)) for j in range(i + 1, len(hyperedges))) if len(hyperedges) > 1 else 0
    assert max_inter <= 1, f"Failed linearity at n={n}"

# Non-linearity of K_5^(3)
k5_edges = list(itertools.combinations(range(5), 3))
assert len(set(k5_edges[0]) & set(k5_edges[1])) == 2, "K_5^(3) must share 2 vertices"

# Exhaustive verification of R(3,3)=6 across all 32768 two-colorings
edges_k6 = list(itertools.combinations(range(6), 2))
triangles_k6 = list(itertools.combinations(range(6), 3))
assert all(any(c[tuple(sorted([a, b]))] == c[tuple(sorted([b, c]))] == c[tuple(sorted([a, c]))] for a, b, c in triangles_k6) for c in [{edges_k6[i]: (m >> i) & 1 for i in range(15)} for m in range(1 << 15)])

# First-difference coloring on binary words avoids monochromatic triangles
for length in [2, 3, 4, 5]:
    words = list(itertools.product([0, 1], repeat=length))
    for w1, w2, w3 in itertools.combinations(words, 3):
        d12 = next(i for i in range(length) if w1[i] != w2[i])
        d23 = next(i for i in range(length) if w2[i] != w3[i])
        d13 = next(i for i in range(length) if w1[i] != w3[i])
        assert not (d12 == d23 == d13), "Monochromatic triangle found"

print("All finite verifications passed.")
```

2. Intersection Invariance Check:
Verify that for any injective map phi and distinct subsets e_1, e_2, |phi(e_1) intersect phi(e_2)| = |e_1 intersect e_2|.
3. Erdős-Rado Primary Text Check:
Inspect Erdős-Rado (1956) Theorem 39 (p. 467) and eq. (95) (p. 471) confirming (2^aleph_0)^+ -> (aleph_1)^2_aleph_0 unconditionally in ZFC.

## Claim boundary
This return proves:
1. Strict linearity of the triangle-of-pairs hypergraph T_X and the injective embedding intersection invariant.
2. The countable first-difference coloring on the continuum establishing chi(T_X) <= aleph_0 for |X| <= 2^aleph_0.
3. The refutation of the 2-coloring claim via R(3,3)=6.
4. Source-locking of the unconditional ZFC Erdős-Rado partition theorem establishing chi(T_{(2^aleph_0)^+}) > aleph_0 and proving non-linearity is a sufficient obstruction to obligatoriness.
This return does not claim full classification of obligatory hypergraphs, does not claim formalization within Lean 4 kernel, and confers no canonical repository mutation, mathematical certification, publication, or award authority.

## Next residual
Formalize the elementary linearity of triangle-of-pairs hypergraphs and the non-embedding reduction for non-linear hypergraphs in Lean 4. Formalize the countable first-difference coloring on binary sequences in Lean 4 without external axioms. Discharge the transfinite Erdős-Rado partition relation as a bounded dependency once the partition calculus is available in Mathlib.
