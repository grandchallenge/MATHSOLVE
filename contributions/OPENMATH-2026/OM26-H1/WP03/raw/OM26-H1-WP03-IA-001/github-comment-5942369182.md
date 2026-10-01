GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H1-WP03-IA-001
agent_ref: INDEPENDENT-AGENT-103
assignment: OM26-H1-WP03
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: ADDITIONAL_PUBLIC_SOURCES
timebox_observed: YES

## Strongest exact statement
For every finite arrangement of distinct pairwise-nonparallel real affine lines, with even n>=4, and with counted objects equal to bounded nondegenerate triangular cells, the four requested geometric premises are valid for arbitrary numbers q of finite multiple points:

(1) bounded-side extraction: every side of a counted triangular cell is one elementary segment; a segment shared by two counted triangles cannot have two ordinary endpoints;

(2) antipodal fan lemma: at an r-fold multiple point (r>=3), no r-1 consecutive radial elementary segments can all be D1; hence d1(v)<=2r-3;

(3) clean-line parity lemma: every clean line contains an ordinary crossing at which one of the two transverse elementary pieces is bounded and has triangle-use count 0 or 2;

(4) blocked endpoint capacity: choosing one such transverse target for every clean line gives n-h<=2U+D1-B.

Two bridge identities used by the existing q<=6 reductions are also proved here:
delta:=n(n-2)-3T = S+U-D1-D2, where S=sum_v r_v(r_v-2), and h<=I-D2, where I=sum_v r_v.

Corollaries needed by earlier H1 reductions follow without extra source assumptions: if d2(v)<=1 then d1(v)<=2r-4; at a triple point d1=3 forces d2=3; a saturated triple has alternating D2,D1 rays and the ordinary D1 endpoint between two D2 neighbors lies strictly between those neighbors.

For n=18,T=95, delta=3. The proved premises alone exclude q=0,1,2, so the prior separate restricted q<=2 theorem is not needed for this reduction.

Event-window UTC: substantive work began 2026-10-01T22:51:00Z; checkpoint 2026-10-01T22:59:56Z; result draft creation 2026-10-01T23:00:43Z. Source head 36b7c79bebd42fde17ea9f0f809406fb55e093f9 was created 2026-10-01T22:00:12Z. Launch commit 4f1b6a1500e18fc53bae135ae6713e7abb126ae4 was created 2026-10-01T22:23:23Z.

## Derivation
Definitions. A vertex where exactly two lines meet is ordinary; an r-fold point with r>=3 is multiple. On each arrangement line, an elementary segment is the closed segment between consecutive finite vertices. A bounded elementary segment has triangle-use count 0,1,2 according to the number of counted triangular cells incident to it. U counts use-0 segments. D1 counts use-2 segments with exactly one multiple endpoint. D2 counts use-2 segments with two multiple endpoints. At a multiple point v, d1(v),d2(v) count corresponding radial first segments. B counts D1 rays adjacent in cyclic order to at least one D2 ray, once per D1 ray. A clean line contains no multiple point; h is the number of non-clean lines.

Bounded-side extraction. Let AB be a side of a counted triangular cell. If another arrangement line met relint(AB), it would cross the supporting line transversely at that point and enter the open triangle on one side, contradicting that the triangle is a cell. Thus AB contains no arrangement vertex in its relative interior and is elementary. At a multiple vertex, a triangular sector therefore ends on each bounding ray at the nearest finite vertex on that ray.

Now suppose one bounded elementary segment AB is incident to counted triangles on both sides and both A,B are ordinary. Let L support AB. At A there is exactly one other arrangement line M, and at B exactly one other arrangement line N. Any triangle incident to AB must therefore use exactly the three supports L,M,N. Since M and N are nonparallel, their intersection C is unique; the bounded triangle of these three supports lies on only the side of L containing C. Hence two counted triangles cannot occupy opposite sides of AB. Therefore every use-2 segment has at least one multiple endpoint and is classified by D1 or D2.

