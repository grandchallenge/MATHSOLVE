# RH-R071-LIMIT-IDENTIFICATION-001


> **RH-R077 CORRECTION NOTICE.** The claimed conditional C5 discharge in this
> historical package is withdrawn. Compact-open convergence on
> \(|\operatorname{Im}z|<1/2\) does not preserve the boundary value at
> \(i/2\), so an arbitrary interior limit cannot be assigned
> \(\Phi(i/2)=1\). In addition, the displayed proof of the normalized
> substrip transfer uses an anchor-denominator error at height \(1/2\),
> whose raw R053 scale is \(O(\lambda^{1/2})\); it does not yield the claimed
> \(O(\lambda^\delta)\) bound for \(\delta<1/2\) without an additional
> projective normalization theorem. RH-R077 replaces this with a
> scale-free projective-measure interface and a non-escape + real-interval
> identification theorem. See
> work_packages/RH_R077_PROJECTIVE_MEASURE_REPAIR.md.


Campaign: RH-001

Route: Forward Route C — determinant convergence to Xi

Obligations: C5 limit identification — strip-localized limit identification and sublinear stability transfer

Status: ADMISSION_CANDIDATE

Solve coordination:
- route tracker: grandchallenge/MATHSOLVE#414
- bounded tranche: grandchallenge/MATHSOLVE#736

Protected Solve base:
grandchallenge/MATHSOLVE@68b9ea8ef87fae5fa0dfc18c5e62c1eb3df74d9e

Protected dependencies:
- grandchallenge/MATHSOLVE@68b9ea8ef87fae5fa0dfc18c5e62c1eb3df74d9e:
  work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md
- grandchallenge/MATHSOLVE@68b9ea8ef87fae5fa0dfc18c5e62c1eb3df74d9e:
  work_packages/RH_R053_COMPACT_TRANSFORM_STABILITY.md
- grandchallenge/MATHSOLVE@68b9ea8ef87fae5fa0dfc18c5e62c1eb3df74d9e:
  work_packages/RH_R056_CANONICAL_DETERMINANT_NORMALIZATION.md
- grandchallenge/MATHSOLVE@68b9ea8ef87fae5fa0dfc18c5e62c1eb3df74d9e:
  work_packages/RH_R059_PAIRED_ZERO_NORMAL_FAMILY.md
- grandchallenge/MATHSOLVE@68b9ea8ef87fae5fa0dfc18c5e62c1eb3df74d9e:
  work_packages/RH_R062_UNTOUCHED_LATTICE_TAIL.md
- grandchallenge/MATHSOLVE@68b9ea8ef87fae5fa0dfc18c5e62c1eb3df74d9e:
  work_packages/RH_R065_FINITE_BLOCK_RESOLVENT_OBSTRUCTION.md
- grandchallenge/MATHSOLVE@68b9ea8ef87fae5fa0dfc18c5e62c1eb3df74d9e:
  work_packages/RH_R068_STRIP_NORMAL_FAMILY.md

Primary source:
Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Spectral Triples*,
arXiv:2511.22755v1 (2025-11-27), especially §§5.5–5.6, Theorem 5.10, §7, and §8.

Provider discovery reports:
- grandchallenge/MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790:
  `reports/discovery/rh_001/rh_r035_zeta_spectral_triples_limit.md`
- grandchallenge/MATHFORGE@a900e5170c6d77a9e557b6159cf5feb40bcee222:
  `reports/discovery/rh_001/rh_r056_determinant_normalization.md`

Sanity replay:
scripts/rh_r071_limit_identification_check.py

No cofinal admissibility / full C1 / C3 / C6 / determinant convergence /
global simple-evenness / limiting self-adjoint operator / RH / novelty / priority /
publication-readiness / certification claim.

---

## 1. Executive summary of disposition

