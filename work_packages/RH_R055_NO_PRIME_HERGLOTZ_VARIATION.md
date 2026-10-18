# RH-R055-NO-PRIME-HERGLOTZ-VARIATION-001

Campaign: RH-001

Status:
ADMISSION_CANDIDATE__DEPENDENCIES_PROTECTED

Solve / coordination tracker:
grandchallenge/MATHSOLVE#412

Protected base:
grandchallenge/MATHSOLVE@20a1f4565bc99c383492894904047af6659fd6ad

Protected dependencies:
- grandchallenge/MATHSOLVE@9519ae68c96c33b1a71548a9984fef1be640a106:work_packages/RH_R041_ODD_HERGLOTZ_GAP_CRITERION.md
- grandchallenge/MATHSOLVE@1a34479235b47405a3ed185c0b1d21d6ad9be190:work_packages/RH_R042_PARITY_BOTTOM_PARAMETER_CONTINUITY.md
- grandchallenge/MATHSOLVE@12e390e455fd9c59d0a6283789073939c69db5de:work_packages/RH_R043_HERGLOTZ_MARGIN_CONTINUITY.md
- grandchallenge/MATHSOLVE@139f35f14ee831aa5aa3ed83b774b762965d58b3:work_packages/RH_R044_EXPLICIT_INITIAL_HERGLOTZ_MARGINS.md
- grandchallenge/MATHSOLVE@fdc539ba2b79b60e458a0ab4ac1370b03a0788bc:work_packages/RH_R051_RANK_ONE_COERCIVITY_EXTENSION.md
- grandchallenge/MATHSOLVE@763e976f2c77c623b619b62b0d0a999c673f76d5:work_packages/RH_R052_REFRESHED_HERGLOTZ_MARGINS.md
- grandchallenge/MATHFORGE@f9aa9ad64812df42ad079958ecff88c84e0e4648:reports/discovery/rh_001/rh_r041_pole_resolvent_interface.md
- grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md

No RH / novelty / priority / certification claim.

## 1. Purpose

Forward Route B reduces continuation of the strict parity gap to quantitative control of

\[
d(a)=\beta_-(a)-\mu(a),
\qquad
\mu(a)=\epsilon_+(e^a),
\qquad
\beta_-(a)=\inf\sigma(B_{a,-}),
\]

and, on \(d(a)>0\),

\[
\Delta_H(a)
=
\frac12-
\langle s_a,(\widetilde B_{a,-}-\mu(a))^{-1}s_a\rangle,
\]

where on the fixed Hilbert space \(L^2(-1,1)\),

\[
s_a(t)=\sqrt a\,\sinh(at/2).
\]

R042/R043 prove qualitative continuity.  This package proves an explicit
no-prime Lipschitz theorem for the sector bottoms, a quantitative
norm-resolvent/scalar variation theorem, and one explicit continuation
corollary beyond the protected R051/R052 endpoint.

The package does not assume simplicity of the pole-free odd bottom.

## 2. Fixed no-prime interval and exact scaled operators

Set

\[
a_0=\frac{89}{500},
\qquad
A=\frac9{50}.
\]

Then

\[
2A=\frac9{25}<\frac{693}{1000}<\log2,
\]

so the prime sum is empty throughout

\[
I=[a_0,A].
\]

Protected R040 gives on \(L^2(-1,1)\)

\[
\bar q_a=s(a)I+\overline{\mathcal L}+K_a,
\]

where \(s(a)=-\log a-c_{\rm src}\) for an \(a\)-independent source constant,
and

\[
K_a(x,y)=a\,q(a|x-y|).
\]

Let \(T\) be the self-adjoint operator associated with
\(\overline{\mathcal L}\).  The scaled full operator is therefore

\[
\widetilde A_a=s(a)I+T+K_a.
\]

In the odd sector the protected pole split gives

\[
\widetilde B_{a,-}
=
s(a)I+T_-+K_{a,-}+2|s_a\rangle\langle s_a|.
\]

All \(a\)-dependence displayed above is bounded relative to the common
self-adjoint part \(T\).  No compressed prime translation occurs on \(I\).

## 3. Extending the protected q-prime bound through 2A

Retain the protected R048 notation
\[
u(t)=\frac1t+\frac12-\coth t,
\qquad
D(t)=\frac1{t^2}-\operatorname{csch}^2t,
\qquad
h''(t)=h(t)\bigl(u(t)^2-D(t)\bigr).
\]

