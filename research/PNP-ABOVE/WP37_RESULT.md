# WP37 — Semantic boundary expansion, native SAT width, and affine shortcut obstruction

Pinned upstream: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970` (Lean 4.35.0-rc3). Protected predecessor WP36B #1292. Question: can logical interaction rather than input access force unrestricted classical decision time? No such time lower bound is claimed.

## Semantic theorem

Let P_v be predicates on Boolean assignments indexed by constraints v and variables e. A line Q depends on finite support F if agreement on F preserves its truth. A derivation starts with any consequence of one constraint and uses any sound binary semantic inference Q,R -> U; each line has support at most w. The Boolean form of a line is unrestricted. Support and fan-in are restricted: this is NOT a computation model for arbitrary algorithms.

One-way RepairLaw requires that flipping an incident variable repairs a false constraint, while flipping a nonincident variable preserves truth. Every disjunctive clause with one fixed polarity per variable satisfies it. For deletion-minimal S entailing Q, every variable occurring in exactly one constraint of S must belong to every support of Q: otherwise repair that constraint while preserving all others and Q, contradicting minimality. If all subsystems of at most k constraints are satisfiable, a binary refutation must pass through a line with deletion-minimal witness of size k < |S| <= 2k. If every such S has more than w unique boundary variables, no width-w refutation exists. This is a width obstruction, not a proof-length or algorithmic time theorem.

## Explicit native SAT family

Use V=Fin N with N=2^q and E=V×V. Each ordered off-diagonal pair is a separate variable incident at both endpoints; diagonal variables are unused. Impose vertex parity, charge one at a fixed root and zero elsewhere. The sum of vertex parities is zero in F₂; the charge sum is one. Every proper subsystem is satisfiable, because a single defect can be moved along a path to an omitted vertex.

For S of size s, at least s(N-s) distinct ordered pairs cross to the complement. If 1<=k, 3k<=N and k<s<=2k, then s(N-s)>=k(k+1)>k². Thus any binary semantic refutation has a line supported on more than k² variables. With k=floor(N/3), this is quadratic in vertex count and linear in available edge-variable count.

The native encoding uses actual MIPRE.SAT.Fml.xor via balanced trees, no additional variables. nativeSubsys_sat_iff proves satisfiability equivalence of every subsystem. Native full encoding length <= N*(N^4*(8q+25)+7)+9 <= 33N^6+7N+9. native_semantic_width pulls every derivation on arbitrary natural-number variable identifiers back to edge assignments with no increase in support, so fresh variable names cannot evade the bound in this proof system. Full native formula unsatisfiable; every proper vertex subsystem satisfiable. WP34 compressed promise equivalence applies at valid indices above its threshold, but no new compressed decision-time transfer is inferred.

## Obstruction to a width-to-time argument

The stronger two-way FlipLaw says each incident variable always reverses truth and nonincident variables never change truth. flip_law_iff_affine classifies this entire finite-variable class exactly as affine equations over F₂, with charge determined by truth at the all-zero assignment. Given incidence and charge data, the class is polynomial-time decidable by Gaussian elimination. We do not claim efficient recovery of incidence from arbitrary opaque succinct predicates.

For the complete graph even Gaussian elimination is unnecessary: complete_sat_iff_even proves satisfiability for arbitrary charges iff sum_v c_v=0. A star assignment sets only outgoing edges from a root to vertices of charge one and satisfies each nonroot equation; the aggregate identity settles the root. Thus high semantic width and minimal global inconsistency coexist with an elementary decision algorithm for the explicit varying-charge presentation. A generic width-to-unrestricted-time implication is invalid. A compiler that always extracts a subquadratic-support binary semantic refutation from an efficient correct solver on this family would contradict the width theorem.

## Boundary and next work

Non-affine constraints under the weaker repair law remain eligible. A genuine unrestricted time lower bound requires an invariant of unrestricted computation or a justified transformation to a lower-bound model. Even superpolynomial refutation size in a named system would not suffice without such a transformation. No superpolynomial decision-time lower bound, standard machine concordance, P≠NP, or external certification is claimed.

Prior art: Ben-Sasson and Wigderson, Short Proofs Are Narrow—Resolution Made Simple (JACM 2001), https://people.inf.ethz.ch/emo/SatSem05/Papers/BensassonWidgerson01.pdf . Boundary expansion and parity constraints are classical. No novelty is claimed for the underlying Tseitin/resolution argument or parity solving. Programme-specific contribution: exact kernel-checked native SAT correspondence, semantic support transfer, and affine classification boundary.

Replay: seven new modules against pinned upstream Mathlib and original native FmlProg, without WP08–WP36 generated modules. WP37_REPLAY.py locks exact sources and audits all 64 theorem declarations. Internal logical audit covers repair, crossing witnesses, parity identities, balanced formula size, support restriction, and absence of an unrestricted-time implication.
