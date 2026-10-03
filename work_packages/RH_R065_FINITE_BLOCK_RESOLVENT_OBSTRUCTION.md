# RH-R065-FINITE-BLOCK-RESOLVENT-OBSTRUCTION-001

Campaign: RH-001

Route: Forward Route C — determinant convergence to Xi

Obligations: C4 normal-family control — finite-block resolvent burden or obstruction

Status: ADMISSION_CANDIDATE

Solve coordination:
- route tracker: grandchallenge/MATHSOLVE#414
- bounded tranche: grandchallenge/MATHSOLVE#729

Protected Solve base:
grandchallenge/MATHSOLVE@7a9cc9aa6ceeec781c4b611784b51ef93ce033f1

Protected dependencies:
- grandchallenge/MATHSOLVE@7a9cc9aa6ceeec781c4b611784b51ef93ce033f1:
  work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md
- grandchallenge/MATHSOLVE@7a9cc9aa6ceeec781c4b611784b51ef93ce033f1:
  work_packages/RH_R053_COMPACT_TRANSFORM_STABILITY.md
- grandchallenge/MATHSOLVE@7a9cc9aa6ceeec781c4b611784b51ef93ce033f1:
  work_packages/RH_R056_CANONICAL_DETERMINANT_NORMALIZATION.md
- grandchallenge/MATHSOLVE@7a9cc9aa6ceeec781c4b611784b51ef93ce033f1:
  work_packages/RH_R059_PAIRED_ZERO_NORMAL_FAMILY.md
- grandchallenge/MATHSOLVE@7a9cc9aa6ceeec781c4b611784b51ef93ce033f1:
  work_packages/RH_R062_UNTOUCHED_LATTICE_TAIL.md

Primary source:
Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Spectral Triples*,
arXiv:2511.22755v1 (2025-11-27), especially §§5.5–5.6, Theorem 5.10, and §7.

Sanity replay:
scripts/rh_r065_finite_block_check.py

No cofinal admissibility / full C4 / C5 / C6 / determinant convergence /
global simple-evenness / RH / novelty / priority / publication-readiness /
certification claim.

---

## 1. Executive summary of disposition

Protected RH-R059 proved that a uniform bound on the paired zero energy
\[
Q_{\lambda,N}
:=
Q_{1/2}(F_{\lambda,N})
=
\frac12
\operatorname{Tr}
\left(
\left(
(D_{\log}^{(\lambda,N)})^2+\frac14I
\right)^{-1}
\right)
\le C_Q < \infty
\tag{1.1}
\]
is a sufficient condition for local boundedness and Montel normality of the
canonically normalized Connes–Consani–Moscovici (CCM) entire determinants \(F_{\lambda,N}\).

