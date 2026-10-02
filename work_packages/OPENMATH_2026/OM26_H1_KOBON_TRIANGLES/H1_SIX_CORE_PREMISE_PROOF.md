# H1 face-to-fan and clean-line extraction

**Record:** `OM26-H1-SIX-CORE-PREMISE-AUDIT-001`  
**State:** `PAPER_PROOF_CANDIDATE__INDEPENDENT_ADVERSARIAL_REPLAY_PASS__TRUSTED_MATHEMATICAL_ADAPTER_PENDING`  
**Scope:** finitely many distinct pairwise nonparallel real affine lines; even n>=4. Faces are bounded, nondegenerate triangular cells. The number q of finite multiple points is unrestricted.

This supplies the geometric extraction omitted from the earlier six-core replay packet. It is internal current-context work, not a zero-context contribution, a kernel-checked global theorem or a MATHCERT disposition. Existing source-conditional claim statuses remain unchanged pending trusted mathematical replay or certification. The zero-context adversarial replay `OM26-H1-WP60-IA-001` found no counterexample within this stated scope; see `H1_PREMISE_SCOPE_DISPOSITION.md`.

## Proposed exact statement

Let U count bounded elementary segments bordering no triangular face. Let D1 and D2 count segments bordering two triangular faces, with respectively one and two multiple endpoints. At each r-fold point, list its 2r rays cyclically and mark D1 rays. Let B count D1 rays adjacent to at least one D2 ray, once per D1 ray. Let h count arrangement lines containing a multiple point. Then:

1. No r-1 consecutive rays are all D1; consequently d1(v)<=2r-3.
2. Each clean line (one containing no multiple point) has a bounded transverse elementary segment with triangle-use count zero or two at one of its ordinary crossings.
3. A charge from a clean line cannot use a blocked D1 segment; therefore n-h<=2U+D1-B.

None of these statements assumes q<=5. In particular the proposed extraction covers q=6, including triple and quadruple points.

## Elementary side extraction

A side of a triangular cell has two finite endpoints and no intervening arrangement vertex. Any other distinct line meeting its relative interior would enter the triangle on one side of that side, contradicting that it is a cell. Thus the side is an elementary segment, not a union of unaccounted segments. At a core v, each triangular sector has v as one vertex and the nearest finite vertex on each of its bounding rays as its other vertices. Those two finite vertices exist because the face is bounded. Every shared ray borders two such sectors.

A shared segment cannot have two ordinary endpoints. At either endpoint there is only one nonradial support. The two opposite faces would therefore use the same three supports, whose only bounded triangular region lies on one fixed side of the shared support. They cannot form two triangles on opposite sides. Hence every shared segment belongs to D1 or D2.

## Fan propagation, without a q hypothesis

Suppose r-1 consecutive D1 rays existed at v. The r sectors adjoining that run are triangular. Write P0,...,Pr for their successive radial endpoints and A0,...,A(r-1) for their opposite supports. The internal endpoints P1,...,P(r-1) are ordinary, since the corresponding rays are D1.

At Pi, both adjacent opposite supports pass through Pi and differ from its radial line through v. Ordinariness leaves precisely one possible nonradial line, so A(i-1)=Ai. Propagation makes every Aj the same line A. In cyclic order, r steps among 2r rays of r distinct full lines take a ray to its antipode. Thus P0 and Pr lie on opposite rays of one line through v, and v lies strictly between them. A contains both endpoints, so it contains v, contrary to nondegeneracy of every fan triangle.

This constructs the needed local fan data from actual bounded faces. Unbounded radial rays cause no gap: a supposed D1 run forces all r+1 relevant endpoints to exist. The argument is local and never counts the other multiple points.

To obtain the numerical bound, count marked rays in all 2r cyclic blocks of length r-1. Each block has at most r-2 marks; each mark occurs r-1 times. Hence (r-1)d1<=2r(r-2). A value d1>=2r-2 would violate this inequality by at least two, so d1<=2r-3.

## Clean-line parity extraction

Fix a clean line L and place it horizontally. Its m=n-1 crossings are distinct and ordinary; m is odd. Label them 1,...,m. Let Ri be the transverse arrangement line at crossing i. For the segment of L between crossings i and i+1, let xi and yi indicate whether its upper and lower incident faces are triangular. Set x0=y0=xm=ym=0 for the exterior rays. Since the bounded segments on L have ordinary endpoints, xi+yi<=1.

At crossing i, the upper transverse elementary piece has triangle-use count x(i-1)+xi and the lower piece has count y(i-1)+yi. An exterior transverse ray has count zero. Assume, for contradiction, that every bounded transverse piece at L has count exactly one. Then a piece of count zero is unbounded, and a piece of count two is impossible.

