# RH-R056-CANONICAL-DETERMINANT-NORMALIZATION-001

Campaign: RH-001

Route: Forward Route C, obligation C0

Status: ADMISSION_CANDIDATE

Solve coordination:
- route tracker: grandchallenge/MATHSOLVE#414
- bounded tranche: grandchallenge/MATHSOLVE#702

Protected Solve base:
grandchallenge/MATHSOLVE@027ae0cd4b2ea5942f70215147220e536e8a6af7

Protected provider inputs:
- grandchallenge/MATHFORGE@a900e5170c6d77a9e557b6159cf5feb40bcee222:
  reports/discovery/rh_001/rh_r056_determinant_normalization.md
- grandchallenge/MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790:
  reports/discovery/rh_001/rh_r035_zeta_spectral_triples_limit.md

No determinant-convergence / global simple-evenness / RH / novelty / priority /
publication-readiness / certification claim.

## 1. Purpose

The protected finite CCM theorem gives, under its finite simple-even hypotheses,

\[
G_{\lambda,N}(z)
:=
\det_{\rm reg}(D_{\log}^{(\lambda,N)}-z)
=
-i\,\lambda^{-iz}\,\widehat{\xi}_{\lambda,N}(z),
\]

with

\[
\delta_N(\xi_{\lambda,N})=1.
\]

The protected provider audit fixes the source spectral-cut convention, the
factor \(-i\), the phase \(\lambda^{-iz}\), and the Fourier/Mellin convention.
It also records that the source does not supply one canonical scalar
normalization toward the classical \(\Xi\)-function.

This package discharges Route C obligation C0 by defining one exact
campaign normalization and proving:

1. it is well-defined on every admitted finite pair \((\lambda,N)\);
2. it is entire and even;
3. it preserves exactly the zero multiset of the finite determinant;
4. it is uniquely characterized inside a declared affine-exponential gauge
   class by evenness and one fixed nonreal classical anchor;
5. the anchor choice is classical and independent of RH;
6. the theorem fixes only normalization and supplies no convergence.

## 2. Admitted finite domain

Fix \(\lambda>1\) and \(N\) satisfying the hypotheses of the protected CCM
finite theorem:

1. the smallest eigenvalue of \(QW_\lambda^N\) is simple;
2. the corresponding eigenvector \(\xi_{\lambda,N}\) is even under
   \(u\mapsto u^{-1}\);
3. its source scale is fixed by \(\delta_N(\xi_{\lambda,N})=1\).

Only on this admitted finite domain do we use the source conclusions that:

- \(G_{\lambda,N}\) is entire;
- \(\widehat{\xi}_{\lambda,N}\) is entire and even;
- every zero of \(\widehat{\xi}_{\lambda,N}\), equivalently of
  \(G_{\lambda,N}\), is real.

No statement below silently extends those source conclusions beyond this
finite hypothesis class.

## 3. Source-fixed phase removal

The protected R056 provider packet gives exactly

\[
G_{\lambda,N}(z)
=
-i\,\lambda^{-iz}\widehat{\xi}_{\lambda,N}(z).
\]

Since \(\lambda>1\),

\[
z\longmapsto \lambda^{iz}
=
\exp(iz\log\lambda)
\]

is an entire zero-free function. Therefore

\[
P_{\lambda,N}(z)
:=
i\,\lambda^{iz}G_{\lambda,N}(z)
=
\widehat{\xi}_{\lambda,N}(z)
\]

is entire and even, and has exactly the same zeros with the same
multiplicities as \(G_{\lambda,N}\).

This phase removal is source-derived. The scalar normalization introduced
below is Solve-native.

## 4. A classical nonzero anchor

The protected MATHFORGE R056 addendum binds the classical identity

\[
\Xi(z)=\xi\!\left(\frac12+iz\right)
\]

in the CCM convention and, from the standard completed-\(\xi\) formula,
proves

\[
\xi(0)=\frac12.
\]

Set

\[
z_*:=\frac{i}{2}.
\]

Then

\[
\Xi(z_*)
=
\xi(0)
=
\frac12
\neq0.
\]

This anchor is nonreal and its nonvanishing is classical; it does not assume
RH.

