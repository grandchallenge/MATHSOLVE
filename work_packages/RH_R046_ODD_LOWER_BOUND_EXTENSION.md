# RH-R046-ODD-LOWER-BOUND-EXTENSION-001

Campaign: RH-001

Status:
PRE_ROUTE_CANDIDATE__DO_NOT_PROMOTE

Solve tracker:
grandchallenge/MATHSOLVE#398

Protected dependencies:
- grandchallenge/MATHSOLVE@139f35f14ee831aa5aa3ed83b774b762965d58b3:work_packages/RH_R045_PARITY_SENSITIVE_REMAINDER.md
- grandchallenge/MATHSOLVE@56ef305581e573650afb50dcd3d1a25b94e8e9bd:work_packages/RH_R040_EFFECTIVE_SMALL_A_SIMPLE_EVEN.md
- grandchallenge/MATHSOLVE@9519ae68c96c33b1a71548a9984fef1be640a106:work_packages/RH_R041_ODD_HERGLOTZ_GAP_CRITERION.md
- grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md

No RH / novelty / priority / certification claim.

## 1. Purpose

RH-R045 proves the full simple-even theorem through

\[
0<a=\log\lambda\le\frac2{15}
\]

using a parity-sensitive decomposition of the smooth no-prime remainder.

Its certificate stops at \(a=1/7\) for two reasons:

1. the limiting odd-sector lower bound
   \[
   \mu_{-,1}\ge\log2
   \]
   is deliberately coarse;
2. the scalar derivative bound
   \[
   0\le q'(t)\le\frac15
   \]
   was proved only for \(t\le4/15\).

This package removes both limitations sufficiently to prove the full
simple-even theorem through

\[
\boxed{
0<a\le\frac17.
}
\]

No ground-state positivity claim is made on the full interval.

## 2. Limiting odd-sector form

Let \(w\in L^2(-1,1)\) be odd, normalized, and in the closed limiting form
domain:

\[
\|w\|_{L^2(-1,1)}=1.
\]

Write

\[
f=w|_{(0,1)}.
\]

Then

\[
\int_0^1 |f(x)|^2\,dx=\frac12.
\]

The limiting form is

\[
\overline{\mathcal L}(w)
=
\frac14
\iint_{[-1,1]^2}
\frac{|w(x)-w(y)|^2}{|x-y|}\,dx\,dy
-
\frac12
\int_{-1}^{1}|w(x)|^2\log(1-x^2)\,dx.
\]

Split the jump term into same-sign and cross-sign quadrants.

## 3. Same-sign jump lower bound

The two same-sign quadrants contribute

\[
J_{\rm same}
=
\frac12
\int_0^1\int_0^1
\frac{|f(x)-f(y)|^2}{|x-y|}\,dx\,dy.
\]

Since \(|x-y|\le1\),

\[
J_{\rm same}
\ge
\frac12
\int_0^1\int_0^1
|f(x)-f(y)|^2\,dx\,dy.
\]

Let

\[
m:=\int_0^1 f(x)\,dx.
\]

Then

\[
\int_0^1\int_0^1
|f(x)-f(y)|^2\,dx\,dy
=
2\int_0^1|f|^2
-
2|m|^2
=
1-2|m|^2.
\]

Hence

\[
\boxed{
J_{\rm same}\ge\frac12-|m|^2.
}
\]

## 4. Cross-sign jump plus logarithmic potential

The two cross quadrants contribute

\[
J_{\rm cross}
=
\frac12
\int_0^1\int_0^1
\frac{|f(x)+f(y)|^2}{x+y}\,dx\,dy.
\]

Expanding gives

\[
J_{\rm cross}
=
\int_0^1
|f(x)|^2
\log\frac{1+x}{x}\,dx
+
H(f),
\]

where

\[
H(f)
=
\operatorname{Re}
\int_0^1\int_0^1
\frac{f(x)\overline{f(y)}}{x+y}\,dx\,dy.
\]

The kernel is positive definite because

\[
\frac1{x+y}
=
\int_0^\infty e^{-t(x+y)}\,dt,
\]