For \(t>0\), the protected partial-fraction estimate gives
\[
0<\coth t-\frac1t\le\frac t3.
\]
Hence on \(0<t\le9/25\),
\[
0<
\frac12-\frac t3
\le
u(t)
<
\frac12,
\]
so \(u(t)^2<1/4\).

The protected lower-bound argument for \(D\) uses
\[
\frac{\sinh t}{t}\ge1+\frac{t^2}{6}
\]
and reduces \(D(t)\ge1/4\) to positivity of
\[
12-8t^2-t^4.
\]
For \(t\le9/25\),
\[
8t^2+t^4
\le
8\left(\frac9{25}\right)^2+\left(\frac9{25}\right)^4
<
2
<
12.
\]
Thus \(D(t)\ge1/4\), and consequently
\[
h''(t)\le0
\qquad
(0<t\le9/25).
\]
Using the protected identity
\[
r_1'''(t)
=
\frac1{2t^2}\int_0^t s\,h''(s)\,ds,
\]
we get
\[
r_1'''(t)\le0.
\]
Therefore
\[
q'(t)=\sinh(t/2)-r_1'''(t)\ge0.
\]

For the upper bound, protected R051 proves, whenever its elementary
condition \(h(t)\le6/5\) holds,
\[
q'(t)
\le
B_*(t)+\sinh(t/2),
\]
with

\[
B_*(t)
=
\frac35\left(
\frac1{24}+\frac t9-\frac{t^2}{30}+\frac{t^4}{2835}
\right).
\]

For \(0\le t\le9/25\),

\[
\frac t2\le\frac9{50}<\log\frac65.
\]

As in R051, \(\sinh t\ge t\) gives
\(h(t)\le e^{t/2}<6/5\), so the displayed R051 estimate remains valid.

The bracket defining \(B_*\) is increasing on this interval because

\[
\frac19-\frac t{15}+\frac{4t^3}{2835}
\ge
\frac19-\frac3{125}
=
\frac{98}{1125}
>0.
\]

Hence

\[
B_*(t)
\le
B_*(9/25)
=
\frac{25381319}{546875000}.
\]

Using the protected elementary bound
\(\sinh x\le x/(1-x^2/2)\),

\[
\sinh(t/2)
\le
\sinh(9/50)
\le
\frac{900}{4919}.
\]

Therefore

\[
0\le q'(t)
\le
\frac{25381319}{546875000}
+
\frac{900}{4919}
=
\frac{617038208161}{2690078125000}
<
\frac{23}{100}.
\]

The final strict comparison is exact:

\[
\frac{23}{100}
-
\frac{617038208161}{2690078125000}
=
\frac{1679760589}{2690078125000}
>0.
\]

Since protected R045 gives \(q(0)=7/4\),

\[
\boxed{
0\le q'(t)\le\frac{23}{100},
\qquad
q(t)\le\frac74+\frac{23}{100}t
\quad
(0\le t\le9/25).
}
\]

No prime-active formula is used.

## 4. Operator-norm Lipschitz bound for K_a

Fix \(u\in[0,2]\) and define

\[
F_u(a)=a\,q(au).
\]

For \(a\in I\),

\[
F_u'(a)=q(au)+au\,q'(au).
\]

Section 3 gives

\[
|F_u'(a)|
\le
\frac74+2\frac{23}{100}Au.
\]

Hence for \(a,b\in I\),

\[
|K_a(x,y)-K_b(x,y)|
\le
|a-b|
\left[
\frac74+
2\frac{23}{100}A|x-y|
\right].
\]

For fixed \(x\in[-1,1]\),

\[
\int_{-1}^1|x-y|\,dy=1+x^2\le2.
\]

The Schur bound therefore gives

\[
\|K_a-K_b\|
\le
C_K|a-b|,
\]

where

\[
\boxed{
C_K
=
\frac72+4\frac{23}{100}\frac9{50}
=
\frac{2291}{625}.
}
\]

The same bound holds after restriction to either parity sector.

## 5. Quantitative variation of the scaled pole term

For

\[
s_a(t)=\sqrt a\,\sinh(at/2),
\]

\[
\partial_a s_a(t)
=
\frac{1}{2\sqrt a}\sinh(at/2)
+
\frac{\sqrt a\,t}{2}\cosh(at/2).
\]

