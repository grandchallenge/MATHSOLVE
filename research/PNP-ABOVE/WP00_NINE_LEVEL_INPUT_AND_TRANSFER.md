# PNP-ABOVE WP00 — explicit nine-level input verifier and resource/decision separation

**Disposition:** finite executable interface verified; theorem-derived *conditional* corollary. No compression implementation, numeric constants, new lower bound, or certification.

Parent [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136). Source: Ji–Natarajan–Vidick–Wright–Yuen, *MIP*=RE*, arXiv:2001.04383v4, [PDF](https://arxiv.org/pdf/2001.04383v4), Remark 4.4/Definition 4.5 (printed p.44), Definition 4.14 (pp.49–50), Definitions 5.30–5.33 (p.65), and Theorem 12.1 (p.184).

## Construction

For each integer index n ≥ 1, choose field size q(n)=2, sampler dimension s(n)=9, and the ambient register space W=F₂⁹. On both sides choose the identity conditionally linear function L_A(z)=L_B(z)=z. Realize it as an *explicit nine-level* CL function: its j-th factor subspace is span(e_j), the j-th linear map is the identity on this one-dimensional space, independent of preceding prefixes, and the j-th marginal retains the first j coordinates and zeros the rest. All nine subspaces sum directly to W, and their maps sum to the identity. This is a nine-level realization under Lemma 4.6, not just an assertion that the game has nine questions.

The six-input sampler query semantics of Definition 4.14 are as follows: DIMENSION returns 9; FIELD returns 2; MARGINAL(j,z) returns the first-j-coordinates projection; FACTOR(j,u) returns the indicator e_j for a well-formed prefix u; LINEAR(j,u,y) returns y_j e_j. Verify player labels, j ∈ {1,…,9}, lengths, and prefix format; malformed requests halt with a fixed default result. The Python emulator is a runnable semantic reference, **not** the paper's Gödel-coded Turing machine.

The distribution from Definition 4.5 is uniform on exactly 512 pairs (z,z), one for each z ∈ F₂⁹. Each pair has probability 1/512. The decider D(n,x,y,a,b) accepts exactly when questions x,y have valid nine-bit format and both prover answers a and b are empty strings. Both provers always returning the empty string give a perfect rank-one, projective, consistent, commuting strategy (identity one-outcome measurements).

## Boundedness, with the remaining encoding obligation stated precisely

The sampler and decider are fixed, total finite algorithms; on correctly formatted bounded auxiliary inputs their time is O(log n+1) for index n ≥ 2 under the paper's binary integer convention, and their descriptions have fixed finite lengths. For any specified faithful Turing-machine encoding, a sufficiently large fixed integer λ can dominate those description lengths and both time bounds by n^λ for all n ≥ 2, satisfying Definition 5.32. This proves *existence* of a λ-bounded nine-level representation. It does **not** supply a numerical λ in the paper's actual encoding; no such encoded byte artifact was produced.

The emulator explicitly implements the finite sampler/decider semantics. To make a completely byte-certified theorem input, the next step is to compile it into the source paper's machine format and demonstrate exact step and length bounds, including timeout conventions where relevant.

## Independently executable finite checks

The companion Python file (WP00_NINE_LEVEL_INPUT_EMULATOR.py) exhaustively checks both players and all 512 nine-bit vectors: factor indicators, marginal and linear reconstruction at all nine levels, exact support of 512 diagonal question pairs, perfect acceptance by a fixed classical strategy, and representative malformed queries. Invoke with python3 on the Python file. The observed result is PASS. These checks do not run the source's compressor or certify any quantum complexity theorem.

## Resource-versus-decision corollary, derived from the published theorem

Choose an encoded implementation V of the specified verifier and a sufficiently large fixed λ. For every n ≥ C₀, the source's Theorem 12.1 applies to V and N=2ⁿ. Since V_N has a value-1 PCC strategy, the compressed game G_n=(Compress(V,λ))_n has a value-1 PCC strategy. A **conservative inequality directly supported by the final proof chain** of Theorem 12.1 (page 189) yields the following. Note that the printed *statement* on page 184 places the factor 1/2 inside the maximum and thus has a stronger second branch; Table 2 and the displayed proof conclude only the weaker form recorded here. See WP01's source-discrepancy audit:

$$
\mathcal E(G_n,1/2)
\geq \frac12\max\left\{\mathcal E(V_{2^n},1/2),2^{(2^n)^\lambda-1}\right\}
\geq 2^{2^{\lambda n}-2}.
$$

Here the original game has E(V_N,1/2)=1. The inequality is exclusively about **minimum Schmidt rank of a qualifying entangled strategy**, not deterministic computational time.

Consider the unary-indexed decision language

$$
L_G=\{1^n:\operatorname{val}^*(G_n)=1\}.
$$

All n ≥ C₀ belong to L_G by completeness. Therefore its complement among positive unary indices is finite, making L_G a *cofinite unary language in P*. In the standard existence-based definition of complexity classes, its finite exceptional membership table can be hardcoded. **This does not claim a computed table or numerical C₀.**

Hence the same family of compressed games can have enormous entanglement requirements and yet its associated indexed perfect-value membership predicate is classically easy. This is a theorem-derived elementary counterexample to inferring **decision-time hardness from Schmidt-rank hardness alone**. It does not prohibit more structured uniform SAT-to-strategy-extraction reductions.

## Exact residual and claim firewall

To upgrade the input implementation, compile to the exact machine encoding and produce an auditable λ bound; then implement the source's introspection, answer reduction and repetition transformations with exact universal parameters, or state a constructive-parameter barrier. The choice n=2 used by the emulator is **not** claimed to exceed C₀, and the compressed output is **not** claimed to have been executed.

The next substantive P-vs-NP-facing target must be a nontrivial input verifier with an explicit ordinary classical predicate and a *separately proved* uniform transfer invariant. The existing PNP-001 machine/encoding concordance obligations are unchanged. No proof of P ≠ NP, new circuit lower bound, mathematical certification, or novelty claim is made.
