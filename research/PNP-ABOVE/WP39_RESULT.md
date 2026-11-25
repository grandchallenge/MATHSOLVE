# WP39A — A planted unique-witness obstruction to proof-width transfer

Pinned upstream: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, Lean 4.35.0-rc3. WP37 and WP38B are protected predecessors. This is a negative control on the search-side route, not a general classical lower bound.

## Mathematical construction

Let P_v(a) be any finite unsatisfiable predicate system on variables E and let p:E→Bool be a prescribed assignment. Introduce a fresh selector s. The augmented constraint list consists of:

* G_v(s,a) = (s=true) OR P_v(a), for every original constraint v;
* H_e(s,a) = (s=false) OR (a(e)=p(e)), for every variable e.

If s=false, every G_v reduces to P_v, which is inconsistent. If s=true, every H_e fixes a(e)=p(e), and all G_v hold. Consequently the augmented system has exactly one model (true,p), for any p. The additional constraint s=false makes it unsatisfiable.

The selector-pinned constraints H_e are not affine equations over F₂: they are satisfied at three of the four possible pairs (s,a(e)). In WP37's FlipLaw formulation, flipping s leaves a satisfying H_e true when a(e)=p(e), but reverses its truth when a(e)≠p(e). No fixed incidence relation can describe both. The weaker one-way RepairLaw is preserved under the explicit extended incidence relation: selector flips repair false guarded constraints, original variable flips repair false original constraints on the false branch, and unrelated variables preserve truth. WP39A verifies this for arbitrary RepairLaw systems and the optional false pin. The planted pattern is explicit, not hidden or pseudorandom.

## Proof-width inheritance

Restrict each line of an arbitrary binary semantic derivation on the augmented system to s=false, deleting s from its support. Width cannot increase. An initial consequence of G_v becomes a consequence of P_v; H_e and the optional pin s=false become tautologies, so their restricted consequences follow from any original constraint. Sound binary inference remains sound under restriction. Induction on the derivation proves that every derived predicate restricts to a predicate derivable in the original system at no greater width.

In particular, if the original system admits no width-w refutation, the augmented satisfiable system admits no width-w derivation of the forced literal s=true, and the augmented system with s=false admits no width-w refutation. This holds for arbitrary predicates on proof lines, not only clauses, and for every planted p.

Instantiate the original system with WP37's complete ordered-pair odd-charge parity family on N vertices. For 1≤k and 3k≤N, the forced selector requires width greater than k². The same holds for refuting the wrong branch. Nevertheless its unique model is given by inspection. The constraint system uses a partition of the original formulas as premises; supplying their entire conjunction as one premise would invalidate the width claim, since then the forced literal itself is a single semantic consequence.

## Native SAT and witness interface

The native compiler reserves identifier 0 for the selector and shifts WP37's edge identifiers by one. Each guarded parity constraint is an actual original Fml; each guarded pin uses two literals. The full conjunction of all constraints has the explicit satisfying assignment i↦(i=0) and every model agrees with it on the selector and indexed edge variables. Arbitrary unused native variable names do not change the specified model. The source proof pulls derivations back through this injection, with non-increasing support, including fresh natural-number identifiers. Explicit plantedBits evaluates to true on every unpinned subsystem and the full family. By WP35 support enumeration and WP38 model-bits verification, a dense witness can be constructed by mapping identifier equality to zero; separate WP39B will bind the actual PolyTimeFun composition to this source.

The significance is a falsification test of the implication “unique satisfying assignment + non-affine constraints + large semantic width for a forced decision implies high unrestricted witness-construction time.” The mathematical construction gives the counterexample, and the new original native modules compile in the development environment. Width alone cannot detect whether a solver even considers the wrong branch. No claim is made that all non-affine systems are easy, that every algorithm admits narrow proofs, or that the hard SAT instances have been found.

## Admission boundary

Development compilation passes. Fresh exact source-lock replay, standard-axiom audit and protected merge/readback remain separate gates. The replay stages seven exact source-matched WP37 modules and freshly checks both WP39A modules (29 theorem declarations). The finite executable control checks all 324 disjoint two-bit truth-table/plant pairs and N=2,3,4 complete graphs (32, 1024, 131072 assignments), each with exactly one planted model; this is not the width proof. No independent certification. WP38's unrestricted search lower bound remains open.
