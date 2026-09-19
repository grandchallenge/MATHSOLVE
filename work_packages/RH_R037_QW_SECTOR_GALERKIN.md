# RH-R037-QW-SECTOR-GALERKIN-001 — Sector-wise Galerkin convergence for the Weil form

- Campaign: RH-001
- Solve tracker: grandchallenge/MATHSOLVE#369
- Protected provider audit: grandchallenge/MATHFORGE@76221c214bcb8227557d25741d83927051e62e8b
- Predecessor: RH-R036-QW-PARITY-GAP-REDUCTION-001
- Terminal target: RH-T-000 — OPEN
- Novelty / priority claim: none
- Certification status: not certified; MATHSOLVE theorem-development result only

## 1. Purpose

RH-R036 reduced the first Zeta Spectral Triples missing theorem to two obligations:

1. simplicity of the lowest even eigenvalue of \(A_\lambda\);
2. the strict parity gap
   \[
   \epsilon_+(\lambda)<\epsilon_-(\lambda).
   \]

The source gives exact finite parity blocks \(E_{N,\pm}\) and a full form core \(E=\bigcup_N E_N\).

This package proves that the finite parity-sector Rayleigh minima converge to the full parity-sector spectral bottoms. It converts finite parity calculations from informal evidence into controlled Galerkin approximants.

It does not prove that the limiting gap is positive.

## 2. Protected inputs

Fix \(\lambda>1\).

Let \(\mathcal H_\lambda\) be the source Hilbert space, \(q_\lambda\) the closed lower-bounded semilocal Weil form, and \(A_\lambda\) its canonical self-adjoint operator.

Let \(J\) be inversion,

\[
(Jf)(u)=f(u^{-1}).
\]

RH-R036 proved:

\[
J\operatorname{Dom}(q_\lambda)=\operatorname{Dom}(q_\lambda),
\qquad
q_\lambda(Jf,Jg)=q_\lambda(f,g),
\]

and

\[
A_\lambda J=J A_\lambda.
\]

Define

\[
\mathcal H_{\lambda,\pm}=\ker(J\mp I).
\]

The source finite spaces are

\[
E_N=\operatorname{span}\{V_n:|n|\le N\},
\]

with

\[
E_N\subset E_{N+1},
\qquad
E=\bigcup_N E_N
\]

a form core for \(q_\lambda\).

The protected R037 audit binds

\[
J E_N=E_N,
\]

and

\[
E_{N,\pm}
=
E_N\cap\mathcal H_{\lambda,\pm}.
\]

## 3. Shifted form norm

Because \(q_\lambda\) is lower bounded, choose \(c\in\mathbb R\) such that

\[
q_{\lambda,c}(f,f)
:=
q_\lambda(f,f)+c\|f\|^2
\]

is positive definite on \(\operatorname{Dom}(q_\lambda)\).

Use the form norm

\[
\|f\|_{q,c}^2
=
q_{\lambda,c}(f,f).
\]

The inversion invariance of \(q_\lambda\) and unitarity of \(J\) give

\[
\|Jf\|_{q,c}
=
\|f\|_{q,c}.
\]

Define the parity projections

\[
P_\pm=\frac{I\pm J}{2}.
\]

For \(f_+\in\mathcal H_{\lambda,+}\) and \(f_-\in\mathcal H_{\lambda,-}\),

\[
q_{\lambda,c}(f_+,f_-)
=
q_{\lambda,c}(Jf_+,Jf_-)
=
-q_{\lambda,c}(f_+,f_-),
\]

so

\[
q_{\lambda,c}(f_+,f_-)=0.
\]

Hence

\[
\|P_\pm f\|_{q,c}
\le
\|f\|_{q,c}.
\]

Thus each \(P_\pm\) is a contraction on the form Hilbert space.

## 4. Parity-sector core theorem

### Proposition RH-P037-SECTOR-CORE

For each sign,

\[
E_\pm
:=
\bigcup_N E_{N,\pm}
\]

is a form core for the restricted form

\[
q_{\lambda,\pm}
=
q_\lambda|_{\operatorname{Dom}(q_\lambda)\cap\mathcal H_{\lambda,\pm}}.
\]

### Proof

Take

\[
f\in
\operatorname{Dom}(q_\lambda)\cap\mathcal H_{\lambda,\pm}.
\]

Since \(E\) is a form core, there exists a sequence \(e_k\in E\) with

\[
\|e_k-f\|_{q,c}\to0.
\]

