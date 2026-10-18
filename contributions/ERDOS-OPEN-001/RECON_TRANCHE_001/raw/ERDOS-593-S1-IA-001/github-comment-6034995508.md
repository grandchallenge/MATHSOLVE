GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-593-S1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-593-S1
assignment: ERDOS-593-S1
disposition: COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement

The protected formalization's proposed sufficient implication

finite 3-uniform F is 2-colorable (Property B) => F is obligatory

is false in ZFC under the protected embedding semantics.

Péter Komjáth, "Some Remarks on Obligatory Subsytems of Uncountably Chromatic Triple Systems", Combinatorica 21(2) (2001), 233-238, DOI 10.1007/s004930100021, MR1832448, defines "obligatory" by exactly the relevant injective edge-preserving, non-induced embedding condition into every triple system of uncountable chromatic number. Theorem 4, p.237, constructs the explicit finite tripartite triple system
V(F)={x0,x1,y0,y1,z0,z1},
E(F)={{xi,yj,zk}: i,j,k in {0,1}},
together with a triple system H satisfying |H|=Chr(H)=aleph_1 and omitting F.

The tripartition itself makes F 2-colorable: color the x-class one color and the y- and z-classes the other. Thus F.IsTwoColorable holds while IsObligatory F fails, directly refuting the protected two_colorable_implies_obligatory variant and therefore the protected biconditional.

Komjáth 2001 also proves stronger necessary structure: Theorem 1 reduces obligatoriness to 2-connected components; Theorem 2 says every obligatory triple system is tripartite; Theorem 3 gives, for every natural n and infinite cardinal kappa, a kappa-chromatic triple system of cardinality kappa every subsystem of size at most n of which is tripartite.

A newer primary-source claim is Eric Li, "A Resolution of Erdős Problems 593 and 1177: Obligatory Triple Systems and Exact Spectra", arXiv:2606.24882 (2026). It claims a complete ZFC classification; this return records that claim as source evidence only and does not certify the proof.

## Derivation

Historical/interface dependency map:

- Erdős-Galvin-Hajnal 1975, "On set-systems having large chromatic number and not containing prescribed subsystems", Colloq. Math. Soc. János Bolyai 10, pp.425-513, MR0398876: historical source for the obligatory-subsystem characterization problem. Semantic match to the characterization target; no support established here for the false Property-B biconditional.
- Komjáth 2001, pp.233-234: definition of obligatory. Exact semantic match to protected injective, edge-preserving, non-induced embedding semantics.
- Komjáth 2001, Theorem 1: finite F obligatory iff every 2-connected component is obligatory.
- Komjáth 2001, Theorems 2-3: obligatory implies tripartite; arbitrary-infinite-kappa witnesses show fixed finite non-tripartite systems can be avoided.
- Komjáth 2001, Theorem 4 p.237: explicit 6-vertex 8-edge tripartite F omitted by an aleph_1-chromatic triple system. Direct conflict with protected two_colorable_implies_obligatory.
- Erdős-Hajnal 1966, "On chromatic number of graphs and set-systems", Acta Math. Acad. Sci. Hungar. 17, 61-99, DOI 10.1007/BF02020444, MR0193025: primary source for the graph-case obligatory iff bipartite result, via Corollary 5.6 and Theorem 7.4.
- Erdős-Hajnal-Rothschild 1973, "On chromatic number of graphs and set systems", Lecture Notes in Mathematics 337, pp.531-538, MR0387103: source interface yielding the necessary linearity condition for obligatory uniform hypergraphs.
- Hajnal-Komjáth 2008, "Obligatory subsystems of triple systems", Acta Math. Hungar. 119, 1-13, DOI 10.1007/s10474-007-6231-2, MR2400791: positive obligatory structure under a linearity-type exclusion.
- Komjáth 2008, "An uncountably chromatic triple system", Acta Math. Hungar. 121, 79-92, DOI 10.1007/s10474-008-7179-6: consistency result only, not a ZFC theorem.
- Reiher, "Obligatory hypergraphs", arXiv:2403.11223; Proc. Amer. Math. Soc., DOI 10.1090/proc/17021: proves obligatory private-vertex expansions K_(n,n)^(k) and records further cycle information.
- Li 2026, arXiv:2606.24882: claims a complete ZFC classification and exact-cardinal constructions; primary-source claim only, not independently certified here.

The graph analogue is semantically sound: finite obligatory graphs are exactly bipartite, with the negative direction supplied by high-odd-girth uncountably chromatic witnesses.

Higher-uniform information is materially stricter than Property B. Published source evidence gives necessary linearity and tripartiteness, structural decomposition, positive obligatory atoms from private-vertex expansions, negative cycle information, and set-theoretic distinctions that must remain explicit.

## Assumptions beyond bootstrap

No extra mathematical assumption is needed for the counterexample; Komjáth 2001 Theorem 4 is used as a ZFC theorem. The CH sentence preceding that construction is not used, and Komjáth 2008 is treated only as a consistency result. Li 2026 is treated only as a recent primary-source claim of resolution pending independent theorem-grade certification.

## Verification / falsification hooks

1. Verify Komjáth 2001 pp.233-234 and Theorems 1-4, especially the six-vertex eight-edge F in Theorem 4 p.237.
2. Encode that F and mechanically verify its 2-coloring; the source theorem then supplies the aleph_1-chromatic F-free host.
3. Source-lock Erdős-Hajnal 1966 Corollary 5.6 and Theorem 7.4 for the graph analogue.
4. Inspect EGH75 Theorem C and Theorem 11.6 directly before formal import.
5. Verify Reiher's theorems on K_(n,n)^(k) and even expanded cycles.
6. Independently proof-audit Li arXiv:2606.24882 before any status promotion.

## Claim boundary

This return establishes a source-grade counterexample to the protected Property-B sufficient implication and hence to the protected Property-B biconditional. It does not certify a complete answer to Erdős #593; the historical target remains characterization of finite obligatory triple systems. Published sources support the stronger necessary condition obligatory => tripartite, while the 2026 claimed full classification remains uncertified here.

## Next residual

Repair the protected ERDOS-593 interface by marking two_colorable_implies_obligatory refuted using Komjáth's six-vertex witness and retaining obligatory_implies_two_colorable only as a weak consequence of tripartiteness. Then open a separate certification lane for arXiv:2606.24882 to verify or falsify its claimed ZFC classification before any status promotion.