Antipodal fan lemma. Fix an r-fold point v. Suppose r-1 consecutive rays rho_1,...,rho_{r-1} are D1. Because a D1 segment is incident to two triangular cells, the r sectors from rho_0 through rho_r are all triangular. Let P_i be the finite endpoint on rho_i supplied by those sectors, and let A_i be the support of the side P_i P_{i+1}. For i=1,...,r-1, P_i is ordinary because rho_i is D1. Both A_{i-1} and A_i pass through P_i and differ from the radial line vP_i; ordinariness leaves only one nonradial arrangement line through P_i, so A_{i-1}=A_i. Hence all A_i are one line A. In the cyclic order of the 2r rays of r distinct lines through v, shifting by r rays takes a ray to its antipode. Thus rho_0 and rho_r are opposite rays of one line through v, so v lies strictly between P_0 and P_r. Since A contains P_0 and P_r, A also contains v, making each supposed fan triangle degenerate. Contradiction. This argument also covers initially unbounded radial directions: the assumed triangular sectors themselves force the required P_i to exist.

For the numerical bound, inspect all 2r cyclic blocks of r-1 rays. Each has at most r-2 D1 marks and each D1 mark belongs to r-1 such blocks, so
(r-1)d1 <= 2r(r-2).
For r>=3 this implies d1<=2r-3.

Sector corollaries. Mark the 2r sectors by t_i in {0,1}, triangular or not. A radial ray is shared exactly when its two adjacent sectors are both triangular. If d2<=1 and d1=2r-3, then either all sectors are triangular, which would give d2=3, or not all are triangular. In the latter case, if d2=1 there are 2r-2 shared rays; the cyclic sector word must have exactly one zero, so those shared rays form one block. One D2 mark cannot split the remaining 2r-3 D1 marks into two runs both of length at most r-2. If d2=0, there are 2r-3 shared rays; the cyclic sector word has one run of 2r-3 shared rays, again containing r-1 consecutive D1 rays. Both contradict the fan lemma. Hence d1<=2r-4 when d2<=1. For r=3, d1=3 and no two consecutive D1 rays forces the D1 marks to alternate; every sector is then adjacent to a D1 ray, so all six sectors are triangular, all six rays are shared, and the other three rays are D2. Thus d1=3 implies d2=3.

Clean-line parity. Fix a clean line L, orient it horizontally, and order its m=n-1 distinct ordinary crossings from left to right. Since n is even, m is odd. Let R_i be the transverse line at crossing i. For the bounded interval of L between crossings i and i+1, let x_i,y_i indicate whether its upper/lower incident face is triangular; put x_0=y_0=x_m=y_m=0 for the exterior rays. A bounded interval of L has two ordinary endpoints, so the preceding shared-segment lemma gives x_i+y_i<=1.

At crossing i, the upper elementary piece of R_i adjacent to L has triangle-use x_{i-1}+x_i; the lower piece has use y_{i-1}+y_i. Assume for contradiction that every bounded transverse piece has use exactly 1. A use-0 transverse piece is then unbounded, while use 2 is impossible because two incident triangles would make that piece bounded.

At crossing 1 at least one transverse direction is bounded: R_1 meets another R_j away from L, and the first vertex in that direction terminates the adjacent piece. Hence x_1 or y_1 is 1. Reflect vertically if necessary so x_1=1,y_1=0.

Inductively, y_i=0 for odd i and x_i=0 for even i. Consider even i. The preceding odd step gives y_{i-1}=0. If x_{i-1}=1, then x_i=0 because otherwise the upper piece of R_i has use 2. If x_{i-1}=0, then i>=4 (since x_1=1), and the preceding even step gives x_{i-2}=0. Thus the upper piece of R_{i-1} has use 0 and is unbounded. Therefore R_{i-1} meets R_i below L; otherwise that upper piece would be bounded. Hence the lower piece of R_i is bounded and has use y_i, so y_i=1. Then x_i=0 from x_i+y_i<=1. The odd step is the vertical mirror.

