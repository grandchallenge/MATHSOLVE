GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H1-WP04-IA-001
agent_ref: INDEPENDENT-AGENT-104
assignment: OM26-H1-WP04
disposition: REPLAY_CLOSURE_VALIDATED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

Independent replay validates the predecessor's strongest bounded claim for distinct pairwise-nonparallel real affine lines.

For every finite arrangement of distinct pairwise-nonparallel real affine lines, with even n>=4 and counted objects equal to bounded nondegenerate triangular cells:

1. Every side of a counted triangle is one elementary segment, and no use-2 elementary segment can have two ordinary endpoints.
2. At an r-fold multiple point (r>=3), no r-1 consecutive radial elementary segments can all be D1. Consequently d1(v)<=2r-3.
3. Every clean line contains an ordinary crossing at which one adjacent transverse elementary piece is bounded and has triangle-use 0 or 2.
4. Choosing one such transverse target for each clean line gives
   n-h <= 2U + D1 - B.

The bridge identities also replay:
delta := n(n-2)-3T = S+U-D1-D2,
where S=sum_v r_v(r_v-2), and
h <= I-D2,
where I=sum_v r_v.

The local corollaries replay as well:
- if d2(v)<=1, then d1(v)<=2r-4;
- at a triple point, d1=3 forces d2=3;
- a saturated triple has alternating D1/D2 rays, and the ordinary endpoint of a D1 ray lying between its two neighboring D2 rays is strictly between the two neighboring D2 endpoints on their common transverse line.

For n=18 and T=95, delta=3, and these statements alone exclude q=0, q=1, and q=2 in the pairwise-nonparallel normalization.

This replay does not validate a global T<=94 theorem and does not close q>=3.

## Derivation

I replayed the argument from definitions rather than accepting the predecessor disposition.

A. Triangle sides and shared segments.

Let AB be a side of a counted triangular cell. Any arrangement line meeting relint(AB) would cross the supporting line and enter the triangle interior, contradicting that the triangle is a cell. Hence AB contains no arrangement vertex in its relative interior and is an elementary segment.

Now suppose an elementary segment AB is incident to counted triangles on both sides and both endpoints are ordinary. Let L support AB, and let M and N be the unique non-L lines through A and B. Any triangle incident to AB must use L,M,N. The lines M and N have one intersection C, and the triangle determined by L,M,N lies on the unique side of L containing C. Therefore AB cannot bound counted triangles on both sides. Thus every use-2 segment has at least one multiple endpoint and is classified as D1 or D2.

B. Antipodal fan lemma.

At an r-fold point v, suppose r-1 consecutive rays rho_1,...,rho_{r-1} are D1. Because each D1 segment is incident to two counted triangles, all r sectors between rho_0 and rho_r are triangular. Let P_i be the far endpoint on rho_i and let A_i be the opposite side line through P_i,P_{i+1}.

For i=1,...,r-1, P_i is ordinary. Therefore A_{i-1} and A_i are the same unique non-radial line through P_i. Hence all A_i are one line A. In the cyclic order of 2r rays, rho_0 and rho_r are antipodal rays of the same arrangement line, so v lies strictly between P_0 and P_r. Since A contains P_0 and P_r, A contains v, contradicting nondegeneracy of the supposed triangular sectors. Therefore no r-1 consecutive D1 rays exist.

Double-count the 2r cyclic blocks of length r-1. Every block contains at most r-2 D1 marks, while every D1 mark lies in r-1 blocks:
(r-1)d1 <= 2r(r-2).
Since 2r(r-2)/(r-1)=2r-2-2/(r-1), integrality gives d1<=2r-3.

For the sharpening, encode the 2r sectors by t_i in {0,1}. A radial ray is shared exactly when its two adjacent sectors are triangular. Assume d2<=1 and d1=2r-3. If all sectors are triangular, all 2r rays are shared, so d2=3, impossible. If d2=1, there are 2r-2 shared rays. A non-all-one cyclic binary sector word with 2r-2 adjacent 11 pairs has exactly one zero, so the shared rays form one block of length 2r-2. Removing one D2 mark leaves 2r-3 D1 marks; two runs of maximum length r-2 can hold at most 2r-4, so an r-1 D1 run is forced, contradiction. If d2=0, there are 2r-3 shared rays; the sector word has one run of 2r-2 ones and hence one run of 2r-3 shared rays, again forcing r-1 consecutive D1 marks. Thus d1<=2r-4 when d2<=1.

