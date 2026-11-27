# SCC-001: coherent matching transport and sparse-fiber syzygies

Status: author-derived exploratory propositions and bounded exact replay, not Lean formalization, independent certification, or novelty claim. Continues [marked graph capacity](MARKED_GRAPH_CAPACITY.md), protected predecessor 813adaa8d90cdb781c845fe30a2877e14fe9e6ac. No proof-certificate extraction, multi-output requirement, or restriction on nonlinear reuse.

## 1. The full marked representation fiber

Let W=V+span(y) on the augmented cube X times {0,1}. Let A be the set of distinct nonzero truth functions that are finite products of elements of W, including the empty product 1. Define E_A=F2^A, with standard basis e_a, and evaluation epsilon_A(e_a)=a. This is surjective onto the full Boolean function space B* because all augmented-coordinate singleton indicators are atoms.

For any h in B*, define the affine fiber F_A(h)={c:epsilon_A(c)=h} and the Hamming weight |c|=|support(c)|. For h=G_f=1+y+f this gives exactly rho_V(f)=min_{c in F_A(h)} |c|, since repeated terms cancel and zero terms may be removed. For general h write r_A(h), including r_A(0)=0. The complete fiber, rather than its minimum alone, is the object under study.

## 2. Coherent compression as an exact matching optimization

For one legal charged multiplication g=uv with u,v in V, let A' be the successor atom set. By the previous Boolean elimination identity, A is contained in A' and every b in A' is an old atom or the XOR of two distinct nonzero old atoms. This is simultaneous elimination of all occurrences of the same g; it does not bound the number of times a computed bit can be used.

Define the undirected simple graph Gamma_g on A, with edge {a,b} iff a+b belongs to A'. Equivalently, test whether a+b is an old atom or has form P(g+w), P a product of old available forms and w in W. The latter form follows by the established one-gate elimination; converse immediate. The graph uses truth functions, not syntactically duplicated factor lists. For S subset A write nu_g(S) for maximum matching cardinality in the induced graph.

**Theorem.** For every h in B*,
    r_{A'}(h) = min_{c in F_A(h)} (|c|-nu_g(support(c))).

Upper bound: choose a matching on the old support; replace each matched pair by its XOR in A', retain each unmatched singleton. The resulting XOR is h, with at most |c|-nu terms after cancellation.

Lower bound: take an optimal A'-representation with r' terms, expand each as an old singleton or pair. On A union {0}, regard a singleton a as the edge {0,a}, and a pair as an edge of Gamma_g. Retain repeated edges as a multigraph. The sum of the nonzero odd-degree vertices is h (each edge contributes the sum of its endpoints). Thus their set S is an old representation, with |S|<=2r'. In each connected component of the multigraph the odd-degree vertices can be paired by edge-disjoint trails: add auxiliary edges pairing them, take Euler tours, remove auxiliary edges, and discard closed trails. Trails with two nonzero endpoints and length one give disjoint matching edges in Gamma_g[S]. A trail between two nonzero endpoints of length >=2 can be replaced by two singleton edges through 0, of cost 2. A trail ending at 0 can be replaced by one singleton edge, of cost 1. These replacements require at most the number of original edges. Hence |S|-nu_g(S)<=r'. This proves equality, even with cancellations and arbitrary reuse. No claim that a single chosen old minimum representation suffices.

The minimization may be restricted to |c|<=2r_A(h), since the constructed S has size <=2r'<=2r_A(h). It is a finite, potentially exponential search, not a polynomial-time selector. If a prescribed representation is used, the matching formula only gives an upper bound on r_{A'}.

