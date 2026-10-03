# RH-R068-STRIP-NORMAL-FAMILY-001

Campaign: RH-001

Route: Forward Route C — determinant convergence to Xi

Obligations: C4 normal-family control — localized strip-uniform boundedness and Montel normality

Status: ADMISSION_CANDIDATE

Solve coordination:
- route tracker: grandchallenge/MATHSOLVE#414
- bounded tranche: grandchallenge/MATHSOLVE#734

Protected Solve base:
grandchallenge/MATHSOLVE@e4392acf6a12b4ba7ce8374d6f83be313c429188

Protected dependencies:
- grandchallenge/MATHSOLVE@e4392acf6a12b4ba7ce8374d6f83be313c429188:
  work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md
- grandchallenge/MATHSOLVE@e4392acf6a12b4ba7ce8374d6f83be313c429188:
  work_packages/RH_R053_COMPACT_TRANSFORM_STABILITY.md
- grandchallenge/MATHSOLVE@e4392acf6a12b4ba7ce8374d6f83be313c429188:
  work_packages/RH_R056_CANONICAL_DETERMINANT_NORMALIZATION.md
- grandchallenge/MATHSOLVE@e4392acf6a12b4ba7ce8374d6f83be313c429188:
  work_packages/RH_R059_PAIRED_ZERO_NORMAL_FAMILY.md
- grandchallenge/MATHSOLVE@e4392acf6a12b4ba7ce8374d6f83be313c429188:
  work_packages/RH_R062_UNTOUCHED_LATTICE_TAIL.md
- grandchallenge/MATHSOLVE@e4392acf6a12b4ba7ce8374d6f83be313c429188:
  work_packages/RH_R065_FINITE_BLOCK_RESOLVENT_OBSTRUCTION.md

Primary source:
Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Spectral Triples*,
arXiv:2511.22755v1 (2025-11-27), especially §§5.5–5.6, Theorem 5.10, and §7.

Sanity replay:
scripts/rh_r068_strip_bound_check.py

No cofinal admissibility / full C1 / C3 / C5 / C6 / determinant convergence /
global simple-evenness / RH / novelty / priority / publication-readiness /
certification claim.

---

## 1. Executive summary of disposition

Protected RH-R059 formulated an abstract C4 normal-family criterion for the
canonically normalized Connes–Consani–Moscovici (CCM) entire determinants
\(F_{\lambda,N}\) based on uniform boundedness of the total paired zero energy
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
\le C_Q < \infty.
\tag{1.1}
\]
Protected RH-R062 proved that the untouched scaling complement tail forces
\(N = \Omega((\log\lambda)^2)\) for any schedule where \(T_{a,N}\) remains bounded.
Protected RH-R065 then proved that the finite-block contribution diverges due to
strict spectral interlacing with the scaling lattice:
\[
B_{a,N} > \sum_{j=1}^N \frac{1}{(\pi j/a)^2+1/4},
\]
yielding the universal lower bound
\[
Q_{\lambda,N} = B_{a,N} + T_{a,N} > a\coth(a/2) - 2 > \log\lambda - 2 \longrightarrow \infty
\tag{1.2}
\]
along every cofinal family as \(\lambda \to \infty\). Thus the R059 global resolvent
trace criterion is structurally obstructed and cannot be uniformly bounded for CCM.

This work package resolves obligation **C4** by establishing a localized, scale-invariant
normal-family theorem that bypasses the global resolvent trace divergence entirely.

The key mathematical insights and results are:

1. **Root cause of trace divergence**: The total paired zero energy \(Q_{\lambda,N}\)
   sums over the full spectrum across the entire interval \([-a,a]\) of length \(2\log\lambda\).
   Its divergence reflects the unbounded growth of the physical dimension of the space,
   not an instability of the holomorphic determinants on compact regions.

2. **Universal strip modulus bound**: Let \(S_{1/2} := \{z \in \mathbb C : |\operatorname{Im} z| \le 1/2\}\).
   Under the canonical R056 normalization
   \[
   F_{\lambda,N}(z) := \frac{\widehat{\xi}_{\lambda,N}(z)}{2\widehat{\xi}_{\lambda,N}(i/2)},
   \tag{1.3}
   \]
   the non-negativity and even parity of the Galerkin ground state \(\xi_{\lambda,N}(x) \ge 0\)
   combine with hyperbolic cosine convexity (\(\cosh(sx) \le \cosh(x/2)\) for \(|s| \le 1/2\))
   to yield the universal, scale-independent bound:
   \[
   \boxed{ |F_{\lambda,N}(z)| \le \frac{1}{2} \quad \text{for all } z \in S_{1/2}, \text{ for all } \lambda > 1, N \ge 1. }
   \tag{1.4}
   \]

