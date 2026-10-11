# Erdős 241/595 — exact next barriers, not proposed solutions

STATUS: RESEARCH_HYPOTHESES_AND_FALSIFICATION_RECEIPT
SOURCE_LOCK: MATH-PROGRAMME #2509 and #2511, plus existing protected MATHSOLVE replay 002
MATH_CLAIM_AUTHORITY: NONE
LEAN_FORMALIZATION: SEPARATE_LOCAL_INTERFACES_ONLY
MATHCERT_OR_NEW_EXECUTION: NONE

## Erdős 241: exact triple-energy bridge to the missing analytic inequality

Let A be a finite strong B₃ subset of the integers with k elements:
all sums of unordered triples with repetition are distinct. Let

    r₃(s)=#{(a,b,c)∈A³ : a+b+c=s}.

A triple with all entries identical has one ordering; there are k of
these. A triple with exactly two equal entries has three orderings;
there are k(k−1) such multisets. A triple with three distinct entries
has six orderings; there are C(k,3) such multisets.

By B₃ uniqueness these orbit contributions occur at distinct s.
Therefore the following **exact integer identity** holds, with no
asymptotic assumption:

    Σ_s r₃(s)² = k + 9 k(k−1) + 36 C(k,3)
                = 6k³ − 9k² + 4k.

Also Σ_s r₃(s)=k³ and |supp(r₃)|=C(k+2,3).
Orthogonality of characters gives the exact Fourier sixth-moment identity

    ∫₀¹ |Σ_{a∈A} exp(2π i a t)|⁶ dt = 6k³−9k²+4k.

This is a rigorous entry point to the continuous autoconvolution
methods of Green and White. The polynomial identity alone does not
improve the best asymptotic B₃ upper bound, which involves
nontrivial information about geometry/distribution of triples.

**Explicit false approach.** There is no guarantee of a cyclic
embedding with safe modulus at most N for every B₃ subset of [1,N].
A={1,2,6}⊆[1,6] is strong B₃ with unordered sums
{3,4,5,6,8,9,10,13,14,18}. Every modulus M≤15 creates at least
one collision; M=16 is the FIRST safe modulus. The safe-modulus
search cannot solve the upper bound by assuming M=O(N) with an
unjustifiably small universal coefficient. All assertions are checked
by the committed exact-integer script.

**Next precise mathematical attack.** Express the White/Green
continuous L² convolution inequality with exactly matching
normalization and quantify how near-B₃ equality constrains
concentration of the empirical measure of a scaled strong-B₃ set.
The target is an explicit additional concentration/stability
inequality beyond the known autoconvolution bound, with a
counterexample generator for false proposed inequalities.
No claim is made that this step has been completed, and the original
question f(N)~N^{1/3} remains open.

## Erdős 595: isolate the invariant that actually matters

The previous proof shows that for finite G the minimum number of
BIPARTITE edge-cover layers is ceil(log₂ χ(G)).
This exact quantity is **not** the minimum count of TRIANGLE-FREE
edge-cover layers: already C₅ has chromatic number three (there is no
2-colouring but the cyclic vertex colouring 0,1,2,0,1 works), so it
needs two bipartite layers, while it is itself triangle-free and needs
only one triangle-free layer.

Thus high vertex chromatic number is not sufficient to force
large triangle-free cover number. This blocks any attempted proof
of the original problem relying on a converse to the bit-code
construction.

A direct reduction instead colours the vertices of the *triangle
hypergraph*: its vertices are the edges of G, and each graph triangle
provides a 3-uniform hyperedge. Countable triangle-free covering of G
is equivalent to a proper countable vertex colouring of this
triangle hypergraph. The K₄-free constraint restricts which
triangle hypergraphs can arise, and that **representability/
coherence restriction** (not the bare vertex chromatic number) is
the target for a future ZFC argument.

Before claiming novelty, independently review prior relevant Lean
material and source semantics:
https://github.com/jaredwilder/erdos595-barrier-tower
The external author records 27 Lean theorem files, including
overlapping continuum/chromatic and hypergraph facts. Their
claimed kernel status is not a GCL independent replay. Do not
rebuild those statements as if first discovered.

**Exact next falsifiable attack.** Search for a K₄-free triangle
hypergraph coherence constraint that forces a countable vertex
colouring in ZFC, or construct a genuine K₄-free hypergraph
representation defeating all such colourings. Test candidate
finite obstructions against odd cycles and Folkman-type graphs;
separate actual ZFC implications from consistency results based
on additional axioms. No assertion resolving the problem is
made by this document.

## Replay and authority boundary

Run from repository root:

    python ci/erdos_catalogue_local_certificates.py --check

The new tests verify the exact energy identity over every strong B₃
subset of [1,N] for N=2,...,10; check the first safe modulus
of A={1,2,6}; and use exhaustive two-colouring plus a three-colour
witness to establish C₅'s elementary gap. This is standard-library
integer checking; not an independent formal proof of the infinite
cardinal or asymptotic assertions. The protected Lean interfaces
reside separately in MathSolve/Erdos/LocalInterfaces.lean.

No SOURCE_ACCEPTED, mathematical certification, original Erdős
solution, external agent independence, or executable successor
is inferred.