For r=3, d1=3 and the no-two-consecutive-D1 rule force the three D1 rays to alternate around the six-ray cycle. Each D1 ray has both adjacent sectors triangular, so all six sectors are triangular; hence all six rays are shared and the other three are D2. Thus d2=3. The two D2 neighbors of a D1 ray and that D1 ray occur as three consecutive rays spanning angle < pi. The two triangular sectors force the two opposite sides through the ordinary D1 endpoint to be the same unique non-radial line, so the two D2 far endpoints and the D1 far endpoint are collinear. Since the D1 ray lies strictly inside the convex cone between the neighboring D2 rays, its intersection with that chord lies strictly between the D2 endpoints.

C. Clean-line parity.

Fix a clean line L and order its m=n-1 ordinary crossings from left to right. Since n is even, m is odd. For the bounded L-interval between crossings i and i+1, let x_i,y_i indicate whether the upper/lower incident face is triangular, and set x_0=y_0=x_m=y_m=0.

Because each bounded L-interval has two ordinary endpoints, part A gives x_i+y_i<=1.

At crossing i, the upper adjacent piece of the transverse line has triangle-use x_{i-1}+x_i, and the lower adjacent piece has use y_{i-1}+y_i.

Assume for contradiction that every bounded transverse adjacent piece has use exactly 1. Then every use-0 adjacent piece is unbounded, and a use-2 adjacent piece is impossible.

At crossing 1 at least one transverse direction is bounded because its transverse line meets another arrangement line away from L. Thus exactly one of x_1,y_1 is 1. Reflecting if necessary, take x_1=1,y_1=0.

Inductively:
- y_i=0 for odd i;
- x_i=0 for even i.

For an even i, if x_{i-1}=1 then x_i=0, else x_{i-1}=0 and the preceding even step gives x_{i-2}=0. The upper adjacent piece of the (i-1)-st transverse line then has use 0 and is unbounded. Hence the intersection of transverse lines i-1 and i must be below L; therefore the lower adjacent piece at crossing i is bounded and has use y_i, forcing y_i=1 and then x_i=0. The odd case is the vertical mirror.

Since m-1 is even, x_{m-1}=0. If also y_{m-1}=0, both adjacent pieces at crossing m have use 0 although at least one is bounded, contradiction. Hence y_{m-1}=1. Then the lower adjacent piece at crossing 1 and the upper adjacent piece at crossing m both have use 0 and are unbounded. But the first and last transverse lines meet away from L. If they meet below L, the lower piece at crossing 1 is bounded; if above L, the upper piece at crossing m is bounded. Contradiction. Therefore the required bounded use-0 or use-2 target exists on every clean line.

D. Endpoint capacity and blocking.

Choose one target for each clean line. Its endpoint on the clean line is ordinary. A use-0 target is counted by U. A use-2 target cannot have two ordinary endpoints by part A and cannot be D2 because its clean-line endpoint is ordinary, so it is D1.

At an ordinary endpoint of a target segment, exactly one transverse arrangement line is available to be the charging clean line. Therefore a U segment has capacity at most two, a D1 segment capacity at most one, and D2 has capacity zero.

If a D1 ray at a multiple point v is adjacent to a D2 ray, their common sector is triangular because the D1 ray is use-2. Let p be the ordinary far endpoint of the D1 segment and q the multiple far endpoint of the D2 segment. The opposite triangle side is the unique non-radial line through p, and it also contains q. Hence that line is not clean, so p cannot receive a clean-line charge. Every D1 ray counted by B therefore loses its one possible unit of capacity. Summing target capacity yields
n-h <= 2U+D1-B.

E. Defect and core-incidence identities.

Let V2 be the number of ordinary intersections. Pairwise nonparallelism gives
C(n,2)=V2+sum_v C(r_v,2).
Thus total line-vertex incidences equal
2V2+sum_v r_v
= n(n-1)-sum_v r_v(r_v-2).

A line with k finite vertices has k-1 bounded elementary segments. Therefore
E_b=n(n-2)-S,
S=sum_v r_v(r_v-2).

Every counted triangle contributes three side incidences. Relative to one incidence per bounded segment, a use-0 segment subtracts one and a use-2 segment adds one. Hence
3T=E_b-U+D1+D2,
so
delta=n(n-2)-3T=S+U-D1-D2.

For core incidence, a line containing k>=1 multiple points contributes k to I and one to h, hence k-1 to I-h. It contains at most k-1 elementary intervals joining consecutive multiple points, and every D2 segment is one such interval. Summing over non-clean lines gives
D2<=I-h,
equivalently h<=I-D2.

F. Exact q<=2 replay for n=18,T=95.

Here delta=18*16-3*95=3. Drop B>=0 from the charging inequality and substitute
U=delta-S+D1+D2:
18-h <= 2delta-2S+3D1+2D2,
equivalently
2delta >= 18+2S-h-3D1-2D2.

