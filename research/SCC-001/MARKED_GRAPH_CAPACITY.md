# SCC-001: marked graph atoms and the sharp multiplicative transport law

Status: author-derived candidate and exact finite replay; no independent certification or novelty claim. Continues TARGET_IDEAL_TRANSPORT.md at protected fbcb380f3d7d90106987f9af9e37b9d89d59e286. Model: unrestricted Boolean circuits, affine operations free, each multiplication of two available bits charged one gate. No proof-certificate extraction hypothesis.

## 1. The marked target

Let X={0,1}^n, B=F2^X, and V a linear subspace of B containing 1 and all input coordinates. The target is f in B. Introduce a formal marker bit y on X times {0,1}; extend each v in V constantly in y, and set W=V+span(y). Define the atom set A(W) to consist of all finite products of elements of W, including the empty product 1 and zero. An atom is an indicator of the simultaneous equations w_i=1; equivalently an affine system on the available feature values and marker. Define rho_V(f) as the least number of atoms whose XOR is G_f=1+y+f. G_f is the graph indicator y=f(x), hence never zero. Existence follows by decomposing G_f into its 2^n singleton graph points using the input literals and marker. No expansion of arbitrary computation is required in the definition; this is a mathematical minimization, not an efficient algorithm.

## 2. Exact completion, affine and spectator invariance

rho=1 iff f belongs to V. Forward: suppose G_f=prod_i(v_i(x)+a_i y), a_i in F2. At every x exactly one marker value makes the product 1. At least one factor has a_i=1, else the product is constant in y. For that factor, evaluating at y=f(x) yields v_i+f=1 for every x, so f=1+v_i lies in V. Reverse: G_f itself belongs to W if f is in V.

If an invertible affine input-coordinate map transports V and f together, pullback is a bijection of their atom sets; rho is unchanged. More generally any bijective relabeling transporting V and f preserves rho (only affine relabelings preserve the initial model automatically).

For independent spectator inputs z and state V_ext=pullback(V)+span(z_j), with f ignoring z, old atoms extend, hence rho_ext<=rho. Conversely restricting all spectators to zero sends each extended factor to W and preserves G_f, hence rho<=rho_ext. This works for any number of unused spectators, including when V contains already-computed functions of x. No claim for interacting spectator states.

## 3. Exact one-gate transport

For a legal gate g=uv, u,v in V, let V'=V+span(g), W'=W+span(g). Every atom of W' is a sum of at most two atoms of W. If all factors lie in W this is immediate. Otherwise choose one factor p=g+w (w in W). Any other factor with coefficient one on g is p+r for r in W. In the Boolean function ring, p(p+r)=p(1+r), since p^2=p. Replace these factors one at a time. The atom is now pP where P is a product of elements of W. Then
    pP = wP + uvP.
Both summands are W-atoms, including possible zeros. This argument does not charge repeated uses of g independently; it eliminates every occurrence simultaneously. If g lies in V the inclusion is equality anyway.

Thus
    rho_{V'}(f) <= rho_V(f) <= 2 rho_{V'}(f).
The first inequality follows from inclusion of atoms; the second substitutes the above decomposition into any optimal new representation. Define the integer potential L_V(f)=ceil(log2 rho_V(f)). It is nonnegative, vanishes exactly at completion, is spectator invariant, and each legal gate drops it by at most one. The real logarithm has the same unit bound. For a computation with t remaining charged gates that produces f, L_V(f)<=t. The transport law is sharp: at the affine initial state on two inputs take f=x1*x2. It is not affine, so rho>=2; the identity G_f=(1+y)+x1*x2 gives rho<=2. Adjoining this gate yields rho'=1.

## 4. Demand: exact obstruction to logarithmic capacity

rho<=2^n from the singleton representation, so L<=n for every state and every one-bit target. It follows that this valid unit-cost potential cannot prove a superpolynomial lower bound in the encoded input length, even if the target is SAT decision. It is a genuine computational-state invariant, but insufficient demand.

The raw atom rank can nevertheless be exponentially large initially. With n input bits, W at the affine state is the space of all affine forms on n+1 bits. Any affine atom is represented by at most n+2 affine equations (reduce a consistent system to independent rows; inconsistent systems represent zero). Padding with the equation 1=1 gives at most 2^((n+2)^2) atoms, as each of n+2 rows has n+2 binary coefficients. Let A be their number. All sums of at most r atoms have at most (A+1)^r possible descriptions (padding with zero). There are exactly 2^(2^n) distinct marked graphs. Hence for any r with r*log2(A+1)<2^n there is a target with rho>r. In particular rho>=Omega(2^n/(n+2)^2) for some targets; this is nonconstructive and not an explicit SAT lower bound. The proved per-gate law controls a ratio, not an additive change of raw rank. It supplies no polynomial additive bound on raw rank and does not refute the possibility of a stronger one.

