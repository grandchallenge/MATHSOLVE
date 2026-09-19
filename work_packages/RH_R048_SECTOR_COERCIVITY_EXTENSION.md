# RH-R048-SECTOR-COERCIVITY-EXTENSION-001

Campaign: RH-001

Status:
ADMISSION_CANDIDATE__INDEPENDENT_CHECK_COMPLETE

Solve tracker:
grandchallenge/MATHSOLVE#402

Protected dependencies:
- grandchallenge/MATHSOLVE@e5aae5f07492562da0edb4d9d9b35f0e01afa6d6:work_packages/RH_R047_INTEGRATED_REMAINDER_EXTENSION.md
- grandchallenge/MATHSOLVE@cf414d991440c3f8a225b8438a7c524a56b1b76e:work_packages/RH_R046_ODD_LOWER_BOUND_EXTENSION.md
- grandchallenge/MATHSOLVE@139f35f14ee831aa5aa3ed83b774b762965d58b3:work_packages/RH_R045_PARITY_SENSITIVE_REMAINDER.md
- grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md

No RH / novelty / priority / certification claim.

## 1. Purpose

Protected R047 proves the full simple-even theorem through

\[
0<a=\log\lambda\le\frac3{20}.
\]

At that endpoint the protected parity-gap estimate still has material
slack, while the explicit even-sector internal-gap estimate is small.
This package strengthens both limiting sector estimates and allows a
slightly larger smooth-remainder Lipschitz constant.

The three new ingredients are:

1. an exact even-sector lower bound
   \[
   \mu_{+,2}\ge1;
   \]
2. an improved odd-sector lower bound
   \[
   \mu_{-,1}>
   \log2+\frac{323}{2688};
   \]
3. a smooth-remainder slope certificate
   \[
   0\le q'(t)\le\frac9{40}
   \qquad
   (0\le t\le1/3).
   \]

Together with the protected R045/R047 positive even trial, these prove the
full simple-even theorem through

\[
\boxed{
0<a\le\frac16.
}
\]

No positivity of the full ground eigenvalue is claimed on the whole
interval.

## 2. Limiting even-sector improvement

Let \(w\) be even, normalized, in the limiting closed form domain, and
orthogonal to the constant function.

Write

\[
f=w|_{(0,1)}.
\]

Then

\[
\int_0^1 |f(x)|^2\,dx=\frac12,
\qquad
\int_0^1 f(x)\,dx=0.
\]

For even \(w\), the limiting jump term is

\[
J_+(f)
=
\frac12
\int_0^1\int_0^1
|f(x)-f(y)|^2
\left(
\frac1{|x-y|}
+
\frac1{x+y}
\right)dx\,dy.
\]

For \(x,y\in(0,1)\), assume without loss of generality that \(x>y\).
Then

\[
\frac1{x-y}+\frac1{x+y}
=
\frac{2x}{x^2-y^2}.
\]

Since

\[
x^2-y^2\le x^2
\]

and \(x\le1\),

\[
\frac{2x}{x^2-y^2}
\ge
\frac2x
\ge2.
\]

Hence, off the diagonal,

\[
\boxed{
\frac1{|x-y|}+\frac1{x+y}\ge2.
}
\]

Therefore

\[
J_+(f)
\ge
\int_0^1\int_0^1
|f(x)-f(y)|^2\,dx\,dy.
\]

Using the mean-zero condition,

\[
\begin{aligned}
\int_0^1\int_0^1
|f(x)-f(y)|^2\,dx\,dy
&=
2\int_0^1|f|^2
-
2\left|\int_0^1 f\right|^2
\\
&=
1.
\end{aligned}
\]

The logarithmic potential term in the limiting form is nonnegative.
Consequently

\[
\overline{\mathcal L}(w)\ge1.
\]

By the max--min principle,

\[
\boxed{
\mu_{+,2}\ge1.
}
\]

This strictly improves the protected R040/R045 lower bound \(3/4\).

## 3. One more logarithmic-potential term in the odd sector

Let \(w\) be odd and normalized, and put again

\[
f=w|_{(0,1)},
\qquad
\int_0^1|f|^2=\frac12.
\]

Protected R046 decomposes the limiting odd form into the same-sign jump
term plus the cross-sign jump and potential.

The same-sign estimate is

\[
J_{\rm same}
\ge
\frac12-|m|^2,
\qquad
m:=\int_0^1 f(x)\,dx.
\]

The cross-sign jump plus logarithmic potential satisfies

