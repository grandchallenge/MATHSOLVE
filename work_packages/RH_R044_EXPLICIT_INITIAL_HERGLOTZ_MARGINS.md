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

The guarded RH-R040 theorem proves, on

\[
0<a\le\frac1{22},
\]

the quantitative estimate

\[
g(a)
:=
\epsilon_-(e^a)-\epsilon_+(e^a)
\ge
2\log2-1-6\sqrt2\,a.
\]

Use the elementary bounds

\[
\log2>\frac{693}{1000},
\qquad
\sqrt2<\frac{99}{70}.
\]

Since \(a\le1/22\),

\[
6\sqrt2\,a
<
6\cdot\frac{99}{70}\cdot\frac1{22}
=
\frac{297}{770}.
\]

Therefore

\[
\begin{aligned}
g(a)
&>
\frac{193}{500}
-
\frac{297}{770}
\\
&=
\boxed{\frac{11}{38500}}.
\end{aligned}
\]

Hence throughout the interval,

\[
\boxed{
g(a)>\frac{11}{38500}>0.
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

Subtracting \(\epsilon_+(e^a)\) gives

\[
d(a)
=
\inf\sigma(B_{a,-})
-
\epsilon_+(e^a)
\ge
g(a).
\]

Using Section 2,

\[
\boxed{
d(a)>\frac{11}{38500}.
}
\]

Thus the Herglotz resolvent is not merely defined: it has a uniform
spectral-separation margin over the whole explicit interval.

## 4. Exact norm of the odd pole vector

In centered logarithmic coordinates,

\[
S(x)=\sinh(x/2),
\qquad
x\in[-a,a].
\]

Hence

\[
\begin{aligned}
\|S\|^2
&=
\int_{-a}^{a}\sinh^2(x/2)\,dx
\\
&=
\frac12\int_{-a}^{a}(\cosh x-1)\,dx
\\
&=
\sinh a-a.
\end{aligned}
\]

So

\[
\boxed{
\|S\|^2=\sinh a-a.
}
\]

For \(0<a\le1/22<1\), Taylor's theorem gives

\[
\sinh a-a
=
\frac{a^3}{6}\cosh\xi
\]

for some \(0<\xi<a\).

Since \(\cosh\xi<\cosh1<2\),

\[
\sinh a-a
<
\frac{a^3}{3}.
\]

Therefore

\[
\|S\|^2
<
\frac1{3\cdot22^3}
=
\boxed{\frac1{31944}}.
\]

## 5. Resolvent scalar upper bound

Let

\[
\mu(a)=\epsilon_+(e^a).
\]

On the interval under consideration,

\[
B_{a,-}-\mu(a)I
\ge
d(a)I.
\]

Functional calculus gives

\[
0<
(B_{a,-}-\mu(a)I)^{-1}
\le
\frac1{d(a)}I.
\]

Therefore

\[
\begin{aligned}
m(a)
&:=
\left\langle
S,
(B_{a,-}-\mu(a)I)^{-1}S
\right\rangle
\\
&\le
\frac{\|S\|^2}{d(a)}.
\end{aligned}
\]

Using Sections 3 and 4,

\[
m(a)
<
\frac{1/31944}{11/38500}
=
\frac{38500}{351384}
=
\boxed{\frac{9625}{87846}}.
\]

The exact rational bound is the authoritative statement.

## 6. Explicit Herglotz margin

By definition,

\[
\Delta_H(a)
=
\frac12-m(a).
\]

Hence

\[
\boxed{
\Delta_H(a)
>
\frac12-\frac{9625}{87846}
=
\frac{17149}{43923}.
}
\]

In particular,

\[
\boxed{
\Delta_H(a)>0.
}
\]

No sharpness claim is made.

## 7. Initial continuation certificate

Combining the results, for every

\[
0<a\le\frac1{22}
\]

the guarded chain yields

\[
\boxed{
d(a)>\frac{11}{38500}
}
\]

and

\[
\boxed{
\Delta_H(a)>\frac{17149}{43923}.
}
\]

Thus the two R043 continuation margins begin with explicit uniform
separation from zero on the entire perturbatively proved simple-even
interval.

This gives a concrete initial compact set from which any future derivative,
comparison, or validated-continuation argument may start.

## 8. Relation to the full parity gap

RH-R041 proves, whenever \(d(a)>0\) and \(\Delta_H(a)>0\),

\[
g(a)\ge2d(a)\Delta_H(a).
\]

Applying the present lower bounds gives a secondary certified lower bound

\[
g(a)
>
2
\left(\frac{11}{38500}\right)
\left(\frac{17149}{43923}\right).
\]

This secondary value is weaker than the direct RH-R040 bound

\[
g(a)>\frac{11}{38500},
\]

so it is retained only as a consistency check on the continuation
interface.

## 9. What this changes

Before this package, R043 supplied continuity but no quantitative starting
margin.

After this package, any attempt to continue the small-\(a\) parity theorem
may work from explicit initial data

\[
d\ge d_0,
\qquad
\Delta_H\ge\Delta_0,
\]

with

\[
d_0=\frac{11}{38500},
\qquad
\Delta_0=\frac{17149}{43923}.
\]

A continuation proof may therefore spend a controlled error budget against
these quantities.

## 10. False-proof firewall

Reject:

1. replacing the strict R040 work-branch theorem by this package before
   R040's provider and exact-head CI gates are protected;
2. inferring that \(d(a)\) or \(\Delta_H(a)\) stays positive for
   \(a>1/22\);
3. using the scalar resolvent outside \(d(a)>0\);
4. replacing the full operator norm \(\|S\|\) by a finite Galerkin vector
   norm without an exact identification;
5. treating the coarse rational constants as optimal;
6. inferring determinant convergence or RH from these local margins.

## 11. Claim boundary

This theorem does not prove:

- continuation beyond \(a=1/22\);
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
