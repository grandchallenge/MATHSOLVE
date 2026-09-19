# RH-R045-PARITY-SENSITIVE-REMAINDER-001

Campaign: RH-001

Status:
PRE_ROUTE_CANDIDATE__DO_NOT_PROMOTE

Solve tracker:
grandchallenge/MATHSOLVE#383

Guarded dependencies:
- RH-R040-EFFECTIVE-SMALL-A-SIMPLE-EVEN-001
- RH-R036-QW-PARITY-GAP-REDUCTION-001

Provider prerequisite:
The Suzuki source audit in MATHFORGE PR #271 must be protected before this
package may be admitted.

No RH / novelty / priority / certification claim.

## 1. Purpose

The guarded R040 theorem controls the full smooth remainder by one global
operator norm.  That pays the dominant even constant mode in both parity
sectors and stops the perturbative proof at \(a=1/16\).

The remainder has much more structure.  In the no-prime regime its scaled
kernel is

\[
K_a(x,y)
=
a\,q(a|x-y|),
\qquad
q(t):=-r''(t).
\]

The function \(q\) is nearly constant near the origin.  The constant part is
a positive rank-one operator in the even sector and vanishes identically in
the odd sector.

This package proves a uniform Lipschitz bound for \(q\), uses it separately
in the two parity sectors, and extends the explicit simple-even regime to

\[
0<a\le\frac18.
\]

## 2. Protected limiting estimates from R040

Let \(T\) be the self-adjoint operator associated with the limiting form

\[
\overline{\mathcal L}.
\]

R040 proves:

\[
\mu_{-,1}\ge\log2,
\]

\[
\mu_{+,1}
\le
\frac{599}{645}-\log2,
\]

and

\[
\mu_{+,2}\ge\frac34.
\]

The even upper bound uses the explicit positive even trial

\[
p(x)=1-\frac{x^2}{2}.
\]

Its exact auxiliary values are

\[
\|p\|^2=\frac{43}{30},
\]

\[
\int_{-1}^{1}p(x)\,dx=\frac53,
\]

and

\[
\iint_{[-1,1]^2}
|x-y|p(x)p(y)\,dx\,dy
=
\frac{178}{105}.
\]

Thus the limiting parity separation is bounded below by

\[
2\log2-\frac{599}{645},
\]

while the limiting first even internal gap is bounded below by

\[
\log2-\frac{461}{2580}.
\]

## 3. Smooth remainder scalar

R040 writes

\[
r=r_0+r_1,
\]

with

\[
r_0''(t)=-2\cosh(t/2)
\]

and

\[
r_1''(t)
=
\frac{h(t)-1}{2t},
\qquad
h(t):=\frac{t e^{t/2}}{\sinh t}.
\]

Hence, for \(t>0\),

\[
q(t)
=
-r''(t)
=
2\cosh(t/2)-r_1''(t).
\]

The continuous extension at the origin satisfies

\[
h(0)=1,
\qquad
h'(0)=\frac12,
\]

so

\[
r_1''(0)=\frac14
\]

and therefore

\[
\boxed{q(0)=\frac74.}
\]

## 4. A calculus lemma for h

For \(t>0\), put

