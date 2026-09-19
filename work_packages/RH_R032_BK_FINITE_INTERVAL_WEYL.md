# RH-R032-BK-FINITE-INTERVAL-WEYL-001 — Fixed-interval counting obstruction

- Campaign: RH-001
- Solve tracker: grandchallenge/MATHSOLVE#347
- Predecessor: RH-R031-BK-HALFLINE-LEBESGUE-001
- Protected source audit: grandchallenge/MATHFORGE@c49d7507dd45338f6328141c7d708acb5806e702
- Parent campaign route: RH-T-200 — Hilbert–Pólya sufficient-route contract
- Terminal target: RH-T-000 — OPEN
- Novelty / priority claim: none
- Certification status: not certified; MATHSOLVE theorem-development result only

## 1. Exact class

Fix \(0<a<b<\infty\) and \(\theta\in[0,2\pi)\). Let

\[
H=-i\left(x\frac{d}{dx}+\frac12\right)
\]

act in \(L^2([a,b],dx)\) with the self-adjoint boundary condition

\[
\sqrt b\,f(b)=e^{i\theta}\sqrt a\,f(a).
\]

Set

\[
\alpha=\log a,\qquad \beta=\log b,\qquad L=\beta-\alpha=\log(b/a).
\]

Under

\[
(Wf)(y)=e^{y/2}f(e^y),
\]

this is unitarily equivalent to

\[
P_\theta=-i\frac{d}{dy}
\]

on \(L^2([\alpha,\beta],dy)\) with

\[
g(\beta)=e^{i\theta}g(\alpha).
\]

The interval and phase are fixed once and for all. Energy-dependent geometry or boundary data are outside this theorem.

## 2. Exact theorem

### Theorem RH-R032-BK-FINITE-INTERVAL-WEYL-001

For the class above, the spectrum is

\[
\sigma(H)
=
\left\{
\frac{\theta+2\pi n}{L}:n\in\mathbb Z
\right\},
\]

with the phase convention induced by the stated boundary condition.

If

\[
N_H(T)=\#\{\lambda\in\sigma(H):0<\lambda\le T\},
\]

counting multiplicity, then

\[
N_H(T)=\frac{L}{2\pi}T+O(1).
\]

By contrast, the positive nontrivial-zeta ordinate count satisfies

\[
N_\zeta(T)
=
\frac{T}{2\pi}
\log\left(\frac{T}{2\pi e}\right)
+O(\log T).
\]

Therefore no fixed triple \((a,b,\theta)\) in this self-adjoint finite-interval Berry–Keating family has eigenvalue multiset equal to the positive raw ordinates of all nontrivial zeta zeros.

The result is unconditional and known in broader compact-graph form. It does not imply RH.

## 3. Proof-obligation DAG

    RH-P032-01  logarithmic unitary reduction to finite-interval momentum
          |
          v
    RH-P032-02  solve -i g' = k g under quasi-periodic boundary
          |
          v
    RH-P032-03  k_n = (theta + 2 pi n)/L
          |
          v
    RH-P032-04  positive counting = L T/(2 pi) + O(1)
          |
          +------------------------------+
          |                              |
          v                              v
    RH-P032-05  RvM count = T log T/(2 pi)+O(T)
          |                              |
          +--------------+---------------+
                         v
    RH-P032-06  fixed-interval exact ordinate spectrum impossible

All obligations are discharged below, with the Riemann–von Mangoldt input inherited from RH-T-030.

## 4. Proof

### 4.1 Unitary reduction

The same calculation as in RH-R031 gives

\[
W H W^{-1}=-i\frac{d}{dy}.
\]

The original boundary condition becomes

\[
(Wf)(\beta)=e^{i\theta}(Wf)(\alpha).
\]

Thus the exact spectral problem is finite-interval momentum with a quasi-periodic self-adjoint boundary condition.

### 4.2 Eigenvalues

An eigenfunction satisfies

\[
-i g'(y)=k g(y),
\]

so

