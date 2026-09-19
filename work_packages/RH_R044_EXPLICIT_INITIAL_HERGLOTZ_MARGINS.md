# RH-R044-EXPLICIT-INITIAL-HERGLOTZ-MARGINS-001

Campaign: RH-001

Status:
PRE_ROUTE_CANDIDATE__DO_NOT_PROMOTE

Solve tracker:
grandchallenge/MATHSOLVE#382

Guarded dependencies:
- RH-R040-EFFECTIVE-SMALL-A-SIMPLE-EVEN-001
- RH-R041-ODD-HERGLOTZ-GAP-CRITERION-001
- RH-R043-HERGLOTZ-MARGIN-CONTINUITY-001

Provider prerequisites:
The Suzuki audit in MATHFORGE PR #271 and the exact pole interface in
MATHFORGE issue #272 must be protected before this package may be admitted.

No RH / novelty / priority / certification claim.

## 1. Purpose

RH-R043 turns continuation of the parity gap into control of two margins:

\[
d(a)
=
\inf\sigma(B_{a,-})
-
\epsilon_+(e^a)
\]

and

\[
\Delta_H(a)
=
\frac12
-
\left\langle
S,
(B_{a,-}-\epsilon_+(e^a))^{-1}S
\right\rangle.
\]

This package supplies explicit strictly positive initial values for both
margins on the guarded effective small-\(a\) interval

\[
0<a\le\frac1{24}.
\]

The bounds are deliberately coarse and fully elementary.

## 2. Effective full parity-gap lower bound

The strengthened guarded RH-R040 theorem proves, on

\[
0<a\le\frac1{16},
\]

the uniform parity-gap estimate

\[
\boxed{
g(a)
=
\epsilon_-(e^a)-\epsilon_+(e^a)
>
\frac{5707773}{351568000}.
}
\]

## 3. Pole-localization margin

The exact odd pole split gives

\[
B_{a,-}
=
A_{a,-}
+
2|S\rangle\langle S|
\ge
A_{a,-}.
\]

Therefore

\[
d(a)
=
\inf\sigma(B_{a,-})
-
\epsilon_+(e^a)
\ge
g(a),
\]

so

\[
\boxed{
d(a)>\frac{5707773}{351568000}.
}
\]

## 4. Exact norm of the odd pole vector

For

\[
S(x)=\sinh(x/2),
\qquad
x\in[-a,a],
\]

one has exactly

\[
\|S\|^2=\sinh a-a.
\]

For \(0<a\le1/16<1\), Taylor's theorem and \(\cosh1<2\) give

\[
\sinh a-a
<
\frac{a^3}{3}
\le
\frac1{3\cdot16^3}
=
\boxed{\frac1{12288}}.
\]

## 5. Resolvent scalar upper bound

Let

\[
\mu(a)=\epsilon_+(e^a).
\]

Since

\[
B_{a,-}-\mu(a)I\ge d(a)I,
\]

functional calculus gives

\[
m(a)
:=
\left\langle
S,
(B_{a,-}-\mu(a)I)^{-1}S
\right\rangle
\le
\frac{\|S\|^2}{d(a)}.
\]

Hence

\[
m(a)
<
\frac{1/12288}{5707773/351568000}
=
\boxed{
\frac{2746625}{547946208}
}.
\]

## 6. Explicit Herglotz margin

By definition,

\[
\Delta_H(a)=\frac12-m(a).
\]

Therefore

\[
\boxed{
\Delta_H(a)
>
\frac{271226479}{547946208}.
}
\]

In particular, \(\Delta_H(a)>0\).

## 7. Initial continuation certificate

For every

\[
0<a\le\frac1{16},
\]

the guarded chain yields

\[
\boxed{
d(a)>\frac{5707773}{351568000}
}
\]

and

\[
\boxed{
\Delta_H(a)>\frac{271226479}{547946208}.
}
\]

Thus the two R043 continuation margins begin with explicit uniform
separation from zero on the full perturbatively proved simple-even interval.

## 8. Relation to the full parity gap

RH-R041 proves, whenever \(d(a)>0\) and \(\Delta_H(a)>0\),

\[
g(a)\ge2d(a)\Delta_H(a).
\]

The direct R040 lower bound on \(g\) is stronger than the bound obtained by
substituting the coarse estimates above, so the R040 value remains the
preferred full-gap certificate.

## 9. What this changes

Continuation may now start at the edge \(a=1/16\) with explicit error
budgets

\[
d_0=\frac{5707773}{351568000},
\qquad
\Delta_0=\frac{271226479}{547946208}.
\]

The next non-perturbative step can therefore ask for a quantitative bound on
the variation of \(d\) and \(\Delta_H\) beyond \(1/16\), rather than merely
their qualitative continuity.

## 10. False-proof firewall

Reject:

1. replacing the strict R040 work-branch theorem by this package before
   R040's provider and exact-head CI gates are protected;
2. inferring that \(d(a)\) or \(\Delta_H(a)\) stays positive for
   \(a>1/16\);
3. using the scalar resolvent outside \(d(a)>0\);
4. replacing the full operator norm \(\|S\|\) by a finite Galerkin vector
   norm without an exact identification;
5. treating the coarse rational constants as optimal;
6. inferring determinant convergence or RH from these local margins.

## 11. Claim boundary

This theorem does not prove:

- continuation beyond \(a=1/16\);
- monotonicity of \(d\) or \(\Delta_H\);
- positivity at the R039 points;
- all-\(a\) even-simplicity;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 12. Admission dependency

Before admission:

1. R040 provider audit must be protected;
2. the effective R040 theorem must be composed and protected;
3. the R041 provider pole split must be protected;
4. the R041 Solve trichotomy must be composed and protected;
5. R043 continuity must be composed and protected if the continuation
   corollary is retained;
6. this theorem must then be replayed on the current live Solve head with
   exact-head Adversary/Referee reviews and required CI.

Terminal candidate disposition:

RH-R044_EXPLICIT_INITIAL_CONTINUATION_MARGINS_PROVED_ON_WORK_BRANCH__AWAITING_DEPENDENCY_PROTECTION
