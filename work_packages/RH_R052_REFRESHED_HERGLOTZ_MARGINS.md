# RH-R052-REFRESHED-HERGLOTZ-MARGINS-001

Campaign: RH-001

Status:
ADMISSION_CANDIDATE__DEPENDENCIES_PROTECTED

Solve tracker:
grandchallenge/MATHSOLVE#431

Coordination:
grandchallenge/MATHSOLVE#412 (Forward Route B)

Protected dependencies:
- grandchallenge/MATHSOLVE@fdc539ba2b79b60e458a0ab4ac1370b03a0788bc:work_packages/RH_R051_RANK_ONE_COERCIVITY_EXTENSION.md
- grandchallenge/MATHSOLVE@9519ae68c96c33b1a71548a9984fef1be640a106:work_packages/RH_R041_ODD_HERGLOTZ_GAP_CRITERION.md
- grandchallenge/MATHSOLVE@1a34479235b47405a3ed185c0b1d21d6ad9be190:work_packages/RH_R042_PARITY_BOTTOM_PARAMETER_CONTINUITY.md
- grandchallenge/MATHSOLVE@12e390e455fd9c59d0a6283789073939c69db5de:work_packages/RH_R043_HERGLOTZ_MARGIN_CONTINUITY.md
- grandchallenge/MATHSOLVE@139f35f14ee831aa5aa3ed83b774b762965d58b3:work_packages/RH_R044_EXPLICIT_INITIAL_HERGLOTZ_MARGINS.md
- grandchallenge/MATHFORGE@f9aa9ad64812df42ad079958ecff88c84e0e4648:reports/discovery/rh_001/rh_r041_pole_resolvent_interface.md
- grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md

No RH / novelty / priority / certification claim.

## 1. Purpose

In Forward Route B (as codified in `handoffs/RH-001/routes/ROUTE_B_HERGLOTZ_CONTINUATION.md`),
continuation of the simple-even parity theorem is governed by two scalar/spectral
continuation margins:

\[
d(a)
=
\inf\sigma(B_{a,-})
-
\epsilon_+(e^a),
\]

and

\[
\Delta_H(a)
=
\frac12
-
\left\langle
S_a,
(B_{a,-}-\epsilon_+(e^a))^{-1}S_a
\right\rangle_{L^2(-a,a)},
\]

defined on the open pole-localization region \(\Omega=\{a>0:d(a)>0\}\).

Protected RH-R041 proves that whenever \(d(a)>0\),
\[
\operatorname{sgn}\bigl(\epsilon_-(e^a)-\epsilon_+(e^a)\bigr)
=
\operatorname{sgn}\Delta_H(a),
\]
and that when both margins are strictly positive, the quantitative lower bound
\[
g(a)=\epsilon_-(e^a)-\epsilon_+(e^a)\ge 2d(a)\Delta_H(a)
\]
holds.  Protected RH-R043 proves that \(d\) and \(\Delta_H\) are continuous, so
a first loss of the parity theorem can occur only through \(d=0\) or \(\Delta_H=0\).

The earlier work package RH-R044 established explicit positive initial margins
only on the small interval \(0<a\le 2/15\).  Section 5 and Priority Subproblem 1
of Route B explicitly designate refreshing the explicit \(d\) and \(\Delta_H\)
lower bounds at the current simple-even frontier as an immediate high-value deliverable.

Protected RH-R051 extended the proved simple-even interval to
\[
0<a\le\frac{178}{1000}=\frac{89}{500}.
\]

This package proves fully explicit, certified positive lower bounds for both
\(d(a)\) and \(\Delta_H(a)\) uniformly across the entire refreshed frontier
\(0<a\le 178/1000\) using exact rational arithmetic.

## 2. Refreshed full parity gap and pole-localization margin

Let \(a>0\) with \(\lambda=e^a\).  Let \(A_{a,-}\) and \(A_{a,+}\) denote the
odd and even sectors of the full localized Weil operator, with lowest
eigenvalues \(\epsilon_-(e^a)\) and \(\mu(a)=\epsilon_+(e^a)\).

The full parity gap is
\[
g(a)=\epsilon_-(e^a)-\epsilon_+(e^a).
\]

