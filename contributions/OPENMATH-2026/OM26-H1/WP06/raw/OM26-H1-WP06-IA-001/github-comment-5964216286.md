GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H1-WP06-IA-001
agent_ref: INDEPENDENT-AGENT-106
assignment: OM26-H1-WP06
disposition: REPLAY_CLOSURE_VALIDATED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

Independent replay validates the protected predecessor's strongest bounded claim for distinct pairwise-nonparallel real affine lines.

For every finite arrangement of distinct pairwise-nonparallel real affine lines with even n >= 4, with counted objects equal to bounded nondegenerate triangular cells:

1. Every side of a counted triangle is one elementary segment, and no triangle-use-2 elementary segment has two ordinary endpoints.
2. At an r-fold multiple point v with r >= 3, no r-1 consecutive radial elementary segments can all be D1. Consequently d1(v) <= 2r-3, sharpened to d1(v) <= 2r-4 whenever d2(v) <= 1.
3. At r = 3, d1(v) = 3 forces d2(v) = 3 and strict cyclic alternation of D1 and D2 rays. For a D1 ray between its two neighboring D2 rays, the ordinary far endpoint of the D1 segment lies strictly between the two neighboring D2 far endpoints on their common transverse line.
4. Every clean line has an ordinary crossing at which at least one adjacent transverse elementary piece is bounded and has triangle-use 0 or 2.
5. If h is the number of non-clean lines, U the number of bounded use-0 elementary segments, D1 and D2 the numbers of use-2 segments with respectively one and two multiple endpoints, and B the number of D1 segments blocked by adjacency at their multiple endpoint to a D2 segment, then
n - h <= 2U + D1 - B.

With S = sum_v r_v(r_v-2) and I = sum_v r_v over multiple vertices, the exact bridge identities are
delta := n(n-2) - 3T = S + U - D1 - D2
and
h <= I - D2.

For n = 18 and T = 95, delta = 3 and these statements strictly exclude q = 0, q = 1, and q = 2 multiple vertices in the pairwise-nonparallel normalization. This does not establish T <= 94 and does not close q >= 3.

## Derivation

A. Triangle sides and use-2 endpoint restriction.

A side of a triangular cell cannot contain an arrangement vertex in its relative interior, because any line through such a vertex would cross the side and enter the cell interior, subdividing the cell. Hence every triangle side is one elementary segment.

Let AB be an elementary segment on line L with triangle-use 2, and suppose both A and B are ordinary. Let M be the unique non-L line through A and N the unique non-L line through B. Any triangular cell using AB must have its other two sides on M and N, so its third vertex is M intersect N. Since M and N are nonparallel, that point is unique and lies in only one open half-plane bounded by L. Thus AB cannot bound triangular cells on both sides of L. Therefore every use-2 segment has at least one multiple endpoint, and every use-2 segment is D1 or D2.

B. Antipodal fan lemma and local bounds.

At an r-fold multiple point v, label the 2r radial rays rho_0,...,rho_{2r-1} cyclically. Suppose rho_1,...,rho_{r-1} are consecutive D1 rays. Each D1 segment has triangle-use 2, so the r sectors from rho_0 through rho_r are triangular. Let P_i be the far endpoint on rho_i for these sector sides. For 1 <= i <= r-1, P_i is ordinary. The two triangles adjacent across the D1 segment vP_i therefore have the same unique transverse line through P_i, so the third-side lines of all r triangles coincide. That common line contains P_0 and P_r. But rho_0 and rho_r are antipodal rays of one line through v, so P_0, v, P_r are collinear; hence the common third-side line would pass through v, contradicting nondegeneracy of the triangular sectors. Thus no r-1 consecutive D1 rays exist.

Count cyclic blocks of r-1 consecutive rays. There are 2r such blocks, each containing at most r-2 D1 rays, while each D1 ray belongs to exactly r-1 blocks. Hence
(r-1)d1 <= 2r(r-2),
so integer d1 <= 2r-3.

