# RH-R049-HIGHER-ODD-COERCIVITY-001

Campaign: RH-001

Status:
ADMISSION_CANDIDATE__INDEPENDENT_CHECK_COMPLETE

Solve tracker:
grandchallenge/MATHSOLVE#405

Protected dependencies:
- grandchallenge/MATHSOLVE@618840447a59af771ca7ce13a6f15cce3c3a5c06:work_packages/RH_R048_SECTOR_COERCIVITY_EXTENSION.md
- grandchallenge/MATHSOLVE@e5aae5f07492562da0edb4d9d9b35f0e01afa6d6:work_packages/RH_R047_INTEGRATED_REMAINDER_EXTENSION.md
- grandchallenge/MATHSOLVE@cf414d991440c3f8a225b8438a7c524a56b1b76e:work_packages/RH_R046_ODD_LOWER_BOUND_EXTENSION.md
- grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md

No RH / novelty / priority / certification claim.

## 1. Purpose

Protected R048 proves the full simple-even theorem through

\[
0<a=\log\lambda\le\frac16.
\]

At that endpoint the active certified bottleneck is the parity-gap lower
bound.  This package strengthens the limiting odd-sector coercivity by
retaining one more positive term in the logarithmic potential, and extends
the integrated smooth-remainder estimate to a slightly larger interval.

The two new ingredients are:

1. a limiting odd lower bound
   \[
   \mu_{-,1}>
   \log2+\frac{331}{2688};
   \]
2. a smooth-remainder slope bound
   \[
   0\le q'(t)\le\frac{11}{50}
   \qquad
   (0\le t\le17/50).
   \]

Together with the protected R048 even-sector estimate
\(\mu_{+,2}\ge1\) and the protected positive even trial, these prove the
full simple-even theorem through

\[
\boxed{
0<a\le\frac{17}{100}.
}
\]

## 2. Retain the next positive logarithmic term

Let \(w\) be odd and normalized in the limiting closed form domain, and
write

\[
f=w|_{(0,1)},
\qquad
\int_0^1|f|^2=\frac12.
\]

Protected R048 gives

\[
\overline{\mathcal L}(w)
\ge
\log2+A_2(f)-|m|^2,
\qquad
m:=\int_0^1 f(x)\,dx,
\]

where, with

\[
u=2x-1,
\]

the weight is

\[
A_2(f)
=
\int_0^1
\left(
1+u^2+\frac12u^4
\right)
|f(x)|^2\,dx.
\]

Now use one more term of the positive expansion

\[
-\log(1-u^2)
=
\sum_{n\ge1}\frac{u^{2n}}n.
\]

For \(0\le u^2<1\),

\[
-\log(1-u^2)
\ge
u^2+\frac12u^4+\frac13u^6.
\]

Hence define

\[
A_3(f)
=
\int_0^1
W_3(x)|f(x)|^2\,dx,
\]

with

\[
W_3(x)
=
1+u^2+\frac12u^4+\frac13u^6.
\]

Then

\[
\boxed{
\overline{\mathcal L}(w)
\ge
\log2+A_3(f)-|m|^2.
}
\]

Since \(W_3\ge1\),

\[
A_3(f)\ge\frac12.
\]

## 3. Rational weighted-Cauchy bound

Weighted Cauchy gives

\[
|m|^2
\le
A_3(f) I_3,
\]

where symmetry under \(u\mapsto-u\) gives

\[
I_3
=
\int_0^1
\frac{du}{
1+u^2+\frac12u^4+\frac13u^6
}.
\]

Let

\[
W_2(u)=1+u^2+\frac12u^4,
\qquad
b(u)=\frac13u^6.
\]

Then

\[
\frac1{W_2+b}
=
\frac1{W_2}
-
\frac{b}{W_2(W_2+b)}.
\]

Protected R048 proves

\[
\int_0^1\frac{du}{W_2(u)}
<
\frac{1021}{1344}.
\]

It remains to bound the correction from below.

For \(0\le u\le1\),

\[
W_2(u)
\le
1+\frac32u^2,
\]

and

