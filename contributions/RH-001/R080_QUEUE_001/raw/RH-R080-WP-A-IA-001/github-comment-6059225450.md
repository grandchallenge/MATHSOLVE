GCL-CONTRIBUTION-RESULT/1
dispatch_id: RH-R080-WP-A-IA-001
agent_ref: INDEPENDENT-AGENT-RH-R080-A
assignment: RH-R080-WP-A
disposition: EXACT_BLOCKER
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
Under the source finite CCM hypotheses (Connes–Consani–Moscovici, arXiv:2511.22755v1, Theorem 5.10), the finite Galerkin operator $QW_\lambda^N = P_N QW_\lambda P_N$ on $E_N = \operatorname{span}\{V_n : |n| \le N\}$ admits NO theorem-grade positivity-preserving, Perron–Frobenius, Krein–Rutman, Jentzsch, Beurling–Deny, or Gantmacher–Krein oscillation mechanism forcing its simple-even ground eigenfunction $\xi$ to be pointwise nonnegative on $[0, a]$.

Specifically:
1. In the real parity-graded finite algebra $\operatorname{End}(E_N)$, simple-evenness (an isolated non-degenerate ground state in the $+1$ parity eigenspace) is mathematically independent of cone invariance for the physical pointwise nonnegativity cone $\mathcal{C}_N = \{f \in E_N : f(x) \ge 0\ \forall x \in [-a, a]\}$.
2. Even under the exact structured CCM Cauchy/parity form $\tau_{ii} = a_i$, $\tau_{ij} = \frac{b_i - b_j}{i - j}$ ($i \ne j$, $a_{-j} = a_j$, $b_{-j} = -b_j$), there exist explicit, non-degenerate finite matrices whose lowest eigenvalue is strictly simple and even, but whose physical eigenfunction changes sign on $[0, a]$.
3. The sharp Galerkin projection $P_N$ acts on $C([-a,a])$ via convolution with the Dirichlet kernel $D_N(x) = \frac{\sin((N+1/2)\pi x / a)}{\sin(\pi x / (2a))}$. Because $D_N$ possesses negative side-lobes whose negative variation diverges ($\|D_N^-\|_{L^1} \sim \frac{2}{\pi^2}\log N$), $P_N$ is not an order-preserving operator; hence Galerkin truncations destroy cone invariance on $C([-a,a])$.
4. The semilocal Weil distribution $QW_\lambda = W_{0,2} - W_{\mathbb{R}} - \sum_p W_p$ contains discrete negative delta measures $-\sum_p W_p$, rendering the continuum operator indefinite rather than positive.

Consequently, pointwise nonnegativity cannot be deduced from simple-evenness or standard positivity machinery. Route C's normal-family gate (C4) cannot rely on pointwise positivity ($\kappa_{1/2} = 1$) and must instead utilize the signed-projective condition number criterion $\sup_j \kappa_\delta(\xi_j) < \infty$ ($\delta < 1/2$).

## Derivation

1. **Decoupling of Spatial Cone and Coefficient Orthant**:
Let $E_N = \operatorname{span}\{V_n : |n| \le N\}$ on $[-a,a]$ with $V_n(x) = \frac{1}{\sqrt{2a}} e^{i n \pi x / a}$. Parity reflection $S$ acts by $V_n \leftrightarrow V_{-n}$. An even vector $\xi = \sum_{|n|\le N} c_n V_n$ has $c_{-n} = c_n$, yielding the real cosine polynomial:
$$\xi(x) = \frac{c_0}{\sqrt{2a}} + \sum_{n=1}^N \frac{2 c_n}{\sqrt{2a}} \cos\left(\frac{n\pi x}{a}\right).$$
By the Fejér–Riesz theorem, the cone of nonnegative trigonometric polynomials $\mathcal{C}_N$ is dual to the cone of positive semi-definite Toeplitz matrices, not the entrywise nonnegative orthant $\mathbb{R}_+^{2N+1}$. In particular:
- Positivity of Fourier coefficients $c_n \ge 0$ does not imply pointwise nonnegativity of $\xi(x)$ (e.g. $\cos(\pi x / a)$ has positive coefficient $c_1 > 0$ but changes sign on $[0, a]$).
- Pointwise positivity $\xi(x) \ge 0$ does not imply positivity of Fourier coefficients $c_n$.
Matrix cone invariance in the Fourier basis is therefore structurally decoupled from pointwise functional positivity.

2. **The Galerkin Dirichlet Kernel Obstruction**:
Suppose a continuum integral operator $T$ has a nonnegative kernel $k(x,y) \ge 0$ on $[-a,a] \times [-a,a]$. The Galerkin projection $T_N = P_N T P_N$ has spatial integral kernel:
$$K_N(x,y) = \int_{-a}^a \int_{-a}^a D_N(x-u) k(u,v) D_N(v-y) \, du \, dv,$$
where $D_N(t) = \frac{1}{2a} \sum_{n=-N}^N e^{i n \pi t / a} = \frac{\sin((N+1/2)\pi t / a)}{2a \sin(\pi t / (2a))}$.
The Dirichlet kernel $D_N$ oscillates and assumes negative values across $[-a,a]$. The Lebesgue constant satisfies $L_N = \int_{-a}^a |D_N(t)| dt \sim \frac{4}{\pi^2} \log N \to \infty$, and the negative lobe integral $\int_{D_N < 0} |D_N(t)| dt \to \infty$. Consequently, $P_N$ is not a positive operator in the lattice sense on $C([-a,a])$ or $L^p$. Even for an underlying positive operator, $P_N T P_N$ does not leave the cone of pointwise nonnegative functions invariant.

