# RH-R036-QW-PARITY-GAP-REDUCTION-001 — Simple-even ground state as a parity-gap theorem

- Campaign: RH-001
- Solve tracker: grandchallenge/MATHSOLVE#366
- Protected provider audit: grandchallenge/MATHFORGE@51042c94185cc9db1fa457ae40f26276747a0a4d
- Predecessor: RH-R035-ZETA-SPECTRAL-TRIPLES-LIMIT-001
- Parent source route: Connes–Consani–Moscovici, Zeta Spectral Triples
- Terminal target: RH-T-000 — OPEN
- Novelty / priority claim: none
- Certification status: not certified; MATHSOLVE theorem-development result only

## 1. Purpose

RH-R035 isolated the first source-named missing theorem in the Zeta Spectral Triples route:

> prove that the smallest eigenvalue of the full semilocal Weil form \(QW_\lambda\) is simple and has an even eigenvector.

The protected R036 source audit establishes the exact substrate:

- inversion symmetry of the Weil form under \(u\mapsto u^{-1}\);
- a canonical lower-bounded self-adjoint operator \(A_\lambda\) representing the closed form;
- discrete lower-bounded spectrum of \(A_\lambda\).

This package proves that the source's simple-even condition is equivalent to a symmetry-reduced parity-gap problem.

It does **not** prove the parity gap itself.

## 2. Source inputs

Fix \(\lambda>1\) and set

\[
\mathcal H_\lambda
=
L^2([\lambda^{-1},\lambda],d^*u).
\]

Let \(q_\lambda\) denote the closed lower-bounded sesquilinear form associated with \(QW_\lambda\), and let

\[
A_\lambda
\]

be its canonical self-adjoint operator.

The source proves that \(A_\lambda\) is lower bounded and has discrete spectrum.

Define the inversion involution

\[
(Jf)(u)=f(u^{-1}).
\]

Because the interval and Haar measure \(d^*u=du/u\) are inversion invariant,

\[
J^*=J,\qquad J^2=I.
\]

The protected source audit binds inversion invariance of the form:

\[
J\operatorname{Dom}(q_\lambda)
=
\operatorname{Dom}(q_\lambda),
\]

and

\[
q_\lambda(Jf,Jg)
=
q_\lambda(f,g).
\]

These are the only source-specific symmetry inputs used below.

## 3. Form symmetry implies operator commutation

### Proposition RH-P036-COMMUTE

The inversion involution preserves the operator domain and commutes with the associated self-adjoint operator:

\[
J\operatorname{Dom}(A_\lambda)
=
\operatorname{Dom}(A_\lambda),
\]

\[
A_\lambda Jf
=
J A_\lambda f
\qquad
(f\in\operatorname{Dom}(A_\lambda)).
\]

### Proof

For a closed lower-bounded form \(q_\lambda\), the associated operator is characterized as follows.

A vector \(f\in\operatorname{Dom}(q_\lambda)\) belongs to \(\operatorname{Dom}(A_\lambda)\) exactly when there exists \(h\in\mathcal H_\lambda\) such that

\[
q_\lambda(f,g)
=
\langle h,g\rangle
\]

for every \(g\in\operatorname{Dom}(q_\lambda)\). In that case \(A_\lambda f=h\).

Take \(f\in\operatorname{Dom}(A_\lambda)\) and \(g\in\operatorname{Dom}(q_\lambda)\).

Using \(J^2=I\) and form invariance,

\[
q_\lambda(Jf,g)
=
q_\lambda(Jf,J(Jg))
=
q_\lambda(f,Jg).
\]

Since \(f\in\operatorname{Dom}(A_\lambda)\),

\[
q_\lambda(f,Jg)
=
\langle A_\lambda f,Jg\rangle.
\]

Because \(J\) is self-adjoint,

\[
\langle A_\lambda f,Jg\rangle
=
\langle J A_\lambda f,g\rangle.
\]

Thus \(Jf\in\operatorname{Dom}(A_\lambda)\) and

\[
A_\lambda Jf
=
J A_\lambda f.
\]

Applying the same argument to \(Jf\) and using \(J^2=I\) gives equality of the domains rather than one-sided inclusion.

QED.

