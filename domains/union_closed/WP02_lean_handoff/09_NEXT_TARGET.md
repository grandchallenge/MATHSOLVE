# Next Analytic Target

WP02 is accepted. Its definitions and elementary lemmas compile under CI.

The immediate restricted extension is already checked in WP04:
`UC-WP04-L001`, the two-element-member case.

WP05 has reconstructed Bouchard's lattice-minimal-counterexample conditions.
The checked targets now include `UC-WP05-L001`, the two-atom condition, and
`UC-WP05-L004`, Bouchard's Theorem 2.3 excluding an inf-irreducible strictly
below a sup-irreducible in a minimum counterexample. Both deletion directions
needed for these arguments are proved in Lean.

`UC-WP05-L005`, Bouchard's Corollary 2.4, is also checked: the top element is
the join of two proper elements.

`UC-WP05-L006`, Bouchard's Lemma 2.5, is checked in the exact form
`2 * |up(x)| = |L| + 1` for every doubly irreducible element.

`UC-WP05-L007`, Bouchard's Theorem 2.6, is checked: a minimum counterexample
has at most one doubly irreducible element.

`UC-WP05-L008`, Bouchard's Theorem 1.4, is checked in both dual directions:
deleting a finite homogeneous set of sup-irreducibles or inf-irreducibles
leaves a lattice.

`UC-WP05-L009`, Bouchard's Theorem 2.9, is checked: every nonempty finite set
`M` of inf-irreducibles contains a strict majority above some
sup-irreducible `j`, expressed without division as
`M.card < 2 * upperConeInterCard j M`.

`UC-WP05-L010` and `UC-WP05-L011`, Bouchard's Corollaries 2.10 and 2.11, are
checked as direct applications of Theorem 2.9 to all inf-irreducibles and to a
two-element set.

`UC-WP05-L012`, Bouchard's Theorem 2.12, is checked: every inf-irreducible
element lies above a sup-irreducible `j` satisfying
`2 * upperConeCard j = Fintype.card L + 1`.

`UC-WP05-L013`, Bouchard's Theorem 2.13, is checked: for every non-endpoint
element, the elements incomparable with it do not form a chain. The proof
uses a reusable upper-interval closure map, endpoint irreducibility for finite
incomparable chains, exact cone partitions, and the minimum-counterexample
contradiction.

`UC-WP05-L014`, Bouchard's Corollary 2.14, is checked: every non-endpoint
element is incomparable with at least three elements. The proof splits the
finite incomparable set into the source cases `0`, `1`, and `2`, using
Theorem 2.13 for chain cases and Theorem 2.6 for the two-element non-chain
case.

Theorem 2.15 and its sublattice criteria have now been source-assessed as
`UC-WP05-C015`. The theorem should not be promoted wholesale as a single Lean
result yet. Its first branch uses a finite-lattice enumeration claim for
lattices of size `4..7`, while its second branch is a deletion/minimality
argument under a dual-atom cardinality-gap hypothesis.

`UC-WP05-L015`, the branch (ii) theorem, is now checked. The formal statement
uses an embedded finite lattice `K ↪o L` to represent an induced finite
subposet. If `L` is a minimum counterexample, `2 < |K|`,
`|K| + 2 < |L|`, and some coatom `d` of `L` satisfies `d <= e(top_K)`,
then a non-endpoint of `K` touches the ambient boundary.

`UC-WP05-C016` now certifies the branch (i) finite-lattice enumeration fact by
independent exact replay. The replay enumerates all strict partial orders whose
labels are a linear extension, filters for lattices, canonicalizes under all
relabelings, reproduces the unlabeled counts `2`, `5`, `15`, and `53` for
sizes `4..7`, and finds zero lattices with fewer than two doubly irreducible
elements.

`UC-WP05-L016` is now checked as the Lean transfer theorem for branch (i): if
an embedded finite lattice subposet contains two distinct internally doubly
irreducible elements, then it must touch the ambient boundary in a minimum
counterexample. Together, `UC-WP05-C016`, `UC-WP05-L016`, and `UC-WP05-L015`
certify the full source Theorem 2.15 as the hybrid package claim
`UC-WP05-C015`; it is not a single Lean theorem.

Bouchard's v1 source ends at Theorem 2.15; there is no later source theorem in
this paper to move to.

Rival's length theorem and Bouchard's Theorem 2.7/Corollary 2.8 are now
locally checked. `LatticeLength.lean` still provides the conditional wrappers
`UC-WP05-L017` and `UC-WP05-L018`, but `RivalLength.lean` now adds
source-style endpoint-inclusive irreducibility, proves Rival's finite lattice
length inequality as `rival_length_bound_source`, derives
`minimumCounterexample_rivalBound`, and promotes the nonconditional wrappers
`UC-WP05-L017A` and `UC-WP05-L018A`.

Bouchard's v1 source spine is therefore complete through Theorem 2.15 and the
formerly external Rival dependency for Theorem 2.7/Corollary 2.8 is no longer a
blocker. Next formal target: pause for source selection rather than extending
the ideal-family branch ad hoc. If that branch is activated, do it only through
a translation layer to the existing public Lean development.
