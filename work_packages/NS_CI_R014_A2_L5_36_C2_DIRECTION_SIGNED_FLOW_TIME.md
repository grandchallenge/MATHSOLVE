# NS-CI-R014-A2-L5-36 — separable direction strain and signed flow time

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Integration base: `f86c378ad29a893092243fb926828f61a53402b6`
- Protected mathematical predecessor:
  `3e184fc3bbc930e7f9813d4a78054b3d8517688b`
- Result:
  `SEPARABLE_DIRECTION_STRAIN_REDUCES_TO_SIGNED_FLOW_TIME__ABSOLUTE_H_SCALE_NOT_NECESSARY`
- A2 theorem: open
- L5: active
- C2-MIX-DIRECTION-STRAIN: separable signed-strain geometry resolved
- MATHCERT adjudication: absent
- Evidence class: conditional critical normal-form theorem and exact
  characteristic-flow identities; not selected whole-space NSE derivation

L5-35 gives an absolute sufficient deformation budget

```math
h^{-1}
\int
|\theta_h|
\|B_h\|_{W^{4,\infty}}
\,ds
=
O(1).
```

For persistent order-one spatial direction gradients this asks for
\(|\theta_h|=O(h)\).

That scale is not necessary even within the one-dimensional principal
direction model.

When the spatial direction profile is separable,

```math
B_h(s,Y)=B(Y),
```

all characteristic geometry depends on one **signed flow time**

```math
\boxed{
\kappa_h(s)
=
h^{-1}
\int_0^s
\theta_h(\sigma)\,d\sigma.
}
```

Let \(\varphi_\kappa\) denote the autonomous flow of \(B\),

```math
\partial_\kappa
\varphi_\kappa(Z)
=
B(
\varphi_\kappa(Z)
),
\qquad
\varphi_0(Z)=Z.
```

Then the full critical characteristic map is exactly

```math
\boxed{
\chi_h(s,Z)
=
\varphi_{\kappa_h(s)}(Z).
}
```

Thus absolute variation of \(\theta_h\) is irrelevant to frame geometry in
this separable class except through the signed clock \(\kappa_h\).

If \(\kappa_h\) remains in a fixed compact interval, the characteristic maps
and their finite spatial derivatives are uniformly bounded.

If moreover

```math
\kappa_h
=
\kappa_0
+
O(h)
```

uniformly in critical time, then

```math
\chi_h
=
\chi_0
+
O(h),
\qquad
J_h
=
J_0
+
O(h)
```

in the finite smooth norms required by L5-35.

For a smooth Eulerian scalar profile \(G_h=G_0+O(h)\), the Lagrangian
accumulated phase also converges at \(O(h)\):

```math
\mathcal F_h(s,Z)
=
\int_0^s
G_h(
\sigma,
\varphi_{\kappa_h(\sigma)}(Z)
)
\,d\sigma
=
\mathcal F_0(s,Z)
+
O(h).
```

Therefore the L5-35 metric phase-mixing theorem applies.

A rapidly oscillating exact separator makes the improvement explicit.

Take

```math
\boxed{
\theta_h(s)
=
\sin(s/h^2).
}
```

Then

```math
\kappa_h(s)
=
h
[
1-\cos(s/h^2)
],
```

so

```math
\boxed{
\sup_s|\kappa_h(s)|
\le
2h.
}
```

Hence the characteristic frame is \(O(h)\)-close to the identity for every
fixed smooth \(B\).

But its absolute L5-35 strain budget satisfies

```math
h^{-1}
\int_0^S
|\theta_h(s)|
\,ds
\asymp
h^{-1}
\to\infty.
```

Thus order-one instantaneous direction-strain amplitude can be fully
compatible with the protected critical frame theorem through signed temporal
cancellation.

For a fixed smooth nondegenerate scalar profile \(G(Y)\),

```math
\mathcal F_h(s,Z)
=
sG(Z)
+
O(h),
```

so the limiting frame is the identity and the protected critical charge
mechanism survives whenever the L5-32 phase nondegeneracy condition holds.

This proves that L5-35's \(O(h)\) persistent absolute strain scale is not a
necessary condition.

A second exact separator shows why the signed flow time still matters.

For

```math
B(Y)=\sin Y,
```

the autonomous flow satisfies