Because every zero of \(\widehat{\xi}_{\lambda,N}\) is real on the admitted
finite domain,

\[
\widehat{\xi}_{\lambda,N}(z_*)\neq0.
\]

Equivalently,

\[
\lambda^{iz_*}G_{\lambda,N}(z_*)\neq0.
\]

Hence the normalization below is well-defined for every admitted finite pair.

## 5. Canonical finite normalized determinant

Define

\[
\boxed{
F_{\lambda,N}(z)
:=
\frac{\Xi(z_*)}{\widehat{\xi}_{\lambda,N}(z_*)}
\widehat{\xi}_{\lambda,N}(z)
}
\]

with \(z_*=i/2\) and \(\Xi(z_*)=1/2\).

Equivalently, directly from the raw determinant,

\[
\boxed{
F_{\lambda,N}(z)
=
\Xi(z_*)
\frac{\lambda^{iz}G_{\lambda,N}(z)}
     {\lambda^{iz_*}G_{\lambda,N}(z_*)}.
}
\]

This second formula is the campaign interface: it defines the normalized
finite entire function entirely from the raw source determinant, the
source-fixed phase, and one fixed classical anchor.

The definition is insensitive to any hypothetical nonzero scalar rescaling
of the raw determinant because the same scalar cancels between numerator and
denominator. The actual CCM determinant is already source-normalized, so this
invariance is a structural property, not a replacement for
\(\delta_N(\xi)=1\).

## 6. Basic properties

### Lemma 6.1 — Entirety and evenness

\(F_{\lambda,N}\) is entire and even.

Proof. It is a nonzero constant multiple of the entire even function
\(\widehat{\xi}_{\lambda,N}\). Therefore

\[
F_{\lambda,N}(-z)=F_{\lambda,N}(z)
\]

for all \(z\in\mathbb C\). \(\square\)

### Lemma 6.2 — Anchor normalization

\[
\boxed{
F_{\lambda,N}(i/2)=\frac12=\Xi(i/2).
}
\]

Proof. Substitute \(z=z_*\) in the defining ratio. \(\square\)

### Lemma 6.3 — Exact zero preservation

\(F_{\lambda,N}\), \(\widehat{\xi}_{\lambda,N}\), and
\(G_{\lambda,N}\) have exactly the same zeros with the same multiplicities.

Proof. The multipliers relating the three functions are nonzero constants
and zero-free exponential functions. Such multipliers neither create nor
remove zeros and do not change multiplicity. \(\square\)

Consequently every zero of \(F_{\lambda,N}\) is real on the admitted finite
domain.

## 7. Uniqueness in the affine-exponential gauge class

The source's Section 7 language permits multiplication by suitable
exponential/scalar factors but does not canonically select them. We therefore
state the exact class in which the campaign normalization is unique.

Fix an admitted pair \((\lambda,N)\). Consider functions of the form

\[
H(z)
=
C\,e^{ibz}G_{\lambda,N}(z),
\qquad
C\in\mathbb C^\times,\quad b\in\mathbb C.
\]

Assume:

1. \(H\) is even;
2. \(H(z_*)=\Xi(z_*)=1/2\).

### Theorem 7.1 — Unique even anchored gauge

Under these assumptions,

\[
\boxed{
b=\log\lambda
}
\]

and

\[
\boxed{
H(z)=F_{\lambda,N}(z).
}
\]

Proof. Using the raw determinant formula and evenness of
\(\widehat{\xi}_{\lambda,N}\),

\[
\frac{H(-z)}{H(z)}
=
\exp\!\left(2iz(\log\lambda-b)\right)
\]

at every \(z\) where \(G_{\lambda,N}(z)\neq0\). Both sides extend
meromorphically, while the exponential is entire. Since \(H\) is even,
the exponential equals one on the nonempty open set where
\(G_{\lambda,N}\neq0\), and hence everywhere by analyticity. Therefore

\[
\exp\!\left(2iz(\log\lambda-b)\right)\equiv1.
\]

An exponential \(\exp(cz)\) is identically one on \(\mathbb C\) only when
\(c=0\). Hence \(b=\log\lambda\).