From protected RH-R051 (Theorem 10.1 and Section 8), for every
\(0<a\le 178/1000 = 89/500\), the parity gap satisfies
\[
g(a)
>
g_{\rm cert}(a),
\]
where
\[
g_{\rm cert}(a)
=
2\left(\frac{693}{1000}\right)+\frac{3}{20}-\frac{13351}{14205}
-
\frac{18515}{5682}a
-
\left(\frac{1173}{4735}+\frac{18653}{100000}\right)a^2.
\]

Because the linear and quadratic coefficients are strictly negative,
\(g_{\rm cert}'(a)<0\) for all \(a>0\).  Therefore, for all \(0<a\le 89/500\),
\[
g_{\rm cert}(a)\ge g_{\rm cert}(89/500).
\]

At the endpoint \(a=89/500\), exact rational evaluation in R051 yields
\[
g_{\rm cert}(89/500)
=
\frac{55428698889}{23675000000000}
\approx 0.002341233955.
\]

By the protected rank-one odd-sector decomposition (RH-R041, RH-R044),
\[
B_{a,-}=A_{a,-}+2|S_a\rangle\langle S_a|
\ge
A_{a,-}.
\]
Taking the spectral infimum gives
\[
\beta_-(a):=\inf\sigma(B_{a,-})\ge\inf\sigma(A_{a,-})=\epsilon_-(e^a).
\]

Therefore, the pole-localization margin satisfies
\[
d(a)
=
\beta_-(a)-\mu(a)
\ge
\epsilon_-(e^a)-\mu(a)
=
g(a)
>
g_{\rm cert}(a).
\]

Thus, for all \(0<a\le 178/1000\),
\[
\boxed{
d(a)>\frac{55428698889}{23675000000000}.
}
\]

In particular, \(d(a)>0\) throughout \((0, 178/1000]\), so \((0, 178/1000]\subset\Omega\)
and the resolvent \((B_{a,-}-\mu(a))^{-1}\) is bounded and strictly positive.

## 3. Elementary certified upper bound for the pole vector norm

In unscaled centered logarithmic coordinates \(x\in[-a,a]\), the odd pole
vector is
\[
S_a(x)=\sinh(x/2).
\]
Its \(L^2(-a,a)\) norm is given by the exact identity
\[
\|S_a\|^2
=
\int_{-a}^a \sinh^2(x/2)\,dx
=
\int_{-a}^a \frac{\cosh x-1}{2}\,dx
=
\sinh a-a.
\]

### Lemma 3.1 (Elementary tail bound for sinh a - a)
For every \(0\le x\le 89/500\),
\[
\sinh x-x\le\frac{x^3}{6}+\frac{x^5}{119}.
\]

*Proof.*
The Taylor series of \(\sinh x-x\) for \(x\ge 0\) is
\[
\sinh x-x
=
\frac{x^3}{6}+\frac{x^5}{120}+\sum_{k=3}^\infty\frac{x^{2k+1}}{(2k+1)!}.
\]
For each \(k\ge 3\), we bound the ratio of consecutive terms:
\[
\frac{x^{2k+1}/(2k+1)!}{x^{2k-1}/(2k-1)!}
=
\frac{x^2}{2k(2k+1)}
\le
\frac{x^2}{6\cdot 7}
=
\frac{x^2}{42}.
\]
Since \(x\le 89/500=0.178<1/5\), we have
\[
x^2\le\left(\frac{89}{500}\right)^2=\frac{7921}{250000}<\frac{1}{31}.
\]
Thus
\[
\frac{x^2}{42}<\frac{1}{31\cdot 42}=\frac{1}{1302}<\frac{1}{1050}.
\]
Summing the geometric tail from \(k=3\) gives
\[
\sum_{k=3}^\infty\frac{x^{2k+1}}{(2k+1)!}
\le
\frac{x^5}{120}\sum_{j=1}^\infty\left(\frac{x^2}{42}\right)^j
=
\frac{x^5}{120}\frac{x^2/42}{1-x^2/42}
\le
\frac{x^5}{120}\frac{1/1050}{1-1/1050}
=
\frac{x^5}{120}\frac{1}{1049}
=
\frac{x^5}{125880}.
\]
Adding the \(x^5/120\) term gives
\[
\frac{x^5}{120}+\frac{x^5}{125880}
=
x^5\left(\frac{1049+1}{125880}\right)
=
x^5\frac{1050}{125880}
=
x^5\frac{35}{4196}.
\]
Now we compare \(35/4196\) with \(1/119\):
\[
35\cdot 119 = 4165 < 4196,
\]
which proves
\[
\frac{35}{4196}<\frac{1}{119}.
\]
Therefore,
\[
\sinh x-x\le\frac{x^3}{6}+\frac{x^5}{119}.
\]
\(\blacksquare\)

### Evaluation at the endpoint a = 89/500
Since \(\sinh a-a\) is strictly increasing for \(a>0\), we have for all
\(0<a\le 89/500\):
\[
\|S_a\|^2\le\frac{(89/500)^3}{6}+\frac{(89/500)^5}{119}.
\]

We evaluate each term in exact rational arithmetic:
\[
\left(\frac{89}{500}\right)^3
=
\frac{704969}{125000000},
\qquad
\frac{(89/500)^3}{6}
=
\frac{704969}{750000000},
\]
\[
\left(\frac{89}{500}\right)^5
=
\frac{5584059449}{31250000000000},
\qquad
\frac{(89/500)^5}{119}
=
\frac{5584059449}{3718750000000000}.
\]

Combining the terms with the common denominator
\(3718750000000000 = 750000000\times 4958333 + 250000000\):
\[
\frac{704969}{750000000}+\frac{5584059449}{3718750000000000}
=
\frac{10503166053347}{11156250000000000}.
\]

Numerically,
\[
\frac{10503166053347}{11156250000000000}\approx 9.4146026\times 10^{-4},
\]
which tightly encloses the true value \(\sinh(0.178)-0.178\approx 9.4144887\times 10^{-4}\).

Therefore, for all \(0<a\le 178/1000\),
\[
\boxed{
\|S_a\|^2\le\frac{10503166053347}{11156250000000000}.
}
\]

## 4. Upper bound for the resolvent matrix element

Let
\[
m(a)
:=
\left\langle
S_a,
(B_{a,-}-\mu(a)I)^{-1}S_a
\right\rangle_{L^2(-a,a)}.
\]

Because \(B_{a,-}-\mu(a)I\ge d(a)I>0\), the functional calculus for the
bounded positive self-adjoint inverse gives
\[
(B_{a,-}-\mu(a)I)^{-1}\le\frac{1}{d(a)}I.
\]
Taking the inner product with \(S_a\) yields
\[
m(a)\le\frac{\|S_a\|^2}{d(a)}.
\]

Using the certified lower bound on \(d(a)\) and upper bound on \(\|S_a\|^2\)
from Sections 2 and 3:
\[
m(a)
\le
\frac{10503166053347/11156250000000000}{55428698889/23675000000000}.
\]

Computing the quotient in exact rational arithmetic:
\[
\begin{aligned}
m(a)
&\le
\frac{10503166053347\times 23675000000000}{11156250000000000\times 55428698889}
\\
&=
\frac{10503166053347\times 1894}{8925\times 55428698889}
\\
&=
\boxed{
\frac{9946498252519609}{24735056879216250}
}.
\end{aligned}
\]

Numerically,
\[
m(a)\le 0.4021215031... <\frac12.
\]

In particular, \(m(a)<1/2\) is strictly bounded away from the critical threshold \(1/2\).

## 5. Explicit Herglotz margin lower bound

By definition, the Herglotz margin is
\[
\Delta_H(a)=\frac12-m(a).
\]

Substituting the upper bound for \(m(a)\):
\[
\begin{aligned}
\Delta_H(a)
&\ge
\frac12-\frac{9946498252519609}{24735056879216250}
\\
&=
\frac{24735056879216250 - 2\times 9946498252519609}{2\times 24735056879216250}
\\
&=
\boxed{
\frac{1210515093544258}{12367528439608125}
}.
\end{aligned}
\]

Numerically,
\[
\Delta_H(a)\ge 0.0978784968... >0.
\]

Therefore, the Herglotz margin \(\Delta_H(a)\) remains strictly positive and
bounded away from zero by nearly \(0.098\) throughout the entire interval
\(0<a\le 178/1000\).

## 6. Consistency with the quantitative gap inequality

Protected RH-R041 establishes that whenever \(d(a)>0\) and \(\Delta_H(a)>0\),
the full parity gap satisfies the product lower bound
\[
g(a)\ge 2d(a)\Delta_H(a).
\]

Using the explicit lower bounds established above:
\[
\begin{aligned}
2d(a)\Delta_H(a)
&>
2\left(\frac{55428698889}{23675000000000}\right)
\left(\frac{1210515093544258}{12367528439608125}\right)
\\
&=
\frac{605257546772129}{1320621093750000000}
\approx 0.0004583128.
\end{aligned}
\]

Since the directly proved parity gap satisfies
\[
g(a)>\frac{55428698889}{23675000000000}\approx 0.0023412333,
\]
we observe
\[
0.0023412333 > 0.0004583128,
\]
so the quantitative inequality \(g(a)\ge 2d(a)\Delta_H(a)\) is satisfied with
substantial margin.  The directly proved R051 gap provides the sharper full
gap, while the product serves as a verified consistency certificate.

## 7. Strategic consequences for Forward Route B

1. **Substantial enlargement of the initial continuation domain:**
   The initial explicit Herglotz margins were previously known only on
   \(0<a\le 2/15\approx 0.133333\) (RH-R044).  This package extends the certified
   domain to
   \[
   0<a\le\frac{178}{1000}=0.178,
   \]
   representing a \(+33.5\%\) enlargement of the certified initial base.

2. **Advancing toward the prime threshold:**
   The ultimate objective of Route B is to transport the simple-even theorem
   across the first prime-entry threshold at
   \[
   a_*=\frac12\log 2\approx 0.34657359.
   \]
   By advancing the explicit base from \(a=2/15\approx 0.13333\) to \(a=0.178\),
   the remaining continuation distance to the prime threshold is reduced from
   \(\approx 0.21324\) to \(\approx 0.16857\) (a \(21\%\) reduction in remaining
   distance).

3. **Solid base margins for variation estimates:**
   Subproblems B2 and B3 of Route B require quantitative variation estimates
   of the form
   \[
   d(a)\ge d(a_0)-(C_\mu+C_\beta)|a-a_0|,
   \qquad
   \Delta_H(a)\ge\Delta_H(a_0)-C_H|a-a_0|.
   \]
   With initial base margins at \(a_0=178/1000\):
   \[
   d_0=\frac{55428698889}{23675000000000}\approx 2.341\times 10^{-3},
   \qquad
   \Delta_0=\frac{1210515093544258}{12367528439608125}\approx 9.788\times 10^{-2},
   \]
   both margins have well-separated, certified positive initial budgets.

## 8. Theorem

### RH-R052-REFRESHED-HERGLOTZ-MARGINS-001

For every
\[
0<a=\log\lambda\le\frac{178}{1000},
\]
the localized Weil operator satisfies:

1. The pole-localization margin is strictly positive and bounded by
   \[
   d(a)=\inf\sigma(B_{a,-})-\epsilon_+(e^a)>\frac{55428698889}{23675000000000}>0.
   \]
2. The resolvent matrix element is bounded away from \(1/2\) by
   \[
   m(a)=\left\langle S_a,(B_{a,-}-\epsilon_+(e^a))^{-1}S_a\right\rangle
   \le
   \frac{9946498252519609}{24735056879216250}
   <\frac12.
   \]
3. The Herglotz continuation margin is strictly positive and bounded by
   \[
   \Delta_H(a)=\frac12-m(a)\ge\frac{1210515093544258}{12367528439608125}>0.
   \]
4. By protected RH-R041, the strict parity gap holds throughout:
   \[
   \epsilon_+(e^a)<\epsilon_-(e^a)
   \qquad
   \left(0<a\le\frac{178}{1000}\right).
   \]

## 9. False-proof firewall

Reject:
1. Inferring that \(d(a)\) or \(\Delta_H(a)\) stays positive for \(a>178/1000\)
   without a certified variation or continuation theorem;
2. Defining the scalar resolvent \((B_{a,-}-\mu)^{-1}\) outside \(d(a)>0\);
3. Replacing the infinite-dimensional norm \(\|S_a\|\) by a finite Galerkin
   vector norm without certified bounds;
4. Assuming norm continuity of compressed translation operators across varying \(a\);
5. Treating the rational bounds as optimal;
6. Claiming determinant convergence to \(\Xi\), global simple-evenness, or RH.

## 10. Claim boundary

This theorem does not prove:
- continuation beyond \(a=178/1000\);
- monotonicity of \(d(a)\) or \(\Delta_H(a)\);
- positivity at the R039 large-\(a\) points;
- all-\(a\) simple-evenness;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 11. Admission disposition

Terminal candidate disposition:

RH-R052_REFRESHED_HERGLOTZ_MARGINS_PROVED__READY_FOR_EXACT_HEAD_ADMISSION
