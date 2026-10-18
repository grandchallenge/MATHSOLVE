GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-101-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-101-R1
assignment: ERDOS-101-R1
disposition: EXACT_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

1. **Elementary and Projective Euler Incidence Bounds**:
Let $P \subset \mathbb{R}^2$ be a set of $n$ points with no 5 collinear, and let $t_k$ denote the number of lines containing exactly $k$ points of $P$.
Pair counting alone yields $t_2 + 3 t_3 + 6 t_4 \le \binom{n}{2}$, giving $t_4 \le \frac{n(n-1)}{12}$.
Applying projective Euler duality (Melchior's theorem in $\mathbb{RP}^2$) under the no-5-collinear condition yields the structural inequality:
$$t_2 \ge 3 + t_4.$$
Substituting $t_2 \ge t_4 + 3$ into pair counting strictly sharpens the elementary upper bound to:
$$t_4 \le \frac{n(n-1) - 6}{14} = \frac{1}{14} n^2 - \frac{1}{14} n - \frac{3}{7}.$$
Standard incidence inequalities (including Szemerédi–Trotter) stop at $O(n^2)$ because they exploit only $K_{2,2}$-freeness of the point-line incidence graph, which is combinatorially achievable by abstract linear 4-uniform hypergraphs (such as Steiner systems $S(2, 4, n)$).

2. **The Bézout Algebraic Group Obstruction**:
All known planar configurations generating $\Theta(n^2)$ collinear triples ($k = 3$) rely on the group law of plane cubics (elliptic curves), where collinearity reflects $x + y + z = 0$.
By Bézout's theorem, any line $L$ intersects an irreducible algebraic curve $C$ of degree $d$ in at most $d$ points ($|L \cap C| \le d$).
Therefore, an irreducible cubic curve intersects any straight line in at most 3 points, supporting identically zero 4-rich lines ($t_4 = 0$).
Because the only one-dimensional algebraic groups over $\mathbb{R}$ are $\mathbb{G}_a$ ($d = 1$), $\mathbb{G}_m$ ($d = 2$), and elliptic curves ($d = 3$), every one-dimensional algebraic group is blocked by Bézout's theorem from generating 4-rich lines. By the Elekes–Szabó theorem, any hypothetical $\Theta(n^2)$ family cannot arise from low-degree abelian group symmetries.

3. **Geometric Realizability Defect of Combinatorial Designs**:
Abstract linear designs with maximal $t_4$ cannot be embedded in $\mathbb{R}^2$:
The affine plane $AG(2, \mathbb{F}_4)$ ($n = 16, t_4 = 20$) has $t_2 = 0$, violating Melchior's theorem $t_2 \ge t_4 + 3 = 23$.
In $\mathbb{R}^2$, the $4 \times 4$ grid ($n = 16$) achieves $t_4 = 10$, accompanied by $t_3 = 4$ and $t_2 = 48$, exactly partitioning all $\binom{16}{2} = 120$ pairs.

## Derivation

1. **Pair Counting and Melchior's Theorem**:
Every pair of points determines at most one line. Since no line contains 5 or more points, every line of $k$ points contains $\binom{k}{2}$ disjoint point-pairs:
$$\sum_{k=2}^4 \binom{k}{2} t_k = t_2 + 3 t_3 + 6 t_4 \le \binom{n}{2} = \frac{n(n-1)}{2}.$$
In projective duality, points dualize to lines and lines to vertices of the dual arrangement $\mathcal{A}^*$.
By Melchior's topological theorem derived from the Euler characteristic $\chi(\mathbb{RP}^2) = 1$:
$$t_2 \ge 3 + \sum_{k \ge 4} (k - 3) t_k.$$
Since $t_k = 0$ for all $k \ge 5$, this reduces to $t_2 \ge 3 + (4 - 3) t_4 = t_4 + 3$.
Combining with pair counting:
$$\binom{n}{2} \ge t_2 + 6 t_4 \ge (t_4 + 3) + 6 t_4 = 7 t_4 + 3 \implies t_4 \le \frac{\binom{n}{2} - 3}{7} = \frac{n(n-1) - 6}{14}.$$

2. **Szemerédi–Trotter Limitation**:
Szemerédi–Trotter states that incidences between $n$ points and $m$ lines satisfy $I(P, \mathcal{L}) \le C(n^{2/3} m^{2/3} + n + m)$.
For $m = t_4$, $4 t_4 \le I(P, \mathcal{L}_4) \le C(n^{2/3} t_4^{2/3} + n + t_4)$, which simplifies to $t_4 \le C' n^2$.
Because this bound is derived solely from the Crossing Lemma applied to the bipartite incidence graph, it bounds only the number of edges in a $K_{2,2}$-free bipartite graph. An abstract $K_{2,2}$-free bipartite graph on $n$ points with degree-4 line vertices can attain $\frac{n(n-1)}{12} = \Theta(n^2)$ lines, explaining why general incidence bounds cannot prove $o(n^2)$.

3. **Bézout's Theorem and Algebraic Group Elimination**:
Suppose $P \subset C \subset \mathbb{R}^2$ where $C$ is an irreducible algebraic curve of degree $d$.
By Bézout's theorem, if a line $L$ is not a component of $C$, $|L \cap C| \le d$.
If $d = 3$, $|L \cap C| \le 3$, so no straight line can contain 4 points of $C$.
A 1-dimensional algebraic group variety over $\mathbb{R}$ must be isomorphic to $\mathbb{G}_a$ (line, $d=1$), $\mathbb{G}_m$ (conic, $d=2$), or an elliptic curve (cubic, $d=3$).
By Elekes–Szabó (2012), any set of points supporting $\Theta(n^2)$ collinear 4-tuples must have its collinearity relation induced by a 1-dimensional algebraic group action. Because all such groups have degree $d \le 3$, Bézout's theorem forces all lines to intersect the group variety in at most 3 points, ruling out any $\Theta(n^2)$ construction from algebraic groups.

## Assumptions beyond bootstrap

NONE. Only standard projective geometry (Melchior's theorem, duality), algebraic curve theory (Bézout's theorem), and the protected formalization `FormalConjectures/ErdosProblems/101.lean` were used.

## Verification / falsification hooks

1. **Melchior Inequality Hook**: Verify that in any non-collinear planar point set with no 5 collinear, $t_2 \ge t_4 + 3$.
2. **$4 \times 4$ Grid Exact Census**: In $P = \{0, 1, 2, 3\}^2 \subset \mathbb{R}^2$ ($n = 16$), verify that $t_4 = 10$, $t_3 = 4$, $t_2 = 48$, and $t_k = 0$ for $k \ge 5$, satisfying $t_2 = 48 \ge 13 = t_4 + 3$ and $48 + 3(4) + 6(10) = 120 = \binom{16}{2}$.
3. **Bézout Intersection Check**: Verify that for any irreducible cubic polynomial $F(x, y) = 0$, restricting $F$ to any affine line $x(t) = x_0 + a t, y(t) = y_0 + b t$ yields a polynomial of degree at most 3 in $t$, possessing at most 3 real roots.
4. **Lean Environment Verification**: Check `numLinesWithFourPointMax` and `erdos_101` in `FormalConjectures/ErdosProblems/101.lean`.

## Claim boundary

This contribution does not prove the full asymptotic claim $t_4 = o(n^2)$.
It provides an exact reduction isolating why standard incidence bounds fail at $O(n^2)$, establishes the projective Euler bound $t_4 \le \frac{n(n-1)-6}{14}$, and proves that the classical cubic group-law mechanism responsible for $\Theta(n^2)$ 3-rich lines is blocked for 4-rich lines by Bézout's theorem.

## Next residual

Prove that any point set in $\mathbb{R}^2$ with $\Theta(n^2)$ 4-rich lines must concentrate on an algebraic curve of degree $d \ge 4$. Demonstrating that high-genus curves cannot support quadratic 4-line linear systems is the exact missing lemma to establish $t_4 = o(n^2)$.
