# SCC-001: affine-quadratic spectral branches and joint parity geometry

Status: exploratory author proof and exact finite regression, not independently adjudicated, Lean-certified or novelty-certified. Continues FOURIER_FIBRE_CAPACITY.md at protected revision 2fdc062bcc88837887b833675a04621ef6a39c5a. One Boolean output, unrestricted intermediate reuse. Public chapter: https://grandchallenge.ai/MATH-PROGRAMME/scc/.

## 1. Branch decomposition

Use the common triangular operand lift H on 2t independent formal bits and the injective linear operand map L on the r-dimensional reduced input, as in the predecessor. Affine output terms only shift frequencies and change global sign. In reverse Walsh recursion fix an entire active-mask pattern A subset of the t gates. For this fixed pattern, each mutable mask is affine in the later frequencies: its updates are linear combinations of p_j,q_j for the fixed active gates. The requirements that each current mask bit have the prescribed value, and that inactive gates have p_j=q_j=0, are affine equations. Consequently the lifted frequencies realizing the pattern form an affine subspace S_A (possibly empty); the sign is a quadratic polynomial Q_A on that space, from sum of p_j q_j and linear constant-offset contributions. The disjoint branches give the exact integer decomposition
$$
2^t W_f(a)=\sum_{A\subseteq[t]} 2^{t-|A|}
\sum_{b\in S_A:L^T b=a}(-1)^{Q_A(b)}.
$$

