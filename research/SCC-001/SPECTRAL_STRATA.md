# SCC-001: affine-quadratic spectral strata and budget-slack obstructions

Status: exploratory author-derived propositions and exact finite regression; no independent adjudication, Lean certification or novelty claim. Continues FOURIER_FIBRE_CAPACITY.md (#1355, protected base 2fdc062bcc88837887b833675a04621ef6a39c5a). One Boolean output, arbitrary AND reuse, free affine operations. The entire spectral partition is constrained, not characterized sufficiently for circuit realization.

## 1. Exact active-set strata

Use the common operand lift and notation of the predecessor. Write frequency b=(p_j,q_j)_{j=1}^t. Let alpha_{lj}, beta_{lj} be the coefficients of the earlier gate Z_j in the affine operand offsets of gate l>j; index 0 denotes the constants. Let c_j be the output mask. Define
    a_j(b)=c_j+sum_{l>j}(p_l alpha_{lj}+q_l beta_{lj})
over F2. These are affine linear forms in the same frequency vector. For a surviving reverse recursion, the current output bit at step j is exactly a_j(b), because an inactive gate has p_l=q_l=0 and therefore contributes nothing to the earlier mask update. Conversely if p_j=q_j=0 whenever a_j(b)=0, descending induction proves that the recursion survives and these are its active bits.

For any A subset [t], the valid frequencies with active set A are therefore exactly the affine subspace
    P_A={b:a_j(b)=1_A(j) for all j; p_j=q_j=0 for j notin A},
possibly empty. These spaces are disjoint. The sign on each is the restriction of the common quadratic
    Q(b)=c_0+sum_j(p_j q_j+p_j alpha_{j0}+q_j beta_{j0}).
The Walsh coefficient is (-1)^Q(b) 2^(-|A|) on P_A and zero outside the union. This follows directly from the predecessor pair recursion, or induction on descending j. In particular P_A is not an arbitrary independently chosen support. The equation at j=t is constant. For t>=1, every nonempty stratum with j=t-|A| inactive gates has dimension at least t+1-2j: at most t-1 active-bit constraints and 2j zero-coordinate constraints in 2t variables. A negative lower bound is harmless.

## 2. Quadratic fibre pushforward

Let L be the injective operand map on the reduced r-variable input, M=L^T, and P=b0+U any nonempty stratum. K=U intersect ker M has dimension k. Let the polar alternating form of Q restricted to K have rank 2h. Choose a linear section of M on U, so a preimage b(a) in P of a in M(P) depends affinely on a. The fibre sum
    sum_{z in K} (-1)^Q(b(a)+z)
is zero or has magnitude 2^(k-h), with support an affine subspace of M(P) and quadratic sign on that support.

Proof: the exponent restricted to z is a fixed quadratic on K plus a linear functional depending affinely on a, plus Q(b(a)). Choose a symplectic basis of the polar form, with h pairs and a radical of dimension k-2h, by iterative splitting of a pair of polar value one. On radical coordinates the exponent is affine linear; summation forces its linear coefficients to vanish, giving at most k-2h affine equations in a and a factor 2^(k-2h). On each pair the quadratic is xy plus linear terms Ax+By, and summing its four values gives 2(-1)^(AB). Here A,B are affine in a, and the remaining factor (-1)^Q(b(a)) has quadratic phase. Thus all nonzero sums have the asserted magnitude, quadratic sign and affine support, of dimension at least dim U-k-(k-2h)=dim U-2(k-h). The phase can be extended to the whole output frequency space by extending affine coordinates from the support.

Multiplying by 2^t and incorporating the affine output frequency shift and constant sign, the target integer spectrum Z(a)=2^t W_f(a) has the exact simultaneous representation
    Z(a)=sum_{A subset [t]} 2^e_A 1_{T_A}(a) (-1)^q_A(a),
where empty packets are discarded, T_A is an affine subspace, q_A has degree <=2 on it, and e_A=t-|A|+k-h>=t-|A|. All packets are derived from the same M and Q; the representation is not sufficient if arbitrary packets are chosen independently. For t>=1,
    dim T_A >= t+1-2e_A.
This follows from the preceding dimension bound for P_A and the fibre dimension loss. This is a coupled magnitude/geometry constraint; even after dropping common-map compatibility it imposes nontrivial necessary restrictions.

## 3. Granularity-saturated and one-slack odd masks

Let gamma be the true Walsh granularity and O_f(a)=(2^gamma W_f(a)) mod 2, the nonzero Boolean mask of coefficients with maximal denominator. Suppose f is computed in t>=gamma gates, with s=t-gamma. Then O_f is bit s of Z modulo 2^(s+1).

When s=0 and t>=1 only the all-active packet can contribute (e_A=0 forces no inactive gates and k=h=0). Hence O_f is exactly the indicator of a nonempty affine subspace of dimension >=t+1. This prohibits any nonaffine odd mask irrespective of whether every individual coefficient meets signed-digit capacity. The affine target case t=0 is excluded from the dimension statement.

When s=1, the only possible exponent-zero packet would be the all-active one, and it must be absent since every Z(a) is even (otherwise its nonempty support would yield an odd entry). Thus O_f is the XOR of the exponent-one packet indicators. Only the all-active and the t one-inactive sets can contribute, so at most t+1 affine subspaces are needed, each of dimension >=t-1. This is a joint obstruction on the full odd mask, not a claim about signs individually.

## 4. General slack: an independent affine-atom bound

Write rho(O) for the minimum number of affine subspace indicators whose XOR equals a Boolean frequency mask O (empty set gives zero). This is not circuit minimization. For s>=0 put
    M(t,s)=sum_{j=0}^{min(s,t)} binomial(t,j), R(r)=1+r+binomial(r,2).
Then
    rho(O_f) <= (1+(s+1) M(t,s) R(r))^(2^s).
Proof: only e_A<=s packets affect the residue modulo 2^(s+1), so there are at most M(t,s). A signed packet of exponent e has bit e equal to 1_T, bits below e zero, and each bit above e equal to 1_T q_A (the binary residue of -2^e has ones from e upwards). Extend q_A as a degree-two polynomial on r coordinates. Each monomial times 1_T is an affine indicator (intersect with the corresponding coordinate-one hyperplanes), so each bit is an XOR of <=R(r) affine indicators.

For any integer z, bit s of its residue modulo 2^(s+1) is the coefficient of X^(2^s) in (1+X)^(z mod 2^(s+1)) over F2: expand the binary factors (1+X^(2^j)) at its set bits. The same coefficient is obtained by multiplying these factors for all the packet residues, since changing the exponent by 2^(s+1) changes nothing in degrees <=2^s. Consequently this bit is a sum of products of packet bits, with the selected bit weights summing to 2^s. At most 2^s bits are selected; each expands into at most R(r) affine indicators and their products remain affine indicators. There are at most N=(s+1)M(t,s) bit positions. An upper bound on all expanded products is (1+NR(r))^(2^s), by padding ordered choices with a dummy. This counts generously and requires neither independence of carries nor nonnegative original coefficients. At s=0,1 use the sharper statements in section 3.

For fixed s the bound is polynomial in t,r. For s growing slowly it still constrains a global parity mask even when every spectral coefficient is a signed power of two. It is a necessary relaxation: it forgets the common M,Q and correlations among packet supports after their exact derivation. No assertion of sufficiency or polynomial cost of determining rho.

## 5. Explicit cheap family where the individual spectral test is blind

For m>=2 let S(u)=1 if the Hamming weight of u in F2^m is nonzero modulo 3, and define
    f_m(x,z;u,b)=x dot u + z b S(u),
where x,u have m bits, z,b one bit. All sums are over F2. Put pi(u,b)=(u,b S(u)). Then f_m is the inner product of (x,z) with pi(u,b). Its normalized Walsh coefficient at frequencies (a,v) of the two (m+1)-bit blocks equals
    2^(-m-1) sum_{y:pi(y)=a} (-1)^(v dot y).
For S(u)=1 the two preimages are singleton fibres at output labels (u,0),(u,1); for S(u)=0 there is one two-point affine fibre at (u,0) and no fibre at (u,1). Thus all nonzero Walsh magnitudes are exactly 2^(-m-1) or 2^-m, gamma=m+1, and D=1 in the predecessor signed-digit bound. The odd mask O_f is exactly S(u) in the first m coordinates of a, independent of all other frequency coordinates. The degree is <=m+2.

The nonlinear dimension r is 2m+2. Indeed any constant derivative in direction (a,c;v,d) forces v=0 by varying x; then varying z forces d=0 because S is not identically zero. The remaining derivative a dot u+c b S(u) is constant only if c=0 (vary b at a true u), then a=0. Hence the maximum of degree-minus-one, gamma, half the nonlinear dimension rounded up, and signed-digit lower bounds is exactly m+1. At t=m+1, the nonaffine mask excludes the budget: restrict to two u bits with the others zero to get the three-point nonzero mask, which is not affine. In particular C_times(f_m)>=m+2 for every m>=2, while all coefficients individually satisfy the signed-digit test even at budget m+1.

There is an asymptotically stronger obstruction using the established Smolensky low-degree approximation theorem. Source: S. Srinivasan, "On Improved Degree Lower Bounds for Polynomial Approximation", FSTTCS 2013, DOI 10.4230/LIPIcs.FSTTCS.2013.201, abstract at https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2013.201 (external theorem, not reconstructed or certified here). In particular there exist constants c,delta>0 such that for sufficiently large m, every F2 polynomial of degree <=floor(c sqrt(m)) has uniform error >=delta against this MOD3 convention. If S is an XOR of K affine indicators, discard those of codimension >d=floor(c sqrt(m)). The rest is a polynomial of degree <=d, and discarded supports have total mass <=K 2^(-d-1). Therefore K>=delta 2^(d+1). Restricting any representation of O_f to the m coordinates of u (fix all other frequencies zero) preserves the affine-indicator dictionary, including empty intersections. Thus rho(O_f)>=delta 2^(d+1).

Take t=m+1+s, s=floor((log2 m)/4). For sufficiently large m, t<=2m, r=2m+2, M(t,s)<=(s+1)t^s. The base-two logarithm of the section 4 capacity is at most 2^s O((s+1) log m)=O(m^(1/4)(log m)^2)=o(sqrt(m)). It contradicts the preceding lower bound. Padding permits exclusion of all budgets <=t. Consequently, for all sufficiently large m,
    C_times(f_m) >= m+2+floor((log2 m)/4).
This is an unbounded additive improvement over all four elementary bounds, including the previous signed-digit test which here has D=1. The numerical threshold for "sufficiently large" depends on the approximation constants and is not claimed explicit. The family remains uniformly cheap: maintain the three residue indicators by updating r_j to r_j+u_i(r_j+r_(j-1 mod 3)) using three ANDs per input bit, add residues 1 and 2, use m ANDs for x dot u and two for zbS. Thus <=4m+2 gates. This result is not a superpolynomial SAT lower bound, and it relies on the cited established approximation theorem only for the asymptotic improvement; the finite one-gate exclusion is self-contained.

## 6. Exact finite replay

Run python3 research/SCC-001/spectral_strata_replay.py. Standard-library integer arithmetic, seed 281126. The independent formula for active flags and common quadratic phase is compared against the predecessor reverse recursion at 65,892 lifted frequencies across 102 lifted outputs with one through six gates; 376 nonempty strata have exact affine cardinalities and the dimension bound. Independent full-rank linear maps with arbitrary cross-pair mixing and affine output shifts give 1,347 Gauss packet checks (1,202 nonzero); the fibre polar rank determines the magnitude, and direct affine-coordinate Mobius transforms verify the quadratic phase and 3,351 affine phase atoms. All 74,412 target coefficients are reconstructed and compared with direct Walsh transforms on the input slice. Checks include 160 saturated/one-slack odd masks, 296,591 signed carry bit comparisons and 303 expanded atom-count bound comparisons. The six MOD3 targets m=2,...,7 have direct full truth-table Walsh, granularity, nonlinear dimension, degree and nonaffine odd-mask checks; D=1 throughout. Initial execution capture 3e8a07dd637b4ac9baa5d20430ec1870. These are finite author-side regression checks, not a proof of the general statements or an independent validation of Smolensky's theorem. The asymptotic bound uses the external theorem as stated in the cited publisher abstract.

## 7. Limits and next boundary

The active-set and quadratic-fibre formulas are exact. The independent parity-mask test is strictly stronger on this family than the individual-coefficient projection, and gives an arbitrary-slack necessary inequality. It still cannot address budgets substantially larger than the nonlinear dimension: if t>=r>=gamma and s=t-gamma is large, the displayed upper bound may exceed the trivial rho<=2^r (one point per atom). No general lower bound for the complete common-map compatibility problem is claimed. The next issue is to retain simultaneous constraints among packet supports and signs without the exponentially slack-sensitive carry expansion; or show a rigorous limitation of such relaxations. No independent adjudication, Lean formalization, novelty or SAT separation claim.

Boundary: AFFINE_QUADRATIC_ACTIVE_STRATA_EXACT__COLLECTIVE_ODD_MASK_OBSTRUCTION__EXPLICIT_LOG_GAP_BEYOND_SIGNED_DIGITS__LARGE_SLACK_COMMON_MAP_OPEN.
