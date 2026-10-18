# H1-12 partial reduction — eliminate parallelism without losing counted faces

**State:** `SOLVE_PROOF_COMPLETE__CONCURRENCE_REMAINS_OPEN`

## Theorem

Let `A` be a finite arrangement of distinct affine straight lines and let `F` be any finite collection of bounded triangular faces counted by the Kobon hill. There exists a projectively equivalent affine line arrangement `A'` such that:

1. no two lines of `A'` are parallel; and
2. every face in `F` maps to a bounded triangular face of `A'`.

Therefore, for upper-bound purposes, the hill's allowance of parallel lines can be removed without decreasing the number of counted triangular faces. The only remaining degeneracy relevant to H1-12 is multiple concurrence.

## Proof

Take the projective completion of the original affine plane. The closure of the union of all faces in `F` is a compact subset of the original affine chart.

Choose an ordinary affine line `M` satisfying all of the following:

- `M` is disjoint from the closed union of the faces in `F`;
- `M` passes through no finite intersection point of two arrangement lines;
- the direction of `M` is different from every direction occurring among the arrangement lines.

Such an `M` exists. There are only finitely many forbidden directions and finitely many finite arrangement vertices. First choose a non-forbidden direction. Then translate a line of that direction sufficiently far from the compact union of the selected faces and, if necessary, avoid the finitely many forbidden translates through arrangement vertices.

In the projective completion, the last condition also means that the point of `M` at the old line at infinity is not any intersection point of a parallel pair of arrangement lines. Hence `M` contains no projective intersection point of any pair of arrangement lines.

Now choose a projective automorphism sending `M` to the new line at infinity. Every arrangement line remains a projective line distinct from `M`, hence becomes an affine line in the new chart. Because every pairwise projective intersection lies off `M`, every pair of transformed arrangement lines intersects at a finite point. Thus `A'` has no parallel pairs.

Each closed triangular face in `F` is disjoint from `M`. Its projective image is therefore contained in the new affine chart and remains compact, hence bounded. Projective transformations preserve incidence, line segments as projective arcs inside the chosen chart, and whether another arrangement line crosses the open face. Thus each selected counted triangular face remains a counted bounded triangular face.

This proves the theorem.

## Consequence for H1-12

A hill-global upper bound need only handle arrangements in which every pair of lines intersects finitely. Parallelism is not a separate obstruction.

However, projective transformations preserve incidence multiplicity. Triple and higher-order concurrence cannot be removed by this argument. The simple-arrangement 94 theorem therefore still does **not** transfer automatically: H1-12 is narrowed to the question of whether multiple-concurrence arrangements at `n=18` can exceed 94, or whether their triangle count can be bounded by 94 directly.

## Claim boundary

This is a Solve-level reduction theorem, not a MATHCERT disposition. It does not prove the hill-global upper bound 94, does not exclude a 95-triangle concurrent arrangement, and does not certify optimality of the 93 construction.
