# NS-CI-R014-A2-L5-37 — nonseparable direction geometry and Lagrangian jet cocycle

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Integration base:
  `c31509bae1d8fe8a148cfea425edaaf620be184d`
- Protected mathematical predecessor:
  `0c320165cf8b0a3fc508698f2b1fa8de29e3475c`
- Result:
  `NONSEPARABLE_DIRECTION_GEOMETRY_CONTROLLED_BY_LAGRANGIAN_JET_COCYCLE__SCALAR_SIGNED_CLOCK_INSUFFICIENT`
- A2 theorem: open
- L5: active
- C2-MIX-DIRECTION-PATHORDER: one-dimensional path-ordered frame geometry resolved conditionally
- MATHCERT adjudication: absent
- Evidence class: exact characteristic-flow identities and conditional critical normal-form theorem;
  not selected whole-space NSE derivation

L5-36 proves that when the spatial direction profile is fixed,

```math
h^{-1}\theta_h(s)B(Y)\partial_Y,
```

the characteristic geometry factors through the scalar signed flow time

```math
\kappa_h(s)
=
h^{-1}\int_0^s\theta_h(\sigma)\,d\sigma.
```

That collapse fails once the spatial profile changes with time.

For the genuinely nonseparable principal direction field

```math
v_h(s,Y)
=
h^{-1}
\theta_h(s)
B_h(s,Y),
```

let

```math
\partial_s\chi_h(s,Z)
=
v_h(
s,
\chi_h(s,Z)
),
\qquad
\chi_h(0,Z)=Z.
```

In one spatial dimension, the first derivative cocycle remains scalar:

```math
\boxed{
J_h(s,Z)
=
\partial_Z\chi_h(s,Z)
=
\exp(
\Omega_{1,h}(s,Z)
),
}
```

where the exact Lagrangian strain is

```math
\boxed{
\Omega_{1,h}(s,Z)
=
\int_0^s
\partial_Yv_h(
\sigma,
\chi_h(\sigma,Z)
)
\,d\sigma.
}
```

This is already path ordered because the strain is sampled along the actual
characteristic.

The finite metric derivatives required by L5-35 are controlled by an exact
normalized jet hierarchy.

Write

```math
J_h
=
\chi_{h,Z},
\qquad
K_h
=
\chi_{h,ZZ},
\qquad
L_h
=
\chi_{h,ZZZ},
\qquad
M_h
=
\chi_{h,ZZZZ}.
```

Along the flow define

```math
a_{m,h}(s,Z)
=
\partial_Y^m
v_h(
s,
\chi_h(s,Z)
),
\qquad
m=1,2,3,4.
```

Then

```math
\boxed{
\begin{aligned}
J_h'
&=
a_{1,h}J_h,
\\
K_h'
&=
a_{1,h}K_h
+
a_{2,h}J_h^2,
\\
L_h'
&=
a_{1,h}L_h
+
3a_{2,h}J_hK_h
+
a_{3,h}J_h^3,
\\
M_h'
&=
a_{1,h}M_h
+
4a_{2,h}J_hL_h
+
3a_{2,h}K_h^2
+
6a_{3,h}J_h^2K_h
+
a_{4,h}J_h^4.
\end{aligned}
}
```

Introduce the normalized jet cocycle

```math
U_{2,h}
=
\frac{K_h}{J_h},
\qquad
U_{3,h}
=
\frac{L_h}{J_h},
\qquad
U_{4,h}
=
\frac{M_h}{J_h}.
```

The common tangent growth cancels exactly:

```math
\boxed{
\begin{aligned}
U_{2,h}'
&=
a_{2,h}J_h,
\\
U_{3,h}'
&=
3a_{2,h}J_hU_{2,h}
+
a_{3,h}J_h^2,
\\
U_{4,h}'
&=
4a_{2,h}J_hU_{3,h}
+
3a_{2,h}J_hU_{2,h}^2
\\
&\qquad
+
6a_{3,h}J_h^2U_{2,h}
+
a_{4,h}J_h^3.
\end{aligned}
}
```

with

```math
U_{2,h}(0)
=
U_{3,h}(0)
=
U_{4,h}(0)
=
0.
```

Thus the one-dimensional path-ordered deformation observable is the finite
Lagrangian jet signature

```math
\boxed{
\mathfrak D_h
=
(
\Xi_h,
\Omega_{1,h},
U_{2,h},
U_{3,h},
U_{4,h}
),
}
```

where \(\Xi_h(s)\) is one lifted basepoint trajectory, for example

```math
\Xi_h(s)
=
\widetilde\chi_h(s,0).
```

