# RH-R051-RANK-ONE-COERCIVITY-EXTENSION-001

Campaign: RH-001

Status:
ADMISSION_CANDIDATE__INDEPENDENT_CHECK_COMPLETE

Solve tracker:
grandchallenge/MATHSOLVE#417

Protected dependencies:
- grandchallenge/MATHSOLVE@7387aa8993355ab854630cf0683b4120a813884c:work_packages/RH_R050_TRIAL_REWEIGHTED_EXTENSION.md
- grandchallenge/MATHSOLVE@79531354b7e8982835e0883286319f362560bb95:work_packages/RH_R049_HIGHER_ODD_COERCIVITY.md
- grandchallenge/MATHSOLVE@618840447a59af771ca7ce13a6f15cce3c3a5c06:work_packages/RH_R048_SECTOR_COERCIVITY_EXTENSION.md
- grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md

No RH / novelty / priority / certification claim.

## 1. Purpose

Protected R050 proves the full simple-even theorem through

\[
0<a=\log\lambda\le\frac{171}{1000}.
\]

At that endpoint the explicit parity-gap margin was strictly positive but
narrow (\(\approx 2.31\times 10^{-4}\)).  In accordance with the Route A
doctrine, this work package avoids microscopic scalar retuning and instead
introduces two structural mathematical improvements:

1. an **exact rank-one coercivity theorem** for the odd limiting form, which
   eliminates the loose infimum replacement \(A(f)\ge 1/2\) used in
   R046–R050 and establishes the significantly stronger limiting odd bound
   \[
   \mu_{-,1}>\log 2+\frac{3}{20};
   \]
2. a **sharp parity-specific remainder bound** derived from the exact operator
   norm of the Green operator on \(L^2(0,1)\) with Dirichlet-Neumann boundary
   conditions, yielding
   \[
   \|K_{a,-}\|\le\frac{8}{\pi^2}L a^2<\frac{811}{1000}La^2,
   \]
   strictly improving on the generic Schur-test Lipschitz bound \(L a^2\);
