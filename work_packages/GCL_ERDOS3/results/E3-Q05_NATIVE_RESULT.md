# E3-Q05 — large-spectrum bound and finite linear-witness no-go

Disposition: **PROVED_NATIVE_PARSEVAL_AMPLIFICATION_REQUIREMENT**.

This is native GCL work. It composes the strengthened E3-Q04 aligned Fourier witness with Parseval and does not use any external theorem.

## Strongest exact statement

Let
\[
G=\mathbb Z/P\mathbb Z,\qquad P>8N,
\]
be the cyclic embedding used by E3-Q02/Q04, and let
\[
g_j=1_{C_j}-\rho_j
\]
be a translated balanced indicator of physical fibre \(B_j\).

Define the Q04 linear-witness threshold
\[
\lambda_\beta
:=
\frac{\beta^3}{20\cdot16^3}.
\]

For each physical fibre define its large spectrum
\[
\operatorname{Spec}_j(\lambda_\beta)
=
\{\xi\in G\setminus\{0\}:|\widehat g_j(\xi)|\ge\lambda_\beta\}.
\]

Then:

\[
\boxed{
|\operatorname{Spec}_j(\lambda_\beta)|
\le
\frac{1}{4\lambda_\beta^2}
=
100\cdot16^6\,\beta^{-6}.
}
\]

Moreover, whenever an adjacent Q04 \(0011\) family lies in its **linear witness alternative**, the corresponding adjacent pair \((A,B)\) satisfies one of the following four exact harmonic clauses for some nonzero \(r\in G\):

\[
\{r,2r\}\subseteq\operatorname{Spec}_A,\qquad
r\in\operatorname{Spec}_B;
\]

\[
\{2r,3r\}\subseteq\operatorname{Spec}_A,\qquad
r\in\operatorname{Spec}_B;
\]

\[
r\in\operatorname{Spec}_A,\qquad
\{2r,3r\}\subseteq\operatorname{Spec}_B;
\]

or

\[
r\in\operatorname{Spec}_A,\qquad
\{r,2r\}\subseteq\operatorname{Spec}_B.
\]

Signs from Q04 may be suppressed because every balanced indicator is real-valued and therefore
\[
|\widehat g(-\xi)|=|\widehat g(\xi)|.
\]

Consequently:

> **Any strategy that tries to contradict Parseval using only Q04 linear witnesses must force more than**
> \[
> 100\cdot16^6\,\beta^{-6}
> \]
> **distinct large frequencies on at least one physical fibre.**

A fixed bounded collection of carry-family witness statements cannot do this uniformly as \(\beta\to0\).

In particular, the three adjacent \(0011\) families \(F_1,F_4,F_7\), even when all three fall in the Q04 linear regime, have no abstract one-scale large-spectrum incompatibility. The constant spectra
\[
S_0=S_1=S_2=S_3=\{\pm1,\pm2,\pm3\}
\]
satisfy the harmonic support requirements of all three adjacent pairs by taking \(r=1\).

This does **not** construct actual near-extremal fibres with those spectra. It proves only that support-counting and Parseval, at one fixed scale and with finitely many witness clauses, cannot supply the required deletion theorem.

## Proof

### 1. Parseval capacity of one physical fibre

For normalized Fourier transform
\[
\widehat g(\xi)=\mathbb E_x g(x)e_P(-\xi x),
\]
Parseval gives
\[
\sum_{\xi\in G}|\widehat g(\xi)|^2
=
\mathbb E_x|g(x)|^2.
\]

For \(g=1_C-\rho\),
\[
\mathbb E|g|^2
=
\rho(1-\rho)
\le \frac14.
\]

Therefore, if \(S=\{\xi:|\widehat g(\xi)|\ge\lambda\}\),
\[
|S|\lambda^2
\le
\sum_{\xi\in S}|\widehat g(\xi)|^2
\le
\frac14,
\]
so
\[
|S|\le\frac{1}{4\lambda^2}.
\]

Substituting
\[
\lambda=\lambda_\beta
=
\frac{\beta^3}{20\cdot16^3}
\]
gives
\[
|\operatorname{Spec}_j(\lambda_\beta)|
\le
\frac{20^2 16^6}{4}\beta^{-6}
=
100\cdot16^6\,\beta^{-6}.
\]

