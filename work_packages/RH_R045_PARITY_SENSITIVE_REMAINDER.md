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

R040 controls the full smooth remainder by one global operator norm.  That
pays the dominant even constant mode in both parity sectors.

The no-prime scaled remainder has kernel

\[
K_a(x,y)=a\,q(a|x-y|),
\qquad
q(t):=-r''(t).
\]

Near the origin, \(q\) is nearly constant.  Its constant part is a
positive rank-one operator in the even sector and vanishes identically on
odd functions.

This package proves a scalar Lipschitz estimate for \(q\), treats the two
parity sectors separately, and uses an optimized positive even trial to
prove the full simple-even theorem explicitly on

\[
\boxed{0<a\le\frac{2}{15}.}
\]

## 2. Limiting estimates

Let \(T\) be the self-adjoint operator associated with the limiting form

\[
\overline{\mathcal L}.
\]

R040 proves the odd lower bound

\[
\boxed{\mu_{-,1}\ge\log2}
\]

and the second-even lower bound

\[
\boxed{\mu_{+,2}\ge\frac34}.
\]

For the present tranche choose the positive even trial

\[
p(x)=1-\frac23x^2.
\]

Direct integration gives

\[
\|p\|^2=\frac{58}{45},
\qquad
\int_{-1}^{1}p(x)\,dx=\frac{14}{9},
\]

\[
\frac14\iint
\frac{|p(x)-p(y)|^2}{|x-y|}\,dx\,dy
=
\frac{16}{135},
\]

and

\[
-\frac12
\int_{-1}^{1}
p(x)^2\log(1-x^2)\,dx
=
\frac{734}{675}
-
\frac{58}{45}\log2.
\]

Hence

\[
\overline{\mathcal L}(p)
=
\frac{814}{675}
-
\frac{58}{45}\log2,
\]

so Rayleigh--Ritz gives

\[
\boxed{
\mu_{+,1}
\le
\frac{407}{435}-\log2.
}
\]

We also need

\[
\boxed{
\iint_{[-1,1]^2}
|x-y|p(x)p(y)\,dx\,dy
=
\frac{1336}{945}.
}
\]

Thus the limiting parity-gap lower bound is

\[
2\log2-\frac{407}{435},
\]

and the limiting first-even internal-gap lower bound is