so

\[
H(f)
=
\int_0^\infty
\left|
\int_0^1 f(x)e^{-tx}\,dx
\right|^2dt
\ge0.
\]

The logarithmic potential on the odd sector is

\[
P(f)
=
-\int_0^1
|f(x)|^2\log(1-x^2)\,dx.
\]

Therefore

\[
J_{\rm cross}+P(f)
\ge
\int_0^1
|f(x)|^2
\left[
\log\frac{1+x}{x}
-
\log(1-x^2)
\right]dx.
\]

The bracket simplifies to

\[
-\log(x(1-x)).
\]

Put

\[
z=x-\frac12.
\]

Since

\[
x(1-x)
=
\frac14-z^2
=
\frac14(1-4z^2),
\]

one has

\[
-\log(x(1-x))
=
\log4-\log(1-4z^2).
\]

Using

\[
-\log(1-u)\ge u
\qquad
(0\le u<1),
\]

we obtain

\[
-\log(x(1-x))
\ge
\log4+4z^2.
\]

Hence

\[
\boxed{
J_{\rm cross}+P(f)
\ge
\log2
+
4\int_0^1
\left(x-\frac12\right)^2
|f(x)|^2\,dx.
}
\]

## 5. Weighted Cauchy improvement

Define

\[
A(f)
:=
\int_0^1
\left[
1+4\left(x-\frac12\right)^2
\right]
|f(x)|^2\,dx.
\]

Sections 3 and 4 give

\[
\overline{\mathcal L}(w)
\ge
\log2+A(f)-|m|^2.
\]

Weighted Cauchy gives

\[
|m|^2
=
\left|\int_0^1 f(x)\,dx\right|^2
\le
A(f)
\int_0^1
\frac{dx}{
1+4(x-\frac12)^2
}.
\]

With

\[
u=2\left(x-\frac12\right),
\]

the scalar integral is

\[
\frac12
\int_{-1}^{1}
\frac{du}{1+u^2}
=
\frac\pi4.
\]

Thus

\[
A(f)-|m|^2
\ge
\left(1-\frac\pi4\right)A(f).
\]

Also

\[
A(f)\ge\int_0^1|f|^2=\frac12.
\]

Therefore

\[
\overline{\mathcal L}(w)
\ge
\log2
+
\frac12
\left(1-\frac\pi4\right).
\]

Using the classical rational bound

\[
\pi<\frac{22}{7},
\]

one has

\[
1-\frac\pi4
>
1-\frac{11}{14}
=
\frac3{14}.
\]

Hence

\[
\boxed{
\overline{\mathcal L}(w)
>
\log2+\frac3{28}.
}
\]

By density/lower semicontinuity the bound holds on the full closed odd form
domain. Therefore

\[
\boxed{
\mu_{-,1}
>
\log2+\frac3{28}.
}
\]

This strictly strengthens the R040/R045 bound
\(\mu_{-,1}\ge\log2\).

## 6. Extending the scalar remainder control to t <= 2/7

Use the R045 notation

\[
q(t)=-r''(t)
=
2\cosh(t/2)-r_1''(t),
\]

\[
r_1''(t)=\frac{h(t)-1}{2t},
\qquad
h(t)=\frac{t e^{t/2}}{\sinh t},
\]

and