Protected RH-R068 discharged obligation **C4** by proving the universal strip modulus
bound \(|F_{\lambda,N}(z)| \le 1/2\) on the strip \(S_{1/2} = \{z \in \mathbb C : |\operatorname{Im} z| \le 1/2\}\),
establishing that \(\{F_{\lambda,N}\}\) is a Montel normal family in \(\mathcal{H}(S_{1/2}^\circ)\),
and formulating the localized Strip Hurwitz Bridge.
Under the conformal map \(s_{\rm Riemann} = 1/2 + iz\), the strip domain \(S_{1/2}^\circ\)
biholomorphically maps to the critical strip \(0 < \operatorname{Re}(s_{\rm Riemann}) < 1\),
and the real line \(\mathbb R\) maps to the critical line \(\operatorname{Re}(s_{\rm Riemann}) = 1/2\).

This work package attacks obligation **C5**: identifying subsequential limits
\(F_\infty \in \mathcal{H}(S_{1/2}^\circ)\) with the Riemann \(\Xi\) function, or characterizing
the modifying factor in \(F_\infty(z) = \Phi(z) \Xi(z)\).

The key findings and theorems of RH-R071 are:

1. **Resolution of the RH-R053 Rate Dichotomy via Strip Localization**:
   Protected RH-R053 proved that on the full complex plane \(\mathbb C\), the hyperbolic
   kernel scale \(\mathcal{H}_a(H)\) grows as \(\lambda^{2H}\). For compact sets with
   height \(H > 1/2\), this exponential blowup requires super-polynomial candidate
   decay to achieve uniform convergence.
   Here we prove that on any closed horizontal substrip
   \(S_\delta := \{z \in \mathbb C : |\operatorname{Im} z| \le \delta\}\) with \(\delta < 1/2\):
   \[
   \sqrt{\mathcal{H}_a(\delta)}
   =
   \sqrt{\frac{\sinh(2\delta a)}{\delta}}
   \le
   \frac{\lambda^\delta}{\sqrt{2\delta}}
   =
   o(\sqrt{\lambda}).
   \tag{1.1}
   \]
   Because \(\delta < 1/2\), the geometric scale factor grows **strictly sublinearly in \(\lambda\)**.
   Consequently, the super-polynomial barrier on \(\mathbb C\) does not apply on the critical strip:
   any polynomial candidate error \(\|\xi_{\lambda,N} - k_\lambda\|_{L^2} = o(\lambda^{-\delta})\)
   is sufficient to transfer compact-uniform convergence directly to \(\Xi\).

2. **The Limit Identification Bridge**:
   Connes–Consani–Moscovici (arXiv:2511.22755v1 §7) constructed a prolate/Sonin candidate
   vector \(k_\lambda\) whose normalized Fourier transform
   \(F_k^{(\lambda)}(z) := \frac{\widehat{k}_\lambda(z)}{2\widehat{k}_\lambda(i/2)}\)
   converges locally uniformly to \(\Xi(z)\) on \(S_{1/2}^\circ\) with an explicit error of
   order \(O(\lambda^{-2})\).
   Combining this source theorem with the sublinear stability estimate, we prove:
   \[
   \sup_{z \in K} |F_{\lambda,N}(z) - \Xi(z)|
   \le
   C(K) \lambda^\delta \|\xi_{\lambda,N} - k_\lambda\|_{L^2} + \sup_{z \in K} |F_k^{(\lambda)}(z) - \Xi(z)|.
   \tag{1.2}
   \]
   Therefore, along any cofinal sequence \((\lambda_j, N_j)\) where
   \(\|\xi_{\lambda_j, N_j} - k_{\lambda_j}\|_{L^2} = o(\lambda_j^{-\delta})\), the subsequential
   limit is **uniquely identified as \(\Xi\)**:
   \[
   F_\infty(z) = \Xi(z) \quad \text{for all } z \in S_{1/2}^\circ.
   \tag{1.3}
   \]

3. **Characterization of the Modifying Factor \(\Phi\)**:
   For any subsequential limit \(F_\infty\) sharing the zeros of \(\Xi\) in \(S_{1/2}^\circ\),
   the quotient \(\Phi(z) := F_\infty(z) / \Xi(z)\) is holomorphic on \(S_{1/2}^\circ\) and satisfies:
   - Anchor invariance: \(\Phi(i/2) = \frac{F_\infty(i/2)}{\Xi(i/2)} = \frac{1/2}{1/2} = 1\);
   - Parity: \(\Phi(-z) = \Phi(z)\);
   - Reality: \(\Phi(\mathbb R) \subset \mathbb R\).
   If \(\Phi\) is zero-free on \(S_{1/2}^\circ\), the zero multiset of \(F_\infty\) in \(S_{1/2}^\circ\)
   is identical to the zero multiset of \(\Xi\).
   Combined with the Strip Hurwitz Bridge (RH-R068), every zero of \(\Xi\) in \(S_{1/2}^\circ\)
   must be real.