At the first crossing at least one transverse direction is bounded, because R1 intersects another nonparallel transverse line away from L. Thus x1 or y1 is one. Reflect the picture if needed so x1=1 and y1=0.

Induct on i=1,...,m-1. For odd i, yi=0; for even i, xi=0. Also, if both preceding indicators vanish, the other indicator at i is one. Here is the even step; swapping upper and lower gives the odd step. If x(i-1)=1, xi=0 because their sum cannot be two. Otherwise the preceding odd step gives x(i-1)=y(i-1)=0. This cannot occur at i=2, since x1=1, so i>=4. The preceding even step gives x(i-2)=0. Consequently the upper piece of R(i-1) has count zero and is unbounded. Its intersection with Ri must be below L; an intersection above L would make that upper piece bounded. Thus the lower piece of Ri is bounded. Its count is one, forcing yi=1 because y(i-1)=0. Finally xi=0 follows from xi+yi<=1. This proves the induction including its additional implication.

Since m-1 is even, x(m-1)=0. If y(m-1)=0 as well, both pieces of Rm have count zero, although at least one is bounded, a contradiction. Otherwise y(m-1)=1. The lower piece of R1 and upper piece of Rm have count zero and are unbounded. Their two lines intersect away from L. An intersection below L makes the former bounded; an intersection above L makes the latter bounded. Either contradicts the assumption.

Therefore L has a bounded transverse piece with use count zero or two. Other intersections of the arrangement may be multiple; the proof needs ordinariness only on L. Pairwise nonparallelism and even n are essential hypotheses, not omitted qualifications.

## Endpoint capacity and the blocked refinement

Choose one chargeable transverse segment for each clean line. The crossing at which it is chosen is ordinary. For any fixed segment and any fixed ordinary endpoint, exactly one nonradial arrangement line can supply that charge. An unused segment has at most two ordinary endpoints, giving capacity two. A D1 segment has precisely one ordinary endpoint, giving capacity one. A D2 segment has none, giving capacity zero.

Now let a D1 ray at v border a D2 ray. Their common sector is triangular, since both rays are shared. Its opposite support joins the ordinary far endpoint of the D1 side to the multiple far endpoint of the D2 side. That support is the unique nonradial line at the ordinary endpoint of D1. It contains a multiple point and hence is not clean. The only possible clean-line charge endpoint of this D1 segment is therefore unavailable. A D1 segment has exactly one core endpoint, so counting such blocked rays once is the same as counting unavailable D1 target segments once. Summing capacities gives n-h<=2U+D1-B.

## Exact evidence and its limits

`ci/validate_openmath_h1_geometric_premises.py` constructs eight exact eighteen-line fixtures, each with precisely six cores. Four have multiplicities 333333 and nine clean lines; four have multiplicities 333444 and six clean lines. No parallel pair or unintended multiple point is permitted by construction. It reconstructs finite vertices, elementary segments, supporting-line face triples, exact cyclic ray order, fan words, blocked targets and explicit charge choices using rational arithmetic. It checks the defect identity, no-long-run property, every charge endpoint and capacity, and the refined inequality. The JSON receipt retains all coefficients and charges.

These examples have 23 through 36 triangles. They are regression witnesses for the geometry interface, not score-95 constructions, broad search coverage or a proof by testing. The checker uses the protected direct geometric oracle; it is not an independent Cert verifier.

Run:

```sh
python ci/validate_openmath_h1_geometric_premises.py
python -m unittest ci.test_openmath_h1_12_q5_profiles -v
```

## Review provenance and continuation

Source reconnaissance: `alejandrozu/kobon-proof@22d1165f6c455fe45e461baef4410f6d5c78a014`, `research/six-hour-2026-09-21/general-bounds/clean-line-parity.md`, `Kobon/FanGeometry.lean`, `Kobon/CyclicFan.lean`, and `Kobon/CleanLineBudget.lean`. These distinguish actual local geometric components from conditional aggregate arithmetic. This note supplies a manuscript extraction and does not claim a new Lean compilation of those external components or priority over that source.

Same-system non-authoring read-only Adversary audit checked the bounded-side extraction, antipodal endpoint step, parity induction including boundary rays, distinction between unused bounded pieces and unbounded rays, and the unique nonradial support behind blocked charges. The Referee audit checked exact fixture multiplicities, charge certificates, source scope and nonconsumption of the public WP02 lease. Reserved independent geometric adjudication and certification remain open.

The next internal tranche is global ray/line consistency in the sixty prism candidates, explicitly conditional on this paper proof until independently adjudicated. Start with the saturated requirement: exactly six clean lines must consume all ordinary-endpoint slots of exactly three unused segments. If that assignment cannot exist, return the precise obstruction; if it can, retain exact incidence/order witnesses before claiming straight-line realization. The all-triple star and the remaining profiles are separate residuals. No global <=94, optimality, novelty, independent certification or competition submission follows here.
