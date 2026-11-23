# PNP-ABOVE WP30: compressed game, classical transfer, complexity boundary

Pinned original `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970` (Lean v4.35.0-rc3). Protected parent `grandchallenge/MATHSOLVE@621f2866eda64f4b00d6b01145351610d0a315da`, including WP29 PR #1277. Initial local original-source kernel proof passed; protected admission requires separate exact uncached replay and readback.

## Original-source theorem

`WP30_CompressedClassical.lean` contains two new original Lean theorems:

- `conditional_compressed_classical_SAT_transfer`: If there exists a genuine original `Cost.PolyTimeFun Nat Bool` oracle that returns true for a perfect-PCC **actual compressed output at the exact source budget B(k,lam)** and false for output value at most 1/2 **at that same budget**, then its composition with WP29's source-polynomial explicit 3CNF-index compiler decides the original finite `Clause3 (Fin m)` satisfiability predicate. Both source `IsBounded lam`, original `G.C₀ ≤ k` and witness-size `m ≤ (2^k)^lam` are explicit. The proof invokes original `WP28C.powerCompressedPCC_of_sat`, `WP28C.powerCompressedSoundness_of_unsat`, and original source 3CNF semantics, not an assumed classical quantum simulation.
- `conditional_compressed_classical_SAT_runtime`: The resulting composed original `Cost.Prog` has an actual source-machine execution certificate `t ≤ (conditionalSATProgram oracle).timeBound.eval (esize cs)` for every explicit 3CNF input `cs`. This polynomial runtime is conditional on the polynomial original game-value oracle; no such oracle is constructed.

## Complete input-size ledger and exact obstruction

Define `N = esize cs` (original encoded input length), `q = cs.length` (clauses), `f = WP29.formula cs`, `k = WP29.source3CNFIndexProgram cs`.

| Stage | Machine object and certified accounting | What is not proved |
|---|---|---|
| 3CNF-to-formula | One fixed `Cost.PolyTimeFun Enc3CNF Fml`; native `Runs` bound `P_formula(N)`. WP29 formula gate count at most `9q+1`. | No SAT search. |
| Formula-to-index | One fixed `Cost.PolyTimeFun Enc3CNF Nat`; native `Runs` bound `P_index(N)`; `Nat.size k = esize f+1 ≤ P_index(N)`. | Numeric k is not polynomial in N. |
| Numeric source index | WP29 proves `2^q ≤ k`. The uncompressed native argument `2^k` has *binary length* `k+1 ≥ 2^q+1`. | No polynomial-time *explicit* construction of that full uncompressed input in N; original compression can operate symbolically. |
| Fixed raw source verifier | WP28B2/C establish code independent of f, all-raw-Data `HasPolyCost`, a single native `IsBounded lam`; actual SAT/UNSAT value one/zero at required indices. | Uniform native bounds are not full-game explicit cost bounds in N. |
| Compressed source verifier | Actual `G.output` has fixed code once `G,U,lam` fixed. The compressed index k has binary length polynomial in N. Original `G.sampler_dim`, `G.sampler_time`, `G.decider_time`, answer cutoff use `B(k,lam)=G.bound.eval(k+lam)`. | B is polynomial in NUMERIC k, not in binary length N. The theorem supplies no polynomial source-length bound for enumerating or running the whole explicit game. This is an absence of a sufficient upper bound, not a proof actual costs always reach B. |
| Classical game oracle | **Assumed** original `oracle : Cost.PolyTimeFun Nat Bool` with polynomial `P_oracle(esize k)` and promised correct yes/no game-value answers. | Neither quantum-to-classical game-value computation nor a lower bound forbidding it is supplied. |
| Classical SAT composition | `conditionalSATProgram oracle = oracle.comp source3CNFIndexProgram` has actual native source `Runs` and source polynomial composite `P_composed(N)`. WP30 proves correctness for scoped finite 3CNF under visible threshold/budget hypotheses. | Those hypotheses need uniform normalization for *all* original inputs. |

Large sparse binary variable identifiers may represent an index m much larger than N; the original full-response game contains m assignment bits. Uniform finite-variable renaming/densification, native index-threshold padding, and witness-budget normalization remain unproved for every arbitrary source instance.

## Precise logical obstruction

The proven direction is `polynomial classical compressed-game solver => polynomial classical SAT solver` (under scoped threshold/budget). This is a reduction showing the indexed game is at least as difficult as SAT. It is **not** a theorem excluding a polynomial classical solver. To infer `P != NP`, an independent lower bound must exclude every polynomial classical SAT algorithm. The upstream GapCompression theorems constrain perfect PCC and tensor quantum values; they impose no lower bound on deterministic classical algorithms. In particular a hypothetical fast classical SAT solver is consistent with everything proved here.

**Boundary:** `PNP_WP30_COMPRESSED_CLASSICAL_TRANSFER_CONDITIONAL__SAT_LENGTH_POLYNOMIAL_FULL_GAME_AND_CLASSICAL_LOWER_BOUND_OPEN`. No `P=NP`, `P!=NP`, efficient quantum-game algorithm or MATHCERT certification is claimed.