## 4. Even/odd reducing decomposition

Define

\[
\mathcal H_{\lambda,+}
=
\ker(J-I),
\qquad
\mathcal H_{\lambda,-}
=
\ker(J+I).
\]

Since \(J\) is a self-adjoint unitary involution,

\[
\mathcal H_\lambda
=
\mathcal H_{\lambda,+}
\oplus
\mathcal H_{\lambda,-}
\]

orthogonally.

By Proposition RH-P036-COMMUTE, both subspaces reduce \(A_\lambda\).

Therefore

\[
A_\lambda
=
A_{\lambda,+}
\oplus
A_{\lambda,-},
\]

where each parity restriction

\[
A_{\lambda,\pm}
=
A_\lambda|_{\mathcal H_{\lambda,\pm}}
\]

is self-adjoint on its natural restricted domain.

Because \(A_\lambda\) has discrete lower-bounded spectrum, each nonzero reducing parity sector has discrete lower-bounded spectrum.

The even and odd sectors are both nonzero on the symmetric multiplicative interval.

Define

\[
\epsilon_+(\lambda)
=
\min \sigma(A_{\lambda,+}),
\]

\[
\epsilon_-(\lambda)
=
\min \sigma(A_{\lambda,-}).
\]

Both minima are eigenvalues.

## 5. Exact parity-gap equivalence

### Theorem RH-R036-QW-PARITY-GAP-REDUCTION-001

For fixed \(\lambda>1\), the following are equivalent.

### Condition A — source simple-even ground state

The lowest eigenvalue of \(A_\lambda\) is simple and its eigenvector is even.

### Condition B — symmetry-reduced pair

1. the lowest eigenvalue \(\epsilon_+(\lambda)\) of the even restriction \(A_{\lambda,+}\) is simple; and
2. the strict parity gap holds:

\[
\epsilon_+(\lambda)
<
\epsilon_-(\lambda).
\]

### Proof

#### A implies B

Assume the global lowest eigenvalue

\[
\epsilon(\lambda)=\min\sigma(A_\lambda)
\]

is simple and has an even eigenvector.

Because that eigenvector lies in \(\mathcal H_{\lambda,+}\),

\[
\epsilon(\lambda)=\epsilon_+(\lambda).
\]

Its global simplicity implies simplicity as an eigenvalue of the even restriction.

Since \(\epsilon(\lambda)\) is the global spectral minimum,

\[
\epsilon_-(\lambda)
\ge
\epsilon_+(\lambda).
\]

If equality held, discreteness of the odd restriction would give a nonzero odd eigenvector at the same eigenvalue.

The even and odd eigenvectors are orthogonal and linearly independent, contradicting simplicity of the global ground eigenspace.

Therefore

\[
\epsilon_+(\lambda)
<
\epsilon_-(\lambda).
\]

#### B implies A

Assume \(\epsilon_+(\lambda)\) is simple and

\[
\epsilon_+(\lambda)
<
\epsilon_-(\lambda).
\]

Because

\[
A_\lambda
=
A_{\lambda,+}\oplus A_{\lambda,-},
\]

the bottom of the full spectrum is

\[
\min\{\epsilon_+(\lambda),\epsilon_-(\lambda)\}
=
\epsilon_+(\lambda).
\]

The strict gap excludes odd eigenvectors at this eigenvalue.

Simplicity within the even sector therefore implies global simplicity.

Its eigenvector belongs to the even subspace by construction.

Hence the global lowest eigenvalue is simple and even.

QED.

## 6. Exact decomposition of the source's first missing step

The source's first open theorem now splits into two independent mathematical obligations.

### R036-A — even-sector simplicity

Prove that

\[
\dim
\ker
\left(
A_{\lambda,+}
-
\epsilon_+(\lambda)I
\right)
=
1.
\]

### R036-B — strict parity gap

Prove

\[
\epsilon_+(\lambda)
<
\epsilon_-(\lambda).
\]

The original source condition holds exactly when both R036-A and R036-B hold.

This is strictly sharper than the phrase "simple-even ground state" because a failure can now be localized:

- multiplicity failure inside the even sector;
- parity-order failure between sectors.

## 7. Variational formulation

By the min–max principle,