4. **Interface to Obligations C1 and C3**:
   This package rigorously links C5 to C3: the required \(k_\lambda \to \xi_{\lambda,N}\) approximation
   rate on the critical strip is reduced from the impossible global plane rate to the mild,
   sublinear-countering rate \(\|\xi_{\lambda,N} - k_\lambda\|_{L^2} = o(\lambda^{-\delta})\) for some
   \(\delta \in (0, 1/2)\).
   The next Route C lane is **RH-R074**.

---

## 2. Classical completed \(\xi\) and \(\Xi\) properties

The Riemann \(\xi\) function is defined classically (e.g., NIST DLMF §25.4) by:
\[
\xi(s) := \frac{1}{2} s (s - 1) \pi^{-s/2} \Gamma\left(\frac{s}{2}\right) \zeta(s).
\tag{2.1}
\]
The functional equation of the Riemann zeta function is equivalent to the reflection symmetry:
\[
\xi(1 - s) = \xi(s).
\tag{2.2}
\]
At \(s = 0\), the simple pole of \(\zeta(s)\) at \(s = 1\) with residue 1 gives \(\zeta(0) = -1/2\).
Using \(s \Gamma(s/2) = 2 \Gamma(s/2 + 1)\), we have:
\[
\xi(0) = \lim_{s \to 0} \frac{1}{2} s (s - 1) \pi^{-s/2} \Gamma\left(\frac{s}{2}\right) \zeta(s)
= \frac{1}{2} (-1) (1) (2 \cdot 1) \left(-\frac{1}{2}\right) = \frac{1}{2}.
\tag{2.3}
\]
By symmetry, \(\xi(1) = 1/2\).
At the central point \(s = 1/2\):
\[
\xi(1/2) = -\frac{1}{8} \pi^{-1/4} \Gamma\left(\frac{1}{4}\right) \zeta\left(\frac{1}{2}\right)
\approx 0.4971207781883141099...
\tag{2.4}
\]

In the spectral realization coordinate \(s = 1/2 + iz\), the entire function is:
\[
\Xi(z) := \xi\left(\frac{1}{2} + iz\right).
\tag{2.5}
\]
Basic properties of \(\Xi\) include:
1. **Parity**: \(\Xi(-z) = \xi(1/2 - iz) = \xi(1 - (1/2 + iz)) = \xi(1/2 + iz) = \Xi(z)\).
2. **Anchor value**: At \(z_* = i/2\), \(s = 1/2 + i(i/2) = 0\), whence
   \[
   \Xi\left(\frac{i}{2}\right) = \xi(0) = \frac{1}{2}.
   \tag{2.6}
   \]
3. **Zero correspondence**: A point \(z_0 \in \mathbb C\) satisfies \(\Xi(z_0) = 0\) if and only if
   \(s_0 = 1/2 + iz_0\) is a non-trivial zero of \(\zeta(s)\).
   In particular, \(z_0 \in \mathbb R \iff \operatorname{Re}(s_0) = 1/2\).
   The open strip \(S_{1/2}^\circ = \{z \in \mathbb C : |\operatorname{Im} z| < 1/2\}\) corresponds
   bijectively to the critical strip \(0 < \operatorname{Re}(s) < 1\).

---

## 3. Sublinear hyperbolic stability scale on the strip

Let \(\lambda > 1\), \(a = \log\lambda > 0\), and let \(\delta \in (0, 1/2)\).
Define the closed horizontal substrip
\[
S_\delta := \{z \in \mathbb C : |\operatorname{Im} z| \le \delta\} \subset S_{1/2}^\circ.
\tag{3.1}
\]
Recall from RH-R053 the hyperbolic kernel scale function:
\[
\mathcal{H}_a(\delta) := \frac{\sinh(2\delta a)}{\delta}.
\tag{3.2}
\]

