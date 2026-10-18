GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-593-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-593-R1
assignment: ERDOS-593-R1
disposition: EXACT_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

The first genuine finite obstruction to Property B occurs on five vertices, and
there it is unique.

Let F be a 3-uniform hypergraph.

1. If |V(F)| <= 4, then F is 2-colorable.
2. If |V(F)| = 5, then F is not 2-colorable if and only if F is the complete
   3-uniform hypergraph K_5^(3), i.e. every 3-subset of its five vertices is an
   edge.

Hence the necessary implication
    IsObligatory F -> F.IsTwoColorable
has no nontrivial counterexample to exclude below five vertices. At the first
possible vertex size it reduces exactly to one construction problem:

    construct a 3-uniform H with
        aleph_0 < H.chromaticCardinal
    and
        K_5^(3) does not appear in H.

Such an H proves that K_5^(3) is not obligatory. By the protected monotonicity
of obligatory appearance, the same H also proves non-obligatoriness for every
finite F in which K_5^(3) appears: if F appeared in H, composition with the
K_5^(3) embedding into F would make K_5^(3) appear in H.

A clean stronger construction principle is sufficient:

    There exists a linear 3-uniform H of chromatic cardinal > aleph_0,

where linear means any two distinct hyperedges intersect in at most one vertex.
Any such H is automatically K_5^(3)-free, because K_5^(3) contains distinct
edges sharing two vertices.

Thus, for the first nontrivial finite obstruction, the smallest exact missing
lemma is the existence of an uncountably chromatic K_5^(3)-free 3-uniform
hypergraph; an uncountably chromatic linear 3-uniform hypergraph is a simple
stronger sufficient lemma.

## Derivation

For |V| <= 4, partition the vertices into two color classes of size at most 2.
No 3-element hyperedge can be monochromatic, so this is a proper 2-coloring.
This argument works for every possible edge set.

Now suppose |V| = 5.

If some 3-subset S is not an edge, color the three vertices of S with color 0
and the two vertices of V\S with color 1. A monochromatic edge cannot lie in
the 2-element color class. The only possible 3-element monochromatic set in
the other class is S itself, which by assumption is not an edge. Therefore F
is 2-colorable.

Conversely, if every 3-subset is an edge, any 2-coloring of five vertices has
a color class of size at least 3. Any three vertices from that color class form
an edge, hence a monochromatic edge. Therefore the complete K_5^(3) is not
2-colorable.

This proves uniqueness of the five-vertex non-Property-B obstruction.

The protected definition of IsObligatory says exactly that F appears in every
3-uniform H with chromatic cardinal > aleph_0. Therefore, for any fixed
non-2-colorable F, the necessary direction is discharged by a single F-free
host of chromatic cardinal > aleph_0. For the first obstruction this is the
K_5^(3)-free host statement above.

For the structural sufficient condition, a linear H cannot contain K_5^(3):
in K_5^(3), for example, the edges {1,2,3} and {1,2,4} are distinct and
intersect in two vertices. Injective appearance preserves that intersection
pattern, contradicting linearity.

Finally, if K_5^(3) appears in F and F were obligatory, then the protected
obligatory_monotone theorem would imply K_5^(3) obligatory. Equivalently, any
uncountably chromatic K_5^(3)-free host simultaneously excludes every such F.

## Assumptions beyond bootstrap

NONE. Only the protected definitions of Appears, IsTwoColorable,
chromaticCardinal, IsObligatory, the protected obligatory-monotonicity theorem,
and elementary finite combinatorics were used.

## Verification / falsification hooks

1. On 4 vertices, explicitly color any two vertices 0 and the remaining at
   most two vertices 1; no 3-edge is monochromatic.

2. On 5 vertices, verify the equivalence:
       F is 2-colorable
       iff some 3-subset is missing from F.edges.
   The forward contraposition is the pigeonhole argument; the reverse is the
   3+2 coloring constructed above.

3. In K_5^(3), inspect the two edges {1,2,3} and {1,2,4}. Their intersection
   has size 2, so no injective copy can occur in a linear 3-uniform host.

4. Check the protected snapshot
   google-deepmind/formal-conjectures@85f863718beeec7b58a3a1926ee92e3472bc2020:
   FormalConjecturesForMathlib/Combinatorics/Hypergraph/ThreeUniform.lean for
   Appears, IsTwoColorable, chromaticCardinal, IsObligatory; and
   FormalConjectures/ErdosProblems/593.lean for obligatory_monotone.

## Claim boundary

This does not construct the required uncountably chromatic K_5^(3)-free host
and does not prove the full necessary direction of Erdős Problem 593. It gives
an exact finite classification through the first non-2-colorable vertex size
and isolates the first genuine construction lemma. It also settles, conditional
on that host lemma, every finite F containing K_5^(3).

## Next residual

Prove the host lemma:
    exists H, aleph_0 < H.chromaticCardinal and K_5^(3) does not appear in H.
A stronger but structurally clean target is to construct an uncountably
chromatic linear 3-uniform hypergraph. If that succeeds, the first obstruction
and every finite F containing it are discharged at once.