3. an extension of the smooth-remainder slope certificate
   \(0\le q'(t)\le 23/100\) through \(t\le 89/250\).

Combining these structural results proves the full simple-even theorem
through

\[
\boxed{
0<a\le\frac{178}{1000}.
}
\]

## 2. Exact rank-one coercivity theorem

In protected predecessors R046–R050, the odd-sector limiting form was
decomposed as

\[
\overline{\mathcal L}(w)
\ge
\log2+A(f)-|m|^2,
\]

where \(w\) is an odd normalized function in the limiting closed form domain,
\(f=w|_{(0,1)}\) satisfies \(\int_0^1 |f(x)|^2\,dx=1/2\),
\(m=\int_0^1 f(x)\,dx\), and

\[
A(f)=\int_0^1 W(u)|f(x)|^2\,dx,
\qquad
u=2x-1\in(-1,1).
\]

Those packages applied the weighted Cauchy--Schwarz inequality
\(|m|^2\le A(f)I\) with \(I=\int_0^1 \frac{du}{W(u)}\) and then lower-bounded
\(A(f)-|m|^2\ge(1-I)A(f)\ge\frac{1}{2}(1-I)\) using only the pointwise
infimum \(W(u)\ge 1\).

The following general lemma provides an exact variational bound that bypasses
this loss.

### Lemma 2.1 (Rank-one coercivity bound)
Let \(W\in L^\infty((0,1))\) satisfy \(W(x)\ge 1\) almost everywhere.
Suppose there exists \(\lambda<1\) such that

\[
\int_0^1\frac{dx}{W(x)-\lambda}\le 1.
\]

Then for every \(f\in L^2(0,1)\) with \(\int_0^1 |f(x)|^2\,dx=\frac12\),

\[
\boxed{
\int_0^1 W(x)|f(x)|^2\,dx-\left|\int_0^1 f(x)\,dx\right|^2\ge\frac12\lambda.
}
\]

#### Proof
Since \(\lambda<1\) and \(W(x)\ge 1\), we have \(W(x)-\lambda>0\) almost
everywhere on \((0,1)\).  Write

\[
f(x)=\sqrt{W(x)-\lambda}f(x)\cdot\frac{1}{\sqrt{W(x)-\lambda}}.
\]

Applying the Cauchy--Schwarz inequality yields

\[
\begin{aligned}
|m|^2
=
\left|\int_0^1 f(x)\,dx\right|^2
&\le
\left(\int_0^1 (W(x)-\lambda)|f(x)|^2\,dx\right)
\left(\int_0^1\frac{dx}{W(x)-\lambda}\right)
\\
&\le
\int_0^1 (W(x)-\lambda)|f(x)|^2\,dx,
\end{aligned}
\]

where the second inequality uses the hypothesis
\(\int_0^1\frac{dx}{W(x)-\lambda}\le 1\).

Expanding the right-hand side gives

\[
|m|^2
\le
\int_0^1 W(x)|f(x)|^2\,dx-\lambda\int_0^1|f(x)|^2\,dx
=
A(f)-\frac12\lambda.
\]

Rearranging gives \(A(f)-|m|^2\ge\frac12\lambda\), completing the proof.
\(\blacksquare\)

## 3. Limiting odd lower bound via Lemma 2.1

Retain the protected R050 weight

\[
W_4(u)=1+u^2+\frac12u^4+\frac13u^6+\frac14u^8.
\]

Set \(\lambda=\frac{3}{10}<1\).  Then

\[
P(u):=W_4(u)-\frac{3}{10}=\frac{7}{10}+u^2+\frac12u^4+\frac13u^6+\frac14u^8.
\]

The polynomial \(P(u)\) is positive and strictly increasing on \([0,1]\).
Subdivide \([0,1]\) into \(N=22\) equal subintervals
\([u_i, u_{i+1}]=[i/22, (i+1)/22]\) for \(i=0,1,\dots,21\).

Since \(P(u)\) is increasing, on each subinterval \([u_i, u_{i+1}]\) we have
\(P(u)\ge P(u_i)\), whence

\[
\int_0^1\frac{du}{P(u)}
\le
\frac{1}{22}\sum_{i=0}^{21}\frac{1}{P(i/22)}.
\]

Direct rational evaluation of this finite sum gives

\[
\frac{1}{22}\sum_{i=0}^{21}\frac{1}{P(i/22)}
=
\frac{17912514401995935440029751192363085856978822195553339579410994352205797813938971656759277094055037492654005401079693385887542018471473072475357681314911890972913511536046166434295985876485801068349942923985924796875540}{17925401523984492395997528639518751843064729400143721688477332104137722177121322826874742853211484862818008291866263979144045146736185213287925167286645083010603938145659654088185104515764552075128694246929527311186823}
<
1.
\]

In decimals, the upper sum is \(\approx 0.99928107<1\).

Thus the hypothesis of Lemma 2.1 holds for \(W_4\) with \(\lambda=3/10\).
Consequently, for every odd normalized function \(w\),

\[
A_4(f)-|m|^2\ge\frac12\left(\frac{3}{10}\right)=\frac{3}{20}.
\]

Therefore

\[
\boxed{
\mu_{-,1}>\log 2+\frac{3}{20}.
}
\]

This strictly improves the protected R050 bound
\(\log 2+9049/72576\approx\log 2+0.12468\).

## 4. Sharp parity-specific remainder bound via the Green operator norm

Let \(L\) be a Lipschitz constant for \(q\) on \([0,2a]\).
As established in R045, the reduced odd remainder kernel on \(L^2(0,1)\) is

\[
K_{a,-}(x,y)=a\left[q(a|x-y|)-q(a(x+y))\right].
\]

Because \(q\) is increasing on \([0,2a]\) and \(|x-y|\le x+y\), we have
\(K_{a,-}(x,y)\le 0\), and

\[
|K_{a,-}(x,y)|\le 2La^2\min(x,y).
\]

Let \(T\) be the integral operator on \(L^2(0,1)\) with kernel
\(k(x,y)=2\min(x,y)\).

### Lemma 4.1 (Green operator norm bound)
The integral operator \(T\) on \(L^2(0,1)\) with kernel \(2\min(x,y)\)
satisfies

\[
\boxed{
\|T\|_{L^2(0,1)\to L^2(0,1)}=\frac{8}{\pi^2}<\frac{811}{1000}.
}
\]

#### Proof
Let \(u\in L^2(0,1)\) and set \(g(x)=\int_0^1\min(x,y)u(y)\,dy\).
Then

\[
g(x)=\int_0^x y u(y)\,dy+x\int_x^1 u(y)\,dy.
\]

Differentiating,

\[
g'(x)=\int_x^1 u(y)\,dy,
\qquad
g''(x)=-u(x).
\]

The function \(g\) satisfies the boundary conditions \(g(0)=0\) and
\(g'(1)=0\).  Thus \(g\) solves the boundary value problem

\[
-g''(x)=u(x),
\qquad
g(0)=0,
\quad
g'(1)=0.
\]

The differential operator \(-d^2/dx^2\) on \((0,1)\) with boundary conditions
\(g(0)=0, g'(1)=0\) is self-adjoint, strictly positive, and has compact
resolvent.  Its normalized eigenfunctions are

\[
\phi_k(x)=\sqrt{2}\sin\left(\left(k+\frac12\right)\pi x\right),
\qquad
k=0,1,2,\dots,
\]

with corresponding eigenvalues

\[
\lambda_k=\left(k+\frac12\right)^2\pi^2.
\]

The Green operator \(G=(-d^2/dx^2)^{-1}\) is bounded and self-adjoint on
\(L^2(0,1)\) with eigenvalues \(\lambda_k^{-1}\).  Its operator norm is its
largest eigenvalue:

\[
\|G\|_{L^2\to L^2}=\frac{1}{\lambda_0}=\frac{1}{(\pi/2)^2}=\frac{4}{\pi^2}.
\]

Since \(T=2G\), we obtain

\[
\|T\|_{L^2\to L^2}=2\|G\|_{L^2\to L^2}=\frac{8}{\pi^2}.
\]

Using the standard certified lower bound \(\pi>3.14159\),

\[
\pi^2>(3.14159)^2=9.8695877\dots>\frac{9869}{1000}.
\]

Hence

\[
\frac{8}{\pi^2}<\frac{8000}{9869}<\frac{811}{1000}.
\]

\(\blacksquare\)

### Consequence for the odd sector
Since \(|K_{a,-}(x,y)|\le La^2(2\min(x,y))\) and \(K_{a,-}(x,y)\le 0\),
for every normalized \(f\in L^2(0,1)\),

\[
|\langle f, K_{a,-}f\rangle|
\le
La^2\int_0^1\int_0^1 2\min(x,y)|f(x)||f(y)|\,dx\,dy
\le
La^2\|T\|\||f|\|^2
\le
\frac{811}{1000}La^2.
\]

Therefore

\[
\boxed{
\|K_{a,-}\|\le\frac{811}{1000}La^2.
}
\]

This strictly sharpens the generic Schur bound \(\|K_{a,-}\|\le La^2\) used
in all predecessors R045–R050.

## 5. Extending the smooth-remainder slope through t = 89/250

Retain the protected notation

\[
q(t)=-r''(t)=\sinh(t/2)-r_1'''(t),
\]

with

\[
-r_1'''(t)\le B_*(t)
=
\frac35\left(\frac{1}{24}+\frac t9-\frac{t^2}{30}+\frac{t^4}{2835}\right),
\]

valid whenever \(h(t)\le 6/5\).

For

\[
0\le t\le\frac{89}{250},
\]

one has

\[
\frac t2\le\frac{89}{500}=0.178<\frac{9}{50}=0.180<\log\frac65,
\]

using the protected elementary estimate \(\log(6/5)>9/50\).  Thus
\(h(t)\le e^{t/2}<6/5\) on this interval.

The bracket in \(B_*(t)\) is strictly increasing for \(0\le t\le 89/250\),
yielding

\[
B_*(t)\le B_*(89/250)=\frac{852751992241}{18457031250000}<0.046203.
\]

Using the protected elementary bound \(\sinh x\le \frac{x}{1-x^2/2}\) for
\(x=t/2\le 89/500\),

\[
\sinh(t/2)\le\frac{89/500}{1-(89/500)^2/2}=\frac{89000}{492079}<0.180866.
\]

Summing these bounds gives

\[
q'(t)<\frac{852751992241}{18457031250000}+\frac{89000}{492079}
=
\frac{294613875548565577}{1297473925781250000}
\approx 0.227067.
\]

Set

\[
\boxed{
L=\frac{23}{100}.
}
\]

Since \(0.227067<\frac{23}{100}\), we have proved

\[
\boxed{
0\le q'(t)<\frac{23}{100}
\qquad
\left(0\le t\le\frac{89}{250}\right).
}
\]

Integrating from \(0\) and using \(q(0)=7/4\),

\[
\boxed{
0\le q(t)-\frac74\le\frac{23}{100}t
\qquad
\left(0\le t\le\frac{89}{250}\right).
}
\]

## 6. Parity-sensitive remainder bounds

Assume

\[
0<a\le\frac{178}{1000}=\frac{89}{500}.
\]

Then

\[
2a\le\frac{89}{250}=0.356<\frac{693}{1000}<\log 2,
\]

so the no-prime formula remains strictly valid.

With \(L=23/100\):

### Odd sector
Section 4 yields

\[
\boxed{
\|K_{a,-}\|\le\frac{811}{1000}\left(\frac{23}{100}\right)a^2
=
\frac{18653}{100000}a^2.
}
\]

Combining with Section 3,

\[
\boxed{
\nu_{-,1}(a)>\log 2+\frac{3}{20}-\frac{18653}{100000}a^2.
}
\]

### Even sector
By protected R045/R048, the even-sector residual \(E_a\) satisfies

\[
\|E_a\|\le 2La^2=\frac{23}{50}a^2.
\]

Using protected R048's second-even lower bound \(\mu_{+,2}\ge 1\),

\[
\boxed{
\nu_{+,2}(a)\ge 1-\frac{23}{50}a^2.
}
\]

## 7. Even-ground trial bound

Retain the protected positive quadratic even trial

\[
p(x)=1-\frac{7}{10}x^2>0
\qquad
(x\in[-1,1]).
\]

Protected R050 evaluates the Rayleigh quotient and residual form ratios for
this trial:

\[
\frac{\overline{\mathcal L}(p)}{\|p\|^2}=\frac{13351}{14205}-\log 2,
\]

\[
\frac{(7a/4)\left(\int p\right)^2}{\|p\|^2}=\frac{18515}{5682}a,
\]

and

\[
\frac{\iint_{[-1,1]^2}|x-y|p(x)p(y)\,dx\,dy}{\|p\|^2}=\frac{1020}{947}.
\]

Multiplying the residual ratio by \(L=23/100\) gives

\[
\frac{23}{100}\cdot\frac{1020}{947}=\frac{1173}{4735}.
\]

Therefore

\[
\boxed{
\nu_{+,1}(a)\le\frac{13351}{14205}-\log 2+\frac{18515}{5682}a+\frac{1173}{4735}a^2.
}
\]

## 8. Strict parity gap through a = 178/1000

Subtracting the even-ground upper bound from the odd-ground lower bound gives

\[
\begin{aligned}
\nu_{-,1}(a)-\nu_{+,1}(a)
>{}&
2\log 2+\frac{3}{20}-\frac{13351}{14205}
\\
&-
\frac{18515}{5682}a
-
\left(\frac{1173}{4735}+\frac{18653}{100000}\right)a^2.
\end{aligned}
\]

The right side is strictly decreasing for \(a>0\).

At the endpoint

\[
a=\frac{178}{1000}=\frac{89}{500},
\]

substituting the protected certified bound \(\log 2>\frac{693}{1000}\) gives

\[
\begin{aligned}
\nu_{-,1}(a)-\nu_{+,1}(a)
&>
2\left(\frac{693}{1000}\right)+\frac{3}{20}-\frac{13351}{14205}
-
\frac{18515}{5682}\left(\frac{89}{500}\right)
-
\left(\frac{1173}{4735}+\frac{18653}{100000}\right)\left(\frac{89}{500}\right)^2
\\
&=
\boxed{
\frac{55428698889}{23675000000000}
}
\approx 0.00234123
>
0.
\end{aligned}
\]

By monotonicity, the parity gap is strictly positive for all
\(0<a\le 178/1000\):

\[
\boxed{
\epsilon_+(e^a)<\epsilon_-(e^a)
\qquad
\left(0<a\le\frac{178}{1000}\right).
}
\]

## 9. Even-sector simplicity through a = 178/1000

From Sections 6 and 7,

\[
\begin{aligned}
\nu_{+,2}(a)-\nu_{+,1}(a)
\ge{}&
\log 2+1-\frac{13351}{14205}
\\
&-
\frac{18515}{5682}a
-
\left(\frac{1173}{4735}+\frac{23}{50}\right)a^2.
\end{aligned}
\]

The right side is strictly decreasing for \(a>0\).

At \(a=89/500\), using \(\log 2>693/1000\), exact rational arithmetic gives

\[
\begin{aligned}
\nu_{+,2}(a)-\nu_{+,1}(a)
&>
\frac{693}{1000}+1-\frac{13351}{14205}
-
\frac{18515}{5682}\left(\frac{89}{500}\right)
-
\left(\frac{1173}{4735}+\frac{23}{50}\right)\left(\frac{89}{500}\right)^2
\\
&=
\boxed{
\frac{1783634369}{11837500000}
}
\approx 0.1506766
>
0.
\end{aligned}
\]

Thus the lowest even-sector eigenvalue is simple throughout
\(0<a\le 178/1000\).

## 10. Theorem

### RH-R051-RANK-ONE-COERCIVITY-EXTENSION-001

For every

\[
0<a=\log\lambda\le\frac{178}{1000},
\]

the full localized Weil operator has:

1. a strict parity gap \(\epsilon_+(\lambda)<\epsilon_-(\lambda)\);
2. a simple lowest even-sector eigenvalue.

Therefore, by protected RH-R036, the global ground eigenvalue is simple and
even.

Uniformly on the interval,

\[
\boxed{
\epsilon_-(\lambda)-\epsilon_+(\lambda)
>
\frac{55428698889}{23675000000000}
}
\]

and

\[
\boxed{
\epsilon_{+,2}(\lambda)-\epsilon_{+,1}(\lambda)
>
\frac{1783634369}{11837500000}.
}
\]

The common scalar shift does not affect multiplicity or parity ordering.

No positivity of the full ground eigenvalue is claimed on the full
interval.

## 11. Method consequence

This tranche establishes two general structural lemmas that significantly
expand the certified budget:

- Lemma 2.1 provides an exact variational bound for rank-one perturbations of
  positive operators, proving \(\mu_{-,1}>\log 2+\lambda/2\) whenever
  \(\int_0^1 \frac{dx}{W(x)-\lambda}\le 1\);
- Lemma 4.1 bounds the integral operator norm of \(2\min(x,y)\) by
  \(8/\pi^2<0.811\), reducing the odd-sector remainder budget by nearly 20%
  compared to generic Schur estimates.

Together, these structural improvements advance the explicit simple-even
regime from \(a=171/1000\) to \(a=178/1000\), an improvement seven times
larger than the increment from R049 to R050, while increasing the certified
endpoint gap margin from \(2.31\times 10^{-4}\) to \(2.34\times 10^{-3}\).

## 12. False-proof firewall

Reject:

1. using Lemma 2.1 with \(\lambda\ge 1\);
2. using Lemma 4.1 for the even-sector remainder where the kernel does not
   contain the same cancellation;
3. using the \(L=23/100\) slope certificate beyond \(t=89/250\);
4. omitting the rank-one term in the even-sector trial bound;
5. inferring ground positivity on all \(a\le 178/1000\);
6. reusing the no-prime formula past \(2a=\log 2\);
7. inferring determinant convergence or RH.

## 13. Claim boundary

This theorem does not prove:

- simple-even ground state for \(a>178/1000\);
- positivity of the ground eigenvalue for \(1/50<a\le 178/1000\);
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

RH-R051_SIMPLE_EVEN_PROVED_THROUGH_178_OVER_1000__READY_FOR_EXACT_HEAD_ADMISSION