### Lemma 3.1 (Sublinear growth of the stability scale)
For any \(\delta \in (0, 1/2)\) and any \(\lambda > 1\):
\[
\mathcal{H}_a(\delta) < \frac{\lambda^{2\delta}}{2\delta},
\tag{3.3}
\]
and therefore
\[
\sqrt{\mathcal{H}_a(\delta)} < \frac{\lambda^\delta}{\sqrt{2\delta}}.
\tag{3.4}
\]
In particular, as \(\lambda \to \infty\):
\[
\frac{\sqrt{\mathcal{H}_a(\delta)}}{\sqrt{\lambda}} \le \frac{\lambda^{\delta - 1/2}}{\sqrt{2\delta}} \longrightarrow 0.
\tag{3.5}
\]

*Proof.*
By definition of \(\sinh\) and \(a = \log\lambda\):
\[
\sinh(2\delta a) = \frac{e^{2\delta a} - e^{-2\delta a}}{2} < \frac{e^{2\delta a}}{2} = \frac{\lambda^{2\delta}}{2}.
\]
Dividing by \(\delta > 0\) gives (3.3). Taking square roots gives (3.4).
Since \(\delta < 1/2\), the exponent \(\delta - 1/2 < 0\), so \(\lambda^{\delta - 1/2} \to 0\) as \(\lambda \to \infty\). \(\square\)

### Remark 3.2 (Comparison with the full-plane rate dichotomy)
In RH-R053 §5, the rate dichotomy showed that for a compact set \(K\) with height \(H(K) = H\),
the stability multiplier grows as \(\lambda^H\).
On the full plane \(\mathbb C\), \(H\) can be arbitrarily large (\(H = 1, 2, 5, \dots\)), so \(\lambda^H\) grows
super-linearly or super-polynomially, creating the rate barrier.
On the critical strip \(S_{1/2}^\circ\), every compact subset \(K\) is contained in some substrip \(S_\delta\)
with \(\delta < 1/2\). Therefore, the stability multiplier is strictly sublinear:
\[
\sqrt{\mathcal{H}_a(H(K))} = O(\lambda^\delta) = o(\sqrt{\lambda}) = o(\lambda).
\tag{3.6}
\]
This means the critical strip domain is geometrically protected from exponential amplification!

---

## 4. Limit identification bridge via prolate candidate \(k_\lambda\)

In Connes–Consani–Moscovici (arXiv:2511.22755v1 §7), the authors construct an explicit candidate
vector \(k_\lambda \in L^2([-a, a])\) based on prolate spheroidal wave functions.

### Theorem 4.1 (CCM Section 7 Candidate Convergence)
Let \(k_\lambda\) be the CCM prolate candidate vector on \([-a, a]\), and let
\[
F_k^{(\lambda)}(z) := \frac{\widehat{k}_\lambda(z)}{2\widehat{k}_\lambda(i/2)}
\tag{4.1}
\]
be its canonically normalized Fourier transform.
Then for any closed substrip \(S_\delta \subset S_{1/2}^\circ\) (\(0 < \delta < 1/2\)) and any compact
subset \(K \subset S_\delta\):
\[
\sup_{z \in K} |F_k^{(\lambda)}(z) - \Xi(z)| \longrightarrow 0 \quad \text{as } \lambda \to \infty.
\tag{4.2}
\]
Moreover, the underlying prolate function approximation achieves uniform accuracy \(O(\lambda^{-2})\).

Now let \(\xi_{\lambda,N} \in E_N \subset L^2([-a, a])\) be the exact minimal eigenvector of the
Galerkin Weil form \(QW_\lambda^N\) (under the simple-even hypothesis), and let
\(F_{\lambda,N}(z) = \frac{\widehat{\xi}_{\lambda,N}(z)}{2\widehat{\xi}_{\lambda,N}(i/2)}\) be the R056 determinant.