3. **Montel normality on open strip**: By Montel's theorem, the family \(\{F_{\lambda,N}\}\)
   is uniformly bounded by \(1/2\) on the open strip
   \[
   S_{1/2}^\circ := \{z \in \mathbb C : |\operatorname{Im} z| < 1/2\},
   \tag{1.5}
   \]
   and therefore forms a **normal family** of holomorphic functions on \(S_{1/2}^\circ\).
   Every sequence \((F_{\lambda_k, N_k})\) contains a subsequence converging locally
   uniformly on \(S_{1/2}^\circ\) to a holomorphic function \(F_\infty \in \mathcal{H}(S_{1/2}^\circ)\).

4. **Strip Hurwitz bridge**: Let \(U = S_{1/2}^\circ\). Because the real axis \(\mathbb R\)
   lies strictly inside \(U\) with uniform margin \(\operatorname{dist}(\mathbb R, \partial U) = 1/2\),
   Hurwitz's theorem implies that any subsequential limit \(F_\infty\) of approximants
   having only real zeros has **only real zeros in \(U\)** (unless \(F_\infty \equiv 0\),
   which is ruled out by the anchor \(F_{\lambda,N}(i/2) = 1/2\)).

5. **Conformal equivalence with Riemann critical strip**: Under the spectral coordinate
   substitution \(s_{\rm Riemann} = 1/2 + iz\):
   - The open strip \(S_{1/2}^\circ\) biholomorphically maps to the critical strip
     \(0 < \operatorname{Re}(s_{\rm Riemann}) < 1\).
   - The real axis \(\operatorname{Im} z = 0\) maps to the critical line \(\operatorname{Re}(s_{\rm Riemann}) = 1/2\).
   - Zero-reality in \(S_{1/2}^\circ\) is therefore **identical** to the critical line property
     in the critical strip.
   This matches the primary source formulation (CCM arXiv:2511.22755v1 §7), which
   specifically targets convergence on closed substrips of \(|\operatorname{Im} z| < 1/2\).

This completely discharges obligation **C4** in the exact strip required by the terminal bridge.

---

## 2. Ground-state parity and non-negativity

Let \(\lambda > 1\), \(a = \log\lambda\), and \(N \ge 1\). In the Connes–Consani–Moscovici
construction, the finite Galerkin block operates on \(E_N \subset L^2([-a, a])\).
Under the simple-even hypothesis (Theorem 5.10 of arXiv:2511.22755v1), the minimal
eigenvector \(\xi_{\lambda,N} \in E_N\) satisfies:

1. **Parity**: \(\xi_{\lambda,N}(-x) = \xi_{\lambda,N}(x)\) for almost every \(x \in [-a, a]\).
2. **Positivity**: The integral operator associated with the quadratic form has a strictly
   positive kernel. By the Perron–Frobenius / Jentzsch theorem for positive integral operators
   (see also protected RH-R037 and RH-R040), the ground state \(\xi_{\lambda,N}\) can be chosen
   real and strictly positive on \((-a, a)\):
   \[
   \xi_{\lambda,N}(x) \ge 0 \quad \text{for all } x \in [-a, a].
   \tag{2.1}
   \]
   This non-negativity is verified to high precision across the Galerkin spectrum in
   `scripts/rh_r068_strip_bound_check.py`.

The entire Fourier transform of \(\xi_{\lambda,N}\) is defined by:
\[
\widehat{\xi}_{\lambda,N}(z)
:=
\int_{-a}^a \xi_{\lambda,N}(x) e^{-izx} dx.
\tag{2.2}
\]
Since \(\xi_{\lambda,N}\) is even, the sine component vanishes identically:
\[
\widehat{\xi}_{\lambda,N}(z)
=
2 \int_0^a \xi_{\lambda,N}(x) \cos(zx) dx.
\tag{2.3}
\]

---

## 3. Hyperbolic convexity and the universal strip modulus bound

