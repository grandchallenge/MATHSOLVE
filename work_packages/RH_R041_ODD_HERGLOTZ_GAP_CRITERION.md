# RH-R041-ODD-HERGLOTZ-GAP-CRITERION-001

Campaign: RH-001

Status:
PRE_ROUTE_CANDIDATE__DO_NOT_PROMOTE

Solve tracker:
grandchallenge/MATHSOLVE#381

Protected theorem substrate:
- RH-R036-QW-PARITY-GAP-REDUCTION-001
- RH-R037-QW-SECTOR-GALERKIN-001

Provider prerequisite:
The exact pole decomposition in MATHFORGE issue #272 / branch
research/rh-r041-pole-resolvent-interface must be protected before this
package may be admitted.

No RH / novelty / priority / certification claim.

## 1. Purpose

RH-R036 reduced the first Zeta Spectral Triples missing theorem to

\[
\epsilon_+(\lambda)<\epsilon_-(\lambda)
\]

plus even-sector simplicity.

The primary CCM pole functional admits the parity split

\[
A_{\lambda,-}
=
B_{\lambda,-}
-
2|S\rangle\langle S|,
\]

where \(B_{\lambda,-}\) is the odd pole-free self-adjoint operator and

\[
S(x)=\sinh(x/2)
\]

in centered logarithmic coordinates.

This package proves the exact odd-sector rank-one criterion under one
explicit spectral-separation hypothesis.  It imports none of the stronger
Perron/inertia claims from adjacent secondary literature.

## 2. Setup

Fix \(\lambda>1\).

Let

\[
\mu:=\epsilon_+(\lambda)
\]

be the lowest even-sector eigenvalue of the full localized Weil operator.

Let

\[
\beta_-:=\inf\sigma(B_{\lambda,-}).
\]

Assume the pole-localization condition

\[
\boxed{\mu<\beta_-.}
\]

Define

\[
T:=B_{\lambda,-}-\mu I.
\]

Then \(T\) is self-adjoint and strictly positive:

\[
T\ge dI,
\qquad
d:=\beta_- - \mu>0.
\]

Hence \(T^{-1}\) is bounded and positive.

Define the scalar

\[
m
:=
\langle S,T^{-1}S\rangle
=
\left\langle
S,
(B_{\lambda,-}-\mu I)^{-1}S
\right\rangle.
\]

Because \(T^{-1}\ge0\),

\[
m\ge0.
\]

The odd shifted operator is

\[
A_{\lambda,-}-\mu I
=
T-2|S\rangle\langle S|.
\]

## 3. Rank-one factorization

In quadratic-form sense,

\[
T-2|S\rangle\langle S|
=
T^{1/2}
\left(
I-2|v\rangle\langle v|
\right)
T^{1/2},
\]

where

\[
v:=T^{-1/2}S.
\]

Indeed,

\[
T^{1/2}|v\rangle\langle v|T^{1/2}
=
|S\rangle\langle S|.
\]

Moreover,

\[
\|v\|^2
=
\langle S,T^{-1}S\rangle
=
m.
\]

The bounded rank-one operator

\[
I-2|v\rangle\langle v|
\]

acts as the identity on \(v^\perp\) and has eigenvalue

\[
1-2m
\]

on the span of \(v\), whenever \(v\ne0\).

If \(S=0\), then \(m=0\) and all conclusions below are immediate.
For the present localized Weil problem \(S\ne0\).

## 4. Positive-margin case

Assume

\[
m<\frac12.
\]

For every form vector \(f\),

\[
|\langle S,f\rangle|^2
=
|\langle T^{-1/2}S,T^{1/2}f\rangle|^2
\le
m\langle Tf,f\rangle.
\]

Therefore

\[
\begin{aligned}
\langle
(A_{\lambda,-}-\mu I)f,f
\rangle
&=
\langle Tf,f\rangle
-
2|\langle S,f\rangle|^2
\\
&\ge
(1-2m)\langle Tf,f\rangle
\\
&\ge
(1-2m)d\|f\|^2.
\end{aligned}
\]

Thus

\[
A_{\lambda,-}-\mu I
\ge
(1-2m)dI
>
0.
\]

Taking spectral infima gives

\[
\boxed{
\epsilon_-(\lambda)-\mu
\ge
(1-2m)(\beta_- - \mu)
>0.
}
\]

Hence

\[
m<\frac12
\Longrightarrow
\epsilon_-(\lambda)>\mu.
\]

## 5. Equality case

Assume

\[
m=\frac12.
\]

Set

\[
f_0=T^{-1}S.
\]

Since \(S\ne0\), one has \(f_0\ne0\).

Now

\[
Tf_0=S
\]

and

\[
\langle S,f_0\rangle=m=\frac12.
\]

Therefore

\[
\begin{aligned}
(A_{\lambda,-}-\mu I)f_0
&=
Tf_0
-
2S\langle S,f_0\rangle
\\
&=
S-2S\cdot\frac12
\\
&=
0.
\end{aligned}
\]

The factorization in Section 3 with \(1-2m=0\) also shows

\[
A_{\lambda,-}-\mu I\ge0.
\]

Hence zero is the bottom of the shifted odd spectrum:

\[
\boxed{
\epsilon_-(\lambda)=\mu.
}
\]

Thus

\[
m=\frac12
\Longrightarrow
\epsilon_-(\lambda)=\mu.
\]

Conversely, under \(\mu<\beta_-\), if
\(\epsilon_-(\lambda)=\mu\), the cases \(m<1/2\) and \(m>1/2\) are
excluded by Sections 4 and 6, so \(m=1/2\).

## 6. Negative-margin case

Assume

\[
m>\frac12.
\]

Again take

