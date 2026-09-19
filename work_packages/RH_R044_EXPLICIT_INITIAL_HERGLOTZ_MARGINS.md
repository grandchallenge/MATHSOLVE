# RH-R044-EXPLICIT-INITIAL-HERGLOTZ-MARGINS-001

Campaign: RH-001

Status:
ADMISSION_CANDIDATE__DEPENDENCIES_PROTECTED

Solve tracker:
grandchallenge/MATHSOLVE#382

Protected dependencies:
- grandchallenge/MATHSOLVE@139f35f14ee831aa5aa3ed83b774b762965d58b3:work_packages/RH_R045_PARITY_SENSITIVE_REMAINDER.md
- grandchallenge/MATHSOLVE@9519ae68c96c33b1a71548a9984fef1be640a106:work_packages/RH_R041_ODD_HERGLOTZ_GAP_CRITERION.md
- grandchallenge/MATHSOLVE@1a34479235b47405a3ed185c0b1d21d6ad9be190:work_packages/RH_R042_PARITY_BOTTOM_PARAMETER_CONTINUITY.md
- grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md
- grandchallenge/MATHFORGE@f9aa9ad64812df42ad079958ecff88c84e0e4648:reports/discovery/rh_001/rh_r041_pole_resolvent_interface.md

Protected dependency:
- grandchallenge/MATHSOLVE@12e390e455fd9c59d0a6283789073939c69db5de:work_packages/RH_R043_HERGLOTZ_MARGIN_CONTINUITY.md

No RH / novelty / priority / certification claim.

## 1. Purpose

RH-R043 turns continuation of the parity gap into control of two margins:

\[
d(a)
=
\inf\sigma(B_{a,-})
-
\epsilon_+(e^a)
\]

and

\[
\Delta_H(a)
=
\frac12
-
\left\langle
S,
(B_{a,-}-\epsilon_+(e^a))^{-1}S
\right\rangle.
\]

This package supplies explicit strictly positive initial values for both
margins on the guarded effective small-\(a\) interval

\[
0<a\le\frac2{15}.
\]

The bounds are deliberately coarse and fully elementary.

## 2. Effective full parity-gap lower bound

The guarded RH-R045 theorem proves, on

\[
0<a\le\frac2{15},
\]

the uniform parity-gap estimate

\[
\boxed{
g(a)
=
\epsilon_-(e^a)-\epsilon_+(e^a)
>
\frac{13301}{2740500}.
}
\]

## 3. Pole-localization margin

The exact odd pole split gives

\[
B_{a,-}
=
A_{a,-}
+
2|S\rangle\langle S|
\ge
A_{a,-}.
\]

Therefore

\[
d(a)
=
\inf\sigma(B_{a,-})
-
\epsilon_+(e^a)
\ge
g(a),
\]

so

\[
\boxed{
d(a)>\frac{13301}{2740500}.
}
\]

## 4. Exact norm of the odd pole vector

For

\[
S(x)=\sinh(x/2),
\qquad
x\in[-a,a],
\]

one has

\[
\|S\|^2=\sinh a-a.
\]

For \(0<a\le2/15<1\), Taylor's theorem and \(\cosh1<2\) give

\[
\sinh a-a
<
\frac{a^3}{3}
\le
\boxed{\frac8{10125}}.
\]

## 5. Resolvent scalar upper bound

Let

\[
\mu(a)=\epsilon_+(e^a).
\]

Since

\[
B_{a,-}-\mu(a)I\ge d(a)I,
\]

functional calculus gives

\[
m(a)
:=
\left\langle
S,
(B_{a,-}-\mu(a)I)^{-1}S
\right\rangle
\le
\frac{\|S\|^2}{d(a)}.
\]

Thus

\[
m(a)
<
\frac{8/10125}{13301/2740500}
=
\boxed{
\frac{6496}{39903}
}.
\]

## 6. Explicit Herglotz margin

By definition,

\[
\Delta_H(a)=\frac12-m(a).
\]

Therefore

\[
\boxed{
\Delta_H(a)
>
\frac{26911}{79806}.
}
\]

In particular, \(\Delta_H(a)>0\).

## 7. Initial continuation certificate

For every

\[
0<a\le\frac2{15},
\]

the guarded chain yields

\[
\boxed{
d(a)>\frac{13301}{2740500}
}
\]

and

\[
\boxed{
\Delta_H(a)>\frac{26911}{79806}.
}
\]

Thus both R043 continuation margins remain explicitly separated from zero
through the full current R045 simple-even interval.

## 8. Relation to the full parity gap

RH-R041 proves, whenever \(d(a)>0\) and \(\Delta_H(a)>0\),

\[
g(a)\ge2d(a)\Delta_H(a).
\]

The direct R045 gap estimate is the preferred full-gap certificate; the
margin product is retained as a consistency check.

## 9. What this changes

Continuation may now start at the edge

\[
a=\frac2{15}
\]

with explicit error budgets

\[
d_0=\frac{13301}{2740500},
\qquad
\Delta_0=\frac{26911}{79806}.
\]

The next nonperturbative tranche can focus on a quantitative variation bound
for \(d\) or \(\Delta_H\) across the short interval toward \(a=1/7\), rather
than restarting from qualitative continuity.

## 10. False-proof firewall

Reject:

1. replacing the strict R045 work-branch theorem by this package before
   R045's dependency and exact-head CI gates are protected;
2. inferring that \(d(a)\) or \(\Delta_H(a)\) stays positive for
   \(a>2/15\);
3. using the scalar resolvent outside \(d(a)>0\);
4. replacing the full operator norm \(\|S\|\) by a finite Galerkin vector
   norm without an exact identification;
5. treating the coarse rational constants as optimal;
6. inferring determinant convergence or RH from these local margins.

## 11. Claim boundary

This theorem does not prove:

- continuation beyond \(a=2/15\);
- monotonicity of \(d\) or \(\Delta_H\);
- positivity at the R039 points;
- all-\(a\) even-simplicity;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 12. Admission dependency

Before admission:

1. this theorem must be composed onto the current live Solve head;
2. exact-head Adversary/Referee reviews and required Solve/GCL CI must pass;
3. protected merge and readback must complete.

Terminal candidate disposition:

RH-R044_EXPLICIT_INITIAL_CONTINUATION_MARGINS_PROVED__READY_FOR_EXACT_HEAD_ADMISSION
