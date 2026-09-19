# NS-CI-R014-A2-L5-35 — bounded nonuniform direction-frame deformation

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor:
  `beef1555be9f61ced61379d3ea6ba4c8d9d4e913`
- Result:
  `BOUNDED_NONUNIFORM_FRAME_DEFORMATION_PRESERVES_CRITICAL_MIXING__ABSOLUTE_DIRECTION_STRAIN_BUDGET_IS_H_SCALE`
- A2 theorem: open
- L5: active
- C2-MIX-DIRECTION-DEFORM: bounded smooth characteristic deformation resolved conditionally
- MATHCERT adjudication: absent
- Evidence class: conditional one-dimensional critical normal-form theorem;
  not a derivation of characteristic-frame bounds from selected whole-space NSE

L5-34 removes arbitrary spatially uniform transverse direction motion exactly
by translation.

For spatially nonuniform principal direction motion, translation is replaced by
a characteristic diffeomorphism.  The transformed frame is no longer
isometric, but the critical phase-mixing theorem still survives under a
uniform smooth bi-Lipschitz deformation contract.

Consider

```math
\boxed{
\partial_s\Phi_h
+
h^{-1}\theta_h(s)B_h(s,Y)\partial_Y\Phi_h
+
ih^{-1}G_h(s,Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h
+
r_h.
}
```

Let the characteristic flow solve

```math
\partial_s\chi_h(s,Z)
=
h^{-1}\theta_h(s)
B_h(s,\chi_h(s,Z)),
\qquad
\chi_h(0,Z)=Z,
```

and write

```math
J_h=\partial_Z\chi_h.
```

If the flow is uniformly smooth and bi-Lipschitz,

```math
0<j_-\le J_h\le j_+<\infty,
```

with fixed spatial derivative bounds and a smooth limiting metric
`J_h\to J_0`, then pullback by \(\chi_h\) converts diffusion to

```math
\boxed{
\partial_Y^2
\longmapsto
J_h^{-2}\partial_Z^2
-
J_h^{-3}(J_h)_Z\partial_Z.
}
```

After exact accumulated-phase removal along characteristics, the leading
critical damping is

```math
-
J_h^{-2}
|(\mathcal F_h)_Z|^2.
```

Thus the limiting amplitude is

```math
\boxed{
A_0(s,Z)
=
\exp
\left(
-
\int_0^s
J_0(\sigma,Z)^{-2}
|(\mathcal F_0)_Z(\sigma,Z)|^2
\,d\sigma
\right).
}
```

The physical Fourier moments are not lost under the nonlinear frame.  They are
recovered from physical derivatives before applying Parseval:

```math
\boxed{
h^2
\sum_n n^2|\widehat\Phi_h(n)|^2
\longrightarrow
\int
J_0^{-1}
|(\mathcal F_0)_ZA_0|^2\,dZ,
}
```

and

```math
\boxed{
h^4
\sum_n n^4|\widehat\Phi_h(n)|^2
\longrightarrow
\int
J_0^{-3}
|(\mathcal F_0)_Z|^4
|A_0|^2\,dZ.
}
```

Hence uniform positive metric-weighted second moment and finite fourth moment
again imply positive physical critical-band mass and the protected
`c/\nu` selector-charge mechanism.

This theorem identifies a sufficient absolute deformation budget.

Since

```math
\partial_sJ_h
=
h^{-1}\theta_h(s)
(\partial_YB_h)(s,\chi_h)
J_h,
```

one has

```math
|\log J_h|
\le
h^{-1}
\int
|\theta_h|
\|\partial_YB_h\|_\infty
\,ds.
```

Therefore

```math
\boxed{
h^{-1}
\int_0^S
|\theta_h(s)|
\|B_h(s)\|_{W^{4,\infty}}
\,ds
\le
C
}
```

is a convenient sufficient route to uniform finite-order characteristic
geometry.

