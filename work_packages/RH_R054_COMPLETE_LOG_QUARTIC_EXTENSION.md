# RH-R054-COMPLETE-LOG-QUARTIC-EXTENSION-001

Campaign: RH-001

Status: ADMISSION_CANDIDATE

Solve coordination tracker: grandchallenge/MATHSOLVE#411

Protected dependencies:
- grandchallenge/MATHSOLVE@4a329f83c27143ee8d3b8cdce64a9bfb6ecd7f51:work_packages/RH_R051_RANK_ONE_COERCIVITY_EXTENSION.md
- grandchallenge/MATHSOLVE@7387aa8993355ab854630cf0683b4120a813884c:work_packages/RH_R050_TRIAL_REWEIGHTED_EXTENSION.md
- grandchallenge/MATHSOLVE@79531354b7e8982835e0883286319f362560bb95:work_packages/RH_R049_HIGHER_ODD_COERCIVITY.md
- grandchallenge/MATHSOLVE@618840447a59af771ca7ce13a6f15cce3c3a5c06:work_packages/RH_R048_SECTOR_COERCIVITY_EXTENSION.md
- grandchallenge/MATHSOLVE@b7adb8f59d79c58b3de915eaa5abafcbb90b009e:work_packages/RH_R055_NO_PRIME_HERGLOTZ_VARIATION.md
- grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md

Exact checker: scripts/rh_r054_exact_check.py

No RH / determinant-convergence / all-parameter simple-evenness / large-a positivity / novelty / priority / publication-readiness / certification claim.

## 1. Purpose

Protected R051 proves the full localized Weil operator has a strict
even-below-odd parity gap and a simple lowest even eigenvalue for

\[
0<a=\log\lambda\le\frac{178}{1000}.
\]

This package makes three controlled changes:

1. use the complete logarithmic potential, rather than a finite Taylor
   truncation, in the protected R051 rank-one coercivity lemma and certify
   the stronger parameter \(\lambda_*=1/3\);
2. introduce an exact two-parameter positive quartic trial-space formula
   and specialize it to a simple rational positive quartic;
3. reuse newly protected RH-R055's exact \(q'\le23/100\) remainder theorem
   through \(t\le9/25\), without changing its constant or regime.

The result is the full-operator theorem

\[
\boxed{0<a\le\frac9{50}.}
\]

Finite Galerkin data are not used.

## 2. Complete-log odd-sector weight

Let \(w\) be odd, normalized, and in the limiting closed form domain. Write

\[
f=w|_{(0,1)},\qquad
\int_0^1|f(x)|^2\,dx=\frac12,
\qquad
m=\int_0^1 f(x)\,dx.
\]

Protected R046-R051 decompose the limiting odd form. Keeping the complete
logarithmic potential gives

\[
\overline{\mathcal L}(w)
\ge
\log2+A_\infty(f)-|m|^2,
\]

where, with \(u=2x-1\),

\[
A_\infty(f)
=
\int_0^1 W_\infty(2x-1)|f(x)|^2\,dx,
\qquad
W_\infty(u)=1-\log(1-u^2).
\]

The weight satisfies \(W_\infty\ge1\) on \((-1,1)\).

Protected R051 Lemma 2.1 says that for any \(\lambda<1\), if

\[
\int_0^1\frac{du}{W_\infty(u)-\lambda}\le1,
\]

then

\[
A_\infty(f)-|m|^2\ge\frac\lambda2.
\]

The next section proves the strict integral inequality for \(\lambda=1/3\).

## 3. Exact complete-log integral certificate

Set

\[
F(u)
=
\frac1{\frac23-\log(1-u^2)}
\qquad(0\le u<1),
\]

and extend continuously by \(F(1)=0\).

### Lemma 3.1 (concavity)

\[
\boxed{F''(u)\le0\quad(0<u<1).}
\]

Put

\[
D(u)=\frac23-\log(1-u^2).
\]

Then

\[
D'(u)=\frac{2u}{1-u^2},
\qquad
D''(u)=\frac{2(1+u^2)}{(1-u^2)^2},
\]

and

