# Erdős successor-003 — protected return synthesis and critical adjudication

**Boundary:** this is an internal critical reconciliation of three protected worker results, not a MathCert certificate, a Lean rebuild, a verification of the entire historical odd-weird search, or resolution of Erdős Problems 593/470.

**Inputs:** #1031 / PR #1042 (593-N3); #1032 / PR #1039 (593-N4); #1033 / PR #1038 (470-N3). Exact comment IDs, SHA-256, Git blob IDs, protected merges, and transport metadata are frozen in the two cohort-003 evidence-closure files. The earlier successor-002 synthesis remains the predecessor and is not rewritten.

## Provenance and agent independence

Every return was authenticated and reservation-controlled, and every raw/receipt pair has passed the transport-intake machinery and a protected merge. This proves custody, **not** mathematical accuracy.

All three Github returns use the same authenticated account, `fyremael`, including N3 and N4 which the dispatch calls independent blind lanes. Nothing in the protected receipts establishes genuinely separate agent runtimes, distinct context isolation, or non-collusion. Hence *worker process independence is UNVERIFIED*. We may compare the results but must not use their purported independent agreement as two independent mathematical confirmations. No extra human-login ceremony is necessary to preserve custody, but specialist mathematical independence cannot be asserted from a role or agent_ref string alone.

## 593-N3: Lean formalization source audit

Read-only inspection of the pinned `ericlisg/erdos-593-1177-lean` commit `5dcb6e4906df03f2e4294b21be73b55db7736f5a` confirms that:

* `lean-toolchain` specifies Lean 4 v4.28.0;
* `lake-manifest.json` records Mathlib `8f9d9cff6bd728b17a24e163c9402775d9e6a365`;
* `RequestProject/PublicationCertificate.lean` contains a declaration `Erdos593.FullResolution` combining Problem 593 and three Problem 1177 propositions, with theorem `full_resolution_unconditional` syntactically invoking named predecessor theorems;
* `RequestProject/AxiomAudit.lean` contains `#print axioms` commands, including the publication theorem;
* `RequestProject/Defs.lean` specifies injective, non-induced edge-preserving finite-to-host embedding and proper countable-coloring obstruction as claimed.

This independently confirms **source identity and textual theorem shape**. It does **not** establish that a pinned `lake build` completed, that the console output actually lists only `[propext, Classical.choice, Quot.sound]`, that every imported theorem body is sound in the pinned package, or that the protected GCL target has been checked definition-for-definition in a formal environment. The worker's "kernel certified" conclusion remains a **SOURCE-REPORTED ASSERTION**, not a GCL-replayed kernel certificate. No automatic problem closure or upstream Mathlib contribution follows from a source declaration.

The next bounded technical action is a hermetic `lake build RequestProject`, `lake env lean RequestProject/AxiomAudit.lean`, exact dependency/axiom receipt and source/target fidelity comparison. Failure, including environmental failure, must return as a bounded blocker; no manufactured green build.

## 593-N4: cardinal-host proof

The worker's elementary linearity proof for the triangle-of-pairs hypergraph is valid: the intersection of hyperedges associated to triples A and B equals the pairs of `A ∩ B`, at most one pair when A and B are distinct triples. Injective hypergraph embeddings preserve edge-intersection sizes. Nonlinear finite triple systems therefore do not embed in linear hosts.

The countable first-difference coloring of pairs of distinct infinite binary sequences is also valid; three binary sequences cannot be pairwise distinct at one coordinate. The two-color version is impossible already for six indices by `R(3,3)=6`. These elementary statements agree with and **are not a second independent verification of** the earlier protected successor-002 native replay.

The worker identifies Erdős–Rado (1956), Theorem 39 and equation (95), as primary sources for `(2^aleph0)^+ → (aleph1)^2_aleph0`; this is the standard partition theorem with the correct ZFC parameter substitution. The **exact historical printed page and theorem formula have not been inspected in this transaction**. Its source lock remains bibliographically reported rather than a primary-image-verified lock. The worker correctly distinguishes sharpness of this particular hypergraph construction from that of arbitrary linear hosts.

## 470-N3: critical first-batch replay barrier

The worker reports a read-only inventory of 183 historical `data-1e21` archives at pinned `fwjmath/ows-data` commit `88d22faf46400f0050287c3c32c9a807ca3b1340`, with 527,827 member records; 485,384 `t` and 42,443 `c` terminal markers. The return embeds a large file-level manifest, but no independent replay of that inventory, archive parsing, or hash verifier has been completed by GCL in this synthesis. Treat counts as **WORKER-REPORTED**, not newly reverified.

The main useful result is a falsifiable **format mismatch**: first-batch workunits reportedly have seven scalar header lines, while the available `wobt-smart.cpp` reads nine; feeding historical archives to that binary as-is misaligns the fields and is not a valid historical replay. The worker describes a separate bounded, freshly generated nine-field computation and subset-sum diagnostics; that demonstrates a possible reproducibility method but does **not** certify historical first-batch data.

A complete lower-bound exclusion below 10^21 additionally requires an exhaustive and disjoint interval cover, original first-batch code/generator, predecessor coverage below 18×10^18, deterministic replay of archived workunit terminal states, and source-locked six-distinct-prime-divisor theorem where invoked. All remain **NOT DISCHARGED**.

## Claim adjudication

| Claim | Disposition |
| --- | --- |
| Authenticated capture and protected receipt identity | ACCEPTED — evidence custody only |
| Worker process independence | UNVERIFIED — shared transport identity |
| 593 formal theorem declaration and dependency pins | SOURCE TEXT VERIFIED |
| 593 full kernel replay, axiom output, full semantics | NOT REPLAYED; NO CERTIFICATION |
| Triangle-of-pairs linearity and embedding obstruction | ACCEPTED elementary proof, already replayed in successor-002 |
| First-difference countable coloring and Ramsey refutation | ACCEPTED elementary proof, already replayed in successor-002 |
| Exact cited printed Erdős–Rado theorem pages | PRIMARY PAGE INSPECTION PENDING |
| 470 seven/nine historical workunit mismatch | WORKER-REPORTED EXACT INTERFACE BLOCKER; independent reproduction pending |
| 470 archive record inventory and bounded checks | WORKER-REPORTED; replay pending |
| 470 exclusion up to 10^21 and six-prime bound | NOT CERTIFIED |

## Exit and concrete residuals

This closes **successor-003 evidence review and synthesis** when its exact integrity validator and protected merge pass. It does not close the underlying research questions. A minimal next execution unit is the pinned Lean kernel replay for 593, plus a separate small source-generation/format-compatibility investigation for 470. Both are executable without new general-purpose reviewer approval; independent mathematical certification is separate, substantive work.

Preserve all original comments unchanged. Do not publish a theorem, novelty claim, award claim, or problem resolution from this record.
