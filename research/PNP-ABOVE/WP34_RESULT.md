# PNP-ABOVE WP34: canonical scope and exact classical promise equivalence

Original source: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`; Lean v4.35.0-rc3. Parent: `935a2e59d13bfb39487b166e187e38e794b913f9`, containing WP33 #1285. Candidate admission requires fresh WP08–WP34 source replay, exact locks, standard kernel axiom audit, protected checks, merge and readback.

## Canonical normalization

For an original `SAT.Fml`, define `scope f = 0` if no variables occur, otherwise maximum occurring numerical identifier plus one. `scope_le_iff` proves for every f,m that `scope f ≤ m ↔ f.InputsLt m`. This is the least sufficient initial segment; unlike the ambient m in WP33 it depends on the formula. Padding by true conjuncts leaves it unchanged.

`scopeProgram : Cost.PolyTimeFun Fml Nat` is an actual original source program scanning the RPN serialization, with original casesNode, binary successor and comparison. Accumulator encoded growth is at most `esize s + esize nd + 4`, so the original additive fold supplies the polynomial run certificate. Exact semantics and original Prog.Runs bounds are proved. `normalizeProgram r : PolyTimeFun Enc3CNF (Fml × Nat)` composes WP29 compilation, WP32 padding, and scope computation. The normalized pair has sufficient scope and preserves SAT for every original finite 3CNF, including arbitrary unused Fin variables.

This is **initial-segment** normalization, not dense relabeling. Gaps between active identifiers may remain. The binary scope representation and computation are polynomial in source length; numerical scope may be exponential. No polynomial full-witness length conclusion is inferred.

## Native budget closure

Induction on the actual original source formula gives `scope f ≤ 2^(esize f)`. WP28B2 proves `2^(esize f) ≤ formulaIndex f`. Hence scope ≤ k. Original `Verifier.IsBounded.two_le` supplies 2 ≤ lam. Thus `scope f ≤ k ≤ 2^k ≤ (2^k)^lam`. `canonical_budget` and `normalized_pair_budget` establish the exact required budget, by changing the witness scope, not claiming WP33's false ambient bound.

`canonical_compressed_yes/no` apply original GapCompression for every valid formula index above C₀ without an external witness budget. `canonical_pcc_iff_sat` and `canonical_gap_iff_unsat` establish perfect PCC iff SAT and tensor value ≤1/2 iff UNSAT there. WP32 supplies threshold by padding. `budget_free_classical_transfer` and `valid_promise_classical_transfer` prove the original polynomial classical composition decides every original finite 3CNF conditional on an original polynomial source promise solver and native boundedness (whose existence for fixed U,G was established in WP28C). The latter needs correctness only at valid formula indices.

## Exact lower-bound frontier

For fixed G,U,lam satisfying original boundedness, define SolvesValidPromise as correctness at valid original formula indices k≥G.C₀ for perfect PCC versus tensor value ≤1/2, at the exact original budget. SolvesFormulaDataSAT means correctness on every valid original encoded formula.

`valid_promise_polytime_iff_formula_SAT` proves:

```
(∃ oracle : PolyTimeFun Nat Bool, SolvesValidPromise G U lam oracle) ↔
(∃ satSolver : PolyTimeFun Data Bool, SolvesFormulaDataSAT satSolver)
```

Reverse: compose the actual original polynomial source decoder with the SAT solver. No expanded game simulation. Forward: compose the original index encoder with the valid-index solver; handle the fixed finitely many indices below G.C₀ by a finite-table original source program using binary comparisons. The labels are mathematical truth values for the finite exception set. This is a fixed-code existence construction for each fixed threshold, not a uniform algorithm computing all SAT labels or polynomial in varying G.C₀. Injectivity ensures uniqueness of the decoded formula on valid indices. Both compositions are actual original PolyTimeFun objects.

`valid_promise_lower_bound_iff_formula_SAT` proves the negation equivalence: excluding every polynomial classical solver on this restricted valid-index promise is exactly as strong as excluding every polynomial solver for encoded-formula SAT in the pinned source machine model. Compression does not supply this exclusion. A lower bound on a larger arbitrary-index family, expanded game size, or quantum dimension does not imply a lower bound on the restricted succinct input family.

No identification of original Cost.Prog with all standard deterministic TM models is claimed; PNP-BRIDGE remains separate. No polynomial expanded-game construction, P=NP, P≠NP, novelty, or external MATHCERT certification is asserted.

Disposition: `WP34_CANONICAL_SCOPE_AND_NATIVE_BUDGET_CLOSED__VALID_PROMISE_POLYTIME_EQUIVALENT_TO_FORMULA_SAT__LOWER_BOUND_OPEN`.
