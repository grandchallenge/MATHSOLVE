# PNP-ABOVE WP04 — Native Prog execution semantics: exact-head Lean replay

**Disposition:** bounded source-aligned interpreter and proof-witness test. No full MIP* compressor, no upstream Lean library build, no extracted quantum introspection compiler, no new classical lower bound, no SAT-to-quantum transfer, no P versus NP result, no independent mathematical certification.

## Source and execution identity

- **Primary source:** [vidick/MIPRE-formalization](https://github.com/vidick/MIPRE-formalization/tree/5926bdff5db621f44682a101007ef2fe3ae8d970) at exact upstream commit \`5926bdff5db621f44682a101007ef2fe3ae8d970\`.
- **Source specification:** [\`MIPRE/Foundations/Cost/Basic.lean\`](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/MIPRE/Foundations/Cost/Basic.lean), including \`Data\`, \`Data.size\`, seven \`Prog\` constructors, \`Env.get\`, and the inductive \`Eval\` cost relation. Upstream code was inspected at the pinned revision, not modified.
- **GCL file:** [\`WP04_NativeProgReplay.lean\`](WP04_NativeProgReplay.lean), Git blob SHA-1 \`1e422f210df6db82538e36e5a99c6630aba6300b\`, SHA-256 \`f4419be14a6e5d913af5c47a41a5890b2191316fa4f9029474ed49bc9208d63e\`. The local executed file's \`git hash-object\` matches the current research branch's GitHub blob SHA.
- **Exact toolchain installed and used:** Lean 4.35.0-rc3, commit \`470d5ce1400764999581fd26d5d72b00d990b0f4\`. This matches upstream's \`lean-toolchain\`. The upstream pinned Mathlib and other Lake packages remain absent locally and were **not** compiled.
- **Command:** \`/home/jim/.elan/toolchains/leanprover--lean4---v4.35.0-rc3/bin/lean /tmp/gcl-mipre-wp04/NativeProgReplay.lean\`. The code imports only \`Init\`, avoiding a false upstream build claim.
- **Clean execution:** exit code **0**, output \`some (PNPAbove.WP04.Data.nil, 12)\`; no compiler errors. \`GCL_CONTROL_BASH_RESULT/1\` receipt ID \`113b69fefc064f159aa2c448d01d42ad\`; output SHA-256 \`6f7b79f32ecd463fc37e9b5b6e14f6b808a2a8109697aad66a029b78a441f725\`. Execution origin: local OS, **not independently authenticated** as a mathematical referee run.

## What was implemented

The file restates the upstream *native semantics* in a separate namespace. The runtime representation includes binary-tree \`Data\`, size measured in constructor nodes, the seven program constructors \`var\`, \`nil\`, \`const\`, \`cons\`, \`elim\`, \`let_\`, \`loop\`, out-of-range environment reads returning \`nil\`, and every constructor of the source's timed big-step relation \`Eval\`.

An independent \`runFuel\` function evaluates these programs with a structural recursion budget. **Fuel is not the source cost \`t\`.** Its numerical \`t\` field accumulates the native source's costs, including copying data on variable reads, \`const\` size charges, environment updates in \`elim\` and \`let_\`, and \`loop\` stop/step costs.

The test includes ten exact Lean guards:

| Covered behavior | Expected result |
| --- | --- |
| Read variable zero holding a three-node tree | Same tree; cost 4 |
| Read nonexistent variable index 9 | \`nil\`; cost 2 |
| Construct a three-node literal | Same tree; cost 3 |
| Build \`cons\` of literal and \`nil\` | Correct binary tree; cost 5 |
| \`elim\` on nonempty data, branch-local variable 0 | \`nil\`; cost 3 |
| \`elim\` on empty data | Literal tree; cost 4 |
| \`let_\` copying input into bound variable | Input tree; cost 9 |
| \`loop\` with a terminating flag | Input tree; cost 7 |
| \`loop\` with one nonterminal transition | \`nil\`; cost 12 |
| Insufficient recursion fuel | \`none\` |

The source file also includes **two Lean-checked term-level witnesses** in the copied \`Eval\` relation: variable-read correctness for all binary trees, and the explicit terminating-loop cost for a concrete tree. These are not a general \`runFuel\` soundness/completeness theorem and do not import the actual upstream \`Eval\` relation.

## Source-faithfulness boundary

This is a **standalone transcribed model** verified by executing it under the exact Lean toolchain. It is not a replay of the upstream library's compiled declarations, and the copied \`Prog\` type is distinct from \`MIPRE.Cost.Prog\` even though its constructors and stated time semantics match the inspected source. A full correspondence requires compiling upstream modules and proving a preservation theorem, not merely comparing names or successful small examples.

The upstream \`DecisionCompiler.compute\` transforms machine/program metadata into a \`Prog\` under its own definitions and dependent proof machinery. WP04 does not call that function or resolve the existential constants used to assemble the full quantum compressor.

## Next executable obligation

1. Materialize the upstream repository's lockfile dependencies, beginning with the exact pinned Mathlib revision, using bounded, resumable fetches and the installed Lean 4.35.0-rc3 toolchain.
2. Compile \`MIPRE.Foundations.Cost.Basic\` and its dependencies and replace copied types with **actual imported \`MIPRE.Cost.Prog\`**.
3. Prove \`runFuel\` soundness relative to the imported \`Eval\` for successful evaluations; test under exact-head tools.
4. Encode the admitted nine-level identity verifier in native \`Prog\` and use the source's program/metadata interface; instantiate \`DecisionCompiler.compute\` only with evidenced parameters, not invented constants.
5. Reconcile the upstream seven-level stage contracts with the paper v4 nine-level interface before claiming a Figure 15 compressor.

The full three-stage quantum compression implementation and any general SAT transfer remain open.