\[
J_{\rm cross}+P(f)
\ge
\int_0^1
|f(x)|^2[-\log(x(1-x))]\,dx.
\]

Put

\[
z=x-\frac12,
\qquad
u=2z.
\]

Then

\[
x(1-x)
=
\frac14(1-u^2).
\]

Hence

\[
-\log(x(1-x))
=
\log4-\log(1-u^2).
\]

For \(0\le u^2<1\),

\[
-\log(1-u^2)
=
\sum_{n\ge1}\frac{u^{2n}}n
\ge
u^2+\frac{u^4}{2}.
\]

In terms of \(z\),

\[
u^2+\frac{u^4}{2}
=
4z^2+8z^4.
\]

Therefore

\[
J_{\rm cross}+P(f)
\ge
\log2
+
\int_0^1
\left[
4z^2+8z^4
\right]
|f(x)|^2\,dx.
\]

Combining with the same-sign term gives

\[
\overline{\mathcal L}(w)
\ge
\log2+A(f)-|m|^2,
\]

where

\[
A(f)
:=
\int_0^1
W(x)|f(x)|^2\,dx
\]

and

\[
W(x)
=
1+4\left(x-\frac12\right)^2
+
8\left(x-\frac12\right)^4.
\]

Since \(W\ge1\),

\[
A(f)\ge\frac12.
\]

## 4. Weighted Cauchy with a rational integral bound

Weighted Cauchy gives

\[
|m|^2
\le
A(f)I,
\]

where

\[
I
=
\int_0^1\frac{dx}{W(x)}.
\]

With \(u=2x-1\),

\[
I
=
\int_0^1
\frac{du}{
1+u^2+\frac12u^4
}.
\]

Write

\[
A_0=1+u^2,
\qquad
b=\frac12u^4.
\]

Then

\[
\frac1{A_0+b}
=
\frac1{A_0}
-
\frac{b}{A_0(A_0+b)}.
\]

For \(0\le u\le1\),

\[
A_0+b
=
1+u^2+\frac12u^4
\le
1+\frac32u^2.
\]

Hence

\[
A_0(A_0+b)
\le
(1+u^2)
\left(1+\frac32u^2\right)
\le
1+4u^2.
\]

Therefore

\[
\frac{b}{A_0(A_0+b)}
\ge
\frac{u^4}{2(1+4u^2)}.
\]

Thus

\[
I
\le
\int_0^1\frac{du}{1+u^2}
-
\int_0^1
\frac{u^4}{2(1+4u^2)}\,du.
\]

The first integral is

\[
\frac\pi4.
\]

Polynomial division gives

\[
\int_0^1
\frac{u^4}{2(1+4u^2)}\,du
=
\frac1{96}
+
\frac{\arctan 2}{64}.
\]

Use

\[
\pi<\frac{22}{7}.
\]

Also

\[
\arctan2>1.
\]

For example, the alternating Taylor bounds give

\[
\sin1<1,
\qquad
\cos1>1-\frac12=\frac12,
\]

so

\[
\tan1<2.
\]

Since tangent is increasing on the relevant interval,
\(\arctan2>1\).

Consequently

\[
\begin{aligned}
I
&<
\frac{11}{14}
-
\left(
\frac1{96}+\frac1{64}
\right)
\\
&=
\boxed{
\frac{1021}{1344}
}.
\end{aligned}
\]

Therefore

\[
A(f)-|m|^2
\ge
(1-I)A(f)
>
\frac{323}{1344}\cdot\frac12
=
\frac{323}{2688}.
\]

Hence

\[
\boxed{
\mu_{-,1}
>
\log2+\frac{323}{2688}.
}
\]

This strictly improves protected R046's
\(\log2+3/28\).

## 5. Extending the smooth-remainder slope to t <= 1/3

Retain the protected R047 definitions

\[
q(t)=-r''(t),
\]

\[
r_1''(t)
=
\frac{h(t)-1}{2t},
\qquad
h(t)=\frac{t e^{t/2}}{\sinh t},
\]

