# RH-R040-EFFECTIVE-SMALL-A-SIMPLE-EVEN-001

Campaign: RH-001

Status:
PRE_ROUTE_CANDIDATE__DO_NOT_PROMOTE

Provider prerequisite:
MATHFORGE PR #271 must be protected before this theorem may be admitted.

Protected theorem substrate:
- RH-R036-QW-PARITY-GAP-REDUCTION-001
- RH-R037-QW-SECTOR-GALERKIN-001

Primary analytic source:
Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
arXiv:2606.09096v2 (17 August 2026), especially equations (2.2),
(4.4), (4.5), and the proof of Theorem 1.4.

## 1. Claim

Let \(A_a\) be the canonical self-adjoint operator representing the
localized Weil quadratic form on \(L^2(-a,a)\).

The proof yields two nested effective statements.

For every

\[
0<a\le \frac1{16},
\]

the lowest eigenvalue of \(A_a\) is simple and has an even eigenfunction.
Equivalently,

\[
\epsilon_+(e^a)<\epsilon_-(e^a)
\]

and the lowest even-sector eigenvalue is simple.

On the smaller interval

\[
0<a\le \frac1{50},
\]

the same ground eigenvalue is additionally strictly positive.

Thus one may take \(e^{1/16}\) as an explicit conservative simple-even
cutoff and \(e^{1/50}\) as an explicit conservative positive-simple-even
cutoff. Neither is asserted to be sharp.

## 2. Scaled source form before the first prime threshold

Suzuki scales \(L^2(-a,a)\) to \(L^2(-1,1)\).  For

\[
0<a<\frac12\log2
\]

the prime sum is empty because \(e^{2a}<2\).

The scaled closed form is

\[
\bar q_a
=
s(a)I+\overline{\mathcal L}+K_a,
\]

where

\[
s(a)=-\log a-(2A+1),
\]

\[
\mathcal L(w)
=
\frac14
\int_{-1}^{1}\int_{-1}^{1}
\frac{|w(x)-w(y)|^2}{|x-y|}\,dx\,dy
-\frac12
\int_{-1}^{1}|w(x)|^2\log(1-x^2)\,dx,
\]

and the bounded remainder operator has kernel

\[
K_a(x,y)=-a\,r''(a(x-y)).
\]

The scalar shift \(s(a)\) does not affect multiplicity or parity ordering.

Let \(T\) be the self-adjoint operator associated with
\(\overline{\mathcal L}\).  Its spectrum is discrete.

Write

\[
\mu_{+,1}\le\mu_{+,2}\le\cdots
\]

for the even-sector eigenvalues of \(T\), and

\[
\mu_{-,1}\le\mu_{-,2}\le\cdots
\]

for the odd-sector eigenvalues.

## 3. Explicit limiting odd-sector lower bound

Let \(w\) be odd and normalized:

\[
\|w\|_{L^2(-1,1)}=1.
\]

Write \(f=w|_{(0,1)}\), so

\[
\int_0^1|f(x)|^2\,dx=\frac12.
\]

Keep only the cross-quadrant contribution in the nonnegative jump term.
Since \(w(-y)=-f(y)\),

\[
\frac14\iint
\frac{|w(x)-w(y)|^2}{|x-y|}
\ge
\frac12
\int_0^1\int_0^1
\frac{|f(x)+f(y)|^2}{x+y}\,dx\,dy.
\]

Expanding the right-hand side gives

\[
\int_0^1
|f(x)|^2\log\frac{1+x}{x}\,dx
+
\operatorname{Re}
\int_0^1\int_0^1
\frac{f(x)\overline{f(y)}}{x+y}\,dx\,dy.
\]

The second term is nonnegative because

\[
\frac1{x+y}
=
\int_0^\infty e^{-t(x+y)}\,dt,
\]

hence

\[
\int_0^1\int_0^1
\frac{f(x)\overline{f(y)}}{x+y}\,dx\,dy
=
\int_0^\infty
\left|
\int_0^1f(x)e^{-tx}\,dx
\right|^2dt
\ge0.
\]

The potential term is

\[
-\int_0^1|f(x)|^2\log(1-x^2)\,dx.
\]

Therefore

\[
\overline{\mathcal L}(w)
\ge
\int_0^1
|f(x)|^2
\left[
\log\frac{1+x}{x}
-\log(1-x^2)
\right]dx.
\]

The bracket simplifies to

