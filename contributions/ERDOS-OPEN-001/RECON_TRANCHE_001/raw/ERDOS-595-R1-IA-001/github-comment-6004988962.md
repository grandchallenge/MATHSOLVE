GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-595-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-595-R1
assignment: ERDOS-595-R1
disposition: COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

The finite Folkman-type statement for every fixed n does NOT pass to the
countable-cover target by ordinary compactness, even if all finite witnesses
are assembled coherently into one K4-free graph.

Let F_n (n >= 1) be finite K4-free graphs such that F_n is not the union of n
triangle-free graphs, as supplied by the protected finite variant. Form the
countable disjoint union

    D = disjoint_union_{n>=1} F_n.

Then:

1. D is K4-free.
2. For every finite n >= 1, D is not the union of n triangle-free graphs.
3. D IS the union of countably many triangle-free graphs.

Thus the implication

    "for every finite n, G is not n-coverable by triangle-free graphs"
        =>
    "G is not countably coverable by triangle-free graphs"

is false, including for a single K4-free host containing all finite
obstructions.

Equivalently, under the protected edge-colouring reformulation, the finite
theorem produces triangle-hypergraphs of arbitrarily large finite chromatic
number. The target requires uncountable chromatic number. The disjoint-union
construction has chromatic number exactly at the countable scale: it is not
finitely colourable, but it is countably colourable.

A sufficient finite-to-infinite bridge requires an additional
colouring-capture/coherence property, not merely nestedness or embeddings.
One clean schema is:

Let G be K4-free and let F_n <= G be finite subgraphs with F_n not n-coverable.
Assume that for every edge colouring c : E(G) -> Nat there exists n such that
c uses at most n distinct colours on E(F_n). Then G is not a countable union
of triangle-free graphs.

Indeed, if c had no monochromatic triangle, its restriction to F_n would
partition E(F_n) into at most n triangle-free colour classes, contradicting
the defining property of F_n.

The missing ingredient is therefore not ordinary finite compactness. It is a
global anti-diagonal property forcing every countable colouring to be captured
on some finite obstruction with fewer colours than that obstruction requires.

## Derivation

Use the protected equivalence:
G is a countable union of triangle-free graphs iff its edges admit a colouring
by Nat with no monochromatic triangle.

For each n >= 1 choose a protected finite witness F_n. Take their vertex-
disjoint union D.

K4-free: every clique of D lies entirely inside one connected component, hence
inside some F_n; each F_n is K4-free.

No fixed finite cover: suppose D were the union of n triangle-free graphs.
Restrict those n graphs to the component F_n. Each restriction remains
triangle-free, and their union covers F_n. This contradicts the choice of F_n.
This is also an immediate application of the protected subgraph monotonicity
lemma.

Countable cover: D has only countably many edges, because it is a countable
union of finite edge sets. Enumerate E(D) as e_0,e_1,... (repeating nothing;
use empty graphs after the enumeration if E(D) is finite). Let H_i be the
single-edge graph containing e_i. Every H_i is triangle-free and
D = sup_i H_i. Hence D is a countable union of triangle-free graphs.

This gives an explicit countermodel to the proposed finite-to-countable
compactness step.

The same obstruction survives stronger-looking compatibility. If the F_n are
embedded into a common countable K4-free host, or arranged as an omega-chain
of finite graphs whose union is countable, the resulting graph still has
countably many edges and is therefore automatically a countable union of
single-edge triangle-free graphs. Thus nestedness, embeddings, and ordinary
omega-directed coherence alone are insufficient.

For the sufficient schema, suppose c : E(G) -> Nat has no monochromatic
triangle. By the colouring-capture hypothesis choose n for which at most n
colours occur on F_n. For each occurring colour, take the corresponding colour
class subgraph of F_n, padding with empty graphs to obtain n pieces. Every
piece is triangle-free because c has no monochromatic triangle. Their union is
F_n, contradicting that F_n is not n-coverable.

## Assumptions beyond bootstrap

NONE. Only the protected finite theorem, protected subgraph monotonicity,
protected edge-colouring reformulation, and elementary finite/countable set
arguments were used.

## Verification / falsification hooks

1. Check the protected snapshot
   google-deepmind/formal-conjectures@85f863718beeec7b58a3a1926ee92e3472bc2020,
   FormalConjectures/ErdosProblems/595.lean:
   - erdos_595.variants.folkman_finite;
   - erdos_595.variants.subgraph_of_countable_union;
   - erdos_595.variants.reformulation_edge_colouring.

2. Given any finite witness list F_1,...,F_N, the finite disjoint union already
   verifies the restriction argument for all n <= N. The countable construction
   is the direct limit of this exact operation.

3. To falsify the countable-cover claim for D, it would suffice to show that a
   countable edge set cannot be enumerated into single-edge subgraphs. This is
   impossible by the definition of countability.

4. To falsify the sufficient bridge, exhibit a no-monochromatic-triangle
   colouring c and an n satisfying the capture hypothesis while F_n remains
   non-n-coverable. Restricting c to F_n immediately constructs the prohibited
   n-cover.

## Claim boundary

This does not solve Erdős Problem 595 and does not establish the required
uncountable K4-free graph. It refutes the direct compactness route from the
protected finite theorem, shows that even a common countable host or omega-chain
of finite witnesses is insufficient, and isolates an exact additional
colouring-capture property that would make the bridge valid.

## Next residual

Construct, or rule out, an uncountable K4-free host carrying finite
high-cover-number subgraphs with a genuine colouring-capture property:
every Nat-colouring of its edges must restrict to some finite obstruction
using no more colours than that obstruction forbids. Bare finite witnesses,
nestedness, and ordinary compactness do not provide this property.