```math
\boxed{
\tan
\left(
\frac{
\varphi_\kappa(Z)
}{2}
\right)
=
e^\kappa
\tan
\left(
\frac Z2
\right).
}
```

The fixed points \(Z=0,\pi\) have Jacobians

```math
\boxed{
\partial_Z\varphi_\kappa(0)
=
e^\kappa,
\qquad
\partial_Z\varphi_\kappa(\pi)
=
e^{-\kappa}.
}
```

Therefore \(|\kappa_h|\to\infty\) produces an exponentially ill-conditioned
frame in this profile.

The next obstruction is genuinely nonseparable direction strain:
\(B_h=B_h(s,Y)\).  Then the characteristic evolution is a time-ordered
composition of different spatial vector fields, and no single scalar signed
clock \(\kappa_h\) captures the geometry.

## 1. Separable principal direction equation

Retain the principal critical model

```math
\partial_s\Phi_h
+
h^{-1}
\theta_h(s)
B(Y)
\partial_Y\Phi_h
+
ih^{-1}G_h(s,Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h
+
r_h.
```

Assume

```math
B\in C^5(\mathbb T;\mathbb R).
```

The direction field is time-dependent only through the scalar coefficient
\(\theta_h\).

## 2. Autonomous spatial flow

Define the autonomous flow of \(B\),

```math
\partial_\kappa
\varphi_\kappa(Z)
=
B(
\varphi_\kappa(Z)
),
\qquad
\varphi_0(Z)=Z.
```

For every finite \(\kappa\), \(\varphi_\kappa\) is an
orientation-preserving smooth circle diffeomorphism.

The group law is

```math
\varphi_{\kappa_1}
\circ
\varphi_{\kappa_2}
=
\varphi_{\kappa_1+\kappa_2}.
```

## 3. Signed critical flow time

Define

```math
\boxed{
\kappa_h(s)
=
h^{-1}
\int_0^s
\theta_h(\sigma)\,d\sigma.
}
```

Then

```math
\kappa_h'(s)
=
h^{-1}\theta_h(s).
```

Set

```math
\chi_h(s,Z)
=
\varphi_{\kappa_h(s)}(Z).
```

By the chain rule,

```math
\begin{aligned}
\partial_s\chi_h
&=
\kappa_h'
\partial_\kappa
\varphi_{\kappa_h}
\\
&=
h^{-1}
\theta_h(s)
B(
\varphi_{\kappa_h}(Z)
)
\\
&=
h^{-1}
\theta_h(s)
B(
\chi_h
).
\end{aligned}
```

Thus \(\chi_h\) is exactly the L5-35 characteristic flow.

## 4. Geometry depends only on signed flow time

Let

```math
J_B(\kappa,Z)
=
\partial_Z
\varphi_\kappa(Z).
```

Then

```math
J_h(s,Z)
=
J_B(
\kappa_h(s),
Z
).
```

Likewise every finite spatial derivative of \(\chi_h\) is a smooth function of

```math
(
\kappa_h(s),
Z
).
```

Therefore for every fixed \(K<\infty\),

```math
\sup_{
|\kappa|\le K
}
\left(
\|
\varphi_\kappa
\|_{W^{4,\infty}}
+
\|
(\varphi_\kappa^{-1})'
\|_{W^{3,\infty}}
\right)
<
\infty.
```

The constant depends on \(B\) and \(K\), not on \(h\).

Hence

```math
\boxed{
\sup_s|\kappa_h(s)|
\le
K
}
```

is a direct sufficient condition for uniformly bounded finite-order
characteristic geometry in the separable class.

## 5. O(h) convergence of frame geometry

Assume there exists a continuous limiting signed clock \(\kappa_0(s)\) such
that

```math
\boxed{
\sup_{0\le s\le S}
|
\kappa_h(s)-\kappa_0(s)
|
\le
C_\kappa h.
}
```

Set

```math
\chi_0(s,Z)
=
\varphi_{\kappa_0(s)}(Z).
```

Smooth dependence of the autonomous flow on its time parameter gives

```math
\boxed{
\sup_s
\|
\chi_h(s)-\chi_0(s)
\|_{W^{4,\infty}}
\le
C h.
}
```

In particular,

```math
\sup_s
\|
J_h(s)-J_0(s)
\|_{W^{3,\infty}}
\le
Ch.
```