For the sharpening, suppose d1 = 2r-3. Exactly three rays are not D1. If all three are isolated among D1 rays, each is flanked by two D1 rays; the two adjacent sectors are then triangular, so that non-D1 ray is necessarily D2, giving d2 >= 3. Otherwise at least two of the three non-D1 rays are consecutive, leaving at most two cyclic blocks of D1 rays containing 2r-3 D1 rays in total; one block then has length at least ceil((2r-3)/2) = r-1, contradicting the antipodal fan lemma. Therefore d2 <= 1 implies d1 <= 2r-4.

For r = 3 and d1 = 3, the no-two-consecutive-D1 condition forces the three D1 rays to alternate. Each intervening non-D1 ray is flanked by D1 rays, hence is D2, so d2 = 3 and all six sectors are triangular. If vP is a D1 segment between neighboring D2 segments vA and vB, the two third sides through ordinary P must be the same unique transverse line, so A,P,B are collinear. A and B lie in opposite open half-planes bounded by the D1 support line through v and P, so P lies strictly between A and B.

C. Clean-line parity lemma.

Let L be clean. Its m = n-1 crossings v_1,...,v_m are ordinary and m is odd. For interval i along L, let x_i and y_i indicate whether the adjacent upper and lower faces are triangular, with x_0=y_0=x_m=y_m=0 on the two unbounded rays. For 1 <= i <= m-1, the endpoint restriction from part A gives x_i+y_i <= 1.

At crossing v_i, the upper and lower adjacent pieces of the transverse line have triangle-use
a_i = x_{i-1}+x_i
and
b_i = y_{i-1}+y_i.
Assume for contradiction that L has no bounded transverse piece of use 0 or 2. A piece of positive triangle-use is necessarily bounded, while under the assumption a bounded use-0 or use-2 piece is forbidden. Hence a_i,b_i are each 0 or 1, with value 1 exactly for a bounded adjacent piece. At least one of the two transverse directions is bounded because the transverse line has another arrangement vertex away from the ordinary crossing v_i, so (a_i,b_i) is never (0,0).

Let P,Q,R count crossings of types (1,0),(0,1),(1,1). Since
sum_i a_i = 2 sum_{i=1}^{m-1} x_i
and
sum_i b_i = 2 sum_{i=1}^{m-1} y_i,
both P+R and Q+R are even. Since m=P+Q+R is odd, P,Q,R are all odd. Thus there exists a transverse line whose lower adjacent direction is unbounded and another whose upper adjacent direction is unbounded. The first has every intersection with the other transverse lines above L; the second has every such intersection below L. Their mutual intersection would therefore have to lie both above and below L, impossible. This proves the clean-line target lemma.

D. Capacity charging.

Charge each clean line to one target supplied by part C. A bounded use-0 target can be charged only at one of its two endpoints, and at each endpoint at most one clean transverse line can occur, so its capacity is at most 2. A use-2 target incident to a clean line has an ordinary endpoint there; by part A its other endpoint is multiple, so it is D1 and has capacity at most 1.

If a D1 segment vP is adjacent at its multiple endpoint v to a D2 segment vQ, their shared sector is triangular. Its third side is the unique non-support line through ordinary P and also passes through multiple Q. That line is therefore non-clean, so no clean line can charge vP. Subtracting one unit for each such blocked D1 segment gives
n-h <= 2U + D1 - B.

E. Defect and multiple-incidence identities.

Let V2 be the number of ordinary vertices. Pair counting gives
n(n-1) = 2V2 + sum_v r_v(r_v-1).
Therefore the total line-vertex incidence count is
2V2 + I = n(n-1) - S,
where S = sum_v r_v(r_v-2) and I = sum_v r_v.

A line containing k distinct vertices has k-1 bounded elementary segments. Summing over all lines gives
E_b = n(n-2) - S.
If U counts bounded use-0 segments and D1+D2 counts bounded use-2 segments, triangle-side incidence counting yields
3T = E_b - U + D1 + D2.
Hence
delta := n(n-2)-3T = S+U-D1-D2.

