# NS-CI-R014-A2-L5-34 — uniform transverse drift as principal moving-frame dynamics

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor:
  `e8c041e8ef6b8845945d3e28b21d3d40ad7b81ab`
- Result:
  `UNIFORM_TRANSVERSE_DRIFT_EXACTLY_PRINCIPALIZED__COMOVING_ACCUMULATED_PHASE_IS_THE_INVARIANT`
- A2 theorem: open
- L5: active
- C2-MIX-DIRECTION-PRINCIPAL: uniform transverse translation resolved
- MATHCERT adjudication: absent
- Evidence class: exact critical normal-form theorem plus calibration examples;
  not a selected whole-space NSE direction-deformation theorem

L5-33 proves that a nondegenerately coupled transverse direction defect cannot
be hidden inside the protected small residual unless it lies in the very narrow

```math
O(h^3)=O(\rho^{-1})
```

corridor.

The first principal case above that corridor is **spatially uniform transverse
drift**.

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

No smallness of `\theta_h` is assumed.

Define the translation path

```math
q_h(s)
=
h^{-1}
\int_0^s\theta_h(\sigma)\,d\sigma.
```

The moving-frame field

```math
\Psi_h(s,y)
=
\Phi_h(s,y+q_h(s))
```

satisfies exactly

```math
\boxed{
\partial_s\Psi_h
+
ih^{-1}\widehat G_h(s,y)\Psi_h
=
h^2(\partial_y^2-1)\Psi_h
+
\widehat r_h,
}
```

where

```math
\widehat G_h(s,y)
=
G_h(s,y+q_h(s)).
```

Thus spatially uniform direction drift is not intrinsically a residual and
does not require an `h^3` bound when it is promoted to the principal
operator.  It is removed exactly by a unitary translation.

The relevant critical object is then the **co-moving accumulated phase**

```math
\boxed{
\widehat F_h(s,y)
=
\int_0^s
G_h(\sigma,y+q_h(\sigma))\,d\sigma.
}
```

Every protected L5-32 conclusion applies with
`\widehat F_h`
in place of `F_h`.

This produces two exact calibration regimes.

### Co-moving profile

If

```math
G_h(s,Y)
=
G_0(Y-q_h(s)),
```

then

```math
\widehat G_h(s,y)
=
G_0(y),
\qquad
\widehat F_h(s,y)
=
sG_0(y).
```

Uniform drift of any size leaves the critical mixing mechanism unchanged.

### Lab-fixed rapidly swept profile

If

```math
G_h(s,Y)
=
\cos Y,
\qquad
\theta_h(s)=\theta_0\ne0,
```

then

```math
q_h(s)=\theta_0s/h
```

and

```math
\boxed{
\widehat F_h(s,y)
=
\frac{h}{\theta_0}
[
\sin(y+\theta_0s/h)-\sin y
].
}
```

Hence

```math
\|\widehat F_h\|_{W^{k,\infty}}
=
O(h)
```

for every fixed spatial derivative order `k`.

The co-moving accumulated phase therefore converges to zero.  The L5-32
critical second moment vanishes instead of remaining order one.

So large uniform drift is not itself a selector-charge theorem.  Depending on
the relative motion of the transport profile, it may preserve the protected
mixing mechanism or average that mechanism away.

The unresolved geometric object is therefore **nonuniform direction
deformation**, not uniform translation.

## 1. Principal equation

Fix a critical interval

```math
0\le s\le S.
```

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

Assume:

- `\theta_h` is real and integrable in critical time;
- `G_h` is real-valued and periodic in `Y`;
- no smallness assumption is made on
  \(\theta_h\).

This is the simplest principal promotion of the L5-33 derivative leakage.

## 2. Exact moving-frame translation

Define

```math
q_h(s)
=
h^{-1}
\int_0^s
\theta_h(\sigma)\,d\sigma.
```

Set

```math
\boxed{
\Psi_h(s,y)
=
\Phi_h(s,y+q_h(s)).
}
```

Then

```math
\partial_s\Psi_h
=
(\partial_s\Phi_h)(s,y+q_h)
+
q_h'(s)
(\partial_Y\Phi_h)(s,y+q_h).
```

Since

```math
q_h'
=
h^{-1}\theta_h,
```

the principal transverse derivative cancels exactly.

Translations commute with \(\partial_Y\), so

```math
\partial_y^2\Psi_h
=
(\partial_Y^2\Phi_h)(s,y+q_h).
```

Therefore

```math
\boxed{
\partial_s\Psi_h
+
ih^{-1}\widehat G_h(s,y)\Psi_h
=
h^2(\partial_y^2-1)\Psi_h
+
\widehat r_h,
}
```