\[
\epsilon_\pm(\lambda)
=
\inf_{
0\ne f\in
\operatorname{Dom}(q_\lambda)\cap
\mathcal H_{\lambda,\pm}
}
\frac{q_\lambda(f,f)}{\|f\|^2}.
\]

Therefore the parity-gap target is equivalently

\[
\inf_{0\ne f\in\operatorname{Dom}(q_\lambda)\cap\mathcal H_{\lambda,+}}
\frac{q_\lambda(f,f)}{\|f\|^2}
<
\inf_{0\ne g\in\operatorname{Dom}(q_\lambda)\cap\mathcal H_{\lambda,-}}
\frac{q_\lambda(g,g)}{\|g\|^2}.
\]

This form makes the next proof search concrete: it asks for a strict comparison of two constrained Rayleigh quotients.

## 8. Finite truncation diagnostic

The source's finite spaces \(E_N\) are symmetric under inversion.

The finite matrix of \(QW_\lambda^N\) can therefore be decomposed into even and odd blocks.

Define finite bottoms

\[
\epsilon_{+,N}(\lambda),
\qquad
\epsilon_{-,N}(\lambda).
\]

A certified finite inequality

\[
\epsilon_{+,N}
<
\epsilon_{-,N}
\]

is evidence for the mechanism but is not the full R036-B theorem.

To promote finite results to the full parity gap one would need quantitative control of convergence of the parity-sector minima.

The source proves convergence of the unrestricted finite minimum to the full lower bound; sector-wise convergence should be established rather than assumed.

## 9. Proof-obligation DAG

    source inversion symmetry of q_lambda
                |
                v
    RH-P036-01 closed-form representation
                |
                v
    RH-P036-02 A_lambda J = J A_lambda
                |
                v
    RH-P036-03 H = H_+ direct-sum H_-
                |
                v
    RH-P036-04 A = A_+ direct-sum A_-
                |
          +-----+-----+
          |           |
          v           v
    even bottom   odd bottom
      epsilon+     epsilon-
          |           |
          +-----+-----+
                v
    RH-P036-05 simple-even equivalence
                |
          +-----+-----+
          |           |
          v           v
       R036-A       R036-B
       OPEN         OPEN

Status:

- RH-P036-01: imported source theorem.
- RH-P036-02 through RH-P036-05: proved in this package.
- R036-A: OPEN.
- R036-B: OPEN.
- RH-T-000: OPEN.

## 10. False-proof firewall

Reject:

1. inversion symmetry of a formal expression without domain invariance;
2. matrix symmetry at finite \(N\) substituted for commutation of the full operator;
3. an even numerical ground vector substituted for an exact even eigenspace theorem;
4. a positive finite parity gap substituted for the full parity gap;
5. global simplicity inferred only from a strict parity gap without proving even-sector simplicity;
6. even-sector simplicity inferred only from a positive parity gap;
7. determinant convergence or RH inferred from the reduction theorem itself.

## 11. Non-implications

This package does not:

- prove \(\epsilon_+<\epsilon_-\);
- prove even-sector simplicity;
- prove the source's first missing theorem;
- prove the \(k_\lambda\)-approximation theorem;
- prove determinant convergence to \(\Xi\);
- prove RH;
- claim novelty or priority;
- render a MATHCERT disposition.

## 12. Next smallest safe target

The next mathematical target should be R036-B first:

\[
\boxed{\epsilon_+(\lambda)<\epsilon_-(\lambda)}
\]

because parity ordering is a binary structural question and can be attacked variationally.

Before attempting a general all-\(\lambda\) proof, the campaign may use finite parity blocks as falsifiers and mechanism probes, provided any numerical claims are clearly separated from proof.

A useful next tranche should:

1. derive the exact even/odd finite matrices from the source formula for \(QW_\lambda^N\);
2. establish sector-wise finite-to-full variational convergence;
3. test whether a monotone or comparison principle can force the strict gap;
4. stop immediately if a certified counterexample to the parity ordering is found for any \(\lambda\).

## 13. Terminal state

RH-R036_PROVED__SIMPLE_EVEN_REDUCED_TO_EVEN_SIMPLICITY_PLUS_PARITY_GAP

The parity gap and RH remain open.
