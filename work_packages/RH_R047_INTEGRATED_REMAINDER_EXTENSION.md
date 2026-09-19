# RH-R047-INTEGRATED-REMAINDER-EXTENSION-001

Campaign: RH-001

Status:
ADMISSION_CANDIDATE__INDEPENDENT_CHECK_COMPLETE

Solve tracker:
grandchallenge/MATHSOLVE#400

Protected dependencies:
- grandchallenge/MATHSOLVE@cf414d991440c3f8a225b8438a7c524a56b1b76e:work_packages/RH_R046_ODD_LOWER_BOUND_EXTENSION.md
- grandchallenge/MATHSOLVE@139f35f14ee831aa5aa3ed83b774b762965d58b3:work_packages/RH_R045_PARITY_SENSITIVE_REMAINDER.md
- grandchallenge/MATHSOLVE@56ef305581e573650afb50dcd3d1a25b94e8e9bd:work_packages/RH_R040_EFFECTIVE_SMALL_A_SIMPLE_EVEN.md
- grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md

No RH / novelty / priority / certification claim.

## 1. Purpose

Protected R046 proves the full simple-even theorem through

\[
0<a=\log\lambda\le\frac17
\]

by strengthening the limiting odd-sector lower bound to

\[
\mu_{-,1}>
\log2+\frac3{28}
\]

and extending the R045 scalar remainder estimate to \(t\le2/7\).

The present package keeps the R046 odd coercivity unchanged and sharpens
only the scalar remainder calculus.  Instead of replacing \(h''\) by one
uniform worst-case constant, it integrates an explicit \(t\)-dependent
envelope.  This proves

\[
0\le q'(t)\le\frac15
\]

through

\[
0\le t\le\frac3{10},
\]

which is sufficient for

\[
\boxed{
0<a\le\frac3{20}.
}
\]

## 2. Protected spectral input

Use the protected R046 bound

\[
\boxed{
\mu_{-,1}>
\log2+\frac3{28}.
}
\]

Use the protected R045 even-sector estimates:

\[
\boxed{
\mu_{+,2}\ge\frac34
}
\]

and, for the positive even trial

\[
p(x)=1-\frac23x^2,
\]

\[
\boxed{
\mu_{+,1}
\le
\frac{407}{435}-\log2.
}
\]

The R045 trial data are also retained:

\[
\|p\|^2=\frac{58}{45},
\qquad
\int_{-1}^{1}p(x)\,dx=\frac{14}{9},
\]

and

\[
\iint_{[-1,1]^2}
|x-y|p(x)p(y)\,dx\,dy
=
\frac{1336}{945}.
\]

No new finite-dimensional spectral approximation is introduced.

## 3. Scalar remainder notation

Retain the R045/R046 definitions

\[
q(t)
=
-r''(t)
=
2\cosh(t/2)-r_1''(t),
\]

\[
r_1''(t)
=
\frac{h(t)-1}{2t},
\qquad
h(t)
=
\frac{t e^{t/2}}{\sinh t},
\]

and