Equivalently define the old slack s(c)=|c|-r_A(h). The actual rank drop is
    r_A(h)-r_{A'}(h) = max_{c in F_A(h)} (nu_g(support(c))-s(c)).
This identifies a coherent gate saving after charging for the extra atoms in a nonminimum old representation. The same g governs all edges in the matching. This is not an additive polynomial capacity ceiling; MOD3 proves the optimized saving can be superpolynomial for some gate of a cheap circuit.

## 3. Equal-cost representations can differ under the same gate

Take four inputs a,b,c,d, index i=a+2b+4c+8d, and affine initial V. Let f have one-fiber {0,1,2} (mask 0x0007), and adjoin g=ab. Encode an augmented function by low 16 bits for y=0 and high 16 for y=1. The marked graph is mask 0x0007fff8.

Two exact minimum old representations have masks:
    S_good={0x0000ffff,0x00010001,0x00060006}
    S_bad ={0x00000ff0,0x00080008,0x000ff000}.
Every term is an old atom, and both XOR to the same marked graph. Exact old rank is 3, new rank is 2. The good representation has a compatible pair with XOR 0x00070007; the bad representation has no compatible pair. In fact the first two pairs in the good representation's sorted order are incompatible, and only its last pair is compatible.

The example proves that minimum length alone, even for a fixed target and fixed gate, does not specify how a given representation compresses. It does not establish that all minimum old representations together are insufficient; that stronger question remains open. The exact formula in section 2 deliberately minimizes over the entire fiber. No claim that this finite example alone implies an asymptotic lower bound.

## 4. Complete linear syzygies are generated by three-term partition relations

For each atom a and each augmented input coordinate z (including y), the two children az and a(1+z) are atoms or zero. When both children are nonzero, they are distinct from one another and from their parent. Define the relation
    e_a+e_{az}+e_{a(1+z)}.
It is in K_A=ker epsilon_A. If a child is zero, the relation is trivial and can be omitted.

**Theorem.** These partition triples generate K_A. Split an atom successively by every augmented input coordinate. Modulo the span of triples, its basis vector becomes the sum of basis vectors of singleton atoms in its support. Therefore every coefficient vector becomes the canonical singleton representation of its evaluation. A zero evaluation reduces to zero, proving the reverse inclusion. This works at every reachable V and even at arbitrary V containing input coordinates and 1. In particular dim K_A=|A|-2^(n+1), and all fibers are affine translates of K_A.

There is a stronger sparse-fiber consequence. Let c0 be any minimum representation of h with weight r. For every partition triple t, the vector c0+t represents h and has weight <=r+3. Thus the affine hull of all representations of h of weight <=r+3 equals F_A(h), because it contains c0 and one translate of every generating triple. This is an exact constant-slack saturation theorem; it is not a statement that the bounded-weight reconfiguration graph is connected, or that all differences of near-minimal representations have low Hamming weight. In particular using the linear span of near-minimal representation differences at slack three or greater loses all target-specific information beyond the affine translation itself. The affine translation (the target syndrome) still matters.

## 5. Exact gate extension of the full fiber and kernel

Choose, for every b in A' minus A, one old expansion s_b of weight two. Extend linearly to L:E_{A'}->E_A by L(e_a)=e_a for old a and L(e_b)=s_b for new b. Write i for old-coordinate inclusion. Then L i=id and epsilon_A L=epsilon_{A'}. Each d_b=e_b+i(s_b) is a relation of weight three, and these are a basis of ker L by their independent new coordinates. Consequently
    K_{A'}=i(K_A) direct_sum span{d_b : b in A' minus A},
    F_{A'}(h) = {i(c)+sum_b lambda_b d_b : c in F_A(h), lambda_b in F2}.
This is an affine isomorphism dependent on the choice of expansions; the exact quotient K_{A'}/i(K_A) is canonical via new coordinates. The new directions are independent of h. All gate-extension syzygies arise from individual atom substitutions, plus the old partition syzygies. They need not be independent as computational tasks: all are induced by the one shared gate.

The extension preserves the target syndrome but does not preserve Hamming weight; compression and cancellations are encoded in the coordinate supports, not in the abstract affine vector spaces. This explains why linearized relations alone, even obtained from a near-minimum family, do not capture the computational cost. Dimension counts can grow with dictionary size and do not vanish at completion.

## 6. Consequence and scope

The non-scalar matching description is exact but does not yet give a new independently estimable lower bound. The additive-slack affine-hull saturation excludes a particular tempting linearization of representation geometry. A viable continuation must retain nonlinear support incidence or joint compatibility under the same gate, rather than collapse those relations to span dimension. The next concrete target is a gate-coherent bounded-weight reconfiguration invariant (or a support-incidence obstruction to matching), with a genuine per-step/amortized law and independent target demand. Test the explicit MOD3 comparator, spectator invariance, and target completion; do not mistake the exact minimization for an efficient algorithm or a lower-bound proof.

No NP not-subset P/poly or P!=NP claim. No external theorem is needed for sections 1-5. Established graph-theoretic Euler-trail pairing and elementary linear algebra are reconstructed in the proof. Novelty has not been adjudicated.

## 7. Abstract minimum-only obstruction and finite evidence

The general matching theorem holds for any spanning dictionary of distinct nonzero vectors over F2 and any successor dictionary obtained by adjoining pair sums. In this broader setting the restriction to old minimum supports is genuinely false. Encode F2^4 vectors as integers using binary XOR. Take A={5,7,9,10,13}, A'=A union {8,14}, h=6. The only old three-term representation is {5,9,10}; its pair sums 12,15,3 are not in A', so its matching cost is 3. No old representation of size <=2 exists (check ten pair sums and five singleton values). The old four-term representation {5,7,9,13} has the disjoint pairs (5,13) and (7,9), producing 8 and 14, whose XOR is 6. Hence new rank is 2 and every old minimum support fails to achieve the new minimum. This example is not claimed to be a reachable SCC gate state; the corresponding stronger restriction question for actual Boolean atom dictionaries remains open.

Run python3 research/SCC-001/coherent_matching_replay.py. Exact independent BFS versus exhaustive matching minimization: 603 pair-generated dictionary extensions in F2^3, all eight syndromes per extension, 4,824 comparisons. No strict minimum-only counterexample in that domain; the explicit F2^4 counterexample above passes. Six actual reachable Boolean states, 3,070 atom singleton expansions, 8,274 partition triples; exact GF(2) rank equals full kernel dimension in each. Three actual gate extensions, 1,464 independent new-coordinate substitution relations. The four-bit equal-minimum witness uses independently established old/new quotient distances and exact compatibility tests. All checks passed. The finite replay does not prove the general theorems or establish independent execution.

Boundary: COHERENT_MATCHING_TRANSPORT_EXACT__NEAR_MINIMUM_AFFINE_HULL_SATURATED__BOUNDED_SUPPORT_INCIDENCE_CAPACITY_OPEN.