Thus

\[
H(z)
=
-iC\,\widehat{\xi}_{\lambda,N}(z).
\]

Since \(\widehat{\xi}_{\lambda,N}(z_*)\neq0\), the anchor condition fixes
the remaining scalar uniquely:

\[
-iC\,\widehat{\xi}_{\lambda,N}(z_*)
=
\Xi(z_*).
\]

Therefore

\[
H(z)
=
\frac{\Xi(z_*)}{\widehat{\xi}_{\lambda,N}(z_*)}
\widehat{\xi}_{\lambda,N}(z)
=
F_{\lambda,N}(z).
\]

\(\square\)

The theorem deliberately allows \(C\in\mathbb C^\times\). Restricting the
residual scalar to positive reals would require an additional phase theorem
that is neither needed nor source-provided.

## 8. The normalization theorem

### RH-R056-CANONICAL-DETERMINANT-NORMALIZATION-001

For every finite pair \((\lambda,N)\) satisfying the protected CCM
simple-even and \(\delta_N\)-normalization hypotheses, define

\[
F_{\lambda,N}(z)
=
\frac12
\frac{\lambda^{iz}G_{\lambda,N}(z)}
     {\lambda^{-1/2}G_{\lambda,N}(i/2)},
\]

where \(G_{\lambda,N}\) is the source regularized determinant.

Here we used

\[
\lambda^{i(i/2)}=\lambda^{-1/2}.
\]

Then:

1. \(F_{\lambda,N}\) is entire and even;
2. \(F_{\lambda,N}(i/2)=1/2=\Xi(i/2)\);
3. every zero of \(F_{\lambda,N}\) is real;
4. \(F_{\lambda,N}\) has exactly the same zero multiset as the raw finite
   determinant;
5. among all functions
   \(C e^{ibz}G_{\lambda,N}(z)\) with
   \(C\in\mathbb C^\times\), \(b\in\mathbb C\), it is the unique one that is
   even and takes the value \(1/2\) at \(i/2\).

This defines one branch-independent campaign normalization for all admitted
finite CCM determinant approximants.

## 9. Interaction with later Route C obligations

R056 discharges only C0.

It gives later tranches a fixed object

\[
F_{\lambda,N}
\]

whose normalization is no longer ambiguous.

It does not discharge:

- C1: a cofinal \((\lambda,N)\) schedule;
- C3: a sufficiently strong \(k_\lambda\to\xi_\lambda\) theorem;
- C4: local boundedness / normal-family control;
- C5: identification of subsequential limits;
- C6: full locally uniform convergence.

In particular, evenness, a real-zero property, and one fixed nonreal anchor
do not imply local boundedness. A separate C4 theorem is necessary.

## 10. False-proof firewall

Reject:

1. applying R056 to finite pairs for which the protected CCM simple-even
   hypotheses are not known;
2. treating the anchor normalization as a CCM source choice;
3. using an arbitrary nonreal anchor whose \(\Xi\)-value is not independently
   known to be nonzero;
4. claiming that one-point matching implies convergence;
5. claiming that real zeros plus one-point normalization imply a normal
   family;
6. restricting the residual scalar to positive reals without a phase theorem;
7. inferring global simple-evenness, determinant convergence, RH, novelty,
   priority, publication readiness, or certification.

## 11. Claim boundary

This package proves only an exact finite normalization theorem.

It does not prove:

- existence of an admitted cofinal finite family;
- any large-\(\lambda\) simple-even theorem;
- convergence of finite eigenvectors;
- local boundedness of \(F_{\lambda,N}\);
- locally uniform convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 12. Admission dependency

Before protected admission:

1. compose this candidate onto the then-current protected Solve main if main
   moves;
2. run non-authoring Adversary and Referee passes on that exact head;
3. require exact-head Solve/GCL green checks;
4. merge through protected controls;
5. perform protected readback and update the Route C tracker/handoff.

Terminal candidate disposition:

RH-R056_CANONICAL_FINITE_DETERMINANT_NORMALIZATION_PROVED__C0_DISCHARGED__READY_FOR_EXACT_HEAD_ADMISSION