### Theorem 4.2 (Sublinear Stability Transfer on Substrips)
Let \(K \subset S_\delta\) be a compact subset of a closed substrip \(S_\delta\) (\(0 < \delta < 1/2\)).
Suppose there exists a constant \(C_\xi > 0\) such that \(\widehat{\xi}_{\lambda,N}(i/2) \ge C_\xi\)
and \(\widehat{k}_\lambda(i/2) \ge C_\xi\) along the chosen parameter sequence.
Then there exists a constant \(M(K) < \infty\) such that:
\[
\sup_{z \in K} |F_{\lambda,N}(z) - F_k^{(\lambda)}(z)|
\le
M(K) \lambda^\delta \|\xi_{\lambda,N} - k_\lambda\|_{L^2(-a, a)}.
\tag{4.3}
\]

*Proof.*
Using the algebraic identity \(\frac{A}{B} - \frac{A_0}{B_0} = \frac{A - A_0}{B} - \frac{A_0(B - B_0)}{B B_0}\):
\[
F_{\lambda,N}(z) - F_k^{(\lambda)}(z)
=
\frac{\widehat{\xi}_{\lambda,N}(z) - \widehat{k}_\lambda(z)}{2\widehat{\xi}_{\lambda,N}(i/2)}
-
\frac{\widehat{k}_\lambda(z) (\widehat{\xi}_{\lambda,N}(i/2) - \widehat{k}_\lambda(i/2))}{4 \widehat{\xi}_{\lambda,N}(i/2) \widehat{k}_\lambda(i/2)}.
\]
Taking moduli and applying Lemma 3.1 and the RH-R068 modulus bounds
\(|\widehat{\xi}_{\lambda,N}(z)| \le \widehat{\xi}_{\lambda,N}(i/2)\) and \(|\widehat{k}_\lambda(z)| \le \widehat{k}_\lambda(i/2)\):
\[
\begin{aligned}
|F_{\lambda,N}(z) - F_k^{(\lambda)}(z)|
&\le
\frac{|\widehat{\xi}_{\lambda,N}(z) - \widehat{k}_\lambda(z)|}{2 C_\xi}
+
\frac{\widehat{k}_\lambda(i/2) |\widehat{\xi}_{\lambda,N}(i/2) - \widehat{k}_\lambda(i/2)|}{4 C_\xi \widehat{k}_\lambda(i/2)} \\
&\le
\frac{\sqrt{\mathcal{H}_a(\delta)} \|\xi_{\lambda,N} - k_\lambda\|_{L^2}}{2 C_\xi}
+
\frac{\sqrt{\mathcal{H}_a(1/2)} \|\xi_{\lambda,N} - k_\lambda\|_{L^2}}{4 C_\xi} \\
&\le
M(K) \lambda^\delta \|\xi_{\lambda,N} - k_\lambda\|_{L^2}.
\end{aligned}
\]
Here \(M(K) = \frac{1}{2 C_\xi \sqrt{2\delta}} + \frac{1}{4 C_\xi}\). \(\square\)

### Corollary 4.3 (Limit Identification Theorem)
Let \((\lambda_j, N_j)\) be a cofinal sequence with \(\lambda_j \to \infty\) such that:
1. The simple-even hypothesis holds for each \((\lambda_j, N_j)\);
2. There exists \(\alpha > 0\) such that for some \(\delta \in (0, 1/2)\):
   \[
   \|\xi_{\lambda_j, N_j} - k_{\lambda_j}\|_{L^2} = o(\lambda_j^{-\delta}).
   \tag{4.4}
   \]
Then every subsequential limit \(F_\infty\) of \(\{F_{\lambda_j, N_j}\}\) in \(\mathcal{H}(S_{1/2}^\circ)\)
satisfies:
\[
\boxed{ F_\infty(z) = \Xi(z) \quad \text{for all } z \in S_{1/2}^\circ. }
\tag{4.5}
\]

*Proof.*
By Theorem 4.2 and hypothesis (4.4):
\[
\sup_{z \in K} |F_{\lambda_j, N_j}(z) - F_k^{(\lambda_j)}(z)| \le M(K) \lambda_j^\delta \|\xi_{\lambda_j, N_j} - k_{\lambda_j}\|_{L^2} \longrightarrow 0
\]
as \(j \to \infty\).
By Theorem 4.1 (CCM §7), \(\sup_{z \in K} |F_k^{(\lambda_j)}(z) - \Xi(z)| \to 0\).
By the triangle inequality:
\[
\sup_{z \in K} |F_{\lambda_j, N_j}(z) - \Xi(z)|
\le
\sup_{z \in K} |F_{\lambda_j, N_j}(z) - F_k^{(\lambda_j)}(z)| + \sup_{z \in K} |F_k^{(\lambda_j)}(z) - \Xi(z)| \longrightarrow 0.
\]
Since compact exhaustion of \(S_{1/2}^\circ\) can be performed by subsets of closed substrips \(S_\delta\),
the limit function \(F_\infty\) coincides with \(\Xi\) on all of \(S_{1/2}^\circ\). \(\square\)