\[
F''(u)
=
\frac{2D'(u)^2-D(u)D''(u)}{D(u)^3}.
\]

Thus it is enough to prove

\[
D(u)\ge\frac{4u^2}{1+u^2}.
\]

Write \(z=u^2\) and \(s=z/(2-z)\). Then \(0\le s<1\) and

\[
1-z=\frac{1-s}{1+s}.
\]

Hence

\[
-\log(1-z)
=
\log\frac{1+s}{1-s}
=
2\operatorname{arctanh}s
\ge2s
=
\frac{2z}{2-z}.
\]

Therefore

\[
\begin{aligned}
D(u)-\frac{4z}{1+z}
&\ge
\frac23+\frac{2z}{2-z}-\frac{4z}{1+z}
\\
&=
\frac{4(2z-1)^2}{3(2-z)(1+z)}
\ge0.
\end{aligned}
\]

This proves concavity.

### Lemma 3.2 (twelve-panel exact midpoint certificate)

For a concave function, Jensen's inequality on each panel gives

\[
\int_{i/12}^{(i+1)/12}F(u)\,du
\le
\frac1{12}F\!\left(\frac{2i+1}{24}\right).
\]

For \(z=u^2\) and \(s=z/(2-z)\),

\[
-\log(1-z)
=
2\sum_{j=0}^{\infty}\frac{s^{2j+1}}{2j+1}.
\]

Define the exact rational lower bound

\[
L_7(z)
=
2\sum_{j=0}^{6}\frac{s^{2j+1}}{2j+1}.
\]

At the twelve midpoints, exact cross-multiplication gives these rational
upper bounds for \(1/(2/3+L_7(u^2))\), and hence for \(F(u)\):

| \(u\) | upper bound |
|---:|---:|
| \(1/24\) | \(7481/5000\) |
| \(1/8\) | \(7327/5000\) |
| \(5/24\) | \(879/625\) |
| \(7/24\) | \(2647/2000\) |
| \(3/8\) | \(6111/5000\) |
| \(11/24\) | \(11081/10000\) |
| \(13/24\) | \(9863/10000\) |
| \(5/8\) | \(4303/5000\) |
| \(17/24\) | \(917/1250\) |
| \(19/24\) | \(6053/10000\) |
| \(7/8\) | \(4723/10000\) |
| \(23/24\) | \(637/2000\) |

Their exact sum is \(7499/625\). Therefore

\[
\boxed{
\int_0^1F(u)\,du
<
\frac1{12}\frac{7499}{625}
=
\frac{7499}{7500}
<1.
}
\]

The exact checker reproduces every cross-multiplication with rational
arithmetic.

## 4. Stronger limiting odd coercivity

Apply protected R051 Lemma 2.1 with

\[
W=W_\infty,\qquad \lambda=\frac13.
\]

Section 3 gives a strict integral bound. Since the normalizing quadratic
form in the Cauchy step is nonzero for normalized \(f\), strictness
propagates:

\[
A_\infty(f)-|m|^2>\frac16.
\]

Therefore

\[
\boxed{
\mu_{-,1}>\log2+\frac16.
}
\]

This improves protected R051's \(\log2+3/20\) bound without replacing the
complete logarithmic potential by a finite polynomial weight.

## 5. Reusable positive quartic trial-space formula

For parameters \(c,d\), set

\[
p_{c,d}(x)=1-cx^2+dx^4.
\]

Direct exact integration gives

\[
N(c,d):=\|p_{c,d}\|^2
=
\frac{2}{315}
\left(
63c^2-90cd-210c+35d^2+126d+315
\right),
\]

\[
M(c,d):=\int_{-1}^{1}p_{c,d}(x)\,dx
=
\frac{2}{15}(15-5c+3d),
\]

and

\[
\frac{\overline{\mathcal L}(p_{c,d})}{\|p_{c,d}\|^2}
=
\frac{H(c,d)}{N(c,d)}-\log2,
\]

where

\[
H(c,d)
=
\frac{2}{99225}
\left(
43659c^2-70200cd-88200c
+30625d^2+60858d+99225
\right).
\]

Also

\[
\frac{
\iint_{[-1,1]^2}|x-y|p_{c,d}(x)p_{c,d}(y)\,dx\,dy
}{
\|p_{c,d}\|^2
}
=
\frac{J(c,d)}{N(c,d)},
\]

with

\[
J(c,d)
=
\frac{8}{10395}
\left(
495c^2-616cd-2772c
+189d^2+1782d+3465
\right).
\]

These formulas give an exact two-parameter analytic trial surface. No
numerical optimizer is part of the theorem.

## 6. A rational positive quartic

Choose

\[
\boxed{
p(x)=1-\frac{13}{20}x^2-\frac{2}{25}x^4.
}
\]

With \(z=x^2\in[0,1]\), the polynomial
\(1-(13/20)z-(2/25)z^2\) is decreasing, so

\[
p(x)\ge p(1)=\frac{27}{100}>0.
\]

Section 5 gives

\[
\boxed{\|p\|^2=\frac{399883}{315000}},
\qquad
\boxed{\int_{-1}^{1}p=\frac{1151}{750}},
\]

\[
\boxed{
\frac{\overline{\mathcal L}(p)}{\|p\|^2}
=
\frac{23727475}{25192629}-\log2,
}
\]

and

\[
\boxed{
\frac{\iint|x-y|p(x)p(y)\,dx\,dy}{\|p\|^2}
=
\frac{70520764}{65980695}.
}
\]

The positive constant rank-one coefficient is

\[
\boxed{
\frac74\frac{\left(\int p\right)^2}{\|p\|^2}
=
\frac{64915249}{19994150},
}
\]

and with \(L=23/100\), the trial-specific residual coefficient is

\[
\boxed{
\frac{23}{100}\frac{70520764}{65980695}
=
\frac{405494393}{1649517375}.
}
\]

## 7. Reuse the protected R055 slope certificate through t <= 9/25

Protected RH-R055 Section 3 now proves on the same no-prime scaled family
\[
0\le q'(t)\le\frac{23}{100}\qquad(0\le t\le9/25).
\]
We import that result. For exact replay and to keep the local arithmetic surface
closed, the endpoint derivation is recorded below using the same protected
R051 envelope.

Retain protected R051's integrated envelope

\[
-r_1'''(t)
\le
B_*(t)
=
\frac35
\left(
\frac1{24}
+\frac t9
-\frac{t^2}{30}
+\frac{t^4}{2835}
\right),
\]

valid whenever \(h(t)\le6/5\).

For

\[
0\le t\le\frac9{25},
\]

one has

\[
\frac t2\le\frac9{50}<\log\frac65
\]

by the protected bound \(\log(6/5)>9/50\). Thus
\(h(t)\le e^{t/2}<6/5\).

The bracket in \(B_*\) is increasing on this interval, hence

\[
B_*(t)
\le
B_*\left(\frac9{25}\right)
=
\frac{25381319}{546875000}.
\]

For \(x=t/2\le9/50\), retain the protected estimate

\[
\sinh x\le\frac{x}{1-x^2/2}.
\]

Thus

\[
\sinh(t/2)\le\frac{900}{4919}.
\]

Consequently

\[
q'(t)
\le
\frac{617038208161}{2690078125000}
<
\frac{23}{100},
\]

because the difference is

\[
\frac{1679760589}{2690078125000}>0.
\]

It remains to revalidate the sign on the enlarged interval. Retain the protected notation

\[
D(t)=\frac1{t^2}-\operatorname{csch}^2t=-u'(t).
\]

Protected R045-R048 show that \(u(t)<1/2\) for \(t>0\), and that \(D(t)\ge1/4\) follows from

\[
12-8t^2-t^4>0.
\]

At \(t=9/25\),

\[
12-8\left(\frac9{25}\right)^2-\left(\frac9{25}\right)^4
=
\frac{4275939}{390625}
>0,
\]

and the polynomial is decreasing for \(t>0\). Hence \(D(t)\ge1/4\) throughout
\(0<t\le9/25\). Therefore

\[
h''(t)=h(t)\left(u(t)^2-D(t)\right)\le0,
\]

so

\[
r_1'''(t)
=
\frac1{2t^2}\int_0^t s h''(s)\,ds
\le0.
\]

Thus \(q'(t)=\sinh(t/2)-r_1'''(t)\ge0\) on the enlarged interval. Combining
this with the upper bound gives

\[
\boxed{
0\le q'(t)<\frac{23}{100}
\qquad
\left(0\le t\le\frac9{25}\right).
}
\]

With \(q(0)=7/4\),

\[
\boxed{
0\le q(t)-\frac74\le\frac{23}{100}t
\qquad
\left(0\le t\le\frac9{25}\right).
}
\]

## 8. Full-operator sector bounds through a <= 9/50

Assume

\[
0<a\le\frac9{50}.
\]

Then

\[
2a\le\frac9{25}<\frac{693}{1000}<\log2,
\]

so the no-prime formula remains strictly valid.

Set \(L=23/100\).

Protected R051's Green-operator bound gives

\[
\boxed{
\nu_{-,1}(a)
>
\log2+\frac16-\frac{18653}{100000}a^2.
}
\]

Protected R048/R051 gives

\[
\boxed{
\nu_{+,2}(a)\ge1-\frac{23}{50}a^2.
}
\]

For the quartic trial,

\[
\boxed{
\nu_{+,1}(a)
\le
\frac{23727475}{25192629}-\log2
+
\frac{64915249}{19994150}a
+
\frac{405494393}{1649517375}a^2.
}
\]

## 9. Strict parity gap through a = 9/50

Subtracting gives

\[
\begin{aligned}
\nu_{-,1}(a)-\nu_{+,1}(a)
>{}&
2\log2+\frac16-\frac{23727475}{25192629}
\\
&-\frac{64915249}{19994150}a
\\
&-
\left(
\frac{405494393}{1649517375}
+\frac{18653}{100000}
\right)a^2.
\end{aligned}
\]

The right side is strictly decreasing for \(a>0\).

At \(a=9/50\), using \(\log2>693/1000\), exact arithmetic gives

\[
\boxed{
\nu_{-,1}(a)-\nu_{+,1}(a)
>
\frac{859636202320933}{69279729750000000}
>0.
}
\]

Hence

\[
\boxed{
\epsilon_+(e^a)<\epsilon_-(e^a)
\qquad
\left(0<a\le\frac9{50}\right).
}
\]

## 10. Even-sector simplicity through a = 9/50

Similarly,

\[
\begin{aligned}
\nu_{+,2}(a)-\nu_{+,1}(a)
\ge{}&
\log2+1-\frac{23727475}{25192629}
\\
&-\frac{64915249}{19994150}a
\\
&-
\left(
\frac{405494393}{1649517375}
+\frac{23}{50}
\right)a^2.
\end{aligned}
\]

This lower bound is decreasing for \(a>0\). At \(a=9/50\),

\[
\boxed{
\nu_{+,2}(a)-\nu_{+,1}(a)
>
\frac{12460054441577}{86599662187500}
>0.
}
\]

Thus the lowest even-sector eigenvalue remains simple throughout the
interval.

## 11. Theorem

### RH-R054-COMPLETE-LOG-QUARTIC-EXTENSION-001

For every

\[
\boxed{
0<a=\log\lambda\le\frac9{50},
}
\]

the full localized Weil operator has:

1. a strict parity gap \(\epsilon_+(\lambda)<\epsilon_-(\lambda)\);
2. a simple lowest even-sector eigenvalue.

Therefore, by protected RH-R036, the global ground eigenvalue is simple
and even.

Uniformly on the interval,

\[
\boxed{
\epsilon_-(\lambda)-\epsilon_+(\lambda)
>
\frac{859636202320933}{69279729750000000},
}
\]

and

\[
\boxed{
\epsilon_{+,2}(\lambda)-\epsilon_{+,1}(\lambda)
>
\frac{12460054441577}{86599662187500}.
}
\]

The common scalar shift does not affect multiplicity or parity ordering.
No positivity of the full ground eigenvalue is claimed on the full
interval.

## 12. Method consequence

This tranche adds two reusable proof mechanisms.

1. The complete logarithmic odd weight supports the stronger protected
   rank-one parameter \(\lambda_*=1/3\). The proof uses concavity of the
   exact reciprocal logarithmic weight and an exact midpoint certificate;
   it is not a finite Taylor truncation of \(-\log(1-u^2)\).
2. Section 5 gives an exact two-parameter quartic trial surface for future
   endpoint work. The chosen quartic is one exact point on that surface.

The endpoint advances from \(178/1000\) to \(9/50=180/1000\), while the
certified parity margin at the larger endpoint is materially positive.

## 13. False-proof firewall

Reject:

1. treating midpoint quadrature as evidence without first proving concavity;
2. replacing the full-log midpoint values by floating-point logarithms;
3. using the atanh series with omitted negative terms;
4. applying the R051 rank-one lemma without checking
   \(W_\infty-1/3>0\);
5. using the quartic residual ratio without proving the trial is positive;
6. using \(q'\le23/100\) beyond \(t=9/25\);
7. reusing the no-prime formula at or beyond \(2a=\log2\);
8. inferring positivity of the full ground eigenvalue on
   \(1/50<a\le9/50\);
9. inferring monotonicity of the actual parity gap from the explicit
   lower-bound polynomial;
10. inferring determinant convergence, RH, large-a positivity, novelty,
    priority, or publication readiness.

## 14. Claim boundary

This theorem does not prove:

- simple-even ground state for \(a>9/50\);
- positivity of the ground eigenvalue for \(1/50<a\le9/50\);
- positivity at the R039 large-\(a\) points;
- monotonicity of the true parity gap;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- publication readiness;
- a MATHCERT disposition.

## 15. Admission dependency

Before protected admission:

1. compose the exact candidate tree onto the then-current protected main if
   main has moved;
2. run non-authoring Adversary and Referee passes on that exact head;
3. require exact-head Solve/GCL CI green;
4. merge through protected controls;
5. perform protected readback and update the Route A coordination record.

Terminal candidate disposition:

RH-R054_SIMPLE_EVEN_PROVED_THROUGH_NINE_FIFTIETHS__READY_FOR_EXACT_HEAD_ADMISSION