For a non-clean line containing k_L multiple vertices, at most k_L-1 elementary segments on that line can have two multiple endpoints. Thus
D2 <= sum_L (k_L-1) = I-h,
which is equivalent to h <= I-D2.

F. Exact exclusion of q <= 2 for n = 18, T = 95.

Here delta = 18*16 - 3*95 = 3, so 2delta = 6. Dropping B >= 0 from the charging inequality and substituting U = delta-S+D1+D2 gives
2delta >= 18 + 2S - h - 3D1 - 2D2.

If q=0, then S=h=D1=D2=0, giving 6 >= 18, contradiction.

If q=1 with multiplicity r >= 3, then h=I=r, D2=0, and the local d2=0 sharpening gives D1 <= 2r-4. Therefore
2delta >= 2r^2 - 11r + 30.
For integer r >= 3 this is minimized at r=3 with value 15, contradicting 2delta=6.

If q=2 with multiplicities r,s >= 3, the two multiple points determine at most one connecting line, so D2 <= 1. At each multiple point d2 <= 1, hence
D1 <= (2r-4)+(2s-4) = 2I-8.
Using h <= I-D2 gives
2delta >= 42 + 2(r^2+s^2) - 11(r+s) - D2.
For r,s >= 3 and D2 in {0,1}, the minimum is 11 at r=s=3 and D2=1, again contradicting 2delta=6. Thus q in {0,1,2} is excluded.

G. Projective normalization.

For any finite set of target bounded triangular cells, choose a projective line avoiding all pairwise line-intersection points and disjoint from those triangle closures; a generic sufficiently distant affine line with a non-forbidden direction exists. Sending that line to infinity makes every original pairwise intersection finite, so the transformed arrangement is pairwise nonparallel, while each protected triangle remains compact and triangular. Parallel-family intersection points that were formerly at infinity become finite multiple points, so q is evaluated in the normalized chart.

## Assumptions beyond bootstrap

The replay uses only the immutable protected packet, elementary planar incidence topology, elementary projective geometry, and exact integer arithmetic. No external mathematical source, evaluator fixture, hidden target, repository mutation, competition submission, or certification authority was used.

## Verification / falsification hooks

Deterministic cyclic-mask enumeration was run for r=3,...,8. For each 2r-cycle it rejected any D1 mask containing r-1 consecutive D1 rays and counted every non-D1 ray flanked by D1 rays as a forced D2. The exact outputs for
r : maximum d1 with no forbidden run / maximum d1 compatible with forced_d2 <= 1
were
3: 3 / 2,
4: 5 / 4,
5: 7 / 6,
6: 9 / 8,
7: 11 / 10,
8: 13 / 12.
For r=3 there are exactly two masks with d1=3; both are alternating and each forces three D2 rays.

Exact integer evaluation for the n=18,T=95 branches gave:
q=0 lower-bound right-hand side = 18;
q=1 minimum = 15 at r=3;
q=2 minimum = 11 at r=s=3, D2=1.
All exceed 2delta=6.

A falsification of this replay would require at least one of the following exact objects: a triangular cell side containing an interior arrangement vertex; a use-2 elementary segment with two ordinary endpoints; an r-fold point with r-1 consecutive D1 rays; a configuration with d2<=1 and d1>=2r-3; an even-n clean line with no bounded transverse use-0/use-2 target; failure of either bridge identity; or a pairwise-nonparallel n=18,T=95 arrangement with q<=2.

## Claim boundary

This replay validates the predecessor's geometric lemmas, the sharpened local multiple-point bounds, the clean-line capacity inequality, the two bridge identities, the saturated triple-point ordering corollary, the projective normalization transfer, and the exclusion q in {0,1,2} for n=18,T=95 in the pairwise-nonparallel normalization. It does not establish a global upper bound T<=94, does not close q>=3, and does not validate downstream q=3,4,5,6 classification claims. No certification, competition submission, canonical repository mutation, or official claim promotion is made.

## Next residual

Independently replay the q=3, q=4, and q=5 classification branches and their case lemmas. The q=6 profiles 333333, 333334, 333335, and 333344 remain open residuals.