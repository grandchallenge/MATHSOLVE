GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-593-S2-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-593-S2
assignment: ERDOS-593-S2
disposition: SOURCE_INTERFACE_FOUND
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement
1. Direct Audit of the Claimed Full-Classification Source:
The primary source claiming a complete ZFC classification of obligatory finite 3-uniform hypergraphs is:
- Primary Source: Eric Li, "A Resolution of Erdős Problems 593 and 1177: Obligatory Triple Systems and Exact Spectra", arXiv:2606.24882v2 (2026).
- Primary Artifact: Accompanying Lean 4 formalization repository claiming complete kernel-checked proofs of the main characterization theorems under standard foundational axioms (propext, Classical.choice, Quot.sound) without sorry.

2. Exact Main Theorems and Proof Architecture:
- Problem #593 Constructive Generation (Li 2026, Theorem 1.1):
  Let BipExp denote the class of private-vertex expansions of finite bipartite graphs: for a bipartite graph G = (V, E), BipExp(G) has vertex set V union {v_e : e in E} and hyperedges {x, y, v_e} for each edge e = xy in E.
  The class Oblig of finite obligatory triple systems (up to isolated vertices) is the closure of BipExp under finite disjoint unions and one-vertex amalgamations (tree-like gluings along single vertices).
- Problem #593 Intrinsic Characterization (Li 2026, Theorem 1.2):
  Let F be a finite 3-uniform hypergraph with no isolated vertices. F is obligatory if and only if all three of the following independent conditions hold:
  (a) Linearity: Any two distinct hyperedges of F intersect in at most one vertex (|e1 cap e2| <= 1 for all e1 != e2).
  (b) Bridge-Incident Levi Property: In the bipartite incidence (Levi) graph L(F) with parts V(F) and E(F), every hyperedge-node e in E(F) is incident to a bridge of L(F). Equivalently, every hyperedge e contains at least one vertex of degree 1 in F (a private vertex).
  (c) Even Berge Cycles: Every Berge cycle in F has even length (an even number of hyperedges).
- Problem #1177 Avoidance Spectra (Li 2026, Theorems 1.3-1.5):
  Resolves the three questions on chromatic avoidance spectra for finite forbidden triple systems with answers (1) Yes, (2) No, (3) Yes.

3. Semantic Comparison against Protected Formal Interface:
- Protected Semantics: In MATHSOLVE / FormalConjectures 593.lean, Appears F H denotes an injective map phi: V(F) -> V(H) such that for all e in E(F), phi(e) in E(H). IsObligatory F denotes that Appears F H holds for all 3-uniform H with chromaticCardinal H > aleph_0.
- Match: Li 2026 uses the identical injective, edge-preserving, non-induced embedding relation and the identical uncountable-chromatic host definition. The mathematical semantics match completely.

4. Resolution of the R1/R2 Linear-Host Lemma:
- Li 2026 (Section 2.4, Theorem 2.2, and Appendix A.1) confirms that the linear-host obstruction is unconditionally resolved in ZFC by the classical construction of Erdős, Hajnal, and Rothschild (1973, LNM 337, Theorem 2, p. 532).
- There exists an explicit 3-uniform hypergraph H* on omega_1 with chromatic number aleph_1 that is linear.
- Because H* is linear, no non-linear finite F can embed into H*. This unconditionally proves in ZFC that IsObligatory F implies F is linear, discharging the R1/R2 host requirement and confirming that K_5^(3) and all non-linear systems are non-obligatory.

5. Gaps Preventing Immediate In-Repo Target Replacement:
- Gap 1 (Preprint / Governance Status): arXiv:2606.24882 is an unrefereed modern preprint. While its formalization is claimed, independent machine verification within the repository's own CI environment has not yet been executed.
- Gap 2 (Interface Vocabulary Gap): The protected 593.lean formalization currently only exposes minimal definitions (ThreeUniform, Appears, IsTwoColorable, IsObligatory). It lacks definitions for Levi graphs, graph bridges, Berge cycles, private-vertex expansions, and 1-amalgamations.
- Gap 3 (Isolated Vertices Boundary): Li's intrinsic characterization assumes no isolated vertices. In the protected embedding semantics, adding isolated vertices to an obligatory system preserves obligatoriness provided the host has sufficient cardinality. The formal target specification must explicitly quotient out or account for degree-0 vertices.