\[
W_2(u)+b(u)
\le
1+\frac{11}{6}u^2.
\]

Therefore

\[
\begin{aligned}
W_2(u)(W_2(u)+b(u))
&\le
\left(1+\frac32u^2\right)
\left(1+\frac{11}{6}u^2\right)
\\
&=
1+\frac{10}{3}u^2+\frac{11}{4}u^4
\\
&\le
1+7u^2
\\
&\le8.
\end{aligned}
\]

Hence

\[
\frac{b(u)}{W_2(u)(W_2(u)+b(u))}
\ge
\frac{u^6}{24}.
\]

Thus

\[
\begin{aligned}
I_3
&<
\frac{1021}{1344}
-
\int_0^1\frac{u^6}{24}\,du
\\
&=
\frac{1021}{1344}
-
\frac1{168}
\\
&=
\boxed{
\frac{1013}{1344}
}.
\end{aligned}
\]

Therefore

\[
A_3(f)-|m|^2
>
\left(
1-\frac{1013}{1344}
\right)
A_3(f)
\ge
\frac{331}{1344}\cdot\frac12.
\]

Consequently

\[
\boxed{
\mu_{-,1}
>
\log2+\frac{331}{2688}.
}
\]

This strictly strengthens the protected R048 bound
\(\log2+323/2688\).

## 4. Extending the integrated smooth-remainder envelope

Retain the protected R048 notation

\[
q(t)=-r''(t),
\]

\[
r_1''(t)=\frac{h(t)-1}{2t},
\qquad
h(t)=\frac{t e^{t/2}}{\sinh t},
\]

and the protected integrated envelope

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
\right)
\]

whenever \(h(t)\le6/5\).

For

\[
0\le t\le\frac{17}{50},
\]

one has

\[
\frac t2\le\frac{17}{100}.
\]

Also

\[
\log\frac65
=
\log\left(1+\frac15\right)
>
\frac15-\frac1{50}
=
\frac9{50}
>
\frac{17}{100},
\]

so

\[
h(t)\le e^{t/2}<\frac65.
\]

The bracket in \(B_*(t)\) is increasing because

\[
\frac19-\frac t{15}+\frac{4t^3}{2835}
\ge
\frac19-\frac{17}{750}
>
0.
\]

Hence

\[
B_*(t)
\le
B_*(17/50)
=
\frac{1339463521}{29531250000}
<
\frac{23}{500}.
\]

## 5. A 11/50 slope bound for q

For

\[
0\le t\le\frac{17}{50},
\]

put

\[
x=\frac t2\le\frac{17}{100}.
\]

Using the protected elementary bound

\[
\cosh s
\le
\frac1{1-s^2/2},
\]

one gets

\[
\sinh x
=
\int_0^x\cosh s\,ds
\le
\frac{x}{1-x^2/2}.
\]

At \(x=17/100\),

\[
\frac{x}{1-x^2/2}
=
\frac{3400}{19711}
<
\frac{87}{500}.
\]

Since \(r_1'''(t)\le0\),

\[
q'(t)
=
\sinh(t/2)-r_1'''(t)
\ge0.
\]

Sections 4 and 5 give

\[
q'(t)
<
\frac{87}{500}
+
\frac{23}{500}
=
\frac{11}{50}.
\]

Thus

\[
\boxed{
0\le q'(t)<\frac{11}{50}
\qquad
(0\le t\le17/50).
}
\]

Using \(q(0)=7/4\),

\[
\boxed{
0
\le
q(t)-\frac74
\le
\frac{11}{50}t
\qquad
(0\le t\le17/50).
}
\]

## 6. Modified parity-sensitive remainder bounds

Assume

\[
0<a\le\frac{17}{100}.
\]

Then

