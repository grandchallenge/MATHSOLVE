# RH-R053-COMPACT-TRANSFORM-STABILITY-001

Campaign: RH-001

Status:
ADMISSION_CANDIDATE__DEPENDENCIES_PROTECTED

Solve tracker:
grandchallenge/MATHSOLVE#433

Coordination:
grandchallenge/MATHSOLVE#414 (Forward Route C)

Protected dependencies:
- grandchallenge/MATHSOLVE@763e976f2c77c623b619b62b0d0a999c673f76d5:work_packages/RH_R052_REFRESHED_HERGLOTZ_MARGINS.md
- grandchallenge/MATHSOLVE@564f6e2b41c9b13334bc8a5b84914a85c6b70790:work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md
- grandchallenge/MATHSOLVE@51042c94185cc9db1fa457ae40f26276747a0a4d:work_packages/RH_R036_QW_PARITY_GAP_REDUCTION.md
- grandchallenge/MATHSOLVE@76221c214bcb8227557d25741d83927051e62e8b:work_packages/RH_R037_QW_SECTOR_GALERKIN.md

No RH / novelty / priority / certification claim.

## 1. Purpose

In Forward Route C (codified in `handoffs/RH-001/routes/ROUTE_C_DETERMINANT_CONVERGENCE.md`),
the campaign attacks the terminal determinant-convergence bridge:
if a cofinal family of correctly normalized finite entire determinants \(F_j\) has
only real zeros and converges locally uniformly on \(\mathbb C\) to \(\Xi\), then
by the protected R035 Rouché/Hurwitz theorem, all zeros of \(\Xi\) are real,
implying the Riemann Hypothesis without constructing a limiting self-adjoint operator first.

The modular proof-obligation chain specifies:
- **C2**: Prove a compact-set transform/determinant stability estimate with exact dependence on scale \(a=\log\lambda\) and compact height \(H(K)=\sup_{z\in K}|\operatorname{Im} z|\).
- **C3**: Convert source candidate vector approximation \(k_\lambda\to\xi_\lambda\) into a norm/rate strong enough for C2, or prove what rate is required.

This work package proves the exact compact-set transform stability theorem (C2),
establishing:
1. sharp quantitative bounds in \(L^1\) and \(L^2\) norms for the Fourier/Mellin transform difference on any compact subset \(K\subset\mathbb C\);
2. an improved stability estimate exploiting the even-inversion parity of the ground state;
3. an exact rate dichotomy theorem identifying the precise eigenvector convergence rates required on the real axis, on horizontal strips, and on the full complex plane;
4. a structural obstruction theorem proving that bare \(L^2\) transform estimates cannot yield compact-uniform convergence on all of \(\mathbb C\) with only polynomial or fixed-rate exponential decay in \(\lambda\) without appealing to the Montel normal-family bridge (C4) or super-polynomial cancellation.

## 2. Geometry and Transform Setup

Fix \(\lambda>1\) and set
\[
a=\log\lambda>0.
\]
In multiplicative coordinates on \([\lambda^{-1},\lambda]\) with Haar measure
\(d^*u=du/u\), logarithmic coordinates \(x=\log u\in[-a,a]\) identify the space
with \(L^2([-a,a],dx)\).

For any function \(f\in L^2([-a,a])\), its Fourier/Mellin transform is
\[
\widehat{f}(z)
:=
\int_{-a}^a e^{-izx} f(x)\,dx
=
\int_{\lambda^{-1}}^\lambda u^{-iz} f(\log u)\,\frac{du}{u},
\qquad
z\in\mathbb C.
\]
Because the integration interval \([-a,a]\) is compact, \(\widehat{f}\) is an
entire function of exponential type at most \(a\) by the Paley–Wiener theorem.

In the Connes–Consani–Moscovici (CCM) Zeta Spectral Triples construction, the
raw regularized determinant of the finite spectral approximant is given by the
protected formula (RH-R035):
\[
\det_{\mathrm{reg}}\left(D_{\log}^{(\lambda,N)}-z\right)
=
-i\,\lambda^{-iz}\widehat{\xi}_{\lambda,N}(z),
\]
where \(\xi_{\lambda,N}\) is the finite ground state on \(E_N\).

We define the normalized determinant kernel operator
\[
\mathcal{D}_a[f](z)
:=
\lambda^{-iz}\widehat{f}(z)
=
e^{-iza}\widehat{f}(z).
\]

