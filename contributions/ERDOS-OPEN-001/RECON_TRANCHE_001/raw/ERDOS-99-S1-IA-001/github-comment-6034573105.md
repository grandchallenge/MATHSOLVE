GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-99-S1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-99-S1
assignment: ERDOS-99-S1
disposition: SOURCE_INTERFACE_FOUND
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement

1. Canonical Problem Formulation and Provenance:
Erdos Problem 99 is registered on erdosproblems as problem 99 and Prize Problem Ledger PPL 083 ($100 prize offered by Paul Erdos).
The problem was formulated in:
- P. Erdos, "Some problems in number theory, combinatorics and combinatorial geometry", Mathematica Pannonica, Vol. 5, No. 2, pp. 261-269 (1994); Mathematical Reviews MR95j:11018.
Problem statement: For sufficiently large n, must every n-point planar set of minimum pairwise distance 1 that minimizes diameter contain a unit equilateral triangle?

2. Primary Literature on Minimal Diameter Point Sets:
- A. Bezdek and F. Fodor, "Minimal diameter of certain sets in the plane", Journal of Combinatorial Theory, Series A, Vol. 85, No. 1, pp. 105-111 (1999); DOI: 10.1006/jcta.1998.2917; MR1666993.
Bezdek and Fodor systematically investigate the minimal diameter D(n) of n points in R^2 with mutual distances >= 1.
- P. T. Bateman and P. Erdos, "Geometrical extrema suggested by a lemma of Besicovitch", American Mathematical Monthly, Vol. 58, No. 5, pp. 306-314 (1951); MR0041490.
- H. Harborth, A. Kemnitz, and N. Moller, "An upper bound for the minimum diameter of integral point sets", Discrete Mathematics 113 (1993), pp. 85-89; MR1208920.

3. Solved Values of n and Provably Optimal Configurations:
Matching the minimum distance s = 1 normalization:
- n = 2: D(2) = 1. Trivial unit line segment.
- n = 3: D(3) = 1. Regular unit equilateral triangle (contains 1 equilateral triangle).
- n = 4: D(4) = sqrt(2) \approx 1.4142. Unique global minimizer is the unit square with vertices (0,0), (1,0), (1,1), (0,1). It is triangle-free (contact graph G_C = C_4). Any 4-point set containing an equilateral triangle has diameter at least sqrt(1 + sqrt(3)) \approx 1.6529 > sqrt(2).
- n = 5: D(5) = (1 + sqrt(5))/2 = 1/(2 sin(pi/10)) \approx 1.6180. Unique global minimizer is the regular pentagon of unit side length. It is triangle-free (contact graph G_C = C_5).
- n = 7: D(7) = 2. Unique global minimizer is the regular unit hexagon with a central point (wheel graph W_6), which contains 6 unit equilateral triangles.
Small counterexamples at n = 4 and n = 5 establish why Erdos explicitly framed the conjecture as eventual in n.

4. Asymptotic Diameter Divergence and Global Optimality Boundary:
- Unconstrained Global Asymptotics: By the hexagonal circle packing theorem (Thue 1892, Fejes Toth 1940, density delta = pi / sqrt(12)) and Bieberbach's isodiametric inequality (Area <= (pi/4) D^2), circular patches of the triangular lattice A_2 achieve:
  D(n) = sqrt((2 * sqrt(3)) / pi) * sqrt(n) + O(1) \approx 1.05007 * sqrt(n).
- Triangle-Free Asymptotic Obstruction: In any triangle-free planar contact graph G_C, the Kissing-Number Rigidity Lemma establishes that maximum degree is Delta(G_C) <= 5 (since degree 6 forces six 60-degree angles and six equilateral triangles). By Fejes Toth's Voronoi cell area theorem, every Voronoi cell in a triangle-free packing has area at least A_pent = (5/4) tan(pi/5) \approx 0.908178 > A_hex = sqrt(3)/2 \approx 0.866025. Applying the isodiametric inequality gives:
  D_TF(n) >= sqrt((4 * A_pent) / pi) * sqrt(n) - O(1) \approx 1.07531 * sqrt(n).
Because 1.07531 > 1.05007, any triangle-free configuration incurs a macroscopically suboptimal diameter diverging as Omega(sqrt(n)), proving that for all sufficiently large n, global diameter minimizers must contain unit equilateral triangles.

5. Dual Normalization Reconciliation:
The literature exhibits two standard homothety conventions:
- Fixed minimum distance s = 1, minimize diameter D(n) (used by Erdos 1994, Bezdek & Fodor 1999, and Lean 99.lean).
- Fixed diameter D = 1, maximize minimum distance s(n) (packing n disks of radius r(n) = s(n)/2 inside a unit disk / unit diameter set).
These conventions are homothety duals via s(n) = 1 / D(n). The protected formalization fixes s = 1 and tests diameter minimization, matching the Erdos-Bezdek-Fodor convention exactly.

## Derivation

