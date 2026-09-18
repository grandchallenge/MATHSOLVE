# RH-R031-BK-HALFLINE-LEBESGUE-001 — Half-line Berry–Keating spectral-type obstruction

- Campaign: RH-001
- Solve tracker: grandchallenge/MATHSOLVE#345
- Predecessor: RH-R030-SPECTRAL-UNBOUNDED-001
- Exact source audit: grandchallenge/MATHFORGE@a6a2e7d65adef8eaf977d77bbacbd05786d7da47, reports/discovery/rh_001/rh_r031_bk_halfline_prior_art.md
- Parent campaign route: RH-T-200 — Hilbert–Pólya sufficient-route contract
- Terminal target: RH-T-000 — OPEN
- Novelty / priority claim: none
- Certification status: not certified; MATHSOLVE theorem-development result only

## 1. Exact operator class

Let

\[
\mathcal H=L^2((0,\infty),dx)
\]

and on \(C_c^\infty(0,\infty)\) define

\[
H_0 f=-i\left(x f'(x)+\frac12 f(x)\right).
\]

This package concerns only the closure of this exact half-line dilation generator in the stated Hilbert space. Compact intervals, compact quantum graphs, rigged Hilbert spaces, nonlocal boundary conditions, bounded transforms, and modified operators are different classes.

## 2. Exact theorem

### Theorem RH-R031-BK-HALFLINE-LEBESGUE-001

Define

\[
(Wf)(y)=e^{y/2}f(e^y),\qquad y\in\mathbb R.
\]

Then \(W : L^2((0,\infty),dx)\to L^2(\mathbb R,dy)\) is unitary and, on the test-function core,

\[
W H_0 W^{-1}=-i\frac{d}{dy}.
\]

Consequently:

1. \(H_0\) is essentially self-adjoint;
2. its closure \(H_{BK}^+\) is unitarily equivalent to the standard momentum operator \(P=-i\,d/dy\) on domain \(H^1(\mathbb R)\);
3. \(\sigma(H_{BK}^+)=\mathbb R\);
4. the spectrum is purely absolutely continuous, with multiplicity one;
5. the point spectrum is empty.

Therefore this exact half-line Berry–Keating realization cannot supply a Hilbert–Pólya operator whose discrete eigenvalues are the raw ordinates of the nontrivial zeta zeros.

This theorem is known prior art and is replayed here to sharpen the governed operator contract. It is unconditional and does not imply RH.

## 3. Proof-obligation DAG

    RH-P031-01  W is unitary under x = exp(y)
          |
          v
    RH-P031-02  W H0 W^{-1} = -i d/dy on C_c^∞(R)
          |
          v
    RH-P031-03  momentum on C_c^∞(R) is essentially self-adjoint
          |
          v
    RH-P031-04  Fourier transform sends its closure to multiplication by ξ
          |
          +--> RH-P031-05  spectrum = R, purely absolutely continuous
          |
          +--> RH-P031-06  point spectrum is empty
          |
          v
    RH-P031-07  exact discrete ordinate-eigenvalue contract fails

Status: all obligations are discharged by the proof below plus standard momentum/Fourier spectral theory, with source status independently fixed by the protected MATHFORGE audit.

## 4. Proof

### 4.1 Unitarity of the logarithmic map

For \(f\in L^2((0,\infty),dx)\),

\[
\|Wf\|_2^2
=\int_{\mathbb R} e^y |f(e^y)|^2\,dy.
\]

With \(x=e^y\) and \(dx=e^y dy\),

\[
\|Wf\|_2^2=\int_0^\infty |f(x)|^2\,dx=\|f\|_2^2.
\]

The inverse is

\[
(W^{-1}g)(x)=x^{-1/2}g(\log x),
\]

so \(W\) is unitary.

### 4.2 Exact conjugation

Let \(g\in C_c^\infty(\mathbb R)\) and set

\[
f(x)=W^{-1}g=x^{-1/2}g(\log x).
\]

Then

\[
f'(x)
=x^{-3/2}\left(g'(\log x)-\frac12 g(\log x)\right).
\]

Hence

\[
x f'(x)+\frac12 f(x)
=x^{-1/2}g'(\log x).
\]

Therefore

\[
H_0 f(x)=-i x^{-1/2}g'(\log x)
\]

and applying \(W\) gives

\[
W H_0 W^{-1}g=-i g'.
\]

Thus \(H_0\) on its test-function core is unitarily equivalent to the usual momentum operator on \(C_c^\infty(\mathbb R)\).

### 4.3 Self-adjoint closure and spectrum

The momentum operator

\[
P_0=-i\frac{d}{dy},\qquad D(P_0)=C_c^\infty(\mathbb R),
\]

is essentially self-adjoint. Its closure \(P\) has domain \(H^1(\mathbb R)\).

Under the unitary Fourier transform \(\mathcal F\),

\[
\mathcal F P\mathcal F^{-1}=M_\xi,
\]

where \(M_\xi\) is multiplication by the real variable \(\xi\) on its natural domain.

The multiplication operator has spectrum \(\mathbb R\), and its spectral measure is Lebesgue measure. It has no eigenvalues: if

\[
M_\xi h=\lambda h,
\]

then \((\xi-\lambda)h(\xi)=0\) almost everywhere, so \(h\) is supported on the singleton \(\{\lambda\}\), a Lebesgue-null set. Therefore \(h=0\) in \(L^2(\mathbb R)\).

Unitary equivalence transfers these properties to the closure \(H_{BK}^+\) of \(H_0\).

QED.

## 5. Exact campaign consequence

The predecessor RH-R030 established that an exact raw-ordinate Hilbert–Pólya operator cannot be bounded. The present theorem shows that satisfying that necessary condition is not remotely sufficient.

For \(H_{BK}^+\),

\[
\sigma(H_{BK}^+)=\mathbb R.
\]

Accordingly, every real zero ordinate belongs to the spectrum in the weak set-containment sense. That observation is useless for the exact correspondence because:

- every other real number belongs to the spectrum too;
- no real number is an \(L^2\) eigenvalue;
- there is no discrete eigenvalue counting function to compare with Riemann–von Mangoldt.

The protected operator contract must therefore distinguish at least:

\[
\text{spectral containment}
\quad\neq\quad
\text{point-spectrum correspondence}
\quad\neq\quad
\text{complete discrete spectral realization}.
\]

## 6. False-proof firewall

The following moves are rejected.

1. Continuous-spectrum substitution. \(\gamma\in\sigma(H)\) does not imply that \(\gamma\) is an eigenvalue.
2. Generalized-eigenfunction substitution. The formal functions \(x^{-1/2+iE}\) are not \(L^2((0,\infty),dx)\) eigenvectors.
3. Self-adjointness-to-RH leap. The spectral parameter \(E\) is real by construction; that supplies no information about \(\Re(\rho)\).
4. Class substitution. Compactification, quantum graphs, rigged Hilbert spaces, or nonlocal boundary conditions are different operator classes.
5. Finite fitting. Agreement of a finite list of modified eigenvalues with zeta ordinates would not establish the exact spectral contract or the Riemann–von Mangoldt counting law.

These protections instantiate the existing campaign hazards RH-F003, RH-F010, and RH-F011.

## 7. Non-implications

This package does not:

- prove or disprove RH;
- construct a Hilbert–Pólya operator;
- exclude all Berry–Keating-inspired operators;
- exclude compact quantum-graph, boundary-conditioned, or modified-Hilbert-space realizations;
- establish a trace formula for the zeta zeros;
- claim novelty or priority;
- supply MATHCERT certification.

## 8. Next smallest safe target

The most informative nearby class is a discretized Berry–Keating realization for which the domain and self-adjoint boundary conditions are explicit. Before any spectral fitting, compare its eigenvalue counting law with the protected Riemann–von Mangoldt asymptotic.

A minimal successor is a single finite logarithmic interval, equivalently \(H_{BK}\) on \([a,b]\subset(0,\infty)\) with a self-adjoint quasi-periodic boundary condition. Under \(y=\log x\), this becomes momentum on a finite interval, giving an arithmetic spectrum and linear counting. That class requires a fresh exact MATHFORGE audit before Solve selection.

## 9. Terminal state

RH-R031_PROVED__HALFLINE_BK_CLASS_ELIMINATED

RH-T-000 remains open.