Thus the geometric convergence hypothesis of L5-35 follows from convergence
of one scalar signed clock.

## 6. Lagrangian phase convergence

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

Define

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

Define \(\mathcal F_0\) analogously with \(G_0,\chi_0\).

Composition stability for smooth \(G_0\) and the frame convergence give

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

Hence the L5-35 phase-convergence hypothesis follows automatically in this
separable setting.

## 7. Conditional critical charge transfer

Assume the protected initialization/residual contract in the characteristic
frame.

If the metric-weighted limiting second moment

```math
\int
J_0^{-1}
|(\mathcal F_0)_ZA_0|^2
\,dZ
```

is uniformly positive on one fixed critical interval, then L5-35 applies.

Therefore

```math
\boxed{
\int
\Lambda(t)^2
\,dt
\ge
\frac{c_*}{\nu}.
}
```

No absolute \(\int|\theta_h|\) bound is required.

Only the signed flow clock and the resulting characteristic geometry enter.

## 8. Rapidly oscillating order-one strain

Take

```math
\theta_h(s)
=
\sin(s/h^2).
```

Then

```math
\begin{aligned}
\kappa_h(s)
&=
h^{-1}
\int_0^s
\sin(\sigma/h^2)
\,d\sigma
\\
&=
h
[
1-\cos(s/h^2)
].
\end{aligned}
```

Hence

```math
\boxed{
0
\le
\kappa_h(s)
\le
2h.
}
```

Thus

```math
\kappa_h
=
0
+
O(h)
```

uniformly on every fixed critical interval.

Consequently

```math
\chi_h
=
\operatorname{Id}
+
O(h)
```

in the finite smooth frame norm.

## 9. Absolute budget diverges in the same example

For fixed \(S>0\),

```math
\int_0^S
|\sin(s/h^2)|
\,ds
```

has a positive order-one limit scale as \(h\to0\).

More precisely its average density converges to \(2/\pi\), so

```math
\int_0^S
|\sin(s/h^2)|
\,ds
=
\frac{2S}{\pi}
+
o(1).
```

Therefore

```math
\boxed{
h^{-1}
\int_0^S
|\theta_h(s)|
\,ds
\sim
\frac{2S}{\pi h}
\to
\infty.
}
```

Thus the L5-35 absolute deformation budget can fail by an unbounded factor
while the actual frame converges to the identity.

This proves that the L5-35 \(O(h)\) persistent amplitude scale is not
necessary.

## 10. Fixed nondegenerate scalar phase

Let

```math
G_h(s,Y)
=
G(Y)
```

for a fixed smooth real profile.

Because

```math
\chi_h
=
\operatorname{Id}
+
O(h),
```

one has

```math
G(
\chi_h(s,Z)
)
=
G(Z)
+
O(h)
```

in the protected smooth norm.

Hence

```math
\boxed{
\mathcal F_h(s,Z)
=
sG(Z)
+
O(h).
}
```

The limiting frame is \(J_0=1\) and the limiting phase is

```math
\mathcal F_0=sG.
```

For nonconstant \(G\), the protected metric second-moment nondegeneracy holds
on compact positive critical intervals.

Thus the rapidly oscillating order-one direction strain is compatible with
the same critical mixing mechanism.

## 11. Exact \(\sin Y\) autonomous flow

Take

```math
B(Y)=\sin Y.
```

The autonomous ODE is

```math
\partial_\kappa
\varphi_\kappa
=
\sin(
\varphi_\kappa
).
```

Using

```math
\int
\frac{dY}{\sin Y}
=
\log
\tan(Y/2),
```

one obtains

```math
\boxed{
\tan
\left(
\frac{
\varphi_\kappa(Z)
}{2}
\right)
=
e^\kappa
\tan
\left(
\frac Z2
\right).
}
```

This identity extends continuously through the fixed points.

## 12. Hyperbolic fixed-point Jacobians

The points

```math
Z=0,
\qquad
Z=\pi
```

are fixed by the \(\sin Y\) flow.

The Jacobian ODE in autonomous time is

```math
\partial_\kappa
J_B
=
\cos(
\varphi_\kappa
)
J_B.
```

At \(Z=0\),

```math
\cos(
\varphi_\kappa(0)
)
=
1,
```

hence

```math
\boxed{
J_B(\kappa,0)
=
e^\kappa.
}
```

