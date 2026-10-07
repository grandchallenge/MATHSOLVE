GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-99-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-99-A1
assignment: ERDOS-99-A1
disposition: COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

The heuristic that a global diameter minimizer forces a unit equilateral triangle is false even for an exact global minimizer.

Take the four vertices of a unit square. Its minimum pairwise distance is 1, its diameter is sqrt(2), and its unit-distance contact graph is exactly the cycle C_4, hence triangle-free. Nevertheless sqrt(2) is the globally minimal possible diameter for four planar points whose pairwise distances are all at least 1.

Thus an exact global diameter minimizer can have no unit equilateral triangle at all. Any proof of the protected eventual statement must therefore use genuinely large-n structure; global optimality, contact-graph activity, local rigidity heuristics, uniqueness, or genericity cannot by themselves force the desired triangle.

## Derivation

It remains only to prove the lower bound D >= sqrt(2) for any four planar points with minimum pairwise distance 1.

Assume for contradiction that four planar points have every pairwise distance in [1, sqrt(2)). Then every triangle determined by three of the four points is acute. Indeed, for any such triangle and any side c opposite an angle gamma, the two adjacent sides a,b satisfy a, b >= 1, while c < sqrt(2). Hence c^2 < 2 <= a^2 + b^2. By the law of cosines this gives gamma < 90 degrees. Since the choice of side was arbitrary, all three angles are acute.

But no set of four planar points has every three-point triangle acute:

1. If three points are collinear, a triple already has an angle of 180 degrees.
2. If one point lies inside the triangle formed by the other three, the three rays from the interior point to the vertices divide 360 degrees into three angles, so at least one is at least 120 degrees; the corresponding three-point triangle is not acute.
3. Otherwise the four points are the vertices of a convex quadrilateral. Its four interior angles sum to 360 degrees, so at least one is at least 90 degrees; three consecutive vertices then form a triangle with a nonacute angle.

Contradiction. Therefore every four-point planar set with minimum distance 1 has diameter at least sqrt(2).

The unit square attains this bound: four side distances are 1, and the two diagonals are sqrt(2). Hence it is a global diameter minimizer.

Its only unit-distance pairs are the four sides, so its contact graph is C_4. In particular there is no triple of points with all three mutual distances 1, hence no unit equilateral triangle.

## Assumptions beyond bootstrap

Only elementary Euclidean geometry and the protected normalization of minimum pairwise distance 1.

No external literature, sibling return, unpublished project material, or later repository state was used.

## Verification / falsification hooks

1. Check directly that the unit square has pairwise distance multiset {1, 1, 1, 1, sqrt(2), sqrt(2)}.
2. Verify the lower-bound lemma: if all six distances of four planar points lie in [1, sqrt(2)), every three-point triangle is acute by c^2 < a^2 + b^2.
3. Verify the elementary four-point dichotomy: collinear triple, one point inside the triangle of the others, or convex quadrilateral.
4. In the interior-point case, one angle at the interior point is at least 120 degrees.
5. In the convex-quadrilateral case, one interior angle is at least 90 degrees.

Any proposed criterion that derives a unit equilateral triangle solely from global diameter minimality with minimum distance 1 is falsified by the square.

## Claim boundary

This does not refute Erdős problem 99, because the protected statement is eventual in n: it asks only for all sufficiently large n.

The result instead eliminates a proof heuristic. Small-n global optimality can coexist with a triangle-free contact graph, so a successful proof must identify a mechanism that appears only after n becomes large.

It also shows that one cannot silently assume genericity or uniqueness: the square is highly symmetric and nongeneric, yet globally optimal.

## Next residual

Successor routes must identify an asymptotic property P_n forced for all sufficiently large diameter-minimizing configurations that guarantees a triangle in the unit-distance graph. Packing density, boundary-versus-interior structure, or global extremal constraints are required because local optimality and finite diameter minimality alone cannot prevent triangle-free contact graphs.
