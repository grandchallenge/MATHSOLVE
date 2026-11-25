# PNP-ABOVE WP12 — imported typed parser and raw-canonicality counterexample replay

**Classification:** `LEAN_REPLAYED` bounded source-native formal result and falsification witness, **not** independent specialist mathematical certification, a full nine-level verifier, or a P-versus-NP claim.

## Source lock and exact execution

- Original upstream: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970` with pinned Lean 4.35.0-rc3 / Mathlib / MIPStarRE.
- Protected MATHSOLVE parent: WP11 squash commit `ef12175a28be8d3bcff1a2ce1dfde44dea30b5de`.
- Exact previous candidate and replayed source commit: `101f2d177dda99a8854a41510712b6de39f9af2d` (contains the 15-theorem proof and corrected auditor).
- Source [WP12_TypedParserAndRawCounterexample.lean](WP12_TypedParserAndRawCounterexample.lean) SHA-256: `8c86a45b25d3d9704793ccc157c1ae222d68d2053fb2f947e72db57cebe16d54`.
- Replay command: `bash research/PNP-ABOVE/WP12_REPLAY.sh PINNED_UPSTREAM EXACT_GCL_CHECKOUT WORK_DIR`.
- Executed at committed head `101f2d1`: CHAD-local GCL CONTROL receipt `2fe3749525d944ca86073d1569504218`, staged lock file `/tmp/gcl-pnp-wp12-locked-101f2d1/lock.txt` and `AxiomAudit.log`.
- Exact original WP08 source blob `45b9fa687fad92bf1b1d4be2809473e0c4f9957d`; WP09 blob `3b64353814fd70a77810e51f2d04cbcfb4271def`; WP10 blob `860ad60fca4e99fcd836eec748fa419efd0701b2`; WP11 blob `088a731db4a7a1a21097a593958706df6b8a488b`. The new WP12 blob is committed-head read by `WP12_REPLAY.sh` and rechecked byte-for-byte against the worktree.

## Observed output

```text
CHECKING_SOURCE_NATIVE_WP08
CHECKING_SOURCE_NATIVE_WP09
CHECKING_SOURCE_NATIVE_WP10
CHECKING_SOURCE_NATIVE_WP11
CHECKING_SOURCE_NATIVE_WP12
WP12_STANDARD_AXIOMS_ONLY_PASS count=15
WP12_IMPORTED_TYPED_PARSER_AND_RAW_COUNTEREXAMPLE_PASS
exit 0
```

A separate Lean `#print axioms` audit covers all fifteen WP12 theorem declarations. Each uses only some subset of the standard axioms `propext`, `Classical.choice`, `Quot.sound`; **none** depends on `sorryAx`, a novel admitted axiom or a generated `native_decide` axiom. The axiom auditor fails closed on unexpected theorem counts or additional axioms; `bash -n`, `python3 -m py_compile` and mathematical Markdown source gates were also checked.

## Exact proved results and limitations

1. **All typed tuples:** source-native `MIPRE.Decider.Accepts n x y a b` holds **if and only if** `n ≠ 0`, both bitstrings have length exactly 9, and both answers are empty. The quantified proof uses imported `Eval` determinism, a structurally recursive evaluator, and an induction on encoded bitstring length, not finite search.
2. **Malformed raw-index witness:** a noncanonical raw field `Data.cons Data.nil Data.nil` decodes to `some (0 : Nat)` but differs from `encode n` for every `n : Nat`. The original WP08 program **accepts** a raw game tuple with this index, two valid nine-bit questions and empty answers; WP09 independently returns canonical true at the WP11 uniform fuel. Thus full raw-canonicality rejection is **false for the original source program**, without contradicting the typed theorem.
3. **Remain open:** formal canonicalization repair or explicit typed-only verifier contract, `Sampler 9`, four run conditions, `CLFun.ExactlyOn`, source-native full `Verifier 9`, quantified verifier boundedness, positive-parameter compressor, uniform succinct classical transfer, external source quantitative discrepancy and Formal Conjectures definition concordance.

**Protected status:** The exact candidate replay is distinct from the final evidence-commit replay and protected PR admission; the latter must be verified with a fresh source-locked run and exact protected-main readback. No parent status or certification promotion is authorized.