The basepoint is needed because spatial derivatives alone do not record rigid
translation.

If

```math
\sup
(
|\Omega_{1,h}|
+
|U_{2,h}|
+
|U_{3,h}|
+
|U_{4,h}|
)
\le
C,
```

then

```math
e^{-C}
\le
J_h
\le
e^C
```

and the characteristic map has uniform \(W^{4,\infty}\) control.

If, in addition,

```math
\mathfrak D_h
=
\mathfrak D_0
+
O(h)
```

uniformly in the corresponding finite norms, then

```math
\chi_h
=
\chi_0
+
O(h)
```

in \(W^{4,\infty}\), and

```math
J_h
=
J_0
+
O(h)
```

in \(W^{3,\infty}\).

This supplies the geometric convergence hypothesis of L5-35.

With the same \(O(h)\) Eulerian scalar-profile convergence as before,

```math
G_h
=
G_0
+
O(h),
```

the Lagrangian accumulated phase

```math
\mathcal F_h(s,Z)
=
\int_0^s
G_h(
\sigma,
\chi_h(\sigma,Z)
)
\,d\sigma
```

also converges at \(O(h)\).

Hence the full L5-35 metric critical-mixing theorem applies whenever the
limiting metric-weighted phase gradient is nondegenerate.

The scalar signed coefficient integral is not enough in the nonseparable case.

There is an exact smooth-pulse separator with

```math
\boxed{
h^{-1}
\int_0^S
\theta_h(s)\,ds
=
0
}
```

but nontrivial characteristic distortion.

Choose two disjoint smooth pulses separated by a gap where \(\theta_h=0\).

During the first pulse let

```math
B_h(s,Y)=1
```

and choose signed flow time \(+\kappa\).

During the second pulse let

```math
B_h(s,Y)=\sin Y
```

and choose signed flow time \(-\kappa\).

The spatial profile can be changed smoothly during the zero-\(\theta_h\) gap,
so the complete coefficient field is smooth.

The final characteristic map is exactly

```math
\boxed{
\chi_h^{\rm fin}
=
\varphi_{\sin}^{-\kappa}
\circ
T_\kappa,
}
```

where \(T_\kappa(Z)=Z+\kappa\).

The scalar signed flow times cancel:

```math
\kappa+(-\kappa)=0.
```

But at the lifted point \(Z=-\kappa\),

```math
T_\kappa(-\kappa)=0,
```

and \(0\) is the expanding fixed point of the \(\sin Y\) flow.

Therefore

```math
\boxed{
\partial_Z
\chi_h^{\rm fin}(-\kappa)
=
e^{-\kappa}.
}
```

For \(\kappa\ne0\), the final frame is not the identity despite zero total
scalar signed clock.

For \(\kappa\to+\infty\), the inverse Jacobian at this point grows like
\(e^\kappa\).

The pathwise strain cocycle detects the effect exactly: it vanishes on the
translation pulse and accumulates \(-\kappa\) on the second pulse along this
trajectory.

Thus the correct nonseparable replacement for L5-36's scalar clock is
trajectory-dependent characteristic strain plus its finite jet cocycle.

## 1. Principal nonseparable direction model

Consider

```math
\partial_s\Phi_h
+
v_h(s,Y)\partial_Y\Phi_h
+
ih^{-1}G_h(s,Y)\Phi_h
=
h^2(
\partial_Y^2-1
)\Phi_h
+
r_h,
```

with

```math
v_h(s,Y)
=
h^{-1}
\theta_h(s)
B_h(s,Y).
```

The direction term is principal.

It is not assigned to NF4.

## 2. Characteristic flow

Let

```math
\partial_s\chi_h
=
v_h(s,\chi_h),
\qquad
\chi_h(0,Z)=Z.
```

Use an orientation-preserving lift

```math
\widetilde\chi_h(s,Z+2\pi)
=
\widetilde\chi_h(s,Z)
+
2\pi.
```

Define

```math
\Xi_h(s)
=
\widetilde\chi_h(s,0).
```

The lifted basepoint records the rigid component of the frame.

## 3. Exact tangent cocycle

Differentiate once:

```math
\partial_s
\chi_{h,Z}
=
(
\partial_Yv_h
)(s,\chi_h)
\chi_{h,Z}.
```

Therefore

```math
\boxed{
J_h(s,Z)
=
\exp
\left(
\int_0^s
(
\partial_Yv_h
)(
\sigma,
\chi_h(\sigma,Z)
)
\,d\sigma
\right).
}
```

Define

