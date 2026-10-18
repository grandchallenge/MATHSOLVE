GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-593-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-593-A1
assignment: ERDOS-593-A1
disposition: COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

A direct graph-case transfer from “bipartite” to “Property B” fails at the first nontrivial structural level.

Let (F=K_4^{(3)}), the 3-uniform hypergraph on vertices ({1,2,3,4}) whose four hyperedges are all 3-element subsets.

Then:

1. (F) has Property B: a (2+2) vertex coloring has no monochromatic hyperedge.
2. No 2-coloring of (F) gives a fixed graph-like crossing type in which every hyperedge contains exactly one red and two blue vertices.
3. By color-complement symmetry, no 2-coloring gives every hyperedge exactly two red and one blue vertices either.
4. The ordinary 2-shadow of (F) is (K_4), hence non-bipartite.
5. Every vertex link graph of (F) is (K_3), hence non-bipartite.

Therefore Property B does not preserve any of three naive graph analogues:
- a fixed oriented bipartite crossing pattern;
- bipartiteness of the 2-shadow;
- bipartiteness of vertex links.

Any sufficiency proof for the protected conjecture must use the genuinely hypergraphic meaning of 2-colorability, not a reduction to ordinary bipartite graph structure.

## Derivation

Color two vertices red and two blue. Every 3-subset of a four-element set omits exactly one vertex, so each hyperedge contains either one red and two blue vertices or two red and one blue vertices. In particular no edge is monochromatic, proving Property B.

Now suppose there were a red set (Rsubseteq V(F)) such that every 3-edge contained exactly one red vertex. Let (r=|R|). Each hyperedge is (V(F)setminus{v}). Its red count is
[
r-mathbf 1_R(v).
]
If (0<r<4), both values (r) and (r-1) occur as (v) ranges over red and nonred vertices. They cannot both equal (1). The cases (r=0) and (r=4) also fail. Thus no such fixed (1+2) orientation exists. Complementing colors gives the same conclusion for fixed (2+1) orientation.

For the 2-shadow, every pair of vertices lies in some 3-subset of the four vertices, so the shadow contains every pair: it is (K_4).

For a vertex (v), the link graph has the other three vertices, with a link edge (xy) whenever ({v,x,y}) is a hyperedge. Since every such triple is present, the link graph is (K_3).

## Assumptions beyond bootstrap

Only standard definitions:
- Property B means a 2-coloring with no monochromatic hyperedge;
- the 2-shadow contains a graph edge (xy) when some hyperedge contains (x,y);
- the link graph at (v) contains (xy) when ({v,x,y}) is a hyperedge.

No external literature, sibling return, unpublished GCL material, or later repository state was used.

## Verification / falsification hooks

1. Enumerate the four triples of (K_4^{(3)}) under a (2+2) coloring and verify all are bichromatic.
2. For any red-set size (r), compute the red count in edge (Vsetminus{v}) as (r-mathbf1_R(v)); fixed count (1) or fixed count (2) is impossible across all (v).
3. Verify the 2-shadow contains all six vertex pairs.
4. Verify every link contains all three possible edges on its three vertices.

Any proposed graph-transfer lemma asserting
[
	ext{Property B} Longrightarrow
	ext{fixed bipartite crossing type}
]
or
[
	ext{Property B} Longrightarrow
	ext{bipartite shadow/link}
]
is falsified by this example.

## Claim boundary

This is not a counterexample to the protected conjecture “obligatory iff Property B.” It does not show that (K_4^{(3)}) fails to be obligatory.

It instead identifies a precise obstruction to importing the graph proof mechanically: the structural content of graph bipartiteness is much stronger than hypergraph Property B. A graph edge has exactly one endpoint on each side of a bipartition; a 3-edge in a Property-B coloring may have either orientation, and those orientations can be forced to coexist.

## Next residual

For the sufficient direction, a valid analogue of the graph argument must tolerate mixed (1+2) and (2+1) edge types and cannot rely solely on bipartite shadows or bipartite links.

The next safe target is therefore to identify the actual embedding invariant preserved by Property B in 3-uniform hosts of uncountable chromatic number.

For the necessary direction, one still needs a construction or theorem producing high-chromatic (F)-free hosts for non-2-colorable (F); the present counterexample only rules out naive graph-style reductions.