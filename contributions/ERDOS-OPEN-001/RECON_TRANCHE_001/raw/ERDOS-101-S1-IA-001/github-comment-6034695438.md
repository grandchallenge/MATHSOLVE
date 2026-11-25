GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-101-S1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-101-S1
assignment: ERDOS-101-S1
disposition: SOURCE_INTERFACE_FOUND
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement

1. Canonical Problem Formulation and Primary Provenance:
Erdos Problem 101 is cataloged on erdosproblems as problem 101 and in the Prize Problem Ledger as PPL 099 ($100 prize offered by Paul Erdos; linked to OEIS sequence A006065).
The problem was posed across several primary problem papers by Paul Erdos:
- P. Erdos, "Some combinatorial problems in geometry", Mathematische Semesterberichte, Vol. 31, pp. 205-213 (1984); MR0768228.
- P. Erdos, "Some problems on number theory and combinatorial geometry", Combinatorial Mathematics, Lecture Notes in Mathematics, Vol. 1385, Springer, pp. 166-173, p. 170 (1989); MR1017409.
- P. Erdos, "Some of my favourite problems in various branches of combinatorics", Matematiche (Catania), Vol. 45, pp. 231-240 (1990); MR1152069.
- P. Erdos, "Some of my favourite problems on tables and graphs", The Mathematics of Paul Erdos I, Algorithms and Combinatorics, Vol. 13, Springer, Berlin, pp. 58-69, p. 66 (1997); MR1425178.
- B. Green, "100 Open Problems", Problem 71 (2014): "Suppose that A \subset R^2 is a set of size n with c n^2 collinear 4-tuples. Does it contain 5 points on a line?"
Conjecture: For any set S of n points in R^2 with no five collinear, the number of lines containing exactly four points of S is o(n^2).

2. Best Current Exponent and Order of Bounds:
- Upper Bound: O(n^2).
  Pair counting alone gives t_4 <= n(n-1)/12 \approx 0.0833 n^2.
  Melchior's projective Euler characteristic inequality in RP^2 (E. Melchior, "Uber Vielseite der Projektiven Ebene", Deutsche Math. 5 (1940), pp. 461-475) establishes t_2 >= t_4 + 3 under the no-5-collinear condition. Substituting into pair counting gives the sharpest unconditional upper bound:
  t_4 <= (n(n-1) - 6) / 14 \approx (1/14) n^2 \approx 0.0714 n^2.
  General incidence theorems (such as Szemerédi-Trotter, Combinatorica 3 (1983), pp. 381-392; MR0729791) rely purely on K_{2,2}-freeness of the incidence graph and cannot beat O(n^2), because abstract linear 4-uniform hypergraphs (e.g., Steiner systems S(2, 4, n)) achieve n(n-1)/12 = \Theta(n^2).
- Lower Bound: n^{2 - c / sqrt(log n)} = n^{2 - o(1)}.
  J. Solymosi and M. Stojakovic, "Many collinear k-tuples with no k+1 collinear points", Discrete & Computational Geometry, Vol. 50, No. 3, pp. 811-818 (2013); DOI: 10.1007/s00454-013-9527-3; arXiv:1203.4380; MR3107052.
  Solymosi and Stojakovic construct planar point sets with no k+1 collinear points containing at least n^{2 - c_k / sqrt(log n)} collinear k-tuples using high-dimensional Behrend-type arithmetic progression-free sets projected into R^2. For k = 4, this establishes that t_4 can be as large as n^{2 - o(1)}, surpassing any power n^{2 - \epsilon} for fixed \epsilon > 0, while remaining consistent with the o(n^2) conjecture due to the subpolynomial factor 2^{-c sqrt(log n)}.

3. The Bezout Algebraic Group Barrier:
Classical orchard constructions achieving \Theta(n^2) collinear triples (k = 3) rely on the group law of cubic curves (S. A. Burr, B. Grunbaum, N. J. A. Sloane, Geometriae Dedicata 2 (1974), pp. 397-424; B. Green and T. Tao, Discrete Comput. Geom. 50 (2013), pp. 409-468). By Bezout's theorem, an irreducible cubic curve intersects any straight line in at most 3 points. Thus, all 1-dimensional algebraic groups over R (lines d = 1, conics d = 2, cubics d = 3) support zero 4-rich lines. By the Elekes-Szabo theorem (Combinatorica 32 (2012), pp. 537-590), \Theta(n^2) collinear 4-tuples cannot arise from low-degree abelian group symmetries.

## Derivation

