# RH-R050-TRIAL-REWEIGHTED-EXTENSION-001

Campaign: RH-001

Status:
ADMISSION_CANDIDATE__INDEPENDENT_CHECK_COMPLETE

Solve tracker:
grandchallenge/MATHSOLVE#408

Protected dependencies:
- grandchallenge/MATHSOLVE@79531354b7e8982835e0883286319f362560bb95:work_packages/RH_R049_HIGHER_ODD_COERCIVITY.md
- grandchallenge/MATHSOLVE@618840447a59af771ca7ce13a6f15cce3c3a5c06:work_packages/RH_R048_SECTOR_COERCIVITY_EXTENSION.md
- grandchallenge/MATHSOLVE@e5aae5f07492562da0edb4d9d9b35f0e01afa6d6:work_packages/RH_R047_INTEGRATED_REMAINDER_EXTENSION.md
- grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md

No RH / novelty / priority / certification claim.

## 1. Purpose

Protected R049 proves the full simple-even theorem through

\[
0<a=\log\lambda\le\frac{17}{100}.
\]

The remaining explicit parity-gap margin is small.  This package makes two
controlled improvements:

1. retain the next positive logarithmic-potential term \(u^8/4\) in the
   limiting odd-sector coercivity estimate;
2. replace the protected quadratic even trial
   \(1-\frac23x^2\) by the rational positive trial
   \[
   p(x)=1-\frac7{10}x^2.
   \]

The protected integrated smooth-remainder argument is extended only from
\(t\le17/50\) to \(t\le171/500\); the same Lipschitz constant \(11/50\)
still closes.

These changes prove the full simple-even theorem through

\[
\boxed{
0<a\le\frac{171}{1000}.
}
\]

## 2. One more positive logarithmic-potential term

Retain the protected R049 odd-sector decomposition.  With

\[
u=2x-1,
\]

R049 uses the weight

\[
W_3(u)
=
1+u^2+\frac12u^4+\frac13u^6
\]

and proves

\[
\overline{\mathcal L}(w)
\ge
\log2+A_3(f)-|m|^2,
\]

for odd normalized \(w\), where

\[
A_3(f)
=
\int_0^1 W_3(u)|f(x)|^2\,dx,
\qquad
m=\int_0^1 f(x)\,dx,
\]

and

\[
\int_0^1|f|^2=\frac12.
\]

Use the next positive term in

\[
-\log(1-u^2)
=
\sum_{n\ge1}\frac{u^{2n}}n:
\]

\[
-\log(1-u^2)
\ge
u^2+\frac12u^4+\frac13u^6+\frac14u^8.
\]

Define

\[
W_4(u)
=
W_3(u)+\frac14u^8.
\]

Then

\[
\boxed{
\overline{\mathcal L}(w)
\ge
\log2+A_4(f)-|m|^2,
}
\]

where

\[
A_4(f)
=
\int_0^1W_4(u)|f(x)|^2\,dx.
\]

Since \(W_4\ge1\),

\[
A_4(f)\ge\frac12.
\]

## 3. Weighted-Cauchy bound for W4

Weighted Cauchy gives

\[
|m|^2
\le
A_4(f) I_4,
\]

where

\[
I_4
=
\int_0^1
\frac{du}{W_4(u)}.
\]

Write

\[
b(u)=\frac14u^8.
\]

Then

\[
\frac1{W_3+b}
=
\frac1{W_3}
-
\frac{b}{W_3(W_3+b)}.
\]

Protected R049 proves

\[
\int_0^1\frac{du}{W_3(u)}
<
\frac{1013}{1344}.
\]

For \(0\le u\le1\),

\[
W_3(u)
\le
1+\frac{11}{6}u^2,
\]

and

\[
W_3(u)+b(u)
\le
1+\frac{25}{12}u^2.
\]

Therefore

\[
\begin{aligned}
W_3(u)(W_3(u)+b(u))
&\le
\left(1+\frac{11}{6}u^2\right)
\left(1+\frac{25}{12}u^2\right)
\\
&=
1+\frac{47}{12}u^2+\frac{275}{72}u^4
\\
&\le
1+8u^2
\\
&\le9.
\end{aligned}
\]

Hence

\[
\frac{b(u)}{W_3(u)(W_3(u)+b(u))}
\ge
\frac{u^8}{36}.
\]

Integrating,

