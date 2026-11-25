# PNP-ABOVE-WP01 — explicit classical transfer, sampler-resource lower bound, and source audit

**Status:** bounded proof-and-code candidate, not mathematically certified, not a full implementation of the published quantum compressor, and not a new P-vs-NP theorem.  
**Parent:** [PNP-ABOVE-WP00, MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136).  
**Primary source:** Ji–Natarajan–Vidick–Wright–Yuen, [MIP*=RE, arXiv:2001.04383v4](https://arxiv.org/pdf/2001.04383v4), 16 October 2026; printed pages 25, 49–50, 184–189, specifically Definition 4.14, Definition 5.32, Theorem 12.1, Figure 15, Table 2, equations (182)–(192).

## 1. Source discrepancy: stronger theorem statement, weaker final proof chain

The **printed statement** of Theorem 12.1, page 184, reads:

$$
\mathcal E(V_n^{\mathrm{compr}},1/2)
\geq\max\left\{\frac12\mathcal E(V_N,1/2),\,2^{N^\lambda-1}\right\},
\qquad N=2^n.
$$

However **Table 2** (p. 186) and the **final displayed proof chain** (p. 189) show:

$$
\mathcal E(V_n^{(3)},1/2)
\geq\mathcal E(V_n^{(2)},1-\epsilon_2)
\geq\frac12\mathcal E(V_n^{(1)},1-\epsilon_1)
\geq\frac12\max\left\{\mathcal E(V_N,1/2),\,2^{N^\lambda-1}\right\}.
$$

The proof-backed inequality is weaker by a factor of two **in the second maximum branch**. The prior GCL ledger called the proof-backed bound an *exact theorem transcription*; that wording was inaccurate. Conversely, silently replacing the proof-backed estimate by the stronger statement would conceal the displayed proof gap. Preserve both readings, do not infer that the paper is otherwise invalid, and seek source-author/independent mathematical reconciliation before relying on the stronger term. The still-correct conservative consequence is

$$
\mathcal E(V_n^{\mathrm{compr}},1/2)\geq 2^{2^{\lambda n}-2}
$$

under the theorem's input conditions. This is a lower bound on Schmidt rank, **not** deterministic time.

## 2. Explicit implementation boundary

Figure 15 of the primary source constructs the 9-level output verifier by (i) ComputeIntroVerifier, (ii) ComputeAnsRedVerifier, and (iii) ComputeRepeatedVerifier. These employ quantum introspection and a specially designed PCP/answer reduction, with existential universal constants. **None of these three source transformations has been implemented or executed by GCL WP01.** Calling a simple CNF conversion 'the MIP* compressor' would be false.

The companion preflight code implements exactly **the source's tuple bit encoding** from Section 3.1: component bit 0 maps to 00, bit 1 to 01, and 10 ends each component. It includes a round-trip decoder which treats encoding as *two-bit tokens*, preventing delimiter confusion across data-bit boundaries; an exhaustive family of valid tuples and malformed instances is checked. For an arity-k tuple of total data length L, the encoding has length exactly 2(L+k). This settles a narrow, source-faithful *input-encoding subroutine*, not the paper's Turing-machine *transition table*, exact machine-description length, timeout schedule, or construction of a numerical lambda/C0.

The nine-level finite identity sampler remains executable in the [protected prior emulator](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/PNP-ABOVE/WP00_NINE_LEVEL_INPUT_EMULATOR.py). It generates 512 diagonal input pairs and checks nine prefix levels. It does not generate the corresponding *compressed* verifier.

## 3. Sharp classical verifier-side randomness lower bound

**Proposition (uniform sampler support obstruction).** Let m be a positive integer and let a classical sampler produce one m-bit output with a fixed deterministic function of at most r independent fair random bits, with no other random source. Its output distribution P satisfies

$$
d_{\mathrm{TV}}(P,U_m)\geq 1-\frac{2^r}{2^m}\qquad(0\leq r\leq m).
$$

In particular, exact sampling of U_m requires at least m random bits. For r<m, the inequality is sharp, achieved by outputting an injective r-bit seed padded with m-r zero bits.

**Proof.** At most 2^r seed strings exist, so P has support S of size at most 2^r. The event of falling outside S has probability zero under P and probability 1-|S|/2^m under U_m. Total variation is at least the difference for this event, proving the bound. For an injective map of seeds into outputs, P is uniform on exactly 2^r outputs, so its total variation from U_m equals 1-2^{r-m}. QED.

For the **uncompressed** F2^9 diagonal identity sampler, this shows that a classical verifier required to output exactly uniform z itself needs at least nine fair random bits. With only eight, total variation is at least 1/2; with seven, 3/4; with zero, 511/512. The preflight enumerates all 54 cases (m=1..9, r=0..m) and checks exact rational TV.

**Boundary:** this is a classical *local output-sampling* lower bound, not an NP lower bound and not a lower bound on the referee's coins in a quantum introspection game. The published quantum construction delegates enormous randomness and certifies constraints through interactive tests. If shared prover randomness, interaction, computational assumptions, or approximate distributions are changed, the model and the inference change. It is not novel information-theoretic mathematics.

## 4. Explicit-table SAT transfer theorem

Let G=(X,Y,A,B,supp,D) be a finite two-player game with finite, explicitly listed question/answer alphabets, positive-probability question pairs supp, and an explicit acceptance table D. Consider **deterministic local strategies without post-question communication**: a function f:X->A for Alice and g:Y->B for Bob.

Introduce a Boolean variable z(P,q,a) for each player P, corresponding question q and possible answer a. For every (P,q), require exactly one answer by the one-hot CNF clauses (one positive disjunction and all pairwise exclusion clauses). For every (x,y) in supp and every (a,b) with D(x,y,a,b)=0, include the clause

$$
\neg z(A,x,a)\ \lor\ \neg z(B,y,b).
$$

**Proposition (explicit SAT strategy compiler).** The resulting CNF F_G is satisfiable **iff** G admits a perfect deterministic local strategy. It has

$$
M=|X||A|+|Y||B|
$$

variables and at most

$$
|X|(1+\tbinom{|A|}{2})+|Y|(1+\tbinom{|B|}{2})
+|\mathrm{supp}|\,|A|\,|B|
$$

clauses. The compiler runs in polynomial time in the **explicit-table** input size.

**Proof.** Any satisfying assignment selects one answer per player/question. The losing-pair clauses prohibit every disallowed joint response on each supported pair, so the selected tables win perfectly. Conversely, a perfect deterministic strategy selects one variable per question and satisfies each losing-pair clause. Clause enumeration is polynomial in the declared explicit table. QED.

**Corollary (genuine, restricted SAT transfer).** If SAT is decidable in polynomial time, there is a polynomial-time algorithm that, given a finite explicit-table game G, either reports that no perfect deterministic local strategy exists or outputs such a strategy. Decide F_G, then fix each of its M variables sequentially by querying satisfiability under the current prefix and a proposed zero bit. At most M+1 calls to a polynomial-time SAT decider, plus polynomial decoding overhead, suffice. The companion code includes a small DPLL solver as a test oracle; DPLL is **not** polynomial-time in general.

**False extrapolation.** This does *not* show that SAT in P yields a polynomial-Schmidt-rank *quantum* winning strategy, or that it yields a perfect classical strategy when only an entangled one exists. The magic square has an entangled perfect strategy and **unsatisfiable** F_G for classical local strategies. Nor is the explicit table necessarily polynomial in the size of a *succinct* compressed verifier: the table may be exponentially large in its short description.

This establishes an actual restricted SAT-to-classical-strategy transfer, and isolates the first still-missing bridge: a **uniform, polynomial-size explicitization or different succinct encoding** plus a sound strategy-extraction interface for the *relevant* classical invariant. Neither is provided by Theorem 12.1.

## 5. Reproducible finite tests

Run both companion Python files with Python 3, no external packages:

- WP01_COMPRESSION_PREFLIGHT.py: tuple encoding PASS; 54 exact finite randomness cases; nine-bit lower-bound values 1/2, 3/4, 511/512.
- WP01_EXPLICIT_GAME_SAT_TRANSFER.py: satisfiable explicit test (8 variables, 20 clauses, 9 self-reduction queries); magic square (48 variables, 678 clauses, **UNSAT** under local deterministic strategies, witnessed classical winning fraction 8/9); prior nine-level identity game (512 supported question pairs, 1,024 variables, 1,024 clauses, SAT). A structural negative test guards against treating the code as full MIP* compressor.

The SAT solver in the test is a finite DPLL procedure. Passing finite tests is not a proof of worst-case polynomial SAT solving.

## 6. Next genuine mathematical/implementation gates

1. Produce **explicit source-faithful Turing-machine transition descriptions**, including Section 3.1 tuple encoding, sampler query parser, malformed-input behavior, timeout-counter representation, and quantified description/step counts for the nine-level input.
2. Implement or formally translate each published Figure 15 transformer, beginning with the **introspection** transformation. Record the exact quantum test, conditional-linear question distribution and its sampler, or document the smallest external implementation dependency. Do not use a classical surrogate under the same name.
3. Determine effective source constants for lambda, mu, sigma, tau and C0 before claiming a finite compressed game at a particular index.
4. Seek a **succinct** classical realization invariant and its genuine cost lower bound, with a uniform encoding of exponential-scale data rather than expanding an enormous game table.
5. Repair the theorem statement/proof transcription discrepancy at the source-semantic level and update the protected Programme/MkDocs projection. The original PNP Formal Conjectures definition concordance remains open.

**Claim boundary:** elementary propositions above are bounded, with proofs and finite tests; no novelty assertion, mathematical certification, unrestricted circuit lower bound, full compression implementation, SAT transfer to quantum strategies, or P versus NP result.
