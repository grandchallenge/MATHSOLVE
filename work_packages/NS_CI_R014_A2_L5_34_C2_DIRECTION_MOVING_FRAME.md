# NS-CI-R014-A2-L5-34 — uniform direction motion as principal moving-frame dynamics

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor:
  `e8c041e8ef6b8845945d3e28b21d3d40ad7b81ab`
- Result:
  `UNIFORM_DIRECTION_MOTION_REMOVED_BY_EXACT_MOVING_FRAME__LAGRANGIAN_ACCUMULATED_PHASE_CONTROLS_CHARGE`
- A2 theorem: open
- L5: active
- C2-MIX-DIRECTION-PRINCIPAL: rigid transverse motion resolved conditionally
- MATHCERT adjudication: absent
- Evidence class: conditional critical normal-form theorem;
  not a derivation of a moving frame from selected whole-space NSE

L5-33 proves that a transverse direction defect cannot be hidden inside the
protected residual unless it is as small as

```math
O(h^3)=O(\rho^{-1})
```

under nondegenerate coupling.

That does **not** mean every larger direction motion is an error.

A spatially uniform transverse drift can be promoted into the principal
operator and removed exactly by a moving frame.

Consider

```math
\boxed{
\partial_s\Phi_h
+
h^{-1}\theta_h(s)\partial_Y\Phi_h
+
ih^{-1}G_h(s,Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h
+
r_h.
}
```

No smallness assumption is imposed on \(\theta_h\).

Define the moving-frame displacement

```math
\Gamma_h(s)
=
h^{-1}
\int_0^s
\theta_h(\sigma)\,d\sigma.
```

Set

```math
\Psi_h(s,Y)
=
\Phi_h(s,Y+\Gamma_h(s)).
```

Then the direction derivative cancels exactly:

```math
\boxed{
\partial_s\Psi_h
+
ih^{-1}\widetilde G_h(s,Y)\Psi_h
=
h^2(\partial_Y^2-1)\Psi_h
+
\widetilde r_h,
}
```

where

```math
\widetilde G_h(s,Y)
=
G_h(s,Y+\Gamma_h(s)),
\qquad
\widetilde r_h(s,Y)
=
r_h(s,Y+\Gamma_h(s)).
```

Translation preserves every spatial Fourier magnitude and every
semiclassical norm used in L5-28--L5-33.

Therefore L5-32 applies **verbatim** in the moving frame.

The decisive phase is not the Eulerian integral of \(G_h\), but the
Lagrangian/moving-frame accumulated phase

```math
\boxed{
\mathcal F_h(s,Y)
=
\int_0^s
G_h(
\sigma,
Y+\Gamma_h(\sigma)
)
\,d\sigma.
}
```

If

```math
\mathcal F_h
=
\mathcal F_0
+
O(h)
```

in the protected spatial smooth norm and the limiting accumulated phase
gradient is nondegenerate, then the full L5-32 critical-mixing conclusion
survives:

```math
\Lambda
\gtrsim
N\rho^{1/3},
\qquad
\int \Lambda^2dt
\gtrsim
\nu^{-1}.
```

Thus direction motion larger than the L5-33 residual corridor can be harmless
to the proof architecture **if it is principal rigid frame motion and the
moving-frame accumulated phase remains nondegenerate**.

The magnitude of direction drift alone does not guarantee mixing.

For example, take

```math
G_h(s,Y)=\cos Y,
\qquad
\theta_h(s)=\theta_0\ne0.
```

Then

```math
\Gamma_h(s)
=
\theta_0s/h
```

and

```math
\widetilde G_h(s,Y)
=
\cos(Y+\theta_0s/h).
```

Its accumulated phase is

```math
\boxed{
\mathcal F_h(s,Y)
=
\frac h{\theta_0}
[
\sin(Y+\theta_0s/h)-\sin Y
],
}
```

hence

```math
\|\mathcal F_h\|_{W^{k,\infty}}
=
O(h)
```

for every fixed spatial \(k\).

The limiting accumulated phase is therefore zero, and the protected
critical second/fourth moment lower mechanism degenerates.

So a theorem based only on the size of direction motion is unavailable even
at the principal normal-form level.

The next unresolved object is **nonuniform direction deformation**.  If the
principal direction field is

```math
h^{-1}\theta_h(s)B_h(s,Y)\partial_Y,
```

its characteristic flow has a nontrivial Jacobian.  The derivative of that
Jacobian is amplified by \(h^{-1}\), so the moving frame is no longer an
isometry and diffusion acquires variable coefficients.

## 1. Principal rigid-direction normal form

Fix a critical interval

```math
0\le s\le S.
```

