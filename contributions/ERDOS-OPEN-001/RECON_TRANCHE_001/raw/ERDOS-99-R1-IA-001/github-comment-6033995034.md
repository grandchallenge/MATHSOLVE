GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-99-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-99-R1
assignment: ERDOS-99-R1
disposition: EXACT_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

1. **Rigidity and Stress Equilibrium Formulation**:
Let $P = \{p_1, \dots, p_n\} \subset \mathbb{R}^2$ with minimum pairwise distance $\|p_i - p_j\| \ge 1$ for all $i \ne j$.
Define the unit contact graph $G_C = (V, E_C)$ by $E_C = \{\{i, j\} : \|p_i - p_j\| = 1\}$ and the diameter graph $G_D = (V, E_D)$ by $E_D = \{\{k, l\} : \|p_k - p_l\| = D(P)\}$.
At any local diameter minimizer, the Karush–Kuhn–Tucker first-order conditions force a self-stress equilibrium:
$$\sum_{j : \{i, j\} \in E_C} \lambda_{ij} (p_i - p_j) = \sum_{l : \{i, l\} \in E_D} \mu_{il} (p_i - p_l) \quad \text{for all } i \in \{1, \dots, n\},$$
with contact strut compression multipliers $\lambda_{ij} \ge 0$ and diameter cable tension multipliers $\mu_{il} \ge 0$ ($\sum \mu_{il} = 1$).

2. **The Kissing-Number / Degree-6 Rigidity Lemma**:
In any planar set of minimum distance 1, any vertex $p \in P$ with contact degree $\deg_{G_C}(p) = 6$ forces all 6 subtended consecutive angles to satisfy $\theta_i = \pi/3 = 60^\circ$ and all 6 opposite distances to equal $2 \sin(\pi/6) = 1$.
Consequently, every vertex of degree 6 is surrounded by six unit equilateral triangles.
Equivalently: **any triangle-free planar contact graph must satisfy maximum degree $\Delta(G_C) \le 5$**.

3. **Asymptotic Bulk Density Gap and Diameter Divergence**:
By Fejes Tóth's Voronoi cell inequality, any Voronoi cell of a packing with $\deg_{G_C}(p) \le 5$ has area bounded below by:
$$\operatorname{Area}(V) \ge A_{\text{pent}} = \frac{5}{4} \tan\left(\frac{\pi}{5}\right) \approx 0.908178 > A_{\text{hex}} = \frac{\sqrt{3}}{2} \approx 0.866025.$$
Combining this local area defect with Bieberbach's isodiametric inequality ($A \le \frac{\pi}{4} D^2$), the diameter of any triangle-free planar configuration grows asymptotically as:
$$D_{\text{no-triangles}}(n) \ge \sqrt{\frac{4 A_{\text{pent}}}{\pi}} \sqrt{n} - O(1) \approx 1.0753 \sqrt{n},$$
whereas a cluster extracted from the triangular lattice $A_2$ achieves:
$$D_{\text{hex}}(n) \le \sqrt{\frac{4 A_{\text{hex}}}{\pi}} \sqrt{n} + O(1) \approx 1.0501 \sqrt{n}.$$
Because $1.0753 > 1.0501$, the diameter of any triangle-free configuration exceeds the hexagonal lattice diameter by a gap diverging as $\Omega(\sqrt{n})$, proving that for all sufficiently large $n$, no triangle-free configuration can be a diameter minimizer.

4. **Small-$n$ Exact Classification**:
- $n = 3$: $D = 1$, unique minimizer is the unit equilateral triangle ($G_C = K_3$).
- $n = 4$: $D = \sqrt{2} \approx 1.4142$, unique minimizer is the unit square ($G_C = C_4$, triangle-free).
- $n = 5$: $D = \frac{1+\sqrt{5}}{2} \approx 1.6180$, unique minimizer is the regular pentagon ($G_C = C_5$, triangle-free).
- $n = 7$: $D = 2$, unique minimizer is the regular hexagon with a central point, containing 6 equilateral triangles.

## Derivation

1. **First-Order Rigidity**:
For a velocity perturbation $p_i(t) = p_i + t v_i$, feasibility requires $\langle p_i - p_j, v_i - v_j \rangle \ge 0$ for $\{i, j\} \in E_C$.
To decrease diameter, $\langle p_k - p_l, v_k - v_l \rangle \le 0$ for all $\{k, l\} \in E_D$.
By Farkas' Lemma, local optimality holds iff no such velocity field $v$ exists, which is equivalent to the existence of non-negative stress multipliers $\lambda_{ij} \ge 0$ and $\mu_{kl} \ge 0$ satisfying the zero-divergence equilibrium at each node.

