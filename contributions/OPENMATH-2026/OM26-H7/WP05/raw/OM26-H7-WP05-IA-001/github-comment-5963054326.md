GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H7-WP05-IA-001
agent_ref: INDEPENDENT-AGENT-705
assignment: OM26-H7-WP05
disposition: REPLAY_CLOSURE_VALIDATED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

At the protected H7 source state, let R(A) mean that the subtype-indexed real family a in A maps to 1/(a : Real) is not summable. Independent replay validates the predecessor's four mathematical reductions: for every finite F, R(A) implies R(A \ F); for every N, R(A) implies R(A ∩ {n | N ≤ n}); for every m ≥ 1, at least one residue r < m has divergent reciprocal fiber B = {n in A | n % m = r}; and for such a fiber, with K = {k | m*k + r in A}, reciprocal divergence of B is equivalent, up to deletion of k = 0 and fixed positive comparison constants, to reciprocal divergence of K.

The density obstruction is also valid, but it can be made self-contained without invoking the primes. Define N_j = 2^(2^j) and L_j = floor(N_j/j) for j ≥ 2, and let C be the union of integer intervals [N_j, N_j + L_j). Then the reciprocal sum over C diverges while C has upper asymptotic density zero. Therefore reciprocal divergence alone does not imply the positive upper-density hypothesis needed for a direct application of Szemerédi's theorem.

## Derivation

Finite deletion follows by contraposition. If the reciprocal family on A \ F were summable, then the family on A ∩ F would be summable because its index set is finite; A is the disjoint union of A \ F and A ∩ F, so finite disjoint-union closure of summability would make the reciprocal family on A summable, contradicting R(A).

Tail divergence is the finite-deletion result with F = {n | n < N}. This set is finite and A ∩ {n | N ≤ n} equals A \ F.

For the residue-fiber claim, fix m ≥ 1 and write A_r = {n in A | n % m = r} for r = 0,...,m-1. The A_r are pairwise disjoint and their finite union is A by uniqueness and boundedness of the Euclidean remainder. If every reciprocal family on A_r were summable, finite disjoint-union closure would make the reciprocal family on A summable, contradicting R(A); hence at least one fiber diverges.

For the scaling transfer, fix r < m and define phi(k) = m*k + r. Because m > 0, phi is injective, and the division algorithm gives a bijection from K = {k | phi(k) in A} onto B = {n in A | n % m = r}. Reindexing therefore identifies the reciprocal series on B with the family 1/(m*k+r) on K. The k = 0 term is a single finite term and is irrelevant to summability. For every k ≥ 1, m*k ≤ m*k+r < m*(k+1) ≤ 2*m*k, hence (1/(2*m))*(1/k) ≤ 1/(m*k+r) ≤ (1/m)*(1/k). Since all terms are nonnegative, the comparison test in both directions gives divergence of the B-series if and only if the reciprocal series over K diverges.

For the zero-density counterexample, the contribution of block j is at least L_j/(N_j+L_j). Since N_j ≥ 2j, L_j ≥ N_j/(2j), while L_j ≤ N_j/j ≤ N_j/2, so the block contribution is at least 1/(3j); summing over j diverges. For density, the total size of all earlier blocks is at most (j-2)N_{j-1}, while N_j = N_{j-1}^2. Throughout block j the counting ratio is therefore at most (j-2)/N_{j-1} + 1/j, and between blocks it only decreases. This tends to zero, so C has upper asymptotic density zero.

## Assumptions beyond bootstrap

The replay uses only the protected source encoding, elementary properties of summability under finite index sets, finite disjoint unions and reindexing, the comparison test for nonnegative real series, and the natural-number division algorithm. No external mathematical source, predecessor execution environment, or predecessor authorship was treated as verification. The pinned D3/D4 proof receipt is used only to locate the already-formalized arithmetic-progression conclusion boundary; it does not supply any of the hypothesis-side replay above.

## Verification / falsification hooks

The immutable task was fetched at TASK_COMMIT 37ef9dc603e66011ae68e5e5f8df32c9231c231a and its Git blob SHA-1 matched TASK_BLOB_SHA1 9ffb26ad5f9f698dad3356b98e596c86870b55eb. Independent SHA-256 recomputation at that commit matched all four protected source digests exactly: H7_D3.lean = 98a517c787311bc08489de4c088fc35c767bb7d485c565f2915ca1f6ddc0e0f9; H7_D4.lean = 6653f226b6d028dad8a764ff0bc055e14cd1f80c466a4d4d61f7753080470481; H7_D4_PROOF_RECEIPT.json = 255dae05057b107cbf315f8af83999df75e3b043f69e82f99666bc5576fcfaa0; statement.lean = 39b2cac164711f18b5cf898d70fdc7f81619ddf05a37f5c4d3782818a663aab0.

The finite-deletion claim is falsified by any example where a finite extension changes summability; the residue claim is falsified by a finite partition of a divergent nonnegative family into only summable fibers; and the scaling claim is falsified by failure of either the K-to-B bijection or the displayed two-sided comparison. The explicit block set C supplies a deterministic check of the density boundary without relying on prime-number asymptotics.

## Claim boundary

This replay validates the mathematical reduction, not Erdős Problem 3 itself. It does not authorize or perform repository mutation, certification, competition submission, or further-agent launch, and it does not convert the predecessor's uncompiled Lean snippets for the new hypothesis-side lemmas into a pinned axiom-gated formal artifact. The density construction establishes only that reciprocal divergence does not by itself imply positive upper asymptotic density; it does not prove that every possible Szemerédi-based strategy must use one particular additional density theorem.

## Next residual

Materialize and axiom-gate the finite-deletion, tail, residue-fiber, and scaling-transfer lemmas in the pinned Lean environment. Then test whether a scale-local concentration statement can bridge reciprocal mass to the already-pinned finite-AP conclusion without incorrectly asserting global positive density.