### 2. Exact harmonic clauses from Q04

Q04 proves that in its triple/Fourier branch there is one nonzero common frequency parameter \(r\) and one of the four triple-position patterns

\[
\{0,1,2\},\quad
\{0,1,3\},\quad
\{0,2,3\},\quad
\{1,2,3\}.
\]

For an adjacent \(0011\) physical pattern \((A,A,B,B)\), Q04's multiplier table is, up to sign,

\[
(r,2r,r),\quad
(2r,3r,r),\quad
(r,3r,2r),\quad
(r,2r,r).
\]

The repeated physical fibre therefore contributes two linked large modes and the other contributes one. Using real-valued symmetry under sign gives exactly the four clauses stated above.

### 3. Why fixed family counting is insufficient

Suppose a proof uses only the fact that each linear witness contributes one or two frequencies of magnitude at least \(\lambda_\beta\), and seeks a contradiction solely because too many **distinct** such frequencies appear on one physical fibre.

Parseval allows up to
\[
100\cdot16^6\,\beta^{-6}
\]
such frequencies.

As \(\beta\to0\), this capacity diverges polynomially. Any fixed set of \(O(1)\) carry-family clauses contributes only \(O(1)\) witness modes unless an additional amplification theorem produces many distinct translated/scale witnesses.

Therefore no fixed one-scale support-counting argument can close the desired asymptotic theorem.

### 4. Explicit abstract compatibility of the adjacent chain

Take
\[
S_j=\{\pm1,\pm2,\pm3\}
\qquad(j=0,1,2,3).
\]

For every adjacent pair choose \(r=1\). The first harmonic clause
\[
\{r,2r\}\subseteq S_j,\qquad r\in S_{j+1}
\]
holds.

Since \(P>8N\) and the Q03/Q04 regime has \(N\ge4\), the modes \(1,2,3\) are nonzero and distinct modulo \(P\).

Hence there is no contradiction at the level of abstract large-spectrum support sets for the three adjacent families.

## What this changes

Q04 reduced the linear branch to explicit aligned Fourier witnesses of size \(c\beta^3\).

Q05 now shows exactly what is still missing in that branch:

\[
\text{one aligned witness}
\not\Rightarrow
\text{mass loss}.
\]

A Parseval-only closure requires a theorem producing at least polynomially many **distinct** witnesses:

\[
\Omega(\beta^{-6})
\]

on one physical fibre, up to the explicit constant above.

Therefore the next useful linear-lane statement is an amplification theorem, not another one-scale Fourier extraction.

## Remaining alternatives

A successful proof may still avoid this \(\beta^{-6}\) multiplicity burden by using information stronger than large-spectrum cardinality, for example:

1. coefficient **phases** and the exact harmonic relations among \(r,2r,3r\);
2. incompatibility between the witnesses obtained at many translated locations;
3. near-extremal local 4-AP-freeness to forbid certain harmonic spectra;
4. the Q04 **joint fourfold** branch directly, before reduction to separate scalar witnesses;
5. positive-density amplification of the finite L01 motif clauses.

## First defect

The live linear residual is now:

> **E3-B-LINEAR-WITNESS-AMPLIFICATION.**  
> Starting from Q04's aligned coefficient threshold
> \[
> \lambda_\beta=\beta^3/(20\cdot16^3),
> \]
> prove that near-extremality plus the carry system forces either:
> - more than \(100\cdot16^6\beta^{-6}\) distinct \(\lambda_\beta\)-large frequencies on one physical fibre; or
> - a stronger phase/structure incompatibility that yields the required deletion cost without a Parseval cardinality contradiction.

The genuinely quadratic/fourfold branch remains separate.

## Frontier effect

- \`E3-Q4-DENSITY-LOSS\` remains **OPEN**.
- \`E3-B-FOUR-FIBRE-DEFICIT\` remains **OPEN_NATIVE_SUBTARGET**.
- \`E3-B-ADJACENT-WITNESS-DICHOTOMY\` remains **PROVED_NATIVE**.
- The one-scale finite-family Fourier-counting route is **PROVED INSUFFICIENT**.
- The joint-witness residual is sharpened to:
  1. linear-witness amplification/phase incompatibility; or
  2. direct joint-fourfold incompatibility.
- No parent frontier or gluing-radius candidate is promoted.
