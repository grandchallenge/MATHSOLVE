# SCC-001: common operand lifts and signed-dyadic Fourier fibre capacity

Status: exploratory author-derived propositions and exact finite regression, not independently adjudicated, Lean-certified or novelty-certified. Continues BUDGET_EXTERIOR_SHADOW.md (#1346, merge 768a7f2380c6a3cfe72f7240f00726d58234047e) at protected base 594815f9216d6ffaa815b86c77dae88238b632a6. One Boolean output, affine operations free, unrestricted multiplication reuse. This is a necessary spectral shadow of the shared branch correlations, not a sufficient characterization of circuit reachability.

Literature context: the dual-domain dimension lower bound is established in C.-P. Schnorr, "The multiplicative complexity of boolean functions", AAECC-6, DOI 10.1007/3-540-51083-4_47. The affine-input topology and linearity-dimension framework is also developed in "Boolean Functions with Multiplicative Complexity 3 and 4", https://pmc.ncbi.nlm.nih.gov/articles/PMC7918276/ . Bibliographic and abstract/text comparison only, not a systematic novelty audit; no novelty claim for the operand lift, dimension bound, Fourier granularity or general Fourier analysis. The specific fibre/digit inequality and example below are proved directly.

## 1. Nonlinear dimension and the common operand lift

For f:F2^n -> F2 put S(f)={a : f(x+a)+f(x) is constant in x}, a linear subspace. The constant derivative is a linear character of S(f); extend it to a linear function l on the input space. Then f+l is constant on cosets of S(f), so descends to a function h on r=n-dim S(f) variables, with no nonzero constant derivative. Its multiplicative complexity equals that of f: lift a circuit using the linear quotient map and add l freely in one direction; in the other restrict f+l to a linear section of the quotient. Adding affine terms, invertible affine changes and unused spectators preserve r and the multiset of nonzero normalized Walsh magnitudes (the latter by Fourier substitution and orthogonality). Thus we may study h on r variables with S(h)=0.

Suppose h is computable with t multiplications, padding with redundant gates if needed. Write each gate as
    G_j=(a_j(x)+alpha_j(G_1,...,G_{j-1}))
         (b_j(x)+beta_j(G_1,...,G_{j-1})),
where a_j,b_j are linear forms in the original inputs and alpha_j,beta_j are affine functions of earlier gate outputs, including constants. The output is l_out(x)+c dot G + c_0. Let L:F2^r -> F2^(2t) collect all a_j,b_j. If a vector lies in ker L, all gates are unchanged under its translation, so the output changes by a constant. Thus ker L=0, proving the known bound r<=2t. The original affine output can be removed, changing only the frequency shift and overall sign.

On 2t formal independent bits (X_j,Y_j), retain exactly the same alpha_j,beta_j and output mask c, and define
    Z_j=(X_j+alpha_j(Z_<j))(Y_j+beta_j(Z_<j)),
    H=c dot Z.
Then h(x)=H(Lx)+l_out(x)+c_0. All correlations among nonlinear branch choices are retained by the common triangular dependency coefficients, and all dependencies among initial operands are retained by the single subspace im L. This statement is exact; any such representation defines a circuit, but finding one is not proposed as a lower-bound algorithm.

## 2. Exact common Fourier recursion

Define normalized Walsh coefficient W_H(p,q)=E[(-1)^(H+sum_j(p_j X_j+q_j Y_j))]. Process pairs j=t,...,1 while maintaining a mutable output mask c on the remaining earlier gates and a scalar multiplier, initially 1.

* If c_j=0, averaging over X_j,Y_j gives zero unless p_j=q_j=0. In the latter case delete the pair, without updating c.
* If c_j=1, shift independent uniform bits by alpha_j,beta_j. The local Walsh coefficient of XY is (1/2)(-1)^(p_j q_j). The remaining sign is (-1)^(p_j alpha_j+q_j beta_j). Multiply by the corresponding signed 1/2 (including the constants of alpha,beta), and add the earlier-gate coefficient masks of p_j alpha_j+q_j beta_j to c.

This follows by summing the four values of the pair; no probabilistic independence of the original circuit gates is assumed. For a fixed lifted frequency the recursion is deterministic and yields either zero or a single signed power 2^-k with 0<=k<=t. This is true for every output mask of the same lift; all share the same transition rules. It is not true in general for the original circuit before restriction to im L.

The recursion is also an exact four-block relation: at any active j, each choice (p_j,q_j) produces a normalized spectrum of the same earlier lifted gates with updated output mask and scalar of modulus 1/2. Its squared mass is 1/4 by Parseval. At an inactive j only the zero pair is allowed. Thus the lifted spectrum is the leaf distribution of a common labelled four-way recursion with total squared mass 1. Every nonzero lifted frequency has a unique path; there is no independent choice of its sign or exponent. No sufficiency is claimed for a vector merely satisfying the dyadic magnitude constraint.

## 3. Fibre capacity and an independent signed-digit obstruction

For a linear injective L, expanding H's sign in Walsh characters gives
    W_(H composed L)(a)=sum_{b:L^T b=a} W_H(b).
Every fibre contains exactly 2^(2t-r) frequencies because L^T is surjective. The output affine function shifts the frequency index and possibly changes all signs. Thus for every coefficient W_f(a), after stripping spectators and harmless affine terms, 2^t W_f(a) is an integer expressible as a sum of at most 2^(2t-r) signed nonnegative integer powers of two. This also holds on the original n-dimensional spectrum: normalized nonzero coefficients are the same up to sign after reduction, and zero coefficients are harmless.

For integer z define w(z)=min number of terms in a sum of signed powers 2^j, j>=0, equal to z, with w(0)=0. This is an arithmetic measure of the target coefficient, not circuit minimization. Cancelling opposite equal terms and carrying same-sign equal terms shows that an optimal representation uses distinct exponents, so parity gives
    w(2z)=w(z),
    w(2z+1)=1+min(w(z),w(z+1)) for z>=0,
with w(1)=1 and w(-z)=w(z). The even recurrence follows since an even number in a distinct-exponent representation cannot use exponent zero, and the converse follows by doubling. For odd numbers the coefficient at exponent zero is either +1 or -1, giving both directions. The recurrences compute w by a short memoized digit recursion (or standard signed-digit arithmetic). They also imply scale invariance under multiplication by any integer power of two.

Let gamma be the least nonnegative integer making 2^gamma W_f(a) integral for every a (Walsh granularity), and D=max_a w(2^gamma W_f(a)). For nonzero sign functions D>=1. Every t-gate circuit necessarily satisfies
    t>=gamma,
    D<=2^(2t-r),
    t>=ceil((r+log2 D)/2).
All quantities on the right are determined directly from f. Equivalently use integer comparisons D<=2^(2t-r) without floating point. This is stronger than the dimension and granularity bounds in examples below. In particular at r=2t, every nonzero Walsh coefficient must be a signed power of two. At nonzero slack the bound counts the maximum necessary number of signed dyadic contributions within a common fibre. It does not assume that arbitrary signed representations can be assembled consistently across all fibres.

A further joint necessary condition uses the same lifted spectrum: if N_j is the number of nonzero coefficients of magnitude 2^-j, then sum_j N_j 4^-j=1, with 0<=j<=t. All target coefficients must be formed by a partition into disjoint equal-size fibres of this single signed multiset (the fibres are parallel affine cosets, not arbitrary bins). This is a coupled constraint; dropping their affine geometry is only a relaxation. We do not assert an independent demand lower bound from that full partition condition yet.

## 4. Explicit family with an unbounded additive improvement

For even m=2s>=4 put k=(4^s-1)/3=1+4+...+4^(s-1). On m-bit y, define pi(y) in F2^m by the following lexicographic truth table (indices are ordinary binary integers):
    first k entries: zero;
    next one: e_2;
    next one: e_1+e_2;
    next two entries for each i=3,...,m: e_i;
    remaining entries: e_1.
There is at least one remaining entry, since 2^m-k-2m+2>=1 for m>=4. The number of remaining entries is odd. Every coordinate of pi has even parity over its table: coordinate one has the odd final count plus the one mixed entry, coordinate two has two entries, and each later coordinate has two. Thus each component of pi has Boolean degree at most m-1. Define the scalar target
    f_m(x,y)=x dot pi(y),  x,y in F2^m.
It has degree <=m and all 2m nonlinear dimensions: if translation by (a,b) has constant derivative, varying x forces pi(y+b)=pi(y). Since the zero fibre has odd cardinality k, translation by a nonzero b cannot preserve it (its orbits would be pairs). Hence b=0. The remaining derivative a dot pi(y) is constant only for a=0, because pi attains zero and every basis vector. Thus r=2m.

Its normalized Walsh coefficients are
    W_f(u,v)=2^-m sum_{y:pi(y)=u} (-1)^(v dot y).
In particular W_f(0,0)=k/2^m, and gamma=m because k is odd. The usual degree, granularity and nonlinear-dimension lower bounds have maximum m. Yet w(k)=s. Proof: write k_s=4k_(s-1)+1. The recurrence gives
    w(k_s)=1+min(w(k_(s-1)),w(2k_(s-1)+1)).
Since w(a+1)>=w(a)-1 by the triangle inequality, the odd recurrence implies w(2a+1)>=w(a). Induction from k_1=1 gives w(k_s)=s. Consequently every circuit requires
    C_times(f_m) >= m + ceil(log_4 s).
This is an unbounded logarithmic additive improvement over the maximum of those three elementary bounds. No claim of optimality or improvement over every known multiplicative-complexity method is made. In particular the family is cheap: a comparator with the fixed constant k and equality tests for the 2m-2 exceptional indices implement pi with O(m^2) charged operations, and the final dot product costs m further AND gates. One can use literal products for equality and the usual most-significant-bit scan for a fixed comparator, with OR expressed using XOR and AND. The construction is uniform, with descriptions polynomial in m.

The signed-digit test by itself cannot give a superpolynomial lower bound. In the reduced r-dimensional domain every nonzero coefficient is an integer multiple of 2^-r, so gamma<=r and D<=r+1 by ordinary binary expansion. In fact it cannot exclude a budget t>=r for r>=1 since r+1<=2^r. The exact common spectral recursion and the affine-fibre compatibility are stronger constraints than the scalar projection; the latter's ceiling is a rigorous limitation, not a dismissal of the full object.

## 5. Exact finite replay

Run python3 research/SCC-001/fourier_fibre_replay.py. Standard-library integer Walsh transform independently checks 117 lifted outputs with budgets zero through six, arbitrary affine dependence on prior gates, and multiple masks on the same lift: 65,907 coefficient comparisons. Random full-column-rank maps include cross-pair dependencies, affine output offsets and zero-dimensional/full-dimensional slices: 76,395 exact fibre sums, fibre cardinality and signed-digit bounds; 315 direct constant-derivative checks against the affine hull of the nonzero spectrum. A finite shortest-path addition-graph replay checks 511 signed digit values and 128 alternating digit lengths. The explicit family is tested at m=4,6,8,10,12,14; full independent scalar truth tables, Walsh spectra, affine support dimensions and Boolean degrees at m<=8, and component-table parity, basis images and zero-fibre checks at larger m. Observed floors 5,7,9,12,14,16 respectively against the baseline m. Capture 6b0ea35f6fb94552bc668bb5a679a9f2 before a cosmetic assertion cleanup. Finite tests are author-side regression, not proof or independent attestation.

## 6. Scope and next boundary

The lift encodes shared reverse-gate correlations in one triangular system and one affine fibre partition. The signed-digit projection is a new candidate independent obstruction beyond the degree-saturated regime, including targets where the gate count can exceed their degree. It applies to arbitrary gate slack but is quantitatively weak when 2t-r is large; it does not establish a general projected witness-coset characterization or a target-completing amortized invariant. Its explicit additive improvement is not a superpolynomial SAT demand. The next substantive obligation is to exploit the full common spectrum (signs, simultaneous affine fibres, and shared four-block recursion), rather than a maximum over individual coefficients, or prove a limitation of that route. No proof certification or novelty assertion.

Boundary: COMMON_OPERAND_FOURIER_LIFT_EXACT__SIGNED_DYADIC_FIBRE_OBSTRUCTION__EXPLICIT_LOG_GAP__GLOBAL_FIBRE_COMPATIBILITY_OPEN.
