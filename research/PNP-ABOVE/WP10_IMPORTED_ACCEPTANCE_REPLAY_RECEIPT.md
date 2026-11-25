# PNP-ABOVE WP10 — imported-source acceptance bridge replay and axiom audit

**Disposition:** exact-source Lean 4.35.0-rc3 elaboration **PASS**, all four WP10 declarations depend only on standard axioms. The result is a bounded Lean-checked source-native theorem, **not** substantive mathematical certification, full verifier construction, quantum compression, or a P-versus-NP result.

## Source and execution identities

- Parent research tracker: MATHSOLVE #1136; protected research baseline `a0af41fad9ad58d3e333092586119b4c660da382`.
- Upstream `vidick/MIPRE-formalization` fixed at Git commit `5926bdff5db621f44682a101007ef2fe3ae8d970`, Lean `v4.35.0-rc3` with its pinned Mathlib and MIPStarRE dependencies.
- Imported GCL WP08 source blob `45b9fa687fad92bf1b1d4be2809473e0c4f9957d`, staged SHA-256 `027384e4a0b7de9551b69b2a5a22ad8589c1707367de96f5caa4956e364715a9`.
- Imported GCL WP09 source blob `3b64353814fd70a77810e51f2d04cbcfb4271def`, staged SHA-256 `bd8e48e284f70a0a4b5856001f8b190cbfb5f8f6cd5bf9d0a6ce2f43bdc6c3c6`.
- New WP10 proof: `WP10_SourceAcceptanceBridge.lean`, SHA-256 `4872dad7f480935faed6801f5d4b58f3e5b480e866af9840f87a560cfdd7c511`.
- Fail-closed replay harness: `WP10_REPLAY.sh`, SHA-256 `84ba9c988308986e2d88ef2ef592610da5cdb5ae022d638e03e8edee7060e0cc`.
- Finite negative-control test: `WP10_EXPLICITIZATION_NEGATIVE_CONTROL.py`, SHA-256 `5d6be837f8e3d183d2126b3b874458cf35f8aeda7bf0c564c068b80f985f9a2b`.
- Recovered upstream source build: `MIPRE.Foundations.Verifier` compiled successfully, **3,111 jobs**, log `/tmp/gcl-pnp-wp10-build-verifier-retry.log` (CHAD-local evidence).

## Checks

- `bash -n research/PNP-ABOVE/WP10_REPLAY.sh`: PASS.
- `python3 -m py_compile research/PNP-ABOVE/WP10_EXPLICITIZATION_NEGATIVE_CONTROL.py`: PASS.
- `python3 research/PNP-ABOVE/WP10_EXPLICITIZATION_NEGATIVE_CONTROL.py --max-m 10`: PASS; checked diagonal strategies and exact one-hot formula counts at m=1..10; bounded enumerative check, not a complexity lower bound.
- `bash WP10_REPLAY.sh PINNED_MIPRE_CHECKOUT EXACT_GCL_CHECKOUT WORK_DIR`: PASS; log `CHECKING_SOURCE_NATIVE_WP08`, `WP09`, `WP10`, `WP10_STANDARD_AXIOMS_ONLY_PASS`, `WP10_IMPORTED_REPLAY_PASS`, exit code 0; checked imported Lean modules and generated `.olean` files. Final candidate source executed after correcting module root and replacing generated-native-axiom tactics with kernel `decide`.
- Four `#print axioms` checks: each declaration has exactly `propext`, `Classical.choice`, `Quot.sound`; no additional generated `native_decide`, `sorryAx`, or other user axioms. Replay harness parses these four reports and fails on any extra axiom. Log: `/tmp/gcl-pnp-wp10-lean-replay-20261117/AxiomAudit.log`.
- Recorded CHAD-local execution capture for final replay log/readback: `1f7e7270763241048ad1ae8d1af71a30`; earlier native-axiom finding capture: `221d3bf3266f4470adda5ea7a015ed7a`.

## Exact proved scope

1. `accepts_of_fuel`: true result of WP09's sound fuel interpreter on the **original** WP08 `identityDeciderProg` implies source-native `Decider.Accepts`.
2. `rejects_of_fuel`: false result of the same interpreter contradicts any source-native accepting evaluation by `Eval.deterministic` and inequality of canonical Boolean encodings.
3. `accepts_nine_bit_example`: one concrete source-native positive-index acceptance statement, discharged with kernel `decide` and the soundness bridge.
4. `rejects_zero_index`: one concrete source-native zero-index rejection statement, discharged with kernel `decide` and the determinism bridge.

The source imports real MIPRE `Prog`, `Eval`, `Decider` and GCL WP08/WP09 modules by exact original bytes; it neither copies source definitions nor assumes WP08 and WP09 interpreters are definitionally equal.

## Residual mathematical obligations

- A **general**, both-direction characterization of the decider's acceptance for every legal nine-bit input and malformed raw input; termination/completeness and a uniform source execution-cost bound remain unproved.
- A full source-native `Sampler 9` and `Verifier 9` satisfying `CLFun.ExactlyOn` and all required run conditions.
- A quantified `IsBounded λ` witness, effective constants and a positive-parameter compression instance, followed by answer reduction and repetition.
- A succinct, polynomial-overhead SAT-to-classical-resource transfer theorem; the current negative control only refutes an inference for the specific explicit-table expansion. Quantum Schmidt-rank lower bounds are not classical time or circuit lower bounds.
- PNP-001's Formal Conjectures machine/encoding concordance and the external Theorem 12.1 quantitative statement/proof discrepancy remain open.

**Governance:** no independent specialist mathematical certification or claim promotion is asserted. Protected PR checks, protected admission and exact-head readback must be recorded separately. Source SHA-256 hashes are the tested content identities, not a substitute for commit-head readback.