Assume

```math
\theta_h\in L^1(0,S;\mathbb R)
```

and \(G_h\) is real-valued.

Consider

```math
\partial_s\Phi_h
+
h^{-1}\theta_h(s)\partial_Y\Phi_h
+
ih^{-1}G_h(s,Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h
+
r_h.
```

The drift coefficient may be order one or larger.

Only its time integral is needed to define the translation.

## 2. Exact moving-frame conjugation

Define

```math
\Gamma_h(s)
=
h^{-1}
\int_0^s\theta_h(\sigma)\,d\sigma.
```

Let

```math
(T_{\Gamma_h(s)}f)(Y)
=
f(Y+\Gamma_h(s)).
```

Set

```math
\Psi_h
=
T_{\Gamma_h}\Phi_h.
```

Then

```math
\partial_s\Psi_h
=
T_{\Gamma_h}\partial_s\Phi_h
+
\Gamma_h'
T_{\Gamma_h}\partial_Y\Phi_h.
```

Because

```math
\Gamma_h'
=
h^{-1}\theta_h,
```

the derivative term cancels exactly.

Also translations commute with \(\partial_Y\) and \(\partial_Y^2\).

Hence

```math
\boxed{
\partial_s\Psi_h
+
ih^{-1}\widetilde G_h\Psi_h
=
h^2(\partial_Y^2-1)\Psi_h
+
\widetilde r_h.
}
```

## 3. Exact isometry of the protected norms

For every translation parameter \(\Gamma\),

```math
\|T_\Gamma f\|_2
=
\|f\|_2.
```

Because translations commute with \(h\partial_Y\),

```math
\boxed{
\|T_\Gamma f\|_{H_h^2}
=
\|f\|_{H_h^2}.
}
```

If

```math
f(Y)
=
\sum_n
\widehat f_n e^{inY},
```

then

```math
\widehat{T_\Gamma f}_n
=
e^{in\Gamma}
\widehat f_n.
```

Therefore

```math
\boxed{
|
\widehat{T_\Gamma f}_n
|
=
|\widehat f_n|.
}
```

The moving frame preserves the complete Fourier magnitude distribution.

Thus all zeroth, scaled second, and scaled fourth Fourier moments are
unchanged.

## 4. Moving-frame accumulated phase

Define

```math
\boxed{
\mathcal F_h(s,Y)
=
\int_0^s
\widetilde G_h(\sigma,Y)
\,d\sigma
=
\int_0^s
G_h(
\sigma,
Y+\Gamma_h(\sigma)
)
\,d\sigma.
}
```

This is the phase actually sampled by the moving packet.

Assume there is a real limit

```math
\mathcal F_0
\in
C([0,S];W^{4,\infty}(\mathbb T))
```

such that

```math
\boxed{
\sup_{0\le s\le S}
\|
\mathcal F_h(s)-\mathcal F_0(s)
\|_{W^{4,\infty}}
\le
C h.
}
```

No smallness of \(\theta_h\) is required.

No smallness of the Eulerian instantaneous profile drift is required.

## 5. Demodulation after frame motion

Set

```math
\Psi_h
=
e^{-i\mathcal F_h/h}A_h.
```

Because

```math
\partial_s\mathcal F_h
=
\widetilde G_h,
```

the fast scalar potential cancels exactly.

The amplitude equation is the protected L5-32 equation:

```math
\boxed{
\begin{aligned}
\partial_sA_h
={}&
h^2\partial_Y^2A_h
-
2ih(\mathcal F_h)_Y\partial_YA_h
-
ih(\mathcal F_h)_{YY}A_h
\\
&-
|(\mathcal F_h)_Y|^2A_h
-
h^2A_h
+
\widehat r_h,
\end{aligned}
}
```

where

```math
\widehat r_h
=
e^{i\mathcal F_h/h}
\widetilde r_h.
```

## 6. Residual and initialization invariance

Suppose the original packet satisfies the L5-28/L5-32 semiclassical
initialization and residual bounds after the two exact conjugations.

Translations preserve \(H_h^2\), while multiplication by the demodulating
phase is exactly the same operation already covered in L5-32.

Hence the protected convergence proof carries over without a new loss.

In particular, if

```math
\|
A_h(0)-1
\|_{H_h^2}
=
O(h)
```

and

```math
\|
\widehat r_h
\|_{L^2_sH_h^2}
=
O(h),
```

then

```math
A_h
\to
A_0
```

at \(O(h)\) in the protected semiclassical norm.

## 7. Moving-frame critical amplitude

The limiting amplitude is