At \(Z=\pi\),

```math
\cos(
\varphi_\kappa(\pi)
)
=
-1,
```

hence

```math
\boxed{
J_B(\kappa,\pi)
=
e^{-\kappa}.
}
```

Therefore the frame condition number is at least

```math
e^{|\kappa|}.
```

## 13. Signed flow time is a sharp geometry variable in the separator

For the \(\sin Y\) profile,

```math
|\kappa_h(s)|
\to
\infty
```

along any sequence forces exponential characteristic ill-conditioning at one
of the two fixed points.

By contrast, bounded \(\kappa_h\) keeps the complete autonomous flow inside a
compact family of smooth diffeomorphisms.

Thus the signed clock is the exact deformation parameter for this separator.

This does not mean bounded \(\kappa_h\) is necessary for every possible
\(B\).  Constant \(B\), for example, gives rigid translation for arbitrary
flow time.

## 14. Relation to L5-35

L5-35 uses the absolute sufficient budget

```math
h^{-1}
\int
|\theta_h|
\|B\|_{W^{4,\infty}}
\,ds
\le
C.
```

L5-36 proves that for separable \(B\), the exact flow instead factors through

```math
\kappa_h
=
h^{-1}
\int
\theta_h\,ds.
```

Hence large absolute strain variation can cancel before it reaches the frame
geometry.

The hierarchy is now

```text
absolute strain budget
        |
        +-- sufficient and easy to verify
        |
signed separable flow time
        |
        +-- exact characteristic geometry variable
```

## 15. Why this is still not the whole-space answer

A generic principal direction profile has

```math
B_h=B_h(s,Y).
```

The spatial vector field itself then changes with time.

Flows at different times need not commute.

There is no scalar group parameter satisfying

```math
\chi_h
=
\varphi_{\kappa_h}
```

for one fixed autonomous \(\varphi\).

The correct object becomes a time-ordered flow, and signed scalar cancellation
of \(\theta_h\) can fail to cancel geometry.

## 16. Next live obligation: C2-MIX-DIRECTION-PATHORDER

The smallest safe successor is:

> For genuinely time-dependent spatial direction profiles, what path-ordered
> strain observable replaces the separable signed clock, and which part of it
> must remain bounded for the L5-35 metric theorem?

The first audit should compare:

1. scalar signed cancellation in \(\theta_h\);
2. noncommuting time-dependent vector fields;
3. characteristic Jacobian accumulation;
4. higher metric derivative growth.

A positive theorem should reduce exactly to \(\kappa_h\) when
\(B_h(s,Y)=B(Y)\).

## 17. Hard rejection tests

Reject any successor that:

- promotes the L5-35 absolute \(O(h)\) scale to necessity;
- replaces the signed integral by the absolute integral in the separable case;
- assumes time-dependent spatial direction fields commute;
- infers bounded geometry from bounded \(\int\theta_h\) when \(B_h\) changes
  shape in time;
- interprets unbounded \(\kappa_h\) as proof of selector-charge failure;
- treats the normal-form theorem as selected whole-space A2 closure.

## 18. Claim boundary

The protected claim sought from this tranche is exactly

```text
SEPARABLE_DIRECTION_STRAIN_REDUCES_TO_SIGNED_FLOW_TIME
__ABSOLUTE_H_SCALE_NOT_NECESSARY.
```

It proves:

- exact factorization of separable principal direction geometry through the
  signed flow time
  \(\kappa_h=h^{-1}\int\theta_h\);
- bounded signed flow time gives bounded finite-order characteristic geometry;
- \(O(h)\) convergence of \(\kappa_h\) gives the L5-35 metric convergence;
- with smooth Eulerian phase convergence, the Lagrangian accumulated phase
  converges at the same order;
- rapidly oscillating order-one
  \(\theta_h=\sin(s/h^2)\)
  has \(\kappa_h=O(h)\) while the absolute strain budget diverges like
  \(h^{-1}\);
- this oscillatory frame is compatible with the protected critical charge
  theorem for nondegenerate fixed scalar profile \(G\);
- the exact \(B=\sin Y\) flow has fixed-point Jacobians \(e^\kappa,e^{-\kappa}\),
  showing signed flow time directly controls exponential deformation in that
  separator.

It does not solve nonseparable time-dependent direction geometry.

It does not prove excessive deformation is charged.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