On \(I\),

\[
a_0=\frac{89}{500}>\frac{64}{361},
\qquad
A=\frac9{50}<\frac{289}{1600},
\]

so

\[
\frac1{\sqrt a}<\frac{19}{8},
\qquad
\sqrt a<\frac{17}{40}.
\]

Also \(a|t|/2\le9/100\).  For \(0\le x<\sqrt2\), the power series and
\((2n)!\ge2^n\), \((2n+1)!\ge2^n\) give the elementary bounds
\[
\cosh x
\le
\sum_{n\ge0}\left(\frac{x^2}{2}\right)^n
=
\frac1{1-x^2/2},
\]
and
\[
\sinh x
\le
x\sum_{n\ge0}\left(\frac{x^2}{2}\right)^n
=
\frac{x}{1-x^2/2}.
\]
At \(x=9/100\), therefore,
\[
\sinh(9/100)\le\frac{1800}{19919},
\qquad
\cosh(9/100)\le\frac{20000}{19919}.
\]

Thus pointwise,

\[
|\partial_a s_a(t)|
\le
\frac{19}{16}\frac{1800}{19919}
+
\frac{17}{80}\frac{20000}{19919}
=
\frac{12775}{39838}.
\]

Since
\[
2\cdot70^2=9800<9801=99^2,
\]
we have \(\sqrt2<99/70\).  Hence

\[
\|\partial_a s_a\|_2
<
\frac{99}{70}\frac{12775}{39838}
=
\frac{36135}{79676}
<
\frac{227}{500}.
\]

Consequently,

\[
\boxed{
\|s_a-s_b\|
\le
\frac{227}{500}|a-b|.
}
\]

Moreover,

\[
\|s_a\|^2=\sinh a-a.
\]

The R052 tail lemma applies because \(A<1/5\), and gives

\[
\|s_a\|^2
\le
\frac{A^3}{6}+\frac{A^5}{119}
=
\frac{36205299}{37187500000}
<
\frac1{1024}.
\]

Hence

\[
\boxed{\|s_a\|<\frac1{32}.}
\]

Using

\[
|u\rangle\langle u|-|v\rangle\langle v|
=
|u-v\rangle\langle u|+|v\rangle\langle u-v|,
\]

we obtain

\[
\left\|
2|s_a\rangle\langle s_a|
-
2|s_b\rangle\langle s_b|
\right\|
\le
C_P|a-b|,
\]

with

\[
\boxed{
C_P
=
4\left(\frac1{32}\right)\left(\frac{227}{500}\right)
=
\frac{227}{4000}.
}
\]

## 6. Explicit Lipschitz theorem for mu and beta-minus

For a self-adjoint operator with compact resolvent, every min-max eigenvalue
moves by at most the operator norm of a bounded self-adjoint perturbation.
No eigenvalue simplicity is needed.

The scalar shift satisfies on \(I\)

\[
|s(a)-s(b)|
=
|\log a-\log b|
\le
\frac{|a-b|}{a_0}
=
\frac{500}{89}|a-b|.
\]

For the even bottom,

\[
\boxed{
|\mu(a)-\mu(b)|
\le
C_\mu|a-b|,
\qquad
C_\mu
=
\frac{500}{89}+\frac{2291}{625}
=
\frac{516399}{55625}.
}
\]

For the pole-free odd bottom,

\[
\boxed{
|\beta_-(a)-\beta_-(b)|
\le
C_\beta|a-b|,
}
\]

where

\[
\boxed{
C_\beta
=
\frac{500}{89}+\frac{2291}{625}+\frac{227}{4000}
=
\frac{16625783}{1780000}.
}
\]

This proves the requested sector-bottom variation theorem without assuming
that \(\beta_-\) is simple.

### Common-shift cancellation in d

Write

\[
\mu(a)=s(a)+\nu_+(a),
\qquad
\beta_-(a)=s(a)+\rho_-(a).
\]

The common scalar shift cancels exactly:

\[
d(a)=\rho_-(a)-\nu_+(a).
\]

Therefore the useful Lipschitz constant for \(d\) does not pay \(2/a_0\):

\[
\boxed{
|d(a)-d(b)|
\le
C_d|a-b|,
\qquad
C_d
=
2C_K+C_P
=
\frac{147759}{20000}.
}
\]