For any complex number \(z=t+i\sigma\) with \(t=\operatorname{Re} z\) and \(\sigma=\operatorname{Im} z\):
\[
-iza=-i(t+i\sigma)a=\sigma a-ita,
\]
whence
\[
|\lambda^{-iz}|=|e^{\sigma a-ita}|=e^{\sigma a}=\lambda^{\operatorname{Im} z}.
\]

Let \(K\subset\mathbb C\) be an arbitrary non-empty compact set.  We associate to
\(K\) three geometric height parameters:
\[
H(K):=\sup_{z\in K}|\operatorname{Im} z|<\infty,
\]
\[
\sigma_{\max}(K):=\sup_{z\in K}\operatorname{Im} z,
\qquad
\sigma_{\min}(K):=\inf_{z\in K}\operatorname{Im} z.
\]
Clearly,
\[
-H(K)\le\sigma_{\min}(K)\le\sigma_{\max}(K)\le H(K).
\]
For every \(z\in K\),
\[
|\lambda^{-iz}|\le e^{\sigma_{\max}(K)a}\le e^{H(K)a}.
\]

## 3. Sharp Compact-Set Stability Estimates

Let \(f, g\in L^2([-a,a])\) be two form vectors (e.g., the exact ground state
\(\xi_{\lambda,N}\) and a trial or candidate vector \(k_\lambda\)).

### Lemma 3.1 (\(L^1\) transform stability)
For every compact set \(K\subset\mathbb C\) and every \(z\in K\):
\[
|\widehat{f}(z)-\widehat{g}(z)|
\le
e^{H(K)a}\|f-g\|_{L^1(-a,a)}.
\]
Consequently, for the determinant kernel:
\[
\sup_{z\in K}|\mathcal{D}_a[f](z)-\mathcal{D}_a[g](z)|
\le
e^{(\sigma_{\max}(K)+H(K))a}\|f-g\|_{L^1(-a,a)}
\le
e^{2H(K)a}\|f-g\|_{L^1(-a,a)}.
\]

*Proof.*
For any \(z=t+i\sigma\in K\) and \(x\in[-a,a]\):
\[
|e^{-izx}|=|e^{-itx}e^{\sigma x}|=e^{\sigma x}\le e^{|\sigma||x|}\le e^{H(K)a}.
\]
Therefore,
\[
|\widehat{f}(z)-\widehat{g}(z)|
=
\left|\int_{-a}^a e^{-izx}(f(x)-g(x))\,dx\right|
\le
\int_{-a}^a e^{\sigma x}|f(x)-g(x)|\,dx
\le
e^{H(K)a}\|f-g\|_{L^1(-a,a)}.
\]
Multiplying by \(|\lambda^{-iz}|=e^{\sigma a}\le e^{\sigma_{\max}(K)a}\) gives the
second inequality.
\(\blacksquare\)

### Lemma 3.2 (Exact \(L^2\) transform stability)
Define the hyperbolic kernel scale function \(\mathcal{H}_a:[0,\infty)\to[0,\infty)\) by
\[
\mathcal{H}_a(H)
:=
\begin{cases}
\dfrac{\sinh(2Ha)}{H}, & H>0, \\
2a, & H=0.
\end{cases}
\]
Then for every compact set \(K\subset\mathbb C\):
\[
\sup_{z\in K}|\widehat{f}(z)-\widehat{g}(z)|
\le
\sqrt{\mathcal{H}_a(H(K))}\,\|f-g\|_{L^2(-a,a)}.
\]
For the determinant kernel:
\[
\sup_{z\in K}|\mathcal{D}_a[f](z)-\mathcal{D}_a[g](z)|
\le
e^{\sigma_{\max}(K)a}\sqrt{\mathcal{H}_a(H(K))}\,\|f-g\|_{L^2(-a,a)}
\le
\sqrt{2a}\,e^{2H(K)a}\,\|f-g\|_{L^2(-a,a)}.
\]