```math
\Omega_{1,h}
=
\log J_h.
```

Because \(J_h>0\), this is globally well defined.

## 4. Exact second jet

Differentiate twice:

```math
K_h'
=
a_{1,h}K_h
+
a_{2,h}J_h^2.
```

Since

```math
J_h'
=
a_{1,h}J_h,
```

one obtains

```math
\boxed{
\left(
\frac{K_h}{J_h}
\right)'
=
a_{2,h}J_h.
}
```

Thus

```math
\boxed{
U_{2,h}(s,Z)
=
\int_0^s
a_{2,h}(\sigma,Z)
J_h(\sigma,Z)
\,d\sigma.
}
```

## 5. Exact third jet

Differentiate three times:

```math
L_h'
=
a_{1,h}L_h
+
3a_{2,h}J_hK_h
+
a_{3,h}J_h^3.
```

Hence

```math
\boxed{
U_{3,h}'
=
3a_{2,h}J_hU_{2,h}
+
a_{3,h}J_h^2.
}
```

Therefore

```math
\boxed{
U_{3,h}(s,Z)
=
\int_0^s
[
3a_{2,h}J_hU_{2,h}
+
a_{3,h}J_h^2
]
\,d\sigma.
}
```

## 6. Exact fourth jet

Faà di Bruno gives

```math
\begin{aligned}
M_h'
={}&
a_{1,h}M_h
+
4a_{2,h}J_hL_h
+
3a_{2,h}K_h^2
\\
&+
6a_{3,h}J_h^2K_h
+
a_{4,h}J_h^4.
\end{aligned}
```

Thus

```math
\boxed{
\begin{aligned}
U_{4,h}'
={}&
4a_{2,h}J_hU_{3,h}
+
3a_{2,h}J_hU_{2,h}^2
\\
&+
6a_{3,h}J_h^2U_{2,h}
+
a_{4,h}J_h^3.
\end{aligned}
}
```

and

```math
\boxed{
\begin{aligned}
U_{4,h}(s,Z)
=
\int_0^s
[
&
4a_{2,h}J_hU_{3,h}
+
3a_{2,h}J_hU_{2,h}^2
\\
&
+
6a_{3,h}J_h^2U_{2,h}
+
a_{4,h}J_h^3
]
\,d\sigma.
\end{aligned}
}
```

## 7. Exact reconstruction of frame derivatives

By definition,

```math
\boxed{
\begin{aligned}
\chi_{h,Z}
&=
J_h
=
e^{\Omega_{1,h}},
\\
\chi_{h,ZZ}
&=
J_hU_{2,h},
\\
\chi_{h,ZZZ}
&=
J_hU_{3,h},
\\
\chi_{h,ZZZZ}
&=
J_hU_{4,h}.
\end{aligned}
}
```

Also

```math
\widetilde\chi_h(s,Z)
=
\Xi_h(s)
+
\int_0^Z
J_h(s,\zeta)
\,d\zeta.
```

Thus the finite signature

```math
(
\Xi_h,
\Omega_{1,h},
U_{2,h},
U_{3,h},
U_{4,h}
)
```

reconstructs the characteristic frame through fourth spatial order.

## 8. Uniform frame theorem

Assume

```math
\sup_{h,s,Z}
|\Omega_{1,h}|
\le
C_1
```

and

```math
\sup_{h,s,Z}
(
|U_{2,h}|
+
|U_{3,h}|
+
|U_{4,h}|
)
\le
C_4.
```

Then

```math
e^{-C_1}
\le
J_h
\le
e^{C_1}.
```

The reconstruction identities give

```math
\sup_h
\sup_s
\|
\chi_h(s)
\|_{W^{4,\infty}}
\le
C.
```

The inverse function formulas express the first four inverse derivatives as
rational polynomials in

```math
J_h,
K_h,
L_h,
M_h
```

with powers of \(J_h^{-1}\).

Therefore

```math
\sup_h
\sup_s
\|
\chi_h(s)^{-1}
\|_{W^{4,\infty}}
\le
C.
```

In particular, the L5-35 smooth bi-Lipschitz frame contract holds.

## 9. O(h) frame convergence from cocycle convergence

Assume there is a limiting signature

```math
\mathfrak D_0
=
(
\Xi_0,
\Omega_{1,0},
U_{2,0},
U_{3,0},
U_{4,0}
)
```

such that

```math
\boxed{
\|
\mathfrak D_h
-
\mathfrak D_0
\|_\infty
\le
Ch.
}
```

Here the norm includes the relevant spatial derivatives of the signature
components.