Since m-1 is even, x_{m-1}=0. If y_{m-1}=0, both pieces of R_m have use 0 although at least one is bounded, contradiction. Thus y_{m-1}=1. The lower piece of R_1 and upper piece of R_m both have use 0 and are therefore unbounded. But R_1 and R_m meet away from L: if below L the lower piece of R_1 is bounded, and if above L the upper piece of R_m is bounded. Contradiction. Therefore L has a bounded transverse piece of use 0 or 2.

Endpoint capacity and blocking. Choose one such target for each clean line. The target endpoint at L is ordinary. A use-0 target is counted by U. A use-2 target cannot have two ordinary endpoints and cannot be D2 because its endpoint on L is ordinary, so it is D1. At any fixed ordinary endpoint of a target segment there is exactly one transverse arrangement line, hence at most one clean line can charge that endpoint. Thus a U segment has capacity at most two, a D1 segment capacity one, and a D2 segment capacity zero.

If a D1 ray from a multiple point v is adjacent to a D2 ray, their common sector is triangular. Let p be the ordinary far endpoint of the D1 segment and q the multiple far endpoint of the D2 segment. The opposite side of that triangular sector is the arrangement line pq. At p this is the unique transverse line. Since it contains the multiple point q, it is not clean. Therefore that D1 target has capacity zero. Counting each such D1 segment once gives total capacity at most 2U+D1-B. Since there are exactly n-h clean lines and each emits one charge,
n-h <= 2U+D1-B.

Defect identity. Let V_2 be the number of ordinary intersections and let the multiple multiplicities be r_v. Pairwise nonparallelism gives
C(n,2)=V_2+sum_v C(r_v,2).
The total number of line-vertex incidences is
2V_2+sum_v r_v = n(n-1)-sum_v r_v(r_v-2).
Each line with k finite vertices has k-1 bounded elementary segments, so the total number E_b of bounded elementary segments is
E_b=n(n-2)-S, S=sum_v r_v(r_v-2).
Every counted triangle contributes three side incidences. A bounded segment of use 0 contributes 0 instead of 1, and a shared segment contributes 2 instead of 1. Therefore
3T=E_b-U+D1+D2,
hence delta=n(n-2)-3T=S+U-D1-D2.

Core incidence. On a line containing k>=1 multiple points, the line contributes k to I and one to h, so it contributes k-1 to I-h. Along that line there are at most k-1 elementary core-to-core intervals, and every D2 segment is one of them. Summing gives D2<=I-h, equivalently h<=I-D2.

New direct q<=2 exclusion for n=18,T=95. Here delta=3. Dropping the nonnegative blocked correction from the charging inequality and eliminating U with the defect identity gives
2delta >= 18+2S-h-3D1-2D2.
For q=0 this requires 6>=18, impossible.
For q=1, D2=0, h=I=r, and d2=0 gives D1<=2r-4. Hence
6 >= 30+2r^2-11r.
For every integer r>=3 the right side is at least 15, contradiction.
For q=2, D2<=1; each core has d2<=1, so D1<=2I-8, and h<=I-D2. Hence
6 >= 42+2S-7I-D2.
The minimum over r_1,r_2>=3 and D2<=1 occurs at r_1=r_2=3,D2=1 and equals 11. Contradiction.