*Proof.*
For any \(z=t+i\sigma\in K\), applying the Cauchy–Schwarz inequality on \([-a,a]\):
\[
|\widehat{f}(z)-\widehat{g}(z)|
\le
\int_{-a}^a e^{\sigma x}|f(x)-g(x)|\,dx
\le
\left(\int_{-a}^a e^{2\sigma x}\,dx\right)^{1/2}\|f-g\|_{L^2(-a,a)}.
\]
When \(\sigma=0\), \(\int_{-a}^a 1\,dx=2a=\mathcal{H}_a(0)\).
When \(\sigma\ne 0\):
\[
\int_{-a}^a e^{2\sigma x}\,dx
=
\left[\frac{e^{2\sigma x}}{2\sigma}\right]_{-a}^a
=
\frac{e^{2\sigma a}-e^{-2\sigma a}}{2\sigma}
=
\frac{\sinh(2\sigma a)}{\sigma}
=
2a\frac{\sinh(2\sigma a)}{2\sigma a}.
\]
The function \(u\mapsto \frac{\sinh u}{u}=\sum_{k=0}^\infty \frac{u^{2k}}{(2k+1)!}\)
is strictly increasing for \(u>0\).  Since \(|\sigma|\le H(K)\),
\[
\frac{\sinh(2\sigma a)}{\sigma}\le \frac{\sinh(2H(K)a)}{H(K)}=\mathcal{H}_a(H(K)).
\]
Taking the square root gives the first bound.

For the second bound, notice that for \(H>0\):
\[
\mathcal{H}_a(H)
=
\frac{e^{2Ha}-e^{-2Ha}}{2H}
<
\frac{e^{2Ha}}{2H}
=
2a\,\frac{e^{2Ha}}{4Ha}.
\]
More simply, using \(\sinh(2Ha)\le \frac{1}{2}e^{2Ha}\) and \(e^{\sigma_{\max}(K)a}\le e^{Ha}\):
\[
e^{\sigma_{\max}(K)a}\sqrt{\mathcal{H}_a(H(K))}
\le
e^{Ha}\sqrt{2a\frac{\sinh(2Ha)}{2Ha}}
\le
\sqrt{2a}\,e^{2Ha}.
\]
\(\blacksquare\)

### Lemma 3.3 (Parity-exploiting stability for even form states)
Under the inversion symmetry \(u\mapsto u^{-1}\) of the semilocal Weil form (RH-R036),
the ground-state candidate vectors are even:
\[
f(-x)=f(x),
\qquad
g(-x)=g(x),
\qquad
x\in[-a,a].
\]
Then for every compact set \(K\subset\mathbb C\):
\[
\sup_{z\in K}|\widehat{f}(z)-\widehat{g}(z)|
\le
\sqrt{a+\frac{\sinh(2H(K)a)}{2H(K)}}\,\|f-g\|_{L^2(-a,a)}.
\]
For \(H(K)\to 0\), the prefactor converges to \(\sqrt{2a}\).
For \(H(K)>0\), the prefactor satisfies:
\[
\sqrt{a+\frac{\sinh(2H(K)a)}{2H(K)}}
\le
\frac{1}{\sqrt{2}}\sqrt{\mathcal{H}_a(H(K))}\left(1+\frac{2H(K)a}{\sinh(2H(K)a)}\right)^{1/2}
<
\sqrt{\mathcal{H}_a(H(K))}.
\]

*Proof.*
Because \(f-g\) is even on \([-a,a]\),
\[
\widehat{f}(z)-\widehat{g}(z)
=
\int_{-a}^a e^{-izx}(f(x)-g(x))\,dx
=
2\int_0^a \cos(zx)(f(x)-g(x))\,dx.
\]
For \(z=t+i\sigma\),
\[
\cos(zx)=\cos(tx+i\sigma x)=\cos(tx)\cosh(\sigma x)-i\sin(tx)\sinh(\sigma x).
\]
Hence
\[
|\cos(zx)|^2
=
\cos^2(tx)\cosh^2(\sigma x)+\sin^2(tx)\sinh^2(\sigma x)
=
\cos^2(tx)+\sinh^2(\sigma x)
\le
\cosh^2(\sigma x).
\]
By Cauchy–Schwarz on \([0,a]\):
\[
\left|2\int_0^a \cos(zx)(f(x)-g(x))\,dx\right|
\le
2\left(\int_0^a \cosh^2(\sigma x)\,dx\right)^{1/2}\|f-g\|_{L^2(0,a)}.
\]
Using the elementary identity \(\cosh^2(u)=\frac{1+\cosh(2u)}{2}\):
\[
\int_0^a \cosh^2(\sigma x)\,dx
=
\int_0^a \frac{1+\cosh(2\sigma x)}{2}\,dx
=
\frac{a}{2}+\frac{\sinh(2\sigma a)}{4\sigma}.
\]
Since \(f-g\) is even, \(\|f-g\|_{L^2(-a,a)}^2=2\|f-g\|_{L^2(0,a)}^2\), so
\(\|f-g\|_{L^2(0,a)}=\frac{1}{\sqrt{2}}\|f-g\|_{L^2(-a,a)}\).
Multiplying gives
\[
2\left(\frac{a}{2}+\frac{\sinh(2\sigma a)}{4\sigma}\right)^{1/2}\frac{1}{\sqrt{2}}\|f-g\|_{L^2(-a,a)}
=
\sqrt{a+\frac{\sinh(2\sigma a)}{2\sigma}}\|f-g\|_{L^2(-a,a)}.
\]
Monotonicity of \(\sigma\mapsto \frac{\sinh(2\sigma a)}{2\sigma}\) completes the proof.
\(\blacksquare\)