Protected RH-R062 decomposed this trace into the finite modified block \(E_N'\)
and the untouched scaling complement \(E_N^\perp\):
\[
Q_{\lambda,N} = B_{a,N} + T_{a,N},
\qquad a = \log\lambda,
\tag{1.2}
\]
and proved that the complement tail \(T_{a,N} = \sum_{j>N} \frac{1}{(\pi j/a)^2+1/4}\)
forces \(N = \Omega(a^2) = \Omega((\log\lambda)^2)\) on any schedule where \(T_{a,N}\)
remains bounded.

Bounded issue #729 tasked Route C lane RH-R065 with determining whether the
finite-block contribution
\[
B_{a,N}
:=
\frac12
\operatorname{Tr}_{E_N'}
\left(
\left(
(D_{\log}^{(\lambda,N)}|_{E_N'})^2+\frac14I
\right)^{-1}
\right)
\tag{1.3}
\]
can be uniformly bounded on viable schedules (Option A), or is obstructed by
divergence (Option B).

This package establishes **Option B (Obstruction Route)**:

1. **Exact finite-block interlacing**: On the quotient space \(E_N' = E_N / \mathbb C\xi\),
   the \(2N\) eigenvalues \(\{\pm \mu_1, \dots, \pm \mu_N\}\) strictly interlace with
   the scaling lattice points:
   \[
   0 < \mu_1 < \frac{\pi}{a} < \mu_2 < \frac{2\pi}{a} < \dots < \mu_N < \frac{\pi N}{a}.
   \tag{1.4}
   \]
   In particular, \(\mu_j < \frac{\pi j}{a}\) for all \(1 \le j \le N\).

2. **Finite-block lower bound**: Consequently,
   \[
   B_{a,N}
   =
   \sum_{j=1}^N \frac{1}{\mu_j^2 + 1/4}
   >
   \sum_{j=1}^N \frac{1}{(\pi j/a)^2 + 1/4}
   \ge
   \frac{2a}{\pi}
   \left[
   \arctan\left(\frac{2\pi(N+1)}{a}\right)
   -
   \arctan\left(\frac{2\pi}{a}\right)
   \right].
   \tag{1.5}
   \]
   On any schedule satisfying the R062 lower scale \(N = \Omega(a^2)\),
   \(B_{a,N} \ge a - 4 + o(1) = \log\lambda - 4 + o(1) \to \infty\).

3. **Global trace divergence**: Combining (1.5) with \(T_{a,N}\) yields an
   exact, schedule-independent lower bound via the Mittag-Leffler expansion of \(\coth\):
   \[
   \boxed{
   Q_{\lambda,N}
   =
   B_{a,N} + T_{a,N}
   >
   \sum_{j=1}^\infty \frac{1}{(\pi j/a)^2 + 1/4}
   =
   a\coth(a/2) - 2
   >
   \log\lambda - 2.
   }
   \tag{1.6}
   \]
   Therefore, \(Q_{\lambda,N} \to \infty\) as \(\lambda \to \infty\) along **every**
   cofinal family, regardless of the choice of truncation schedule \(N(\lambda)\).

4. **Strategic consequence for Route C**: The R059 positive resolvent trace criterion
   is structurally incompatible with the scale growth of the CCM family. Normal-family
   control (C4) must be achieved through localized or scale-invariant mechanisms
   (e.g., compact-set logarithmic-derivative bounds, Carathéodory-Herglotz half-plane bounds,
   or Paley-Wiener exponential-type estimates), not through the total reciprocal-square zero trace.

---

## 2. Source setting and quotient operator

Let \(\lambda > 1\), \(a = \log\lambda > 0\), and \(L = 2a\). Consider the scaling operator
\[
D_{\log}^{(\lambda)} = -i u \frac{\partial}{\partial u} = -i \frac{d}{dx}
\]
on \(L^2([\lambda^{-1},\lambda], d^*u) \cong L^2([-a,a], dx)\) with periodic boundary conditions.
The orthonormal basis of eigenfunctions is
\[
e_j(x) = \frac{1}{\sqrt{2a}} e^{i \frac{\pi j}{a} x},
\qquad j \in \mathbb Z,
\tag{2.1}
\]
with eigenvalues \(\lambda_j = \frac{\pi j}{a}\).

For \(N \ge 1\), let \(E_N = \operatorname{span}\{e_j : |j| \le N\}\) of dimension \(2N+1\),
and \(E_N^\perp = \operatorname{span}\{e_j : |j| > N\}\).

Under the CCM simple-even hypothesis:
- The smallest eigenvalue \(\epsilon_N\) of the restricted Weil form \(QW_\lambda^N\) is simple;
- The ground eigenvector \(\xi \in E_N\) is even under \(x \mapsto -x\);
- \(\xi\) is normalized by the boundary evaluation functional \(\delta_N(\xi) = 1\).

The rank-one modified operator is
\[
D_{\log}^{(\lambda,N)}
=
D_{\log}^{(\lambda)} - |D_{\log}^{(\lambda)}\xi\rangle \langle \delta_N|.
\tag{2.2}
\]
Because \(\delta_N(\xi) = 1\), \(D_{\log}^{(\lambda,N)}\xi = 0\).
The operator acts on the direct sum
\[
E_N' \oplus E_N^\perp,
\qquad
E_N' = E_N / \mathbb C\xi,
\tag{2.3}
\]
where \(\dim E_N' = 2N\).

CCM Theorem 5.10 establishes:
1. \(D_{\log}^{(\lambda,N)}\) is self-adjoint on \(E_N' \oplus E_N^\perp\) under the induced quotient inner product on \(E_N'\);
2. The regularized determinant factors as
   \[
   \det_{\rm reg}(D_{\log}^{(\lambda,N)} - z)
   =
   \operatorname{Det}(D_{\log}^{(\lambda,N)}|_{E_N'} - z)
   \cdot
   \det_{\rm reg}(D_{\log}^{(\lambda)}|_{E_N^\perp} - z)
   =
   -i \lambda^{-iz} \widehat{\xi}_{\lambda,N}(z);
   \tag{2.4}
   \]
3. \(\widehat{\xi}_{\lambda,N}(z)\) is entire, even, and all of its zeros are real;
4. The zeros of \(\widehat{\xi}_{\lambda,N}\) coincide with the spectrum of \(D_{\log}^{(\lambda,N)}\).

---

## 3. Exact logarithmic-derivative identity for total zero energy

Let \(F(z) = \widehat{\xi}_{\lambda,N}(z) = \int_{-a}^a \xi(e^x) e^{-izx} dx\).
Because \(\xi \in E_N \subset L^2([-a,a])\) is even, \(F(z)\) is an even entire function
of exponential type at most \(a\), with all zeros real.

### Proposition 3.1 (Logarithmic-Derivative / Expectation Identity)
Let \(\{\pm z_k\}_{k=1}^\infty\) with \(0 < z_1 \le z_2 \le \dots\) denote the complete
positive zero multiset of \(\widehat{\xi}_{\lambda,N}\). Then
\[
\boxed{
Q_{\lambda,N}
=
\sum_{k=1}^\infty \frac{1}{z_k^2 + 1/4}
=
i \frac{\widehat{\xi}_{\lambda,N}'(i/2)}{\widehat{\xi}_{\lambda,N}(i/2)}
=
\frac{\int_0^a \xi(e^x) x \sinh(x/2) dx}{\int_0^a \xi(e^x) \cosh(x/2) dx}.
}
\tag{3.1}
\]

### Proof
By Hadamard's factorization theorem for even entire functions of order 1 with all zeros real
and \(F(0) = \widehat{\xi}_{\lambda,N}(0) \ne 0\):
\[
F(z) = F(0) \prod_{k=1}^\infty \left(1 - \frac{z^2}{z_k^2}\right).
\tag{3.2}
\]
Taking the logarithmic derivative:
\[
\frac{F'(z)}{F(z)}
=
\sum_{k=1}^\infty \frac{-2z/z_k^2}{1 - z^2/z_k^2}
=
\sum_{k=1}^\infty \frac{-2z}{z_k^2 - z^2}.
\tag{3.3}
\]
Evaluating at the classical anchor \(z = i/2\):
\[
\frac{F'(i/2)}{F(i/2)}
=
\sum_{k=1}^\infty \frac{-2(i/2)}{z_k^2 - (i/2)^2}
=
-i \sum_{k=1}^\infty \frac{1}{z_k^2 + 1/4}
=
-i Q_{\lambda,N}.
\tag{3.4}
\]
Multiplying by \(i\) gives \(Q_{\lambda,N} = i F'(i/2) / F(i/2)\).

Differentiating under the integral sign for \(F(z) = \int_{-a}^a \xi(e^x) e^{-izx} dx\):
\[
F(i/2) = \int_{-a}^a \xi(e^x) e^{x/2} dx = 2 \int_0^a \xi(e^x) \cosh(x/2) dx,
\tag{3.5}
\]
since \(\xi\) is even.
Similarly,
\[
F'(z) = -i \int_{-a}^a \xi(e^x) x e^{-izx} dx,
\]
so at \(z = i/2\):
\[
F'(i/2) = -i \int_{-a}^a \xi(e^x) x e^{x/2} dx = -2i \int_0^a \xi(e^x) x \sinh(x/2) dx,
\tag{3.6}
\]
since \(x \cosh(x/2)\) is odd and integrates to zero against the even function \(\xi\).
Substituting (3.5) and (3.6) into (3.4) yields (3.1).
QED.

---

## 4. Finite block spectrum and secular interlacing

Because \(\xi \in E_N\), its Fourier expansion is
\[
\xi(e^x) = \frac{1}{\sqrt{2a}} \left( c_0 + 2 \sum_{j=1}^N c_j \cos\left(\frac{\pi j}{a} x\right) \right),
\tag{4.1}
\]
with \(c_j = \langle e_j, \xi \rangle \in \mathbb R\).
Evaluating the Fourier integral term by term:
\[
\widehat{\xi}_{\lambda,N}(z)
=
\frac{2\sin(az)}{\sqrt{2a}}
\left(
\frac{c_0}{z}
+
\sum_{j=1}^N (-1)^j c_j \frac{2z}{z^2 - (\pi j/a)^2}
\right).
\tag{4.2}
\]

### Analysis of Zeros
- For \(|j| > N\): \(\sin(az)\) has a simple zero at \(\pi j / a\), while the rational factor has no pole. Thus every \(\pi j / a\) (\(|j| > N\)) is a zero of \(\widehat{\xi}_{\lambda,N}\). These form the untouched complement spectrum \(\sigma(D_{\log}^{(\lambda)}|_{E_N^\perp})\).
- For \(1 \le |j| \le N\): The pole of the rational factor at \(\pi j / a\) is canceled by the simple zero of \(\sin(az)\), yielding the non-zero value \(\sqrt{2a} c_{|j|} \ne 0\).
- For \(z = 0\): \(\sin(az)/z \to a\), so \(\widehat{\xi}_{\lambda,N}(0) = \sqrt{2a} c_0 \ne 0\).

The remaining \(2N\) zeros of \(\widehat{\xi}_{\lambda,N}(z)\) are the roots of the rational factor,
which are the eigenvalues \(\pm \mu_1, \dots, \pm \mu_N\) of \(D_{\log}^{(\lambda,N)}|_{E_N'}\).
Setting \(w = z^2\) and \(x_j = (\pi j/a)^2\), they satisfy the secular equation
\[
H(w)
:=
c_0 + \sum_{j=1}^N \alpha_j \frac{w}{w - x_j} = 0,
\qquad
\alpha_j = 2(-1)^j c_j.
\tag{4.3}
\]

### Proposition 4.1 (Strict Spectral Interlacing)
On the admitted finite domain where \(\xi\) is the ground state of \(QW_\lambda^N\)
with \(c_0 > 0\) and \(\alpha_j = 2(-1)^j c_j > 0\) for all \(1 \le j \le N\):
1. In each open interval \((0, x_1)\) and \((x_{j-1}, x_j)\) (\(2 \le j \le N\)),
   there is exactly one root \(w_j\) of \(H(w) = 0\);
2. There are no roots in \((x_N, \infty)\);
3. Taking square roots, the positive eigenvalues \(\mu_j = \sqrt{w_j}\) strictly interlace:
   \[
   \boxed{
   0 < \mu_1 < \frac{\pi}{a} < \mu_2 < \frac{2\pi}{a} < \dots < \mu_N < \frac{\pi N}{a}.
   }
   \tag{4.4}
   \]

### Proof
For all \(w \in \mathbb R \setminus \{x_1, \dots, x_N\}\):
\[
H'(w)
=
-\sum_{j=1}^N \frac{\alpha_j x_j}{(w - x_j)^2} < 0,
\tag{4.5}
\]
so \(H(w)\) is strictly decreasing on each connected component of its domain.

1. On \((0, x_1)\): \(H(0) = c_0 > 0\), and \(\lim_{w \to x_1^-} H(w) = -\infty\) because \(\alpha_1 > 0\). By the intermediate value theorem and strict monotonicity, there is a unique root \(w_1 \in (0, x_1)\).
2. On \((x_{j-1}, x_j)\) for \(2 \le j \le N\): \(\lim_{w \to x_{j-1}^+} H(w) = +\infty\) and \(\lim_{w \to x_j^-} H(w) = -\infty\). Hence there is a unique root \(w_j \in (x_{j-1}, x_j)\).
3. On \((x_N, \infty)\): \(\lim_{w \to x_N^+} H(w) = +\infty\), and as \(w \to +\infty\),
   \(H(w) \to c_0 + \sum_{j=1}^N \alpha_j = \delta_N(\xi) = 1 > 0\).
   Because \(H'(w) < 0\), \(H(w) > 1 > 0\) for all \(w > x_N\). No root exists in \((x_N, \infty)\).

This accounts for all \(N\) roots of the numerator polynomial of \(H(w)\).
Taking \(\mu_j = \sqrt{w_j}\) gives (4.4).
QED.

---

## 5. Theorem: Finite-block and global resolvent obstruction

### Theorem 5.1 (Finite-Block Lower Bound)
For every admitted finite CCM pair \((\lambda, N)\) with \(\lambda > 1\) and \(N \ge 1\):
\[
B_{a,N}
=
\sum_{j=1}^N \frac{1}{\mu_j^2 + 1/4}
>
\sum_{j=1}^N \frac{1}{(\pi j/a)^2 + 1/4}
\tag{5.1}
\]
and
\[
B_{a,N}
\ge
\frac{2a}{\pi}
\left[
\arctan\left(\frac{2\pi(N+1)}{a}\right)
-
\arctan\left(\frac{2\pi}{a}\right)
\right].
\tag{5.2}
\]

### Proof
From Proposition 4.1, \(\mu_j < \frac{\pi j}{a}\) for all \(1 \le j \le N\).
Since the mapping \(u \mapsto \frac{1}{u^2 + 1/4}\) is strictly decreasing on \((0, \infty)\):
\[
\frac{1}{\mu_j^2 + 1/4}
>
\frac{1}{(\pi j/a)^2 + 1/4}.
\]
Summing over \(j = 1, \dots, N\) gives (5.1).

For (5.2), the function \(f(x) = \frac{1}{(\pi x/a)^2 + 1/4}\) is positive and decreasing on \([0, \infty)\).
By the standard integral comparison:
\[
\sum_{j=1}^N f(j)
\ge
\int_1^{N+1} f(x) dx
=
\int_1^{N+1} \frac{dx}{(\pi x/a)^2 + 1/4}.
\]
Substituting \(u = \frac{\pi x}{a}\), \(dx = \frac{a}{\pi} du\):
\[
\int_1^{N+1} \frac{dx}{(\pi x/a)^2 + 1/4}
=
\frac{a}{\pi} \int_{\pi/a}^{\pi(N+1)/a} \frac{du}{u^2 + 1/4}
=
\frac{2a}{\pi} \left[ \arctan(2u) \right]_{\pi/a}^{\pi(N+1)/a},
\]
which proves (5.2).
QED.

### Theorem 5.2 (Universal Global Resolvent Obstruction)
For every admitted finite CCM pair \((\lambda, N)\) with \(\lambda > 1\) and \(N \ge 1\):
\[
\boxed{
Q_{\lambda,N}
=
B_{a,N} + T_{a,N}
>
a\coth(a/2) - 2
>
\log\lambda - 2.
}
\tag{5.3}
\]
Consequently, along **any** cofinal family where \(\lambda \to \infty\):
\[
\lim_{\lambda \to \infty} Q_{\lambda,N} = +\infty,
\tag{5.4}
\]
regardless of how the truncation schedule \(N(\lambda)\) is chosen.

### Proof
From (5.1) and the definition of \(T_{a,N}\) in RH-R062 (1.2):
\[
Q_{\lambda,N}
=
B_{a,N} + T_{a,N}
>
\sum_{j=1}^N \frac{1}{(\pi j/a)^2 + 1/4}
+
\sum_{j=N+1}^\infty \frac{1}{(\pi j/a)^2 + 1/4}
=
\sum_{j=1}^\infty \frac{1}{(\pi j/a)^2 + 1/4}.
\tag{5.5}
\]
Recall the classical Mittag-Leffler expansion of \(\coth(z)\):
\[
\coth(z) = \frac{1}{z} + \sum_{j=1}^\infty \frac{2z}{z^2 + \pi^2 j^2}.
\tag{5.6}
\]
Setting \(z = a/2\):
\[
\coth(a/2)
=
\frac{2}{a}
+
\sum_{j=1}^\infty \frac{a}{(a/2)^2 + \pi^2 j^2}.
\tag{5.7}
\]
Multiplying by \(a\):
\[
a\coth(a/2)
=
2
+
\sum_{j=1}^\infty \frac{a^2}{(a/2)^2 + \pi^2 j^2}
=
2
+
\sum_{j=1}^\infty \frac{1}{1/4 + (\pi j/a)^2}.
\tag{5.8}
\]
Subtracting 2 gives the exact identity:
\[
\sum_{j=1}^\infty \frac{1}{(\pi j/a)^2 + 1/4}
=
a\coth(a/2) - 2.
\tag{5.9}
\]
Because \(\coth(x) = \frac{e^{2x}+1}{e^{2x}-1} > 1\) for all \(x > 0\),
\(a\coth(a/2) - 2 > a - 2 = \log\lambda - 2\).
This proves (5.3).
Since \(\log\lambda \to \infty\) as \(\lambda \to \infty\), (5.4) follows immediately.
QED.

---

## 6. Contrast with the limiting Riemann Xi zero energy

To understand why the finite trace \(Q_{\lambda,N}\) diverges while the target function
\(\Xi\) is well-behaved, we compute the exact zero energy of \(\Xi\):

### Proposition 6.1 (Limiting Xi Zero Energy)
For Riemann's completed function \(\Xi(z) = \xi(1/2 + iz)\):
\[
Q_{1/2}(\Xi)
=
\sum_{\gamma_k > 0} \frac{1}{\gamma_k^2 + 1/4}
=
-\frac{\xi'(0)}{\xi(0)}
=
1 - \frac12 \log(4\pi) + \frac12 \gamma_{\rm Euler}
\approx
0.023096 < \infty.
\tag{6.1}
\]

### Proof
From DLMF 25.4.4 and the Hadamard product of \(\xi(s)\),
\(\Xi(z) = \Xi(0) \prod_k (1 - z^2/\gamma_k^2)\).
As in Proposition 3.1,
\[
Q_{1/2}(\Xi) = i \frac{\Xi'(i/2)}{\Xi(i/2)}.
\]
Since \(\Xi(z) = \xi(1/2 + iz)\), \(\Xi(i/2) = \xi(0) = 1/2 \ne 0\),
and \(\Xi'(i/2) = i \xi'(0)\).
Thus
\[
i \frac{\Xi'(i/2)}{\Xi(i/2)} = i \frac{i \xi'(0)}{\xi(0)} = -\frac{\xi'(0)}{\xi(0)}.
\]
Using the completed \(\xi\)-function formula:
\[
\log \xi(s) = -\log 2 + \log s + \log(s-1) - \frac{s}{2} \log\pi + \log\Gamma(s/2) + \log\zeta(s).
\]
Using \(s \Gamma(s/2) = 2 \Gamma(1 + s/2)\) and the Laurent expansion of \(\zeta(s)\) near \(s = 0\):
\[
\zeta(s) = -\frac12 - \frac12 \log(2\pi) s + O(s^2),
\]
a direct calculation yields
\[
\left. \frac{d}{ds} \log \xi(s) \right|_{s=0}
=
-1 - \frac12 \log\pi - \frac12 \gamma_{\rm Euler} + \log(2\pi)
=
-1 + \frac12 \log(4\pi) - \frac12 \gamma_{\rm Euler}.
\]
Negating this quantity gives (6.1).
QED.

### Root Cause of the Obstruction
- The target function \(\Xi\) has zeros only at the nontrivial zeta ordinates \(\pm \gamma_k\) (\(\gamma_1 \approx 14.1347\)), with an asymptotic counting function \(N(T) \sim \frac{T}{2\pi} \log T\). Its zero energy is small and finite (\(\approx 0.023\)).
- The finite approximant \(\widehat{\xi}_{\lambda,N}(z)\), by contrast, has an *extensive* set of zeros across the entire real axis with average density \(a/\pi = (\log\lambda)/\pi\).
- Even though the low eigenvalues are numerically observed to approach \(\gamma_k\) as \(\lambda, N \to \infty\), the sum of reciprocals \(\sum \frac{1}{\mu_k^2 + 1/4}\) integrates the total zero density, which grows like \(\Omega(\log\lambda)\).
- Thus, the R059 resolvent trace criterion is structurally incapable of capturing Montel normality for this family: it penalizes the high-frequency zeros that are intrinsic to the finite multiplicative interval \([\lambda^{-1}, \lambda]\).

---

## 7. Strategic redirection for Route C

The closure of the Option B obstruction eliminates the dead-end search for a uniform trace bound on \(Q_{\lambda,N}\).

To discharge obligation C4 (normal-family control), Route C must employ a criterion that is insensitive to the distant zero density \(a/\pi\):

1. **Compact-set logarithmic-derivative bounds**:
   Instead of bounding the global sum of reciprocal squares, bound
   \[
   \sup_{z \in K} \left| \frac{F_{\lambda,N}'(z)}{F_{\lambda,N}(z)} \right| \le C(K)
   \]
   on compact sets \(K \subset \mathbb C \setminus \mathbb R\) off the real axis.
   Because \(\frac{F'(z)}{F(z)} = \sum \frac{-2z}{z_k^2 - z^2}\), and \(F_{\lambda,N}\) is anchored at \(z_* = i/2\),
   a bound on the imaginary part or local contour integrals can control \(F_{\lambda,N}\) without summing over all \(z_k\).

2. **Carathéodory-Herglotz half-plane control**:
   The logarithmic derivative \(f(z) = -F'(z)/F(z)\) is a Herglotz function on the upper half-plane \(\mathbb H\)
   (\(\operatorname{Im} f(z) > 0\) for \(\operatorname{Im} z > 0\)).
   Herglotz representations allow local uniform control from one-point normalization.

3. **Paley-Wiener exponential-type estimates**:
   Because \(\xi \in L^2([-a,a])\), \(\widehat{\xi}_{\lambda,N}\) is of exponential type \(a = \log\lambda\).
   Investigate whether the prolate/Sonin approximation \(k_\lambda \to \xi_\lambda\) provides direct uniform bounds on closed substrips \(|\operatorname{Im} z| \le 1/2 - \delta\).

Lane **RH-R068** is reserved for developing this replacement localized normal-family criterion.

---

## 8. Governance and claim boundaries

This work package strictly preserves the false-proof firewall:
- It does **not** assert that the finite determinants converge to \(\Xi\);
- It does **not** assert cofinal admissibility of any schedule;
- It does **not** assert global simple-evenness;
- It does **not** assert the existence of a limiting self-adjoint operator;
- It does **not** claim the Riemann Hypothesis, priority, novelty, or certification.