\[
\log2+\frac34-\frac{407}{435}.
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

Hence

\[
q(t)
=
-r''(t)
=
2\cosh(t/2)-r_1''(t).
\]

The continuous extension at zero has

\[
h(0)=1,
\qquad
h'(0)=\frac12,
\qquad
r_1''(0)=\frac14,
\]

so

\[
\boxed{q(0)=\frac74.}
\]

## 4. Calculus control on h

For \(t>0\), put

\[
u(t)
=
\frac{h'(t)}{h(t)}
=
\frac1t+\frac12-\coth t.
\]

Then

\[
h''(t)=h(t)\left(u(t)^2+u'(t)\right).
\]

Use

\[
\coth t-\frac1t
=
2t\sum_{n\ge1}\frac1{t^2+\pi^2n^2}.
\]

For

\[
0<t\le\frac4{15},
\]

this gives

\[
0<
\coth t-\frac1t
\le
\frac t3,
\]

and hence

\[
\frac{37}{90}
\le
u(t)
<
\frac12.
\]

Set

\[
D(t)
=
\frac1{t^2}-\operatorname{csch}^2t
=
-u'(t).
\]

Differentiating the partial-fraction expression termwise gives

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

Since \(t<\pi\), each differentiated summand is positive.  Also

\[
D(t)
\le
2\sum_{n\ge1}\frac1{\pi^2n^2}
=
\frac13.
\]

For the lower bound \(D(t)\ge1/4\), note that

\[
\frac{\sinh t}{t}
\ge
1+\frac{t^2}{6}.
\]

It is therefore enough to check

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

which is positive on \(0<t\le4/15\).

Thus

\[
\frac14\le D(t)\le\frac13.
\]

Therefore

\[
u(t)^2+u'(t)
=
u(t)^2-D(t)
\le0,
\]

so

\[
h''(t)\le0.
\]

For the lower bound,

\[
u(t)^2+u'(t)
\ge
\left(\frac{37}{90}\right)^2-\frac13
=
-\frac{1331}{8100}.
\]

Also

\[
h(t)
\le
e^{t/2}
\le
e^{2/15}
<
\frac{15}{13},
\]

where \(e^x<1/(1-x)\) for \(0<x<1\).

Hence

\[
h''(t)
>
-\frac{15}{13}\frac{1331}{8100}
=
-\frac{1331}{7020}
>
-\frac14.
\]

We have proved

\[
\boxed{
-\frac14<h''(t)\le0
\qquad
(0<t\le4/15).
}
\]

## 5. Lipschitz bound for q

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

Section 4 gives

\[
-\frac1{16}<r_1'''(t)\le0.
\]

Therefore

\[
q'(t)
=
\sinh(t/2)-r_1'''(t)
\ge0.
\]

For \(t\le4/15\), one has \(t/2\le2/15\).  Using

\[
\cosh x
\le
\frac1{1-x^2/2},
\]

we get

\[
\sinh(2/15)
=
\int_0^{2/15}\cosh s\,ds
\le
\frac{2/15}{1-2/225}
=
\frac{30}{223}.
\]

Thus

\[
q'(t)
<
\frac{30}{223}+\frac1{16}
=
\frac{703}{3568}
<
\frac15.
\]

Hence

\[
\boxed{
0\le q'(t)\le\frac15
\qquad
(0\le t\le4/15),
}
\]

and, using \(q(0)=7/4\),

\[
\boxed{
0
\le
q(t)-\frac74
\le
\frac t5
\qquad
(0\le t\le4/15).
}
\]

## 6. Odd-sector remainder

Assume

\[
0<a\le\frac2{15}.
\]

Then \(2a\le4/15\).

Identify the odd sector of \(L^2(-1,1)\) with \(L^2(0,1)\).
For \(x,y\in(0,1)\), the reduced kernel is

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
\frac{2a^2}{5}\min(x,y).
\]

The Schur row sum is bounded by

\[
\frac{2a^2}{5}
\int_0^1\min(x,y)\,dy
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

Therefore

\[
\boxed{
\nu_{-,1}(a)
\ge
\log2-\frac{a^2}{5}.
}
\]

## 7. Even-sector remainder decomposition

Write

\[
q(t)=\frac74+\delta(t),
\]

with

\[
0\le\delta(t)\le\frac t5.
\]

Then

\[
K_a
=
\frac{7a}{4}|1\rangle\langle1|
+
E_a,
\]

where \(E_a\) has kernel

\[
a\,\delta(a|x-y|).
\]

The constant rank-one term is positive and acts only in the even sector.

Moreover,

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

Schur gives

\[
\boxed{
\|E_a\|\le\frac{2a^2}{5}.
}
\]

Thus on the even sector

\[
K_{a,+}\ge-\frac{2a^2}{5}I,
\]

and

\[
\boxed{
\nu_{+,2}(a)
\ge
\frac34-\frac{2a^2}{5}.
}
\]

## 8. Perturbed even-ground trial bound

For

\[
p(x)=1-\frac23x^2>0,
\]

positivity of \(p\) and \(\delta\) gives

\[
\langle p,K_ap\rangle
\le
\frac{7a}{4}
\left(\int p\right)^2
+
\frac{a^2}{5}
\iint
|x-y|p(x)p(y)\,dx\,dy.
\]

Divide by

\[
\|p\|^2=\frac{58}{45}.
\]

The constant rank-one contribution is

\[
\frac{
(7a/4)(14/9)^2
}{
58/45
}
=
\frac{1715}{522}a.
\]

The residual contribution is

\[
\frac{
(a^2/5)(1336/945)
}{
58/45
}
=
\frac{668}{3045}a^2.
\]

Therefore

\[
\boxed{
\nu_{+,1}(a)
\le
\frac{407}{435}-\log2
+
\frac{1715}{522}a
+
\frac{668}{3045}a^2.
}
\]

## 9. Strict parity gap through a = 2/15

Subtract Section 8 from Section 6:

\[
\begin{aligned}
\nu_{-,1}(a)-\nu_{+,1}(a)
\ge{}&
2\log2-\frac{407}{435}
\\
&-
\frac{1715}{522}a
-
\left(
\frac{668}{3045}+\frac15
\right)a^2.
\end{aligned}
\]

The right side decreases with \(a>0\).

Use

\[
\log2>\frac{693}{1000}
\]

and set \(a=2/15\).  Exact arithmetic gives

\[
\boxed{
\nu_{-,1}(a)-\nu_{+,1}(a)
>
\frac{13301}{2740500}
>
0.
}
\]

Therefore

\[
\boxed{
\epsilon_+(e^a)<\epsilon_-(e^a)
\qquad
(0<a\le2/15).
}
\]

## 10. Even-sector simplicity through a = 2/15

Sections 7 and 8 give

\[
\begin{aligned}
\nu_{+,2}(a)-\nu_{+,1}(a)
\ge{}&
\log2+\frac34-\frac{407}{435}
\\
&-
\frac{1715}{522}a
-
\left(
\frac{668}{3045}+\frac25
\right)a^2.
\end{aligned}
\]

Again the right side decreases with \(a>0\).

At \(a=2/15\), using \(\log2>693/1000\),

\[
\boxed{
\nu_{+,2}(a)-\nu_{+,1}(a)
>
\frac{319531}{5481000}
>
0.
}
\]

Thus the lowest even eigenvalue is simple throughout the interval.

## 11. Theorem

### RH-R045-PARITY-SENSITIVE-REMAINDER-001

For every

\[
0<a=\log\lambda\le\frac2{15},
\]

the full localized Weil operator has:

1. a strict parity gap;
2. a simple lowest even-sector eigenvalue.

Therefore, by RH-R036, the global ground eigenvalue is simple and even.

Uniformly on the interval,

\[
\boxed{
\epsilon_-(\lambda)-\epsilon_+(\lambda)
>
\frac{13301}{2740500}
}
\]

and

\[
\boxed{
\epsilon_{+,2}(\lambda)-\epsilon_{+,1}(\lambda)
>
\frac{319531}{5481000}.
}
\]

The common scalar shift does not alter multiplicity or parity ordering.

This theorem does not assert positivity of the full ground eigenvalue on
all of \(a\le2/15\).  R040 separately supplies an explicit positivity
certificate on \(a\le1/50\).

## 12. Method boundary

The optimized one-parameter quadratic trial family
\(1-cx^2\), combined with the present \(q'\le1/5\) budget, no longer
closes the parity-gap estimate at \(a=1/7\).

This does not imply a spectral failure at \(1/7\).

Further extension requires a genuinely sharper ingredient, for example:

- a higher-dimensional even trial space;
- a sharper odd limiting lower bound;
- a sharper parity-sensitive kernel comparison;
- quantitative continuation of \(d(a)\) and \(\Delta_H(a)\).

Thus \(2/15\) is the current exact certificate boundary of this
one-parameter parity-sensitive perturbative method.

## 13. False-proof firewall

Reject:

1. treating pointwise sign of a reduced kernel as an operator sign;
2. dropping the positive even rank-one contribution from the ground trial;
3. using \(q'\le1/5\) beyond \(t=4/15\);
4. replacing the exact rational endpoint margins by floating-point evidence;
5. inferring ground-state positivity on all of \(a\le2/15\);
6. interpreting failure of this certificate at \(1/7\) as a counterexample;
7. inferring determinant convergence or RH.

## 14. Claim boundary

This theorem does not prove:

- simple-even ground state for \(a>2/15\);
- positivity of the ground eigenvalue for \(1/50<a\le2/15\);
- monotonicity of the parity gap;
- positivity at the R039 points;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 15. Admission dependency

Before admission:

1. MATHFORGE PR #271 must be protected;
2. R040's provider identity must be protected;
3. this package must be composed onto the current live Solve head;
4. exact-head Adversary and Referee passes must be recorded;
5. required Solve/GCL checks must be green;
6. protected merge and readback must complete.

Terminal candidate disposition:

RH-R045_PARITY_SENSITIVE_SIMPLE_EVEN_PROVED_THROUGH_TWO_FIFTEENTHS_ON_WORK_BRANCH__AWAITING_DEPENDENCY_PROTECTION
