# PNP-ABOVE WP03 — numeric parameter recurrence and executable compiler boundary

**Disposition:** bounded implementation checkpoint, not execution of the upstream Lean transformer or quantum compression pipeline.

**Parent:** MATHSOLVE #1136; predecessor: WP02_LEAN_COMPRESSION_SOURCE_INTERFACE.md.

## Source pin

External repository: vidick/MIPRE-formalization, commit 5926bdff5db621f44682a101007ef2fe3ae8d970. Path MIPRE/Foundations/Pipeline/Compress.lean; blob SHA-1 37023b8d945c57b342bb8b5cf75339beb58b67d8. Relevant declarations: sigmaFun, sigmaFun_zero, sigmaFun_succ, le_sigmaFun. Upstream toolchain is leanprover/lean4:v4.35.0-rc3 with pinned Mathlib and MIPStarRE dependencies.

An exact source tarball was retrieved through the GitHub archive API to a temporary CHAD directory. The available CHAD toolchains at the check were Lean 4.29.1, 4.33.0, 4.33.0-rc1 and 4.34.1; the required v4.35.0-rc3 and packages were not installed. The first standalone Init-only Lean attempt failed because Nat.size was not available in its imports. Subsequent CHAD Bash calls returned internal errors even for a trivial command; the separate service-status call remained healthy. **There is no evidence of a successful upstream Lake build, standalone Lean replay, or actual DecisionCompiler.compute execution.**

## Source numeric recurrence

The upstream function is a polymorphic polynomial-time program constructor with numerical values

$$
\sigma_0(n)=2n+1,\qquad
\sigma_{c+1}(n)=2^{2\,\operatorname{size}(\sigma_c(n))}.
$$

Here size is binary bit length of positive natural numbers. The companion Python code WP03_SIGMA_NUMERICAL.py computes **only the numerical values**, using integer.bit_length. The separate Lean file WP03_SIGMA_NUMERICAL.lean is an Init-only, stand-alone smoke-test *candidate* using an explicit bit-size function, not a claimed execution receipt.

**Proposition (elementary exact closed form).** Put b(n) = size(2n+1). For every c >= 1,

$$
\sigma_c(n)=2^{2^c(b(n)+1)-2}.
$$

**Proof.** For each j let b_j = size(sigma_j(n)). The first power of two is sigma_1(n)=2^(2b_0), whence b_1=2b_0+1. Inductively b_(j+1)=2b_j+1, so b_j=2^j(b_0+1)-1. Substitution gives the displayed formula for c >= 1. QED.

For each **fixed** c the numerical function grows polynomially in n, with degree 2^c up to multiplicative constants; it is not uniformly a low-degree polynomial in c. The exact closed form does not select the source's noncomputably chosen Csig or any of the soundness constants.

## Numerical replay evidence

An independent local Python implementation checked:
- 320 exact recurrence-versus-closed-form cases with 0 <= c < 8 and 0 <= n < 40: PASS.
- 126 sampled inequalities c(n+1)^c <= sigma_c(n) with 0 <= c < 6, 0 <= n < 21: PASS. This is a sample check, **not** an independent proof of the upstream universal le_sigmaFun.
- For n=3 and c=0,1,2,3,4,5: 7, 64, 16384, 1073741824, 4611686018427387904, 85070591730234615865843651857942052864.

The Python script is an exact finite arithmetic test of the recurrence; it is not a source Prog object or quantum compressor. The stand-alone Lean candidate is stored without claiming that it has compiled.

## Next actual compressor gate

1. Install exact upstream Lean 4.35.0-rc3 and pinned dependencies in an isolated work directory; replay its Lake build and verify commit/toolchain evidence.
2. Encode the protected nine-level finite input verifier in the formalization's actual Prog representation, including the six-input sampler/decider semantics, malformed inputs, and explicit time/length bounds.
3. Identify constructive numerical parameter witnesses for the first compiler stage or explicitly prove they are unavailable from the current source constants.
4. Run the *actual* upstream DecisionCompiler.compute and execute the emitted program on specified inputs. Record exact inputs, output bytes, traces and comparator checks.
5. Then separately address answer reduction, repetition and nine-level source-concordance. A parameter subroutine is not a full MIP*=RE compression implementation.

**Research claim status unchanged:** no unrestricted classical lower bound, no new SAT transfer theorem, no P versus NP resolution, no mathematical certification.