For an order-one spatial direction gradient persisting on an order-one
critical interval, this absolute route asks for

```math
|\theta_h|
=
O(h)
=
O(\rho^{-1/3}).
```

This is much wider than the L5-33 residual corridor
`O(h^3)=O(\rho^{-1})`.

The \(O(h)\) scale is only a sufficient absolute deformation budget.  It is not
claimed necessary.  Signed or oscillatory strain may cancel along
characteristics.

An exact route separator shows why some geometric budget is required.
For

```math
B(Y)=\sin Y,
\qquad
\theta_h=\theta_0>0,
```

the characteristic starting at \(Z=0\) remains at \(Y=0\), while

```math
\boxed{
J_h(s,0)
=
\exp(\theta_0s/h).
}
```

Thus order-one nonuniform direction strain can create exponentially large
frame distortion on critical time.  This does not prove charge failure; it
proves only that the bounded-frame transfer theorem cannot be automatic.

The next whole-space obligation is therefore no longer direction motion
itself.  It is direction **strain**:

> derive a bounded characteristic-deformation budget from selected
> Navier--Stokes structure, or prove that excessive direction strain pays a
> selector/dissipation charge.

## 1. Nonuniform principal direction equation

Fix

```math
0\le s\le S.
```

Consider

```math
\partial_s\Phi_h
+
v_h(s,Y)\partial_Y\Phi_h
+
ih^{-1}G_h(s,Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h
+
r_h,
```

where

```math
v_h(s,Y)
=
h^{-1}\theta_h(s)B_h(s,Y).
```

The direction term is principal.

It is not assigned to the L5-28 residual.

## 2. Characteristic frame

Let

```math
\partial_s\chi_h
=
v_h(s,\chi_h),
\qquad
\chi_h(0,Z)=Z.
```

Assume each \(\chi_h(s,\cdot)\) is an orientation-preserving periodic
diffeomorphism.

Define

```math
J_h(s,Z)
=
\partial_Z\chi_h(s,Z).
```

Set

```math
\Psi_h(s,Z)
=
\Phi_h(s,\chi_h(s,Z)).
```

Then

```math
\partial_s\Psi_h
=
(\partial_s\Phi_h+v_h\partial_Y\Phi_h)
\circ\chi_h.
```

Thus the principal direction derivative cancels exactly.

## 3. Exact transformed derivatives

At

```math
Y=\chi_h(s,Z),
```

the chain rule gives

```math
\boxed{
(\partial_Y\Phi_h)\circ\chi_h
=
J_h^{-1}
\partial_Z\Psi_h.
}
```

A second derivative gives

```math
\boxed{
(\partial_Y^2\Phi_h)\circ\chi_h
=
J_h^{-2}
\partial_Z^2\Psi_h
-
J_h^{-3}(J_h)_Z
\partial_Z\Psi_h.
}
```

Define

```math
a_h=J_h^{-2},
\qquad
b_h=-J_h^{-3}(J_h)_Z.
```

Then the transformed equation is

```math
\boxed{
\partial_s\Psi_h
+
ih^{-1}\widetilde G_h\Psi_h
=
h^2
[
a_h\partial_Z^2\Psi_h
+
b_h\partial_Z\Psi_h
-
\Psi_h
]
+
\widetilde r_h,
}
```

where

```math
\widetilde G_h
=
G_h\circ\chi_h,
\qquad
\widetilde r_h
=
r_h\circ\chi_h.
```

## 4. Physical measure and diffusion identity

The physical measure transforms as

```math
dY
=
J_h\,dZ.
```

The transformed diffusion is symmetric in that physical measure.

Indeed,

```math
\begin{aligned}
&
\operatorname{Re}
\int
\overline\Psi
[
J_h^{-2}\Psi_{ZZ}
-
J_h^{-3}(J_h)_Z\Psi_Z
]
J_h\,dZ
\\
&=
-
\int
J_h^{-1}
|\Psi_Z|^2\,dZ.
\end{aligned}
```

