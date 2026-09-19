# RH-R043-HERGLOTZ-MARGIN-CONTINUITY-001

Campaign: RH-001

Status:
ADMISSION_CANDIDATE__AWAITING_R042_PROTECTION

Protected dependencies:
- grandchallenge/MATHSOLVE@139f35f14ee831aa5aa3ed83b774b762965d58b3:work_packages/RH_R045_PARITY_SENSITIVE_REMAINDER.md
- grandchallenge/MATHSOLVE@9519ae68c96c33b1a71548a9984fef1be640a106:work_packages/RH_R041_ODD_HERGLOTZ_GAP_CRITERION.md
- grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md
- grandchallenge/MATHFORGE@f9aa9ad64812df42ad079958ecff88c84e0e4648:reports/discovery/rh_001/rh_r041_pole_resolvent_interface.md

Pending dependency:
- RH-R042-PARITY-BOTTOM-PARAMETER-CONTINUITY-001, PR #393, exact candidate `03fbfa07a147e446091d86b4efd908403f5eb240` pending final Solve check and protected merge.

## 1. Claim

Let \(a>0\), \(\lambda=e^a\), and let \(A_{a,-}\) denote the odd
restriction of the localized Weil operator.

Let \(B_{a,-}\) be the odd pole-free operator obtained from the exact
RH-R041 decomposition

\[
A_{a,-}=B_{a,-}-2|S\rangle\langle S|
\]

in the unscaled Hilbert space \(L^2(-a,a)\).

Define

\[
\beta_-(a):=\inf\sigma(B_{a,-}),
\qquad
\mu(a):=\epsilon_+(e^a),
\]

and

\[
d(a):=\beta_-(a)-\mu(a).
\]

Then:

1. \(\beta_-(a)\) is continuous on \((0,\infty)\);
2. \(d(a)\) is continuous on \((0,\infty)\);
3. on the open pole-localization region
   \[
   \Omega:=\{a>0:d(a)>0\},
   \]
   the Herglotz margin
   \[
   \Delta_H(a)
   :=
   \frac12-
   \langle
   S,
   (B_{a,-}-\mu(a))^{-1}S
   \rangle_{L^2(-a,a)}
   \]
   is continuous.

Combined with RH-R041, for every \(a\in\Omega\),

\[
\operatorname{sgn}
\bigl(
\epsilon_-(e^a)-\epsilon_+(e^a)
\bigr)
=
\operatorname{sgn}\Delta_H(a),
\]

with zero interpreted in the usual way.

If \(\Delta_H(a)>0\), the quantitative lower bound

\[
g(a)
\ge
2d(a)\Delta_H(a)
\]

holds.

## 2. Work on one fixed Hilbert space

Use the unitary scaling

\[
(U_av)(t)=\sqrt a\,v(at),
\qquad
t\in[-1,1].
\]

Write \(\widetilde A_a=U_aA_aU_a^{-1}\), and similarly for parity
restrictions.

Suzuki's fixed-interval closed form has the decomposition

\[
\bar q_a=\bar q^0+\bar q_a^1,
\]

where \(\bar q^0\) is an \(a\)-independent lower-bounded closed form and
\(\bar q_a^1\) is bounded on \(L^2(-1,1)\).

On each compact \(a\)-interval \(K\Subset(0,\infty)\), the bounded
operators representing \(\bar q_a^1\) are uniformly bounded.

The source formula shows that they are strongly continuous in \(a\).
Indeed, locally in \(a\), the bounded part is a finite sum of:

- scalar multiples of the identity;
- compressed translations with shifts \(\log n/a\);
- integral operators with continuous kernels.

Compressed translations are strongly continuous in their shift after
zero-extension to \(L^2(\mathbb R)\), including at the threshold where
the overlap interval shrinks to zero.  Continuous-kernel terms vary in
Hilbert--Schmidt norm locally in \(a\).

Thus there is a common self-adjoint lower-bounded operator \(T^0\)
associated with \(\bar q^0\) and bounded self-adjoint operators \(V_a\)
such that

\[
\widetilde A_a=T^0+V_a,
\]

with common operator domain \(\mathfrak D(T^0)\), and

\[
V_{a_n}f\to V_af
\quad\text{for every fixed }f\in L^2(-1,1)
\]

whenever \(a_n\to a\).

All statements below may be restricted to the closed odd sector because
every term commutes with parity.

## 3. Scaled odd pole vector