This cancellation is the main quantitative gain of the Route B formulation.

## 7. Quantitative resolvent and Herglotz-scalar variation

On \(d(a)>0\), define on the fixed odd Hilbert space

\[
H_a
=
\widetilde B_{a,-}-\mu(a)I,
\qquad
R_a=H_a^{-1}.
\]

Because the common scalar shift cancels,

\[
H_a
=
T_-+K_{a,-}+2|s_a\rangle\langle s_a|-\nu_+(a)I.
\]

Sections 4-6 therefore give

\[
\boxed{
\|H_a-H_b\|
\le
C_d|a-b|.
}
\]

If \(a,b\in I\) and

\[
d(a),d(b)\ge\delta>0,
\]

then

\[
\|R_a\|,\|R_b\|\le\delta^{-1}.
\]

The resolvent identity gives

\[
\boxed{
\|R_a-R_b\|
\le
\frac{C_d}{\delta^2}|a-b|.
}
\]

Define

\[
m(a)=\langle s_a,R_as_a\rangle,
\qquad
\Delta_H(a)=\frac12-m(a).
\]

Using Sections 5 and the inverse bound,

\[
\boxed{
|m(a)-m(b)|
=
|\Delta_H(a)-\Delta_H(b)|
\le
C_H(\delta)|a-b|,
}
\]

where one admissible explicit constant is

\[
\boxed{
C_H(\delta)
=
\frac{227}{8000\,\delta}
+
\frac{C_d}{1024\,\delta^2}.
}
\]

This is a norm-resolvent theorem only for the present no-prime family, where
the actual varying bounded operator has been explicitly norm-controlled.
It does not promote compressed translations to norm continuity.

## 8. Explicit continuation beyond a = 178/1000

Set

\[
a_1=\frac{3561}{20000}
=
0.17805,
\qquad
a_1-a_0=\frac1{20000}.
\]

Protected R052 gives at \(a_0\)

\[
d(a_0)>
d_0
:=
\frac{55428698889}{23675000000000}.
\]

Section 6 yields, for every \(a\in[a_0,a_1]\),

\[
d(a)
>
d_0-\frac{C_d}{20000}
=
\boxed{
d_1
=
\frac{93366426153}{47350000000000}
}
>0.
\]

To control the Herglotz scalar, use the sharper direct positive-resolvent
inequality from R052,

\[
m(a)\le\frac{\|s_a\|^2}{d(a)}.
\]

Section 5 gives uniformly on the larger interval \(I\)

\[
\|s_a\|^2
\le
U
:=
\frac{36205299}{37187500000}.
\]

Therefore on \([a_0,a_1]\),

\[
\Delta_H(a)
\ge
\frac12-\frac{U}{d(a)}
>
\frac12-\frac{U}{d_1}
=
\boxed{
\frac{3562843673}{569774600626}
}
>0.
\]

The exact residual budget is

\[
d_1-2U
=
\boxed{
\frac{138950903247}{5634650000000000}
}
>0.
\]

By protected R041,

\[
g(a)
=
\epsilon_-(e^a)-\epsilon_+(e^a)
\ge
2d(a)\Delta_H(a)
>
\boxed{
\frac{138950903247}{5634650000000000}
}
\]

through \(a_1\).

Combining with protected R052 below \(a_0\), both Route B margins are
strictly positive for every

\[
0<a\le\frac{3561}{20000}.
\]

## 9. Transport of even-sector simplicity

Let \(\epsilon_{+,1}(e^a)\le\epsilon_{+,2}(e^a)\) be the first two even
eigenvalues.  The common scalar shift cancels in their difference, and
Section 4 implies that each shifted even eigenvalue moves by at most
\(C_K|a-b|\).

Hence the even internal gap moves by at most

\[
2C_K|a-b|.
\]

Protected R051 gives at \(a_0\)

\[
\epsilon_{+,2}(e^{a_0})-\epsilon_{+,1}(e^{a_0})
>
\frac{1783634369}{11837500000}.
\]

Thus on \([a_0,a_1]\),

\[
\epsilon_{+,2}(e^a)-\epsilon_{+,1}(e^a)
>
\frac{1783634369}{11837500000}
-
\frac{2C_K}{20000}
=
\boxed{
\frac{355859043}{2367500000}
}
>0.
\]

The lowest even-sector eigenvalue therefore remains simple through \(a_1\).