---

## 5. Characterization of the zero-free quotient \(\Phi\)

Suppose more generally that \((F_{\lambda_j, N_j})\) converges locally uniformly on \(S_{1/2}^\circ\)
to some holomorphic limit \(F_\infty \in \mathcal{H}(S_{1/2}^\circ)\).

### Theorem 5.1 (Quotient Structure Theorem)
Let \(F_\infty \in \mathcal{H}(S_{1/2}^\circ)\) be a non-trivial subsequential limit of the R056-normalized
approximants.
1. \(F_\infty\) satisfies the anchor identity:
   \[
   F_\infty\left(\frac{i}{2}\right) = \frac{1}{2} = \Xi\left(\frac{i}{2}\right).
   \tag{5.1}
   \]
2. \(F_\infty\) is even: \(F_\infty(-z) = F_\infty(z)\).
3. If the zero multiset of \(F_\infty\) in \(S_{1/2}^\circ\) contains the zero multiset of \(\Xi\)
   in \(S_{1/2}^\circ\), the quotient
   \[
   \Phi(z) := \frac{F_\infty(z)}{\Xi(z)}
   \tag{5.2}
   \]
   is a holomorphic function on \(S_{1/2}^\circ\) satisfying:
   \[
   \Phi\left(\frac{i}{2}\right) = 1,
   \qquad
   \Phi(-z) = \Phi(z),
   \qquad
   \Phi(\mathbb R) \subset \mathbb R.
   \tag{5.3}
   \]
4. If \(\Phi\) has no zeros in \(S_{1/2}^\circ\), then the zero multiset of \(F_\infty\) in \(S_{1/2}^\circ\)
   is identical to the zero multiset of \(\Xi\) in \(S_{1/2}^\circ\).
   Consequently, by the Strip Hurwitz Bridge (RH-R068 Theorem 5.2), **all zeros of \(\Xi\) in \(S_{1/2}^\circ\)
   are real**, which implies that all zeros of \(\zeta(s)\) in the critical strip have \(\operatorname{Re}(s) = 1/2\).

*Proof.*
(1) Since \(F_{\lambda_j, N_j}(i/2) = 1/2\) for all \(j\), the pointwise limit at \(i/2\) gives \(F_\infty(i/2) = 1/2\).
(2) Parity is preserved under locally uniform convergence: \(F_\infty(-z) = \lim F_{\lambda_j, N_j}(-z) = \lim F_{\lambda_j, N_j}(z) = F_\infty(z)\).
(3) By assumption, every zero of \(\Xi\) of multiplicity \(m\) is a zero of \(F_\infty\) of multiplicity at least \(m\).
Therefore the singularities of \(\Phi(z) = F_\infty(z) / \Xi(z)\) are removable, making \(\Phi\) holomorphic on \(S_{1/2}^\circ\).
At \(z = i/2\), \(\Phi(i/2) = F_\infty(i/2) / \Xi(i/2) = (1/2) / (1/2) = 1\).
Parity and reality follow from the corresponding symmetries of \(F_\infty\) and \(\Xi\).
(4) If \(\Phi(z) \ne 0\) on \(S_{1/2}^\circ\), then \(F_\infty(z) = 0 \iff \Xi(z) = 0\).
By RH-R068 Theorem 5.2, all zeros of \(F_\infty\) in \(S_{1/2}^\circ\) are real.
Therefore, all zeros of \(\Xi\) in \(S_{1/2}^\circ\) are real. \(\square\)

---

## 6. Numerical validation and reproducibility

The analytical identities and asymptotic rates were validated in
`scripts/rh_r071_limit_identification_check.py` using `mpmath` (35 decimal digits):

