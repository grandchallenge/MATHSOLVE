# SCC-001: common spectral incidence and a universal packet-relaxation barrier

Status: author-derived exploratory propositions and exact finite replay; not independently adjudicated, Lean-certified or novelty-certified. Continues SPECTRAL_STRATA.md (#1357) and SPECTRAL_PARITY_GEOMETRY.md, at protected base d3af19a08c0d1cfe2439148f2020cb4496c592ad, also preserving TWO_WITNESS_REACHABILITY.md (#1360). One Boolean output, arbitrary AND reuse, free affine operations. This is a precise no-go for a specified relaxation, not for the exact common operand lift.

## 1. Exact common active-mask incidence

Let b=(p_j,q_j) in F2^(2t) be a lifted frequency, M=L^T the common surjective frequency projection on the r-dimensional reduced target, and a(b)=c+Db the affine active flag vector of SPECTRAL_STRATA.md. The row j of D has nonzero entries only in pairs l>j. The surviving stratum at label A (identified with its indicator vector) is exactly
    P_A={b: Db=A+c; (p_j,q_j)=0 for j not in A}.
The sign is the common quadratic Q(b), and amplitude is 2^(-|A|).

Let K=ker M and J=D(K). The linear map D descends modulo J to a unique linear map E:F2^r -> F2^t/J satisfying E(Mb)=Db+J. This is well defined by the definition of J and surjectivity. For every nonzero projected packet support T_A (after the quadratic Gauss sum), with affine output frequency shift ell,
    T_A subset {u: E(u+ell)=A+c+J}.
Thus packets are grouped by a common quotient syndrome. Distinct labels A,B can overlap only if A+B in J. For any output frequency u, the affine span of all labels of nonzero packets at u has dimension <= dim J <= min(t-1,2t-r). The bound t-1 follows because the last row of D vanishes (t>=1). There are at most 2^dim J labels at a point. These statements remain true for arbitrary slack; at large slack they can be weak.

More generally, for any finite list of actual lifted points b_i in P_(A_i) and any binary coefficients eps_i with sum eps_i=0 and sum eps_i b_i=0, necessarily sum eps_i A_i=0. Equivalently the affine assignment b -> A on the union of strata must extend to a single affine map on the ambient space; checking this by elimination is exact, not a circuit enumeration. The row restrictions of D impose the stronger suffix version: for each j the j-th flag must be an affine function only of pairs later than j. This is necessary AND sufficient to reconstruct one triangular flag map from prescribed labelled points: solve each row's affine linear system independently. Point consistency alone does not require equality with all valid frequencies. However, the unit Parseval condition makes equality automatic, as proved in section 3.

## 2. Universal common-packet relaxation

Consider the following relaxation of a t-gate Fourier lift, for a target on r bits:
* one ambient F2^(2t), one surjective linear M to F2^r, one quadratic Q with standard hyperbolic quadratic part sum_j p_j q_j (plus linear/constant terms);
* disjoint possibly empty affine P_A indexed by distinct active subsets A of [t], with zero coordinates in inactive gate pairs, dimension >= t+1-2(t-|A|), and coefficient (-1)^Q 2^(-|A|) on P_A, zero elsewhere;
* Parseval and a Boolean inverse Walsh spectrum on the full ambient space;
* the common fibre sum is the target Walsh spectrum. Thus all the Gauss packet amplitude, affine support, quadratic sign and dimension conditions of SPECTRAL_STRATA.md hold.

Drop the requirement that the P_A are the EXACT solution sets of one common affine flag map with triangular rows. In particular the set of nonempty labels need not arise from those equations. The following theorem gives a linear ceiling for this relaxation, even though it retains all signs, common quadratic geometry, shared affine fibres, and exact Booleanity on the lifted domain.

Theorem: every Boolean f on r>=1 bits satisfies the relaxation at t=3r+2. The construction uses the truth table of f to choose strata and is not an efficient circuit construction.

Proof. Use r mandatory gate pairs B_i, two selector gate pairs C_(i,0), C_(i,1) per i, and two sign gate pairs S_0,S_1. These total t=3r+2. For each x in F2^r use the active label A_x consisting of all B_i, exactly C_(i,x_i) for every i, and S_(f(x)). Thus |A_x|=2r+1, and labels are distinct. The affine stratum P_x is defined by:
    B_i: (p,q)=(a_i,x_i), a_i free;
    C_(i,x_i): both coordinates free; C_(i,1-x_i): both zero;
    S_(f(x)): both free; S_(1-f(x)): both zero.
There are 2^r disjoint strata (the B_i q coordinates identify x), each of dimension r+2r+2=3r+2. All inactive coordinates vanish. The dimension requirement is t+1-2(t-|A_x|)=r+1, so it holds with room to spare.

Let Q=sum_all_pairs p q + p_(S_1)+q_(S_1). Let M(b)=(p_(B_i))_i. This is one common surjective map and one common hyperbolic quadratic phase for all strata. Define W(b)=2^(-2r-1)(-1)^Q on their union, zero otherwise. Parseval holds exactly: the number of nonzero points is 2^(4r+2), each squared magnitude 2^(-4r-2).

For a fixed projected frequency a, sum W over the fibre. In each stratum x, the mandatory pairs give sign (-1)^(a dot x), the r free selector pairs give Gauss factors 2 each, and the sign pair gives 2(-1)^f(x) (sum over p,q of (-1)^(pq) is 2, and with p+q added it is -2). Thus the entire fibre sum equals
    2^(-r) sum_x (-1)^(f(x)+a dot x)=W_f(a).
In particular each individual projected packet has full support F2^r, linear phase a dot x+f(x), and magnitude 2^-r. In scaled units 2^t this is valuation t-r=2r+2; all predecessor dimension and valuation bounds hold.

The inverse Walsh transform is Boolean on the entire lifted domain, not just the target slice. At arbitrary ambient input v, the sum over the r mandatory p coordinates enforces x_i=v_(B_i,p) by orthogonality and contributes 2^r. Only one stratum remains. The fixed mandatory q coordinates give a sign; each of the r+1 free active pairs gives a Gauss factor of absolute value 2, even with any linear character from v and Q. The total absolute value is 2^(-2r-1) 2^r 2^(r+1)=1. Thus the inverse Walsh transform is everywhere +/-1, as required. This proves the theorem for arbitrary f, with no bound on its actual multiplicative complexity.

The construction also preserves the weak quotient-syndrome conditions from section 1 if one merely permits a free J of dimension <= min(t-1,2t-r): choose J to contain the label differences, of dimension <=r+1 (the r complementary selector choices and one complementary sign choice), and take E=0 with appropriate c. Thus the syndrome bound alone cannot repair the relaxation. This choice does not assert the existence of the underlying common flag map D on the lifted points.

## 3. Exact incidence test for a supplied normalized decomposition

Let a relaxed decomposition from section 2 be supplied explicitly by one affine basis (base point plus a direction basis) for each nonempty P_A, with the specified common Q and M. For each j form the linear system for unknown c_j and the coefficients D_(j,l) on all pairs l>j:
    c_j + sum_(l>j)(D_(j,l,p) p_l + D_(j,l,q) q_l) = A_j
at the base point and the base point plus each basis direction of each P_A. Because both sides are affine on each stratum, these equations hold at every point of P_A iff they hold at those basis points. There are 1+2(t-j) unknowns in row j (using 1-based gate indices).

Theorem: the relaxed decomposition comes from a triangular common operand lift, with its supplied Q, M and labels, iff every such row system is consistent.

Necessity is section 1. For sufficiency choose solutions, set the affine operand-offset coefficients of gate l using the two entries in row j at pair l, the constants using Q's linear coefficients, and the output mask using c and Q's constant term. These specify a legitimate triangular circuit on the independent 2t operand bits. By the exact reverse Fourier formula, each supplied point belongs to the actual stratum with the same label and has exactly the supplied coefficient. The actual normalized Walsh spectrum has squared mass one by Booleanity and Parseval. The supplied disjoint strata already have total squared mass one, and all actual nonzero coefficients have strictly positive squared mass. Therefore there are no additional valid points: actual and supplied strata coincide, with identical coefficients and common projection. Restriction along M^T gives the target circuit. This proof does not require an extra Boolean-inverse assumption for sufficiency; Parseval and point consistency already imply it.

An inconsistent row has a certificate consisting of at most 2(t-j)+2 of the tested points, with an even number of selected points, XOR of their later pairs zero, and XOR of their j-th active bits one. Indeed take a minimal linear dependence of augmented suffix vectors (1,b_(>j)) with inconsistent right-hand sides. Equivalently use a basis of the row vectors and a conflicting dependent equation, at most the dimension plus one equations. Such a certificate is directly checked and uses no search over circuits. It may involve repeated points in the listing but redundant copies can be removed. A separate, weaker unrestricted affine-map test allows all pairs as unknowns. The certificates prove incompatibility of a supplied decomposition, NOT nonexistence of every decomposition for the target. The number of supplied strata may itself be exponential in t.

For the universal construction, take the canonical representative b_x of P_x with every free coordinate zero, leaving only q_(B_i)=x_i. The map x->b_x is linear. The active flag of S_1 is f(x). If f is nonaffine, there exist x,y with f(0)+f(x)+f(y)+f(x+y)=1: otherwise f+f(0) is additive and hence linear over F2. The four representatives sum to zero and their S_1 flags sum to one. Therefore this particular relaxed decomposition fails even unrestricted affine flag consistency, independent of the ordering of gates. For affine f, ordering all mandatory B pairs last yields a valid triangular flag map: mandatory flags are one, selector flags are x_i or 1+x_i read from q_(B_i), and sign flags are f(x) and 1+f(x). The exact consistency theorem applies. Thus this construction makes the lost incidence visible as an explicit four-point certificate for every nonaffine target; it does not exclude other compatible decompositions of such targets.

## 4. Exact replay

Run python3 research/SCC-001/common_packet_incidence_replay.py. Reconstructs the triangular flag rows from the supplied affine bases of 72 genuine lifts at budgets one through six, compares 65,520 full lifted coefficients and the reconstructed Boolean functions, checks 5,007 basis equations, 250,304 quotient-syndrome points and 5,869 nonzero packet-overlap rank tests. Tests the universal construction on all Boolean functions on one, two and three bits and twelve seeded four-bit functions (288 targets; 259 nonaffine). Row consistency matches affine target status; inconsistent systems return explicit bounded-size dependence certificates. Enumerates 1,130,752 packet points, verifies common projection against the independent target Walsh transform, unit Parseval and inactive-coordinate constraints. Full ambient inverse transforms check all 1,052,672 values for every one- and two-bit target; 64 larger inverse samples on selected three- and four-bit targets. All passed; initial capture bb7a5011f01f44c79f90d04012d9fbc0. These are bounded author-side checks, not independent adjudication or a substitute for the general proof.

## 5. Consequence for structural capacity

For every reduced r-variable target the relaxed feasibility threshold is at most 3r+2, hence at most 3n+2 in input count. Any lower-bound test that depends only on infeasibility of this relaxation cannot establish superpolynomial multiplicative complexity. This remains true if it tests the entire signed spectrum, the common quadratic phase, exact affine packet intersections and fibre sums, the lifted Boolean inverse, Parseval, or the weak quotient-syndrome conditions. It does not apply to tests requiring the labelled affine incidence of section 3, or other additional constraints not preserved by the construction. Nor does it rule out an independent obstruction computed directly from the target that excludes ALL compatible decompositions at a given budget.

At large slack, a genuine lower bound must therefore exploit the shared triangular flag equations (or constraints comparably strong but easier to evaluate). The normalized incidence theorem removes the separate omitted-point verification burden for a proposed decomposition, but the existence of some compatible decomposition is exactly the original circuit problem. The next substantive task is to derive a target-only necessary condition on the incidence of every potential decomposition, preferably via polynomial identities among the spectrum's affine restrictions or correlations, rather than solve the equivalent existential circuit problem. No explicit superpolynomial target demand or unrestricted SAT lower bound, no certification or novelty claim.

Boundary: COMMON_FLAG_INCIDENCE_EXACT_WITH_PARSEVAL__FULL_BOOLEAN_COMMON_PACKET_RELAXATION_LINEAR_CEILING__TARGET_ONLY_INCIDENCE_OBSTRUCTION_OPEN.
