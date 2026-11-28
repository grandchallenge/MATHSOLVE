# SCC-001: joint witness elimination and fixed-family compatibility barrier

Status: author-derived exploratory propositions and bounded exact replay; not independently adjudicated, Lean-certified or novelty-certified. Continues [exterior visibility](GATE_LABELLED_AFFINE_FRONTIER.md), [support incidence](SUPPORT_INCIDENCE.md), [minimal-generator barrier](MINIMAL_GENERATOR_BARRIER.md), exact base 83acea6a49bd190d99c3c8aebbb6a078f08c3fcf. [SCC tracker](https://github.com/grandchallenge/MATHSOLVE/issues/1309). Unrestricted nonlinear reuse and one-bit target semantics.

## 1. Joint elimination theorem

Use the Boolean function algebra B on n>=2 bits, with available-feature space V containing affine inputs. Fix M nonzero linear functionals Lambda initially annihilating V. A witness is live while it annihilates the current feature space; once dead it stays dead. No independence, disjointness, efficient enumeration or target-independence is required. The complete target-disagreeing family consists of annihilators of V with lambda(f)=1. Computing f kills every member; killing every member implies f is available by duality.

Let d_V(lambda) be the first degree with nonzero evaluation on F_d(V), the span of products of at most d available features. Since coordinate literals are available, d<=n; dead witnesses have d=1, live ones d>=2. The predecessor all-orders theorem says a live witness has nonzero leading exterior d-form on V/span(1); a gate uv decreases d exactly by one iff its double contraction with u,v is nonzero. Otherwise d is unchanged. A uniform independent ordered pair u,v in V gives a decrease with probability >=(1-2^(-d))(1-2^(-(d-1)))>=3/8. The radical of a nonzero alternating k-form has codimension >=k, applied to both successive contractions. This works in every evolving state, including nonlinear features.

Define the integer potential

$$
P(V)=\sum_{\lambda\in\Lambda}(2^{d_V(\lambda)-1}-1).
$$

A successful contraction reduces its summand by 2^(d-2), at least half of that summand. Conditional on the actual state, expected next P is <=(13/16)P, using the SAME global operand pair for all witnesses. No independence between events is needed. Some legal gate achieves that bound; if P>0 it is nonredundant. Greedy iteration gives

$$
P_t\le (13/16)^t P_0.
$$

Uniform random pairs give the same upper bound on expected P_t by conditional expectation. As P is integral, elimination is complete when (13/16)^t P_0<1, and random survival probability is at most that expression. Since P_0<=M(2^(n-1)-1), sufficient greedy length is O(n+log M); specifically 1+floor(log(P_0)/log(16/13)) for P_0>=1, zero when P_0=0. Random length O(n+log M+log(1/delta)) suffices for failure probability <=delta. This is an existential gate-count argument, not efficient uniform gate selection.

Consequently a fixed family of size at most 2^poly(n) cannot force superpolynomial multiplicative complexity merely by requiring every member eliminated, even for nonadditive functions of the surviving witnesses. Stronger than a weighted-sum ceiling: the entire family can actually be discharged by one shared legal history. This does not show incomplete families suffice for targets or that prescribed order or evolving constraints can be met cheaply.

## 2. Exact transfer to joint support compatibility

Use augmented points (x,y), W=V+span(y), and nonempty desired atom supports S. For p outside S define the obstruction set of augmented linear functionals eta supported in S union {p}, with eta_p=1 and eta(W)=0. By feature-row closure, p lies in closure(S) iff such a relation exists: R(p) lies in span R(S) iff there is a dependence with coefficient one at p. Thus S is an atom iff every obstruction set is empty.

When adding features, an initially eligible eta remains an obstruction iff it annihilates the new features. Define its projection lambda(x)=eta(x,0)+eta(x,1). Every legal gate is marker-independent, so eta(g)=lambda(g). The projection annihilates V. If lambda=0 the obstruction is permanent even when all Boolean functions of x are available. Otherwise it is an ordinary witness from section 1.

For any fixed family of supports feasible in saturated W_max=B+span(y), no permanent obstruction occurs. Collect distinct nonzero projected witnesses Lambda from all outside points and desired supports. Simultaneous atom availability is exactly elimination of all Lambda: a necessary and sufficient cumulative condition for arbitrary feature extensions, not a requirement that every support be realized in the same step. Section 1 constructs one legal history of O(n+log |Lambda|) gates realizing all supports together. Already available supports add no obstruction. Empty support is the zero atom.

In particular all saturated-feasible supports of size at most k can be realized simultaneously in O(n(k+1)) gates. Each projected obstruction has Hamming weight <=k+1, so there are at most sum_{j=1}^{k+1} binomial(2^n,j) <= (2^n+1)^(k+1) possible distinct nonzero projected witnesses, regardless of number of supports. Thus fixed polynomial-point-size support tests cannot force superpolynomial gates, even for exponentially many supports. This bounds actual point support size, not description length of large supports.

## 3. Target necessity and remaining gap

If a fixed support family consists of atoms of V+span(f,y), all its initial projected obstructions obey lambda(f)=1: adjoining f alone eliminates every obstruction. A family certifies f across reachable states only if its disappearance implies f belongs to the current V. The joint elimination theorem then bounds the remaining multiplicative complexity C from above. For C>=1, n>=2 and M>0, applying the greedy estimate at t=C-1 gives the necessary condition

$$
M\ge \frac{(16/13)^{C-1}}{2^{n-1}-1}.
$$

A superpolynomial C therefore rules out singly exponential size 2^poly(n) for a complete fixed witness family. Exponential C requires doubly exponentially many witnesses. This is conditional, not proof of SAT hardness. It does not exclude compact descriptions of huge witness sets, or nonadditive, state-dependent coupled constraints.

Explicit sparse-test escape: on three bits take f=abc and compute ab, ac, bc. The resulting V is all functions of degree <=2, not containing f. Its annihilator is the one-dimensional span of full eight-point parity: each degree<=2 monomial has even support and V has dimension seven. That parity evaluates f to one. Every target-disagreeing witness of weight <=7 has disappeared although f remains unavailable. Sparse tests cannot be presumed complete.

## 4. Existence versus explicit SAT demand

There are 2^(2^n) Boolean targets on n bits. With s charged gates, gate i chooses two affine combinations of the n inputs, constant and i-1 previous gates, at most 2^(2(n+i)) choices. Final affine output has at most 2^(n+s+1) choices. Redundant padding covers all circuits of at most s gates. The count is at most 2^(s^2+2ns+2s+n+1). For sufficiently large n and s=floor(2^(n/2)/2), this is below the number of targets. Thus some targets require exponentially many legal rank-two operations in the evolving-space model. Their complete target-disagreeing witness families cannot be eliminated faster, by duality. This is nonconstructive, not an explicit target or SAT proof. An explicit superpolynomial lower bound for total encoded SAT in this model would imply NP is not contained in P/poly.

## 5. Replay and boundary

Run python3 research/SCC-001/joint_elimination_replay.py (standard library). It builds truth-table filtrations, enumerates ordered operand pairs via their product multiplicities, checks individual visibility-decrease frequencies and joint expected-potential inequality, and greedily replays complete target witness families in actual evolving states. It separately exhausts nonempty augmented supports on two bits, compares permanent-witness tests to saturated atom closure, and checks all sixteen possible extra unmarked features. PASS: 53 target-complete greedy cases, 65 charged steps, 20,864 witness/distinct-gate comparisons, 255 support-closure cases, 4,080 one-feature transfers, sparse false-completion fixture. Initial capture 8550cae7950a43d880834b4c85b31052; final replay and Markdown capture 6093a80ab96c478b9f93c1f1ec8e9581; script SHA-256 b69d329227c206d3b0fa5756f8243c1be9f7289d4c287f4d636b749d4a7987a5. Finite regression is not independent attestation or general proof.

Next: an independently characterized target-complete obstruction with genuinely global or state-dependent coupled constraints, rather than fixed singly exponential collections of linear elimination tests. Prove lower bounds surviving compact representations of large witness cosets and dynamic rank-two choices; invoking the complete witness coset is equivalent to the original construction, not a new lower bound. No unrestricted SAT demand, P/NP separation or certification.

Boundary: FIXED_WITNESS_FAMILY_JOINT_ELIMINATION_LOG_CARDINALITY__SPARSE_SUPPORT_COMPATIBILITY_POLYNOMIAL__GLOBAL_TARGET_COMPLETE_CAPACITY_OPEN.