In unscaled centered coordinates,

\[
S_a^{\rm phys}(x)=\sinh(x/2).
\]

The odd pole term is

\[
-2|\langle S_a^{\rm phys},v\rangle_{L^2(-a,a)}|^2.
\]

Under \(U_a\),

\[
\langle S_a^{\rm phys},v\rangle
=
\left\langle
\sqrt a\,\sinh(at/2),
U_av
\right\rangle_{L^2(-1,1)}.
\]

Hence define the scaled odd pole vector

\[
s_a(t)=\sqrt a\,\sinh(at/2).
\]

Then

\[
\widetilde A_{a,-}
=
\widetilde B_{a,-}
-
2|s_a\rangle\langle s_a|,
\]

or equivalently

\[
\widetilde B_{a,-}
=
\widetilde A_{a,-}
+
2|s_a\rangle\langle s_a|.
\]

The map

\[
a\mapsto s_a
\]

is norm-continuous from \((0,\infty)\) into \(L^2(-1,1)\).
Consequently the rank-one operator

\[
2|s_a\rangle\langle s_a|
\]

is norm-continuous in \(a\).

## 4. Continuity of the pole-free odd bottom

Let

\[
\widetilde b_a
=
\bar q_{a,-}
+
2|\langle s_a,\cdot\rangle|^2
\]

be the scaled odd pole-free closed form.

It has the same structure as the parity form in RH-R042:

\[
\widetilde b_a
=
\bar q^0_-
+
\widetilde b_a^1,
\]

with one fixed closed lower-bounded form and a bounded \(a\)-dependent
part.

The additional rank-one term is norm-continuous, so the RH-R042
upper/lower semicontinuity proof applies verbatim.

Therefore

\[
\boxed{
\beta_-(a)=\inf\sigma(B_{a,-})
\text{ is continuous on }(0,\infty).
}
\]

RH-R042 gives continuity of

\[
\mu(a)=\epsilon_+(e^a).
\]

Hence

\[
\boxed{
d(a)=\beta_-(a)-\mu(a)
\text{ is continuous.}
}
\]

In particular,

\[
\Omega=\{a:d(a)>0\}
\]

is open.

## 5. Strong continuity of the shifted inverse on \(\Omega\)

Fix \(a_0\in\Omega\).

By continuity of \(d\), choose a neighborhood \(I\ni a_0\) and
\(\delta>0\) such that

\[
d(a)\ge\delta
\quad
(a\in I).
\]

On the fixed odd Hilbert space define

\[
T_a
=
\widetilde B_{a,-}-\mu(a)I.
\]

Then

\[
T_a\ge\delta I
\quad
(a\in I),
\]

so

\[
R_a:=T_a^{-1}
\]

exists and

\[
\|R_a\|\le\delta^{-1}.
\]

Write

\[
T_a=T^0_-+W_a,
\]

where \(W_a\) is bounded self-adjoint and strongly continuous in \(a\).
The term \(-\mu(a)I\) is norm-continuous, the source bounded part is
strongly continuous, and the pole rank-one correction is norm-continuous.

Let \(a_n\to a_0\).  The resolvent identity gives

\[
R_{a_n}-R_{a_0}
=
-R_{a_n}
(W_{a_n}-W_{a_0})
R_{a_0}.
\]

For any fixed \(f\),

\[
(W_{a_n}-W_{a_0})R_{a_0}f\to0
\]

because \(W_a\) is strongly continuous.

The uniform inverse bound then gives

\[
\|(R_{a_n}-R_{a_0})f\|
\le
\delta^{-1}
\|
(W_{a_n}-W_{a_0})R_{a_0}f
\|
\to0.
\]

Therefore

\[
\boxed{
a\mapsto
(\widetilde B_{a,-}-\mu(a)I)^{-1}
\text{ is strongly continuous on }\Omega,
}
\]

with locally uniform operator-norm bounds.

No norm-resolvent continuity is claimed or required.

## 6. Continuity of the Herglotz scalar

Define on the fixed Hilbert space

\[
m(a)
=
\langle
s_a,R_as_a
\rangle.
\]

Let \(a_n\to a_0\in\Omega\).

Because \(s_{a_n}\to s_{a_0}\) in norm, \(R_{a_n}\to R_{a_0}\)
strongly, and \(\sup_n\|R_{a_n}\|<\infty\) locally,

