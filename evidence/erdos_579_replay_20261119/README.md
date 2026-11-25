# Erdős #579 — source-locked independent replay evidence

This packet preserves exact source bytes and local verification logs, not a MATHCERT certificate.

## Inputs

- Original 810,011-byte / 18,336-line `Main.lean` downloaded from `https://conjectures.io/results/e4934265-aa96-4bf5-a3c0-d01153dfcfaa/solution/download` with SHA-256 `c210bfcb2e4f1d9acf56e210d8800f831868783ff949d964033bb9cda6b684b2`.
- Task manifest from `conjectures-io/conjectures-tasks@2a58149e6edb0f1dc15b32391f8c29fdd85e9db3`; `Solution.lean` is the exact concatenation of Header + Main + Footer, SHA-256 `d0fa2f94aacf873ae57c982c46d8682fc7de8ee69d8c9cc8bd63fd733a28036d`.
- Formal Conjectures provider tree `6a786f997e18e8f095762a2830d191b7e25e505e` independently reconstructed from base and task patch with exact matching SHA. Pinned original GCL source `85f863718beeec7b58a3a1926ee92e3472bc2020` and theorem statement compared separately.
- Lean 4.33.1 (commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`) and Mathlib v4.33.1 (commit `0df444a360eaa60ab8c11dca51a86af692955474`).

## Read the outcomes precisely

- `build.log`: `lake build Challenge Solution` returned **0** after **8,901 jobs**. `Challenge.lean` is the unsolved original task scaffold; its expected `sorry` warning is *not* the theorem's proof. The `Solution.lean` target built.
- `axioms.log`: `#print axioms Bounty.target` returned **[propext, Classical.choice, Quot.sound]**, and the printed result has theorem type `¬ (True ↔ original_statement)`.
- `kernel_replay.log`: independent empty-kernel replay of **57,271** transitive declarations returned **`kernel replay into an empty environment: OK in 83061 ms`**, with 0 unsafe or partial declarations. The wrapper subsequently returned nonzero on an incompatible post-replay target lookup; the kernel did not reject a declaration.
- `comparator_incomplete.log`: a later corrected wrapper was terminated owing to substantial memory swapping. This does *not* provide proof that the entire separate challenge-vs-solution comparator passed. Exact statement concordance was separately reviewed and recorded on [MATH-PROGRAMME #1850](https://github.com/grandchallenge/MATH-PROGRAMME/issues/1850#issuecomment-6998200134).
- `Replay_lean4331_adapter.lean` is the *local verifier adapter*, not the imported proof. The original upstream verifier is `plasma-ai/erdos@6ca84eeb1eb98dcb7012e2a628982cfc0b3b809d:library/number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/Replay.lean`; the local changes are `import Lean.Replay`, `Lean.Environment.replay closure empty`, and `replayed.toKernelEnv.find? target` for Lean 4.33.1. This verifier source is preserved for audit but the full wrapper's PASS is NOT claimed.

## Mathematical and authority scope

The result disproves the original universal positive assertion about dense `K_{2,2,2}`-free graphs: it supplies fixed density `3/2048` and arbitrarily small independence ratio for arbitrarily large graphs. This does not compute the exact Ramsey–Turán density, grant novelty or priority, or constitute a protected MATHCERT certificate. MATHCERT has a separate intake, route and independent specialist-claim gate.

`SHA256SUMS.txt` checks the evidence source files. The later `README.md` is intentionally not included in that precomputed inventory.