Dependency table / prior-work comparison.
- q=0,1,2: now directly excluded by this contribution; the prior protected restricted q<=2 upper theorem is not needed for this reduction.
- q=3: the seven admitted geometric premises in the prior three-core classification are either proved above or immediate corollaries (including d2<=1 sharpening and the triple refinement). I also checked its arithmetic elimination and saturated-template endpoint argument during this tranche; no additional source premise was found. Thus the q=3 exclusion is premise-complete mathematically, subject to non-authoring adjudication of this contribution.
- q=4: the initial five-profile reduction, D2 lower-bound replay, saturated-core nonextremality dependency, and the local fan/charging dependencies of the later 3333/3334 chain no longer require the previously unproved fan/charging premises. I did not independently rerun every q=4 finite certificate or re-prove every later case lemma in this bounded tranche, so the final q=4 closure is not independently certified by this comment.
- q=5: the exact q=5 profile replay uses precisely sector consistency, the no-long-run rule, the defect/core-incidence identities, and the blocked clean-line capacity proved above. Thus its reduction to 33333,33334,33344 is geometrically justified. The protected later q=5 closure has its predecessor fan/charging condition discharged, but its separate finite replays and the prior external residual proof were not independently replayed here.
- q=6: the internal replay's declared necessary-state relaxation is now supported by proved geometry rather than an unproved premise. In particular its use of U=3-S+D1+D2 and 18-I+D2<=2U+D1-B is justified. The 333444 saturated-prism argument was also checked: d1=3,d2=3 at triple cores forces alternating D1/D2; d1=5,d2=3 at quadruple cores plus no three consecutive D1 forces D1-gap multiset (2,2,1), so no adjacent D2 rays; an elementary D2 3-cycle then contradicts the elementary-triangle angular lemma. Therefore 333444 is premise-complete, pending non-authoring adjudication/replay. The q=6 profiles 333333,333334,333335,333344 remain unresolved.

The evaluator permits parallel lines. For hill-wide upper-bound reasoning I independently rederived the already-recorded projective normalization: choose a projective line M disjoint from all selected counted faces and all pairwise projective intersections, then send M to infinity. The selected faces remain bounded counted faces and all transformed arrangement pairs meet finitely. This is prior work, not a novelty claim.

## Assumptions beyond bootstrap
No hidden target, private evaluator fixture, competition submission, paid compute, or repository mutation was used.

The mathematical proof assumes distinct real affine lines. Pairwise nonparallelism is used inside the local proof, but the public hill permits parallels; the projective normalization above removes parallelism for any finite selected set of counted faces without decreasing its count. Multiple concurrence is unrestricted.

Authorship provenance: the mathematical argument and audit in this return were produced in this ChatGPT session by OpenAI GPT-5.6 Sol acting under AGENT_REF INDEPENDENT-AGENT-103. GitHub transport is authenticated through the account login fyremael. No separate human mathematical coauthor or independent checker participated in this tranche. The account environment can contain historical conversation context; I deliberately used only the launch packet and source artifacts explicitly followed from it as mathematical evidence, so this should not be represented as cryptographically isolated zero-context execution.

Review provenance: all computational checks reported below are same-session checks. They are not independent review, MATHCERT certification, or a substitute for the required non-authoring adjudication.

## Verification / falsification hooks
Pinned source-byte verification was performed by fetching each exact path at source head 36b7c79bebd42fde17ea9f0f809406fb55e093f9 and computing SHA-256 on the returned ASCII bytes. Actual output:

H1_SIX_CORE_PREMISE_PROOF.md
bytes=10051
sha256=631ecee3e7304ed8dac53b3de5f8b126adff49a5f446d57a69790df6623e1b21
match=true

H1_SATURATED_PRISM_OBSTRUCTION.md
bytes=4622
sha256=a82107eac72a6eaa09053e00b47582e63932840fb6f2436a8d1633db89041370
match=true

H1_Q6_INTERNAL_REPLAY.md
bytes=5390
sha256=c45b29d741769b006d62b3b8dbceca7bcaa570490fd19baa5110b642ad13b12e
match=true

Public evaluator/source identities additionally read during the audit:
MATHFORGE source-lock blob 7a90cd6eeb54e8e4c5b63c5977e40a1ab5bcaa2c
captured-statement blob 47e529bce21e76c575c69a26824e182848dceedc
evaluator-contract blob b9f9d8b58fa613c9e788d09f987b50260066bc67
The evaluator contract explicitly permits parallel lines and higher concurrence and counts bounded triangular faces by exact rational geometry.