Because the exponential map is smooth on the bounded interval supplied by
the uniform frame theorem,

```math
J_h
-
J_0
=
O(h).
```

The exact derivative reconstruction then gives

```math
\boxed{
\sup_s
\|
\chi_h(s)-\chi_0(s)
\|_{W^{4,\infty}}
\le
Ch.
}
```

Hence

```math
\sup_s
\|
J_h(s)-J_0(s)
\|_{W^{3,\infty}}
\le
Ch.
```

This is the metric convergence needed by L5-35.

## 10. Lagrangian phase convergence

Assume

```math
G_h
=
G_0
+
O(h)
```

in

```math
C(
[0,S];
W^{4,\infty}
).
```

Set

```math
\mathcal F_h(s,Z)
=
\int_0^s
G_h(
\sigma,
\chi_h(\sigma,Z)
)
\,d\sigma.
```

The frame convergence gives

```math
\boxed{
\sup_s
\|
\mathcal F_h(s)-\mathcal F_0(s)
\|_{W^{4,\infty}}
\le
Ch.
}
```

Therefore all geometric and phase convergence hypotheses of L5-35 follow from
the jet-cocycle theorem.

## 11. Conditional charge transfer

Retain the protected L5-35 initialization and residual assumptions in the
characteristic frame.

Assume also the limiting metric-weighted phase nondegeneracy

```math
\inf_{s\in\mathcal J}
\int
J_0^{-1}
|(\mathcal F_0)_ZA_0|^2
\,dZ
>
0
```

on one fixed positive critical interval.

Then the L5-35 physical moment argument applies and yields

```math
\boxed{
\int
\Lambda(t)^2
\,dt
\ge
\frac{c_*}{\nu}.
}
```

Thus bounded convergent Lagrangian jet cocycle is a sufficient nonseparable
direction-frame condition for the protected critical-mixing theorem.

## 12. Smooth two-profile zero-clock separator

Fix \(\kappa>0\).

Choose disjoint smooth time pulses \(p_1,p_2\) with

```math
h^{-1}
\int
p_1(s)\,ds
=
\kappa,
\qquad
h^{-1}
\int
p_2(s)\,ds
=
-\kappa.
```

Let

```math
\theta_h
=
p_1+p_2.
```

During the support of \(p_1\), set

```math
B_h(s,Y)=1.
```

During the support of \(p_2\), set

```math
B_h(s,Y)=\sin Y.
```

Because the supports are disjoint, choose an open gap where
\(\theta_h=0\) and interpolate \(B_h\) smoothly from \(1\) to \(\sin Y\)
inside that gap.

Then the complete coefficient field is smooth and

```math
\boxed{
h^{-1}
\int
\theta_h(s)\,ds
=
0.
}
```

## 13. Exact final flow of the separator

The first pulse is a rigid translation of signed time \(\kappa\):

```math
T_\kappa(Z)
=
Z+\kappa.
```

The second pulse is the autonomous \(\sin Y\) flow of signed time
\(-\kappa\).

Hence

```math
\boxed{
\chi_h^{\rm fin}
=
\varphi_{\sin}^{-\kappa}
\circ
T_\kappa.
}
```

No approximation is used.

## 14. Scalar signed clock cancels but geometry does not

Take the lifted starting point

```math
Z_*=-\kappa.
```

After the first pulse,

```math
T_\kappa(Z_*)=0.
```

The second \(\sin Y\) flow fixes \(0\).

From L5-36,

```math
\partial_Y
\varphi_{\sin}^{\tau}(0)
=
e^\tau.
```

Therefore

```math
\boxed{
\partial_Z
\chi_h^{\rm fin}(Z_*)
=
e^{-\kappa}.
}
```

Thus

```math
h^{-1}
\int
\theta_h\,ds
=
0
```

does not imply

```math
J_h^{\rm fin}=1.
```

For \(\kappa\to\infty\), the inverse Jacobian at \(Z_*\) grows as
\(e^\kappa\).

## 15. The Lagrangian strain detects the separator exactly

On the first translation pulse,

```math
\partial_Yv_h=0.
```

At the selected trajectory, the second pulse begins at the fixed point
\(Y=0\), so

```math
\partial_YB_h
=
\cos0
=
1.
```

Therefore the pathwise strain integral on the second pulse is exactly

```math
-\kappa.
```

Hence

```math
\Omega_{1,h}^{\rm fin}(Z_*)
=
-\kappa
```

and

```math
J_h^{\rm fin}(Z_*)
=
e^{\Omega_{1,h}}
=
e^{-\kappa}.
```