\[
u(t)
:=
\frac{h'(t)}{h(t)}
=
\frac1t+\frac12-\coth t.
\]

Then

\[
h''(t)=h(t)\left(u(t)^2+u'(t)\right).
\]

The standard partial-fraction expansion

\[
\coth t-\frac1t
=
2t\sum_{n\ge1}
\frac1{t^2+\pi^2n^2}
\]

gives, on \(0<t\le1/4\),

\[
0
<
\coth t-\frac1t
\le
\frac t3.
\]

Hence

\[
\frac12-\frac t3
\le
u(t)
<
\frac12.
\]

In particular,

\[
\frac5{12}\le u(t)<\frac12.
\]

Differentiate the partial-fraction expression.  Set

\[
D(t)
:=
\frac1{t^2}-\operatorname{csch}^2 t
=
-u'(t).
\]

Termwise differentiation gives

\[
D(t)
=
2\sum_{n\ge1}
\frac1{t^2+\pi^2n^2}
-
4t^2
\sum_{n\ge1}
\frac1{(t^2+\pi^2n^2)^2}.
\]

Since \(t<\pi\), each differentiated summand is positive, so

\[
D(t)>0.
\]

Dropping the negative second sum and bounding the first sum gives

\[
D(t)
\le
2\sum_{n\ge1}\frac1{\pi^2n^2}
=
\frac13.
\]

A lower bound \(D(t)\ge1/4\) follows elementarily.  Since

\[
\frac{\sinh t}{t}
\ge
1+\frac{t^2}{6},
\]

it is enough to verify

\[
\left(1+\frac{t^2}{6}\right)^2
\left(1-\frac{t^2}{4}\right)
\ge1.
\]

The difference from \(1\) is

\[
\frac{t^2}{144}
\left(
12-8t^2-t^4
\right),
\]

which is positive for \(0<t\le1/4\).

Thus

\[
\frac14\le D(t)\le\frac13.
\]

Consequently,

\[
u(t)^2+u'(t)
=
u(t)^2-D(t)
\le
\frac14-\frac14
=
0,
\]

so

\[
h''(t)\le0.
\]

For the lower bound,

\[
u(t)^2+u'(t)
\ge
\frac{25}{144}-\frac13
=
-\frac{23}{144}.
\]

Also

\[
h(t)
=
\frac{t}{\sinh t}e^{t/2}
\le
e^{t/2}
\le
e^{1/8}
<
\frac87,
\]

where the last inequality follows from
\(e^x<1/(1-x)\) for \(0<x<1\).

Therefore

\[
h''(t)
\ge
-\frac87\frac{23}{144}
=
-\frac{23}{126}
>
-\frac14.
\]

We have proved

\[
\boxed{
-\frac14<h''(t)\le0
\qquad
(0<t\le1/4).
}
\]

## 5. Lipschitz bound for q

Differentiate

\[
r_1''(t)
=
\frac{h(t)-1}{2t}.
\]

Since

\[
t h'(t)-h(t)+1
=
\int_0^t s h''(s)\,ds,
\]

one has

\[
r_1'''(t)
=
\frac1{2t^2}
\int_0^t s h''(s)\,ds.
\]

By Section 4,

\[
-\frac1{16}
<
r_1'''(t)
\le0.
\]

Thus

\[
q'(t)
=
\sinh(t/2)-r_1'''(t)
\ge0.
\]

For the upper bound, on \(0\le t\le1/4\),

\[
\sinh(t/2)\le\sinh(1/8).
\]

Using

\[
\cosh x
=
\sum_{n\ge0}\frac{x^{2n}}{(2n)!}
\le
\sum_{n\ge0}
\left(\frac{x^2}{2}\right)^n
=
\frac1{1-x^2/2},
\]

we obtain

\[
\sinh(1/8)
=
\int_0^{1/8}\cosh s\,ds
\le
\frac18\cosh(1/8)
\le
\frac{16}{127}.
\]

Hence

\[
q'(t)
<
\frac{16}{127}+\frac1{16}
=
\frac{383}{2032}
<
\frac15.
\]

Therefore

\[
\boxed{
0\le q'(t)\le\frac15
\qquad
(0\le t\le1/4).
}
\]

Together with \(q(0)=7/4\),

\[
\boxed{
0
\le
q(t)-\frac74
\le
\frac t5
\qquad
(0\le t\le1/4).
}
\]

## 6. Odd-sector remainder is O(a^2)

Assume

\[
0<a\le\frac18.
\]

Then \(2a\le1/4\).

Identify the odd sector of \(L^2(-1,1)\) with \(L^2(0,1)\).
For \(x,y\in(0,1)\), the reduced odd kernel is

\[
K_{a,-}(x,y)
=
a
\left[
q(a|x-y|)
-
q(a(x+y))
\right].
\]

Because \(q\) is increasing,

\[
K_{a,-}(x,y)\le0.
\]

The Lipschitz estimate gives

\[
|K_{a,-}(x,y)|
\le
\frac{a^2}{5}
\left[
(x+y)-|x-y|
\right]
=
\frac{2a^2}{5}\min(x,y).
\]

The Schur row sum satisfies

\[
\frac{2a^2}{5}
\int_0^1\min(x,y)\,dy
=
\frac{2a^2}{5}
\left(
x-\frac{x^2}{2}
\right)
\le
\frac{a^2}{5}.
\]

Hence

\[
\boxed{
\|K_{a,-}\|
\le
\frac{a^2}{5}.
}
\]

Therefore the perturbed odd bottom obeys

\[
\boxed{
\nu_{-,1}(a)
\ge
\log2-\frac{a^2}{5}.
}
\]

## 7. Even sector: isolate the positive rank-one part

Write

\[
q(t)=\frac74+\delta(t),
\]

where

\[
0\le\delta(t)\le\frac t5
\qquad
(0\le t\le1/4).
\]

Then the full remainder operator is

\[
K_a
=
\frac{7a}{4}
|1\rangle\langle1|
+
E_a,
\]

where \(E_a\) has kernel

\[
a\,\delta(a|x-y|).
\]

The constant rank-one term is positive and acts only in the even sector.

For the residual kernel,

\[
|E_a(x,y)|
\le
\frac{a^2}{5}|x-y|.
\]

Since

\[
\int_{-1}^{1}|x-y|\,dy
=
1+x^2
\le2,
\]

the Schur bound gives

\[
\boxed{
\|E_a\|
\le
\frac{2a^2}{5}.
}
\]

Therefore, on the even sector,

\[
K_{a,+}
\ge
-\frac{2a^2}{5}I,
\]

and the second even eigenvalue obeys

\[
\boxed{
\nu_{+,2}(a)
\ge
\frac34-\frac{2a^2}{5}.
}
\]

## 8. Explicit upper bound for the perturbed even ground

Use again

\[
p(x)=1-\frac{x^2}{2}>0.
\]

Because \(p\) is positive and \(\delta\ge0\),

\[
\langle p,K_ap\rangle
\le
\frac{7a}{4}
\left(
\int_{-1}^{1}p
\right)^2
+
\frac{a^2}{5}
\iint
|x-y|p(x)p(y)\,dx\,dy.
\]

Using the exact values from Section 2 and dividing by

\[
\|p\|^2=\frac{43}{30},
\]

the rank-one contribution is

\[
\frac{
(7a/4)(5/3)^2
}{
43/30
}
=
\frac{875}{258}a,
\]

while the residual contribution is

\[
\frac{
(a^2/5)(178/105)
}{
43/30
}
=
\frac{356}{1505}a^2.
\]

Thus Rayleigh--Ritz gives

\[
\boxed{
\nu_{+,1}(a)
\le
\frac{599}{645}-\log2
+
\frac{875}{258}a
+
\frac{356}{1505}a^2.
}
\]

## 9. Strict parity gap through a = 1/8

Subtract the even upper bound from the odd lower bound:

\[
\begin{aligned}
\nu_{-,1}(a)-\nu_{+,1}(a)
\ge{}&
2\log2-\frac{599}{645}
\\
&-
\frac{875}{258}a
-
\left(
\frac{356}{1505}+\frac15
\right)a^2.
\end{aligned}
\]

The right-hand side is decreasing for \(a>0\).

Use

\[
\log2>\frac{693}{1000}
\]

and set \(a=1/8\).  Then

\[
\begin{aligned}
\nu_{-,1}(a)-\nu_{+,1}(a)
>{}&
\frac{693}{500}
-
\frac{599}{645}
-
\frac{875}{2064}
\\
&-
\frac1{64}
\left(
\frac{356}{1505}+\frac15
\right)
\\
={}&
\boxed{
\frac{63963}{2408000}
}
>0.
\end{aligned}
\]

Therefore

\[
\boxed{
\epsilon_+(e^a)<\epsilon_-(e^a)
\qquad
(0<a\le1/8).
}
\]

## 10. Even-sector simplicity through a = 1/8

Sections 7 and 8 give

\[
\begin{aligned}
\nu_{+,2}(a)-\nu_{+,1}(a)
\ge{}&
\log2-\frac{461}{2580}
\\
&-
\frac{875}{258}a
-
\left(
\frac{356}{1505}+\frac25
\right)a^2.
\end{aligned}
\]

Again the right-hand side is decreasing for \(a>0\).

At \(a=1/8\), using \(\log2>693/1000\),

\[
\begin{aligned}
\nu_{+,2}(a)-\nu_{+,1}(a)
>{}&
\frac{693}{1000}
-
\frac{461}{2580}
-
\frac{875}{2064}
\\
&-
\frac1{64}
\left(
\frac{356}{1505}+\frac25
\right)
\\
={}&
\boxed{
\frac{96847}{1204000}
}
>0.
\end{aligned}
\]

Thus the lowest even eigenvalue is simple throughout the interval.

## 11. Theorem

### RH-R045-PARITY-SENSITIVE-REMAINDER-001

For every

\[
0<a=\log\lambda\le\frac18,
\]

the full localized Weil operator has:

1. a strict parity gap
   \[
   \epsilon_+(\lambda)<\epsilon_-(\lambda);
   \]
2. a simple lowest even-sector eigenvalue.

Therefore, by RH-R036,

\[
\boxed{
\text{the global ground eigenvalue is simple and even.}
}
\]

Moreover the explicit bounds

\[
\boxed{
\epsilon_-(\lambda)-\epsilon_+(\lambda)
>
\frac{63963}{2408000}
}
\]

and

\[
\boxed{
\epsilon_{+,2}(\lambda)-\epsilon_{+,1}(\lambda)
>
\frac{96847}{1204000}
}
\]

hold throughout the interval after the common scalar shift is restored.

The theorem does not assert that the global ground eigenvalue is positive
on the full \(a\le1/8\) interval.  R040 separately supplies an explicit
positivity certificate on \(a\le1/50\).

## 12. Why this improves R040

The global norm estimate used in R040 treats the large constant component of
\(K_a\) as if it acted equally in both parity sectors.

The exact decomposition here shows:

- the constant component is positive rank one and even;
- it vanishes identically on odd functions;
- the odd remainder is only \(O(a^2)\);
- the even residual away from the positive rank-one part is only \(O(a^2)\).

The resulting parity-sensitive comparison extends the explicit
simple-even cutoff from \(1/16\) to \(1/8\).

## 13. Method boundary

At \(a=1/7\), the explicit lower bound in Section 9 obtained from this same
trial and Lipschitz budget is no longer positive.

This does not imply parity-gap failure at \(a=1/7\).

It means that further extension requires at least one of:

- a sharper even trial vector;
- a sharper odd limiting lower bound;
- a sharper scalar kernel slope estimate;
- a nonperturbative continuation estimate for \(d(a)\) and
  \(\Delta_H(a)\).

Thus \(1/8\) is the current certificate boundary for this parity-sensitive
perturbative method, not a spectral counterexample boundary.

## 14. False-proof firewall

Reject:

1. treating pointwise negativity of the odd reduced kernel as operator
   negativity; only the Schur norm bound is used;
2. treating the positive constant even rank-one term as harmless for the
   first even eigenvalue; its exact trial contribution is retained;
3. replacing the \(O(a^2)\) residual bounds by numerical observations;
4. extending the \(q'\le1/5\) lemma beyond \(t=1/4\) without a new proof;
5. inferring ground-state positivity on the entire \(a\le1/8\) interval;
6. inferring determinant convergence or RH.

## 15. Claim boundary

This theorem does not prove:

- simple-even ground state for \(a>1/8\);
- positivity of the ground eigenvalue for \(1/50<a\le1/8\);
- monotonicity of the parity gap;
- positivity at the R039 points;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 16. Admission dependency

Before admission:

1. MATHFORGE PR #271 must be protected;
2. R040's protected provider identity must replace the guarded dependency;
3. this package must be composed onto the current live Solve head;
4. exact-head Adversary and Referee passes must be recorded;
5. required Solve/GCL checks must be green;
6. protected merge and readback must complete.

Terminal candidate disposition:

RH-R045_PARITY_SENSITIVE_SIMPLE_EVEN_PROVED_THROUGH_A_ONE_EIGHTH_ON_WORK_BRANCH__AWAITING_DEPENDENCY_PROTECTION
