# ERDOS-593-N5 — pinned proof replay and statement-fidelity review candidate

This is a mathematical-review candidate. It is not a MATHCERT certificate, a canonical statement rewrite, a publication or a GCL novelty claim.

## Exact subject and source custody

Historical question: characterize finite triple systems appearing in every uncountably chromatic triple system. External author: Eric Li, *A Resolution of Erdős Problems 593 and 1177: Obligatory Triple Systems and Exact Spectra*, arXiv:2606.24882v2.

- Source repository: `ericlisg/erdos-593-1177-lean`.
- Exact source commit: `5dcb6e4906df03f2e4294b21be73b55db7736f5a`.
- Lean: `4.28.0`, compiler commit `7e01a1bf5c70fc6167d49c345d3bf80596e9a79b`.
- Mathlib: `8f9d9cff6bd728b17a24e163c9402775d9e6a365`; the complete dependency lock is retained in the replay manifest.
- Canonical source manifest SHA256: `116c6ef00aa899fb38c08c5e4c92c0e434d0e7f9d574fcb5d4d42cc90ffb07cb`.
- `PublicationCertificate.lean` source SHA256: `60b4c30486d84a1c5317769746393eec62751f9b12b18ef427a6293b84d30179`.
- Protected Formal Conjectures snapshot: `google-deepmind/formal-conjectures@85f863718beeec7b58a3a1926ee92e3472bc2020`.
- Protected problem-statement blob: `fe5872380f07a2989c8a25ba44f4b29bb5d65dd7` at `FormalConjectures/ErdosProblems/593.lean`.
- Protected GCL predecessor: successor-003 synthesis at Solve `350c07c6a8ddee4fabd11f6991eedbbaecff7866`.
- The first protected worker result on issue 1031 remains comment `6081359458`; this is a subsequent operator replay, not a replacement worker result.

## Established replay evidence

The exact pinned project completed `lake build` with 8,091 build jobs. Mathlib dependency artifacts came from the content-keyed pinned cache; the entire compiler and Mathlib library were not rebuilt from bootstrap sources.

The separate execution of `RequestProject/AxiomAudit.lean` printed 17 actual dependency reports. Every report contains only `propext`, `Classical.choice` and `Quot.sound`, including `Erdos593.full_resolution_unconditional`, the classification, and the E2–E5 inputs. The source-dependent overlap witness also compiled with only those standard axioms.

The original build failures are retained as environmental history: host-disk exhaustion caused SIGBUS and corrupted compiled cache files. Ubuntu was moved to D: with explicit user authorization. A read-only header audit identified 285 damaged compiled files; pinned cache restoration and quarantine of ten broken project outputs preceded the successful build. No original theorem body, dependency lock or protected target was edited to obtain success.

## Exact statements offered for review

1. `Erdos593.full_resolution_unconditional` proves the source's `FullResolution` structure without literature hypotheses under the recorded standard axioms.
2. Its problem-593 field states obligatoriness iff `Bclass`, and `Bclass` iff the reduced intrinsic linear/bridge/even-Berge-cycle condition. It does not state obligatoriness iff Property B.
3. The four-vertex source with triples `{0,1,2}` and `{0,1,3}` is two-colorable, non-linear and source-defined non-obligatory. The first two finite facts also have a standalone Init-only certificate.
4. The formal source-to-target bridge is offered to check injective non-induced embeddings, countable-colouring versus cardinal-infimum semantics, all finite source families and isolated vertices. The final compiler execution passed and printed four standard-only axiom reports, including the finite-source roundtrip. The actual output and file digests are included in the packet.

The bridge copies the protected definitions into a namespace under the pinned 4.28.0 environment. Adaptations are confined to import/module/public-section scaffolding and namespace placement; mathematical definition bodies are preserved. The original protected definition text and its content digest accompany the candidate. This is not a claim that the original upstream project was rebuilt with its own newer dependency tree.

## Reviewer acceptance questions

- Do the copied definitions and formal adapters preserve the exact protected semantics, including universe-0 hosts, finite edge families, isolated vertices and non-induced injective embeddings?
- Does the palette argument establish strict uncountable chromaticity for all relevant hosts, including degenerate finite or edgeless cases?
- Does every `Bclass` generator and closure operation match the historical intended constructive classification? Does the intrinsic condition match the paper after isolated-vertex reduction?
- Is the source's theorem dependency closure sound under the stated axioms, with no weakened external interface or unintended vacuity?
- Does the resulting counterexample refute precisely the protected conjectural Property-B sufficient direction while leaving the historical characterization question and the external author's attribution distinct?
- Do the reproduction scripts, source/dependency identities, log digests and declared scopes agree?

## Certification routing and dispositions

Live MATHCERT `426d19a9ce6ecb9307ea7eb04047a961975c94df` has no registered route for ERDOS-593. Consequently this candidate is **not submitted as a generic schema-bound MATHCERT handoff**: doing so would require inventing an admitted route or using an unrelated campaign. The ordinary generic handoff's older pinned contract also has no ERDOS route.

Proposed intake scope for a separately admitted route: the exact 593 classification replay, its standard-axiom dependency record and the source-to-protected statement correspondence. Problem 1177 proof declarations are recorded as dependency-audit context, not requested for blanket certification. Route admission and specialist source-semantic/mathematical review remain pending; neither build success nor ordinary PR checks substitutes for them.

Requested disposition now: preserve and review this exact evidence candidate. Requested MATHCERT disposition later, after route admission: evaluate the stated proof and semantic claims under `LEAN_FORMALIZATION` and `SEMANTIC_REPLAY`, retaining the explicit source-versus-GCL and Property-B-versus-classification boundaries.

## Reopening conditions

Any change to the source commit, compiler, dependencies, statement/definition text, formal bridge, axiom list, source attribution, review provenance or route scope requires material rebinding and affected replay. Preserve all prior worker comments and historical receipts unchanged.

## Packet validation and reproduction

From the packet directory, run `python verify_packet.py` to check recorded file digests, the body-preserving protected-definition adapter, actual compiler output and the pending review/route boundaries. This checks the submitted evidence; it does not rerun Lean.

With the exact Lean 4.28.0 compiler on PATH, run `bash replay_593_review.sh /absolute/scratch/directory` to reproduce the pinned build, source axiom audit and formal bridge. Under WSL, supply `TASK_HOST_FREE_BYTES` measured on the Windows volume hosting the VHDX (at least 40 GB). Cold imports can take several minutes; the bridge execution limit is 1,800 seconds. The script writes fresh logs in the scratch directory. Reviewers must compare the theorem names, axiom sets, source/dependency identities and the final `BRIDGE_PASS` marker, rather than requiring identical progress-message formatting.
