# PNP-ABOVE WP00 — source extraction: gap-preserving compression theorem

Status: source-extraction candidate; **not** a new theorem, not an explicit executable finite-game instance, and not P vs NP progress by itself.

Parent: [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136). Predecessor calibration: [PR #1137](https://github.com/grandchallenge/MATHSOLVE/pull/1137).

## Primary source identity

Ji, Natarajan, Vidick, Wright and Yuen, *MIP*=RE*, arXiv:2001.04383v4, dated 16 October 2026; https://arxiv.org/abs/2001.04383 ; PDF https://arxiv.org/pdf/2001.04383 . Source section 12, “Gap-preserving compression,” Theorem 12.1, Figure 15, Lemma 12.2. Version/date confirmed on arXiv abstract. Exact downloaded PDF checksum and archival source blob **not yet obtained**: source citation is a version lock, not a byte-level lock.

## The theorem interface to inspect

Input: a pair of Turing machines V=(S,D) implementing a verifier, and a positive integer bound parameter lambda. A polynomial-time machine Compress(V,lambda) returns a **9-level normal form verifier** V_compr with a standard timeout-counter decider.

Its sampler and decider run in time poly(n,lambda) at index n, and the constructed sampler does not depend on V, only lambda. The sampler's description is constructible from the binary encoding of lambda in polylog(lambda) time; do not confuse this property with polynomial-time generation of a winning prover strategy.

Completeness/soundness require that the input V itself be **lambda-bounded and 9-level normal form**, where lambda bounds its description lengths and the time of sampler/decider by n^lambda for n >= 2. For sufficiently large n (n >= universal C0), with N=2^n:

1. If V_N has a value-1 PCC strategy, compressed (V_compr)_n has a value-1 PCC strategy.
2. Its soundness is stated in the source through the quantity E(game,1/2), with a bound comparing E((V_compr)_n,1/2) against E(V_N,1/2) and a second exponentially tiny term. **Before using this inequality, import and check the exact source definition of E and the bound's exponent and quantifier conventions**; no informal reinterpretation as a bound on classical value is allowed.

These conditions are essential and are *not* guaranteed for an arbitrary SAT instance or finite game.

## Exact construction chain from Figure 15

- Step 1: ComputeIntroVerifier(V,lambda,9).
- Step 2: ComputeAnsRedVerifier(previous,lambda,mu,sigma(lambda)).
- Step 3: ComputeRepeatedVerifier(previous,lambda,tau).
- Return the resulting normal-form verifier.

Here mu,tau are universal constants in the theorem proof, and sigma(lambda) is selected by the source. Their precise definitions/parameter constraints are a pending line-by-line audit; do not fill with guessed constants.

## New boundary learned

The theorem compresses the **verifier description and its indexed computational resources**, while carrying perfect *PCC* strategy existence and a quantified entangled-strategy soundness measure. It does NOT show that:
- a classical game strategy can be constructed cheaply;
- the compressed game has a classical circuit lower bound;
- entanglement dimension is a classical decision-time lower bound;
- a SAT solver directly implements the compressed strategy.

Moreover, the n-to-2^n parameter reduction is not automatically a polynomial-time reduction on ordinary *explicitly expanded instances*; succinct representations, uniformity and decoding cost must be kept distinct.

## Exact next bounded lemma (not proved)

Select one explicit lambda-bounded 9-level normal-form verifier V from the paper, identify its sampler/decider machines and concrete input index n >= C0, and make the finite verifier/game representation reproducible. Record question/answer distributions, verifier execution cost, source constants or symbolic bounds and the interpretation of E. Then ask whether a hypothetical polynomial-time SAT algorithm implies a polynomial classical implementation of the compressed game's required strategy or only polynomial evaluation of an encoded decider. If no reduction exists, record an explicit failed premise, not a lower-bound theorem.

## Claims and status

- Theorem 12.1 is attributed to its authors, not claimed as a GCL result.
- This is a *source-normalized interface sketch*. A fully parameterized finite family with executable instances, a byte-level source lock, independent exact verification and classical transfer **remain open**.
- PNP-001's existing Formal Conjectures machine/encoding concordance obligation is unchanged.