Deterministic finite falsification hook used for the local sector corollaries (standard Python 3; 1=D1 in the saturated-word count):

python - <<'PY'
from itertools import product
def run(b,k):
    n=len(b)
    return any(all(b[(i+j)%n] for j in range(k)) for i in range(n))
def shared(t):
    n=len(t)
    return tuple(bool(t[(i-1)%n] and t[i]) for i in range(n))
for r in (3,4,5):
    N=2*r; best=-1; mind2=None
    for t in product((0,1), repeat=N):
        s=shared(t); idx=[i for i,x in enumerate(s) if x]
        for mask in range(1<<len(idx)):
            D1={idx[j] for j in range(len(idx)) if (mask>>j)&1}
            b=tuple(i in D1 for i in range(N))
            if run(b,r-1): continue
            d1=len(D1); d2=len(idx)-d1
            if d2<=1: best=max(best,d1)
            if r==3 and d1==3:
                mind2=d2 if mind2 is None else min(mind2,d2)
    print(f"r={r} max_d1(d2<=1)={best}")
    if r==3: print(f"r=3 min_d2(d1=3)={mind2}")
def sat(r,d1):
    return [b for b in product((0,1),repeat=2*r)
            if sum(b)==d1 and not run(b,r-1)]
print("saturated_r3_words",len(sat(3,3)))
print("saturated_r4_words",len(sat(4,5)))
PY

Actual output:
r=3 max_d1(d2<=1)=2
r=3 min_d2(d1=3)=3
r=4 max_d1(d2<=1)=4
r=5 max_d1(d2<=1)=6
saturated_r3_words 2
saturated_r4_words 8

Deterministic integer check used for the q<=2 reduction:

python - <<'PY'
n=18; delta=n*(n-2)-3*95
print("delta =",delta)
print("q=0 necessary inequality:",2*delta,">=",n,"=>",2*delta>=n)
v1=[]
for r in range(3,19):
    S=r*(r-2); I=r
    v1.append((n+2*S-7*I+12,r))
print("q=1 minimum RHS:",min(v1),"; 2delta =",2*delta)
v2=[]
for r in range(3,19):
  for s in range(3,19):
    S=r*(r-2)+s*(s-2); I=r+s
    v2.append((n+2*S-7*I+24-1,r,s))
print("q=2 minimum RHS:",min(v2),"; 2delta =",2*delta)
PY

Actual output:
delta = 3
q=0 necessary inequality: 6 >= 18 => False
q=1 minimum RHS: (15, 3) ; 2delta = 6
q=2 minimum RHS: (11, 3, 3) ; 2delta = 6

No independent replay or formal checker has reviewed the proof in this session. Promotion therefore still requires the task-mandated non-authoring adjudication.

## Claim boundary
This contribution establishes the requested affine-geometric premises and the stated corollaries as paper proofs, not as kernel-checked formal theorems. It establishes a new direct q<=2 exclusion for n=18,T=95 and removes the previously missing fan/clean-line geometric assumptions from the q<=6 necessary-state machinery.

It does not by itself certify the complete prior q=4 or q=5 closure, because their separate finite certificates and later case arguments were not all independently replayed inside this timebox. It does not prove T<=94 globally: q>=6 remains, and within q=6 the profiles 333333,333334,333335,333344 remain live after the 333444 obstruction. It makes no optimality, novelty, competition-score, official-submission, or certification claim.

## Next residual
Non-authoring adjudication should first replay the four lemmas and the new q<=2 inequality, then rerun the protected q=4/q=5 dependency chain to determine whether those existing closures can be promoted without the former source-condition labels. For q=6, retain 333333,333334,333335,333344 as the mathematical residual and treat 333444 as promotable only after that adjudication. Do not spend search effort on 333444 unless the proof replay fails.