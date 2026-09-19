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
0<a\le\frac1{19},
\]

the uniform parity-gap estimate

\[
\boxed{
g(a)
=
\epsilon_-(e^a)-\epsilon_+(e^a)
>
\frac{91801}{8578500}.
}
\]

## 3. Pole-localization margin

The exact odd pole split is

\[
A_{a,-}
=
B_{a,-}
-
2|S\rangle\langle S|,
\]

hence

\[
B_{a,-}
=
A_{a,-}
+
2|S\rangle\langle S|
\ge
A_{a,-}
\]

in form order.

Therefore

\[
\inf\sigma(B_{a,-})
\ge
\epsilon_-(e^a).
\]

Subtracting \(\epsilon_+(e^a)\),

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
d(a)>\frac{91801}{8578500}.
}
\]

## 4. Exact norm of the odd pole vector

In centered logarithmic coordinates,

\[
S(x)=\sinh(x/2),
\qquad
x\in[-a,a].
\]

Hence

\[
\|S\|^2
=
\int_{-a}^{a}\sinh^2(x/2)\,dx
=
\sinh a-a.
\]

For \(0<a\le1/19<1\), Taylor's theorem gives

\[
\sinh a-a
=
\frac{a^3}{6}\cosh\xi
<
\frac{a^3}{3}
\]

for some \(0<\xi<a\), because \(\cosh\xi<\cosh1<2\).

Therefore

\[
\boxed{
\|S\|^2
<
\frac1{3\cdot19^3}
=
\frac1{20577}.
}
\]

## 5. Resolvent scalar upper bound

Let

\[
\mu(a)=\epsilon_+(e^a).
\]

Since

\[
B_{a,-}-\mu(a)I
\ge
d(a)I,
\]

functional calculus gives

\[
0<
(B_{a,-}-\mu(a)I)^{-1}
\le
\frac1{d(a)}I.
\]

Therefore

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

Using the preceding bounds,

\[
m(a)
<
\frac{1/20577}{91801/8578500}
=
\boxed{
\frac{150500}{33140161}
}.
\]

## 6. Explicit Herglotz margin

By definition,

\[
\Delta_H(a)=\frac12-m(a).
\]

Thus

\[
\boxed{
\Delta_H(a)
>
\frac12
-
\frac{150500}{33140161}
=
\frac{32839161}{66280322}.
}
\]

In particular,

\[
\Delta_H(a)>0.
\]

## 7. Initial continuation certificate

For every

\[
0<a\le\frac1{19},
\]

the guarded chain yields

\[
\boxed{
d(a)>\frac{91801}{8578500}
}
\]

and

\[
\boxed{
\Delta_H(a)>\frac{32839161}{66280322}.
}
\]

Thus the two R043 continuation margins start with explicit uniform
separation from zero on the full perturbatively proved simple-even interval.

## 8. Relation to the full parity gap

RH-R041 proves, whenever \(d(a)>0\) and \(\Delta_H(a)>0\),

\[
g(a)\ge2d(a)\Delta_H(a).
\]

Substituting the present bounds gives a secondary consistency bound.  The
direct R040 estimate

\[
g(a)>\frac{91801}{8578500}
\]

remains stronger and is the preferred full-gap certificate.

## 9. What this changes

Before this package, R043 supplied continuity but no quantitative starting
margin.

After this package, continuation may start from

\[
d_0=\frac{91801}{8578500},
\qquad
\Delta_0=\frac{32839161}{66280322},
\]

valid uniformly on \(0<a\le1/19\).

Any derivative, comparison, or validated-continuation argument may therefore
spend a controlled error budget against these two explicit quantities.

## 10. False-proof firewall

Reject:

1. replacing the strict R040 work-branch theorem by this package before
   R040's provider and exact-head CI gates are protected;
2. inferring that \(d(a)\) or \(\Delta_H(a)\) stays positive for
   \(a>1/19\);
3. using the scalar resolvent outside \(d(a)>0\);
4. replacing the full operator norm \(\|S\|\) by a finite Galerkin vector
   norm without an exact identification;
5. treating the coarse rational constants as optimal;
6. inferring determinant convergence or RH from these local margins.

## 11. Claim boundary

This theorem does not prove:

- continuation beyond \(a=1/19\);
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