Set

\[
e_k^\pm=P_\pm e_k.
\]

Because every \(E_N\) is \(J\)-invariant, if \(e_k\in E_{N_k}\), then

\[
e_k^\pm\in E_{N_k,\pm}.
\]

Since \(P_\pm f=f\) and \(P_\pm\) is a form-norm contraction,

\[
\|e_k^\pm-f\|_{q,c}
=
\|P_\pm(e_k-f)\|_{q,c}
\le
\|e_k-f\|_{q,c}
\to0.
\]

Thus \(E_\pm\) is dense in the restricted form domain in the form norm.

QED.

## 5. Finite parity Rayleigh minima

Define

\[
\epsilon_{\pm,N}(\lambda)
=
\min_{0\ne f\in E_{N,\pm}}
\frac{q_\lambda(f,f)}{\|f\|^2}.
\]

These are exactly the lowest eigenvalues of the finite parity blocks of the source matrix \(QW_\lambda^N\).

Define the full sector bottoms

\[
\epsilon_\pm(\lambda)
=
\inf_{
0\ne f\in
\operatorname{Dom}(q_\lambda)\cap\mathcal H_{\lambda,\pm}
}
\frac{q_\lambda(f,f)}{\|f\|^2}.
\]

By RH-R036 and source discreteness, these full infima are eigenvalues of the parity-restricted self-adjoint operators.

## 6. Sector-wise Galerkin convergence

### Theorem RH-R037-QW-SECTOR-GALERKIN-001

For each fixed \(\lambda>1\),

\[
\epsilon_{\pm,N}(\lambda)
\downarrow
\epsilon_\pm(\lambda)
\qquad
(N\to\infty).
\]

Consequently, with

\[
g_N(\lambda)
=
\epsilon_{-,N}(\lambda)
-
\epsilon_{+,N}(\lambda),
\]

and

\[
g(\lambda)
=
\epsilon_-(\lambda)
-
\epsilon_+(\lambda),
\]

one has

\[
g_N(\lambda)\to g(\lambda).
\]

### Proof

Because

\[
E_{N,\pm}\subset E_{N+1,\pm},
\]

the finite Rayleigh minima are nonincreasing:

\[
\epsilon_{\pm,N+1}
\le
\epsilon_{\pm,N}.
\]

Since every \(E_{N,\pm}\) is contained in the full parity form domain,

\[
\epsilon_{\pm,N}
\ge
\epsilon_\pm.
\]

Therefore \(\epsilon_{\pm,N}\) has a limit \(\ell_\pm\) with

\[
\ell_\pm\ge\epsilon_\pm.
\]

It remains to prove the reverse inequality.

Fix \(\delta>0\). By the definition of \(\epsilon_\pm\), choose nonzero

\[
f\in
\operatorname{Dom}(q_\lambda)\cap\mathcal H_{\lambda,\pm}
\]

such that

\[
\frac{q_\lambda(f,f)}{\|f\|^2}
<
\epsilon_\pm+\delta.
\]

By Proposition RH-P037-SECTOR-CORE, choose

\[
f_k\in E_\pm
\]

with

\[
f_k\to f
\]

in the form norm.

Form-norm convergence implies Hilbert-norm convergence and

\[
q_\lambda(f_k,f_k)\to q_\lambda(f,f).
\]

For sufficiently large \(k\), \(f_k\ne0\), and hence

\[
\frac{q_\lambda(f_k,f_k)}{\|f_k\|^2}
\to
\frac{q_\lambda(f,f)}{\|f\|^2}.
\]

Each \(f_k\) belongs to some finite \(E_{N_k,\pm}\). Therefore

\[
\ell_\pm
\le
\epsilon_{\pm,N_k}
\le
\frac{q_\lambda(f_k,f_k)}{\|f_k\|^2}.
\]

Passing to the limit gives

\[
\ell_\pm
\le
\frac{q_\lambda(f,f)}{\|f\|^2}
<
\epsilon_\pm+\delta.
\]

Since \(\delta>0\) is arbitrary,

\[
\ell_\pm\le\epsilon_\pm.
\]

Thus

\[
\ell_\pm=\epsilon_\pm.
\]

Subtracting the two convergent sequences gives

\[
g_N\to g.
\]

QED.

## 7. Certified asymptotic-gap criterion

### Corollary RH-P037-GAP-CERTIFICATE

For fixed \(\lambda\), if

