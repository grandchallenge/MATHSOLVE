# WP05: Lattice-Minimal-Counterexample Theorem Spine

Source reconstructed from [Bouchard, 2025](https://arxiv.org/abs/2503.00277).

## 1. Exact setup

For a finite lattice `L`, let `up(j) = {x | j <= x}`. Bouchard's lattice form of
Frankl states that every finite lattice with more than one element has a
join-irreducible `j` satisfying `2 * |up(j)| <= |L|`.

A counterexample therefore satisfies
`2 * |up(j)| > |L|` for every join-irreducible `j`. The source then fixes a
counterexample `L_tilde` of minimum cardinality among all counterexamples.

The paper defines join-irreducible and meet-irreducible by unique lower and
upper covers, respectively. In finite lattices these correspond to mathlib's
`SupIrred` and `InfIrred`, subject to checking endpoint conventions.

## 2. Source theorem spine

| Source result | Exact necessary condition | Main dependency |
|---|---|---|
| Lemma 1.2 | Deleting one join-irreducible or meet-irreducible element leaves a lattice. | Finite-lattice cover analysis. |
| Theorem 1.4 | Deleting any set consisting entirely of join-irreducibles, or entirely of meet-irreducibles, leaves a lattice. | Iterated Lemmas 1.2 and 1.3. |
| Theorem 2.1 | Every join-irreducible `j`, with unique lower cover `x`, has an upper cover `y` that lies below no join-irreducible and covers exactly `j` and one other element `z`, with `x < z`. | Delete `j`; contradict minimum cardinality. |
| Corollary 2.2 | The bottom element is meet-reducible. Equivalently under the source convention, the lattice has at least two atoms. | Theorem 2.1. |
| Theorem 2.3 | No meet-irreducible element lies below a join-irreducible element. | Delete a meet-irreducible; contradict minimum cardinality. |
| Corollary 2.4 | The top element is join-reducible. | Theorem 2.3. |
| Lemma 2.5 | A doubly irreducible element `x` has `2 * |up(x)| = |L| + 1`. | Delete `x`; parity/cardinality comparison. |
| Theorem 2.6 | There is at most one doubly irreducible element. | Lemma 2.5 and deletion of two irreducibles. |
| Theorem 2.7 | Every join-irreducible has upper cone cardinality greater than lattice length. | Checked unconditionally as `UC-WP05-L017A` after local Rival formalization `UC-WP05-L019`; the conditional wrapper `UC-WP05-L017` is retained. |
| Corollary 2.8 | Every doubly irreducible element lies below a doubly reducible element. | Checked in non-top form as `UC-WP05-L018A` after local Rival formalization `UC-WP05-L019`; the conditional wrapper `UC-WP05-L018` is retained. |
| Theorem 2.9 | For every nonempty set `M` of meet-irreducibles, some join-irreducible `j` satisfies `2 * |up(j) intersect M| > |M|`. | Delete `M`; contradict minimum cardinality. |
| Theorem 2.12 | Every meet-irreducible `m` lies above a join-irreducible `j` with `2 * |up(j)| = |L| + 1`. | Lemma 2.5 and deletion of `m`. |
| Theorem 2.13 | For every non-endpoint `x`, the elements incomparable with `x` do not form a chain. | Restrict to the upper interval and use earlier conditions. |
| Corollary 2.14 | Every non-endpoint element is incomparable with at least three elements. | Theorems 2.13 and 2.6. |
| Theorem 2.15 | Certain lattice subposets of a minimum counterexample must have a non-endpoint that covers or is covered by an outside element. | Hybrid-certified as `UC-WP05-C015`: branch (ii) is checked as `UC-WP05-L015`; branch (i) combines the replay certificate `UC-WP05-C016` with the Lean transfer theorem `UC-WP05-L016`. |

## 3. Dependency graph

```text
cover definitions
  -> deletion preserves lattice (Lemma 1.2)
  -> irreducibility survives deletion (Lemma 1.3)
  -> delete a homogeneous set of irreducibles (Theorem 1.4)

minimum-counterexample predicate + upper-cone cardinality
  -> local cover configuration (Theorem 2.1)
  -> bottom meet-reducible (Corollary 2.2)

Lemma 1.2
  -> meet/join irreducibles cannot be ordered (Theorem 2.3)
  -> top join-reducible (Corollary 2.4)

Lemma 1.2 + Theorem 1.4
  -> exact cone size for doubly irreducibles (Lemma 2.5)
  -> at most one doubly irreducible (Theorem 2.6)
```

## 4. Checked targets

The first exact formalization target was `UC-WP05-L001`:

> If `L` is a minimum-cardinality finite-lattice counterexample to the lattice
> form of Frankl's conjecture, then `L` has at least two atoms.

This is Corollary 2.2 of the source. It is selected because its statement uses
standard finite-lattice notions, exposes whether the source and mathlib
irreducibility conventions agree, and forces the minimum-counterexample
predicate and deletion infrastructure to be specified before deeper results are
attempted.

## 5. Lean implementation

The selected target is now checked in:

- `MATHCERT/MathCert/Domains/UnionClosed/LatticeDeletion.lean`
- `MATHCERT/MathCert/Domains/UnionClosed/LatticeMinimum.lean`

The implementation defines the upper-cone cardinality, lattice counterexample,
and minimum-cardinality counterexample predicates. For a sup-irreducible
element `a`, the induced subtype deleting `a` receives inherited joins; any meet
equal to `a` is replaced by the greatest element strictly below `a`.

For `UC-WP05-L001`, assume there is only one atom `a`. The formal proof shows:

1. every nonbottom element lies above `a`;
2. deleting `a` preserves join-irreducibility of the remaining
   join-irreducibles;
3. their upper cones are equivalent before and after deletion;
4. the deleted lattice remains a counterexample;
5. its cardinality is strictly smaller, contradicting minimum cardinality.

This is a direct formalization of the deletion argument needed for Corollary
2.2; it does not take Bouchard's Theorem 2.1 as an assumption.

The dual deletion construction is now checked as `UC-WP05-L003`. For an
inf-irreducible element `m`, meets are inherited and any join equal to `m` is
replaced by the least element strictly above `m`.

That machinery proves `UC-WP05-L004`, Bouchard's Theorem 2.3. If an
inf-irreducible `m` lay strictly below a sup-irreducible `j`, deleting `m`
would preserve a counterexample:

1. old sup-irreducibles keep enough elements in their upper cones;
2. any new sup-irreducible created by deletion is the unique upper cover of
   `m`;
3. its upper cone is bounded using the original upper cone of `j`;
4. the deleted lattice is strictly smaller, contradicting minimum cardinality.

Corollary 2.4 is now checked as `UC-WP05-L005`. A finite nontrivial lattice
has a coatom, and every coatom is inf-irreducible. If top were
sup-irreducible, Theorem 2.3 would forbid that coatom from lying strictly below
top. Lean then unfolds non-sup-irreducibility at top to produce two proper
elements whose join is top.

Lemma 2.5 is now checked as `UC-WP05-L006` in the division-free form
`2 * |up(x)| = |L| + 1`. The formal proof first obtains the lower bound from
the counterexample condition. If the upper cone were any larger, deleting the
doubly irreducible element would leave a smaller counterexample:

1. deleting one point reduces the lattice cardinality by exactly one;
2. every relevant upper cone loses at most the deleted point;
3. new join-irreducibles created by deletion occur at the upper cover of the
   deleted element and satisfy the same one-point-loss bound;
4. the assumed strict excess makes every remaining upper cone a strict
   majority, contradicting minimum cardinality.

Theorem 2.6 is now checked as `UC-WP05-L007`. Two distinct doubly irreducible
elements cannot be comparable by the checked Theorem 2.3. If they are
incomparable, deleting the first preserves both irreducibility predicates of
the second, so it can be deleted next. The formal proof then:

1. proves upper-cone cardinality grows strictly down a strict order relation;
2. bounds the loss from each deletion by at most one point;
3. handles join-irreducibles inherited from the original lattice and those
   created at either upper cover;
4. shows the twice-deleted lattice remains a counterexample, contradicting
   minimum cardinality.

Theorem 1.4 is now checked as `UC-WP05-L008` in both dual directions. The Lean
construction works directly on the subtype outside a finite deleted set:

1. after deleting sup-irreducibles, joins are inherited and the new meet is
   the supremum of all surviving common lower bounds;
2. sup-irreducibility guarantees this supremum cannot be one of the deleted
   elements;
3. dually, after deleting inf-irreducibles, meets are inherited and the new
   join is the infimum of all surviving common upper bounds;
4. no claim is made for a mixed set of sup- and inf-irreducibles, matching the
   source boundary.

Theorem 2.9 is now checked as `UC-WP05-L009`. The formal proof replaces the
source's maximal-chain analysis with an equivalent closure-map argument:

1. every lattice element maps to the least surviving element above it after
   deleting the inf-irreducible set `M`;
2. this map preserves joins and is onto the deleted lattice;
3. every sup-irreducible in the deleted lattice therefore has an original
   sup-irreducible `j` mapping to it;
4. the original cone `up(j)` partitions exactly into the surviving cone and
   `up(j) intersect M`;
5. if no `j` met a strict majority of `M`, the deleted lattice would remain a
   smaller counterexample, contradicting minimum cardinality.

Corollaries 2.10 and 2.11 are now checked as `UC-WP05-L010` and
`UC-WP05-L011`. They are direct specializations of Theorem 2.9:

1. Corollary 2.10 takes `M` to be the finite set of every inf-irreducible
   element; a coatom proves this set is nonempty;
2. Corollary 2.11 takes `M = {m₁, m₂}`; strict majority forces the resulting
   sup-irreducible below both members, including when `m₁ = m₂`.

Theorem 2.12 is now checked as `UC-WP05-L012` in the statement:

```text
InfIrred m ->
  exists j, SupIrred j /\ j <= m /\
    2 * upperConeCard j = Fintype.card L + 1
```

The proof uses the singleton specialization of the finite deletion machinery:

1. assume every sup-irreducible `j <= m` has
   `Fintype.card L + 1 < 2 * upperConeCard j`;
2. delete the singleton `{m}`;
3. assign every sup-irreducible of the deleted lattice an original
   sup-irreducible origin `j`;
4. if `j <= m`, the exact cone partition loses one point and the assumed
   stronger inequality keeps a strict majority after deletion;
5. if `j` is not below `m`, the cone loses no points and the original
   counterexample inequality is inherited;
6. the deleted lattice is therefore a smaller counterexample, contradicting
   minimum cardinality.

This proof does not need the source's auxiliary assertion that a newly created
join-irreducible forces `m` itself to be join-irreducible. The checked
least-survivor origin theorem handles old and new join-irreducibles uniformly.

Theorem 2.13 is now checked as `UC-WP05-L013`:

```text
x != bottom -> x != top ->
  not IsChain (fun a b => a <= b) (incomparableSet x)
```

The formal proof restricts a hypothetical chain configuration to `Set.Ici x`.
The reusable interval layer proves that joining with `x` is a surjective join
homomorphism and gives every interval join-irreducible an original
join-irreducible origin. The two source branches then become exact counting
arguments:

1. if the greatest incomparable element is doubly irreducible, its unique
   upper cover loses exactly one cone point while at least two points lie
   outside the interval;
2. otherwise every incomparable element is meet-irreducible, the least one is
   the unique doubly irreducible element, and `c |-> (c, x inf c)` injects two
   copies of the incomparable chain into the complement of the interval;
3. in both branches every interval join-irreducible has a strict-majority
   upper cone, making `Set.Ici x` a smaller counterexample.

The ideal-family branch remains deferred. Activating it requires a translation
layer to the existing public Lean development rather than a duplicate local
formalization.

Corollary 2.14 is now checked as `UC-WP05-L014`:

```text
x != bottom -> x != top ->
  3 <= (incomparableFinset x).card
```

The proof follows the source split. If the incomparable set has cardinality
`0` or `1`, it is a chain, contradicting Theorem 2.13. If it has cardinality
`2`, then either the two elements are comparable, again giving a chain, or
they are incomparable with each other. In the latter case each is both maximal
and minimal among the elements incomparable with `x`, so the checked
maximal/minimal incomparable lemmas make both elements doubly irreducible,
contradicting Theorem 2.6.

The public set-family representation remains `Family alpha := Finset (Finset
alpha)`. WP05 is a separate finite-lattice layer.

## 6. Theorem 2.7 and Corollary 2.8 assessment

Theorem 2.7 and Corollary 2.8 are source-audited as `UC-WP05-C018`. Their
former external dependency, Rival's finite lattice length inequality, is now
formalized locally as `UC-WP05-L019`:

```text
|L| >= 2 * (ell(L) + 1) - |Irr(L)|.
```

The local Lean layer has `LatticeLength.lean`, which defines `latticeLength`
as the maximum finite chain cardinality minus one and introduces the
subtraction-free predicate

```text
RivalBound L := 2 * (latticeLength L + 1) <= |L| + |Irr(L)|.
```

`RivalLength.lean` adds Rival's source-style endpoint-inclusive
`RivalSupIrred`, `RivalInfIrred`, and `rivalDoublyIrredFinset`, proves the
source inequality for every finite bounded lattice, and then derives
`minimumCounterexample_rivalBound` by endpoint transfer. The transfer uses
`UC-WP05-L001` to exclude bottom from source-style double irreducibility and
`UC-WP05-L005` to exclude top.

The conditional Theorem 2.7 wrapper remains checked as `UC-WP05-L017`, and
the unconditional promoted theorem is now checked as `UC-WP05-L017A`:
`IsMinimumCounterexample L -> SupIrred j ->
latticeLength L < upperConeCard j`.

The conditional non-top form of Corollary 2.8 remains checked as
`UC-WP05-L018`, and the unconditional promoted theorem is now checked as
`UC-WP05-L018A`: every mathlib-style doubly irreducible element `x` lies
strictly below some non-top element `y` with `¬SupIrred y` and `¬InfIrred y`.
The proof still uses the source's upper-cone chain argument; the Rival
hypothesis is now supplied by `minimumCounterexample_rivalBound`.

## 7. Theorem 2.15 assessment

Theorem 2.15 is now recorded as `UC-WP05-C015`, a hybrid-certified package
claim rather than a single checked Lean theorem. The theorem has two different
certification profiles:

1. The small-lattice branch relies on enumeration data for all unlabeled
   lattices of cardinality `4`, `5`, `6`, and `7`, together with the observed
   property that each has at least two doubly irreducible elements. The
   enumeration fact is locally replay-certified as `UC-WP05-C016`, and the
   Lean transfer from two internal doubly irreducible elements to an ambient
   boundary touch is checked as `UC-WP05-L016`.
2. The dual-atom branch is a deletion/minimality argument. It is now checked
   as `UC-WP05-L015`.

The Lean formalization represents the finite subposet as an order embedding
`e : K ↪o L`, with carrier `Finset.univ.image e`. This avoids subtype
typeclass diamonds while keeping the source meaning: the order on `K` is the
ambient order induced by the embedding. The checked proof shows that if
`2 < Fintype.card K`, `Fintype.card K + 2 < Fintype.card L`, and a coatom
`d` of the ambient lattice satisfies `d <= e top`, then some non-endpoint of
`K` covers or is covered by an element outside the embedded carrier.

The proof splits on whether `top : K` is sup-irreducible. If it is not, `K`
itself becomes the smaller counterexample under a no-boundary hypothesis. If
it is, Lean deletes the top element using the checked sup-irreducible deletion
construction and obtains a smaller counterexample after a two-point cone-loss
bound.

The branch (i) certificate is intentionally not a Lean theorem. The replay
enumerates all strict partial orders on `{0,...,n-1}` whose labels are a linear
extension, checks the lattice property by pairwise joins and meets, canonicalizes
the resulting reflexive orders under all relabelings, and verifies the
doubly-irreducible lower bound for sizes `4..7`. It reproduces the unlabeled
counts `2`, `5`, `15`, and `53`, with zero violations.

The branch (i) Lean transfer is `UC-WP05-L016`. Under a no-boundary hypothesis,
internal sup-irreducibility and internal inf-irreducibility both transfer across
the order embedding to the ambient lattice. Two distinct internal doubly
irreducible elements would therefore become two distinct ambient doubly
irreducible elements, contradicting the checked uniqueness theorem
`UC-WP05-L007`.

The detailed assessment is in
`MATHSOLVE/domains/union_closed/WP05_lattice_minimal_counterexample/THEOREM_2_15_ASSESSMENT.md`.

## 8. Certification boundary

- `UC-WP05-L001` is `FORMALIZED/CHECKED`.
- `UC-WP05-L002`, the sup-irreducible deletion construction, is
  `FORMALIZED/CHECKED`.
- `UC-WP05-L003`, the inf-irreducible deletion construction, is
  `FORMALIZED/CHECKED`.
- `UC-WP05-L004`, excluding an inf-irreducible strictly below a
  sup-irreducible in a minimum counterexample, is `FORMALIZED/CHECKED`.
- `UC-WP05-L005`, expressing top as the join of two elements strictly below
  it, is `FORMALIZED/CHECKED`.
- `UC-WP05-L006`, the exact upper-cone equation for doubly irreducible
  elements, is `FORMALIZED/CHECKED`.
- `UC-WP05-L007`, uniqueness of a doubly irreducible element in a minimum
  counterexample, is `FORMALIZED/CHECKED`.
- `UC-WP05-L008`, finite homogeneous deletion in both dual directions, is
  `FORMALIZED/CHECKED`.
- `UC-WP05-L009`, the strict-majority theorem for nonempty finite sets of
  inf-irreducibles, is `FORMALIZED/CHECKED`.
- `UC-WP05-L010`, the all-inf-irreducibles specialization, is
  `FORMALIZED/CHECKED`.
- `UC-WP05-L011`, the common sup-irreducible lower bound for two
  inf-irreducibles, is `FORMALIZED/CHECKED`.
- `UC-WP05-L012`, the exact-cone lower witness below every inf-irreducible, is
  `FORMALIZED/CHECKED`.
- `UC-WP05-L013`, the non-chain condition for elements incomparable with any
  non-endpoint, is `FORMALIZED/CHECKED`.
- `UC-WP05-L014`, the three-incomparables lower bound for every non-endpoint,
  is `FORMALIZED/CHECKED`.
- `UC-WP05-L015`, Bouchard's Theorem 2.15 branch (ii), the dual-atom
  cardinality-gap criterion for embedded finite lattice subposets, is
  `FORMALIZED/CHECKED`.
- `UC-WP05-C016`, the finite-lattice enumeration fact needed by Theorem 2.15
  branch (i), is `COMPUTED_EXACTLY/CERTIFIED` by independent replay for sizes
  `4..7`.
- `UC-WP05-L016`, the Lean transfer theorem for Theorem 2.15 branch (i), is
  `FORMALIZED/CHECKED`.
- `UC-WP05-C015`, the full source Theorem 2.15, is
  `PROVED_IN_PACKAGE/CERTIFIED` as a hybrid result combining `UC-WP05-C016`,
  `UC-WP05-L016`, and `UC-WP05-L015`; it is not claimed as one single Lean
  theorem.
- `UC-WP05-C017`, the earlier source audit of Rival's finite lattice length
  inequality, is superseded by the checked local theorem `UC-WP05-L019`.
- `UC-WP05-L017`, the conditional Theorem 2.7 wrapper assuming `RivalBound`,
  is `FORMALIZED/CHECKED`.
- `UC-WP05-L018`, the conditional non-top Corollary 2.8 wrapper assuming
  `RivalBound`, is `FORMALIZED/CHECKED`.
- `UC-WP05-L019`, Rival's source-style finite lattice length inequality and
  the endpoint-transfer theorem `minimumCounterexample_rivalBound`, is
  `FORMALIZED/CHECKED`.
- `UC-WP05-L017A`, Bouchard Theorem 2.7 without an explicit `RivalBound`
  hypothesis, is `FORMALIZED/CHECKED`.
- `UC-WP05-L018A`, Bouchard Corollary 2.8 without an explicit `RivalBound`
  hypothesis, is `FORMALIZED/CHECKED`.
- `UC-WP05-C018`, Bouchard Theorem 2.7 and Corollary 2.8 dependency
  assessment, is superseded by `UC-WP05-L017A` and `UC-WP05-L018A`.
- `UC-WP05-C019`, the Rival local formalization feasibility assessment, is
  superseded by `UC-WP05-L019`.
- The full Theorem 2.1 local configuration and other later source results
  remain literature-derived.