\[
u(t)
=
\frac{h'(t)}{h(t)}
=
\frac1t+\frac12-\coth t,
\]

and

\[
D(t)
=
\frac1{t^2}-\operatorname{csch}^2t.
\]

Protected R047 proves

\[
D(t)
\le
\frac13-\frac{t^2}{45}+\frac{2t^4}{945}
\]

and

\[
u(t)\ge\frac12-\frac t3.
\]

The same lower bound

\[
D(t)\ge\frac14
\]

remains valid for \(t\le1/3\), since the sufficient polynomial

\[
12-8t^2-t^4
\]

is positive there.

Thus \(h''\le0\).

As in R047, put

\[
G(t)
=
\frac1{12}
+
\frac t3
-
\frac{2t^2}{15}
+
\frac{2t^4}{945}.
\]

Then

\[
h''(t)\ge-h(t)G(t).
\]

For \(t\le1/3\),

\[
h(t)
\le
e^{t/2}
\le
e^{1/6}
<
\frac65.
\]

Indeed,

\[
\log\frac65
=
\log\left(1+\frac15\right)
>
\frac15-\frac1{50}
=
\frac9{50}
>
\frac16.
\]

Hence

\[
\boxed{
h''(t)\ge-\frac65G(t).
}
\]

## 6. Integrated r1''' bound through t = 1/3

Using

\[
r_1'''(t)
=
\frac1{2t^2}
\int_0^t s h''(s)\,ds,
\]

Section 5 gives

\[
-r_1'''(t)
\le
B_*(t),
\]

where

\[
B_*(t)
=
\frac35
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

The bracket is increasing for \(0\le t\le1/3\), because

\[
\frac19-\frac t{15}+\frac{4t^3}{2835}
\ge
\frac19-\frac1{45}
=
\frac4{45}
>
0.
\]

Therefore

\[
B_*(t)
\le
B_*(1/3)
=
\boxed{
\frac{137789}{3061800}
}.
\]

Since \(h''\le0\),

\[
r_1'''(t)\le0.
\]

## 7. A 9/40 Lipschitz constant for q

For \(t\le1/3\),

\[
\frac t2\le\frac16.
\]

Use

\[
\cosh s
\le
\frac1{1-s^2/2}.
\]

For \(0\le s\le1/6\),

\[
\cosh s
\le
\frac1{1-1/72}
=
\frac{72}{71}.
\]

Hence

\[
\sinh\frac16
=
\int_0^{1/6}\cosh s\,ds
\le
\frac{12}{71}.
\]

Now

\[
q'(t)
=
\sinh(t/2)-r_1'''(t).
\]

Therefore

\[
0\le q'(t)
\le
\frac{12}{71}
+
\frac{137789}{3061800}
=
\frac{46524619}{217387800}.
\]

Moreover,

\[
\frac9{40}
-
\frac{46524619}{217387800}
=
\frac{596909}{54346950}
>
0.
\]

Thus

\[
\boxed{
0\le q'(t)<\frac9{40}
\qquad
(0\le t\le1/3).
}
\]

Using \(q(0)=7/4\),

\[
\boxed{
0\le q(t)-\frac74\le\frac9{40}t
\qquad
(0\le t\le1/3).
}
\]

## 8. Modified parity-sensitive remainder bounds

Assume

\[
0<a\le\frac16.
\]

Then

\[
2a\le\frac13<\log2,
\]

so the no-prime formula remains valid.

Let

\[
L:=\frac9{40}.
\]

The protected R045 reduced-kernel argument works with an arbitrary
Lipschitz constant \(L\).

### Odd sector

The reduced odd kernel obeys

\[
|K_{a,-}(x,y)|
\le
2La^2\min(x,y).
\]

Since

\[
\sup_x\int_0^1\min(x,y)\,dy
=
\frac12,
\]

Schur gives

\[
\boxed{
\|K_{a,-}\|
\le
La^2
=
\frac9{40}a^2.
}
\]

Therefore

\[
\boxed{
\nu_{-,1}(a)
>
\log2+\frac{323}{2688}
-
\frac9{40}a^2.
}
\]

### Even sector

Write

\[
q(t)=\frac74+\delta(t),
\qquad
0\le\delta(t)\le Lt.
\]

Then

\[
K_a
=
\frac{7a}{4}|1\rangle\langle1|
+
E_a,
\]

and

\[
|E_a(x,y)|
\le
La^2|x-y|.
\]

Because

\[
\sup_x
\int_{-1}^{1}|x-y|\,dy
\le2,
\]

\[
\boxed{
\|E_a\|
\le
2La^2
=
\frac9{20}a^2.
}
\]

Using Section 2,

\[
\boxed{
\nu_{+,2}(a)
\ge
1-\frac9{20}a^2.
}
\]

## 9. Even-ground trial with the modified residual budget

Retain the protected positive even trial

\[
p(x)=1-\frac23x^2.
\]

The positive constant rank-one contribution remains

\[
\frac{1715}{522}a.
\]

The residual trial ratio before multiplying by \(L\) is

\[
\frac{
\iint |x-y|p(x)p(y)\,dx\,dy
}{
\|p\|^2
}
=
\frac{668}{609}.
\]

Therefore the \(L=9/40\) residual contribution is

\[
\frac9{40}
\frac{668}{609}
a^2
=
\boxed{
\frac{501}{2030}a^2.
}
\]

Thus

\[
\boxed{
\nu_{+,1}(a)
\le
\frac{407}{435}-\log2
+
\frac{1715}{522}a
+
\frac{501}{2030}a^2.
}
\]

## 10. Strict parity gap through a = 1/6

Subtract Section 9 from the odd lower bound:

\[
\begin{aligned}
\nu_{-,1}(a)-\nu_{+,1}(a)
>{}&
2\log2
+
\frac{323}{2688}
-
\frac{407}{435}
\\
&-
\frac{1715}{522}a
-
\left(
\frac{501}{2030}
+
\frac9{40}
\right)a^2.
\end{aligned}
\]

The right side is decreasing for \(a>0\).

At

\[
a=\frac16,
\]

use the protected bound

\[
\log2>\frac{693}{1000}.
\]

Exact arithmetic gives

\[
\boxed{
\nu_{-,1}(a)-\nu_{+,1}(a)
>
\frac{123433}{12528000}
>
0.
}
\]

Therefore

\[
\boxed{
\epsilon_+(e^a)<\epsilon_-(e^a)
\qquad
(0<a\le1/6).
}
\]

## 11. Even-sector simplicity through a = 1/6

Sections 8 and 9 give

\[
\begin{aligned}
\nu_{+,2}(a)-\nu_{+,1}(a)
\ge{}&
\log2
+
1
-
\frac{407}{435}
\\
&-
\frac{1715}{522}a
-
\left(
\frac{501}{2030}
+
\frac9{20}
\right)a^2.
\end{aligned}
\]

Again the right side is decreasing for \(a>0\).

At \(a=1/6\), using \(\log2>693/1000\),

\[
\boxed{
\nu_{+,2}(a)-\nu_{+,1}(a)
>
\frac{2087591}{10962000}
>
0.
}
\]

Thus the lowest even-sector eigenvalue is simple throughout
\(0<a\le1/6\).

## 12. Theorem

### RH-R048-SECTOR-COERCIVITY-EXTENSION-001

For every

\[
0<a=\log\lambda\le\frac16,
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
\frac{123433}{12528000}
}
\]

and

\[
\boxed{
\epsilon_{+,2}(\lambda)-\epsilon_{+,1}(\lambda)
>
\frac{2087591}{10962000}.
}
\]

The common scalar shift does not affect multiplicity or parity ordering.

No positivity of the full ground eigenvalue is claimed on the full
interval.

## 13. Method consequence

At \(a=1/6\), unlike R047, the explicit even internal-gap bound has large
slack.  The active certificate bottleneck has returned to the parity-gap
budget.

Further extension should therefore prioritize:

- stronger odd-sector coercivity;
- a sharper even-ground trial upper bound;
- a sharper smooth-remainder slope than the coarse \(9/40\) budget;
- or the protected \(d/\Delta_H\) continuation route.

No spectral failure beyond \(1/6\) is inferred.

## 14. False-proof firewall

Reject:

1. using the kernel inequality in Section 2 without the even mean-zero
   constraint;
2. replacing the weighted-Cauchy integral bound by a numerical integral;
3. using \(\arctan2>1\) without an elementary monotonicity argument;
4. using the \(9/40\) slope certificate beyond \(t=1/3\);
5. retaining the R045 \(1/5\)-dependent remainder constants after changing
   the Lipschitz constant to \(9/40\);
6. inferring ground positivity on all \(a\le1/6\);
7. inferring determinant convergence or RH.

## 15. Claim boundary

This theorem does not prove:

- simple-even ground state for \(a>1/6\);
- positivity of the ground eigenvalue for \(1/50<a\le1/6\);
- monotonicity of the true parity gap;
- positivity at the R039 points;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 16. Admission dependency

Before admission:

1. the theorem must be composed onto the current live Solve head;
2. exact-head Adversary and Referee passes must be recorded;
3. required Solve/GCL checks must be green;
4. protected merge and readback must complete.

Terminal candidate disposition:

RH-R048_SIMPLE_EVEN_PROVED_THROUGH_ONE_SIXTH__READY_FOR_EXACT_HEAD_ADMISSION