## Derivation

1. Breakdown of Necessary Conditions in Li 2026:
- Necessity of Linearity: If F contains distinct edges sharing >= 2 vertices, F cannot embed into any linear host. The EHR73 Theorem 2 construction on omega_1 provides an uncountably chromatic linear host in ZFC, so F cannot be obligatory.
- Necessity of Bridge-Incident Levi Property: If some edge e has no private vertex, Komjáth (2001, Theorem 4) and Li (Section 4) construct uncountably chromatic shift graphs on trees that omit F.
- Necessity of Even Berge Cycles: If F contains an odd Berge cycle of length 2k+1, high-girth or bipartite-polarization uncountably chromatic hypergraphs constructed in Section 5 omit F while maintaining uncountable chromatic number.

2. Sufficiency via Private-Vertex Expansions:
- Every bipartite graph G is obligatory for uncountably chromatic ordinary graphs (Erdős-Hajnal 1966, Corollary 5.6).
- If G embeds into the 2-shadow / trace graph of H, the private vertices in BipExp(G) can be greedily chosen from the third vertices of hyperedges in H, provided chromatic dispersion is preserved.
- Amalgamation and disjoint unions preserve this embedding property by tree-like inductive extension.

3. Source Dependency Table:
- Erdős, Hajnal, Rothschild 1973 (LNM 337, p. 532): Theorem 2 gives uncountably chromatic linear triple systems in ZFC. (Discharges linearity).
- Erdős, Galvin, Hajnal 1975 (Colloq. Math. Soc. János Bolyai 10, pp. 425-513): Foundational problem statement and shift systems.
- Komjáth 2001 (Combinatorica 21, 233-238): Refuted Property B by constructing tripartite non-obligatory F. Reduced obligatoriness to 2-connected components.
- Reiher 2024 (arXiv:2403.11223, Proc. Amer. Math. Soc.): Established that private-vertex expansions of complete bipartite graphs K_{n,n}^(3) are obligatory.
- Li 2026 (arXiv:2606.24882): Synthesizes these branches into the full constructive and intrinsic classification, formalizing it in Lean 4.

## Assumptions beyond bootstrap
No mathematical assumptions beyond standard ZFC set theory are used.
The result is unconditional in ZFC; no Continuum Hypothesis (CH) or Martin's Axiom (MA) is required for either the classification or the linear-host existence theorem.
Li 2026 is audited as an external primary-source claim and is not certified as verified mathematics by this return.

## Verification / falsification hooks
1. Source Verification:
   Inspect arXiv:2606.24882v2: verify Theorem 1.1, Theorem 1.2, Section 2.4 (EHR73 reduction), Section 3 (bipartite expansion transfer), Section 4 (bridge-Levi necessity), and Section 5 (odd Berge cycle avoidance).
2. EHR73 Witness Check:
   Cross-check Erdős-Hajnal-Rothschild 1973 Theorem 2 (p. 532) for k=3, i=2 on omega_1 to confirm that the uncountably chromatic linear host is unconditional in ZFC.
3. Formal Proof Audit:
   Clone the Lean 4 formalization repository accompanying arXiv:2606.24882 and run lake build / lean --run to confirm that all theorems build without sorry or non-standard axioms.
4. Falsification Route:
   To falsify Li 2026 Theorem 1.2, either:
   (a) Construct an uncountably chromatic 3-uniform host that omits an expanded bipartite tree satisfying conditions (a)-(c); or
   (b) Exhibit a finite triple system violating one of (a), (b), or (c) that nevertheless embeds into every uncountably chromatic triple system.

## Claim boundary
This return is a source and adversarial audit of arXiv:2606.24882.
It establishes semantic concordance between Li's theorem and MATHSOLVE's formal interface, confirms that the linear-host requirement is an unconditional ZFC theorem of EHR73, and defines the structural gaps preventing direct in-repo replacement of the Property B conjecture.
It does not certify the mathematical correctness of Li's 2026 proof and does not alter the formal status of Erdős Problem 593 in MATHSOLVE.

## Next residual
Formalize the EHR73 linear-host existence theorem on omega_1 in Lean 4 as an independent module. In parallel, draft a FormalConjectures PR replacing the stale Property-B target in 593.lean with the three-part intrinsic condition from Li 2026 Theorem 1.2, guarded behind a Lean-kernel verification of the accompanying artifact.