\[
-\log(x(1-x)).
\]

Since

\[
x(1-x)\le\frac14,
\]

we obtain

\[
\overline{\mathcal L}(w)
\ge
(\log4)\frac12
=
\log2.
\]

Thus

\[
\boxed{\mu_{-,1}\ge\log2.}
\]

The estimate extends from the smooth/form-core domain to the closed odd
form by lower semicontinuity.

## 4. Explicit even ground upper bound

The normalized constant gives the baseline bound

\[
\mu_{+,1}\le1-\log2.
\]

A sharper fully explicit trial is

\[
p(x)=1-\frac{x^2}{2}.
\]

This even polynomial belongs to the closed limiting form domain.  Direct
integration gives

\[
\|p\|^2
=
\int_{-1}^{1}\left(1-\frac{x^2}{2}\right)^2dx
=
\frac{43}{30}.
\]

For the jump term, using symmetry and
\(p(x)-p(y)=-(x-y)(x+y)/2\),

\[
\frac14
\iint_{[-1,1]^2}
\frac{|p(x)-p(y)|^2}{|x-y|}\,dx\,dy
=
\frac1{15}.
\]

For the logarithmic potential term,

\[
-\frac12
\int_{-1}^{1}
p(x)^2\log(1-x^2)\,dx
=
\frac{569}{450}
-
\frac{43}{30}\log2.
\]

Therefore

\[
\overline{\mathcal L}(p)
=
\frac{599}{450}
-
\frac{43}{30}\log2,
\]

and the Rayleigh quotient is

\[
\frac{\overline{\mathcal L}(p)}{\|p\|^2}
=
\frac{599}{645}-\log2.
\]

Hence

\[
\boxed{
\mu_{+,1}
\le
\frac{599}{645}-\log2.
}
\]

This strictly improves \(1-\log2\).

## 5. Explicit second-even lower bound

Let \(w\) be even, normalized, and orthogonal to the constant \(c\).
Write again \(f=w|_{(0,1)}\).

Then

\[
\int_0^1f(x)\,dx=0,
\qquad
\int_0^1|f(x)|^2dx=\frac12.
\]

Split the nonnegative jump term into the two same-sign quadrants
and the two cross-sign quadrants.  Since \(w\) is even, both contributions
contain \(|f(x)-f(y)|^2\):

\[
\frac14\iint_{[-1,1]^2}
\frac{|w(x)-w(y)|^2}{|x-y|}\,dx\,dy
=
\frac12\int_0^1\int_0^1
|f(x)-f(y)|^2
\left(
\frac1{|x-y|}+\frac1{x+y}
\right)dx\,dy.
\]

For \(x,y\in(0,1)\),

\[
\frac1{|x-y|}\ge1,
\qquad
\frac1{x+y}\ge\frac12
\]

off the diagonal.  The potential term in \(\overline{\mathcal L}\) is
also nonnegative. Therefore

\[
\overline{\mathcal L}(w)
\ge
\frac34
\int_0^1\int_0^1
|f(x)-f(y)|^2\,dx\,dy.
\]

The mean-zero condition gives

\[
\int_0^1\int_0^1
|f(x)-f(y)|^2\,dx\,dy
=
2\int_0^1|f(x)|^2dx
-
2\left|\int_0^1f(x)dx\right|^2
=
1.
\]

Hence

\[
\overline{\mathcal L}(w)\ge\frac34.
\]

By the max–min characterization of the second even eigenvalue, choosing
the one-dimensional comparison subspace \(\operatorname{span}\{c\}\),

\[
\boxed{\mu_{+,2}\ge\frac34.}
\]

Consequently,

\[
\mu_{+,2}-\mu_{+,1}
\ge
\log2+\frac34-\frac{599}{645}
=
\log2-\frac{461}{2580},
\]

and

\[
\mu_{-,1}-\mu_{+,1}
\ge
2\log2-\frac{599}{645}.
\]

These are the strengthened explicit limiting simplicity and parity margins.

## 6. Exact bound on the small-\(a\) remainder

Suzuki decomposes

\[
r=r_0+r_1
\]

with

\[
r_0(t)=-4(e^{t/2}+e^{-t/2}-2)
\]

and, for \(t>0\),

\[
r_1''(t)
=
\frac{e^{-t/2}}{1-e^{-2t}}
-\frac1{2t}
=
\frac{e^{t/2}}{2\sinh t}-\frac1{2t}.
\]