\[
\begin{aligned}
I_4
&<
\frac{1013}{1344}
-
\int_0^1\frac{u^8}{36}\,du
\\
&=
\frac{1013}{1344}
-
\frac1{324}
\\
&=
\boxed{
\frac{27239}{36288}
}.
\end{aligned}
\]

Thus

\[
A_4(f)-|m|^2
>
\left(
1-\frac{27239}{36288}
\right)
A_4(f)
\ge
\frac{9049}{36288}\cdot\frac12.
\]

Therefore

\[
\boxed{
\mu_{-,1}
>
\log2+\frac{9049}{72576}.
}
\]

## 4. Reweighted positive even trial

Use

\[
\boxed{
p(x)=1-\frac7{10}x^2.
}
\]

It is strictly positive on \([-1,1]\).

Direct integration gives

\[
\boxed{
\|p\|^2=\frac{947}{750}
}
\]

and

\[
\boxed{
\int_{-1}^{1}p(x)\,dx=\frac{23}{15}.
}
\]

For a general quadratic trial \(1-cx^2\), the limiting form numerator is

\[
\frac{22}{25}c^2-\frac{16}{9}c+2
-
\|1-cx^2\|^2\log2.
\]

At \(c=7/10\), Rayleigh--Ritz therefore gives

\[
\boxed{
\mu_{+,1}
\le
\frac{13351}{14205}-\log2.
}
\]

The positive constant rank-one contribution is

\[
\frac{
(7a/4)\left(\int p\right)^2
}{
\|p\|^2
}
=
\boxed{
\frac{18515}{5682}a.
}
\]

Also

\[
\iint_{[-1,1]^2}
|x-y|p(x)p(y)\,dx\,dy
=
\frac{2568}{1995},
\]

so

\[
\frac{
\iint |x-y|p(x)p(y)\,dx\,dy
}{
\|p\|^2
}
=
\boxed{
\frac{1020}{947}.
}
\]

## 5. Extend q-prime through t = 171/500

Retain the protected R049 integrated envelope

