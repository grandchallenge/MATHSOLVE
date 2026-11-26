# SCC-001: shared-interaction communication capacity and its ceiling

Status: author-derived candidate propositions and exact bounded regression; not independently adjudicated, Lean-certified or novelty-certified. Continuation of [#1309](https://github.com/grandchallenge/MATHSOLVE/issues/1309), [syzygy transport](SYZYGY_TRANSPORT.md) and [Cogentic provider extraction](https://github.com/grandchallenge/MATHFORGE/blob/273039ed8384e2d54815b7bca64627372a808cec/sources/COGENTIC-26/METHOD_AND_ARITHMETIC_CROSSWALK.md). This is a new model-relative comparator, not an identification of communication and circuit cost.

## State and relative interaction

Partition the n Boolean coordinates into x and y, each with a fixed zero anchor. For h in the Boolean function ring define the linear map

$$
\Gamma h(x,y)=h(x,y)+h(x,0)+h(0,y)+h(0,0).
$$

All operations in this expression are over the binary field. The kernel is exactly the sum of functions depending only on x and functions depending only on y: one direction follows by cancellation, and the other by rearranging the defining identity. Both parties know the input-dependent values of a basis of Gamma(V) as common free advice, not the entire input or values of V. This definition is basis-independent since changing bases requires only linear combinations of the common advice. A deterministic two-party protocol may depend on the advice, and must enable both parties to determine Gamma(f) on each actual input. Define Phi for this cut as the minimum worst-case bit cost of such a protocol. It is equivalently the maximum of minimum deterministic communication costs on the separate advice fibers, with both parties outputting and the fiber common knowledge. No computational cost for local calculation is charged.

## One-gate theorem

Let g=uv with u,v in V, and V' be V plus the span of g. Monotonicity follows by ignoring the extra advice. To simulate the successor advice using the old advice, Alice sends u(x,0) and v(x,0). Bob reconstructs both operands via the Gamma identity, knows u(0,y), v(0,y), u(0,0), v(0,0), and computes

$$
\Gamma g=uv+u(x,0)v(x,0)+u(0,y)v(0,y)+u(0,0)v(0,0).
$$

Bob sends this one bit to Alice. The parties can now reconstruct the successor basis advice, even if the gate is redundant. This proves

$$
0\leq\Phi(V,f)-\Phi(V',f)\leq3.
$$

If f belongs to V then the target interaction is already common knowledge and Phi is zero. Conversely zero does not imply f belongs to V: a local-only function has zero interaction. The maximum Psi over all coordinate cuts retains monotonicity, the 3-bit bound and target completion. Telescoping gives a lower bound of Psi(initial,f)/3 on the charged gate count. This is a necessary bound, not a characterization of circuit cost.

## Exact spectator invariance and model correction

Appending independent unused coordinates means lifting V and adding the affine span of those new coordinates. It does NOT mean granting the entire tensor-product function space as degree-one state, since that would give cross products for free. The filtration, rather than the degree-one space, has the tensor-product structure described in SYZYGY_TRANSPORT.md. For any extended cut, the interaction advice and target equal those for the restricted original cut, ignoring spectators. An old protocol can ignore the spectators; an extended protocol can be restricted by fixing them all to zero. These two simulations prove equality of optimum costs, including empty cuts. Taking the maximum over cuts also preserves equality because every original cut extends.

## Absolute ceiling: why the candidate fails the central demand gate

For any state and any cut, Alice can send her full input to Bob, who computes Gamma(f) locally and returns one output bit; reverse the roles if Bob has fewer input bits. Thus for n input bits,

$$
\Phi_{X|Y}(V,f)\leq\min(|X_{bits}|,|Y_{bits}|)+1\leq\lfloor n/2\rfloor+1.
$$

The same bound holds for Psi and for any fixed probability-weighted average over cuts. This is independent of the algebraic degree, reuse depth and truth-table size. Such an unscaled communication cost cannot supply superpolynomial initial demand. A fixed nonnegative unnormalized sum of cuts is also limited by the following argument. Nonlinear or target-dependent reweightings require a new estimate. This is a no-go for the proposed direct transfer, not for all communication-derived or SCC invariants.

At the initial affine state the advice vanishes. For the inner-product target on two m-bit blocks, the sign matrix is Walsh–Hadamard and has real rank 2^m. Each leaf of a deterministic protocol on the full rectangle is a rectangle and, with both parties outputting, monochromatic. A depth-d protocol therefore expresses the sign matrix as at most 2^d rank-one matrices, proving d at least m. The candidate can detect linear interaction demand but not the required superpolynomial demand. Even maximal communication may correspond to an inexpensive circuit.

## Fixed nonnegative cut sums: a stronger obstruction

For n at least two let each unordered nontrivial coordinate cut c have a nonnegative weight w_c, fixed independently of V and f. Define the aggregate potential by

$$
\Psi_w(V,f)=\sum_c w_c\Phi_c(V,f).
$$

Suppose a uniform one-gate ceiling K(n) holds for this aggregate for every target and every legal gate. At the affine state take the target f=x_i*x_j for each distinct pair of input coordinates. The single gate computing f makes the successor potential zero. For every cut separating i and j the initial interaction is a nonconstant AND of two private bits, with no interaction advice, so its communication cost is at least one (fix all remaining inputs to zero). For cuts not separating the pair the interaction is zero. Nonnegativity therefore implies that the sum of weights over cuts separating that pair is at most K(n). Sum these inequalities over unordered pairs. A cut of block sizes a and n-a separates exactly a(n-a) pairs, at least n-1. Hence

$$
(n-1)\sum_c w_c\leq\binom n2 K(n),\qquad
\sum_c w_c\leq nK(n)/2.
$$

The individual input-transfer ceiling gives, for every target and state,

$$
\Psi_w(V,f)\leq\frac{nK(n)}2(\lfloor n/2\rfloor+1).
$$

Thus the ratio of initial demand to the universal one-gate bound is at most quadratic for every fixed nonnegative cut weighting, even when exponentially many cuts appear and weights are not normalized. For K(n)=0 all nontrivial weights vanish. This argument does not cover signed weights, target-dependent weights, or nonlinear functionals; these need independent demand and gate estimates. The elementary pair-counting proof is author-derived and not a separate finite replay claim.

## Replay and evidence boundary

Run python3 research/SCC-001/interaction_replay.py. The exact finite minimax solver partitions each advice fiber by all distinct one-bit row or column queries. A terminal fiber is one on which the target is determined separately by each party's local input; it need not be a monochromatic rectangle on a promise. The deterministic recursion is exhaustive because a nontrivial query strictly shrinks the fiber and any constant query can be omitted. The tests cover all affine operand pairs and every target on two total bits, 64 seeded four-gate histories on four total bits and random targets, and explicit spectator extensions. Observed: 320 gate reconstructions; 2048 target-cost comparisons; 320 completion checks; 16 spectator comparisons; seed 90210; PASS. CHAD capture b86e4e2ded604bdb8ffa17e948ad4c44, replay SHA-256 853e91fee2d510526eb48fe17ba969f9a9e6e65c37538f68e2e655437b411edf. Finite regression is not a proof or independent review.

## Next substantive obligation

Retain the exact gate simulation and spectator invariance as tests, reject direct communication depth as superpolynomial demand. Return to the actual SCC successor algebra C[t] with its correction cross-relations; seek a target-dependent relation measure that charges reuse even when communication of the complete input is cheap. Require independent characterization of initial demand, polynomial gate effect and target completion; do not hide the original circuit minimization inside the definition. The unrestricted SAT demand and transfer remain open. No certification or public claim promotion.