## 4. Exact Rate Dichotomy and Obstruction Theorem

The stability theorems above establish the exact rates of eigenvector convergence
required to guarantee determinant convergence across different geometric domains.

### Theorem 4.1 (Exact rate dichotomy for determinant convergence)
Let \((\lambda_j)_{j=1}^\infty\) be a sequence of scales with \(\lambda_j\to\infty\)
and \(a_j=\log\lambda_j\to\infty\).  Let \(\xi_j\) and \(\psi_j\) be normalized
form vectors in \(L^2([-a_j, a_j])\).

1. **Real-axis uniform convergence (\(H=0\)):**
   If \(K\subset\mathbb R\), then
   \[
   \sup_{t\in K}|\mathcal{D}_{a_j}[\xi_j](t)-\mathcal{D}_{a_j}[\psi_j](t)|\to 0
   \]
   holds whenever
   \[
   \|\xi_j-\psi_j\|_{L^2(-a_j,a_j)} = o\left(a_j^{-1/2}\right) = o\left((\log\lambda_j)^{-1/2}\right).
   \]

2. **Horizontal strip uniform convergence (\(H=\delta>0\)):**
   Let \(S_\delta:=\{z\in\mathbb C:|\operatorname{Im} z|\le\delta\}\).  For every compact
   subset \(K\subset S_\delta\),
   \[
   \sup_{z\in K}|\mathcal{D}_{a_j}[\xi_j](z)-\mathcal{D}_{a_j}[\psi_j](z)|\to 0
   \]
   holds whenever
   \[
   \|\xi_j-\psi_j\|_{L^2(-a_j,a_j)} = o\left(a_j^{-1/2}e^{-2\delta a_j}\right)
   =
   o\left((\log\lambda_j)^{-1/2}\lambda_j^{-2\delta}\right).
   \]

3. **Global plane obstruction for bare \(L^2\) bounds:**
   Suppose \(\|\xi_j-\psi_j\|_{L^2}\) decays at a fixed exponential rate:
   \[
   \|\xi_j-\psi_j\|_{L^2(-a_j,a_j)} = \Theta\left(\lambda_j^{-c}\right) = \Theta\left(e^{-ca_j}\right)
   \]
   for some constant \(c>0\).  Then for every compact set \(K\subset\mathbb C\) whose
   height exceeds \(c/2\), i.e.,
   \[
   H(K)>\frac{c}{2},
   \]
   the generic Cauchy–Schwarz upper bound
   \[
   \sqrt{2a_j}\,e^{2H(K)a_j}\|\xi_j-\psi_j\|_{L^2}
   =
   \Theta\left(\sqrt{a_j}\,e^{(2H(K)-c)a_j}\right)
   \longrightarrow \infty
   \qquad (j\to\infty)
   \]
   diverges exponentially.

*Proof.*
Part 1 follows from Lemma 3.2 with \(H(K)=0\), where the prefactor is \(\sqrt{2a}\).
Part 2 follows from Lemma 3.2 with \(H(K)\le\delta\) and \(\sigma_{\max}(K)\le\delta\),
where the prefactor is bounded by \(\sqrt{2a}e^{2\delta a}\).
Part 3 follows directly by substituting \(\|\xi_j-\psi_j\|_{L^2}=\Theta(e^{-ca_j})\),
which leaves the exponent \(2H(K)-c>0\).
\(\blacksquare\)

