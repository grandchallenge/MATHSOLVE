# PNP-ABOVE WP03: Lean parameter recurrence execution receipt

**Status:** bounded numerical compiler-parameter slice executed and replayed; not a full implementation of the MIP*=RE compressor and not mathematical certification.

## Source lock and semantics

Upstream: vidick/MIPRE-formalization, commit 5926bdff5db621f44682a101007ef2fe3ae8d970. File: [MIPRE/Foundations/Pipeline/Compress.lean](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/MIPRE/Foundations/Pipeline/Compress.lean), Git blob SHA-1 37023b8d945c57b342bb8b5cf75339beb58b67d8. Upstream archive was acquired by commit-specific GitHub tarball after direct Git clone failed; archive SHA-256: 312b3900ed437f651a8b51e4e8c7d66b2b87545fa44261e83c083917ec1f9842. Upstream requires Lean 4.35.0-rc3 and locked external dependencies, which have NOT yet been installed or built here.

The upstream numerical recurrence is

$$
\sigma_0(n)=2n+1,\qquad
\sigma_{c+1}(n)=2^{2\,\mathrm{size}(\sigma_c(n))}.
$$

Its upstream construction additionally supplies a certified PolyTimeFun program. The standalone Lean test implements only the natural-number value recursion, using the bit-length formula floor(log2 x)+1 for positive x in place of Nat.size. Every recurrence output is positive. No kernel-checked cross-project equivalence theorem for the upstream PolyTimeFun object has been produced.

## Exact tested artifact

Code: [WP03_ParameterRecurrence.lean](WP03_ParameterRecurrence.lean). SHA-256: 540f7c27755c2b74c3b5f2b5001134fca65c634962dc9cb82ea93b5ff651b380. The GitHub branch artifact was fetched back and compared byte-for-byte to the local tested file; both hashes match.

Command: execute the file with standalone Lean 4.34.1, using the absolute Lean binary rather than an environment-selected wrapper. This test imports Init only and does not build upstream MIPRE.

Result: exit code 0, without Lean errors. Values at n=3 were:

| c | sigmaValue(c,3) |
|---:|---:|
| 0 | 7 |
| 1 | 64 |
| 2 | 16384 |
| 3 | 1073741824 |
| 4 | 4611686018427387904 |

Four fixed-value guards passed. A further table guard verified 126 finite inequalities

$$
c(n+1)^c\le \sigma_c(n) \quad (0\le c\le 5,\;0\le n\le20).
$$

This is finite exhaustive evaluation of the declared table, NOT an asymptotic or universal proof of the upstream bound.

Execution receipt: GCL_CONTROL_BASH_RESULT/1 run ID 2d88a9f1292d4e29874f167afdbbadfa; output SHA-256 d1409fd33334441b9394612568137278fe6efef32ec53ad7f8f31bb2a78ee586. The local OS execution is not independently authenticated as a separate mathematical verification.

Earlier unsuccessful tests (Nat.size unavailable in Init; malformed adjacent comment) were corrected before the final clean replay. They are not acceptance evidence.

## Next genuine gates

1. Reproduce upstream Lean 4.35.0-rc3 toolchain and exact Mathlib/MIPStarRE dependencies and run the upstream build/comparator, with resource budgets.
2. Encode the nine-level identity verifier as faithful source Prog objects with explicit interpreter steps, malformed-input and timeout semantics.
3. Instantiate DecisionCompiler.compute with concrete program metadata and independently justified parameter witnesses. A standalone sigmaValue evaluation is not this compiler.
4. Reconcile upstream seven-level stage contracts against the v4 paper's nine-level normal form and verify a literal compression transformation before numerical or quantum-resource claims.

No full introspection, answer reduction, repetition, executable compressed game, new classical lower bound, SAT-to-quantum transfer, or P-vs-NP claim is asserted.
