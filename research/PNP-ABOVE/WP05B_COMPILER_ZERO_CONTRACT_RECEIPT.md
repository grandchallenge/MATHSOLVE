# PNP-ABOVE WP05B — Exact imported compiler zero-branch contract and totality witness

**Status:** Lean-checked, source-imported theorem-interface test. Not an evaluation of a positive-parameter compressed verifier and not mathematical certification.

## Source and environment

- Upstream exact revision: vidick/MIPRE-formalization commit 5926bdff5db621f44682a101007ef2fe3ae8d970.
- Compiler source: MIPRE/Background/Introspection/DecisionCompiler.lean.
- Required toolchain: Lean 4.35.0-rc3.
- Upstream module compiled successfully at the pinned source revision: 3,978 build jobs, exit zero, as recorded in MATHSOLVE WP05/PR #1162.
- Test file: [WP05B_CompilerZeroContract.lean](WP05B_CompilerZeroContract.lean), Git blob a22cde356b8eb85cda019bca1710ddae030d8446, SHA-256 ec4a273f1e57187d53a33c2bd1866916e8aba091b063a23ea2dc2da1c9c11572.
- The test imports the genuine upstream DecisionCompiler module. No copied type or axiom declarations are used.

## Three Lean-checked propositions

1. For every natural compiler constant c, ClockedUniversalMachine U and upstream Prog values S,D, the zero-parameter compiler output equals DecisionCompiler.zeroProg:

    DecisionCompiler.compute c U ((S,D),0) = DecisionCompiler.zeroProg.

    Proof: rewrite using the genuine upstream DecisionCompiler.compute_apply theorem, then reflexivity.

2. That same zero-parameter output is well-scoped for one environment variable:

    (DecisionCompiler.compute c U ((S,D),0)).WellScoped 1.

    Proof: imported DecisionCompiler.compute_closed.

3. For arbitrary index n and binary-tree payload, the zero-parameter decider has a terminating native-program run with the declared zeroTest output:

    exists t, (DecisionCompiler.decider c U S D 0).prog.Runs
      (.cons (encode n) payload) (encode (DecisionCompiler.zeroTest payload)) t.

    Proof: imported DecisionCompiler.zero_runs, selecting the lambda-zero disjunct.

These are universal theorem-interface checks with symbolic arguments, not a batch of sampled instances.

## Exact execution evidence

Source was fetched from the GitHub branch and hashed on CHAD. The Lean command in the upstream pinned Lake environment was:

    lake env lean /tmp/gcl-mipre-wp05/CompilerZeroContract.lean

The test exited with code **0** and no compiler messages. Receipt for execution launch: GCL_CONTROL_BASH_RESULT/1 ID 32c173990263400f9ac248ff5a7bd7f7. Final exit/readback receipt: 6dbd0e20988e43dc88223556c428caa3. This attests the CHAD local process and exact file state, not an independent external mathematical referee.

A prior WP05 proof draft failed on a trivial unsimplified if-true conditional. The corrected draft was separately executed with exit zero and matched protected-main Git blob d63fc00ec780fb36b582d1d5e474aacf189978d2. This WP05B test adds an imported termination/totality witness and is the accepted successor.

## Unsolved compiler obligations

The compiler is built and its zero branch is now source-checked. A positive-parameter test still requires a ClockedUniversalMachine instance, finite native source metadata, soundness correspondence and control of the original source's noncomputable choices. The completed zero branch deliberately selects a fallback and does not invoke the positive introspection kernel, answer reduction or parallel repetition.

The earlier explicit-table classical SAT transfer remains restricted to classical strategies and explicit game descriptions. No new asymptotic classical lower bound, full MIP*=RE Figure 15 compressor or P-versus-NP conclusion is claimed.
