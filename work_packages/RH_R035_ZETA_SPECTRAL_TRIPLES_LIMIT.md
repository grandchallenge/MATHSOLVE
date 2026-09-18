# RH-R035-ZETA-SPECTRAL-TRIPLES-LIMIT-001 — Prime-built self-adjoint approximants and the exact convergence gate

- Campaign: RH-001
- Solve tracker: grandchallenge/MATHSOLVE#363
- Protected provider audit: grandchallenge/MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790
- Predecessor: RH-R034-RINDLER-PRIME-FIXED-DOMAIN-001
- Parent campaign route: RH-T-200 — Hilbert–Pólya sufficient-route contract
- Terminal target: RH-T-000 — OPEN
- Novelty / priority claim: none
- Certification status: not certified; MATHSOLVE theorem-development result only

## 1. Purpose

The RH-001 spectral route has now passed four earlier design gates:

1. exact raw-ordinate realization cannot use a bounded operator;
2. unboundedness alone does not supply point spectrum;
3. discreteness alone does not supply the Riemann–von Mangoldt counting law;
4. prime-labelled arithmetic structure can be specified without inserting the zero list.

The protected R035 source audit identifies the strongest current synthesis: the Connes–Consani–Moscovici Zeta Spectral Triples construction gives finite prime-built self-adjoint spectral approximants with exact real spectra and an exact regularized-determinant formula.

The missing step is convergence.

This package records the exact finite theorem boundary and isolates two sufficient convergence routes:

- a limiting-operator / spectral-convergence route;
- a locally uniform entire-determinant route.

The second route is logically sufficient for RH even without first constructing one limiting self-adjoint operator.

## 2. Imported finite source theorem

Fix \(\lambda>1\), set

\[
L=2\log\lambda,
\]

and let

\[
D_{\log}^{(\lambda)}
=
-i\,u\frac{\partial}{\partial u}
\]

act on

\[
L^2([\lambda^{-1},\lambda],d^*u),
\qquad
d^*u=\frac{du}{u},
\]

with periodic boundary conditions.

Let \(E_N\) be the span of the \(2N+1\) scaling eigenfunctions of smallest absolute eigenvalue, and let \(QW_\lambda^N\) be the semilocal Weil form restricted to \(E_N\).

Let \(\epsilon_N\) be its smallest eigenvalue and \(\xi\) a corresponding eigenvector.

Under the source assumptions that:

- \(\epsilon_N\) is simple;
- \(\xi\) is even under \(u\mapsto u^{-1}\);
- \(\delta_N(\xi)=1\);

the source defines a rank-one perturbation

\[
D_{\log}^{(\lambda,N)}
=
D_{\log}^{(\lambda)}
-
\left|D_{\log}^{(\lambda)}\xi\right\rangle
\left\langle\delta_N\right|.
\]

The protected provider audit records the source theorem:

1. \(D_{\log}^{(\lambda,N)}\) is self-adjoint on the source's finite/direct-sum Hilbert structure;
2. its regularized determinant is

\[
\det_{\mathrm{reg}}
\left(D_{\log}^{(\lambda,N)}-z\right)
=
-i\,\lambda^{-iz}\widehat{\xi}(z);
\]

3. \(\widehat{\xi}\) is entire;
4. every zero of \(\widehat{\xi}\) is real;
5. those zeros are exactly the finite approximant spectrum.

These are imported source facts, not re-proved here.

## 3. Noncircular arithmetic input

The semilocal Weil form contains the prime contribution

\[
-\sum_{1<n\le\lambda^2}
\Lambda(n)\langle f,T(n)f\rangle.
\]

Thus each finite approximant is specified from arithmetic data at scale \(\lambda\), including primes and prime powers below the scale cutoff.

No target zeta-zero ordinate is an adjustable domain parameter.

This repairs the exact defect isolated in RH-R034: at finite scale, the spectral problem is fixed before its eigenvalues are read.

## 4. What the finite theorem does not yet imply

The family

\[
D_{\log}^{(\lambda,N)}
\]

changes with \(\lambda\) and \(N\).

Finite self-adjointness does not imply:

- existence of a limiting operator;
- self-adjointness of such a limit;
- norm-, strong-, or strong-resolvent convergence;
- convergence of point spectra;
- convergence with the protected multiplicity convention;
- equality with the complete nontrivial-zeta ordinate multiset.

Likewise, high-precision numerical agreement of low eigenvalues with low zeta ordinates is route evidence only.

The source itself states that rigorous convergence would establish RH.

## 5. Exact determinant-convergence bridge

The finite determinant formula gives a second sufficient path that does not require constructing a limiting operator first.

### Proposition RH-P035-DETERMINANT-HURWITZ

Let \((F_j)\) be entire functions such that every zero of every \(F_j\) is real. Suppose

\[
F_j \longrightarrow \Xi
\]

locally uniformly on \(\mathbb C\), where \(\Xi\) is the classical nonzero Riemann \(\Xi\)-function.

Then every zero of \(\Xi\) is real.

Consequently, the Riemann Hypothesis holds.

### Proof

Assume for contradiction that

\[
\Xi(z_0)=0
\]

for some \(z_0\notin\mathbb R\).

Choose \(r>0\) so small that the closed disk

\[
\overline{B(z_0,r)}
\]

is disjoint from the real axis and its boundary contains no zero of \(\Xi\).

Because \(F_j\to\Xi\) locally uniformly, for all sufficiently large \(j\),