\[
g(y)=C e^{iky}.
\]

The boundary condition gives

\[
e^{ik\beta}=e^{i\theta}e^{ik\alpha},
\]

hence

\[
e^{ikL}=e^{i\theta}.
\]

Therefore

\[
kL=\theta+2\pi n
\]

for some \(n\in\mathbb Z\), and

\[
k_n=\frac{\theta+2\pi n}{L}.
\]

These eigenvalues are simple for a single interval.

### 4.3 Exact counting order

The condition \(0<k_n\le T\) is equivalent to

\[
0<\theta+2\pi n\le LT.
\]

The number of integers in this interval differs from its length \(LT/(2\pi)\) by a uniformly bounded endpoint error. Therefore

\[
N_H(T)=\frac{L}{2\pi}T+O(1).
\]

In particular,

\[
\frac{N_H(T)}{T}\to \frac{L}{2\pi}.
\]

### 4.4 Comparison with Riemann–von Mangoldt

The protected RH-T-030 interface gives

\[
N_\zeta(T)
=
\frac{T}{2\pi}
\log\left(\frac{T}{2\pi e}\right)
+O(\log T).
\]

Dividing by \(T\),

\[
\frac{N_\zeta(T)}{T}
=
\frac{1}{2\pi}\log T+O(1)
\to\infty.
\]

Thus \(N_H(T)\) and \(N_\zeta(T)\) cannot agree for all sufficiently large \(T\), and the underlying eigenvalue multisets cannot be equal.

QED.

## 5. Campaign consequence

RH-R030 forced any exact raw-ordinate candidate to be unbounded.

RH-R031 showed that the canonical unbounded half-line Berry–Keating operator has only continuous spectrum.

RH-R032 now shows that the simplest fixed self-adjoint compactification restores discreteness but produces the wrong asymptotic density:

\[
\text{finite interval}
\Rightarrow
N(T)=O(T),
\]

where the target requires

\[
N_\zeta(T)\asymp T\log T.
\]

Hence the Riemann–von Mangoldt growth law is not merely a final consistency check. It is an early operator-design gate.

## 6. False-proof firewall

Rejected moves:

1. Finite spectral fitting cannot override an asymptotically incompatible counting law.
2. Choosing a very large fixed \(L\) changes only the linear coefficient and cannot create the missing \(\log T\).
3. Letting \(L=L(T)\) changes the operator with the spectral cutoff and is not one fixed self-adjoint realization.
4. Letting the boundary phase depend on energy leaves the audited \(U(1)\) self-adjoint family.
5. Nonlinear transformations of \(k_n\) change the protected raw-ordinate normalization.
6. A general compact graph is a different class, although established prior art gives the same linear-Weyl obstruction for fixed compact graphs.

## 7. Non-implications

This package does not:

- prove or disprove RH;
- rule out every unbounded self-adjoint operator;
- rule out every Berry–Keating-inspired modification;
- rule out noncompact graphs or genuinely different operators;
- authorize energy-dependent geometry as a fixed operator;
- establish novelty or priority;
- render MATHCERT certification.

## 8. Next smallest safe target

The current sequence identifies the missing structural feature:

a viable discrete spectral candidate must produce the extra logarithmic growth in its counting function while remaining one fixed self-adjoint operator.

The next route should therefore be selected by mechanism, not by level fitting. Before Solve work, MATHFORGE should audit one exact class in which a \(T\log T\) counting law can arise from fixed operator structure, such as a noncompact geometry, a logarithmically growing effective phase-space volume, or another rigorously fixed spectral mechanism.

Any candidate must specify:

- one fixed Hilbert space;
- one fixed densely defined operator;
- one fixed self-adjoint domain;
- the exact spectral normalization;
- the mechanism that changes the Weyl/counting growth from \(O(T)\) to \(T\log T\).

## 9. Terminal state

RH-R032_PROVED__FIXED_FINITE_INTERVAL_BK_CLASS_ELIMINATED

RH-T-000 remains open.