The derivative of \(J_h^{-1}\) generated by integration by parts cancels the
explicit first-order coefficient.

This is the correct metric energy identity.

## 5. Bounded smooth frame contract

Assume fixed constants

```math
0<j_-<j_+<\infty
```

such that

```math
j_-
\le
J_h(s,Z)
\le
j_+
```

on the full critical cylinder.

Assume also fixed spatial smoothness

```math
\sup_h
\sup_s
(
\|J_h\|_{W^{3,\infty}}
+
\|J_h^{-1}\|_{W^{3,\infty}}
)
\le
C_J.
```

Finally assume there is a smooth positive limit \(J_0\) such that

```math
\boxed{
\sup_s
\|J_h(s)-J_0(s)\|_{W^{3,\infty}}
\le
C_Jh.
}
```

These are characteristic-frame hypotheses.

They are not claimed automatic.

## 6. Lagrangian accumulated phase

Define

```math
\boxed{
\mathcal F_h(s,Z)
=
\int_0^s
G_h(
\sigma,
\chi_h(\sigma,Z)
)
\,d\sigma.
}
```

Assume a limit

```math
\mathcal F_0
\in
C([0,S];W^{4,\infty})
```

with

```math
\boxed{
\sup_s
\|
\mathcal F_h(s)-\mathcal F_0(s)
\|_{W^{4,\infty}}
\le
C_Fh.
}
```

This is the nonuniform-frame analogue of L5-34.

## 7. Exact phase removal

Set

```math
\Psi_h
=
e^{-i\mathcal F_h/h}
A_h.
```

Since

```math
\partial_s\mathcal F_h
=
\widetilde G_h,
```

the fast scalar potential cancels exactly.

Expanding the metric diffusion gives