\[
\liminf_{N\to\infty}g_N(\lambda)>0,
\]

then

\[
\epsilon_+(\lambda)<\epsilon_-(\lambda).
\]

### Proof

By the theorem,

\[
g_N(\lambda)\to g(\lambda).
\]

Therefore

\[
\liminf_N g_N(\lambda)=g(\lambda).
\]

A positive liminf implies \(g(\lambda)>0\), which is exactly the strict parity gap.

QED.

A stronger practical certificate is any pair \(N_0,\delta>0\) together with a rigorous tail bound proving

\[
g_N(\lambda)\ge\delta
\quad
\text{for all }N\ge N_0.
\]

## 8. What a finite negative gap means

A finite value

\[
g_N(\lambda)<0
\]

shows that the \(N\)-dimensional approximation has odd spectral bottom below the even one.

It does **not** by itself prove

\[
g(\lambda)<0,
\]

because both sector minima move downward with \(N\), and their difference need not be monotone.

However, once explicit convergence error bounds are available, a finite negative gap larger than the total error budget can become a certified counterexample to the full parity ordering.

Thus the correct next numerical protocol is two-sided:

- seek positive lower certificates for \(g\);
- seek negative upper certificates that would falsify the route.

## 9. Consequence for finite even-simplicity

At finite \(N\), source even-simplicity is equivalent to:

1. simplicity of \(\epsilon_{+,N}\);
2. \(g_N>0\).

The present theorem controls only the sector bottoms.

It does not imply that finite even-sector simplicity persists to the full operator.

A full proof of the source's first missing theorem therefore still requires:

- R036-B: \(g>0\);
- R036-A: simplicity of the full lowest even eigenvalue.

These are logically separate.

## 10. Computationally controlled next step

The protected R037 provider audit gives explicit formulas for every finite matrix entry:

\[
QW_\lambda^N
=
W_{0,2}
-
W_{\mathbb R}
-
\sum_p W_p.
\]

The exact finite matrices commute with parity and can be block-diagonalized before eigensolution.

A bounded evidence runner may therefore compute

\[
\epsilon_{+,N},
\quad
\epsilon_{-,N},
\quad
g_N,
\]

over a selected \((\lambda,N)\) grid with:

- high precision;
- independently checked matrix symmetry;
- parity-commutator residuals;
- quadrature / special-function error controls;
- cross-precision stability;
- interval or certified eigenvalue enclosures where feasible.

The runner remains evidence unless it also supplies a rigorous tail estimate.

## 11. Proof-obligation DAG

    source full form core E = union E_N
                 |
                 +--> J E_N = E_N
                 |
                 v
    RH-P037-01 parity projections contract form norm
                 |
                 v
    RH-P037-02 union E_{N,+/-} sector form cores
                 |
                 v
    RH-P037-03 finite sector minima decrease
                 |
                 v
    RH-P037-04 eps_{+/- ,N} -> eps_{+/-}
                 |
                 v
    RH-P037-05 g_N -> g
                 |
          +------+------+
          |             |
          v             v
    positive tail   negative tail
      certificate     certificate
          |             |
          v             v
      prove gap      falsify gap
          |
          v
       R036-B

Status:

- RH-P037-01 through RH-P037-05: PROVED.
- positive/negative certified tail estimate: OPEN.
- R036-B strict parity gap: OPEN.
- R036-A even-sector simplicity: OPEN.
- RH-T-000: OPEN.

## 12. False-proof firewall

Reject:

1. positivity of \(g_N\) for finitely many \(N\) as proof that \(g>0\);
2. visual convergence of \(g_N\) as a tail estimate;
3. a negative finite gap as a full counterexample without error control;
4. unrestricted finite minimum convergence substituted for sector-wise convergence without the parity-core proof;
5. finite even-simplicity substituted for full even-simplicity;
6. floating-point eigenvalues without matrix-entry error control as proof evidence;
7. any inference to determinant convergence or RH from this theorem alone.

## 13. Non-implications

This package does not:

- prove a strict parity gap;
- prove even-sector simplicity;
- provide a certified numerical tail bound;
- prove the source simple-even theorem;
- prove determinant convergence to \(\Xi\);
- prove RH;
- claim novelty or priority;
- render MATHCERT certification.

## 14. Terminal state

RH-R037_PROVED__PARITY_SECTOR_GALERKIN_CONVERGENCE_ESTABLISHED

The strict parity gap, even-sector simplicity, determinant convergence, and RH remain open.
