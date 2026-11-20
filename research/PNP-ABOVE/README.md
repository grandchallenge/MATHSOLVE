# PNP-ABOVE — GCL source and documentary record through WP20

**Historical WP00–WP17 source snapshot:** 18 November 2026; separately source-locked WP20 extension dated 19 November 2026. Governing research tracker: [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136); parent campaign: [PNP-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/162). Both remain **OPEN**.

The [source coverage snapshot](COVERAGE_SNAPSHOT.json) inventories **all 72 source artifacts** for WP00–WP17 at protected MATHSOLVE commit `d741a85572cd99a1f8e206d1211543ef72445da2`, with every path's Git blob SHA-1, primary source and receipt/test. The [no-network validator](validate_coverage_snapshot.py) checks that entire pinned tree, all 18 groups and their source identities:

```sh
python3 research/PNP-ABOVE/validate_coverage_snapshot.py
```

The inventory is a dated record, **not** a mathematical proof or certification. Future WP18+ sources and later amended proofs require a separately dated snapshot. Original imported upstream for the later work: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970` (Lean 4.35.0-rc3). The earlier WP00–WP04 work did **not** uniformly execute this original imported model.

## WP24 source SAT-instance-dependent game — original mathematical layer (20 November 2026)

[WP24 result, original MIPRE game, 3CNF translation, source circuit compiler and open obligations](WP24_RESULT.md) construct a genuine formula-dependent MIPRE synchronous game with original kernel-checked tensor quantum value **1 iff SAT, 0 if UNSAT**; a concrete perfect PCC strategy on satisfiable instances; and an exact original 3CNF SAT-witness equivalence. The generated original Boolean circuit is well formed, has **at most 9m+1 gates**, and uses the pinned original polynomial-time formula-to-circuit compiler. [Adversarial scope audit](WP24_SCOPE_ADVERSARIAL_AUDIT.md) withholds original seven-level source verifier, normal-form decider/runtime, compressor integration and any P-versus-NP inference. Exact full uncached replay and protected admission are required for this candidate.

## WP23B original executable verifier to succinct SAT — scope-limited (19 November 2026)

[WP23B original Cook–Levin source bridge, exact forward/reverse characterization and scope](WP23B_RESULT.md) instantiate the pinned constructed MIPRE.SAT.succinctCookLevin polynomial-time circuit describer against the original WP21/22 executable decider. The protected-admitted result proves exact validity/time-bound conditions and characterizes satisfiability of the fixed Bell game's original succinct SAT formula by simple mask and question-length conditions. This confirms the existing verifier-acceptance-to-SAT direction but does not supply arbitrary SAT-to-verifier hardness, a compatible compression promise family, a PNP lower bound or independent certification. Original uncached WP08–WP23B source replay, 20 new standard-axiom Lean theorem audits, and all protected checks passed; MATHSOLVE PR #1259 was merged at exact protected head 28a710900ed8217769c5bed95492e7efd2cbe779.

## Verified predecessor proof cache — development-only (19 November 2026)

[PNP-CACHE-001 content-addressed predecessor cache](PNP_REPLAY_CACHE.md) implements and tests a local SHA-256 keyed accelerator for 65 source-locked WP08–WP23A or 70 WP08–WP23B original Lean modules and their compiled proof objects. The extension preserves the original WP23A cache key and adds an explicitly selected, separately source-locked WP23B stage. Cache checks rehash exact source and compiler provenance and every object; hostile mutations fail closed. New Lean proofs compile against the restored predecessors. **All protected-admission replays continue to recompile every original source module and run the exact source-lock and standard-axiom audits.** This is an engineering improvement, not a mathematical-certification bypass.

## WP23A fixed Bell-game incompatibility with compressor promises (19 November 2026)

[WP23A exact native classical optimum and compression-interface diagnostics](WP23A_RESULT.md) prove in the original MIPRE source that the unrestricted local classical optimum is **exactly 3/4** for every positive index and one-bit-capable answer budget; that both original quantum and classical game values are **index/budget invariant**; and that every power-of-two index fails the **quantum-value at most 1/2** soundness antecedent of the original GapCompression interface. [Scope audit](WP23A_SCOPE_ADVERSARIAL_AUDIT.md) excludes any general compression impossibility, P-versus-NP or certification claim. The original upstream compression construction is real, but its seven-level, perfect-PCC/low-quantum-value interface is not directly applicable to this fixed nine-level game. An input-dependent source-native verifier family and the classical SAT cost transfer remain OPEN.

## WP22 original native bounded verifier with strict Bell gap (19 November 2026)

[WP22 admitted-result scope and proof inventory](WP22_RESULT.md) upgrade the actual source-native original MIPRE Verifier 9 to a globally synchronous, polynomially bounded, answer-sensitive game with a **proved unrestricted local classical upper bound 3/4, an original native quantum lower bound 81/100, and strict gap >= 3/50** for all n != 0 and T >= 1, including the bounded original budget T = n ^ boundLam for n >= 2. The proofs are nine new source-locked Lean modules and 35 new theorem declarations. [Adversarial claim audit](WP22_SCOPE_ADVERSARIAL_AUDIT.md) distinguishes theorem scope from positive-parameter gap compression, uniform SAT lower bounds, P-versus-NP transfer and public certification; those remain OPEN. Original MIPRE GameTransport answer extension, invalid-answer rejection, native synchrony and exact source-support distribution are explicitly proved or reused. The full source-native gap was NOT established by the earlier WP20 or WP21 tranches.

## WP21 original bounded answer-sensitive source verifier (19 November 2026)

[WP21 source-native result, scope and next obligations](WP21_RESULT.md) construct a true original MIPRE `Cost.Prog` binary-answer decider and an original `Verifier 9` on the WP20 cyclic sampler. Lean proves source well-scoping, totality, native acceptance/evaluator agreement, accepted-question length, a source polynomial runtime bound, and original `Verifier.IsBounded`. The masked mathematical predicate is globally synchronous and agrees with WP20 on every source seed; 2,048 original evaluator seed/answer checks passed. At the WP21 admission date, the universal native parity bridge, synchrony and native gap transfer were **not yet proved**; these are now discharged in WP22. Compression, succinct SAT transfer, P versus NP and independent certification remain OPEN.

## WP20 cyclic sampler and strict rational original game gap (19 November 2026)

[WP20 source-native theorem, explanation, claim boundaries and next obligations](WP20_RESULT.md) construct a **different original nine-stage two-sided CL distribution**, with 128 full four-edge question squares over 512 uniformly weighted pairs. Its original [Cost.Prog sampler](WP20_SourceSamplerProg.lean) has all four quantified source queries, valid original `Sampler 9`, raw termination and polynomial runtime certificates; 17 new source-locked original Lean modules, [manifest](WP20_SOURCE_LOCK.json), [full replay](WP20_REPLAY.sh) and [107-theorem axiom audit](WP20_AXIOM_AUDIT.py). An **answer-sensitive mathematical synchronous CHSH predicate** has **exact unrestricted local classical value 3/4**, a genuine original dimension-two projective measurement strategy of value **81/100**, and a strict **original quantum/classical gap of at least 3/50** for all indices. **Not yet a source-executable answer-sensitive decider:** the original bounded `Verifier 9`, accepted answer-length bridge, compression and classical SAT transfer remain OPEN. The old immutable WP00–WP17 72-artifact snapshot is unchanged; do not read these results as independent MATHCERT certification or P versus NP.

## WP19 universal star-support no-advantage theorem (19 November 2026)

[WP19 original-source theorem and explanation](WP19_RESULT.md) proves the **exact 512-pair WP18 source law** and an unconditional no-quantum-advantage theorem for **every mathematical synchronous decision predicate** over that original sampler. A general no-signalling convex-bound theorem is proved and instantiated directly with the original tensor-product Born and tracial commuting strategy models. Original synchronous, quantum and commuting values are exactly equal, not necessarily one; changing the WP18 decider cannot help. Its [eight Lean modules with exact Git blobs](WP19_SOURCE_LOCK.json), [full original-source WP08–WP19 replay](WP19_REPLAY.sh) and [axiom audit](WP19_AXIOM_AUDIT.py) form a separate new tranche. The historical **WP00–WP17 72-file source inventory remains unchanged**. WP20 requires a richer two-sided CL question law (not a star/matching) and then a genuinely answer-sensitive bounded source decider with a proved positive gap.

## WP18 extension (18 November 2026; separate exact source lock)

[WP18 full-depth original asymmetric source sampler and bounded verifier](WP18_RESULT.md) constructs an actual **non-diagonal original CL distribution** and player-aware `Cost.Prog` query implementation, with quantified source contracts, raw termination, and polynomial bounds. At all positive indices, all three original source game values equal **one** under the unchanged identity decider: this is a precise negative control, **not** a hard game or quantum advantage. The [nine-module new-source manifest](WP18_SOURCE_LOCK.json) and [original-source replay](WP18_REPLAY.sh) are independent of the immutable **WP00–WP17 72-file historical snapshot** below. WP19 subsequently proves the sparse star support **always forbids** an original synchronous/quantum/commuting value separation under any mathematical synchronous decision predicate. A structurally richer source sampler is now necessary.

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

WP18 supplies an original bounded off-diagonal player-asymmetric sampler but WP19 proves its **star-shaped support forbids quantum advantage under every synchronous decision predicate**. WP20 therefore replaces the question source with a genuinely two-sided 128-square CL distribution and proves **a strict original-model mathematical CHSH quantum/classical game-value gap ≥ 3/50**, exact local classical value 3/4 and a concrete dimension-two quantum witness of 81/100, while completing the original *sampler* source-execution/query/runtime obligations.

**Next substantive source obligation:** convert WP20's mathematical answer-sensitive parity predicate into a provably semantically equivalent **original bounded Cost.Prog decider** and complete an original `Verifier 9` and answer-budget/value correspondence. Only thereafter attempt positive-parameter introspection, answer reduction, repetition/compression, Theorem 12.1 source constants, uniform succinct SAT-to-classical transfer and the separate PNP-001 model/NP/endpoint bridges. All remain **OPEN**, and no P-versus-NP conclusion or independent MATHCERT certification has been reached.

**Documentary disposition:** `SOURCE_INVENTORY_COMPLETE_WP00_WP17__SUBSTANTIVE_RESEARCH_AND_CERTIFICATION_OPEN`. No P = NP, P != NP, unrestricted lower bound, full quantum compressor or independent certification is claimed.
