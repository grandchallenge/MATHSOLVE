# PNP-ABOVE WP11 — exact-source completeness and native decision replay

**Disposition:** bounded source-native Lean proof replay PASS, not independent mathematical certification or a P-versus-NP proof. The source theorem contents are independently interpretable only within the pinned upstream model.

## Source identity and replay

- Protected MATHSOLVE ancestor: `b447809368083cdab92395dd1f64654388b2aa64` (WP10).
- First tested WP11 candidate head: `691d6b82a85f26bc940e0d64fb4051d49adc6059`.
- External upstream commit: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, Lean 4.35.0-rc3 and pinned Mathlib/MIPStarRE.
- WP08 original Git blob `45b9fa687fad92bf1b1d4be2809473e0c4f9957d`; staged SHA-256 `027384e4a0b7de9551b69b2a5a22ad8589c1707367de96f5caa4956e364715a9`.
- WP09 original Git blob `3b64353814fd70a77810e51f2d04cbcfb4271def`; staged SHA-256 `bd8e48e284f70a0a4b5856001f8b190cbfb5f8f6cd5bf9d0a6ce2f43bdc6c3c6`.
- WP10 original Git blob `860ad60fca4e99fcd836eec748fa419efd0701b2`; staged SHA-256 `4872dad7f480935faed6801f5d4b58f3e5b480e866af9840f87a560cfdd7c511`.
- New WP11 [Lean source](WP11_EvalFuelCompleteness.lean) SHA-256 `eecbc4ffec6cc671d048ca8566aef01e41bb9159cbf8353522ac3ae27109de34`. Git blob identity and final committed-head confirmation must be read back after protected admission.
- Replay command: `bash research/PNP-ABOVE/WP11_REPLAY.sh PINNED_MIPRE_CHECKOUT EXACT_GCL_CHECKOUT WORK_DIR`. Local exact-head replay transcript/checksum file: `/tmp/gcl-pnp-wp11-exact-head-691d6b8/lock.txt`, `WP11.log`, `AxiomAudit.log` and `status.txt`.
- Authenticated GCL CONTROL execution capture for the first exact-head replay: `9653482b0e07422f8486f3fedd3d26f3`; CHAD-local OS execution, not independent mathematical attestation.

## Observed result

```text
CHECKING_SOURCE_NATIVE_WP08
CHECKING_SOURCE_NATIVE_WP09
CHECKING_SOURCE_NATIVE_WP10
CHECKING_SOURCE_NATIVE_WP11
WP11_STANDARD_AXIOMS_ONLY_PASS count=18
WP11_IMPORTED_COST_COMPLETENESS_PASS
Exit code: 0
```

The 18 printed theorem axiom reports are limited to `propext`, `Classical.choice` and `Quot.sound`. None requires a new local axiom, generated `native_decide` axiom, `sorry` or `sorryAx`. The source is imported against the original pinned MIPRE `Cost.Eval`, `Prog` and `Decider` types.

## Verified scope

- Every terminating upstream `Eval` proof of a result and exact cost has a fuel-`cost+1` interpreter witness, and soundness provides the converse.
- The actual WP08 source decider is loop-free, copy-free, and terminates on every raw input. A source-cost structural bound evaluates to `89`, so fuel `90` is sufficient for every input. A separate proof establishes canonical Boolean output.
- For every typed question, source-native `Decider.Accepts` holds exactly when the 90-fuel interpreter returns canonical true, and its negation exactly when that interpreter returns canonical false.

**Excluded:** The specific input-parser specification (positive index, nine-bit question lengths and empty answers) is **not** yet proved equivalent to source acceptance for all raw inputs; `Sampler 9`, `Verifier 9`, quantified verifier boundedness, full positive-parameter compressor and SAT-to-classical lower-bound transfer are not established. The source's Theorem 12.1 quantitative discrepancy and PNP-001 Formal Conjectures concordance remain open. Mathematical certification and external claim promotion are excluded.