\[
2a\le\frac{17}{50}
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

The protected parity-sensitive kernel argument gives:

### Odd sector

\[
\boxed{
\|K_{a,-}\|
\le
La^2
=
\frac{11}{50}a^2.
}
\]

Hence

\[
\boxed{
\nu_{-,1}(a)
>
\log2+\frac{331}{2688}
-
\frac{11}{50}a^2.
}
\]

### Even sector

The positive constant rank-one part is unchanged and the residual obeys

\[
\boxed{
\|E_a\|
\le
2La^2
=
\frac{11}{25}a^2.
}
\]

Using protected R048,

\[
\boxed{
\nu_{+,2}(a)
\ge
1-\frac{11}{25}a^2.
}
\]

## 7. Even-ground trial

Retain the protected positive even trial

\[
p(x)=1-\frac23x^2.
\]

The constant rank-one contribution remains

\[
\frac{1715}{522}a.
\]

The residual trial ratio before multiplication by \(L\) is

\[
\frac{668}{609}.
\]

Therefore

\[
L\frac{668}{609}
=
\frac{3674}{15225}.
\]

Hence

\[
\boxed{
\nu_{+,1}(a)
\le
\frac{407}{435}-\log2
+
\frac{1715}{522}a
+
\frac{3674}{15225}a^2.
}
\]

## 8. Strict parity gap through a = 17/100

Subtract Section 7 from the odd lower bound:

\[
\begin{aligned}
\nu_{-,1}(a)-\nu_{+,1}(a)
>{}&
2\log2
+
\frac{331}{2688}
-
\frac{407}{435}
\\
&-
\frac{1715}{522}a
-
\left(
\frac{3674}{15225}
+
\frac{11}{50}
\right)a^2.
\end{aligned}
\]

The right side is decreasing for \(a>0\).

At

\[
a=\frac{17}{100},
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
\frac{6032129}{3654000000}
>
0.
}
\]

Therefore

\[
\boxed{
\epsilon_+(e^a)<\epsilon_-(e^a)
\qquad
(0<a\le17/100).
}
\]

## 9. Even-sector simplicity through a = 17/100

Sections 6 and 7 give

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
\frac{3674}{15225}
+
\frac{11}{25}
\right)a^2.
\end{aligned}
\]

Again the right side is decreasing for \(a>0\).

At \(a=17/100\), using \(\log2>693/1000\),

\[
\boxed{
\nu_{+,2}(a)-\nu_{+,1}(a)
>
\frac{81828109}{456750000}
>
0.
}
\]

Thus the lowest even-sector eigenvalue remains simple throughout
\(0<a\le17/100\).

## 10. Theorem

### RH-R049-HIGHER-ODD-COERCIVITY-001

For every

\[
0<a=\log\lambda\le\frac{17}{100},
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
\frac{6032129}{3654000000}
}
\]

and

\[
\boxed{
\epsilon_{+,2}(\lambda)-\epsilon_{+,1}(\lambda)
>
\frac{81828109}{456750000}.
}
\]

The common scalar shift does not affect multiplicity or parity ordering.

No positivity of the full ground eigenvalue is claimed on the full
interval.

## 11. Method consequence

At \(a=17/100\), the explicit parity-gap certificate is positive but small,
while the even-sector internal-gap certificate remains large.

The next obstruction is therefore again the parity-gap budget.

Further extension should prioritize:

- retaining still more positive logarithmic-potential terms;
- sharpening the weighted-Cauchy integral estimate;
- improving the positive even ground trial;
- sharpening the smooth-remainder slope;
- or using the protected Herglotz continuation interface.

No spectral failure beyond \(17/100\) is inferred.

## 12. False-proof firewall

Reject:

1. using the \(u^6/3\) term without preserving positivity of the remaining
   logarithmic series;
2. using the correction bound in Section 3 outside \(0\le u\le1\);
3. using \(q'\le11/50\) beyond \(t=17/50\);
4. retaining the R048 \(9/40\)-dependent remainder constants after changing
   to \(L=11/50\);
5. inferring ground positivity on all \(a\le17/100\);
6. inferring determinant convergence or RH.

## 13. Claim boundary

This theorem does not prove:

- simple-even ground state for \(a>17/100\);
- positivity of the ground eigenvalue for \(1/50<a\le17/100\);
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

RH-R049_SIMPLE_EVEN_PROVED_THROUGH_SEVENTEEN_HUNDREDTHS__READY_FOR_EXACT_HEAD_ADMISSION