```math
\boxed{
A_0(s,Y)
=
\exp
\left(
-
\int_0^s
|
(\mathcal F_0)_Y(\sigma,Y)
|^2
\,d\sigma
\right).
}
```

The formula is identical to L5-32, but with the moving-frame accumulated phase
\(\mathcal F_0\).

## 8. Fourier moment limits

Because translation changes only Fourier phases, the Fourier magnitude
distribution of \(\Phi_h\) equals that of \(\Psi_h\).

Therefore

```math
\boxed{
h^2
\sum_n
n^2
|\widehat\Phi_h(n)|^2
\longrightarrow
\|
(\mathcal F_0)_Y A_0
\|_2^2.
}
```

Likewise

```math
\boxed{
h^4
\sum_n
n^4
|\widehat\Phi_h(n)|^2
\longrightarrow
\|
(\mathcal F_0)_Y^2 A_0
\|_2^2.
}
```

Thus the critical Fourier distribution is controlled by the accumulated phase
seen along the moving frame.

## 9. Charge theorem under moving-frame nondegeneracy

Assume on one fixed positive critical interval \(J\),

```math
\boxed{
\inf_{s\in J}
\|
(\mathcal F_0)_Y(s)
A_0(s)
\|_2
\ge
m_*>0.
}
```

Then the L5-32 Paley--Zygmund/Markov argument applies unchanged.

There is fixed positive mass at

```math
|n|
\asymp
h^{-1}.
```

Under the protected packet reconstruction contract, one physical block has
frequency

```math
\lambda_p
\asymp
N\rho^{1/3}.
```

Its amplitude is threshold violating for sufficiently large \(R\).

Consequently

```math
\boxed{
\int_{I_{\rm crit}}
\Lambda(t)^2
\,dt
\ge
\frac{c_*}{\nu}.
}
```

The constant is independent of \(R\).

## 10. No small direction corridor for principal rigid motion

L5-33 proves the \(h^3\) corridor only when the direction term is classified as
**residual**.

The present theorem shows that a spatially uniform direction drift can instead
be principal with no smallness requirement.

Therefore the correct dichotomy is

```text
uniform direction motion
        |
        +-- residual classification --> requires O(h^3)
        |
        +-- principal moving frame --> no size restriction;
                                      test moving-frame accumulated phase
```

The two statements are compatible.

## 11. Fast rigid drift can average the phase

Take

```math
G_h(s,Y)
=
\cos Y,
\qquad
\theta_h(s)
=
\theta_0\ne0.
```

Then

```math
\Gamma_h(s)
=
\theta_0s/h.
```

Hence

```math
\widetilde G_h(s,Y)
=
\cos(
Y+\theta_0s/h
).
```

The moving-frame accumulated phase is

```math
\begin{aligned}
\mathcal F_h(s,Y)
&=
\int_0^s
\cos(
Y+\theta_0\sigma/h
)
\,d\sigma
\\
&=
\frac h{\theta_0}
[
\sin(
Y+\theta_0s/h
)
-
\sin Y
].
\end{aligned}
```

Therefore

```math
\boxed{
\sup_{0\le s\le S}
\|
\mathcal F_h(s)
\|_{W^{k,\infty}}
\le
C_{k,\theta_0}h
}
```

for every fixed \(k\).

Thus

```math
\mathcal F_0
=
0.
```

The limiting amplitude is

```math
A_0=1
```

and the protected scaled second/fourth moment limits are zero.

Hence **order-one direction speed alone does not imply the L5-32 critical
mixing mechanism**.

This is a normal-form route separator, not a selected whole-space trajectory
claim and not a proof that every selector charge vanishes.

## 12. Why direction magnitude alone is insufficient

The two rigid-motion cases

```math
\theta_h=0
```

and

```math
\theta_h=\theta_0\ne0
```

can have the same Eulerian profile \(G(Y)=\cos Y\).

But the moving-frame phases are respectively

```math
\mathcal F_h=s\cos Y
```

and

```math
\mathcal F_h=O(h).
```

One has a nondegenerate critical phase.

The other has complete leading-order phase averaging.

Therefore no theorem depending only on

```math
|\theta_h|
```

can replace the moving-frame phase calculation.

## 13. Nonuniform direction motion changes the metric

Now consider

```math
h^{-1}
\theta_h(s)
B_h(s,Y)
\partial_Y.
```

Let the characteristic flow satisfy

```math
\partial_s
\chi_h(s,Z)
=
h^{-1}
\theta_h(s)
B_h(
s,
\chi_h(s,Z)
),
\qquad
\chi_h(0,Z)=Z.
```

Its Jacobian

```math
J_h
=
\partial_Z\chi_h
```

obeys