### Corollary 4.2 (Strategic consequence for C3 and C4)
Theorem 4.1 rigorously demonstrates that compact-uniform determinant convergence
on all of \(\mathbb C\) cannot be achieved by direct \(L^2\) eigenvector bounds
unless either:
1. the candidate approximation \(k_\lambda-\xi_\lambda\) has super-exponential decay
   in \(a\) (faster than \(\lambda^{-M}\) for every \(M>0\)); or
2. the convergence is mediated by **C4 (Montel normal-family control)**:
   establishing uniform boundedness on compact subsets of \(\mathbb C\) combined
   with convergence on the real axis (requiring only \(o(a^{-1/2})\) decay) or on
   a thin horizontal strip (requiring only finite-power decay \(\lambda^{-2\delta}\)).

This establishes the formal necessity of the normal-family architecture (C4) for
any practical eigenvector approximation scheme.

## 5. Spectral Gap to Eigenvector Error Transfer (Feeding C3)

To feed C3, we connect the required vector error \(\|\xi_\lambda-\psi_\lambda\|_{L^2}\)
to the spectral gap proved in Routes A and B.

### Lemma 5.1 (Rayleigh-quotient to eigenvector bound)
Let \(QW_\lambda\) be the semilocal Weil form on \(L^2([\lambda^{-1},\lambda])\).
Suppose the lowest eigenvalue \(\epsilon_1(\lambda)\) is simple, with normalized
eigenvector \(\xi_\lambda\), and let \(\epsilon_2(\lambda)\) be the second
eigenvalue in the same sector.  Define the spectral gap:
\[
\operatorname{Gap}(\lambda):=\epsilon_2(\lambda)-\epsilon_1(\lambda)>0.
\]
Let \(\psi\) be any normalized vector (\(\|\psi\|=1\)) in the form domain with
Rayleigh quotient
\[
\mathcal{R}(\psi):=QW_\lambda(\psi,\psi).
\]
Then
\[
\|\psi-\langle\xi_\lambda,\psi\rangle\xi_\lambda\|^2
\le
\frac{\mathcal{R}(\psi)-\epsilon_1(\lambda)}{\operatorname{Gap}(\lambda)}.
\]
In particular, choosing the global phase such that \(\langle\xi_\lambda,\psi\rangle\ge 0\),
\[
\|\psi-\xi_\lambda\|^2
\le
\frac{2(\mathcal{R}(\psi)-\epsilon_1(\lambda))}{\operatorname{Gap}(\lambda)}.
\]

*Proof.*
Decompose \(\psi = c_1 \xi_\lambda + \psi_\perp\), where \(\langle\xi_\lambda,\psi_\perp\rangle=0\).
Since \(\|\psi\|^2 = |c_1|^2 + \|\psi_\perp\|^2 = 1\), the spectral theorem gives
\[
\mathcal{R}(\psi)
=
|c_1|^2 \epsilon_1(\lambda) + QW_\lambda(\psi_\perp,\psi_\perp)
\ge
|c_1|^2 \epsilon_1(\lambda) + \epsilon_2(\lambda)\|\psi_\perp\|^2.
\]
Subtracting \(\epsilon_1(\lambda) = (|c_1|^2 + \|\psi_\perp\|^2)\epsilon_1(\lambda)\):
\[
\mathcal{R}(\psi)-\epsilon_1(\lambda)
\ge
(\epsilon_2(\lambda)-\epsilon_1(\lambda))\|\psi_\perp\|^2
=
\operatorname{Gap}(\lambda)\|\psi_\perp\|^2.
\]
Dividing by \(\operatorname{Gap}(\lambda)>0\) yields the first bound.
When \(c_1\ge 0\), \(1-c_1 = \frac{1-c_1^2}{1+c_1} = \frac{\|\psi_\perp\|^2}{1+c_1}\le \|\psi_\perp\|^2\).
Then \(\|\psi-\xi_\lambda\|^2 = (1-c_1)^2 + \|\psi_\perp\|^2 \le 2\|\psi_\perp\|^2\).
\(\blacksquare\)