The Lagrangian strain cocycle records precisely the deformation missed by the
scalar signed coefficient integral.

## 16. Why "path ordered" is the correct language

In one spatial dimension, the tangent equation itself is scalar, so no matrix
ordering symbol is needed for \(J_h\).

The path ordering enters through:

1. the characteristic \(\chi_h\) inside every coefficient
   \(a_{m,h}(s,Z)\);
2. the ordered composition of distinct spatial vector fields;
3. the nonlinear higher-jet recursions.

Changing the order of two noncommuting spatial profiles changes the final
characteristic map and generally changes the entire jet signature.

Thus a scalar integral of \(\theta_h\) is insufficient.

## 17. Reduction to L5-36

If

```math
B_h(s,Y)
=
B(Y)
```

is independent of time, then the spatial vector field is fixed.

The characteristic flow reduces exactly to

```math
\chi_h(s,Z)
=
\varphi_{\kappa_h(s)}(Z),
\qquad
\kappa_h
=
h^{-1}\int_0^s\theta_h.
```

The full jet cocycle is then a deterministic smooth function of
\((\kappa_h,Z)\).

Therefore L5-37 reduces exactly to L5-36 in the separable case.

## 18. Relation to L5-35

L5-35 assumes a bounded convergent characteristic frame.

L5-37 provides an exact one-dimensional pathwise decomposition of that frame
through:

- basepoint motion \(\Xi_h\);
- tangent strain \(\Omega_{1,h}\);
- normalized curvature jet \(U_{2,h}\);
- normalized third jet \(U_{3,h}\);
- normalized fourth jet \(U_{4,h}\).

This converts the geometric black-box hypothesis into explicit Lagrangian
deformation observables.

It does not yet derive bounds for those observables from Navier--Stokes.

## 19. Next live obligation: C2-MIX-DIRECTION-JET-COST

The smallest safe successor is:

> Can selected active-band Navier--Stokes dynamics force the Lagrangian
> deformation-jet cocycle to remain bounded on critical intervals, or does
> failure of one cocycle component itself pay a selector/dissipation cost?

The first audit should separate:

1. tangent strain \(\Omega_1\);
2. curvature jet \(U_2\);
3. higher metric jets \(U_3,U_4\);
4. rigid basepoint motion \(\Xi\);
5. Lagrangian accumulated scalar phase.

A positive route should derive these observables from equation-level velocity
gradient structure rather than assume the frame contract.

A negative route should exhibit finite A2 occupancy with an unbounded cocycle
component and no compensating charge.

## 20. Hard rejection tests

Reject any successor that:

- uses \(h^{-1}\int\theta_h\) as the nonseparable deformation variable;
- replaces pathwise strain by its Eulerian pointwise value;
- ignores the basepoint/rigid component of the frame;
- controls only \(J_h\) while assuming higher metric derivatives are free;
- invokes matrix noncommutativity for the scalar one-dimensional tangent
  equation itself;
- treats bounded jet cocycle as already derived from selected NSE;
- interprets unbounded cocycle as proof of selector-charge failure without an
  equation-derived cost;
- promotes the conditional frame theorem to A2 closure.

## 21. Claim boundary

The protected claim sought from this tranche is exactly

```text
NONSEPARABLE_DIRECTION_GEOMETRY_CONTROLLED_BY_LAGRANGIAN_JET_COCYCLE
__SCALAR_SIGNED_CLOCK_INSUFFICIENT.
```

It proves:

- exact Lagrangian strain representation
  \(J_h=\exp(\Omega_{1,h})\);
- exact normalized second/third/fourth characteristic-jet recursions;
- the finite signature
  \((\Xi_h,\Omega_{1,h},U_{2,h},U_{3,h},U_{4,h})\)
  reconstructs the frame through fourth spatial order;
- bounded signature implies the smooth bi-Lipschitz frame contract used by
  L5-35;
- \(O(h)\) signature convergence gives \(O(h)\) frame/metric convergence;
- smooth Eulerian scalar-profile convergence then gives \(O(h)\) Lagrangian
  accumulated-phase convergence;
- under protected residual and metric-nondegeneracy hypotheses, the L5-35
  \(c/\nu\) selector-charge theorem transfers;
- a smooth two-profile pulse sequence can have zero total scalar signed clock
  while producing final Jacobian \(e^{-\kappa}\);
- the pathwise tangent strain records that deformation exactly;
- the theorem reduces exactly to L5-36 for time-independent spatial profile.

It does not derive cocycle bounds from selected whole-space NSE.

It does not prove excessive cocycle growth is charged.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
