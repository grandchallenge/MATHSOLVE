# SCC-001: gate-labelled affine compatibility and amortized frontier capacity

Status: exploratory author-derived relative-state propositions with exact finite regression; no independent certification, Lean formalization, or novelty claim. Continues SUPPORT_INCIDENCE.md and BOUNDED_RECONFIGURATION.md at protected 58a5c6045edcae92cc8a84da3f273241c0948cf0. One Boolean decision output, unrestricted AND/XOR reuse; no proof of correctness extraction.

## 1. Local completion and the labelled dual relation space

Let X=F2^n, B=F2^X, V a linear space of available functions containing 1 and the coordinates, f the target. For any nonempty C subset X, write U=V|C. Completion on C is f|C in U. Let D_C(V)=U^perp in F2^C under the nondegenerate pointwise dot product. The target-disagreeing witnesses are
    L_C(V,f)={lambda in D_C(V): lambda(f|C)=1}.
The set is empty iff locally complete, by finite-dimensional duality. If nonempty it is an affine coset of codimension one in D_C(V).

A legal charged gate g=uv with u,v in V produces V'=V+span(g). Exact transport:
    D_C(V')={lambda in D_C(V): lambda(g)=0},
    L_C(V',f)={lambda in L_C(V,f): lambda(g)=0}.
Thus a gate label deletes incompatible witnesses using a SINGLE common condition. This is an exact law across every evolving state, not independent labels per region. On any live lambda define the bilinear form
    B_lambda(u,v)=lambda((uv)|C).
It is alternating on V since lambda(u^2)=lambda(u)=0, and descends to V/span(1) since lambda(v)=0. In an arbitrary quotient basis its alternating matrix is R_lambda. The label q=u wedge v pairs with R_lambda by summing upper-triangle coordinates, yielding lambda(g). This is the dual version of the exterior gate label in SUPPORT_INCIDENCE.md. Avoid using the full matrix trace pairing in characteristic two.

If lambda survives and the gate is nonredundant, the enlarged alternating matrix is the old matrix with one row and column appended, with zero diagonal (lambda(g^2)=0). Its rank cannot decrease and increases by at most two; alternating forms have even rank, as follows by splitting off a nonzero two-by-two symplectic block and induction. Thus a surviving witness rank either stays fixed or rises by two; a redundant gate leaves it unchanged. Rank itself is not asserted a target-completing potential.

## 2. Affine-leaf frontier

A V-tree on C is a finite binary decision tree whose queries are functions in V and whose leaf labels are functions in V. The tree is valid for f on C if each reached leaf label agrees with f throughout its reached region. Empty branches can be discarded; queries constant on the reached region can be bypassed. Write A_V(f;C) for the minimum worst-case number of queries, with final leaf evaluation free. The tree is an auxiliary mathematical decomposition, not an extra required output or a claim about decision-tree running time.

Equivalently the exact recursion is A=0 if f|C belongs to V|C, otherwise
    A_V(f;C) = 1 + min_{z in V, nonconstant on C}
                           max(A_V(f;C intersect {z=0}), A_V(f;C intersect {z=1})).
This terminates on strictly smaller cells. All trees exist because coordinates separate points. For n>=1, A<=n-1: query n-1 coordinate bits, then every remaining cell has at most two points with different last bit, on which f is affine. For n=0, A=0. Local completion is exactly A=0.

At the initial affine state this is the ordinary parity decision tree with affine rather than constant leaves; ordinary parity decision tree depth lies between A and A+1 (evaluate leaf by at most one extra parity query). The one-operand gate elimination principle already appears in Chistopolskaya and Podolskii, *Parity Decision Tree Complexity is Greater Than Granularity*, arXiv:1810.08668, Lemma 5, https://arxiv.org/abs/1810.08668 ; their Theorem 6 relates ordinary depth to Fourier granularity. No novelty claim for this known connection. Here the state-relative local compatibility, dual labels and weighted activation obstruction are derived explicitly. No external theorem is required for the proofs below.

## 3. Exact local one-gate transport and amortization

Define a_C(V,g)=1 if g|C is not in V|C and 0 otherwise. Let b_C(V,f)=1 if f|C is not in V|C and 0 otherwise. For every C,
    0 <= A_V(f;C)-A_V'(f;C) <= b_C(V,f) a_C(V,g) <= 1.

Inclusion gives the lower bound. If g|C is old, all successor queries and leaf labels on C can be replaced by old forms, so depth is unchanged. If target is already complete both depths are zero. Otherwise query the gate operand u once; on the two branches g equals 0 or v. Every successor form w+alpha*g (queries AND leaf labels) is now an old form on the branch. Restrict and translate a successor optimal tree on each branch, pruning constant queries. This gives old depth at most new depth plus one. Crucially every occurrence of the computed g is erased by the SAME query and branch substitution, regardless of its fanout and later nonlinear uses in the computation history.

Stronger than the depth scalar, for each successor valid tree there exists an old valid tree whose depth at every x is at most the successor depth at x plus b_C a_C. In the already-complete case use an old single leaf. Consequently any nonnegative weighted expected depth (probability measure on C, including zero-probability points still subject to exact correctness), or any supremum over distributions, obeys the same normalized unit bound. This is a pointwise transport of the depth-profile family, not an equality of optimal trees on all distributions.

For an actual history, label split nodes with the original gate index: at each leaf of the current V0-tree maintain V_j|leaf contained in V0|leaf. If g_j is affine there, no split; else replace its operand by an old form on that leaf and query it, making g_j affine on each child. This maintains the invariant by induction. At completion every leaf has an old affine label for f. Indices are strictly increasing on each branch, with at most one query per charged gate. The same global g_j may require different old forms on different leaves. No assumption of one globally fixed old operand across all leaves. The number of queries on an input is exactly the number of active split labels encountered along its path, and at most the number of charged gates. This constructs an independently bounded auxiliary profile from any successful circuit, not shortest circuit search in disguise.

For any finite family of nonempty regions and nonnegative fixed weights w_C, set
    Psi_V(f)=sum_C w_C A_V(f;C),
    charge_V(f,g)=sum_C w_C b_C(V,f) a_C(V,g).
Then along EVERY history,
    Psi_V0(f)-Psi_Vt(f) <= sum_{j<t} charge_Vj(f,g_j).
If the target is completed Psi_Vt=0. For a family containing X with positive weight, Psi=0 iff globally complete. With sum w_C=1 each charge <=1, giving an unconditional amortized lower bound. For a single whole cube this is sharp: f=ab, affine V, depth 1 then 0. This holds for arbitrary finite collections, even overlapping regions, with no independence assumption.

## 4. Spectator invariance

For the whole cube and cylindrically extended f,V, old trees lift unchanged; any padded tree restricts at spectator bits zero to an old tree (restrict queries/leaf labels, prune constant branches), no larger depth. Hence A is exactly invariant. The same proof holds for a region C lifted to C times the whole spectator cube, and weighted families of such lifted regions. Do not assert invariance of arbitrary non-cylindrical families or arbitrary changed distributions.

## 5. A constant-activation obstruction to weighted local accumulation

This is a sharper limitation than merely normalizing the weights by hand. Consider any unresolved region C. Because V includes input coordinates, its restriction U separates all points of C and contains 1. If U were closed under multiplication, it would contain every point indicator on C (multiply coordinate literals), hence all functions on C. Since the target is unresolved, U is not closed under multiplication. Equivalently, some lambda in D_C(V) has a nonzero alternating form B_lambda.

In fact at least one such lambda can be chosen target-disagreeing: the nonempty affine coset L_C(V,f) spans D_C(V) (each lambda of target parity zero is a sum of two elements of the coset). The map lambda -> B_lambda is linear, so if all coset elements had zero form, all of D_C(V) would have zero form, contradicting nonclosure.

Choose u,v independently uniformly from V. For a fixed lambda with nonzero B_lambda of rank r, a uniform u is outside its radical with probability 1-2^-r; conditional on that, the functional B_lambda(u,-) is nonzero and exactly half of v give one. Thus
    Pr[lambda(uv)=1] = (1-2^-r)/2 >= 3/8,
because nonzero alternating rank is at least two. This probability is exact for the individual witness, and the event implies a_C(V,uv)=1. The choice of witness may vary across regions, but the random operands are the SAME global pair across all regions. Independence across region events is unnecessary.

Let W_active=sum_C w_C b_C(V,f) and K=max_{u,v in V} charge_V(f,uv). By linearity of expectation K>=3 W_active/8. In particular,
    Psi_V(f) <= max(n-1,0) W_active <= (8/3) max(n-1,0) K.
The constant 3/8 is sharp for a single four-point affine plane at the initial two-input state, where its annihilator is the unique nonzero four-point parity witness with alternating rank two. This rules out superpolynomial demand for any nonnegative weighted local-frontier sum whose per-gate ACTIVITY-CHARGE ceiling is polynomial, even with exponentially many overlapping regions or target-dependent weights fixed along the history. It does not rule out a tighter capacity bound on the ACTUAL drops, correlated gate schedules, or nonadditive joint constraints. An active gate need not reduce optimal frontier depth. Random activation need not lead to fast target completion. These distinctions are essential.

## 6. Independently computed demand controls

At V0 the inner product f=sum_{i=1}^m a_i b_i on 2m variables has A=m. Query all a_i for the upper bound. Every leaf of an affine-query tree is an affine subspace of codimension at most its depth. If a quadratic function is affine on a coset, its polar form vanishes on the direction space L (take the second finite difference in two directions). For this inner product the polar form is nondegenerate alternating, so L subset L^perp implies dim L<=m. Hence every nonempty leaf requires depth >=m. The m charged multiplications attain the bound; unused spectator coordinates leave it unchanged. This is a direct independent demand calculation, not optimization over possible circuits.

For all n-bit targets, including the explicit cheap MOD3 comparator, A<=max(n-1,0), so normalized weighted demand cannot be superpolynomial. This is not a failed soundness test; it is a proven insufficient demand ceiling for the stated calculus. The next route must retain constraints that accumulate across states without reducing to local affine-query depth or counting mere gate activity. In particular the exact live-witness labels allow investigation of which surviving target-disagreeing relations can first become visible under future gates; the rank/activation result alone does not provide a superpolynomial lower bound.

The all-orders extension below strengthens this boundary.

## 7. All-orders visibility of surviving target witnesses

This strengthens the negative result of section 5 from a bound on a coarse activity charge to a bound on actual drops of a distinct potential.

Fix a nonzero functional lambda on B, with lambda(1)=0 and lambda(f)=1; local witnesses extend by zero outside their regions. Let F_d(V) be the span of products of at most d available forms, including 1. Define ell_V(lambda) as the least d>=1 for which lambda(F_d(V)) is nonzero. It exists and is <=n for n>=1 because F_n contains all singleton indicators. Dead witnesses have ell=1, live witnesses have ell>=2. Once dead they stay dead.

For live lambda with d=ell_V(lambda), define the d-linear form
    omega_d(w_1,...,w_d)=lambda(w_1 ... w_d).
It is nonzero, symmetric and alternating: repeating any operand reduces the product length using idempotence, and inserting 1 reduces length, so these evaluations vanish. It descends to E=V/span(1), defining an exterior d-form. This is the first nonzero exterior visibility level of the witness, and at d=2 it is exactly B_lambda.

For a gate g=uv, the established filtration law F_k(V')=F_k(V)+g F_{k-1}(V) yields the exact criterion
    ell_V'(lambda) in {d-1,d},
    ell_V'(lambda)=d-1 iff i_v i_u omega_d is nonzero.
Indeed F'_{d-2} is annihilated, and lambda(F'_{d-1}) is nonzero precisely when lambda(uv w_1 ... w_{d-2}) is nonzero for some old factors. At d=2 the contraction is scalar and the event kills the witness; at d>=3 it lowers the visibility level but the witness survives. Dead witnesses have zero drop. This is not a formal derivation that every old minimum representation suffices; it acts on linear functional tests of products, independent of atom minimization.

For a nonzero alternating k-form on a finite-dimensional vector space over F2, its radical (vectors whose contraction is zero) has codimension at least k: the form descends to that quotient and remains nonzero, requiring dimension >=k. Therefore for independent uniform u,v in V, equivalently their uniform classes in E, the probability of a live visibility decrease is at least
    (1-2^-d)(1-2^-(d-1)) >= 3/8.
First contract with u, nonzero with probability >=1-2^-d. Conditional on any successful u, contract the nonzero alternating (d-1)-form with v, nonzero with probability >=1-2^-(d-1). For d=2 this agrees with the exact rank formula in section 5. For a decomposable volume form on a d-dimensional quotient the two factors are equalities. At the initial affine state, lambda summing evaluations on a d-dimensional coordinate flat has first visibility d and the associated form is the determinant on its d coordinate directions. Indeed a product of d affine restrictions contributes to the full square-free monomial coefficient precisely the determinant of the linear coefficient matrix, while lower degrees have zero full coefficient. Thus the probability bound is sharp at every d<=n. This is an algebraic statement about uniform ordered operand pairs, including redundant products, not a random circuit efficiency guarantee.

For fixed nonnegative weights w_lambda on any family of these target-disagreeing functionals, define
    P_V(f)=sum_lambda w_lambda (ell_V(lambda)-1).
The exact per-gate drop is a weighted sum of contraction indicators, with zero contribution from dead witnesses. For all histories the drops telescope, and P vanishes at completion. If all target-disagreeing lambda with lambda(1)=0 receive positive weight, it vanishes ONLY at completion by duality. For each fixed state let K_actual=max_{u,v in V}(P_V-P_{V+span(uv)}). Linearity of expectation and the visibility theorem imply
    K_actual >= (3/8) sum_{lambda live} w_lambda,
    P_V <= (8/3) max(n-1,0) K_actual.
Thus even a polynomial ceiling on ACTUAL drops of this entire weighted visibility family forces polynomial demand. No assumptions of disjointness, independence of events, or efficiently enumerable witnesses. Weights must be fixed across the step; arbitrary recalibration between states is not covered. The maximum live visibility is exactly the established relative filtration degree of f when f is not in V: f in F_d gives ell<=d for every lambda(f)=1; f not in F_{d-1} gives a separating lambda annihilating F_{d-1} and with lambda(f)=1, hence ell=d. The maximum (minus one) is therefore not a new degree lower bound.

The visibility geometry is exact across nonlinear reuse, and admits a useful label hierarchy, but scalar fixed nonnegative weighting is again insufficient. The remaining route is genuinely coupled, nonadditive visibility/compatibility constraints with an independently proved amortized law and superpolynomial SAT demand; neither the present theorem nor the previous exact support matching supplies that demand.

## 8. Finite replay

Run python3 research/SCC-001/gate_labelled_frontier_replay.py. The standard-library replay checks the exact recursion, local gate transport, dual cuts, surviving alternating ranks, exact bilinear activation probabilities, target-disagreeing visible witnesses, arbitrary cylindrical spectator regions, pointwise depth profiles and a forward gate-labelled history with nonlinear reuse. It also checks all-orders filtration visibility against explicit alternating contractions. Finite tests do not establish the general theorems independently or certify novelty.

Observed PASS: 11 states, 24 transitions, 53,472 local comparisons, 88 old and 55 surviving witness-cut checks, 1,550 pointwise profile checks, 354 unresolved cells, 49 exact bilinear probabilities, 12,584 target-disagreeing visible witness checks, 80 cylindrical spectator checks. Four-gate labelled history completed all 256 three-bit target functions with four frontier leaves. All-orders: 3,216 contraction checks, 38 visibility probability checks, 2,084 weighted actual-drop certificates. Sharp coordinate-flat counts (d, successful ordered pairs, total): (2,24,64), (3,168,256), (4,840,1024), (5,3720,4096). Initial complete replay capture 44882c3d8e8840d1a7f43ba6c6612935.

Final boundary: GATE_LABELLED_AFFINE_FRONTIER_AND_EXTERIOR_VISIBILITY_EXACT__WEIGHTED_ACTUAL_VISIBILITY_DROPS_POLYNOMIALLY_BOUNDED__NONADDITIVE_GLOBAL_COMPATIBILITY_OPEN.
