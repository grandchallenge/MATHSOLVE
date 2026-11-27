# SCC-001: support incidence and strict nonminimum compression

Status: exploratory author-derived propositions and exact finite computer-assisted counterexample, not Lean-certified, independently adjudicated or novelty-certified. Continues [coherent matching](COHERENT_MATCHING.md) and [marked graph capacity](MARKED_GRAPH_CAPACITY.md), protected base e24feab62c7b86851b1d1ed157c40b2292494359. No extra computational outputs or restriction on nonlinear reuse.

## 1. Exact atom membership by feature closure

Let W be the available feature space on the augmented cube, including constant 1 and marker y. Choose a basis with constant 1; write R(p) for its evaluation row at augmented point p. For a nonempty point subset S, define cl_W(S) as the set of p whose row belongs to span R(S). The constant coordinate makes this equivalent to affine closure of the nonconstant feature rows. S is an atom support iff cl_W(S)=S. An atom is a conjunction of available affine equations, so every point in this row-span closure satisfies them. Conversely the common zeros of the annihilator of span R(S) are exactly its row span by finite-dimensional duality; multiply the complemented linear forms to obtain its indicator. Empty support is the zero atom. This is an independent membership test by elimination, polynomial in explicitly supplied truth-table size, not necessarily in input bit count n.

Append the evaluation bit g of a legal gate to each row. Write U=span R(S), U' for the lifted span. Projection U' to U is surjective with kernel dimension zero or one. If the kernel has dimension one, U'=U times F2 and closure does not change. Otherwise U' is the graph of a unique linear functional ell on U, and

$$
\mathrm{cl}_{W'}(S)=\{p\in\mathrm{cl}_W(S):g(p)=\ell(R(p))\}.
$$

The new atom support condition is either old closure, or exact separation of every excluded point in old closure by the same appended bit and affine extrapolation determined on S. The functional extends to the entire feature-row space. Two old distinct atoms are compatible for coherent matching exactly when this test accepts their symmetric difference. The same g must work across every matched pair. Individual closure tests are not independent computational gates. No polynomial total compression bound follows.

## 2. Strict nonminimum compression in an actual reachable state

Use four bits a,b,c,d. Start with affine inputs and adjoin h=ab, so V=span(1,a,b,c,d,h). Next compute g=d(a+b); successor V'=V+span(g). Both are legal multiplications. Encode unmarked functions by mask bit index a+2b+4c+8d, augmented functions by low 16 bits for y=0 and high 16 for y=1. Target f=0x0127, graph G_f=0x0127fed8.

Old three-atom representation:

    {0x00000ff0, 0x000ff000, 0x01280128}.

Old four-atom representation:

    {0x00006699, 0x00669900, 0x00010001, 0x01400140}.

The latter has two disjoint compatible pairs in displayed order, producing

    {0x0066ff99, 0x01410141}.

The exact dictionaries contain 11,503 old and 36,511 successor nonzero atoms. The graph is not in either dictionary. For every old atom p, G_f+p is NOT in the successor dictionary: verified both by enumeration and by independent row-span membership. Thus no two old atoms represent the target; the displayed triple is minimum. The successor pair is minimum. No old triple compresses to a successor pair by matching: an unmatched old atom would remain, yielding a mixed old/successor pair, which is excluded. The matching formula strictly requires a nonminimum old representation in this actual SCC state. The four-term representation is minimal among those achieving cost two. This resolves the reachable-state question in section 7 of COHERENT_MATCHING.md by finite exact counterexample, not an asymptotic bound.

## 3. Complete census for this transition

For augmented atom p write low/high halves p0,p1 and marker coefficient p0+p1. A mixed old/new pair represents a marked graph iff its two coefficients XOR to all ones. Its target mask is all ones XOR the two low halves. Group atoms by marker coefficient, join complementary groups and collect target masks. Compare with exact quotient BFS ranks from MARKED_GRAPH_CAPACITY.md. On rank-three-to-two targets, existence of a mixed pair is equivalent to some old minimum triple achieving matching cost two: expand the successor atom into two old atoms; the resulting three atoms must be distinct, else cancellation gives rank one. The successor atom cannot be old because old rank is three. Conversely a compressed triple leaves an old atom.

The census gives 20,736 rank-three-to-two targets; exactly 4,096 have no mixed pair. This count is for this particular transition, not a general-circuit frequency estimate.

## 4. Verification and boundary

Run python3 research/SCC-001/support_incidence_replay.py from the repository root. It reuses existing standard-library marked graph and quotient replay modules. Exact atom enumeration, independent closure membership for 48,014 nonzero old/new atoms, 11,503 independent mixed-pair exclusions for the witness, exact quotient ranks and all 65,536 target masks for the census. PASS capture 4ed0b9f7f92f488184c7a9f6bc79e97c, original tested script SHA-256 3361f2202b7dfe7c21005dc0dd971604eb8eb70779c0feae34c134d0887503ba. Local exact regression, not independently attested execution. Predecessor affine-hull saturation and MOD3 scalar domination remain in force. Next candidate must retain nonminimum supports, nonlinear incidence and shared-gate compatibility rather than just minimum fiber or affine span. Seek an independently bounded amortized quantity on support reconfiguration, not shortest legal gate path in disguise. No unrestricted SAT demand bound, complexity separation or public claim promotion.

Boundary: REACHABLE_STRICT_NONMINIMUM_COMPRESSION_ESTABLISHED_BY_FINITE_REPLAY__GATE_COHERENT_AMORTIZED_CAPACITY_OPEN.