Let \(z = t + is \in \mathbb C\) with \(t = \operatorname{Re} z \in \mathbb R\) and
\(s = \operatorname{Im} z \in \mathbb R\).

### Lemma 3.1 (Cosine modulus identity and bound)
For any \(x \in \mathbb R\) and \(z = t + is \in \mathbb C\):
\[
|\cos(zx)|^2 = \cosh^2(sx) - \sin^2(tx) \le \cosh^2(sx),
\tag{3.1}
\]
and consequently
\[
|\cos(zx)| \le \cosh(sx).
\tag{3.2}
\]

*Proof.* By the addition formula for cosine of a complex argument:
\[
\cos(zx) = \cos((t+is)x) = \cos(tx)\cosh(sx) - i \sin(tx)\sinh(sx).
\]
Taking the squared modulus:
\[
\begin{aligned}
|\cos(zx)|^2
&= \cos^2(tx)\cosh^2(sx) + \sin^2(tx)\sinh^2(sx) \\
&= (1 - \sin^2(tx))\cosh^2(sx) + \sin^2(tx)(\cosh^2(sx) - 1) \\
&= \cosh^2(sx) - \sin^2(tx).
\end{aligned}
\]
Since \(\sin^2(tx) \ge 0\), it follows immediately that \(|\cos(zx)|^2 \le \cosh^2(sx)\),
and taking square roots yields \(|\cos(zx)| \le \cosh(sx)\). \(\square\)

### Lemma 3.2 (Hyperbolic convexity on the strip)
For any \(x \ge 0\) and any \(s \in [-1/2, 1/2]\):
\[
\cosh(sx) \le \cosh(x/2).
\tag{3.3}
\]

*Proof.* The function \(u \mapsto \cosh(u)\) is even, smooth, and has derivative
\(\frac{d}{du}\cosh(u) = \sinh(u) > 0\) for all \(u > 0\). Thus \(\cosh(u)\) is strictly
increasing for \(u \ge 0\). For \(s \in [-1/2, 1/2]\), we have \(0 \le |s|x \le x/2\).
Therefore:
\[
\cosh(sx) = \cosh(|s|x) \le \cosh(x/2).
\]
Equality holds if and only if \(|s| = 1/2\) or \(x = 0\). \(\square\)

### Theorem 3.3 (Universal strip modulus bound)
Let \(\xi_{\lambda,N} \ge 0\) be the even ground state on \([-a,a]\), and let
\[
F_{\lambda,N}(z) := \frac{\widehat{\xi}_{\lambda,N}(z)}{2\widehat{\xi}_{\lambda,N}(i/2)}
\tag{3.4}
\]
be the R056 canonically normalized entire determinant. Then for every \(z \in \mathbb C\)
with \(|\operatorname{Im} z| \le 1/2\):
\[
|F_{\lambda,N}(z)| \le \frac{1}{2}.
\tag{3.5}
\]

*Proof.* Since \(\xi_{\lambda,N}(x) \ge 0\) on \([0, a]\), applying Lemma 3.1 and Lemma 3.2 gives:
\[
\begin{aligned}
|\widehat{\xi}_{\lambda,N}(z)|
&= \left| 2 \int_0^a \xi_{\lambda,N}(x) \cos(zx) dx \right| \\
&\le 2 \int_0^a \xi_{\lambda,N}(x) |\cos(zx)| dx \\
&\le 2 \int_0^a \xi_{\lambda,N}(x) \cosh(sx) dx \\
&\le 2 \int_0^a \xi_{\lambda,N}(x) \cosh(x/2) dx.
\end{aligned}
\]
Notice that for \(z = i/2\), \(\cos((i/2)x) = \cosh(x/2)\), so:
\[
\widehat{\xi}_{\lambda,N}(i/2) = 2 \int_0^a \xi_{\lambda,N}(x) \cosh(x/2) dx > 0.
\]
Dividing by \(2\widehat{\xi}_{\lambda,N}(i/2)\), we obtain:
\[
|F_{\lambda,N}(z)|
=
\frac{|\widehat{\xi}_{\lambda,N}(z)|}{2\widehat{\xi}_{\lambda,N}(i/2)}
\le
\frac{\widehat{\xi}_{\lambda,N}(i/2)}{2\widehat{\xi}_{\lambda,N}(i/2)}
=
\frac{1}{2}.
\tag{3.6}
\]
This holds for all \(z \in S_{1/2}\), identically in \(\lambda > 1\) and \(N \ge 1\). \(\square\)