q=0:
S=h=D1=D2=0, so the necessary inequality is
6>=18,
false.

q=1:
Let the unique core have multiplicity r>=3. Then D2=0, h=I=r, and d2=0 implies D1<=2r-4. Hence any such arrangement would require
6 >= 18+2r(r-2)-r-3(2r-4)
  = 30+2r^2-11r.
For every integer r>=3 this right-hand side is at least 15, contradiction.

q=2:
D2<=1 because the two multiple points determine at most one arrangement line joining them. At each core d2<=1, so summing the sharpening gives D1<=2I-8. Also h<=I-D2. Therefore
6 >= 42+2S-7I-D2.
Writing the multiplicities as r,s>=3, the relaxed right-hand side is minimized at r=s=3 and D2=1, where it equals 11. Thus q=2 is impossible.

G. Parallel-line transfer.

The predecessor packet also states a projective normalization. That transfer replays: for any finite selected set of bounded triangular faces, choose an affine line M sufficiently far from their compact closures and perturb it to avoid the finite set of projective pair-intersection points. Sending M to the projective line at infinity preserves incidences and triangular cells; every selected face remains compact in the new affine chart, hence bounded, and every pair of transformed arrangement lines meets finitely. This justifies using the pairwise-nonparallel normalization for hill-wide upper-bound reasoning. It does not by itself preserve a pre-normalization count of finite multiple points, so q is to be read in the normalized arrangement when applying the q<=2 exclusion.

## Assumptions beyond bootstrap

No external source, hidden target, evaluator fixture, repository mutation, competition submission, or certification mechanism was used. The only project-specific evidence used was the immutable protected packet embedded in OM26-H1-WP04.

The mathematical replay uses standard Euclidean/projective incidence facts and exact integer arithmetic. The finite scripts below are same-session falsification hooks, not independent formal verification.

The execution environment can contain prior conversational context. I did not use prior OPENMATH material outside the protected launch packet for this replay, so the required context_class is respected operationally but should not be interpreted as cryptographic isolation.

## Verification / falsification hooks

1. Cyclic-sector falsification check.

A deterministic exhaustive checker was run for r=3,...,8. It enumerates sector words, derives shared rays, and tests all d2=0 or d2=1 assignments relevant to the sharpening. It also checks the pure no-(r-1)-run maximum.

Observed tuples are
(r, max_d1_without_(r-1)-run, max_d1_with_d2<=1, min_d2_when_r=3_and_d1=3):
(3,3,2,3)
(4,5,4,None)
(5,7,6,None)
(6,9,8,None)
(7,11,10,None)
(8,13,12,None)

No counterexample to d1<=2r-4 for d2<=1 was found. These outputs match the exact formulas 2r-3 and 2r-4.

2. Integer replay for q<=2.

Deterministic enumeration over r,s in {3,...,18} and D2 in {0,1} gives:
delta = 3
q=0 RHS = 18
q=1 minimum RHS = 15 at r=3
q=2 minimum relaxed RHS = 11 at r=s=3, D2=1

Since 2delta=6, all three cases contradict the necessary charging inequality.

3. Direct proof-failure hooks.

The replay would fail if any one of the following were produced:
- a counted triangle side containing an arrangement vertex in its relative interior;
- a use-2 segment with two ordinary endpoints;
- an r-fold point carrying r-1 consecutive D1 rays;
- a clean line in an even-n arrangement for which every bounded transverse adjacent piece has use exactly 1;
- a q<=2 multiplicity tuple satisfying the derived necessary inequality for n=18,T=95.

The first four are excluded by the incidence/parity proofs above; the fifth is excluded by exact integer enumeration.

## Claim boundary

This result validates the predecessor's four affine-geometric premises, the two bridge identities, the stated local corollaries, and the direct q<=2 exclusion for n=18,T=95.

It does not independently rerun the separate q=3, q=4, or q=5 finite classifications or their later case lemmas. It does not promote the predecessor's dependency-table statements about complete q=4/q=5 closure. It does not prove the global upper bound T<=94. The normalized q>=3 cases, including the previously identified q=6 residual profiles 333333, 333334, 333335, and 333344, remain outside this replay closure.

No novelty, optimality, competition score, official submission, repository state, or certification claim is made.

## Next residual

The replay-closure gate for the predecessor's newly supplied geometry and q<=2 reduction is satisfied.

The next bounded non-authoring work should separately replay the protected q=3/q=4/q=5 dependency chain before any of those closures are promoted. For q=6, retain 333333, 333334, 333335, and 333344 as live residual profiles. The 333444 obstruction should only be promoted after its own bounded replay rather than inferred from this result.