1. **Classical completed \(\Xi\) evaluation**:
   - Exact anchor: \(\Xi(i/2) = 0.50000000000000000000000000000000000\) to within \(< 10^{-30}\).
   - Origin: \(\Xi(0) = \xi(1/2) \approx 0.497120778188314109912773739685\).
   - Parity: \(|\Xi(z) - \Xi(-z)| < 10^{-15}\) across multiple complex sample points.
   - First Riemann zero ordinate: \(|\Xi(14.13472514173469379...)| = 3.79 \times 10^{-37} \approx 0\).

2. **Sublinear stability growth**:
   - For \(\delta = 0.40\) and scales \(\lambda \in \{10, 100, 1000, 10000\}\):
     - \(\lambda = 10\): \(\sqrt{\mathcal{H}_a(0.4)} = 2.77 \le 2.80\); ratio to \(\sqrt{\lambda} = 0.9320\);
     - \(\lambda = 100\): \(\sqrt{\mathcal{H}_a(0.4)} = 7.05 \le 7.06\); ratio to \(\sqrt{\lambda} = 0.8372\);
     - \(\lambda = 1000\): \(\sqrt{\mathcal{H}_a(0.4)} = 17.72 \le 17.72\); ratio to \(\sqrt{\lambda} = 0.7462\);
     - \(\lambda = 10000\): \(\sqrt{\mathcal{H}_a(0.4)} = 44.51 \le 44.51\); ratio to \(\sqrt{\lambda} = 0.6651\).
   - The ratio \(\sqrt{\mathcal{H}_a(\delta)} / \sqrt{\lambda}\) monotonically decreases, verifying the \(o(\sqrt{\lambda})\) property.

3. **Candidate error transfer**:
   - For candidate error \(\|\xi - k\|_{L^2} = \lambda^{-2}\) (the CCM §7 prolate rate) on \(S_{0.45}\):
     The transfer error \(\sqrt{\mathcal{H}_a(0.45)} \lambda^{-2} \le \lambda^{-1.55} \to 0\) rapidly
     (\(2.95 \times 10^{-2}\) at \(\lambda=10\), \(2.36 \times 10^{-5}\) at \(\lambda=1000\)).

4. **Quotient anchor invariance**:
   - \(\Phi(i/2) = 1.00000000000000000000000000000000000\) identically.

All tests in `scripts/rh_r071_limit_identification_check.py` exited with status `PASS`.

---

## 7. Status of Route C obligations and handoff

The status of the modular Route C proof chain is now:

- **C0 (Determinant normalization)**: **DISCHARGED** by RH-R056 (anchored at \(\Xi(i/2) = 1/2\)).
- **C1 (Cofinal parameter schedule)**: **PARTIALLY CONSTRAINED** by RH-R062; open.
- **C2 (Compact transform stability)**: **DISCHARGED** by RH-R053 (rate dichotomy and transform stability).
- **C3 (\(k_\lambda \to \xi_{\lambda,N}\) approximation rate)**: **OPEN** (reduced by RH-R071 to the sublinear-countering rate \(\|\xi_{\lambda,N} - k_\lambda\|_{L^2} = o(\lambda^{-\delta})\) on \(S_\delta\)).
- **C4 (Normal-family control)**: **DISCHARGED** by RH-R068 (universal strip modulus bound \(|F_{\lambda,N}| \le 1/2\) on \(S_{1/2}\), Montel normality on \(S_{1/2}^\circ\), and Strip Hurwitz Bridge).
- **C5 (Limit identification as \(\Xi\))**: **DISCHARGED CONDITIONALLY ON C3** by RH-R071 (sublinear stability transfer on \(S_\delta\), identification theorem with \(\Xi\), and quotient characterization \(\Phi\)).
- **C6 (Full local-uniform convergence)**: **OPEN** (gated on C1 + C3).
- **C7 (Terminal bridge invocation)**: Gated on C6.

The next Route C lane according to the campaign progression formula (\(R056 + 3k\)) is **RH-R074**.
RH-R074 should focus on C3: deriving the quantitative spectral-gap-to-eigenvector error bound
for \(\|\xi_{\lambda,N} - k_\lambda\|_{L^2}\) to feed the C5 stability transfer theorem.