```math
\boxed{
\partial_sJ_h
=
h^{-1}
\theta_h(s)
(\partial_YB_h)(
s,\chi_h
)
J_h.
}
```

Hence

```math
\boxed{
J_h(s,Z)
=
\exp
\left(
h^{-1}
\int_0^s
\theta_h(\sigma)
(\partial_YB_h)(
\sigma,\chi_h(\sigma,Z)
)
\,d\sigma
\right).
}
```

Unlike rigid translation, this frame is not automatically an isometry.

## 14. Diffusion under a deformed frame

Under a nonuniform characteristic change of variables, the Laplacian no longer
commutes with the pullback.

In one transverse dimension it becomes a variable-coefficient second-order
operator involving

```math
J_h^{-2}\partial_Z^2
```

plus lower-order terms containing derivatives of \(J_h\).

Thus order-one deformation in \(J_h\) changes the critical diffusion operator.

If the exponent controlling \(J_h\) is large, the L5-32/L5-34 semiclassical
energy structure does not transfer automatically.

This is the next genuine direction-coherence boundary.

## 15. A minimal deformation budget

A sufficient elementary condition for bounded frame distortion is

```math
\boxed{
h^{-1}
\int_0^S
|
\theta_h(s)
|
\|
\partial_YB_h(s)
\|_\infty
\,ds
\le
C.
}
```

Then

```math
e^{-C}
\le
J_h
\le
e^C.
```

This alone is not enough to prove the full critical theorem, because derivatives
of the transformed metric must also be controlled.

But it identifies the first exact quantity absent in the rigid case.

## 16. Relation to L5-33

L5-33 says:

```text
direction derivative term hidden as residual
        --> theta = O(h^3)
```

under nondegenerate coupling.

L5-34 says:

```text
spatially uniform direction derivative term promoted to principal
        --> no theta smallness needed;
            exact moving-frame reduction
```

provided the **moving-frame accumulated phase** is nondegenerate.

Thus the \(h^3\) corridor is not a physical prohibition on direction motion.

It is only the cost of pretending principal rigid motion is a small residual.

## 17. Consequence for the whole-space bridge

The next whole-space extraction problem should not seek a fixed direction.

It should seek either:

1. a rigid or nearly rigid moving frame whose Lagrangian accumulated phase is
   nondegenerate; or
2. quantitative control of the deformation tensor/Jacobian of a nonuniform
   moving frame.

This is weaker and more geometrically natural than forcing all direction drift
into NF4.

## 18. Next live obligation: C2-MIX-DIRECTION-DEFORM

The smallest safe successor is:

> For a nonuniform principal direction field, how much characteristic-frame
> deformation can the critical phase-mixing theorem tolerate before the
> transformed diffusion and Fourier-moment argument fail?

The first audit should control:

- the flow Jacobian \(J_h\);
- the transformed diffusion metric;
- the semiclassical commutators created by that metric;
- the accumulated phase along characteristics.

A positive theorem should reduce to L5-34 when \(\partial_YB_h=0\).

A negative theorem should identify an explicit deformation regime in which
metric growth destroys the protected moment argument.

## 19. Hard rejection tests

Reject any successor that:

- applies the L5-33 \(h^3\) corridor to a direction term after promoting it to
  principal dynamics;
- assumes a rigid moving frame when \(B_Y\ne0\);
- uses Eulerian accumulated phase instead of phase along characteristics;
- infers mixing from direction speed alone;
- interprets the fast-sweep example as proof of zero selector charge;
- ignores the transformed diffusion metric under a nonuniform frame;
- promotes the conditional normal-form theorem to selected whole-space A2.

## 20. Claim boundary

The protected claim sought from this tranche is exactly

```text
UNIFORM_DIRECTION_MOTION_REMOVED_BY_EXACT_MOVING_FRAME
__LAGRANGIAN_ACCUMULATED_PHASE_CONTROLS_CHARGE.
```

It proves:

- exact removal of arbitrary spatially uniform transverse direction motion by
  translation;
- exact preservation of Fourier magnitudes and \(H_h^2\) under that frame;
- reduction to L5-32 with moving-frame accumulated phase
  \(\mathcal F_h\);
- nondegenerate moving-frame accumulated phase gives the same critical
  \(c/\nu\) selector charge;
- no smallness of rigid direction speed is required;
- fast rigid drift can average the accumulated phase to zero, so direction
  magnitude alone does not imply critical mixing;
- nonuniform direction motion introduces a characteristic Jacobian and a
  variable transformed diffusion metric.

It does not prove a nonuniform moving-frame theorem.

It does not derive a principal moving frame from selected whole-space NSE.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
