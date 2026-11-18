# PNP-ABOVE — GCL source and documentary record through WP17

**Snapshot:** 18 November 2026. Governing research tracker: [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136); parent campaign: [PNP-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/162). Both remain **OPEN**.

The [source coverage snapshot](COVERAGE_SNAPSHOT.json) inventories **all 72 source artifacts** for WP00–WP17 at protected MATHSOLVE commit `d741a85572cd99a1f8e206d1211543ef72445da2`, with every path's Git blob SHA-1, primary source and receipt/test. The [no-network validator](validate_coverage_snapshot.py) checks that entire pinned tree, all 18 groups and their source identities:

```sh
python3 research/PNP-ABOVE/validate_coverage_snapshot.py
```

The inventory is a dated record, **not** a mathematical proof or certification. Future WP18+ sources and later amended proofs require a separately dated snapshot. Original imported upstream for the later work: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970` (Lean 4.35.0-rc3). The earlier WP00–WP04 work did **not** uniformly execute this original imported model.

## Evidence progression

| WP | Bounded source evidence (primary receipt or note) | Claim limit |
| --- | --- | --- |
| 00 | [Parameter ledger](WP00_COMPRESSION_PARAMETER_LEDGER.md), [finite input](WP00_NINE_LEVEL_INPUT_AND_TRANSFER.md) | Symbolic and finite only |
| 01 | [Explicit-table SAT transfer](WP01_EXPLICIT_CLASSICAL_TRANSFER_AND_SOURCE_AUDIT.md) | Not succinct/general transfer |
| 02 | [Source interface](WP02_LEAN_COMPRESSION_SOURCE_INTERFACE.md) | Extraction, not execution |
| 03 | [Parameter recurrence](WP03_LEAN_PARAMETER_EXECUTION_RECEIPT.md) | Bounded Lean numeric replay |
| 04 | [Interpreter control](WP04_NATIVE_PROG_EXECUTION_RECEIPT.md) | Not imported full compiler |
| 05 | [Native build](WP05_UPSTREAM_BUILD_AND_NATIVE_REPLAY_RECEIPT.md) | Imported Prog/zero-parameter only |
| 06 | [Compiler branch](WP06_COMPILER_BRANCH_VERIFICATION_RECEIPT.md) | Zero-parameter and erasure |
| 07 | [Clamp adequacy](WP07_SOURCE_ERASURE_EXECUTION_RECEIPT.md) | Bounded source proof |
| 08 | [Nine-bit decider](WP08_NINE_BIT_DECIDER_EXECUTION_RECEIPT.md) | Original program, finite checks |
| 09 | [Imported Eval soundness](WP09_INTERPRETER_SOUNDNESS_EXECUTION_RECEIPT.md) | Soundness only |
| 10 | [Acceptance bridge](WP10_IMPORTED_ACCEPTANCE_REPLAY_RECEIPT.md) | Native implications, negative control |
| 11 | [Fuel completeness](WP11_IMPORT_REPLAY_RECEIPT.md) | Uniform bounded identity decider |
| 12 | [Typed parser](WP12_IMPORT_REPLAY_RECEIPT.md) | All typed inputs, out-of-contract raw counterexample |
| 13 | [Nine-level verifier](WP13_IMPORT_REPLAY_RECEIPT.md) | Bounded reference, not hard |
| 14 | [Conditional CL stages](WP14_IMPORT_REPLAY_RECEIPT.md) | Real stages; identical player questions |
| 15 | [Perfect strategy](WP15_IMPORT_REPLAY_RECEIPT.md) | Original game has value 1 in all three models |
| 16 | [Diagonal law](WP16_IMPORT_REPLAY_RECEIPT.md) | Native diagonal support and conditional no-gap |
| 17 | [General diagonal theorem](WP17_IMPORT_REPLAY_RECEIPT.md) | Unconditional sync/quantum/commuting equality |

Every auxiliary Lean module, source test, shell replay, axiom audit and alternate receipt is individually indexed in the snapshot; this table is only the navigation layer. Protected CI, compilation and internal logical review do not amount to independent public mathematical certification.

## Related GCL records, with separate authority

- [MATH-PROGRAMME public evidence](https://github.com/grandchallenge/MATH-PROGRAMME/blob/7a9abb42c72ab408d2265aa2799ff6e9cfd62e7f/docs/pnp_above/evidence.md) is the editorial projection. The 1 November 2026 [preprint manifest](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/research/preprints/PNP_ABOVE_v0_1_MANIFEST.json) and prerelease are an **unchanged historical edition** and do not contain WP17.
- The **separate** PNP-001 [definition audit](../../work_packages/PNP_DEFINITION_CONCORDANCE_001/concordance.json) is complete **as an audit**, not as theorem equivalence. [Bridge status](../../work_packages/PNP_BRIDGE_001/bridge_status.json) records the carrier and polynomial-bound bridges kernel-checked, with machine, NP-verifier and endpoint bridges still open.
- The [MATHFORGE provider manifest](https://github.com/grandchallenge/MATHFORGE/blob/main/provider_manifests/PNP-001.json) and [Formal Conjectures concordance](https://github.com/grandchallenge/MATHFORGE/blob/main/formal_sources/formal_conjectures/concordance/PNP-001.json) are retrospective; their older scoped statuses must not override Solve's newer separate source-locked audit. The [MATHSOLVE campaign manifest](../../campaign_manifests/PNP-001.json) is likewise a historical WP00–WP02 handoff, not this 18-WP inventory.
- [MATHCERT's pending handoff](../../cert_handoffs/PNP-001.json) preserves certification authority. No new terminal claim has been handed off, and no MATHCERT certification is asserted.

## Substantive open obligations

WP17 proves that for any original diagonal-supported synchronous game with nonempty answers, the classical/synchronous, quantum and commuting optimum is the **same feasible-diagonal mass**, even if some sampled questions are impossible to win. Therefore changing only the decider while retaining WP14's identical-player question distribution **cannot** yield a quantum advantage.

Next: an **off-diagonal player-asymmetric source-native sampler** with proved runtime bounds, a bounded **answer-sensitive executable Cost.Prog decider**, and an actual quantified **game-value gap**. Positive-parameter introspection/answer reduction/repetition, Theorem 12.1 quantitative reconciliation, general succinct SAT-to-classical transfer and the separate PNP-001 model/NP/endpoint bridges remain **OPEN**.

**Documentary disposition:** `SOURCE_INVENTORY_COMPLETE_WP00_WP17__SUBSTANTIVE_RESEARCH_AND_CERTIFICATION_OPEN`. No P = NP, P != NP, unrestricted lower bound, full quantum compressor or independent certification is claimed.