\[
u(t)
=
\frac{h'(t)}{h(t)}
=
\frac1t+\frac12-\coth t.
\]

Also set

\[
D(t)
=
\frac1{t^2}-\operatorname{csch}^2t
=
-u'(t).
\]

For \(t>0\),

\[
\coth t-\frac1t
=
2t\sum_{n\ge1}
\frac1{t^2+\pi^2n^2}.
\]

Therefore

\[
u(t)
\ge
\frac12-\frac t3.
\]

For

\[
0<t\le\frac3{10},
\]

this gives

\[
u(t)\ge\frac25>0,
\qquad
u(t)<\frac12.
\]

## 4. Refined upper bound for D(t)

The protected R045 proof uses \(D(t)\le1/3\).  Here we retain one more
order.

Since

\[
D(t)
=
2\sum_{n\ge1}
\frac1{t^2+\pi^2n^2}
-
4t^2
\sum_{n\ge1}
\frac1{(t^2+\pi^2n^2)^2},
\]

one has

\[
D(t)
\le
2\sum_{n\ge1}
\frac1{t^2+\pi^2n^2}.
\]

For \(A>0\) and \(x\ge0\),

\[
\frac1{A+x}
\le
\frac1A-\frac{x}{A^2}+\frac{x^2}{A^3},
\]

because the difference between the right side and the left side is

\[
\frac{x^3}{A^3(A+x)}
\ge0.
\]

Taking

\[
A=\pi^2n^2,
\qquad
x=t^2,
\]

and using

\[
\sum_{n\ge1}\frac1{\pi^2n^2}=\frac16,
\]

\[
\sum_{n\ge1}\frac1{\pi^4n^4}=\frac1{90},
\]

\[
\sum_{n\ge1}\frac1{\pi^6n^6}=\frac1{945},
\]

gives

\[
\boxed{
D(t)
\le
\frac13-\frac{t^2}{45}+\frac{2t^4}{945}.
}
\]

The protected lower bound

\[
D(t)\ge\frac14
\]

also remains valid through \(t\le3/10\), since the same sufficient
polynomial inequality used in R045/R046 is positive there.

Hence, because \(u(t)<1/2\),

\[
u(t)^2-D(t)\le0,
\]

so

\[
\boxed{
h''(t)\le0.
}
\]

## 5. A t-dependent lower envelope for h''

From

\[
u(t)\ge\frac12-\frac t3
\]

and Section 4,

\[
u(t)^2-D(t)
\ge
-
G(t),
\]

where

\[
G(t)
:=
\frac1{12}
+
\frac t3
-
\frac{2t^2}{15}
+
\frac{2t^4}{945}.
\]

Indeed,

\[
\left(
\frac13-\frac{t^2}{45}+\frac{2t^4}{945}
\right)
-
\left(
\frac12-\frac t3
\right)^2
=
G(t).
\]

Also

\[
h(t)\le e^{t/2}\le e^{3/20}<\frac76.
\]

For example,

\[
\log\frac76
>
\frac16-\frac1{72}
=
\frac{11}{72}
>
\frac3{20}.
\]

Therefore

\[
\boxed{
h''(t)
\ge
-\frac76G(t)
\qquad
(0<t\le3/10).
}
\]

This replaces the uniform R046 lower bound by an integrable polynomial
envelope.

## 6. Integrated bound for r1'''

R045/R046 use

\[
t h'(t)-h(t)+1
=
\int_0^t s h''(s)\,ds
\]

and

\[
r_1'''(t)
=
\frac1{2t^2}
\int_0^t s h''(s)\,ds.
\]

Section 5 gives

\[
-r_1'''(t)
\le
B(t),
\]

where

\[
B(t)
=
\frac7{12}
\left(
\frac1{24}
+
\frac t9
-
\frac{t^2}{30}
+
\frac{t^4}{2835}
\right).
\]

The derivative of the bracket is

\[
\frac19-\frac t{15}+\frac{4t^3}{2835}.
\]

For \(0\le t\le3/10\),

\[
\frac19-\frac t{15}
\ge
\frac19-\frac1{50}
>
0,
\]

so \(B(t)\) is increasing.

Hence

\[
B(t)
\le
B(3/10)
=
\boxed{
\frac{25201}{600000}.
}
\]

Since Section 4 gives \(h''\le0\), one also has

\[
r_1'''(t)\le0.
\]

## 7. Extending q-prime through t = 3/10

Because

\[
q'(t)
=
\sinh(t/2)-r_1'''(t),
\]

Sections 4 and 6 imply

\[
q'(t)\ge0.
\]

For \(t\le3/10\),

\[
\frac t2\le\frac3{20}.
\]

Use the elementary series bound

\[
\cosh s
\le
\frac1{1-s^2/2}.
\]

On \(0\le s\le3/20\),

\[
\cosh s
\le
\frac1{1-9/800}
=
\frac{800}{791}.
\]

Therefore

\[
\sinh\frac3{20}
=
\int_0^{3/20}\cosh s\,ds
\le
\frac3{20}\frac{800}{791}
=
\frac{120}{791}.
\]

Thus

\[
q'(t)
\le
\frac{120}{791}
+
\frac{25201}{600000}
=
\frac{91933991}{474600000}.
\]

Finally,

\[
\frac15
-
\frac{91933991}{474600000}
=
\frac{2986009}{474600000}
>
0.
\]

Hence

\[
\boxed{
0\le q'(t)<\frac15
\qquad
(0\le t\le3/10).
}
\]

Using the protected value \(q(0)=7/4\),

\[
\boxed{
0
\le
q(t)-\frac74
\le
\frac t5
\qquad
(0\le t\le3/10).
}
\]

## 8. Parity-sensitive remainder through a <= 3/20

Assume

\[
0<a\le\frac3{20}.
\]

Then

\[
2a\le\frac3{10}.
\]

Also

\[
\frac3{10}
<
\frac{693}{1000}
<
\log2,
\]

so the no-prime formula remains valid.

By Section 7, the complete R045 parity-sensitive remainder argument applies
unchanged:

\[
\boxed{
\|K_{a,-}\|
\le
\frac{a^2}{5},
}
\]

\[
\boxed{
K_{a,+}
\ge
-\frac{2a^2}{5}I
}
\]

after retaining the positive constant rank-one part separately, and

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

Using protected R046,

\[
\boxed{
\nu_{-,1}(a)
>
\log2+\frac3{28}-\frac{a^2}{5}.
}
\]

Using protected R045,

\[
\boxed{
\nu_{+,2}(a)
\ge
\frac34-\frac{2a^2}{5}.
}
\]

## 9. Strict parity gap through a = 3/20

Subtract the even-ground upper bound from the odd lower bound:

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

The right side is decreasing for \(a>0\).

At

\[
a=\frac3{20},
\]

using the protected bound

\[
\log2>\frac{693}{1000},
\]

exact arithmetic gives

\[
\boxed{
\nu_{-,1}(a)-\nu_{+,1}(a)
>
\frac{641}{11600}
>
0.
}
\]

Therefore

\[
\boxed{
\epsilon_+(e^a)<\epsilon_-(e^a)
\qquad
(0<a\le3/20).
}
\]

## 10. Even-sector simplicity through a = 3/20

The even internal-gap lower bound is

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

Again the right side decreases for \(a>0\).

At \(a=3/20\),

\[
\boxed{
\nu_{+,2}(a)-\nu_{+,1}(a)
>
\frac1{1624}
>
0.
}
\]

Thus the lowest even-sector eigenvalue is simple throughout
\(0<a\le3/20\).

## 11. Theorem

### RH-R047-INTEGRATED-REMAINDER-EXTENSION-001

For every

\[
0<a=\log\lambda\le\frac3{20},
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
\frac{641}{11600}
}
\]