\[
f_0=T^{-1}S.
\]

Then

\[
\langle Tf_0,f_0\rangle
=
\langle S,T^{-1}S\rangle
=
m
\]

and

\[
|\langle S,f_0\rangle|^2=m^2.
\]

Therefore

\[
\begin{aligned}
\langle
(A_{\lambda,-}-\mu I)f_0,f_0
\rangle
&=
m-2m^2
\\
&=
m(1-2m)
\\
&<
0.
\end{aligned}
\]

By the variational principle,

\[
\inf\sigma(A_{\lambda,-}-\mu I)<0.
\]

Thus

\[
\boxed{
\epsilon_-(\lambda)<\mu.
}
\]

Hence

\[
m>\frac12
\Longrightarrow
\epsilon_-(\lambda)<\mu.
\]

Conversely, if \(\epsilon_-(\lambda)<\mu\), Sections 4 and 5 exclude
\(m\le1/2\), so \(m>1/2\).

## 7. Exact trichotomy theorem

### Theorem RH-R041-ODD-HERGLOTZ-GAP-CRITERION-001

Under the single pole-localization hypothesis

\[
\mu=\epsilon_+(\lambda)
<
\beta_-=\inf\sigma(B_{\lambda,-}),
\]

define

\[
m(\lambda)
=
\left\langle
S,
(B_{\lambda,-}-\mu I)^{-1}S
\right\rangle.
\]

Then exactly one of the following holds:

\[
\boxed{
m<\frac12
\iff
\epsilon_+(\lambda)<\epsilon_-(\lambda),
}
\]

\[
\boxed{
m=\frac12
\iff
\epsilon_+(\lambda)=\epsilon_-(\lambda),
}
\]

\[
\boxed{
m>\frac12
\iff
\epsilon_+(\lambda)>\epsilon_-(\lambda).
}
\]

Moreover, in the positive case,

\[
\boxed{
\epsilon_-(\lambda)-\epsilon_+(\lambda)
\ge
(1-2m)
\left(
\inf\sigma(B_{\lambda,-})
-
\epsilon_+(\lambda)
\right).
}
\]

Define the Herglotz margin

\[
\Delta_H(\lambda)
=
\frac12-m(\lambda)
\]

and the pole-localization margin

\[
d(\lambda)
=
\inf\sigma(B_{\lambda,-})
-
\epsilon_+(\lambda).
\]

Then whenever \(\Delta_H(\lambda)>0\),

\[
\boxed{
g(\lambda)
:=
\epsilon_-(\lambda)-\epsilon_+(\lambda)
\ge
2\Delta_H(\lambda)d(\lambda).
}
\]

## 8. Why the pole-localization hypothesis is the exact domain condition

The scalar resolvent

\[
(B_{\lambda,-}-\mu I)^{-1}
\]

is bounded exactly because

\[
\mu<\inf\sigma(B_{\lambda,-}).
\]

No inverse is invoked at or beyond the boundary

\[
\mu=\inf\sigma(B_{\lambda,-}).
\]

The theorem therefore does not hide a spectral-domain assumption in the
notation \(m(\lambda)\).

On any parameter value where the full strict parity gap is already known,

\[
\epsilon_+(\lambda)<\epsilon_-(\lambda),
\]

pole localization follows automatically because

\[
B_{\lambda,-}
=
A_{\lambda,-}+2|S\rangle\langle S|
\ge
A_{\lambda,-}
\]

in form order, hence

\[
\inf\sigma(B_{\lambda,-})
\ge
\epsilon_-(\lambda)
>
\epsilon_+(\lambda).
\]

Thus any already-proved parity-gap regime lies inside the natural domain of
the Herglotz criterion.

## 9. No secondary inertia assumptions

The proof does not use or require:

- \(B_{\lambda,+}\) to have exactly one negative eigenvalue;
- \(B_{\lambda,-}>0\);
- Perron or Krein--Rutman structure;
- positivity-improving semigroups;
- nonzero overlap of \(S\) with every eigenvector of \(B_{\lambda,-}\);
- a secular-root ordering theorem;
- global operator monotonicity of any Loewner symbol.

Only:

1. the exact primary CCM pole split;
2. self-adjointness of \(B_{\lambda,-}\);
3. the explicit inequality
   \[
   \epsilon_+(\lambda)<\inf\sigma(B_{\lambda,-});
   \]
4. elementary rank-one operator algebra

are used.

## 10. False-proof firewall

Reject:

1. defining the resolvent scalar when
   \(\mu\ge\inf\sigma(B_{\lambda,-})\);
2. treating \(m<1/2\) as proved without a bound on the actual infinite
   operator resolvent;
3. replacing the full resolvent scalar by a finite Galerkin value without
   a tail theorem;
4. importing secondary Perron/inertia claims as if primary or independently
   proved;
5. inferring even-sector simplicity from the odd-sector criterion;
6. inferring determinant convergence or RH from a positive parity gap.

## 11. Claim boundary

This theorem does not prove:

- pole localization for all \(\lambda\);
- \(\Delta_H(\lambda)>0\) for all \(\lambda\);
- the parity gap for all \(\lambda\);
- even-sector simplicity for all \(\lambda\);
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 12. Admission dependency

This work package remains guarded until:

1. the provider-side exact pole decomposition is protected in MATHFORGE;
2. this candidate is composed onto the current live Solve head;
3. exact-head Adversary and Referee passes are recorded;
4. required Solve/GCL checks are green on that exact head;
5. protected merge and protected readback complete.

Terminal candidate disposition:

RH-R041_ODD_HERGLOTZ_TRICHOTOMY_PROVED_ON_WORK_BRANCH__AWAITING_PROVIDER_PROTECTION