\[
R_{a_n}s_{a_n}
-
R_{a_0}s_{a_0}
=
R_{a_n}(s_{a_n}-s_{a_0})
+
(R_{a_n}-R_{a_0})s_{a_0}
\to0.
\]

Hence

\[
m(a_n)\to m(a_0).
\]

Thus

\[
\boxed{
\Delta_H(a)=\frac12-m(a)
\text{ is continuous on }\Omega.
}
\]

Unitary invariance identifies this with the unscaled RH-R041 scalar

\[
\frac12-
\langle
S,
(B_{a,-}-\mu(a))^{-1}S
\rangle_{L^2(-a,a)}.
\]

## 7. Exact sign interface

RH-R041 proves that whenever \(d(a)>0\),

\[
g(a)>0
\iff
\Delta_H(a)>0,
\]

\[
g(a)=0
\iff
\Delta_H(a)=0,
\]

and

\[
g(a)<0
\iff
\Delta_H(a)<0.
\]

Therefore on every connected component of \(\Omega\), loss of the parity
gap through a sign change must occur at a zero of the continuous scalar
margin \(\Delta_H\).

Moreover, if \(\Delta_H(a)>0\),

\[
\boxed{
g(a)\ge2d(a)\Delta_H(a).
}
\]

Thus certified lower bounds on \(d\) and \(\Delta_H\) yield a certified
full parity-gap lower bound.

## 8. Interaction with the effective small-a regime

The guarded RH-R045 parity-sensitive package proves

\[
g(a)>0
\quad
(0<a\le2/15)
\]

once its provider/admission gates are discharged.

On that interval,

\[
\widetilde B_{a,-}
=
\widetilde A_{a,-}
+
2|s_a\rangle\langle s_a|
\ge
\widetilde A_{a,-},
\]

so

\[
\beta_-(a)\ge\epsilon_-(e^a)>\epsilon_+(e^a)=\mu(a).
\]

Hence

\[
d(a)>0
\]

there.  RH-R041 then forces

\[
\Delta_H(a)>0.
\]

Therefore the effective small-\(a\) theorem supplies an explicit initial
interval on which both continuation margins are strictly positive.

The present theorem does not provide a quantitative lower bound for
either margin on that interval; it only establishes their continuity.

## 9. First-failure classification

Assume RH-R045 and RH-R042 are protected, and let

\[
(0,a_*)
\]

be the maximal connected interval adjacent to zero on which \(g(a)>0\).

If \(a_*<\infty\), RH-R042 gives

\[
g(a_*)=0.
\]

There are two mutually exhaustive interfaces.

### Case 1 — pole localization closes

\[
d(a_*)=0.
\]

Then

\[
\inf\sigma(B_{a_*,-})
=
\epsilon_+(e^{a_*}).
\]

### Case 2 — pole localization stays strict

\[
d(a_*)>0.
\]

Then \(a_*\in\Omega\), and the RH-R041 sign criterion gives

\[
\Delta_H(a_*)=0.
\]

Thus any finite first loss of the parity gap is forced through

\[
\boxed{
d=0
\quad\text{or}\quad
\Delta_H=0.
}
\]

This is a classification of failure interfaces, not a proof that neither
interface occurs.

## 10. Falsification checks

1. Strong continuity is not silently promoted to norm continuity.
   The proof uses only the strong resolvent conclusion and a locally
   uniform inverse norm bound.

2. Translation operators are not norm-continuous in their shift.
   They are used only through strong continuity.

3. Prime-entry thresholds do not create a hidden discontinuity.
   The compressed shifted overlap operator tends strongly to zero when its
   overlap interval collapses at threshold.

4. The pole vector changes with \(a\) after unitary scaling.
   The correct vector
   \[
   s_a(t)=\sqrt a\,\sinh(at/2)
   \]
   is retained explicitly.

5. The Herglotz scalar is defined only where \(d(a)>0\).
   No inverse is invoked at or beyond the pole-localization boundary.

6. Continuity of the two margins does not imply their positivity for all
   \(a\).

## 11. Claim boundary

This theorem does not prove:

- \(d(a)>0\) for all \(a\);
- \(\Delta_H(a)>0\) for all \(a\);
- monotonicity of either margin;
- a lower bound reaching the R039 points;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority.

## 12. Terminal candidate disposition

RH-R043_HERGLOTZ_MARGIN_CONTINUITY_PROVED__AWAITING_R042_PROTECTION
