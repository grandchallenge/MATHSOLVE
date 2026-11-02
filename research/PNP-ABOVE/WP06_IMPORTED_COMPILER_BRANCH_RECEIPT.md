# PNP-ABOVE WP06 — Imported introspection compiler branch: Lean theorem replay

**Disposition:** exact-head Lean 4.35.0-rc3 theorem replay **PASS** on the genuine upstream MIPRE compiler definitions. The zero-parameter branch is proved; the positive-parameter branch is characterized symbolically, **not evaluated** into a concrete compressed verifier. No P-vs-NP conclusion, SAT transfer, independent mathematical certification, or Figure 15 implementation claim.

## Source lock and environment

Upstream repository [vidick/MIPRE-formalization](https://github.com/vidick/MIPRE-formalization/tree/5926bdff5db621f44682a101007ef2fe3ae8d970), exact revision `5926bdff5db621f44682a101007ef2fe3ae8d970`. Imported source module `MIPRE.Background.Introspection.DecisionCompiler`, which itself imports the genuine program, source-description, and zero-branch modules. Pinned Lean `4.35.0-rc3`, upstream-locked Mathlib `c55e6e786f49471c72fbddbec5415808896aec1e`, and upstream-locked MIPStarRE `5fc363bc8b77b1a6bbdaaeea634f1b0f3ff0ad79` were previously restored. The upstream compiler build completed successfully (3,978 jobs; WP05).

## Exact executable test

Source: [WP06_SourceCompilerProofReplay.lean](WP06_SourceCompilerProofReplay.lean), SHA-256 `d6c4242a5242157edae2426bd407ab46469fe0ad0c764865fd0362fde2783451`, Git blob SHA-1 `68443763c21f182f02f05a151addd38c14e576ff`. The source was fetched back from the working GitHub branch, and its local `git hash-object` matched this blob. Command from the exact pinned upstream checkout:

```sh
lake env lean /tmp/gcl-mipre-wp06/SourceCompilerProofReplay.lean
```

The final run returned **exit code 0**, with an empty Lean compiler log (no errors). Execution output is silent because this file contains kernel-checked theorems, not `#eval` output. The control-run receipt for the final exit check is `49764bcadcca42e8a4249e5aa21b4a56`; the successful replay was the second invocation following correction of an unqualified `SourceDescriptionCompiler.clamp` name. Do not count the earlier namespace error as a mathematical test failure.

## Seven checked source-facing theorems

| Theorem | Mathematical claim or tested interface |
| --- | --- |
| `zero_parameter_compile` | For all `c,U,S,D`, `compute c U ((S,D),0) = zeroProg` |
| `zero_parameter_scoped` | The compiled result is `WellScoped 1` |
| `zero_parameter_execution` | The genuine `MIPRE.Cost.Eval` relation supplies an execution witness for every index and payload |
| `zero_parameter_criterion` | Exact source acceptance condition: `x=[]`, `y=[]`, and answer lengths at most two |
| `zero_accepts_empty` | An explicit empty-question/empty-answer instance is accepted |
| `zero_rejects_nonempty` | An explicit nonempty Alice question is rejected |
| `positive_one_branch` | For parameter `lam=1`, the source produces a symbolic zero-wrapped `positiveCompiler` applied to clamped metadata |

The first six establish a **degenerate but actual** source compiler interface and its acceptance semantics, not a new quantum compression result. The final theorem identifies the published implementation branch without executing the resulting program. Source `compute_apply`, `compute_closed`, `zero_runs`, and `accepts_zero` are imported verified upstream statements.

## Exact limitations and next work

1. The source file proves properties about the actual compiler for arbitrary `ClockedUniversalMachine` values. It does **not** instantiate a specific machine object `U` or compute the large positive compiler output.
2. For `lam=0`, the implementation deliberately takes the `zeroProg` special case. That is not an instance satisfying the positive-parameter assumptions of Theorem 12.1.
3. The first genuinely nondegenerate task is encoding the admitted nine-level identity sampler/decider in upstream `Prog` notation with correct source serialization, clock, malformed input, and finite `lam` size promises, then supplying a concrete `ClockedUniversalMachine`.
4. Run `DecisionCompiler.compute c U ((S,D),lam)` with `lam≥1`, retain the generated `Prog` artifact, and test it against the source semantics. Reconcile levels and quantitative constants before any full compression or classical-transfer claim.

**Boundary:** one source-exact Lean theorem replay is completed. The general P versus NP problem and all nontrivial asymptotic classical lower-bound and succinct SAT-transfer obligations remain open.