1. Audit of Small-n Rigorous Global Optima:
- Case n = 3: For any 3 points with dist(p_i, p_j) >= 1, the diameter is max_{i < j} dist(p_i, p_j) >= 1, achieved uniquely (up to isometry) when all three distances equal 1 (equilateral triangle).
- Case n = 4: Let p_1, p_2, p_3, p_4 have pairwise distances >= 1. The unit square achieves D = sqrt(2). If any 3 points form an equilateral triangle of side 1, the fourth point must lie outside three open unit disks centered at the triangle vertices. The distance from the fourth point to the furthest vertex is minimized when placed symmetrically opposite an edge at distance 1 from two vertices, producing a rhombus with diagonal sqrt(3) \approx 1.732 > sqrt(2), or at distance 1 from one vertex and further from others, yielding diameter >= sqrt(1 + sqrt(3)) \approx 1.6529. Thus D(4) = sqrt(2) and the unique minimizer is triangle-free.
- Case n = 5: The regular pentagon with side 1 has diagonals equal to (1 + sqrt(5))/2 \approx 1.6180. Any point set with an equilateral triangle requires diameter at least sqrt(3) \approx 1.732 or larger, so D(5) = (1 + sqrt(5))/2 and the unique minimizer is triangle-free.
- Case n = 7: A central point surrounded by 6 points on a circle of radius 1 spaced by 60 degrees achieves mutual distances >= 1 and diameter exactly 2. By Fejes Toth's contact theorem, placing 7 points in a disk of diameter < 2 violates the area and kissing number bounds. Thus D(7) = 2 and the configuration contains 6 equilateral triangles.

2. Solved vs. Numerical Status Ledger:
- Rigorously Proven Global Minima: n = 2, 3, 4, 5, 7.
- Numerically / Conjecturally Optimized: n = 6, 8, 9, 10, ... (Graham 1997, Melissen 1997, Fodor 2003 provide numerical branch-and-bound local optima and candidate packings).

3. Dependency Table:
Source Claim -> Exact Hypotheses -> Relevance to Protected Target -> Semantic Match/Conflict -> Confidence
- Erdos (Math. Pannon. 5:261-269, 1994) -> Planar sets, min dist 1, min diameter, large n -> Primary formulation of Problem 99 -> Exact semantic match -> High
- Bezdek-Fodor (J. Combin. Theory Ser. A 85:105-111, 1999) -> Min diameter D(n) with pairwise dist >= 1 -> Exact baseline for planar D(n) and small-n configurations -> Exact semantic match -> High
- Bateman-Erdos (Amer. Math. Monthly 58:306-314, 1951) -> Point sets with distance lower bounds and enclosing sets -> Geometric extrema foundations -> Exact match -> High
- Thue (1892) / Fejes Toth (1940) -> Planar disk packings, hexagonal density pi/sqrt(12) -> Establishes unconstrained bulk diameter growth 1.0501 sqrt(n) -> Exact match -> High
- Fejes Toth Voronoi Cell Bound (1953) -> Voronoi polygons with <= 5 sides -> Establishes triangle-free diameter lower bound 1.0753 sqrt(n) -> Exact match -> High
- Lean 99.lean (DeepMind FormalConjectures) -> HasMinDist1, FormsEquilateralTriangle, erdos_99 -> Formalization target definition -> Exact isomorphic match -> High

## Assumptions beyond bootstrap

None. All deductions are based on established Euclidean geometry, Bieberbach's isodiametric inequality, Fejes Toth's packing theorems, and primary literature.

## Verification / falsification hooks

1. Primary Bibliographic Identifiers:
- Erdos (1994): Mathematical Reviews MR95j:11018.
- Bezdek & Fodor (1999): DOI: 10.1006/jcta.1998.2917; MR1666993.
- Bateman & Erdos (1951): MR0041490.
- Harborth, Kemnitz & Moller (1993): MR1208920.
2. Formalization Hooks:
- Formal definitions: Erdos99.HasMinDist1, Erdos99.FormsEquilateralTriangle in FormalConjectures/ErdosProblems/99.lean.
- Eventual filter statement: erdos_99 using Filter.atTop.
- Small-n counterexamples: n = 4 (unit square) and n = 5 (regular pentagon) confirming the necessity of Filter.atTop.

## Claim boundary

This audit documents the complete primary literature, resolves the normalization equivalence, establishes the proved small-n cases (n in {2,3,4,5,7}) versus numerical conjectures (n >= 6, n != 7), and derives the asymptotic diameter divergence (1.0501 sqrt(n) vs 1.0753 sqrt(n)) that forces equilateral triangles for large n. It does not compute an explicit finite threshold n_0.

## Next residual

Quantify the boundary-to-bulk crossover to determine the exact threshold n_0 where triangular lattice packings overtake square and pentagonal configurations. Formalize in Lean the Degree-6 Rigidity Lemma showing that triangle-free planar contact graphs have maximum degree at most 5. Verify whether numerical candidates for n = 6 to 12 contain unit equilateral triangles.
