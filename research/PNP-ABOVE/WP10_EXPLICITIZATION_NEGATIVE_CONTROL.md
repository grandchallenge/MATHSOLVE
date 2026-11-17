# PNP-ABOVE — exact one-hot explicitization negative control

**Evidence grade:** CAL (elementary proof plus reproducible finite tests). **Scope:** one fixed SAT compilation scheme, not arbitrary succinct encodings. **Parent:** [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136). **Upstream classical transfer:** [WP01](WP01_EXPLICIT_CLASSICAL_TRANSFER_AND_SOURCE_AUDIT.md).

## Proposition (output-size cost of the specified compiler)

For each positive integer `m`, define a succinctly generated two-prover game `H_m` with question sets `X_m=Y_m={0,1}^m`, single answer alphabet `A_m=B_m={empty}`, and support the diagonal pairs `(z,z)`, sampled by uniformly choosing `m` bits. All supported pairs with empty answers win.

The constant answer functions `f_m(x)=empty` and `g_m(y)=empty` form a perfect deterministic local strategy. The family has a uniform sampler and acceptance predicate using `m`-bit operations. Its perfect-value indexed membership language is trivial.

Apply the **particular explicit-table one-hot strategy-to-CNF compiler of WP01**, which introduces one Boolean variable per player/question/possible-answer tuple, includes an at-least-one-answer clause per player/question, pairwise exclusion clauses, and a losing-pair clause for each supported disallowed response.

There are exactly `2^m` questions for each player and one answer for each. Thus its variable count is

$$
M(m)=|X_m||A_m|+|Y_m||B_m|=2^{m+1}.
$$

Since the unique answer is legal on every supported pair, the compiler introduces precisely one positive unit clause per question on each side, no pairwise exclusions, and no losing-answer clauses. **Its output therefore contains exactly `2^{m+1}` variables and `2^{m+1}` unit clauses.** The all-true assignment satisfies the formula.

The output-size lower bound is sharp for this **fixed expansion procedure**. It is not a lower bound on alternative succinct SAT encodings or on circuits representing the winning strategy: the winning strategy is constant-size. Any assumed polynomial-time SAT procedure applied *after* this explicit expansion runs polynomially in a formula whose size is exponential in `m`, so this particular reduction does not supply a polynomial-`m) uniform strategy extractor.

This family is a source-independent negative control. At `m=9`, it shares the diagonal 512-pair support pattern of WP00's toy input, but the varying-`m` game is **not** certified as a nine-level, `λ`-bounded input verifier for the MIP*=RE compressor.

## Independent finite test

[WP10_EXPLICITIZATION_NEGATIVE_CONTROL.py](WP10_EXPLICITIZATION_NEGATIVE_CONTROL.py) constructs the one-hot clauses, verifies their exact counts, evaluates the constant strategy on every supported pair, and rejects representative invalid answers and off-support pairs for `m=1,...,10`. It uses Python's standard library only.

- Source SHA-256: `5d6be837f8e3d183d2126b3b874458cf35f8aeda7bf0c564c068b80f985f9a2b`.
- Exact command: `python3 research/PNP-ABOVE/WP10_EXPLICITIZATION_NEGATIVE_CONTROL.py --max-m 10`.
- Result: process exit 0, final `PASS: exact one-hot CNF size and uniform winning strategy`.
- At `m=9`: 512 supported pairs, 1,024 variables/clauses. At `m=10`: 1,024 supported pairs, 2,048 variables/clauses.
- CHAD execution capture `8270831865834b55b7649d04a5e067c0`, local OS evidence, not mathematical certification.

## Research consequence and limits

The WP01 SAT self-reduction is valid for **explicit** game tables. For a succinct verifier, converting it into that table is a separately costed step. A future SAT-to-classical-realization theorem must avoid or justify this expansion and precisely bind the representation and output cost of its strategy extraction. The quantum Schmidt-rank invariant from MIP*=RE does not supply that missing implication.

This is an elementary counterexample to a proposed compiler's *efficiency*, not a new circuit lower bound, not a P-versus-NP result, and not a general impossibility theorem for succinct SAT-to-strategy reductions. The parent PNP-001 Formal Conjectures concordance and all substantive PNP-ABOVE transfer obligations remain open.
