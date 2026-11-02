# PNP-ABOVE WP05 — native upstream Prog import and executable readback

**Disposition:** bounded upstream-module build and imported-semantic execution, not a full compression implementation, an implementation of DecisionCompiler.compute, or mathematical certification.

## Pinned upstream and build environment

- External repository: [vidick/MIPRE-formalization](https://github.com/vidick/MIPRE-formalization/tree/5926bdff5db621f44682a101007ef2fe3ae8d970) at commit `5926bdff5db621f44682a101007ef2fe3ae8d970`.
- Native source: `MIPRE/Foundations/Cost/Basic.lean`. Unlike WP04, the WP05 test imports that actual module and uses the actual source types `MIPRE.Cost.Prog`, `MIPRE.Cost.Data`, and `MIPRE.Cost.Eval`.
- Toolchain: Lean 4.35.0-rc3, binary commit `470d5ce1400764999581fd26d5d72b00d990b0f4` (matches upstream `lean-toolchain`).
- The upstream Lake package directory has 15 named dependencies, including exact checked-out Mathlib commit `c55e6e786f49471c72fbddbec5415808896aec1e` and MIPStarRE commit `5fc363bc8b77b1a6bbdaaeea634f1b0f3ff0ad79`. The pinned Mathlib object files are present.
- Genuine upstream build command, in the pinned source tree: `lake build MIPRE.Foundations.Cost.Basic`. Result: **Build completed successfully (1219 jobs)**; an `MIPRE/Foundations/Cost/Basic.olean` output was generated.

## Imported native interpreter result

File: [WP05_ImportedProgReplay.lean](WP05_ImportedProgReplay.lean).

The exact branch file was retrieved from the GitHub contents API and copied to the test workspace; its SHA-256 is `3e6bab54a5b4bf9650946b5c74ee8b95ec50d31995192ddc7ce5066d3aaa9f8c` and its Git blob SHA-1 is `1f5f35fdfc4336339da90117966a7f64f275d088`.

The file defines only the independent fuel-bounded evaluator; the data, program and inductive proof relation are **imported upstream**, not transcribed. It checks all ten WP04 finite cases with `#guard decide`, including out-of-range variable lookup, `elim`, `let_`, a terminating `loop`, a nonterminal transition and insufficient fuel. Two additional Lean proof terms inhabit the actual upstream `Eval` relation, including a concrete terminating-loop cost of seven.

Command in upstream Lake environment:

```bash
lake env lean /tmp/gcl-mipre-wp05/ImportedProgReplay.lean
```

The bounded first invocation timed out at the connector boundary. A second, detached in-turn execution wrote `imported-replay.exit` and `imported-replay.log`; readback confirmed **exit code 0**, exact output:

```text
some (MIPRE.Cost.Data.nil, 12)
```

Run initiation receipt `GCL_CONTROL_BASH_RESULT/1` ID `0f018b69d010450c8da0a8080989ef5d`; terminal-file readback receipt `8dde5341316b433480baaa715dfb0ba8`. The environment is an authenticated local-OS execution transport, not an independent mathematical verifier.

**Limitation:** the source model is now genuinely imported, but the independently written `runFuel` still lacks a general soundness/completeness theorem relative to upstream `Eval`. Ten passing tests plus two separate examples are not such a theorem.

## Next target: actual introspection compiler

The exact source function is `MIPRE.Introspection.DecisionCompiler.compute (c : Nat) (U : ClockedUniversalMachine) : PolyTimeFun Metadata Prog` in `MIPRE/Background/Introspection/DecisionCompiler.lean`. The upstream module declares a `noncomputable section`, even though the function is represented by `PolyTimeFun` objects with computability theorems. A valid runtime instantiation must provide its `ClockedUniversalMachine` argument, finite source-program metadata and justified parameters. It must not conflate executing `compute` with existence of the three-stage gap-compression assembly.

The larger build target `lake build MIPRE.Background.Introspection.DecisionCompiler` was launched, with latest confirmed progress over 3,700 jobs. **No completed status or successful compiler invocation is claimed in this receipt until its exit code and exact logs are read back.** A transient connection failure is an operations-recovery condition, not a mathematical obstruction.

Remaining obligations: obtain the exact larger-build terminal receipt, test the source's zero-parameter compiler clause with actual `ClockedUniversalMachine` and `compute_apply`, implement and prove interpreter soundness for imported `Eval`, encode the nine-level verifier as native `Prog`, and carry the introspection/answer-reduction/repetition composition through a source-correspondence audit.

No new classical lower bound, unrestricted SAT transfer, quantum compression execution, or P-versus-NP claim is asserted.
