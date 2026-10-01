# Saturated prism obstruction

Record: `OM26-H1-SATURATED-PRISM-OBSTRUCTION-001`.
State: **CONDITIONAL_PAPER_PROOF__INDEPENDENT_GEOMETRIC_REVIEW_PENDING**.

## Result and hypotheses

The sixty labeled triangular-prism candidates in the `333444` six-core
profile cannot be realized by the arrangement. Consequently six clean lines
cannot fill the three unused-segment charge slots in this profile: the
underlying elementary-edge geometry is already impossible.

This is conditional on the no-long-run and clean-line charging premises in
[H1_SIX_CORE_PREMISE_PROOF.md](H1_SIX_CORE_PREMISE_PROOF.md), and on the
necessary-state reduction in [H1_Q6_INTERNAL_REPLAY.md](H1_Q6_INTERNAL_REPLAY.md).
Independent geometric adjudication remains pending. CI is a finite certificate
check, not certification of the real-geometric argument.

## 1. Saturation forces isolated D2 rays

The predecessor replay leaves seventy cubic core graphs for this profile:
ten copies of K3,3, excluded by planarity, and sixty triangular prisms.
Every core therefore has three incident D2 segments. The local totals are
`D1 = B = 24`, `D2 = 9`, `U = 3`; the clean-line lower bound is six.
These are the unique feasible totals in the declared relaxation.

At a core of multiplicity r, the no-long-run premise gives `d1 <= 2r-3`.
The three triple cores and three quadruple cores have total cap
`3*3 + 3*5 = 24`. Equality in the total forces equality at each core.
Together with its three D2 rays, each core thus has all `2r` rays shared.

At a triple core the cyclic word has three D1 and three D2 rays, and no two
consecutive D1 rays. Its D1 gaps between D2 rays are `(1,1,1)`.
At a quadruple core there are five D1 and three D2 rays, and no three
consecutive D1 rays. Its three gaps each have size at most two and sum to
five, so they are a cyclic permutation of `(2,2,1)`.
In either case **no two D2 rays are adjacent in cyclic order**. An exhaustive
check retains two labeled triple words and eight labeled quadruple words.

## 2. Elementary triangle lemma

Let A, B, C be three noncollinear arrangement vertices, with AB, BC, CA
elementary arrangement segments (no arrangement vertex in their relative
interiors). Then the rays AB and AC must be consecutive in the angular
interval forming the triangle's interior angle at A.

Proof: an additional arrangement ray from A strictly inside that angle has
direction `u = alpha*(B-A) + beta*(C-A)` with `alpha,beta > 0`, after choosing
a positive scale. Its supporting full line meets BC at

`P = (alpha*B + beta*C)/(alpha+beta)`.

Both coefficients are strictly positive, so P lies in the relative interior
of BC. The extra line differs from BC, since A is not on BC. Their intersection
P is an arrangement vertex, contradicting the elementary nature of BC.
This does not require the interior of ABC to be a counted triangular face,
nor does it require the extra ray's first segment to extend as far as BC.

## 3. Every prism is forbidden

Each triangular prism contains two 3-cycles of D2 edges. Their three cores
cannot be collinear: the segment joining the extreme cores would contain the
third core, contradicting elementary edges. Choose either triangle and any
of its corners. Its internal angle is strictly less than pi. The two bounding
D2 rays are not adjacent by Section 1, so that angular interval contains an
additional ray. The elementary triangle lemma gives a contradiction.

Thus all sixty prism candidates are excluded. With the ten nonplanar K3,3
candidates already excluded, **zero geometric candidates remain in `333444`**,
conditional on the stated premises.

## Evidence and next direction

[H1_SATURATED_PRISM_OBSTRUCTION_RECEIPT.json](H1_SATURATED_PRISM_OBSTRUCTION_RECEIPT.json)
retains all ten saturated local words and a forbidden D2 triangle for each
of the sixty predecessor prism masks. The checker
`ci/validate_openmath_h1_prism_obstruction.py` binds the predecessor receipt
by SHA-256 and validates the certificates through the existing routed tests.
The predecessor receipt is preserved unchanged.

The four remaining q=6 profiles are `333333`, `333334`, `333335`, `333344`.
The next internal target is `333335`: test its sixty D2=7 candidate graphs
against the elementary triangle lemma and compatible cyclic ray orders,
then retain surviving incidence certificates or a conditional obstruction.
This result neither closes q=6 nor addresses q>=7. It does not consume
WP02's independent-agent lease, promote a certified claim, or change the
accepted historical frontier. Independent review of the premise proof and
this triangle argument remains a separate obligation.