with

```math
\widehat G_h(s,y)
=
G_h(s,y+q_h(s)),
```

and

```math
\widehat r_h(s,y)
=
r_h(s,y+q_h(s)).
```

This is exactly the L5-32 time-dependent-profile normal form.

## 3. Translation preserves the critical norms

For every integer Fourier mode,

```math
\widehat{\Psi_h}(n)
=
e^{inq_h}
\widehat{\Phi_h}(n).
```

Hence

```math
|\widehat{\Psi_h}(n)|
=
|\widehat{\Phi_h}(n)|.
```

Therefore translation preserves:

- `L^2`;
- every standard Sobolev norm;
- every semiclassical `H_h^k` norm;
- the zeroth, scaled second, and scaled fourth Fourier moments;
- frequency-band mass;
- Littlewood--Paley block norms up to the same physical translation.

Thus moving-frame principalization does not alter the selector-scale Fourier
information used by L5-32.

## 4. Co-moving accumulated phase

Define

```math
\boxed{
\widehat F_h(s,y)
=
\int_0^s
\widehat G_h(\sigma,y)\,d\sigma
=
\int_0^s
G_h(
\sigma,
y+q_h(\sigma)
)\,d\sigma.
}
```

The L5-32 exact phase transform now gives

```math
\Psi_h
=
e^{-i\widehat F_h/h}
A_h.
```

Consequently the uniform-drift principal problem is completely reduced to the
protected accumulated-phase bridge.

A sufficient critical mixing condition is:

```math
\widehat F_h
=
\widehat F_0
+
O(h)
```

in the L5-32 fixed spatial smooth norm, together with the protected
semiclassical residual and a nondegenerate co-moving accumulated gradient.

## 5. Co-moving profile calibration

Let `G_0` be one fixed real nonconstant smooth periodic profile and define

```math
\boxed{
G_h(s,Y)
=
G_0(Y-q_h(s)).
}
```

Then

```math
\widehat G_h(s,y)
=
G_h(s,y+q_h(s))
=
G_0(y).
```

Thus

```math
\boxed{
\widehat F_h(s,y)
=
sG_0(y).
}
```

The result is independent of the size or speed of the uniform drift
\(\theta_h\).

The L5-31/L5-32 critical amplitude is therefore

```math
A_0(s,y)
=
\exp(
-s^3|G_0'(y)|^2/3
).
```

If `G_0` is nonconstant, the protected positive critical variance and
`c/\nu` selector-charge mechanism remain intact.

Uniform translation is therefore compatible with full critical mixing.

## 6. Lab-fixed cosine under constant drift

Now take

```math
G_h(s,Y)
=
\cos Y
```

and

```math
\theta_h(s)
=
\theta_0
\ne
0
```

independent of `h` and `s`.

Then

```math
q_h(s)
=
\theta_0s/h,
```

so

```math
\widehat G_h(s,y)
=
\cos(
y+\theta_0s/h
).
```

Its accumulated phase is exactly

```math
\begin{aligned}
\widehat F_h(s,y)
&=
\int_0^s
\cos(
y+\theta_0\sigma/h
)
\,d\sigma
\\
&=
\frac{h}{\theta_0}
[
\sin(
y+\theta_0s/h
)
-
\sin y
].
\end{aligned}
```

Thus, for every fixed integer `k`,

```math
\boxed{
\sup_{0\le s\le S}
\|
\widehat F_h(s)
\|_{W^{k,\infty}}
\le
\frac{2h}{|\theta_0|}.
}
```

The co-moving accumulated phase has the L5-32 limit

```math
\widehat F_0
=
0.
```

## 7. Vanishing critical phase gradient

In the lab-fixed cosine calibration,

```math
\|(\widehat F_h)_y\|_\infty
=
O(h).
```

With zero or protected `O(h)` demodulated residual, L5-32 gives

```math
A_h
=
1
+
O(h)
```

in the semiclassical norm on a fixed critical interval.

The exact first derivative identity is

```math
h\partial_y\Psi_h
=
e^{-i\widehat F_h/h}
[
h\partial_yA_h
-
i(\widehat F_h)_yA_h
].
```

Both terms on the right are `O(h)` in `L^2`.

Hence

```math
\boxed{
h^2
\sum_n
n^2
|
\widehat{\Psi_h}(n)
|^2
=
O(h^2).
}
```

Translation preserves Fourier magnitudes, so the same estimate holds for
\(\Phi_h\).

## 8. Critical-band mass vanishes in the swept calibration