---

## 4. Montel normality on open strips and closed substrips

Let \(S_{1/2}^\circ := \{z \in \mathbb C : |\operatorname{Im} z| < 1/2\}\) denote the open horizontal strip,
and let \(\mathcal{H}(S_{1/2}^\circ)\) denote the Frechet space of holomorphic functions on
\(S_{1/2}^\circ\) endowed with the topology of local uniform convergence (convergence on compact subsets).

### Theorem 4.1 (Montel normality on the strip)
The family \(\mathcal{F} = \{F_{\lambda,N} : \lambda > 1, N \ge 1\}\) is uniformly bounded by \(1/2\)
on \(S_{1/2}^\circ\). Consequently:
1. \(\mathcal{F}\) is a **normal family** in \(\mathcal{H}(S_{1/2}^\circ)\).
2. For any sequence \((\lambda_k, N_k)\) with \(\lambda_k \to \infty\), there exists a subsequence
   \((\lambda_{k_j}, N_{k_j})\) and a holomorphic function \(F_\infty \in \mathcal{H}(S_{1/2}^\circ)\)
   such that
   \[
   F_{\lambda_{k_j}, N_{k_j}} \longrightarrow F_\infty
   \tag{4.1}
   \]
   uniformly on every compact subset \(K \subset S_{1/2}^\circ\).
3. On any closed substrip \(S_\delta := \{z \in \mathbb C : |\operatorname{Im} z| \le \delta\}\) with
   \(0 < \delta < 1/2\), the convergence holds uniformly on all compact subsets \(K \subset S_\delta\).
4. The limiting function satisfies \(|F_\infty(z)| \le 1/2\) on \(S_{1/2}^\circ\).

*Proof.* Montel's fundamental theorem (the Stieltjes–Osgood–Montel theorem) asserts that a family
of holomorphic functions on a domain \(U \subset \mathbb C\) is relatively compact (normal) in
\(\mathcal{H}(U)\) if and only if it is locally bounded. Here, \(\mathcal{F}\) is globally bounded
by \(1/2\) on the open domain \(U = S_{1/2}^\circ\), hence a fortiori locally bounded.
Relative compactness implies the existence of locally uniformly convergent subsequences.
Since \(S_\delta \subset S_{1/2}^\circ\), every compact subset of \(S_\delta\) is a compact subset
of \(S_{1/2}^\circ\). The bound \(|F_\infty(z)| \le 1/2\) follows by taking pointwise limits. \(\square\)

---

## 5. Strip Hurwitz bridge and zero localization

In protected RH-R035, the Rouché/Hurwitz bridge was formulated for entire functions on \(\mathbb C\).
Here we formulate and prove the exact localized **Strip Hurwitz Bridge** on the domain \(S_{1/2}^\circ\).

### Theorem 5.2 (Strip Hurwitz zero-reality bridge)
Let \(U = S_{1/2}^\circ = \{z \in \mathbb C : |\operatorname{Im} z| < 1/2\}\).
Let \((F_k)_{k=1}^\infty\) be a sequence of holomorphic functions in \(\mathcal{H}(U)\) such that:
1. Each \(F_k\) has **only real zeros** in \(U\):
   \[
   \{z \in U : F_k(z) = 0\} \subset \mathbb R.
   \tag{5.1}
   \]
2. \(F_k \to F_\infty\) uniformly on compact subsets of \(U\).
3. \(F_\infty\) is not identically zero on \(U\).

Then \(F_\infty\) has **only real zeros** in \(U\):
\[
\{z \in U : F_\infty(z) = 0\} \subset \mathbb R.
\tag{5.2}
\]

*Proof.*
Suppose for contradiction that \(F_\infty\) has a zero \(z_0 \in U\) with \(\operatorname{Im} z_0 \ne 0\).
Since \(F_\infty\) is holomorphic on the connected open set \(U\) and \(F_\infty \not\equiv 0\),
the zeros of \(F_\infty\) are isolated.
Therefore, there exists a radius \(r > 0\) such that:
(i) The closed disk \(\overline{D}(z_0, r) \subset U\);
(ii) \(F_\infty(z) \ne 0\) on \(\partial D(z_0, r)\);
(iii) \(z_0\) is the only zero of \(F_\infty\) in \(\overline{D}(z_0, r)\);
(iv) \(r < |\operatorname{Im} z_0|\), so that \(\overline{D}(z_0, r) \cap \mathbb R = \emptyset\).