```math
\boxed{
\begin{aligned}
\partial_sA_h
={}&
h^2a_hA_{ZZ}
+
h^2b_hA_Z
-
h^2A_h
\\
&-
2ih a_h(\mathcal F_h)_ZA_Z
\\
&-
ih
[
a_h(\mathcal F_h)_{ZZ}
+
b_h(\mathcal F_h)_Z
]
A_h
\\
&-
a_h
|(\mathcal F_h)_Z|^2
A_h
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

The order-one real damping is the metric-weighted term

```math
-a_h|(\mathcal F_h)_Z|^2.
```

## 8. Semiclassical frame norm

Use

```math
D_h=h\partial_Z.
```

Define

```math
\|f\|_{H_{h,Z}^2}^2
=
\sum_{j=0}^2
\|D_h^jf\|_{L^2_Z}^2.
```

Uniform bi-Lipschitz control makes this norm uniformly equivalent, after the
coordinate map, to the corresponding finite-order physical semiclassical
derivative control.

The coefficients \(a_h,b_h\) and their required derivatives are uniformly
bounded by the frame contract.

Commuting \(D_h\) through these coefficients always produces at least one
explicit factor \(h\).

Therefore the L5-28/L5-32 semiclassical energy induction extends to this
variable metric.

## 9. Initialization and residual

Assume

```math
\|A_h(0)-1\|_{H_{h,Z}^2}
\le
C_{\rm in}h.
```

Assume also

```math
\boxed{
\left(
\int_0^S
\|
\widehat r_h(s)
\|_{H_{h,Z}^2}^2
\,ds
\right)^{1/2}
\le
C_rh.
}
```

This is the protected residual size in the characteristic frame.

## 10. Limiting amplitude

Set

```math
a_0
=
J_0^{-2}.
```

The limiting equation is

```math
\partial_sA_0
=
-
a_0
|(\mathcal F_0)_Z|^2
A_0,
\qquad
A_0(0)=1.
```

Therefore

```math
\boxed{
A_0(s,Z)
=
\exp
\left(
-
\int_0^s
J_0(\sigma,Z)^{-2}
|(\mathcal F_0)_Z(\sigma,Z)|^2
\,d\sigma
\right).
}
```

It is strictly positive on the fixed critical interval.

## 11. Strong semiclassical convergence

Let

```math
W_h=A_h-A_0.
```

The frame and phase convergence hypotheses give

```math
a_h-a_0
=
O(h)
```

in the fixed coefficient norm.

Inserting \(A_0\) into the finite-\(h\) equation produces:

- \(O(h)\) first-order imaginary terms;
- \(O(h^2)\) metric diffusion and scalar terms;
- \(O(h)\) coefficient errors in
  \(a_h|(\mathcal F_h)_Z|^2\).

The uniform metric energy estimate and residual bound therefore give

```math
\boxed{
\sup_{0\le s\le S}
\|A_h(s)-A_0(s)\|_{H_{h,Z}^2}
\le
Ch.
}
```

## 12. Physical zeroth moment

Let the physical Fourier expansion be

```math
\Phi_h(s,Y)
=
\sum_n
c_n^{(h)}(s)
e^{inY}.
```

Then

```math
\sum_n|c_n^{(h)}|^2
=
\|\Phi_h\|_{L^2_Y}^2.
```

In characteristic coordinates,

```math
\|\Phi_h\|_{L^2_Y}^2
=
\int
|A_h(s,Z)|^2
J_h(s,Z)\,dZ.
```

Hence

```math
\boxed{
\sum_n|c_n^{(h)}|^2
\longrightarrow
\int
|A_0|^2J_0\,dZ.
}
```

The limiting mass is positive.

## 13. Physical scaled second moment

Using the exact physical derivative identity,

```math
h(\partial_Y\Phi_h)\circ\chi_h
=
J_h^{-1}
e^{-i\mathcal F_h/h}
[
hA_{h,Z}
-
i(\mathcal F_h)_ZA_h
].
```

Because

```math
hA_{h,Z}
\to
0
```

and \(dY=J_h\,dZ\),

```math
\boxed{
h^2
\sum_n
n^2|c_n^{(h)}|^2
\longrightarrow
\int
J_0^{-1}
|(\mathcal F_0)_Z A_0|^2
\,dZ.
}
```

This is the physical metric-weighted critical variance.

## 14. Physical scaled fourth moment

The exact second-derivative pullback is

```math
(\partial_Y^2\Phi_h)\circ\chi_h
=
J_h^{-2}\Psi_{h,ZZ}
-
J_h^{-3}(J_h)_Z\Psi_{h,Z}.
```

After phase removal, the leading order term in

```math
h^2
(\partial_Y^2\Phi_h)\circ\chi_h
```

is

```math
-
J_h^{-2}
(\mathcal F_h)_Z^2
A_h
e^{-i\mathcal F_h/h}.
```

All other terms vanish in \(L^2_Y\) under the frame and semiclassical
convergence hypotheses.

Therefore

```math
\boxed{
h^4
\sum_n
n^4|c_n^{(h)}|^2
\longrightarrow
\int
J_0^{-3}
|(\mathcal F_0)_Z|^4
|A_0|^2
\,dZ.
}
```

The power \(J_0^{-3}\) is the product of \(J_0^{-4}\) from two physical
derivatives and \(J_0\) from physical measure.

## 15. Metric nondegeneracy

Assume on a fixed positive critical interval \(\mathcal J\)

```math
\boxed{
\inf_{s\in\mathcal J}
\int
J_0(s,Z)^{-1}
|(\mathcal F_0)_Z(s,Z)A_0(s,Z)|^2
\,dZ
\ge
m_*^2
>
0.
}
```

The fourth limiting moment is finite by the smooth frame contract.

Together with positive zeroth mass, the normalized
Paley--Zygmund/Markov argument applies to the **physical** Fourier
distribution.

Hence fixed positive physical Fourier mass lies in

```math
c_-\le |hn|\le c_+.
```

## 16. Critical selector charge

The physical critical frequency remains

```math
\lambda_p
\asymp
Nh^{-1}
=
N\rho^{1/3}.
```

The finite-band mass and mode count yield one physical Fourier coefficient at
least \(c h^{1/2}\) relative to the carrier scale.

Under the protected reconstruction contract this produces a threshold-
violating LP block throughout the fixed critical interval.

As before,

```math
dt
=
\frac{\rho^{-2/3}}{\nu N^2}\,ds.
```

Therefore

```math
\boxed{
\int_{I_{\rm crit}}
\Lambda(t)^2\,dt
\ge
\frac{c_*}{\nu}.
}
```

The constant depends on the fixed frame/phase bounds but not on \(R\).

## 17. Exact Jacobian equation

Differentiate the characteristic ODE in \(Z\):

```math
\partial_sJ_h
=
h^{-1}\theta_h(s)
(\partial_YB_h)(s,\chi_h)
J_h.
```

Thus

```math
\boxed{
J_h(s,Z)
=
\exp
\left(
h^{-1}
\int_0^s
\theta_h(\sigma)
(\partial_YB_h)
(
\sigma,
\chi_h(\sigma,Z)
)
\,d\sigma
\right).
}
```

This is the first deformation observable.

## 18. Absolute bounded-distortion budget

Taking absolute values gives

```math
|\log J_h(s,Z)|
\le
h^{-1}
\int_0^s
|\theta_h(\sigma)|
\|
\partial_YB_h(\sigma)
\|_\infty
\,d\sigma.
```

Hence

```math
\boxed{
h^{-1}
\int_0^S
|\theta_h|
\|\partial_YB_h\|_\infty
\,ds
\le
C
}
```

implies

```math
e^{-C}
\le
J_h
\le
e^C.
```

To obtain the full \(W^{3,\infty}\) frame contract, it is sufficient to use
the stronger budget

```math
\boxed{
h^{-1}
\int_0^S
|\theta_h(s)|
\|
B_h(s)
\|_{W^{4,\infty}}
\,ds
\le
C_B,
}
```

together with fixed initial geometry.

Standard differentiated flow ODEs and Gronwall then give finite-order
characteristic derivative bounds depending on \(C_B\).

This is an absolute sufficient route.

## 19. Persistent strain scale

Suppose

```math
\|\partial_YB_h(s)\|_\infty
\asymp
1
```

and

```math
|\theta_h(s)|
\asymp
\Theta_h
```

on an order-one critical interval.

The absolute bounded-distortion budget becomes

```math
h^{-1}\Theta_h
=
O(1).
```

Thus a sufficient persistent scale is

```math
\boxed{
\Theta_h
=
O(h)
=
O(\rho^{-1/3}).
}
```

This is two powers wider than the L5-33 residual corridor

```math
O(h^3)
=
O(\rho^{-1}).
```

The \(O(h)\) scale is **not** asserted necessary.

Signed or rapidly oscillating deformation may have smaller accumulated
characteristic strain than the absolute budget predicts.

## 20. Exact exponential-distortion separator

Take

```math
B(Y)=\sin Y,
\qquad
\theta_h(s)=\theta_0>0.
```

At \(Z=0\),

```math
\chi_h(s,0)=0
```

because \(B(0)=0\).

Since

```math
B_Y(0)=1,
```

the Jacobian ODE becomes

```math
\partial_sJ_h(s,0)
=
h^{-1}\theta_0
J_h(s,0),
\qquad
J_h(0,0)=1.
```

Therefore

```math
\boxed{
J_h(s,0)
=
\exp(\theta_0s/h).
}
```

At the opposite fixed point \(Z=\pi\),

```math
J_h(s,\pi)
=
\exp(-\theta_0s/h).
```

Thus order-one nonuniform principal direction strain can generate
exponentially ill-conditioned characteristic geometry during one critical
interval.

This separator proves that bounded deformation is not automatic.

It does **not** prove that such a trajectory has zero or infinite selector
charge.

## 21. Relation to L5-33 and L5-34

The protected direction architecture is now:

### Residual direction defect

L5-33:
under nondegenerate coupling,

```math
\theta_h
=
O(h^3)
```

is required to hide direction leakage in NF4.

### Principal rigid direction motion

L5-34:
no smallness of \(\theta_h\) is required;
translation removes it exactly.

### Principal nonuniform direction motion

L5-35:
bounded smooth characteristic deformation plus nondegenerate Lagrangian
accumulated phase preserves the critical charge theorem.

An absolute sufficient persistent direction-strain scale is \(O(h)\).

These are different classifications and must not be conflated.

## 22. What remains unresolved

The theorem does not derive the frame contract from selected whole-space NSE.

It does not prove that large deformation is charged.

It does not prove that the absolute \(O(h)\) strain scale is necessary.

It does not handle multidimensional frame deformation, vorticity stretching,
or arbitrary packet-direction tensors.

It establishes only that controlled nonuniform one-dimensional direction
deformation is compatible with the protected critical-mixing mechanism.

## 23. Next live obligation: C2-MIX-DIRECTION-STRAIN

The smallest safe successor is:

> Can selected whole-space active-band dynamics force a bounded accumulated
> characteristic-strain budget, or does failure of that budget itself produce
> a selector/dissipation cost?

The first audit should distinguish:

1. absolute strain magnitude;
2. signed/oscillatory accumulated strain along characteristics;
3. Jacobian condition number;
4. deformation-gradient energy.

Do not assume the absolute \(O(h)\) sufficient scale is necessary.

A positive whole-space bridge must derive an invariant frame-deformation
quantity from the actual velocity-gradient dynamics.

## 24. Hard rejection tests

Reject any successor that:

- treats the L5-33 \(h^3\) residual corridor as the principal-frame strain
  threshold;
- assumes a nonlinear characteristic frame preserves Fourier magnitudes;
- ignores the physical measure factor \(J_h\,dZ\);
- omits the \(J_h^{-3}(J_h)_Z\partial_Z\) diffusion term;
- infers bounded deformation merely from bounded direction amplitude;
- calls the absolute \(O(h)\) strain scale necessary;
- interprets exponential frame distortion as proof of selector-charge failure;
- promotes the conditional frame theorem to selected whole-space A2 closure.

## 25. Claim boundary

The protected claim sought from this tranche is exactly

```text
BOUNDED_NONUNIFORM_FRAME_DEFORMATION_PRESERVES_CRITICAL_MIXING
__ABSOLUTE_DIRECTION_STRAIN_BUDGET_IS_H_SCALE.
```

It proves:

- exact characteristic removal of one-dimensional nonuniform principal
  direction transport;
- exact transformed diffusion metric
  \(J^{-2}\partial_Z^2-J^{-3}J_Z\partial_Z\);
- metric-weighted critical damping
  \(-J^{-2}|\mathcal F_Z|^2\);
- strong semiclassical convergence under a smooth bi-Lipschitz frame contract;
- physical scaled second/fourth moment limits with weights
  \(J^{-1}\) and \(J^{-3}\);
- metric nondegeneracy implies positive physical critical-band mass and
  \(c/\nu\) selector charge;
- the absolute characteristic-strain budget
  \(h^{-1}\int|\theta|\|B\|_{W^{4,\infty}}ds=O(1)\)
  is sufficient for bounded finite-order frame geometry;
- persistent order-one direction gradients therefore have a sufficient
  amplitude scale \(O(h)=O(\rho^{-1/3})\);
- order-one nonuniform strain can cause exponential characteristic distortion.

It does not derive the deformation budget from selected whole-space NSE.

It does not prove that excessive deformation is charged.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
