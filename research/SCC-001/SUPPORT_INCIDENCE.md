# SCC-001: support incidence and strict nonminimum compression

Status: exploratory author-derived propositions and exact finite computer-assisted counterexample, not Lean-certified, independently adjudicated or novelty-certified. Continues [coherent matching](COHERENT_MATCHING.md) and [marked graph capacity](MARKED_GRAPH_CAPACITY.md), protected base e24feab62c7b86851b1d1ed157c40b2292494359. No extra computational outputs or restriction on nonlinear reuse.

## 1. Exact atom membership by feature closure

Let W be the available feature space on the augmented cube, including constant 1 and marker y. Choose a basis with constant 1; write R(p) for its evaluation row at augmented point p. For a nonempty point subset S, define cl_W(S) as the set of p whose row belongs to span R(S). The constant coordinate makes this equivalent to affine closure of the nonconstant feature rows. S is an atom support iff cl_W(S)=S. An atom is a conjunction of available affine equations, so every point in this row-span closure satisfies them. Conversely the common zeros of the annihilator of span R(S) are exactly its row span by finite-dimensional duality; multiply the complemented linear forms to obtain its indicator. Empty support is the zero atom. This is an independent membership test by elimination, polynomial in explicitly supplied truth-table size, not necessarily in input bit count n.

Append the evaluation bit g of a legal gate to each row. Write U=span R(S), U' for the lifted span. Projection U' to U is surjective with kernel dimension zero or one. If the kernel has dimension one, U'=U times F2 and closure does not change. Otherwise U' is the graph of a unique linear functional ell on U, and

$$
\mathrm{cl}_{W'}(S)=\{p\in\mathrm{cl}_W(S):g(p)=\ell(R(p))\}.
$$

The new atom support condition is either old closure, or exact separation of every excluded point in old closure by the same appended bit and affine extrapolation determined on S. The functional extends to the entire feature-row space. Two old distinct atoms are compatible for coherent matching exactly when this test accepts their symmetric difference. The same g must work across every matched pair. Individual closure tests are not independent computational gates. No polynomial total compression bound follows.

## Joint gate compatibility is a linear system with a decomposability constraint

For each desired non-old atom support S let C_S=cl_W(S). The lift criterion says exactly

$$
g|_{C_S}+\mathbf{1}_{C_S\setminus S}\in W|_{C_S}.
$$

Necessity follows from the graph case above (the full-kernel case cannot create a non-old atom). Sufficiency follows because the displayed equality expresses g on S by an available affine form and forces disagreement at every other point in C_S. Already-old atom supports impose no constraint. The condition is affine-linear in the truth function g, and is unchanged by adding any element of V to g. Thus for any prescribed collection of pair contractions, concatenate these quotient-restriction equations. They define an affine linear system on B/V, with no independent gate choice per pair.

Let E=V/span(1). Multiplication induces the linear map

$$
\mu:\bigwedge^2 E\to B/V,\qquad \mu(\bar u\wedge\bar v)=[uv].
$$

It is well-defined because changing either representative by a constant changes the product only by V, and u squared equals u. A legal single gate exists for the prescribed contractions iff the pulled-back affine system on the exterior square has a decomposable solution q (zero allowed). In a basis of E the exterior coordinates form a symmetric zero-diagonal matrix Q over F2, with Q_ij=u_i v_j+u_j v_i. Decomposability is equivalent to rank at most two: a nonzero such matrix of rank at most two has a nonzero off-diagonal pivot Q_ij=1, and its two corresponding rows are independent. Since they span every row, symmetry and the pivot imply Q_kl=Q_ki Q_jl+Q_kj Q_il, an exterior product of those rows. Conversely any exterior product has rank at most two.

This provides a concrete joint constraint system: linear relation demands plus one rank-two resource condition, not independently counted pair savings. It tests a prescribed matching; it does not find the best matching or prove a polynomial bound on its size. The input truth-table size may be exponential; the criterion is not an efficient SAT algorithm. No demand estimate is asserted.

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

Run python3 research/SCC-001/support_incidence_replay.py from the repository root. It reuses existing standard-library marked graph and quotient replay modules. Exact atom enumeration, independent closure membership for 48,014 nonzero old/new atoms, 11,503 independent mixed-pair exclusions for the witness, exact quotient ranks and all 65,536 target masks for the census. PASS capture 4ed0b9f7f92f488184c7a9f6bc79e97c, original tested script SHA-256 3361f2202b7dfe7c21005dc0dd971604eb8eb70779c0feae34c134d0887503ba. Also run python3 research/SCC-001/joint_gate_replay.py. All 512 distinct legal gate values, five support fixtures, 2,560 linear-constraint versus lifted-closure comparisons, all 1,024 exterior-square symbols (156 decomposable including zero); the two desired contractions admit exactly one legal gate class modulo V. PASS capture 4e7835406aef42f396018d0a95befb3e; script SHA-256 a0ac854fee61d86aa89ee927125547fefaf95612826c81312713ca27ccc960d9. Local exact regression, not independently attested execution. Predecessor affine-hull saturation and MOD3 scalar domination remain in force. Next candidate must retain nonminimum supports, nonlinear incidence and shared-gate compatibility rather than just minimum fiber or affine span. Seek an independently bounded amortized quantity on support reconfiguration, not shortest legal gate path in disguise. No unrestricted SAT demand bound, complexity separation or public claim promotion.

Boundary: REACHABLE_STRICT_NONMINIMUM_COMPRESSION_ESTABLISHED_BY_FINITE_REPLAY__GATE_COHERENT_AMORTIZED_CAPACITY_OPEN.