\[
u(t)
=
\frac{h'(t)}{h(t)}
=
\frac1t+\frac12-\coth t.
\]

For \(t>0\),

\[
\coth t-\frac1t
=
2t
\sum_{n\ge1}
\frac1{t^2+\pi^2n^2}
\le
\frac t3.
\]

Hence for

\[
0<t\le\frac27,
\]

\[
u(t)
\ge
\frac12-\frac{2}{21}
=
\frac{17}{42},
\qquad
u(t)<\frac12.
\]

As in R045, define

\[
D(t)
=
\frac1{t^2}-\operatorname{csch}^2t
=
-u'(t).
\]

The R045 estimates remain valid on \(0<t\le2/7\):

\[
\frac14\le D(t)\le\frac13.
\]

For the lower bound, the same sufficient inequality is

\[
\left(1+\frac{t^2}{6}\right)^2
\left(1-\frac{t^2}{4}\right)\ge1,
\]

whose difference from \(1\) is

\[
\frac{t^2}{144}
\left(12-8t^2-t^4\right)>0
\]

through \(t\le2/7\).

Since

\[
h''(t)
=
h(t)(u(t)^2-D(t)),
\]

the upper bounds \(u(t)^2\le1/4\) and \(D(t)\ge1/4\) give

\[
h''(t)\le0.
\]

For the lower bound,

\[
u(t)^2-D(t)
\ge
\left(\frac{17}{42}\right)^2-\frac13
=
-\frac{299}{1764}.
\]

Moreover,

\[
h(t)\le e^{t/2}\le e^{1/7}<\frac76.
\]

For example,

\[
\log\frac76
>
\frac16-\frac1{72}
=
\frac{11}{72}
>
\frac17,
\]

so \(e^{1/7}<7/6\).

Therefore

\[
h''(t)
>
-
\frac{299}{1764}\frac76
=
-\frac{2093}{10584}
>
-\frac15.
\]

Thus

\[
\boxed{
-\frac15<h''(t)\le0
\qquad
(0<t\le2/7).
}
\]

## 7. Extended q-prime bound

R045 uses

\[
t h'(t)-h(t)+1
=
\int_0^t s h''(s)\,ds
\]

and therefore

\[
r_1'''(t)
=
\frac1{2t^2}
\int_0^t s h''(s)\,ds.
\]

Section 6 gives

\[
-\frac1{20}<r_1'''(t)\le0.
\]

Hence

\[
q'(t)
=
\sinh(t/2)-r_1'''(t)
\ge0.
\]

For \(t\le2/7\),

\[
\frac t2\le\frac17.
\]

The elementary series estimate

\[
\cosh s
\le
\sum_{n\ge0}\left(\frac{s^2}{2}\right)^n
=
\frac1{1-s^2/2}
\]

gives, for \(0\le s\le1/7\),

\[
\cosh s\le\frac{98}{97}.
\]

Therefore

\[
\sinh\frac17
=
\int_0^{1/7}\cosh s\,ds
\le
\frac17\frac{98}{97}
=
\frac{14}{97}.
\]

Thus

\[
q'(t)
<
\frac{14}{97}+\frac1{20}
=
\frac{377}{1940}
<
\frac15.
\]

Consequently

\[
\boxed{
0\le q'(t)\le\frac15
\qquad
(0\le t\le2/7).
}
\]

Using \(q(0)=7/4\),

\[
\boxed{
0\le q(t)-\frac74\le\frac t5
\qquad
(0\le t\le2/7).
}
\]

This is exactly the R045 scalar remainder estimate on the larger interval.

## 8. Parity-sensitive remainder estimates through a <= 1/7

Assume

\[
0<a\le\frac17.
\]

Then

\[
2a\le\frac27,
\]

so Section 7 applies.

The R045 odd reduced-kernel argument gives

\[
\boxed{
\|K_{a,-}\|
\le
\frac{a^2}{5}.
}
\]

Combining with the improved limiting odd bound,

\[
\boxed{
\nu_{-,1}(a)
>
\log2+\frac3{28}-\frac{a^2}{5}.
}
\]

The R045 even decomposition remains unchanged:

\[
K_a
=
\frac{7a}{4}|1\rangle\langle1|
+
E_a,
\qquad
\|E_a\|\le\frac{2a^2}{5}.
\]

Therefore

\[
\boxed{
\nu_{+,2}(a)
\ge
\frac34-\frac{2a^2}{5}.
}
\]

For the positive even trial

\[
p(x)=1-\frac23x^2,
\]

R045 proves

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

No new finite-dimensional approximation is introduced here.

## 9. Strict parity gap through a = 1/7

Subtract the even-ground upper bound from the improved odd lower bound:

\[
\begin{aligned}
\nu_{-,1}(a)-\nu_{+,1}(a)
>{}&
2\log2+\frac3{28}-\frac{407}{435}
\\
&-
\frac{1715}{522}a
-
\left(
\frac{668}{3045}+\frac15
\right)a^2.
\end{aligned}
\]

The right side is strictly decreasing for \(a>0\).

Use the protected R045 elementary bound

\[
\log2>\frac{693}{1000}
\]

and set \(a=1/7\).

Exact arithmetic gives

\[
\boxed{
\nu_{-,1}(a)-\nu_{+,1}(a)
>
\frac{890791}{11190375}
>
0.
}
\]

Therefore

\[
\boxed{
\epsilon_+(e^a)<\epsilon_-(e^a)
\qquad
(0<a\le1/7).
}
\]

## 10. Even-sector simplicity through a = 1/7

The R045 even-sector bounds give

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

This lower bound is decreasing for \(a>0\).

At \(a=1/7\), using

\[
\log2>\frac{693}{1000},
\]

exact arithmetic gives

\[
\boxed{
\nu_{+,2}(a)-\nu_{+,1}(a)
>
\frac{2271989}{89523000}
>
0.
}
\]

Thus the lowest even-sector eigenvalue remains simple throughout
\(0<a\le1/7\).

## 11. Theorem

### RH-R046-ODD-LOWER-BOUND-EXTENSION-001

For every

\[
0<a=\log\lambda\le\frac17,
\]

the full localized Weil operator has:

1. a strict parity gap;
2. a simple lowest even-sector eigenvalue.

Therefore, by protected RH-R036, the global ground eigenvalue is simple and
even.

Uniformly on the interval,

\[
\boxed{
\epsilon_-(\lambda)-\epsilon_+(\lambda)
>
\frac{890791}{11190375}
}
\]

and

\[
\boxed{
\epsilon_{+,2}(\lambda)-\epsilon_{+,1}(\lambda)
>
\frac{2271989}{89523000}.
}
\]

The common scalar shift does not alter multiplicity or parity ordering.

The theorem does not assert positivity of the full ground eigenvalue on the
whole interval.  Protected R040 retains the positivity certificate through
\(a\le1/50\).

## 12. Relation to the former R045 method boundary

R045 states that its original one-parameter certificate does not close at

\[
a=\frac17.
\]

The present theorem does not contradict that statement.

R045 used the coarse limiting odd bound

\[
\mu_{-,1}\ge\log2.
\]

R046 adds the previously unused same-sign jump energy and weighted Cauchy
estimate to prove

\[
\mu_{-,1}>
\log2+\frac3{28}.
\]

That additional coercive margin is what closes the \(1/7\) endpoint.

Thus the former boundary was a proof-budget boundary, not a spectral
counterexample.

## 13. False-proof firewall

Reject:

1. treating the weighted-Cauchy estimate as an exact odd eigenvalue;
2. dropping the same-sign jump term before claiming the \(3/28\) gain;
3. using \(-\log(1-u)\ge u\) outside \(0\le u<1\);
4. using the extended \(q'\le1/5\) estimate beyond \(t=2/7\);
5. inferring ground-state positivity on all of \(a\le1/7\);
6. inferring monotonicity of the actual parity gap from monotonicity of the
   explicit lower-bound polynomial;
7. inferring determinant convergence or RH.

## 14. Claim boundary

This theorem does not prove:

- simple-even ground state for \(a>1/7\);
- positivity of the ground eigenvalue for \(1/50<a\le1/7\);
- monotonicity of the parity gap;
- positivity at the R039 points;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 15. Admission dependency

Before admission:

1. this package must be independently checked against the exact R040/R045
   source formulas;
2. it must be composed onto the current live Solve head;
3. exact-head Adversary and Referee passes must be recorded;
4. required Solve/GCL checks must be green;
5. protected merge and readback must complete.

Terminal candidate disposition:

RH-R046_SIMPLE_EVEN_PROVED_THROUGH_ONE_SEVENTH_ON_WORK_BRANCH__AWAITING_EXACT_HEAD_ADMISSION
