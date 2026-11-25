# ERDOS-OPEN successor-002: protected synthesis

Evidence: MATHSOLVE protected PRs #1021 (470-S2), #1022 (593-R2), and #1023 (593-S2). Separate closure records bind exact raw payloads, receipts, comment IDs and merge commits. Both 593 returns were collected independently before comparison. These are worker contributions, not automatically accepted proofs.

## 593: structural reduction

Define a 3-uniform hypergraph T on vertices consisting of unordered pairs from an index set X. For each three distinct indices a,b,c, add the hyperedge formed by the three unordered pairs ab, bc, ac. Two different hyperedges of T intersect in at most one pair: sharing two would recover the same three indices. This elementary proof is independent of any literature. The native checker reproduces linearity for X of sizes 3 through 7.

If X has cardinality (2^aleph0)^+, the classical Erdős-Rado partition theorem says that every countable coloring of pairs of X contains a homogeneous triple (indeed an uncountable homogeneous set). Subject to independently verifying the precise theorem and its hypotheses, T is uncountably chromatic. Injectivity preserves intersection sizes of hyperedges. Thus no non-linear finite 3-uniform F can embed into a linear H, and after the host theorem is discharged such F is not obligatory.

**R2 correction:** The assertion that a two-coloring of all pairs of the continuum can avoid monochromatic triangles is false. The native replay exhausts all 32768 two-colorings of K6; each contains a monochromatic triangle. A two-coloring of K5 without such a triangle exists by coloring a 5-cycle red and its complement blue.

There is instead an elementary countable-color construction on an index set of cardinality at most the continuum: inject indices into infinite binary sequences and color a pair by the least differing coordinate. Three binary sequences cannot have their pairwise first disagreement at the same coordinate. Hence there is no monochromatic triangle. This is a *countable* coloring, not a two-coloring. Finite analogues at binary lengths 2 through 5 are checked in the native replay. The successor cardinal threshold applies to this explicit construction, not to all possible linear hosts.

## 593: external classification lane

S2 identifies Eric Li's arXiv:2606.24882v2 and the public Lean repository ericlisg/erdos-593-1177-lean. The repository and PublicationCertificate.lean were located; inspected repository head: 5dcb6e4906df03f2e4294b21be73b55db7736f5a. The source *claims* an unconditional kernel-checked full classification. GCL has not yet independently built that pinned dependency tree, checked its axiom report, or matched all definitions with the protected formal interface. Therefore this is SOURCE_REPORTED_NOT_VERIFIED, not an independently certified theorem. S2's stronger omega_1 host-size claim is likewise not promoted without its theorem body.

## 470: computational source lane

S2 identifies Fang's arXiv:2207.12906v1 and fwjmath/ows-data commit 88d22faf46400f0050287c3c32c9a807ca3b1340. That GitHub commit exists. Neither the full data-1e21 prefix cover nor sampled workunit checksums nor subset-sum witness certificates were independently replayed here. A terminal 'c' marker alone cannot establish exhaustive coverage. The claimed six-distinct-prime-divisor theorem body remains source-gated. Neither the search exclusion N < 10^21 nor that factor restriction is certified.

## Decision

The exact evidence receipts, the elementary linearity/nonembedding proofs, finite Ramsey contradiction, and first-difference construction are accepted as bounded *internal* findings. The transfinite host theorem is external-source conditional. The Li classification, Lean kernel build, and Fang exhaustive workunit coverage remain unverified.

Three bounded successors are specified under work_packages/ERDOS_OPEN/:

- ERDOS-593-N3-SOURCE-KERNEL-FIDELITY;
- ERDOS-593-N4-CARDINAL-HOST-LOCK;
- ERDOS-470-N3-WORKUNIT-COVER-REPLAY.

They are READY_FOR_PROTECTED_DISPATCH only. The ordinary protected queue registration, immutable task source and authenticated worker-pickup mechanisms must run before they become AVAILABLE. No parent problem closure, mathematical certification, publication, or prize effect follows from this record.
