# PNP-ABOVE WP33: formal refutation of unconditional native witness-budget transfer

**Status:** original-source Lean theorem candidate; local original kernel compile PASSED. Protected admission requires exact uncached source replay, kernel axiom audit, protected CI, logical adversarial review, merge/readback. Parent: `MATHSOLVE/main@46ec251d240066ea2abef652a35c42a8069953f4` (WP32 protected). Upstream: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`; Lean `v4.35.0-rc3`.

## Negative theorem, scoped exactly

WP32 removes the fixed compressor threshold `G.C₀ ≤ k` with a single original-source polynomial padding program. Its genuine compression completeness and classical-SAT reduction still require `m ≤ (2^k)^lam`, where `m` is the ambient `Fin m` variable cardinality and the actual source index `k` depends ONLY on `fromOriginal3CNF cs`, the list of encoded clauses. The `Fin m` cardinality itself is not retained in that encoded clause list.

WP33 uses the **nonempty, satisfiable original finite 3CNF** consisting of the single clause `(x₀ ∨ x₀ ∨ x₀)`, with ambient type `Fin (n+1)`. The clause depends only on variable zero and its original `MIPRE.SAT` source encoding is exactly `[((0,true),(0,true),(0,true))]` for every `n`. The original MIPRE satisfiability predicate has the all-true witness.

For EVERY `index : WP29.Enc3CNF → Nat` and EVERY exponent `lam : Nat`, let `K = (2 ^ index [((0,true),(0,true),(0,true))]) ^ lam` and choose `n=K`. Then the actual ambient cardinality is `m=K+1`, while the encoded source instance and index do not change. Therefore `m > (2^k)^lam`. This is a genuine quantified counterexample, not an empirical size extrapolation and not restricted to the WP29 serializer.

The resulting actual-original-source theorems in `WP33_AmbientBudgetBarrier.lean` are:

1. `repeatedZeroClause_encoded`: exact original `SAT.Clause3 (Fin (n+1))` to encoded-list equality, for every `n`.
2. `repeatedZeroClause_satisfiable`: all-true assignment is an actual original `Cnf3.Sat` witness.
3. `no_uniform_budget_nonempty`: generic quantifier over **all** encoded-list-only numeric index functions and exponents.
4. `native_compiled_index_invariant` and `native_index_budget_not_uniform`: specialize to the **actual original** source-polynomial `WP29.source3CNFIndexProgram`.
5. `normalized_index_budget_not_uniform`: specialize to the **actual WP32 source-polynomial** `normalizedIndexProgram G.C₀`, for every original `MIPRE.GapCompression G` and exponent.
6. `threshold_holds_while_budget_fails`: for every `G,lam`, a native SAT instance exists with **proved** `G.C₀ ≤ k` but **refuted** `m ≤ (2^k)^lam` at the same index. The two premises are logically independent.

## Consequence

**Refuted route:** One cannot discharge WP32's original `m ≤ (2^k)^lam` premise *for all arbitrary native `List (Clause3 (Fin m))`* merely from source polynomial-time compilation, from the native compression threshold theorem, or from ANY encoding of the clause list alone that ignores ambient unused variables.

**NOT refuted:** Original `GapCompression` completeness/soundness; WP29–WP32 conditional SAT reductions; dense/normalized finite-variable SAT; possible efficient succinct-game evaluation; or any P-vs-NP proposition. The counterexample attacks one invalid way of removing a hypothesis, not quantum compression itself.

**Next positive interface:** Produce a source-native, uniformly polynomial **support-densifier**: construct an equivalent explicitly encoded 3CNF whose variable set is exactly its active support (at most three per clause), prove SAT and native verifier equivalence, account for numerical identifier size, and show the *actual normalized* ambient cardinality satisfies the source `(2^k)^lam` budget. `lam=0` must be treated explicitly; an increase of boundedness exponent requires its own legal native monotonicity proof or suitable source construction. Prove genuine `Cost.PolyTimeFun` execution and full raw-input cost, not only a Lean function.

**Separate fundamental barrier:** Even a completed normalizer and fully polynomial input-to-index reduction would yield a conditional NP-hardness statement for a *succinct compressed-game value-promise problem*, not a deterministic classical complexity lower bound. A lower-bound mechanism must still show that every proposed classical SAT solver would require superpolynomial resources. Upstream `GapCompression` gives no such result on its own.

**Disposition:** `PNP_WP33_NATIVE_UNIFORM_WITNESS_BUDGET_REFUTED_FOR_UNNORMALIZED_FIN_m__DENSIFICATION_AND_CLASSICAL_LOWER_BOUND_OPEN`. No `P=NP`, `P≠NP`, MATHCERT certification or novelty claim.