## 5. Implications and next target

This closes a useful model test: exact completion + spectator invariance + arbitrary nonlinear reuse + bounded one-gate decrease can coexist, but this natural logarithmic compression measure still has only linear demand. In contrast to prior support-ideal ranks, the marked graph has exactly one output value per input and no residual obligation at completion.

Next, investigate whether raw marked-atom rank admits an additive transport estimate, or a cheap explicit family with large raw one-gate drop. The ratio theorem alone does not decide that. The counting demand has no explicit efficient SAT family; no unrestricted SAT lower bound or complexity separation is claimed. Do not infer such a bound from generic counting, a restricted representation class, or the addition of an auxiliary marker. The marker is only a mathematical feature of the potential, not an extra computational output.

The exact truth-table replay enumerates all atom indicators by closing the available linear space under products, computes minimum XOR length by shortest paths over all truth functions for n<=3, then independently tests completion and transport. This is bounded finite verification of definitions and identities, not an asymptotic proof.

## 6. Exact affine-correction characterization

Write sigma_V(h) for the minimum number of products of elements of V whose XOR is h (sigma_V(0)=0). Then
    rho_V(f) = 1 + min_{a in V} sigma_V(f+a).
Upper bound: G_f=(1+y+a)+(f+a), with the first summand an atom and every summand of a minimum representation of f+a an atom.

Lower bound: each marker atom is either a cylinder P(x), or has a factor y+h(x) with h in V. By the same Boolean elimination identity used in section 3, all its other marker-dependent factors can be replaced by marker-independent factors, so it is P(x)(y+h(x)), with P a product of elements of V. Split an optimal marked representation into cylinders Q_i and marker atoms P_j(y+h_j). Comparing the coefficient of y as a function on X gives sum_j P_j=1, so at least one marker atom occurs. Comparing the constant term gives 1+f=sum_i Q_i+sum_j P_j h_j. Add h_1 and use the coefficient identity:
    f+(1+h_1)=sum_i Q_i+sum_{j>1} P_j(h_j+h_1).
Every summand on the right is a V-atom, at most rho-1 in number. This proves the reverse bound. Thus marked rank can be computed on the quotient vector space B/V using the images of V-atoms as unit generators, avoiding the extra marker truth table. This is an exact equality of minima, not just an upper bound.

