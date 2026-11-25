GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-138-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-138-A1
assignment: ERDOS-138-A1
disposition: COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

The protected prose bound and the protected Lean theorem body are not interchangeable: they have opposite consequences for the registered root-growth problem.

With the protected normalization `W k = monoAPNumber 2 k`, suppose the prose bound were literally true:

`W (p + 1) ≥ p^(2^p)` for every prime `p`.

Then, using only monotonicity of the exact two-color van der Waerden number and Bertrand's postulate, one obtains

`(W k)^(1/k) → ∞`.

By contrast, the actual protected Lean theorem body

`p * 2^p ≤ W (p + 1)`

does not imply root-growth divergence, even after adding monotonicity and the protected solved difference-growth behavior. An explicit monotone integer-sequence countermodel is

`A(1)=1`, `A(2)=3`, and `A(k)=k*2^k` for `k≥3`.

It satisfies, for every prime `p`,

`p*2^p ≤ A(p+1)`,

and

`A(k+1)-A(k)=(k+2)*2^k → ∞`,

but

`A(k)^(1/k)=2*k^(1/k) → 2`,

not infinity.

Therefore any inference that treats the protected theorem body as if it carried the prose exponentiation bound is false. The discrepancy is outcome-changing, not cosmetic.

A second independent adversarial point is that subsequence root growth plus monotonicity is not enough without a gap condition. If `n_j=2^(2^j)` and a nondecreasing step sequence `B` is defined by

`B(k)=j^(n_j)` for `n_j ≤ k < n_(j+1)`,

then

`B(n_j)^(1/n_j)=j → ∞`,

while along `k=n_(j+1)-1`,

`B(k)^(1/k)=j^(n_j/(n_(j+1)-1)) → 1`.

Thus a sparse-subsequence proof requires explicit control of successive index gaps.

## Derivation

1. Monotonicity of the protected `W` follows from its exact meaning. Any monochromatic arithmetic progression of length `k+1` contains one of length `k`. Hence every `N` guaranteeing length `k+1` also guarantees length `k`, so the minimal guarantee satisfies

`W(k) ≤ W(k+1)`.

2. Assume the prose bound `W(p+1) ≥ p^(2^p)` for all primes `p`. For every sufficiently large `k`, put

`m = floor((k-1)/2)`.

Bertrand's postulate gives a prime `p` with

`m < p < 2m ≤ k-1`.

Hence `p+1 ≤ k` and `p ≥ k/2`. By monotonicity,

`W(k) ≥ W(p+1) ≥ p^(2^p)`.

Therefore

`log((W(k))^(1/k)) ≥ (2^p/k) * log p ≥ (2^(k/2)/k) * log(k/2)`,

which tends to infinity. So the prose bound would prove the registered Erdős-138 root-growth statement outright.

3. Under the actual Lean body `W(p+1) ≥ p*2^p`, the prime-subsequence lower bound has only

`(p*2^p)^(1/(p+1)) → 2`.

Prime density cannot upgrade a lower bound whose own subsequence roots stay bounded into divergence. The explicit sequence `A` above makes this logical failure concrete while preserving monotonicity, the weak prime bound, the protected values `A(1)=1`, `A(2)=3`, and even divergence of successive differences.

4. The exact interpolation lemma needed for any valid subsequence route is:

If `F : ℕ → [1,∞)` is nondecreasing, `n_j` is increasing, `F(n_j)^(1/n_j) → ∞`, and there is a constant `c>0` such that eventually

`n_j / n_(j+1) ≥ c`,

then `F(k)^(1/k) → ∞`.

Indeed, for `n_j ≤ k < n_(j+1)`,

`F(k)^(1/k) ≥ F(n_j)^(1/n_(j+1)) = (F(n_j)^(1/n_j))^(n_j/n_(j+1))`.

The right side diverges under the stated gap condition. For prime indices `n_j=p_j+1`, Bertrand supplies such a bounded-ratio gap condition. Thus the interpolation step is safe for the strong prose bound, but it is useless for the weak Lean body because the required subsequence-root divergence is absent.

5. Normalization audit within the protected formal file: `monoAPNumber` takes `(number of colors, progression length)`, and `W k` is exactly `monoAPNumber 2 k`. The protected prime theorem is therefore about two colors and progression length `p+1`. The off-by-one matters in interpolation: one must choose `p` with `p+1 ≤ k`, not merely `p ≤ k`. The Bertrand construction above does this. No further internal normalization identification is justified from this adversarial packet.

## Assumptions beyond bootstrap

Only standard mathematics: monotonicity of arithmetic-progression containment and Bertrand's postulate. No external literature, source reconciliation, sibling returns, campaign discussion, pull requests, or unpublished GCL material were used.

The historical question of whether Berlekamp's primary-source theorem is the prose formula or the Lean-body formula is deliberately not adjudicated here; that belongs to the source-audit lane.

## Verification / falsification hooks

1. Formally prove monotonicity of the protected `W` from `monoAP_guarantee_set` / `ContainsMonoAPofLength`.
2. Formalize the bounded-gap interpolation lemma for any nondecreasing positive sequence.
3. Instantiate it with prime indices using a formal Bertrand theorem.
4. Under the hypothetical strong bound `p^(2^p) ≤ W(p+1)`, the root-growth theorem should then close mechanically.
5. Under only the actual theorem body, check the explicit sequence `A(k)=k*2^k` for `k≥3`; it falsifies the logical implication from weak prime lower bound plus monotonicity plus divergent successive differences to root-growth divergence.
6. Source audit should resolve the protected prose/body discrepancy before either formula is used downstream.

## Claim boundary

This is not a counterexample to Erdős Problem 138 and makes no claim about the actual asymptotic growth of van der Waerden numbers.

It is a counterexample to a proposed inference from the protected weak prime lower bound (even augmented by monotonicity and difference growth) to the full root-growth limit, and it proves that the prose/body discrepancy changes the mathematical disposition of the problem.

No source provenance, certification, or canonical mutation is claimed.

## Next residual

Resolve the Berlekamp formula in the source-audit lane. If the protected theorem body is source-correct, the root-growth problem remains untouched by that lower bound beyond a constant-scale root lower bound. If the prose formula is source-correct under the exact protected two-color normalization, then the remaining work is the formal monotonicity-plus-Bertrand interpolation, which would prove the registered root-growth statement.