\[
\sup_{z\in\partial B(z_0,r)}
|F_j(z)-\Xi(z)|
<
\inf_{z\in\partial B(z_0,r)}
|\Xi(z)|.
\]

Rouché's theorem implies that \(F_j\) and \(\Xi\) have the same number of zeros in \(B(z_0,r)\), counted with multiplicity.

Since \(\Xi\) has at least one zero there, \(F_j\) must have a zero there for all sufficiently large \(j\).

But \(B(z_0,r)\cap\mathbb R=\varnothing\), contradicting the hypothesis that every zero of \(F_j\) is real.

Therefore all zeros of \(\Xi\) are real.

Under the standard \(\Xi\)-normalization, this is equivalent to RH.

QED.

### Campaign consequence

A proof of locally uniform convergence of suitably normalized finite Zeta Spectral Triple determinants to \(\Xi\) is by itself a complete sufficient bridge to RH.

It is not necessary first to prove convergence to one self-adjoint limiting operator.

This does not weaken the source's open convergence burden; it identifies the weakest exact output sufficient for the terminal claim.

## 6. Operator-limit route

A separate sufficient route remains available.

If one proves that a cofinal family of the finite self-adjoint operators converges in a topology strong enough to yield a self-adjoint limit \(D_\infty\), and proves spectral convergence with no missing or extraneous points such that

\[
\sigma_{\mathrm{pt}}(D_\infty)
=
\{\gamma:\zeta(\tfrac12+i\gamma)=0\},
\]

with the protected multiplicity convention, then the Hilbert–Pólya route closes.

This route requires substantially more operator-theoretic structure than the determinant bridge.

The campaign therefore treats determinant convergence as the smaller sufficient target unless source analysis proves it is inaccessible.

## 7. Source-named missing steps

The protected R035 audit binds two explicit missing steps from the source.

### 7.1 Simple-even ground state

For the full semilocal Weil form \(QW_\lambda\), prove that its smallest eigenvalue:

- is simple;
- has an even eigenvector \(\xi_\lambda\).

The source has existence of a lowest eigenvalue, but not the required simple-even theorem.

### 7.2 Approximation strong enough for zero convergence

The source constructs an approximating vector \(k_\lambda\).

One must prove sufficiently strong control of

\[
k_\lambda-\xi_\lambda
\]

to transfer that approximation to the entire transforms / determinants and ultimately to their zeros.

Numerical eigenvector or zero proximity does not discharge this obligation.

## 8. Proof-obligation DAG

    RH-P035-01  bind prime-built finite Weil-form approximants
          |
          v
    RH-P035-02  source simple-even hypothesis at finite scale
          |
          v
    RH-P035-03  finite self-adjointness + exact determinant
          |
          v
    RH-P035-04  all finite determinant zeros real
          |
          +---------------------------+
          |                           |
          v                           v
    operator convergence        determinant convergence
          |                           |
          v                           v
    exact limiting spectrum     local uniform F_j -> Xi
          |                           |
          |                    RH-P035-05 Hurwitz/Rouché
          |                           |
          +-------------+-------------+
                        v
                      RH-T-000

Current status:

- RH-P035-01 through RH-P035-04: imported from the protected source audit under the stated finite hypotheses.
- RH-P035-05: proved in Section 5.
- operator convergence: OPEN.
- determinant convergence: OPEN.
- source simple-even full-form theorem: OPEN.
- source \(k_\lambda\)-approximation theorem: OPEN.
- RH-T-000: OPEN.

## 9. False-proof firewall

Reject:

1. finite self-adjointness \(\Rightarrow\) limiting self-adjointness;
2. many accurate low eigenvalues \(\Rightarrow\) complete spectral equality;
3. pointwise determinant convergence \(\Rightarrow\) zero convergence;
4. locally uniform convergence without controlling the normalization;
5. real zeros of all approximants \(\Rightarrow\) real zeros of an unspecified limit;
6. suppressing the simple-even hypothesis used by the finite theorem;
7. replacing proof of \(k_\lambda\to\xi_\lambda\) with numerical overlap;
8. treating a varying family as one fixed operator without a limit theorem;
9. claiming RH before either a sufficient determinant-convergence theorem or a complete operator/spectral convergence theorem is proved.

## 10. Non-implications

This package does not:

- prove RH;
- prove determinant convergence to \(\Xi\);
- prove existence of a limiting self-adjoint operator;
- prove the full simple-even theorem for \(QW_\lambda\);
- prove the required \(k_\lambda\)-to-\(\xi_\lambda\) estimate;
- certify the imported finite theorem;
- claim novelty or priority for the source construction or the standard Hurwitz/Rouché bridge.

## 11. Next smallest safe target

The smaller source-named obstruction should be attacked first:

\[
\boxed{\text{simple-even lowest eigenspace of }QW_\lambda}
\]

before the global convergence problem.

The protected source records inversion symmetry of the Weil form. Therefore the first reduction to establish is whether the associated self-adjoint operator commutes with inversion and hence decomposes into even and odd reducing subspaces.

If so, the simple-even ground-state problem can be sharpened to a parity-gap problem:

- simplicity of the lowest even eigenvalue;
- strict inequality between the lowest even and lowest odd eigenvalues.

That reduction should be source-audited before use.

## 12. Terminal state

RH-R035_PROVED__PRIME_BUILT_SELFADJOINT_APPROXIMANTS_CONFIRMED__EXACT_CONVERGENCE_GATE_ISOLATED

RH-T-000 remains open.