Each branch projected through L^T is either zero or a constant signed power of two on an affine support, with quadratic sign on that support. Proof: choose an affine section of S_A onto its image and let U be the kernel direction of the projection. Write the phase as Q(b(a))+q(u)+B(b(a),u), with q(0)=0 and B the polar form. On the radical of B restricted to U, q is linear. Summing over that radical cancels unless the affine-linear compatibility equations on a hold. On their affine solution set, choose a nondegenerate complement to the radical. Completing the square by its unique linear-polar shift (affine in a) leaves a constant Gauss sum of absolute value 2^(d/2) for complement dimension d; this follows by squaring the sum and using character orthogonality. Multiply by the radical size. The resulting phase is quadratic in a. Hence each nonzero contribution has form ±2^e on an affine set, e>=t-|A|, sign given by a quadratic phase. This argument uses the standard quadratic Walsh/Gauss-sum mechanism (see Carlet, Boolean Functions for Cryptography and Coding Theory, https://www.math.univ-paris13.fr/~carlet/book-fcts-Bool-vect-crypt-codes.pdf); the common-gate branch application is derived here. No novelty claim.

## 2. Joint parity constraint

Let gamma be the minimal Walsh granularity, and s=t-gamma>=0. Define P_f(a)=(2^gamma W_f(a)) mod 2, and let C_aff(P) denote the least number of affine-subspace indicators whose XOR equals P. Empty indicators may be omitted. This measure is defined directly from the target spectrum, not its circuit. Shifts of frequencies and adding/removing spectators preserve the tight affine-support property; the argument uses the reduced domain.

At slack zero, only the all-active branch can have odd amplitude; all other branches have an explicit factor of two. Its odd support is affine and nonempty because gamma=t. Therefore C_aff(P_f)=1.

At slack one, all contributions other than the all-active branch are even, and the total is even, so the all-active branch is also everywhere even. Dividing by two, each branch of amplitude valuation exactly one contributes its affine support indicator modulo two. At most t+1 patterns have at most one inactive gate. Thus C_aff(P_f)<=t+1. This uses the whole parity pattern, not a maximum of coefficient magnitudes.

For arbitrary slack, put N=sum_{j=0}^s binomial(t,j) and B=(s+1)N. Discard all branches with amplitude valuation >s modulo 2^(s+1); at most N remain. For each remaining signed contribution of valuation e, its binary residue has bit e equal to the affine support indicator and each higher bit equal to that indicator times its quadratic negative-sign bit. Extend the quadratic on the affine support to a quadratic in r ambient coordinates by extending affine coordinate forms. Each bit is therefore an XOR of at most L0=1+r+binomial(r,2) affine-subspace indicators: monomials of degree <=2 times the support are affine intersections.

The bit s of a sum of binary residues is the coefficient of X^(2^s) in the product of (1+d X^(2^j)) over all bits d at positions j. Indeed at any frequency this product equals (1+X)^sum in F2[X]; the binary expansion of the exponent gives the bit by Frobenius (equivalently Lucas parity). Reduction modulo 2^(s+1) does not change that bit. Every term uses at most 2^s bit indicators; products of affine indicators are affine indicators. Expanding yields
$$
C_{\rm aff}(P_f)\le \sum_{k=1}^{2^s}\binom{B}{k}L_0^k
\le (1+B L_0)^{2^s}.
$$
Binomial coefficients outside 0..B are zero. This is polynomial in t,r for fixed s. It is a budget-dependent joint obstruction, not a universal amortized potential. The displayed coarse bound becomes vacuous compared with singleton indicators once 2^s>=r (for r>=1). No superpolynomial lower bound follows.

## 3. Explicit separator from preceding scalar tests

For m>=3 define pi on m-bit y. For the four values with all coordinates y_3,...,y_m zero, assign the four singleton values 0,e_1,e_2,e_3 in lexicographic order of the first two bits. For every other y, partition by its first nonzero bit j>=3, assigning e_1+e_2 if j=3 and e_j if j>=4. All nonempty fibres of pi are affine sets. Its image contains zero and every coordinate basis vector. Let f(x,y)=x dot pi(y) on 2m bits.

The normalized Walsh coefficient at (u,v) is 2^-m times sum of (-1)^(v dot y) over pi(y)=u. Every nonzero sum is a signed power of two because the fibre is affine. The four singleton fibres imply gamma=m, and the predecessor signed-digit demand D equals one. Nonlinear dimension is 2m: a constant derivative under (a,b) forces pi(y+b)=pi(y) by varying x, and a singleton fibre forces b=0. The remaining derivative is constant only if a=0 since the image contains zero and every basis vector. The degree is at most m+1 (each component of pi uses only m variables), so the degree bound is at most m. All three predecessor scalar tests and the signed-digit bound thus give at most m, with granularity and dimension attaining m.

However the odd numerator support is exactly
$$
\{0,e_1,e_2,e_3\}\times\mathbb F_2^m,
$$
since the remaining fibres have even size. This is not affine, as it contains zero, e_1 and e_2 in the first factor but not e_1+e_2. The new joint test excludes t=m, proving t>=m+1. This is a strict separation from the previous scalar spectral bound, not a claim of optimal circuit size or improvement over every literature bound. The construction itself has a polynomial circuit via tests of the first nonzero bit and the two singleton bits. It is not a SAT lower bound.

## 4. Evidence and frontier

Run python3 research/SCC-001/spectral_parity_replay.py. Exact integer Walsh transforms independently check the common lift, affine branch supports, uniform dyadic amplitudes and degree-at-most-two signs; check projected fibre sums and bit extraction for all sampled slacks. Seed 20261128: 100 circuits (budgets 1..5), 309 nonempty lifted branches (some have zero projection), 5070 target frequencies, including 23 zero-slack and 24 one-slack cases. Six full affine-fibre fixtures for m=3..8 verify granularity, signed-digit ceiling, nonaffine parity support and full affine hull of nonzero frequencies. Author-side finite evidence only; no independent certification. No claim of exhaustive novelty search.

The next target is a stronger simultaneous constraint on the projected affine-quadratic branches that preserves their common triangular dependency coefficients. The coarse affine-XOR bound forgets those correlations and rapidly loses power at larger slack. A possible next test is the entire sequence of residue planes together, rather than only its first nonzero plane. Any proposed amortized measure must resist arbitrary reuse and have superpolynomial range on an explicit target. The present result is a budget-relative spectral obstruction only.

Boundary: AFFINE_QUADRATIC_BRANCH_DECOMPOSITION_EXACT__JOINT_PARITY_GEOMETRY__SCALAR_SEPARATOR__LARGE_SLACK_OPEN.