3. **Inapplicability of Krein–Rutman / Jentzsch / Perron–Frobenius**:
The Krein–Rutman theorem requires an operator (or resolvent / semigroup) leaving a reproducing, solid cone invariant with non-zero spectral radius.
- In $C_{\mathrm{even}}([-a,a])$ with cone $K_+ = \{f \ge 0\}$, $QW_\lambda^N$ does not preserve $K_+$ due to the Gibbs/Dirichlet oscillations and the negative prime terms $-\sum_p W_p$.
- In the coefficient basis, the matrix $\tau$ has indefinite off-diagonal entries $\tau_{ij} = \frac{b_i - b_j}{i - j}$ whose signs alternate with prime distributions and indices, precluding entrywise nonnegativity or $M$-matrix structure.

4. **Inapplicability of Gantmacher–Krein Oscillation Theory**:
An oscillation kernel requires strict total positivity ($K\begin{pmatrix} x_1 \dots x_k \\ y_1 \dots y_k \end{pmatrix} > 0$ for ordered tuples). A kernel commuting with reflection $S(x) = -x$ satisfies $K(-x, -y) = K(x,y)$. On a symmetric domain $[-a,a]$, non-trivial parity invariance prevents strict sign-consistency of all minors across the anti-diagonal. Furthermore, $K_N(x,y)$ has oscillatory nodal lines in $[-a,a] \times [-a,a]$.

5. **Exact Replayable Structured CCM Counter-Model**:
To demonstrate that the exact CCM structured format $\tau_{ii} = a_i, \tau_{ij} = \frac{b_i - b_j}{i - j}$ ($a_{-j} = a_j, b_{-j} = -b_j$) admits a simple, even ground state that changes sign, consider $N = 1$ on $[-\pi, \pi]$ ($a = \pi$) with indices $\{-1, 0, 1\}$:
$b_0 = 0$, $b_1 = -0.2$, $b_{-1} = 0.2$; $a_0 = 5.0$, $a_1 = a_{-1} = -2.5$.
Then:
- $\tau_{-1, 1} = \frac{b_{-1} - b_1}{-1 - 1} = \frac{0.4}{-2} = -0.2 = b_1$.
- $\tau_{-1, 0} = \frac{b_{-1} - b_0}{-1 - 0} = \frac{0.2}{-1} = -0.2 = b_1$.
- $\tau_{0, 1} = \frac{b_0 - b_1}{0 - 1} = \frac{0.2}{-1} = -0.2 = b_1$.
The resulting symmetric matrix is:
$$\tau = \begin{pmatrix} -2.5 & -0.2 & -0.2 \\ -0.2 & 5.0 & -0.2 \\ -0.2 & -0.2 & -2.5 \end{pmatrix}.$$
- Eigenvalues: $\lambda_0 \approx -2.71038$ (even), $\lambda_1 = -2.30000$ (odd), $\lambda_2 \approx 5.01038$ (even).
- Ground state: $\lambda_0 \approx -2.71038$ is non-degenerate and strictly separated by gap $\Delta \approx 0.41038$.
- Ground eigenvector: $c \approx [-0.70663, -0.03666, -0.70663]^T$, strictly even ($c_{-1} = c_1$).
- Physical function: $f(x) \propto c_0 + 2 c_1 \cos(x)$.
  At $x = 0$: $f(0) \approx -0.03666 + 2(-0.70663) = -1.44992 < 0$.
  At $x = \pi$: $f(\pi) \approx -0.03666 - 2(-0.70663) = +1.37660 > 0$.
The eigenfunction changes sign on $[0, \pi]$. Simple-evenness holds, but pointwise nonnegativity fails.

## Assumptions beyond bootstrap
NONE. Relies exclusively on the protected packet (arXiv:2511.22755v1 Theorem 5.10 structure, finite Galerkin projections, and parity symmetry).

## Verification / falsification hooks
Replay the structured CCM counter-model in Python:
```python
import numpy as np

# Exact CCM structured Cauchy form: a_{-j}=a_j, b_{-j}=-b_j
tau = np.array([[-2.5, -0.2, -0.2], [-0.2, 5.0, -0.2], [-0.2, -0.2, -2.5]])
vals, vecs = np.linalg.eigh(tau)
assert vals[0] < vals[1]  # Simple ground state
ground = vecs[:, 0]
assert np.isclose(ground[0], ground[2])  # Strictly even
# Physical eigenfunction f(x) = ground[1] + 2*ground[0]*cos(x) on [0, pi]
f_0 = ground[1] + 2 * ground[0] * np.cos(0)
f_pi = ground[1] + 2 * ground[0] * np.cos(np.pi)
assert f_0 * f_pi < 0  # Sign change on [0, pi]
```

## Claim boundary
This is an exact finite operator-theoretic obstruction proving that standard positivity machinery cannot establish pointwise nonnegativity of the CCM ground eigenfunction from simple-evenness. It does not assert that the true CCM eigenfunction for large $N$ must change sign, nor does it invalidate Route C; rather, it proves that Route C must not depend on pointwise positivity ($\kappa_{1/2}=1$) and validates the signed-projective condition number reduction ($\kappa_\delta < \infty$). No repository mutation, adjudication, or RH claim is made.

## Next residual
The remaining Route C normality obligation (C4) reduces to proving that the signed-projective condition numbers $\sup_{(\lambda, N) \in \mathcal{A}} \kappa_\delta(\xi_{\lambda, N}) < \infty$ remain bounded for each $\delta < 1/2$ along an admitted cofinal family, or verifying uniform relative approximation against a sign-definite reference candidate via the R080 error transfer theorem.