and

\[
\boxed{
\epsilon_{+,2}(\lambda)-\epsilon_{+,1}(\lambda)
>
\frac1{1624}.
}
\]

The common scalar shift does not affect multiplicity or parity ordering.

No positivity of the full ground eigenvalue is claimed on the full interval.

## 12. Method boundary

The present argument is deliberately conservative.

The parity-gap bound still has substantial slack at \(a=3/20\), but the
explicit even-sector internal-gap lower bound is only

\[
\frac1{1624}.
\]

Thus the next obstruction in this certificate is the even-sector
simplicity budget, not the odd parity lower bound.

Further extension should therefore prioritize one of:

- a sharper lower bound for the second even limiting eigenvalue;
- a better even ground trial space;
- a sharper even-sector residual bound;
- or the protected R043/R044 continuation-margin route.

No spectral failure beyond \(3/20\) is inferred.

## 13. False-proof firewall

Reject:

1. using the refined \(D(t)\) upper bound without preserving the positive
   remainder in \(1/(A+x)\);
2. replacing the integrated \(h''\) envelope by its endpoint without the
   monotonicity check on \(B(t)\);
3. using \(q'\le1/5\) beyond \(t=3/10\);
4. inferring positivity of the full ground eigenvalue on all
   \(a\le3/20\);
5. interpreting the small even-gap certificate at the endpoint as a
   numerical eigenvalue estimate;
6. inferring determinant convergence or RH.

## 14. Claim boundary

This theorem does not prove:

- simple-even ground state for \(a>3/20\);
- positivity of the ground eigenvalue for \(1/50<a\le3/20\);
- monotonicity of the true parity gap;
- positivity at the R039 points;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 15. Admission dependency

Before admission:

1. it must be composed onto the current live Solve head;
2. exact-head Adversary and Referee passes must be recorded;
3. required Solve/GCL checks must be green;
4. protected merge and readback must complete.

Terminal candidate disposition:

RH-R047_SIMPLE_EVEN_PROVED_THROUGH_THREE_TWENTIETHS__READY_FOR_EXACT_HEAD_ADMISSION
