# PNP-ABOVE WP05 — Imported native Prog and introspection-decider build receipt

**Status:** bounded executable research result, using the **actual imported upstream** MIPRE types and theorem declarations. This record does not assert execution of the positive-parameter introspection transformation or of the three-stage quantum compressor.

## Upstream source and dependencies

- Pinned repository: [vidick/MIPRE-formalization at 5926bdff5db621f44682a101007ef2fe3ae8d970](https://github.com/vidick/MIPRE-formalization/tree/5926bdff5db621f44682a101007ef2fe3ae8d970).
- Source modules: `MIPRE/Foundations/Cost/Basic.lean` and `MIPRE/Background/Introspection/DecisionCompiler.lean`.
- Toolchain: Lean 4.35.0-rc3, Lean commit `470d5ce1400764999581fd26d5d72b00d990b0f4`, matching upstream's `lean-toolchain`.
- Lake lock revisions checked against local Git checkouts: Mathlib `c55e6e786f49471c72fbddbec5415808896aec1e`; MIPStarRE `5fc363bc8b77b1a6bbdaaeea634f1b0f3ff0ad79`. Fifteen dependency directories are present. This is a *local dependency checkout*, not a claim of upstream mathematical certification.

## Successful genuine upstream builds

| Command, executed in the pinned source checkout | Outcome |
| --- | --- |
| `lake build MIPRE.Foundations.Cost.Basic` | **Success; 1,219 build jobs** |
| `lake build MIPRE.Background.Introspection.DecisionCompiler` | **Success; 3,978 build jobs** |

The latter created `MIPRE/Background/Introspection/DecisionCompiler.olean`; its build-exit file records zero. There were nonfatal deprecated `if_neg` warnings in the pinned upstream source. The module contains the actual `DecisionCompiler.compute` object; **compiling its definition is not the same as invoking it on specific program metadata**.

## Exact-file runtime replay

[WP05_ImportedProgReplay.lean](WP05_ImportedProgReplay.lean) imports `MIPRE.Foundations.Cost.Basic`, opens `MIPRE.Cost`, and declares **no copy** of `Data`, `Prog`, `Env` or `Eval`. Instead, it defines a separate fuel-limited interpreter `runFuel` for the imported `Prog` constructors. Fuel measures recursion depth and is **distinct from** `Eval` time units.

The file includes ten finite interpreter regression guards covering all seven constructors, out-of-bounds variables, both `elim` branches, let-binding, stopping and stepping loops, and exhausted fuel. Two additional examples inhabit the **imported** `MIPRE.Cost.Eval` relation: a universal variable-read witness and a concrete seven-unit stop-loop witness.

- Git blob SHA-1 of exact tested branch file: `1f5f35fdfc4336339da90117966a7f64f275d088`.
- SHA-256 of local tested file: `3e6bab54a5b4bf9650946b5c74ee8b95ec50d31995192ddc7ce5066d3aaa9f8c`.
- Readback: source file fetched from the GitHub branch, with corresponding Git blob identity.
- Run: `lake env lean /tmp/gcl-mipre-wp05/ImportedProgReplay.lean` from the pinned upstream checkout.
- Result: **exit code 0**, output `some (MIPRE.Cost.Data.nil, 12)`, no Lean errors; 10 guards and two examples completed. The replay was launched via GCL CONTROL on CHAD and its result read from the saved process exit and log.

The exact portable source path is in this PR. The temporary CHAD path is execution workspace only.

## Next compiler branch and honest remaining status

The actual upstream file `MIPRE/Background/Introspection/DecisionCompiler.lean` defines

`compute (c : Nat) (U : ClockedUniversalMachine) : PolyTimeFun Metadata Prog`.

Its upstream `compute_apply` theorem selects `zeroProg` whenever `lam=0` and otherwise selects a zero-wrapped positive-parameter compiler on clamped source metadata. The imported module has been built; the **positive-parameter compilation has not been executed**.

A separate **unexecuted source-regression candidate** [WP05_SourceCompilerBranch.lean](WP05_SourceCompilerBranch.lean) states test obligations for zero-parameter source-program selection, well-scopedness and execution. It is a candidate for a subsequent Lean replay, **not** an accepted proof or runtime result; the command transport ceased accepting further execution requests after the successful upstream build and native replay. Do not infer that staging a Lean source file is the same as elaborating it.

Remaining mathematical/engineering tasks:

1. Replay and correct the staged compiler-branch proof file with the upstream build environment; include exact file hash and interpreter log.
2. Prove `runFuel` soundness against the imported `MIPRE.Cost.Eval` for every successful run, rather than only example-level consistency.
3. Encode the admitted 9-level identity input verifier as **actual** source `Prog` metadata with the source's serialization, uniform boundedness, clock and malformed-input semantics.
4. Instantiate a justified positive `lam`, computational `ClockedUniversalMachine`, and `DecisionCompiler.compute`; benchmark source-faithful output against the published introspection conditions.
5. Reconcile the source formalization's seven-level stage contracts and the v4 paper's nine-level normal form before attempting answer-reduction/repetition composition.

**Claim boundary:** native imported semantics and actual compiler *build*, but not a compiled positive-parameter finite game, new classical lower bound, SAT-to-quantum strategy transfer, P versus NP resolution or mathematical certification.