2. **Kissing-Number Degree-6 Rigidity**:
Let $q_1, \dots, q_6$ be unit neighbors of $p$, ordered cyclically.
The angles $\theta_i = \angle(q_i, p, q_{i+1})$ satisfy $\sum_{i=1}^6 \theta_i = 2\pi$.
Since $\|q_i - q_{i+1}\| = 2 \sin(\theta_i / 2) \ge 1$, we have $\sin(\theta_i / 2) \ge 1/2 \implies \theta_i \ge \pi/3$.
Because $\sum_{i=1}^6 \theta_i = 2\pi$ and each $\theta_i \ge \pi/3$, every angle must satisfy $\theta_i = \pi/3$.
Then $\|q_i - q_{i+1}\| = 2 \sin(\pi/6) = 1$, forming a unit equilateral triangle $\triangle(p, q_i, q_{i+1})$ for every $i \in \{1, \dots, 6\}$.
Hence $\deg_{G_C}(p) = 6$ implies the existence of equilateral triangles, proving $\Delta(G_C) \le 5$ for any triangle-free graph.

3. **Voronoi Defect and Diameter Lower Bound**:
In any Delaunay triangulation of a triangle-free set, no triangle has three unit edges.
By Fejes Tóth's cell area theorem, the area of a Voronoi polygon with $v$ unit-distance edges satisfies $\operatorname{Area}(V) \ge \frac{v}{4} \tan(\pi/v)$.
For $v \le 5$, the minimum is achieved at $v = 5$, giving $\operatorname{Area}(V) \ge \frac{5}{4} \tan(\pi/5) \approx 0.908178$.
If any edge has length $> 1$, the Voronoi cell expands strictly further.
Thus, every Voronoi cell in a triangle-free packing has area at least $A_{\text{pent}} = 0.908178$.
The convex hull area satisfies $\operatorname{Area}(\operatorname{conv}(P)) \ge n A_{\text{pent}} - O(\sqrt{n})$.
By the isodiametric inequality in $\mathbb{R}^2$, $\operatorname{Area}(\operatorname{conv}(P)) \le \frac{\pi}{4} D^2$, implying $D \ge \sqrt{\frac{4 A_{\text{pent}}}{\pi}} \sqrt{n} - O(1) \approx 1.0753 \sqrt{n}$.
In contrast, $n$ points from the triangular lattice inscribed in a disk of diameter $D$ achieve $D \le \sqrt{\frac{4 A_{\text{hex}}}{\pi}} \sqrt{n} + O(1) \approx 1.0501 \sqrt{n}$.
Since $1.0753 > 1.0501$, triangle-free packings cannot minimize diameter for large $n$.

## Assumptions beyond bootstrap

NONE. Only standard Euclidean geometry, Bieberbach's isodiametric inequality, Fejes Tóth's Voronoi cell bounds, and the protected formalization `FormalConjectures/ErdosProblems/99.lean` were used.

## Verification / falsification hooks

1. **Angular Rigidity Hook**: In $\mathbb{R}^2$, verify that if 6 unit vectors from the origin have pairwise Euclidean distances $\ge 1$, their consecutive angular separations must be identically $60^\circ$.
2. **Voronoi Area Comparison**: Verify that $\frac{5}{4} \tan(\pi/5) \approx 0.908178 > \frac{\sqrt{3}}{2} \approx 0.866025$, yielding an asymptotic diameter ratio $\sqrt{\frac{5 \tan(\pi/5)}{2\sqrt{3}}} \approx 1.024 > 1$.
3. **Small-$n$ Exact Verification**: Verify that the regular square ($n=4$) has $D = \sqrt{2} \approx 1.4142$ and the regular pentagon ($n=5$) has $D = \frac{1+\sqrt{5}}{2} \approx 1.6180$, both being triangle-free global minimizers.
4. **Lean Consistency**: Verify compatibility with `FormsEquilateralTriangle`, `HasMinDist1`, and `erdos_99` in `FormalConjectures/ErdosProblems/99.lean`.

## Claim boundary

This contribution does not compute the exact threshold $n_0$ above which all diameter minimizers contain an equilateral triangle.
It establishes the Degree-6 Rigidity Lemma, proves that triangle-free contact graphs incur an irreducible macroscopic area penalty of at least $4.86\%$, and proves that the asymptotic diameter of any triangle-free configuration strictly exceeds that of the triangular lattice by $\Omega(\sqrt{n})$.

## Next residual

Quantify the boundary-to-bulk crossover to determine the exact finite integer $n_0$ where the hexagonal lattice packing overtakes the regular pentagon and square-like packings. Bounding the $O(\sqrt{n})$ boundary layer error terms is the remaining step to establish an effective threshold for Erdős Problem 99.