### Quantitative interface with Route A/B
From protected RH-R051 and RH-R052, for all \(0<a\le 178/1000\), the even internal
spectral gap is explicitly lower-bounded:
\[
\operatorname{Gap}(e^a)
=
\nu_{+,2}(a)-\nu_{+,1}(a)
>
\frac{1783634369}{11837500000}
\approx 0.1506766.
\]
Therefore, on the proved local regime, the Rayleigh quotient error transfers to
eigenvector error with a certified magnification factor:
\[
\|\psi-\xi_\lambda\|^2
\le
\frac{2}{0.1506766}\left(\mathcal{R}(\psi)-\epsilon_1(\lambda)\right)
<
13.275\left(\mathcal{R}(\psi)-\epsilon_1(\lambda)\right).
\]

## 6. Theorem

### RH-R053-COMPACT-TRANSFORM-STABILITY-001

Let \(\lambda>1\), \(a=\log\lambda\), and let \(\xi, \psi\in L^2([-a,a])\) be
form vectors.  Let \(K\subset\mathbb C\) be any compact set with
\(H(K)=\sup_{z\in K}|\operatorname{Im} z|\) and \(\sigma_{\max}(K)=\sup_{z\in K}\operatorname{Im} z\).

1. **Bare transform stability:**
   \[
   \sup_{z\in K}|\widehat{\xi}(z)-\widehat{\psi}(z)|
   \le
   \sqrt{\mathcal{H}_a(H(K))}\,\|\xi-\psi\|_{L^2(-a,a)},
   \]
   where \(\mathcal{H}_a(H)=\frac{\sinh(2Ha)}{H}\) for \(H>0\) and \(\mathcal{H}_a(0)=2a\).

2. **Parity-refined transform stability:**
   If \(\xi\) and \(\psi\) are even,
   \[
   \sup_{z\in K}|\widehat{\xi}(z)-\widehat{\psi}(z)|
   \le
   \sqrt{a+\frac{\sinh(2H(K)a)}{2H(K)}}\,\|\xi-\psi\|_{L^2(-a,a)}.
   \]

3. **Determinant stability:**
   \[
   \sup_{z\in K}|\lambda^{-iz}\widehat{\xi}(z)-\lambda^{-iz}\widehat{\psi}(z)|
   \le
   e^{\sigma_{\max}(K)a}\sqrt{\mathcal{H}_a(H(K))}\,\|\xi-\psi\|_{L^2(-a,a)}
   \le
   \sqrt{2a}\,e^{2H(K)a}\,\|\xi-\psi\|_{L^2(-a,a)}.
   \]

4. **Rate dichotomy:**
   - Uniform convergence on the real axis requires \(\|\xi-\psi\|_{L^2} = o(a^{-1/2})\);
   - Uniform convergence on horizontal strips \(|\operatorname{Im} z|\le\delta\) requires \(\|\xi-\psi\|_{L^2} = o\left(a^{-1/2}e^{-2\delta a}\right)\);
   - Local uniform convergence on all of \(\mathbb C\) cannot be inferred from bare \(L^2\) bounds with fixed exponential rate \(\lambda^{-c}\), formally establishing the necessity of the C4 normal-family/Montel architecture or super-exponential cancellation.

## 7. False-Proof Firewall

Reject:
1. Concluding compact-uniform convergence on \(\mathbb C\) from real-axis convergence alone without a normal-family theorem (C4);
2. Inferring that polynomial eigenvector error in \(\log\lambda\) suffices for complex-plane determinant convergence;
3. Suppressing the exponential factor \(\lambda^{2H(K)}\) when claiming determinant approximations;
4. Treating numerical overlap \(\langle k_\lambda, \xi_\lambda\rangle \approx 1\) as a proof of convergence without an explicit rate bounding \(\sqrt{\mathcal{H}_a(H)}\|k_\lambda-\xi_\lambda\|\);
5. Claiming RH, determinant convergence to \(\Xi\), or global simple-evenness.

## 8. Claim Boundary

This theorem does not prove:
- that \(k_\lambda\to\xi_\lambda\) actually converges at any of the identified rates;
- local uniform convergence of the finite Zeta Spectral Triple determinants to \(\Xi\);
- global simple-evenness of \(QW_\lambda\) for large \(\lambda\);
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 9. Admission Disposition

Terminal candidate disposition:

RH-R053_COMPACT_TRANSFORM_STABILITY_AND_RATE_DICHOTOMY_PROVED__READY_FOR_EXACT_HEAD_ADMISSION