\[
-r_1'''(t)
\le
B_*(t),
\]

with

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
\right),
\]

whenever \(h(t)\le6/5\).

For

\[
0\le t\le\frac{171}{500},
\]

one has

\[
\frac t2\le\frac{171}{1000}<\frac9{50}
<
\log\frac65,
\]

using the protected elementary estimate

\[
\log\frac65>\frac9{50}.
\]

Thus

\[
h(t)\le e^{t/2}<\frac65.
\]

The bracket in \(B_*(t)\) is increasing on this interval, so

\[
B_*(t)
\le
B_*(171/500)
<
\frac{23}{500}.
\]

For

\[
x=\frac t2\le\frac{171}{1000},
\]

the protected elementary estimate

\[
\sinh x
\le
\frac{x}{1-x^2/2}
\]

gives

\[
\sinh(t/2)
<
\frac{87}{500}.
\]

Therefore

\[
0\le q'(t)
<
\frac{23}{500}+\frac{87}{500}
=
\boxed{
\frac{11}{50}
}
\]

through \(t=171/500\).

Hence

\[
\boxed{
0
\le
q(t)-\frac74
\le
\frac{11}{50}t
\qquad
(0\le t\le171/500).
}
\]

## 6. Parity-sensitive remainder bounds

Assume

\[
0<a\le\frac{171}{1000}.
\]

Then

\[
2a\le\frac{171}{500}
<
\frac{693}{1000}
<
\log2,
\]

so the no-prime formula remains valid.

Set

\[
L=\frac{11}{50}.
\]

Protected R045-R049 give the general Lipschitz-budget estimates

\[
\boxed{
\|K_{a,-}\|
\le
La^2
=
\frac{11}{50}a^2,
}
\]

and

\[
\boxed{
\|E_a\|
\le
2La^2
=
\frac{11}{25}a^2.
}
\]

Using protected R048's second-even lower bound,

\[
\boxed{
\nu_{+,2}(a)
\ge
1-\frac{11}{25}a^2.
}
\]

Using Section 3,

\[
\boxed{
\nu_{-,1}(a)
>
\log2+\frac{9049}{72576}
-
\frac{11}{50}a^2.
}
\]

## 7. Even-ground upper bound with the new trial

Section 4 and the \(L=11/50\) residual budget give

\[
\boxed{
\nu_{+,1}(a)
\le
\frac{13351}{14205}-\log2
+
\frac{18515}{5682}a
+
\frac{2244}{9470}a^2.
}
\]

Indeed,

\[
\frac{11}{50}\frac{1020}{947}
=
\frac{2244}{9470}.
\]

## 8. Strict parity gap through a = 171/1000

Subtract Section 7 from the odd lower bound:

\[
\begin{aligned}
\nu_{-,1}(a)-\nu_{+,1}(a)
>{}&
2\log2
+
\frac{9049}{72576}
-
\frac{13351}{14205}
\\
&-
\frac{18515}{5682}a
-
\left(
\frac{2244}{9470}
+
\frac{11}{50}
\right)a^2.
\end{aligned}
\]

The right side decreases for \(a>0\).

At

\[
a=\frac{171}{1000},
\]

use

\[
\log2>\frac{693}{1000}.
\]

Exact arithmetic gives

\[
\boxed{
\nu_{-,1}(a)-\nu_{+,1}(a)
>
\frac{775974967}{3355931250000}
>
0.
}
\]

Therefore

\[
\boxed{
\epsilon_+(e^a)<\epsilon_-(e^a)
\qquad
(0<a\le171/1000).
}
\]

## 9. Even-sector simplicity through a = 171/1000

Sections 6 and 7 give

\[
\begin{aligned}
\nu_{+,2}(a)-\nu_{+,1}(a)
\ge{}&
\log2
+
1
-
\frac{13351}{14205}
\\
&-
\frac{18515}{5682}a
-
\left(
\frac{2244}{9470}
+
\frac{11}{25}
\right)a^2.
\end{aligned}
\]

Again the right side decreases for \(a>0\).

At \(a=171/1000\),

\[
\boxed{
\nu_{+,2}(a)-\nu_{+,1}(a)
>
\frac{12508575979}{71025000000}
>
0.
}
\]

Thus the lowest even-sector eigenvalue is simple throughout
\(0<a\le171/1000\).

## 10. Theorem

### RH-R050-TRIAL-REWEIGHTED-EXTENSION-001

For every

\[
0<a=\log\lambda\le\frac{171}{1000},
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
\frac{775974967}{3355931250000}
}
\]

and

\[
\boxed{
\epsilon_{+,2}(\lambda)-\epsilon_{+,1}(\lambda)
>
\frac{12508575979}{71025000000}.
}
\]

The common scalar shift does not affect multiplicity or parity ordering.

No positivity of the full ground eigenvalue is claimed on the full
interval.

## 11. Method consequence

This tranche demonstrates that two independent sources of slack remain:

- additional positive logarithmic-potential terms improve odd coercivity;
- the even positive trial can be retuned as \(a\) increases.

The improvement from \(17/100\) to \(171/1000\) is deliberately small.
Further micro-optimization of the same one-dimensional trial family is not
a preferred research direction.

A subsequent tranche should either:

- use a genuinely richer positive trial space with a clean analytic bound;
- derive a stronger odd-sector coercivity inequality not based only on
  truncating the logarithmic series;
- or switch to the protected Herglotz continuation interface.

## 12. False-proof firewall

Reject:

1. dropping positivity of the remainder logarithmic series after the
   \(u^8/4\) truncation;
2. using the \(W_4\) denominator bound outside \(0\le u\le1\);
3. using the \(11/50\) slope certificate beyond \(t=171/500\);
4. reusing the old \(c=2/3\) trial constants after changing to \(c=7/10\);
5. inferring ground positivity on all \(a\le171/1000\);
6. treating this small endpoint improvement as evidence for an all-\(a\)
   statement;
7. inferring determinant convergence or RH.

## 13. Claim boundary

This theorem does not prove:

- simple-even ground state for \(a>171/1000\);
- positivity of the ground eigenvalue for \(1/50<a\le171/1000\);
- monotonicity of the true parity gap;
- positivity at the R039 points;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 14. Admission dependency

Before admission:

1. the theorem must be composed onto the current live Solve head;
2. exact-head Adversary and Referee passes must be recorded;
3. required Solve/GCL checks must be green;
4. protected merge and readback must complete.

Terminal candidate disposition:

RH-R050_SIMPLE_EVEN_PROVED_THROUGH_171_OVER_1000__READY_FOR_EXACT_HEAD_ADMISSION
