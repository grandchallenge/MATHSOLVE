# SCC-001: Target-relative gluing and compositional transport

Status: exploratory author-derived propositions, bounded exact finite replay, no formal certification or novelty claim. Continuation of [SCC-001](https://github.com/grandchallenge/MATHSOLVE/issues/1309) and [syzygy transport](SYZYGY_TRANSPORT.md). Public [illustrated chapter](https://grandchallenge.ai/MATH-PROGRAMME/scc/).

## 1. Mark a target, rather than a gate

Let B be the Boolean function algebra over F2, V contain constants and coordinates, and F_r be the predecessor filtration. Fix a single Boolean decision function f. Let B_0 and B_1 be the two support ideals determined by f=0 and f=1. Define N_r=F_r+fF_r, and the target-relative gluing space G_r=N_r/F_r. Equivalently, N_r is the direct sum of the two independent restrictions (embedded by zero extension) of F_r to the target's zero and one regions. This follows because (1+f)a=a+fa. Thus G_r measures the gap between independent realizability in the two regions and joint realizability by a single expression in F_r.

Writing d_r=dim G_r,

$$
d_r=\dim(fF_r)+\dim((1+f)F_r)-\dim F_r.
$$

It follows that d_r is nonnegative and at most the smaller of the two restriction dimensions, hence at most the smaller support-cell size. The marked class f+F_r is zero precisely when f belongs to F_r. Unlike the whole G_r, this marked class detects target completion at r=1.

## 2. A common algebra for successive gates

The Rees algebra R=sum over r>=0 of F_r z^r is a graded subalgebra of B[z]; z is formal and represents a one-step increase of allowed degree. Put N=R+fR and G=N/R. As a graded R-module,

$$
G\cong R/J_f,\qquad J_f=\{a\in R:fa\in R\}.
$$

Indeed multiplication by f followed by quotient is surjective onto G with kernel J_f, which is an ideal since R is a subalgebra. The marked element is the image of 1, namely f+R. It is killed by z^d exactly when f has relative degree at most d. The least such d is the known degree invariant; the module's other relations need not share this small complexity.

For a legal gate g=uv put t=gz. The enlarged Rees algebra is exactly R'=R+tR by the predecessor promotion formula, with t^2=zt by idempotence. Its corresponding module numerator is N'=N+tN. These inclusions induce canonical maps G to G' for every gate and compose under any circuit history. No identification of unrelated gate-local correction cohomologies is assumed.

The base-change map G tensor_R R' to G' is onto, with kernel J'_f/(J_f R'), since G tensor_R R'=R'/(J_f R') and J'_f contains that ideal. It is precisely the new target-relative relation ideal modulo the inherited ideal. This identity does not yet give a resource bound on that kernel.

## 3. Exact death/birth sequence

In degree r, the canonical map sends a class in N_r/F_r to its class in N'_r/F'_r. Define

$$
K_r=(N_r\cap F'_r)/F_r,\qquad
C_r=N'_r/(N_r+F'_r).
$$

Then

$$
0\to K_r\to G_r\to G'_r\to C_r\to0.
$$

The kernel and cokernel follow directly from the quotient map. Also N'_r=N_r+gN_{r-1} and F'_r=F_r+gF_{r-1}, with negative grades zero. Multiplication by g therefore gives a surjection from G_{r-1} onto C_r: changing a representative by F_{r-1} changes the image by F'_r. In particular,

$$
\dim G'_r=\dim G_r-\dim K_r+\dim C_r,\qquad
\dim C_r\leq\dim G_{r-1}.
$$

These are exact target-relative transport laws that allow both disappearance and creation of gluing classes. Across arbitrary sequential gates the maps on the quotients compose by inclusion in B[z]. They require no restriction on the reuse of nonlinear intermediate primitives.

## 4. Counterexample: the target is already available

Take three independent bits a,b,c and target f=a. In the affine state, G_1 has basis the classes of ab and ac, so dimension two. Adjoin g=bc. The target is still available at zero nonlinear cost, but G'_1 has the independent classes ab,ac,abc, giving dimension three. Independence follows from the square-free monomial basis and the fact that the new degree-one space contains exactly the affine functions and bc.

More generally for target f=a among n affine input coordinates, the classes of a times square-free monomials of degree r on the other n-1 bits form a basis of G_r. Therefore dim G_r=binomial(n-1,r) and the total dimension is 2^(n-1). This is an exponentially large target-relative module for a free target. Its raw dimension is neither terminal nor monotone under gates.

## 5. Spectator law and normalization barrier

Append k independent spectator bits to the input space, available only as affine coordinates; keep f and all old gates independent of those bits. The extended filtration decomposes into the direct sum, indexed by spectator square-free monomials s, of s F_{r-deg s}. This is an exact consequence of the unique square-free expansion on the spectators and the degree filtration; the same decomposition holds for N and hence G. Consequently the extended gluing module is the direct sum of the original modules with corresponding degree shifts as a graded F2[z]-module. Writing D(X)=sum_r dim(G_r) X^r, the new polynomial is (1+X)^k D(X). The total mass divided by 2^n is thus spectator invariant.

However, G_r vanishes for r>=n, since F_n=B. Every dimension is bounded by the smaller of the two target support sizes, so the normalized mass is at most n/2. Furthermore for n=2, f=ab, the affine state has G_0 and G_1 each dimension one, and computing ab eliminates G_1. Normalized mass falls by 1/4 in one gate. Adding spectators extends this example to every n>=2 with the same normalized decrease. Thus even the sharp uniform one-gate ceiling is at least 1/4, and the ratio of total normalized mass to that ceiling is at most 2n. Neither normalization nor raw dimension yields the desired superpolynomial demand, and mass still need not vanish on completion.

## 6. Evidence and frontier

Run node research/SCC-001/target_gluing_replay.js. Exact finite replay PASS on pinned source c4991198ee27d2130ad26ffc07b4d1d5108bbfc5: 68,160 target/gate transitions; 341,184 grade checks; 7,680 compositional image checks; 80 spectator convolution checks; 1,650 increases in grade dimension; seed 90210. Exhaustive affine operand pairs and all targets for one to three inputs, 64 seeded six-step histories with four targets on four inputs, and explicit completed-target fixture (2 to 3). These tests check finite-space identities and rank accounting, not formal proof of the Rees-module theorem. Live public chapter independently rendered through restored Chromium: 8/8 plates, 97/97 expressions, zero MathJax errors/overflow on desktop light/dark and mobile.

Next: investigate minimal homogeneous relations in J_f modulo inherited relations, rather than total vector-space rank, while preserving the marked target and arbitrary reuse. In particular, compare J'_f/(J_f R') for explicit decision families under two consecutive gates; seek an independently characterized amortized bound or cheap counterfamily. The cyclicity of G itself is not a lower bound. Formal verification and literature comparison remain outstanding. No unrestricted superpolynomial lower bound or SAT transfer is claimed.