## 10. Theorem

### RH-R055-NO-PRIME-HERGLOTZ-VARIATION-001

On

\[
I=
\left[\frac{89}{500},\frac9{50}\right],
\]

the actual fixed-Hilbert-space no-prime operator family satisfies:

1. sector-bottom Lipschitz bounds
   \[
   |\mu(a)-\mu(b)|
   \le
   \frac{516399}{55625}|a-b|,
   \]
   \[
   |\beta_-(a)-\beta_-(b)|
   \le
   \frac{16625783}{1780000}|a-b|;
   \]
2. the common-shift-improved pole-localization variation bound
   \[
   |d(a)-d(b)|
   \le
   \frac{147759}{20000}|a-b|;
   \]
3. whenever \(d(a),d(b)\ge\delta>0\), the quantitative resolvent bound
   \[
   \|R_a-R_b\|
   \le
   \frac{147759}{20000\,\delta^2}|a-b|
   \]
   and scalar Herglotz variation bound
   \[
   |\Delta_H(a)-\Delta_H(b)|
   \le
   \left(
   \frac{227}{8000\,\delta}
   +
   \frac{147759}{20480000\,\delta^2}
   \right)|a-b|.
   \]

As an explicit continuation corollary, for every

\[
\boxed{
0<a=\log\lambda\le\frac{3561}{20000},
}
\]

one has

\[
d(a)>
\frac{93366426153}{47350000000000}>0,
\]

\[
\Delta_H(a)>
\frac{3562843673}{569774600626}>0
\]

on the new tranche \(a\in[89/500,3561/20000]\), and hence

\[
\epsilon_-(e^a)-\epsilon_+(e^a)
>
\frac{138950903247}{5634650000000000}>0.
\]

The first even-sector eigenvalue remains simple, with internal gap on the new
tranche bounded below by

\[
\frac{355859043}{2367500000}>0.
\]

Together with the protected R051 theorem below \(a_0\), the full localized
Weil ground state is simple and even through

\[
\boxed{
a=\frac{3561}{20000}=0.17805.
}
\]

## 11. Reproducible exact arithmetic

The exact rational comparisons and endpoint budgets are checked by

\[
\texttt{python scripts/rh_r055_route_b_variation.py}.
\]

The checker uses only Python's standard-library Fraction type and asserts all
strict sign comparisons used above.

A clean replay on the authoring head produced:

\`\`\`text
qprime_bound = 617038208161/2690078125000
C_K = 2291/625
C_mu = 516399/55625
C_beta = 16625783/1780000
C_d = 147759/20000
d1 = 93366426153/47350000000000
Delta1 = 3562843673/569774600626
parity_gap1 = 138950903247/5634650000000000
even_internal_gap1 = 355859043/2367500000
RH-R055 exact arithmetic: PASS
\`\`\`

## 12. False-proof firewall

Reject:

1. using the no-prime formula at or beyond \(2a=\log2\);
2. interpreting the present norm-Lipschitz theorem as norm continuity of
   compressed prime translations;
3. defining \(R_a\), \(m(a)\), or \(\Delta_H(a)\) when \(d(a)\le0\);
4. assuming simplicity or differentiability of \(\beta_-(a)\);
5. inferring monotonicity of \(\mu\), \(\beta_-\), \(d\), or \(\Delta_H\);
6. using a finite plot or Galerkin value as an infinite-operator margin;
7. claiming all-\(a\) simple-evenness, determinant convergence, RH, novelty,
   priority, or publication readiness.

## 13. Claim boundary

This theorem does not prove:

- simple-evenness beyond \(a=3561/20000\);
- positivity of \(d\) or \(\Delta_H\) up to the first prime threshold;
- any prime-threshold crossing;
- monotonicity of either continuation margin;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 14. Admission dependency

Before admission:

1. recompose onto the current protected Solve main if it moved;
2. record exact-head non-authoring Adversary and Referee passes;
3. require exact-head Solve/GCL green checks;
4. merge through protected controls;
5. perform protected readback and update the RH handoff.

Terminal candidate disposition:

RH-R055_NO_PRIME_SECTOR_BOTTOM_AND_HERGLOTZ_VARIATION_PROVED__SIMPLE_EVEN_EXTENDED_THROUGH_3561_OVER_20000__READY_FOR_EXACT_HEAD_ADMISSION