At the initial state the unmarked atoms are indicators of affine subspaces of the binary cube. This is the XOR-of-AND-of-XOR representation model, not the OR-of-AND-of-XOR model in the DNF-of-parities literature (e.g. https://eccc.weizmann.ac.il/report/2014/099/). Do not import OR-top lower bounds into the XOR-top measure. For background on unrestricted AND-gate multiplicative complexity see https://csrc.nist.gov/projects/circuit-complexity. Novelty comparison beyond these model distinctions remains open.

## 7. Explicit superpolynomial one-gate drop via MOD3

External theorem: Smolensky's uniform-distribution polynomial approximation lower bound in characteristic 2 for the function f_n=1[sum x_i !=0 mod 3]. See Srikanth Srinivasan, *On Improved Degree Lower Bounds for Polynomial Approximation*, FSTTCS 2013, pp. 201–212, DOI 10.4230/LIPIcs.FSTTCS.2013.201, abstract, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2013.201 . The quoted mathematical consequence is: for some fixed delta>0 and c>0, all sufficiently large n, every F2 polynomial of degree <=floor(c sqrt(n)) has uniform error >=delta on f_n. This is an established external result, not proved or kernel-checked here. In particular one may choose an error threshold below 1/6 (e.g. 1/12) and reduce c to ensure the stated weak inequality. Bibliographic pin; no claim of source-byte acquisition.

At the affine initial state, each nonzero atom is an affine-subspace indicator of some codimension k. It has an exact product of k independent affine linear equations' truth indicators, hence polynomial degree <=k, and uniform mass 2^-k. Suppose f_n=a+sum_{i=1}^r P_i for an affine a and atoms P_i. For integer d>=1 retain only atoms of codimension <=d. The retained expression is a polynomial of degree <=d. Its disagreement with f_n is contained in the union of the deleted supports, each of probability <=2^(-d-1), so its error is <=r 2^(-d-1). Smolensky's bound for d=floor(c sqrt(n)) therefore gives r>=delta*2^(d+1). Apply section 6's exact equality of minima:
    rho_{V0}(f_n)-1 >= delta*2^(floor(c sqrt(n))+1).
No comparison with OR-top DNF is used. This is a proved consequence of an external approximation theorem, not generic counting or a restricted circuit lower bound misidentified as unrestricted.

A uniform AND/XOR computation of f_n uses at most 3n charged gates. Keep one-hot residue indicators r_0,r_1,r_2 (initially 1,0,0). On receiving x, replace each r_j by
    r'_j=r_j+x(r_j+r_{j-1 mod 3}),
using the OLD residue indicators simultaneously and one multiplication for each j. For x=0 the state is unchanged; for x=1 it cyclically shifts. Output 1+r_0. Affine combinations are free and all intermediate values are retained, as in the SCC state model. All reachable states in this explicit sequence have polynomial-size descriptions. The final rank is 1. Telescoping the actual nonnegative rank drops along the at most 3n steps proves that at least one step drops raw rank by
    delta*2^(floor(c sqrt(n))+1)/(3n).
This is superpolynomial in n (also in the polynomial-size state representation), even on an explicit linear-size circuit family. The argument asserts existence of a gate along the explicit history, not an identified index for every n. It refutes ANY universal polynomial additive ceiling on raw rank. It does not refute the sharp factor-of-two transport law. Nor does it give a lower bound for unrestricted MOD3 or SAT; the cheap MOD3 circuit is the counterexample.

## 8. No monotone scalar recalibration can recover superpolynomial demand

The preceding comparison extends to every potential of the form Phi_n(V,f)=h_n(rho_V(f)), where h_n is nonnegative and nondecreasing in the integer rank, h_n(1)=0, and Phi is invariant under extension by independent spectators. The same h_n applies to every state on n inputs. Assume that every legal gate decreases Phi by at most a fixed polynomial p(n,s) in input count n and the number s of previous gates (a polynomial in n and polynomial-size circuit-state encoding is equivalent along the explicit comparator). Take p nonnegative and bounded above by a polynomial in n+s; no uniformity of h_n as an algorithm is required.

For arbitrary n and any reachable V,f on n inputs, rho_V(f)<=2^n. Choose N=O((n+1)^2), N>=n, large enough that the explicit MOD3 target on N inputs has initial rank at least 2^n by section 7. Extend V and f by N-n independent unused inputs. Spectator invariance gives Phi_n(V,f)=Phi_N(V_ext,f_ext), and the rank is unchanged. By monotonicity of h_N,
    Phi_n(V,f) <= h_N(rho_initial(MOD3_N)).
The explicit 3N-gate MOD3 computation reaches rank 1. Telescoping the hypothesized per-step bound gives h_N(rho_initial(MOD3_N)) <= sum_{s<3N} p(N,s), polynomial in N and therefore in n. This proves a uniform polynomial ceiling on every target and state, including SAT decision, for every such scalar recalibration. For dimension-independent h, the same proof does not even require spectator invariance of Phi as an additional premise, since the unchanged rank already implies it. No assumption that h is continuous, computable, logarithmic or strictly increasing is needed. This is a no-go for rank-only monotone potentials under the stated soundness and spectator assumptions, not for all target-sensitive invariants or for joint measures depending on the complete representation geometry.

This removes the residual uncertainty in section 5 about whether raw rank might have a polynomial additive law. The next viable route must use more than scalar minimum atom count: e.g. the geometry of families of near-minimal decompositions and how legal gates act jointly on them, with independent demand and universal amortized estimates. A new measure must explicitly evade this MOD3 domination comparator.

## 9. Exact finite replay receipt

Run the following two standard-library scripts from the repository root:
    python3 research/SCC-001/marked_graph_replay.py
    python3 research/SCC-001/marked_quotient_replay.py

Observed PASS: 69 reachable gate transitions; 15,840 atom transport checks; 2,304 exact marked-target comparisons; 48 affine relabelings; 32 spectator comparisons. Independent quotient shortest-path computations agree with marker shortest-path computations on 548 targets. Five four-bit gates give 327,680 additional exact target comparisons; raw drop histogram 0:260512, 1:58976, 2:8192. Explicit four-bit sharp ratio counterexample: f=1[weight(a,b,c,d)<=1], g=ab. The mask of f is 0x117 with bit index a+2b+4c+8d. At V0, rho=4: the three old atoms with masks 0x1,0x6,0x110 sum to f; independent enumeration of every pair of old atoms and every affine correction excludes a two-atom representation. At V0+span(g), rho=2 because
    f=(1+a+b+g)+(1+g)(1+c+d)(a+b+c).
The target is not itself in the new state. Thus raw rank drops from 4 to 2 in one step. The uniform MOD3 residue automaton was exhaustively checked on all 8,190 input assignments for n=1,...,12. This confirms the finite computation construction, not the Smolensky asymptotic theorem. No independent execution attestation or Lean formalization is asserted.

Final research boundary: MARKED_GRAPH_TRANSPORT_EXACT__MONOTONE_SCALAR_RECALIBRATIONS_POLYNOMIALLY_BOUNDED__NONSCALAR_STATE_CAPACITY_OPEN.
