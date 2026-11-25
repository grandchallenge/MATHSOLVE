# ERDOS-593-N3 — independent Lean source and theorem-fidelity replay

STATE: READY_FOR_PROTECTED_DISPATCH
EXTERNAL_DISPATCH_AUTHORIZED: NO
CANONICAL_PARENT_PROBLEM_EFFECT: NO
CERTIFICATION_AUTHORIZED: NO
WORK_PACKAGE: ERDOS-593-N3-SOURCE-KERNEL-FIDELITY
PREDECESSOR: contributions/ERDOS-OPEN-001/SUCCESSOR_002/synthesis/ERDOS-SUCCESSOR-002-SYNTHESIS-001.md

## Bounded objective
Independently check the externally reported full classification in Eric Li, arXiv:2606.24882v2, against its Lean 4 source repository ericlisg/erdos-593-1177-lean. The source head observed at reconnaissance was 5dcb6e4906df03f2e4294b21be73b55db7736f5a; independently verify and pin a source commit, Mathlib dependency lock, compiler version, and build environment.

1. Read the actual final theorem Erdos593.full_resolution_unconditional and dependent theorem bodies, not only README claims.
2. Inspect FTS, Embeds, obligatory, chromaticity, Bclass, intrinsic conditions, isolated vertices, and one-point amalgamation semantics against protected Appears/IsObligatory.
3. Rebuild in a reproducible environment and capture lake build logs plus #print axioms for all final results. Reject sorry/admit/axiom/native_decide/implemented_by or equivalent opaque substitutes within the dependency closure.
4. Produce theorem-by-theorem correspondence (or counterexample) to the mathematical source statement; state which facts are merely source-quoted versus native GCL proof.

## Return
An exact repository-identity receipt, environment + logs, concise statement-fidelity table, explicit missing source/axiom premises, and a smallest falsifiable discrepancy if any. A green build alone is not certification. No canonical target rewrite or MathCert effect. Do not treat a draft external preprint as a protected GCL theorem.
