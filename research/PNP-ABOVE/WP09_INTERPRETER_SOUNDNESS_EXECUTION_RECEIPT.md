# PNP-ABOVE WP09 — imported-evaluation soundness proof

**Disposition:** native Lean theorem checked against upstream `MIPRE.Cost.Eval` in the original pinned Lean environment. This is a local formal proof of interpreter soundness, not proof of full quantum compression or P versus NP.

## Exact source and test

- Upstream: `vidick/MIPRE-formalization` at `5926bdff5db621f44682a101007ef2fe3ae8d970`, with `leanprover/lean4:v4.35.0-rc3`, pinned Mathlib/MIPStarRE and the successfully built `MIPRE.Foundations.Verifier`.
- GCL antecedent: [WP08 native identity decider](WP08_NineBitDecider.lean), protected-main blob `45b9fa687fad92bf1b1d4be2809473e0c4f9957d`. WP09 contains the **same seven-clause fuel interpreter** as WP08, with actual upstream `Prog`, `Data`, `Env` and `Eval` imports. The interpreter source is reproduced in WP09 so this proof file can be checked independently of the GCL project module layout.
- Exact WP09 tested Git branch source: [WP09_InterpreterSoundness.lean](WP09_InterpreterSoundness.lean). Git blob `3b64353814fd70a77810e51f2d04cbcfb4271def`; SHA-256 `bd8e48e284f70a0a4b5856001f8b190cbfb5f8f6cd5bf9d0a6ce2f43bdc6c3c6`. The branch source was fetched through GitHub, compared byte for byte with the locally corrected test file, and returned `EXACT_BYTES_MATCH`.
- Original attempt yielded 8 Lean elaboration errors in proof branches (no mathematical counterexample). They were repaired by explicitly unpacking equality of result and time using `rcases h with ⟨hr,ht⟩; subst r; subst t`.
- Final command, from the pinned upstream checkout: `lake env lean /tmp/gcl-pnp-wp09/Branch.lean`. **Exit code 0**, compiler stdout/stderr empty (SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`). Run launch GCL CONTROL receipt `af21496d18b5421f915094b1a4e5109c`; exit/readback receipt `7165e8ae8d1b4160851868e73f72e084`. OS-local execution evidence, not an independent third-party mathematical certification.

## Proved statement

For all fuel budgets `f`, environments `e`, native source programs `p`, results `r`, and execution costs `t`:

```lean
runFuel f e p = some (r,t) → MIPRE.Cost.Eval e p r t
```

The proof proceeds by induction on fuel and uses the **actual upstream constructors** `Eval.var`, `Eval.nil`, `Eval.const`, `Eval.cons`, `Eval.elim_nil`, `Eval.elim_cons`, `Eval.let_`, `Eval.loop_nil`, `Eval.loop_stop` and `Eval.loop_step`. It checks successful results against exact source costs and environment mutation. No `sorry`, `admit`, or axiom was introduced in this file.

**Consequence:** any finite successful run of this interpreter has a corresponding native source evaluation proof with the same output and cost. The WP08 finite identity-decider checks used the identical interpreter logic, but WP09 does not import WP08 by module path and does not yet add a separate theorem connecting its specific game-decider acceptance to the source's `Decider.Accepts`.

## Remaining obligations

1. Prove a program-specific `Decider.Accepts` equivalence using the WP08 identity decider and this soundness lemma, together with exact completeness/termination and malformed-input bounds.
2. Implement the **actual nine-level source sampler** with the upstream query interface, `CLFun.ExactlyOn`, all four run conditions and uniform halting. Do not call the existing decider a complete `Verifier 9`.
3. Establish `Verifier.accepts_length`, a uniform source-model execution-cost bound, and a positive `IsBounded λ` witness.
4. Only then instantiate and execute positive-parameter `DecisionCompiler.compute`, followed by answer reduction/repetition. The previous upstream positive-branch source-shape theorem is not a runtime execution of the compiled game.

No general SAT-to-classical strategy cost transfer, new lower bound, or P ≠ NP proof follows from this result.