Thus

\[
r_0''(t)=-2\cosh(t/2).
\]

Put

\[
h(t)=\frac{t e^{t/2}}{\sinh t}.
\]

Then

\[
r_1''(t)=\frac{h(t)-1}{2t}.
\]

For \(t>0\),

\[
\frac{h'(t)}{h(t)}
=
\frac1t+\frac12-\coth t.
\]

Use the standard partial-fraction expansion

\[
\coth t-\frac1t
=
2t\sum_{n\ge1}\frac1{t^2+\pi^2n^2}
\le
\frac t3.
\]

Hence, for \(0<t\le\log2\),

\[
0<
\frac12-\frac t3
\le
\frac{h'(t)}{h(t)}
\le
\frac12.
\]

So \(h\) is increasing, \(h(0)=1\), and

\[
h(t)\le e^{t/2}\le\sqrt2.
\]

Therefore

\[
0\le h'(t)\le\frac{\sqrt2}{2},
\]

and the mean-value theorem gives

\[
0\le r_1''(t)\le\frac{\sqrt2}{4}.
\]

The same differential inequality also gives a lower bound.
Because \(h\ge1\) and

\[
\frac{h'(t)}{h(t)}
\ge
\frac12-\frac t3,
\]

one has

\[
h'(t)
\ge
\frac12-\frac t3.
\]

Integrating from \(0\) to \(t\),

\[
h(t)-1
\ge
\frac t2-\frac{t^2}{6},
\]

and hence

\[
r_1''(t)
=
\frac{h(t)-1}{2t}
\ge
\frac14-\frac t{12}.
\]

Since the earlier upper bound on \(r_1''\) is \(<2\cosh(t/2)\),
\(r''(t)<0\).  Therefore, for \(|t|\le2a\le\log2\),

\[
|r''(t)|
=
2\cosh(t/2)-r_1''(t)
\le
2\cosh a-\frac14+\frac a6.
\]

Thus

\[
|K_a(x,y)|
\le
a\left(
2\cosh a-\frac14+\frac a6
\right).
\]

The Schur bound on the interval of length \(2\) gives

\[
\boxed{
\|K_a\|
\le
4a\cosh a-\frac a2+\frac{a^2}{3}.
}
\]

Set

\[
\eta(a)
=
4a\cosh a-\frac a2+\frac{a^2}{3}.
\]

## 7. Perturbation transfer

Since \(K_a\) is bounded and self-adjoint, the min--max principle gives

\[
|\nu_{\pm,j}(a)-\mu_{\pm,j}|
\le
\eta(a),
\]

with

\[
\eta(a)
=
4a\cosh a-\frac a2+\frac{a^2}{3}.
\]

Thus the even-sector internal gap satisfies

\[
\nu_{+,2}(a)-\nu_{+,1}(a)
\ge
\log2-\frac{461}{2580}-2\eta(a),
\]

and the parity gap satisfies

\[
\nu_{-,1}(a)-\nu_{+,1}(a)
\ge
2\log2-\frac{599}{645}-2\eta(a).
\]

Use

\[
\log2>\frac{693}{1000}.
\]

For \(0<a\le1/16\), the elementary series bound

\[
\cosh a
=
\sum_{n\ge0}\frac{a^{2n}}{(2n)!}
\le
\sum_{n\ge0}\left(\frac{a^2}{2}\right)^n
=
\frac1{1-a^2/2}
\]

gives

\[
\cosh a
\le
\frac{512}{511}.
\]

Moreover,

\[
2\eta(a)
=
8a\cosh a-a+\frac{2a^2}{3}
\]

is strictly increasing for \(a>0\). Hence on \(0<a\le1/16\),

\[
2\eta(a)
\le
8\cdot\frac1{16}\cdot\frac{512}{511}
-
\frac1{16}
+
\frac1{384}
=
\frac{86551}{196224}.
\]

Therefore the even-sector internal gap obeys

\[
\log2-\frac{461}{2580}-2\eta(a)
>
\frac{693}{1000}
-
\frac{461}{2580}
-
\frac{86551}{196224}
=
\boxed{
\frac{25747149}{351568000}
}
>
0,
\]

and the parity gap obeys

\[
2\log2-\frac{599}{645}-2\eta(a)
>
\frac{693}{500}
-
\frac{599}{645}
-
\frac{86551}{196224}
=
\boxed{
\frac{5707773}{351568000}
}
>
0.
\]

Hence throughout

\[
0<a\le\frac1{16},
\]

the lowest even eigenvalue is simple, the odd spectral bottom lies
strictly above it, and the full ground state is simple and even.

At \(a=1/15\), this same chain of explicit lower and upper bounds no longer
has positive parity-margin slack.  No failure of the theorem at \(1/15\)
is inferred; only this perturbative certificate stops closing there.

## 8. Explicit positivity

The limiting form is nonnegative:

\[
\overline{\mathcal L}\ge0.
\]

Therefore

\[
\lambda_a
\ge
-\log a-(2A+1)-\eta(a).
\]

Suzuki's constant satisfies

\[
2A+1=\log(2\pi)+C_0.
\]

For \(0<a\le1/50\), first bound the sharpened remainder itself.
The function

\[
\eta(a)=4a\cosh a-\frac a2+\frac{a^2}{3}
\]

is increasing for \(a>0\), since

\[
\eta'(a)
=
4\cosh a+4a\sinh a-\frac12+\frac{2a}{3}
>
0.
\]

Also

\[
\cosh a
\le
\frac{1}{1-a^2/2}
\le
\frac{5000}{4999}.
\]

Therefore

\[
\eta(a)
\le
\eta(1/50)
\le
\frac4{50}\frac{5000}{4999}
-\frac1{100}
+\frac1{7500}
=
\frac{1315037}{18746250}
<
\frac9{100}.
\]

Use also the coarse elementary bounds

\[
\log50>\frac72,
\qquad
\log(2\pi)<2,
\qquad
C_0<1.
\]

For example, \(\log50>7/2\) follows from
\(e<3\) and \(\sqrt e<\sqrt3<7/4\), which give
\(e^{7/2}<27\cdot7/4<50\).

Thus

\[
\lambda_a
>
\frac72-3-\frac9{100}
=
\frac{41}{100}
>
0.
\]

So the ground eigenvalue is strictly positive throughout the claimed interval.

## 9. Effective theorem

Section 7 gives the structural theorem

\[
\boxed{
0<a\le\frac1{16}
\Longrightarrow
\begin{cases}
\lambda_a\text{ is simple},\\
v_a\text{ is even},\\
\epsilon_+(e^a)<\epsilon_-(e^a).
\end{cases}
}
\]

Section 8 supplies the additional positivity certificate

\[
\boxed{
0<a\le\frac1{50}
\Longrightarrow
\lambda_a>0.
}
\]

Therefore:

- \(e^{1/16}\) is an explicit conservative simple-even cutoff;
- \(e^{1/50}\) is an explicit conservative positive-simple-even cutoff.

No claim is made that either cutoff is maximal.

## 10. Falsification checks

The proof depends on the following exact points.

1. The prime sum must be absent.
   For the larger structural interval,
   \(2a\le1/8<\log2\), so the no-prime formula still applies.

2. The constant must belong to the closed limiting form domain.
   This follows because the fixed-\(a\) closed forms differ from
   \(\overline{\mathcal L}\) by bounded forms in the no-prime regime and
   the localized Weil form domain contains constants. This domain bridge
   must be retained explicitly in final review.

3. The odd Hilbert-kernel term is nonnegative.
   This follows from the Laplace representation of \(1/(x+y)\).

4. The second-even estimate uses max–min, not an assumption that the
   constant is the ground eigenfunction.

5. The remainder estimate is an operator-norm bound. It does not infer
   eigenvalue stability from pointwise kernel agreement.

6. All multiplicity and parity conclusions are made only inside the
   explicit no-prime interval.

## 11. Claim boundary

This theorem does not prove:

- simplicity/evenness for \(a>1/16\);
- monotonic continuation of the parity gap;
- any statement at \(a=\tfrac12\log13\) or
  \(a=\tfrac12\log14\);
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority.

## 12. Admission dependency

This package is deliberately not yet linked into the canonical RH handoff.

Before admission:

1. MATHFORGE PR #271 must merge and its protected exact SHA must replace
   the provider placeholder;
2. the proof must receive exact-head Adversary and Referee passes;
3. standard Solve/GCL checks must pass on the final live-base composition.

Terminal candidate disposition:

RH-R040_EFFECTIVE_SMALL_A_SIMPLE_EVEN_PROVED_ON_WORK_BRANCH__AWAITING_PROVIDER_PROTECTION
