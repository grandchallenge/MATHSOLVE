# PNP-ABOVE-WP00 — exact entanglement-resource audit and classical transfer obstruction

**Status:** source-checked technical correction / bounded finding; not a new circuit lower bound, not an executable compressed game, and not mathematical certification.  
**Parent:** [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136).  
**Preceding candidate:** [PR #1140](https://github.com/grandchallenge/MATHSOLVE/pull/1140).

## Source and theorem locus

Ji–Natarajan–Vidick–Wright–Yuen, *MIP*=RE*, arXiv:2001.04383v4 (16 October 2026), PDF pages labelled 54 (Definition 5.12), 184 (Theorem 12.1), 185 (Figure 15/Lemma 12.2), 186 (Table 2), 189 (end of proof). Stable version URL: https://arxiv.org/pdf/2001.04383v4. This is a *version-and-locus* lock, not yet a downloaded PDF checksum or local source archive.

## Exact interpretation of E

Definition 5.12 specifies E(G,nu) as the **minimum positive integer Schmidt rank** of a shared bipartite state supporting *some finite-dimensional tensor-product strategy* with success probability at least nu. If there is no such strategy, E(G,nu) = infinity. In particular, E is **not**:
- the length of a Boolean witness or a proof;
- Turing-machine time complexity or Boolean circuit size;
- communication complexity;
- a lower bound on the computational complexity of determining whether val*(G) exceeds a threshold.

Theorem 12.1, for lambda-bounded, 9-level normal-form input verifier V and n >= universal C0 with N=2^n, preserves the existence of a perfect PCC strategy and provides a quantitative lower bound on E((Compress(V,lambda))_n, 1/2) in terms of E(V_N,1/2), n and a large n/lambda-dependent term. Any reproduction of the exact exponent must be checked against the typeset equation (the PDF text extraction loses superscript grouping). The compressor's sampler and decider each run in poly(n,lambda); this is about **verifier** computation, not a prover strategy construction. Figure 15 explicitly composes introspection, answer reduction, and parallel repetition.

## Rigorous no-automatic-transfer lemma

**Lemma (separation of resource semantics).** A lower bound on the minimum entangled-strategy Schmidt rank E(G,nu), even one superpolynomial in the size of a succinct game description, does not alone supply a superpolynomial decision-time lower bound for the yes/no language L={(description of G): val*(G)>=nu} or for SAT.

**Reason:** Definition 5.12 places a constraint on *witnessing strategy resources*, not on the computational cost of determining the truth of membership. A decision algorithm is not required to output a strategy, a state, or its Schmidt-rank realization. An additional reduction must show that a hypothetical efficient decider *uniformly constructs* an object contradicting the strategy-rank lower bound. No such reduction is part of Theorem 12.1. This is an interface non-implication, not a proof that all possible reductions fail.

A particularly elementary stress test is the family H_d of threshold questions over a fully **fixed** game G of arbitrarily large finite entanglement requirements (if available): recognizing its fixed membership truth remains constant-time after hardcoding one bit, even though constructing a suitable strategy may be costly. A finite counterexample with a known explicit high-dimensional game is useful but not required for the semantic lemma; a fixed decision predicate does not force a strategy witness. Do not present this thought experiment as a uniform complexity separation.

## Parameter identity and proof-boundary audit

1. `n` indexes the compressed game; `N=2^n` indexes the input game, and its explicit expanded representation may be exponentially larger than the succinct verifier description.
2. `lambda` bounds description lengths and sampler/decider running time `<=n^lambda` for the **input** verifier; it does not automatically bound strategy resources.
3. The input must be 9-level normal form and lambda-bounded for Theorem 12.1's completeness/soundness conclusions; the compression construction exists for arbitrary machine pairs, but those conclusions do not automatically apply.
4. The Figure 15 staging is **introspection → answer reduction → repeated anchored verifier**. Table 2 reports respectively levels 5, 7, and 9, and the final sampler/decider complexity poly(n,lambda).
5. The proof's constants C0, mu, tau, sigma(lambda), and the exact formula for the entanglement-growth exponent must be archived from the typeset paper before executable parameter instantiation. Universal constants need not be numerically specified by the theorem and are not permission to invent numerical values.
6. No implication from `P=NP` to `E(G_n,1/2) <= poly(n)` has been constructed. This is the central open bridge.

## Next bounded obligation

Prepare a *symbolic* transformation ledger that binds each Figure 15 stage to exact definitions/equation references and captures the typeset soundness inequality correctly. Then select an actual 9-level lambda-bounded input verifier with a fully recorded machine encoding, timeout behavior and universal-constant dependencies. Do not claim an executable `n >= C0` finite instance until the source constructions and constants permit one.

An alternate mathematically productive target is to prove a **restricted model** impossibility of a specific proposed *strategy-extracting* SAT reduction. This must be stated with uniformity, oracle access and output requirements and may reveal which extra assumptions are missing.

## Claim boundary

Source interpretation and missing-lemma audit only. No P-vs-NP implication, no new lower bound, no certified novelty, no protected PNP-001 status change. The pending original PNP machine/encoding concordance audit remains a prerequisite for later unrestricted claims.
