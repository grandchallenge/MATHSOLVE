# WP40 — Native semantic-capacity obstruction and witness-carrying presentations

Scope: a no-go theorem for one precisely specified route to a superpolynomial classical SAT witness lower bound, not a solution to P versus NP. Pinned upstream MIPRE 5926bdff5db621f44682a101007ef2fe3ae8d970; Lean 4.35.0-rc3. WP35 and WP38B are protected predecessors. WP39A/B are protected at ffd5b2d01c80e25604c8044d3245ab0c485c14e4 and 937ae62dba248fee1a43fb107fb36c0c840a3f9e.

## Construction

For an arbitrary original Fml f and BitStr b, let T_b be a right-nested conjunction of Boolean constant leaves encoding b, terminating in the negation of the constant true. Define tag(f,b) = (T_b OR true) AND f. No new variables, advice oracle, nonuniform program, or change to the native syntax is involved. The tag prefix of the original postorder node representation contains the bits, a true delimiter constant and a negation node. One fixed total native polynomial reader scans that prefix, removes the delimiter, and returns b. One fixed polynomial builder constructs tag from (f,b). Neither computation promises that b is correct unless the original witness verifier accepts it.

The truth function is exactly preserved for every assignment. WP35's ordered support, dense-renamed evaluation and dense witness verifier are unchanged. The tag incurs at most 16*length(b)+46 extra native encoded units; for short witnesses, esize(tag(f,b)) <= 17*esize(f)+46.

Consequently every satisfiable formula has a logically equivalent, linearly larger presentation whose witness can be extracted by the same uniform polynomial-time program. This is an existential presentation, not a polynomial reduction from arbitrary SAT inputs. Constructing it requires a witness.

## Capacity theorem

A capacity M maps formulas to natural numbers. SemanticInvariant means exact equality under equality of the entire truth function and ordered support. LocalSound means that for every fixed total native polynomial witness program A there exists a polynomial p_A bounding M(f) by p_A(esize(f)) on every input f on which A succeeds (as determined by the native witness verifier). This is weaker than bounding M by the actual successful-run time, and stronger than requiring a bound only for programs solving all SAT instances.

Apply LocalSound to the single reader. For every satisfiable f, choose a short accepted witness and the corresponding tag g. Invariance gives M(f)=M(g), and the reader succeeds on g. Monotonicity of natural-coefficient polynomials gives M(f)<=p_reader(17*esize(f)+46). The composed polynomial bounds M on every satisfiable formula. RunSound, a direct bound by the actual charged native execution cost of any successful run, implies LocalSound using the native polynomial execution certificate.

This obstruction holds even if the measure is not computable. It rules out an invariant that simultaneously ignores all logically redundant syntactic information and lower-bounds every successful individual computation in the above precise sense. It does not exclude semantic or syntactic measures of family-uniform difficulty, bounds for globally correct algorithms, restricted proof-system complexity, worst-case hardness, or representation-aware lower bounds.

## Exact normalization boundary

A total native polynomial normalizer that outputs a tag of its own input containing an accepted witness for every satisfiable input exists if and only if a total polynomial witness constructor exists, and hence if and only if native SAT decision is in polynomial time (WP38B). Arbitrary formula simplification or equivalence-preserving normalization does not imply the result; the normalizer must supply a valid readable tag. No correctness is demanded on NO instances, but total polynomial running time remains required.

## Next route

A Structural Capacity Calculus must distinguish the information available in the original description from the information made available by a transformation. It must charge the computation of useful redundant structure instead of identifying the cost of the input and output solely by their equal semantics. A family-level or execution-state invariant with quantified uniform transformation costs remains a candidate; the present no-go theorem does not construct such an invariant or prove its growth bound.

## Verification boundary

The native source modules and independent finite syntax checks are supplied. The finite checks exhaust 109,800 formula/payload pairs, checking every assignment to the three test variables. They test implementation behavior, not the quantified theorem. Kernel replay and protected admission are separately recorded.

Recovery receipt, 2026-11-26: the CHAD HDD-backed dependency load timed out on the original attempt; all 18 tag declarations had passed. An authorized existing Colab CPU session rebuilt the pinned upstream libraries, freshly replayed WP08–WP34, and encountered the historical WP35 transition guard when invoked against a later revision. A separate source-matched incremental recovery compared all 94 predecessor source/object pairs against the historical WP35 protected checkout and freshly replayed WP35Dense with its original source lock and 55-declaration axiom audit. WP38A and WP38B were then freshly checked. Both WP40 modules compiled and all 33 theorem declarations passed the standard-axiom audit. Exact Lean source candidate: 9dcea58a69767390e4064c9fde825bcdb19c109c. Status SHA256 5b5940ff1858696b0232297535dec7b529079fa1e68a67912862732df9a09af3; axiom log SHA256 e0f1716cc2f880ca1d52883a85dcb92f2d6a2f2d88d3bc08908af9f51605e83f; 99 predecessor receipts SHA256 04632f9d0e8d3c110711fca3dc3caef3b253b7f2c6fe2fdbc8f1cbed4214f931. No proof source changed. This is internal kernel verification, not independent public certification.

The revised direct replay guard fails closed on CHAD/WSL before any staging, verifies pins and basic capacity on native Linux, and records bounded execution evidence. See REPLAY_RUNBOOK.md. Local full SSD staging remains capacity-blocked; the alternate runner avoids that bottleneck without weakening proof checks.
