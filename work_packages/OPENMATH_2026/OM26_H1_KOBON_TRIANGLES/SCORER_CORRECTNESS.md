# Independent exact scorer correctness note

The GCL scorer is deliberately independent of the AutoLab/Hills implementation. It uses only the source-locked semantics and Python standard-library exact arithmetic.

For each normalized submitted line, collect every exact pairwise intersection with other nonparallel lines. Sort the distinct vertices on that line by dot product with the exact direction vector `(b,-a)`. Consecutive vertices are exactly the bounded arrangement edges on that line.

The scorer then constructs the undirected planar arrangement graph and counts its nondegenerate 3-cycles.

Why this is the required face count:

1. Every bounded triangular face has three distinct boundary vertices and each side contains no other arrangement vertex. Its three sides are therefore three arrangement-graph edges, so the face gives a graph 3-cycle.
2. Conversely, take a nondegenerate graph 3-cycle. Each side is a consecutive intersection segment on one submitted line. If another submitted infinite line crossed the triangle interior, it would have to leave the bounded triangle again. Unless it coincided with a support line (impossible for distinct normalized lines), that traversal would create an intersection in the interior of at least one cycle edge, contradicting consecutiveness. A line entering through a cycle vertex has the same problem on exit. Thus the cycle interior is not crossed or subdivided.
3. Exact `Fraction` coordinates and determinant tests avoid geometric tolerances. Concurrency and parallelism are admitted naturally; zero-area cycles are rejected.

The baseline fixture is the exact source-reported family `2*i*x - y - i*i = 0` for `i=0,...,17`. Unit tests additionally cover a single triangle, concurrency, a parallel pair, subdivision of an original triangle, proportional-line rejection, and the exact baseline support-triple pattern.

This note establishes the intended logic of the independent scorer. It is not MATHCERT certification and does not make any optimality or novelty claim.
