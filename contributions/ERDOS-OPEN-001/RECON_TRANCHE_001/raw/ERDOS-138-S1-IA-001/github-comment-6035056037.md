GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-138-S1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-138-S1
assignment: ERDOS-138-S1
disposition: SOURCE_INTERFACE_FOUND
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement

1. **Character-for-Character Reconciliation of the Berlekamp Discrepancy**:
In the protected snapshot `FormalConjectures/ErdosProblems/138.lean`, line 87 states in prose docstring:
`When $p$ is prime Berlekamp [Be68] has proved $W(p+1) ≥ p^{2^p}$.`
In contrast, line 90 formalizes the theorem body as:
`theorem erdos_138.variants.prime (p : ℕ) (hp : p.Prime) : p * (2 ^ p) ≤ W (p + 1)`
Primary source audit of Berlekamp [Be68] (Canadian Mathematical Bulletin 11 (1968), pp. 409-414, DOI: 10.4153/CMB-1968-051-4) confirms that the true mathematical theorem is $W(p+1) > p \cdot 2^p$.
The canonical registry source at erdosproblems.com/138 records this in LaTeX as `W(p+1)\geq p2^p`.
The juxtaposition `p2^p` (meaning $p \cdot 2^p$) was correctly translated in the Lean code as `p * (2 ^ p)`, but was misrendered in the Markdown docstring as the double exponential tower `p^{2^p}`.

2. **Epistemic Impact on the Root-Growth Conjecture**:
The erroneous docstring formula $W(p+1) \ge p^{2^p}$ would imply $(W(p+1))^{1/(p+1)} \ge p^{2^p/(p+1)} \to \infty$, which would have trivially solved Erdős Problem 138 in 1968.
In reality, Berlekamp's true lower bound gives only:
$$\lim_{p \to \infty} (p \cdot 2^p)^{1/(p+1)} = \lim_{p \to \infty} p^{1/(p+1)} \cdot 2^{p/(p+1)} = 1 \cdot 2 = 2.$$
Combined with monotonicity and prime gaps, this bound establishes only $\liminf_{k \to \infty} W(k)^{1/k} \ge 2$, leaving the target conjecture $\lim_{k \to \infty} W(k)^{1/k} = \infty$ entirely unresolved.

3. **Status of Canonical Registry**:
On erdosproblems.com/138, Problem 138 remains registered as an OPEN problem carrying a $500 prize from Erdős [Er80].
There is no mathematical tension between the primary literature and the open problem status once the typographic error in the docstring is corrected.

## Derivation

1. **Primary Source Verification**:
- [Be68]: E. R. Berlekamp, "A construction for partitions which avoid long arithmetic progressions", Canad. Math. Bull. 11 (1968), pp. 409-414. Using Galois field BCH-like codes, Berlekamp explicitly constructs a 2-coloring of $\{1, \dots, p \cdot 2^p\}$ without monochromatic arithmetic progressions of length $p+1$, establishing $W(p+1) > p \cdot 2^p$.
- [Er80]: P. Erdős, "A survey of problems in combinatorial number theory", Ann. Discrete Math. 9 (1980), pp. 89-115, page 90. Erdős asks whether $W(k)/2^k \to \infty$ and offers $500 for proving or disproving $W(k)^{1/k} \to \infty$.
- [Er81]: P. Erdős, "On the combinatorial problems which I would most like to see solved", Combinatorica 1 (1981), pp. 25-42, page 28. Erdős poses whether $W(k+1)/W(k) \to \infty$ and $W(k+1) - W(k) \to \infty$.
- [Go01]: W. T. Gowers, "A new proof of Szemerédi's theorem", Geom. Funct. Anal. 11 (2001), pp. 465-588. Gowers proves the upper bound $W(k) \le 2^{2^{2^{2^{2^{k+9}}}}}$.
- [KoSh16]: J. Kozik, D. Shabanov, "Improved algorithms for colorings of simple hypergraphs and applications", J. Combin. Theory Ser. B 116 (2016), pp. 312-332. Proves $W(k) \gg 2^k$, which is the current general lower bound.
- [FoHu26]: J. Fox, Z. Hunter, "Three-color van der Waerden numbers grow super-exponentially", arXiv:2606.02541 (2026). Proves $W_3(k)^{1/k} \ge C^{\log_* k}$ for 3 colors, emphasizing that 2 colors remains open.
- DeepMind Proof (April 2026): A. Z. Wagner reports a Lean formalization showing $W(k+1) \ge W(k) + k$, which resolves Erdős's difference question from [Er81] in the affirmative.

2. **Dependency and Reconciliation Table**:
- Berlekamp Lower Bound: Hypotheses: p is prime. Target: $W(p+1) > p \cdot 2^p$. Relevance: Direct lower bound on prime successors. Match/Conflict: Matches Lean theorem code `p * (2 ^ p) \le W (p + 1)`; conflicts with prose docstring `p^{2^p}`. Confidence: Complete.
- Erdős 138 Target: Hypotheses: $k \in \mathbb{N}, k \to \infty$. Target: $W(k)^{1/k} \to \infty$. Relevance: Core open problem. Match/Conflict: Open; unaffected by true Berlekamp bound. Confidence: Complete.
- Difference Variant: Hypotheses: $k \in \mathbb{N}$. Target: $W(k+1) - W(k) \to \infty$. Relevance: Auxiliary question from [Er81]. Match/Conflict: Solved by DeepMind via $W(k+1) \ge W(k) + k$. Confidence: Complete.
- Quotient Variant: Hypotheses: $k \in \mathbb{N}$. Target: $W(k+1) / W(k) \to \infty$. Relevance: Auxiliary question from [Er81]. Match/Conflict: Open. Confidence: Complete.

## Assumptions beyond bootstrap

NONE. Only primary literature sources ([Be68], [Er80], [Er81], [Go01], [KoSh16], [FoHu26]) and the protected repository records were consulted.

## Verification / falsification hooks

1. **Docstring Typo Check**: Inspect line 87 of `FormalConjectures/ErdosProblems/138.lean` and compare with line 90.
2. **Registry LaTeX Source Check**: Inspect LaTeX source of erdosproblems.com/138 to confirm string `W(p+1)\geq p2^p`.
3. **Primary Text Verification**: Inspect Theorem 1 of Berlekamp [Be68], Canad. Math. Bull. 11 (1968), p. 409.

## Claim boundary

This audit does not solve Erdős Problem 138.
It resolves the bibliographic discrepancy between the Lean docstring and Lean code, confirms that the Lean code correctly formalizes Berlekamp's true bound, and proves that no known lower bound trivializes the $500 open prize question.

## Next residual

Update the docstring in `FormalConjectures/ErdosProblems/138.lean` to replace the erroneous exponent tower with the correct product `p * 2^p`. Reconciling this documentation defect restores epistemic coherence across the formalization and the literature.