1. Audit of Incidence Geometry Bounds:
- Szemerédi-Trotter (1983): I(P, L) <= C(n^{2/3} m^{2/3} + n + m). For lines with >= 4 points, 4 t_4 <= I(P, L_4) <= C(n^{2/3} t_4^{2/3} + n + t_4) \implies t_4 = O(n^2). Because the proof depends only on the Crossing Lemma for graph drawings, it applies equally to any pseudoline arrangement or abstract bipartite incidence graph without K_{2,2}, both of which permit \Theta(n^2) lines of size 4.
- Multiplicity Cap Four / Melchior Inequality:
  Points dualize to lines in RP^2 forming cell complex with V vertices, E edges, F faces.
  Euler characteristic \chi(RP^2) = V - E + F = 1.
  Summing face boundaries \sum_{i >= 3} i f_i = 2E and vertex degrees \sum_{k >= 2} k t_k = 2E yields:
  t_2 = 3 + \sum_{k >= 4} (k - 3) t_k + \sum_{i >= 4} (i - 3) f_i >= 3 + \sum_{k >= 4} (k - 3) t_k.
  Under the no-5-collinear cap (t_k = 0 for k >= 5), this yields t_2 >= t_4 + 3.
  Combining with pair partition \binom{n}{2} = t_2 + 3 t_3 + 6 t_4 >= 7 t_4 + 3 yields t_4 <= (n(n-1) - 6) / 14.

2. Dependency Map (Combinatorial vs. Geometric Inputs):
- Combinatorial Inputs:
  - Pair Counting: \sum \binom{k}{2} t_k <= \binom{n}{2}. Purely combinatorial; stops at n^2 / 12.
  - Crossing Lemma / ST: Bipartite graph crossing number. Purely topological/combinatorial; stops at O(n^2).
  - Steiner Systems S(2, 4, n): Abstract linear 4-hypergraphs achieving n^2 / 12 with no 5-element hyperedges.
- Geometric Inputs:
  - Projective Euler characteristic (Melchior): Requires RP^2 topological embedding; improves constant to 1/14.
  - Bezout Theorem: Algebraic intersections with algebraic curves; eliminates cubic group law constructions.
  - Behrend projection (Solymosi-Stojakovic): Projecting sphere/grid subsets without APs; proves n^{2 - o(1)} lower bound.

3. Dependency Table:
Source Claim -> Exact Hypotheses -> Relevance to Protected Target -> Semantic Match/Conflict -> Confidence
- Erdos (Sem. Ber. 31:205-213, 1984; LNM 1385, 1989) -> Planar point sets, no 5 collinear -> Original conjecture t_4 = o(n^2) -> Exact semantic match -> High
- Melchior (Deutsche Math. 5:461-475, 1940) -> Planar projective line arrangements -> Bound t_2 >= t_4 + 3 under t_{>=5} = 0 -> Exact match -> High
- Szemerédi-Trotter (Combinatorica 3:381-392, 1983) -> Incidence of points and lines in R^2 -> Establishes general O(n^2) barrier -> Exact match -> High
- Burr-Grunbaum-Sloane (Geom. Dedicata 2:397-424, 1974) -> Orchard problem for 3-point and 4-point lines -> Foundational configuration constructions -> Exact match -> High
- Solymosi-Stojakovic (DCG 50:811-818, 2013) -> Point sets with no k+1 collinear -> Lower bound t_4 >= n^{2 - c / sqrt(log n)} -> Exact match -> High
- Green (100 Open Problems, Problem 71, 2014) -> n-point sets with c n^2 4-tuples -> Dual formulation of Problem 101 -> Exact match -> High
- Lean 101.lean (DeepMind FormalConjectures) -> numLinesWithFourPointMax, erdos_101 -> Protected formal target definition -> Exact isomorphic match -> High

## Assumptions beyond bootstrap

None. All derivations and mappings rely strictly on standard projective geometry, incidence combinatorics, and cited primary literature.

## Verification / falsification hooks

1. Primary Bibliographic Identifiers:
- Erdos (1984): MR0768228.
- Erdos (1989): MR1017409.
- Erdos (1997): MR1425178.
- Melchior (1940): Deutsche Math. 5, pp. 461-475.
- Szemerédi-Trotter (1983): Combinatorica 3, pp. 381-392; MR0729791.
- Solymosi & Stojakovic (2013): DOI: 10.1007/s00454-013-9527-3; arXiv:1203.4380; MR3107052.
2. Formalization Hooks:
- Formal definition: Erdos101.linesWithPointsFor, Erdos101.numLinesWithFourPointMax in FormalConjectures/ErdosProblems/101.lean.
- Asymptotic statement: erdos_101 =o[atTop] (fun n => (n : R)^2).
- Finite check: 4 x 4 grid (n = 16) yields t_4 = 10, satisfying 10 <= (16 * 15 - 6) / 14 = 234 / 14 \approx 16.71.

## Claim boundary

This audit documents that Erdős Problem 101 remains open. The best proved upper bound is O(n^2) with leading coefficient 1/14 via Melchior's theorem, and the best proved lower bound is n^{2 - c / sqrt(log n)} via Solymosi and Stojakovic (2013). This audit documents the structural obstruction separating combinatorial incidence theory from the geometric o(n^2) conjecture without asserting a proof that t_4 = o(n^2).

## Next residual

Determine whether higher-dimensional Behrend-type projections can be modified to produce an algebraic configuration with Omega(n^2) 4-rich lines or if an o(n^2) upper bound can be derived via higher-order polynomial partitioning. Formalize in Lean the Melchior projective Euler characteristic inequality showing t_2 >= t_4 + 3 under the no-5-collinear condition. Investigate whether the Elekes-Szabo algebraic group obstruction can be extended to ruled surfaces and higher-degree curve configurations.