Fix

```math
0<c_-<c_+<\infty.
```

On the band

```math
c_-
\le
|hn|
\le
c_+,
```

one has

```math
h^2n^2
\ge
c_-^2.
```

Therefore

```math
\begin{aligned}
\sum_{c_-\le|hn|\le c_+}
|\widehat{\Phi_h}(n)|^2
&\le
c_-^{-2}
h^2
\sum_n
n^2
|\widehat{\Phi_h}(n)|^2
\\
&=
O(h^2).
\end{aligned}
```

Thus

```math
\boxed{
\sum_{c_-\le|hn|\le c_+}
|\widehat{\Phi_h}(n)|^2
\longrightarrow
0.
}
```

The positive critical-band mass mechanism of L5-26--L5-32 is absent in this
rapid uniform-sweep calibration.

This does **not** prove that every selector charge vanishes.  It proves only
that the protected critical phase-mixing front is not generated by this
mechanism.

## 9. Principal versus residual interpretation

L5-33 says a nondegenerately coupled direction term cannot be treated as a
small residual unless

```math
\theta_h
=
O(h^3)
```

in the stated critical norm.

L5-34 shows that a spatially uniform direction term of arbitrary size need not
be residualized at all.

It can be promoted to principal dynamics and removed exactly by translation.

After that promotion:

- a co-moving profile may retain the full protected mixing charge;
- a lab-fixed rapidly swept profile may have vanishing critical accumulated
  phase and no positive protected critical-band mass.

Therefore the magnitude of uniform drift alone does not determine charge.

The relative co-moving phase does.

## 10. Galilean interpretation

A spatially uniform velocity component is the local form of a Galilean
translation.

This is consistent with the exact moving-frame calculation:

- uniform translation changes phase location but not Fourier magnitudes;
- it cannot by itself define a preferred absolute direction from scalar shell
  data;
- only relative motion between the transport frame and the transverse profile
  enters the co-moving accumulated phase.

No claim is made that every whole-space direction change is Galilean.

## 11. What remains unresolved

The exact translation argument fails once the transverse drift depends on
space.

For example,

```math
h^{-1}
V_h(s,Y)
\partial_Y\Phi_h
```

with nonconstant `V_h` is not removed by one translation.

A general characteristic flow can remove the first-order transport, but then:

- the spatial metric changes;
- the diffusion operator acquires variable coefficients;
- derivatives of the flow map enter;
- compression/stretching can create its own frequency growth.

That is a genuinely different principal problem.

## 12. Next live obligation: C2-MIX-DIRECTION-DEFORMATION

The smallest safe successor is:

> Analyze spatially nonuniform transverse direction drift after promotion to
> principal characteristic dynamics.

The first bounded calculation should consider a one-dimensional moving flow

```math
\partial_s\Phi_h
+
h^{-1}V(Y)\partial_Y\Phi_h
+
ih^{-1}G(Y)\Phi_h
=
h^2\partial_Y^2\Phi_h
```

and compute exactly how the characteristic pullback transforms the diffusion
operator.

The decisive object is the deformation gradient of the flow.

If its growth immediately creates critical frequency/dissipation, record the
charge mechanism.

If it merely changes coordinates without a non-summable cost, record that
obstruction.

## 13. Hard rejection tests

Reject any successor that:

- counts spatially uniform drift as an automatic selector charge;
- applies the L5-33 `h^3` residual corridor after the drift has been
  principalized exactly;
- assumes a lab-fixed profile is co-moving;
- assumes a co-moving profile is lab-fixed;
- concludes from vanishing L5-32 critical-band mass that all selector charge
  vanishes;
- treats a nonuniform drift as a pure translation;
- promotes the conditional critical model to whole-space A2 closure.

## 14. Claim boundary

The protected claim sought from this tranche is exactly

```text
UNIFORM_TRANSVERSE_DRIFT_EXACTLY_PRINCIPALIZED
__COMOVING_ACCUMULATED_PHASE_IS_THE_INVARIANT.
```

It proves:

- exact moving-frame removal of arbitrary spatially uniform transverse drift;
- preservation of Fourier magnitudes and critical norms under that
  translation;
- reduction to L5-32 with the co-moving accumulated phase
  \(\widehat F_h\);
- preservation of the full critical mixing mechanism for a co-moving
  nonconstant profile;
- \(O(h)\) accumulated phase and vanishing positive critical-band mass for a
  lab-fixed cosine under fixed nonzero rapid drift;
- uniform drift magnitude alone is not a selector-charge criterion.

It does not resolve spatially nonuniform direction deformation.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