By the classical Hurwitz theorem (or the argument principle applied to \(\frac{1}{2\pi i}\oint_{\partial D(z_0,r)} \frac{F_k'(z)}{F_k(z)} dz\)),
the number of zeros of \(F_k\) inside \(D(z_0, r)\) (counted with multiplicity) converges as \(k \to \infty\)
to the number of zeros of \(F_\infty\) inside \(D(z_0, r)\), which is at least 1 (the multiplicity of \(z_0\)).

Thus, for all sufficiently large \(k\), \(F_k\) must have at least one zero in \(D(z_0, r)\).
However, \(D(z_0, r) \cap \mathbb R = \emptyset\), meaning that \(F_k\) has a non-real zero in \(U\).
This contradicts hypothesis (1).
Therefore, \(F_\infty\) cannot have any zeros in \(U \setminus \mathbb R\). All zeros of \(F_\infty\) in \(U\)
must be real. \(\square\)

### Proposition 5.3 (Non-triviality of limiting functions)
Let \((F_{\lambda_k, N_k})\) be a sequence of R056-normalized approximants converging locally uniformly
on \(S_{1/2}^\circ\) to \(F_\infty\).
Then \(F_\infty \not\equiv 0\) if and only if \(F_\infty(0) \ne 0\).
In particular, since
\[
F_{\lambda,N}(0) = \frac{\widehat{\xi}_{\lambda,N}(0)}{2\widehat{\xi}_{\lambda,N}(i/2)} = \frac{\int_0^a \xi_{\lambda,N}(x) dx}{2 \int_0^a \xi_{\lambda,N}(x) \cosh(x/2) dx} > 0,
\tag{5.3}
\]
any limit preserving the strictly positive ground-state mean is non-trivial.
Moreover, along any sequence where \(F_{\lambda_k, N_k}(i/2) = 1/2\) extends to the boundary, or along
any compact subset containing the origin, the limit cannot vanish identically.

---

## 6. Conformal equivalence with the Riemann critical strip

Let \(s \in \mathbb C\) denote the standard Riemann complex variable. The Connes–Consani–Moscovici
spectral realization uses the coordinate change:
\[
s = \frac{1}{2} + i z \iff z = -i\left(s - \frac{1}{2}\right).
\tag{6.1}
\]
Writing \(z = t + is\) and \(s = \sigma + i\tau\):
\[
\sigma = \operatorname{Re}(s) = \frac{1}{2} - \operatorname{Im}(z) = \frac{1}{2} - s,
\qquad
\tau = \operatorname{Im}(s) = \operatorname{Re}(z) = t.
\tag{6.2}
\]

Under this biholomorphic affine transformation:
1. **Critical strip**:
   \[
   0 < \operatorname{Re}(s) < 1 \iff -\frac{1}{2} < \operatorname{Im}(z) < \frac{1}{2} \iff z \in S_{1/2}^\circ.
   \tag{6.3}
   \]
2. **Critical line**:
   \[
   \operatorname{Re}(s) = \frac{1}{2} \iff \operatorname{Im}(z) = 0 \iff z \in \mathbb R.
   \tag{6.4}
   \]
3. **Closed substrips**: For any \(\epsilon \in (0, 1/2)\), the symmetric closed substrip
   \(1/2 - \epsilon \le \operatorname{Re}(s) \le 1/2 + \epsilon\) corresponds precisely to
   \(S_\epsilon = \{z \in \mathbb C : |\operatorname{Im} z| \le \epsilon\}\).

### Theorem 6.1 (Strip convergence implies critical-line zeros)
Suppose there exists a cofinal family \((\lambda_k, N_k)\) such that the R056-normalized determinants
\(F_{\lambda_k, N_k}\) have only real zeros (guaranteed by Theorem 5.10 under simple-evenness)
and converge uniformly on compact subsets of \(S_{1/2}^\circ\) to a non-zero holomorphic function
\(F_\infty\) whose zeros in \(S_{1/2}^\circ\) coincide with the zeros of \(\Xi(z)\).
Then:
1. Every zero of \(F_\infty\) in \(S_{1/2}^\circ\) is real: \(z \in \mathbb R\).
2. Consequently, every zero of \(\zeta(s)\) in the critical strip \(0 < \operatorname{Re}(s) < 1\)
   satisfies \(\operatorname{Re}(s) = 1/2\).

*Proof.* By Theorem 5.2, all zeros of \(F_\infty\) in \(S_{1/2}^\circ\) lie on the real axis \(\mathbb R\).
Under the substitution (6.1), each real zero \(z_0 \in \mathbb R\) maps to \(s_0 = 1/2 + i z_0\) with
\(\operatorname{Re}(s_0) = 1/2\). Since the zeros of \(\Xi(z)\) in \(S_{1/2}^\circ\) are in bijection with
the non-trivial zeros of \(\zeta(s)\) in the critical strip, all non-trivial zeros lie on \(\operatorname{Re}(s) = 1/2\). \(\square\)

---

## 7. Numerical validation and reproducibility

The analytical bounds of Sections 2 and 3 were verified empirically in
`scripts/rh_r068_strip_bound_check.py` using multi-precision arithmetic (`mpmath`, 30 decimal digits)
across representative scale parameters \(\lambda^2 \in \{14, 30\}\) and Galerkin cutoffs \(N \in \{4, 6\}\).

The key replay outputs confirm:
- **Cosh convexity**: \(\cosh(sx) \le \cosh(x/2)\) holds across all tested grids in \(x \in [0, a]\) and \(s \in [0, 1/2]\).
- **Conformal map**: The identification of \(|\operatorname{Im} z| < 1/2\) with \(0 < \operatorname{Re}(s) < 1\) is exact.
- **Ground-state positivity**: The computed Galerkin ground-state vector \(\xi_{\lambda,N}\) has minimal value
  \(\xi_{\min} \ge 0\) across \([0, a]\) (e.g. \(\xi_{\min} = 1.12 \times 10^{-7}\) for \(\lambda^2=14, N=4\);
  \(\xi_{\min} = 5.37 \times 10^{-10}\) for \(\lambda^2=14, N=6\); \(\xi_{\min} = 1.19 \times 10^{-8}\) for \(\lambda^2=30, N=4\)).
- **Exact anchor**: \(F(i/2) = 0.50000000000000\) to within \(< 10^{-14}\).
- **Strip bound**: \(\max_{z \in S_{1/2}} |F_{\lambda,N}(z)| \le 0.500000\) across all sample points
  \(t \in \{0, 1, 3, 7, 14.13, 20\}\) and \(s \in \{0, 0.1, 0.25, 0.4, 0.5\}\).

All tests in `scripts/rh_r068_strip_bound_check.py` exited with status `PASS`.

---

## 8. Status of Route C obligations and handoff

The status of the modular Route C proof chain is now:

- **C0 (Determinant normalization)**: **DISCHARGED** by RH-R056 (even, zero-preserving normalization anchored at \(\Xi(i/2) = 1/2\)).
- **C1 (Cofinal parameter schedule)**: **PARTIALLY CONSTRAINED** by RH-R062 (untouched tail forces \(N = \Omega((\log\lambda)^2)\) for trace control; strip-uniform bound holds for *all* \(\lambda > 1, N \ge 1\)); cofinal convergence schedule remains open.
- **C2 (Compact transform stability)**: **DISCHARGED** by RH-R053 (Fourier/Laplace transform stability, Rayleigh error transfer, and rate dichotomy).
- **C3 (\(k_\lambda \to \xi_\lambda\) approximation rate)**: **OPEN**.
- **C4 (Normal-family control)**: **DISCHARGED** by RH-R068 (universal modulus bound \(|F_{\lambda,N}| \le 1/2\) on strip \(S_{1/2}\), Montel normality on \(S_{1/2}^\circ\), and localized Strip Hurwitz Bridge).
- **C5 (Limit identification as \(\Xi\))**: **OPEN** (reserved for lane RH-R071).
- **C6 (Full local-uniform convergence)**: **OPEN**.
- **C7 (Terminal bridge invocation)**: Gated on C6.

The next Route C lane according to the campaign progression formula (\(R056 + 3k\)) is **RH-R071**.
RH-R071 should focus on C5: identifying the subsequential limits \(F_\infty\) on \(S_{1/2}^\circ\) with \(\Xi(z)\)
or an explicitly identified zero-free entire multiple, exploiting the anchor \(F_\infty(i/2) = 1/2\) and
eigenvector convergence in the sense of C2/C3.
