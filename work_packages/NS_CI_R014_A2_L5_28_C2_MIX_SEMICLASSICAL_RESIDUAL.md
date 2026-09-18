# NS-CI-R014-A2-L5-28 — semiclassical bridge residual weakening and NF4 depletion scale

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor:
  `11faa7a2bccbfedba5909e6a8eab2c12e8d6f494`
- Result:
  `SEMICLASSICAL_BRIDGE_RESIDUAL_WEAKENING_PROVED__ABSOLUTE_NF4_DERIVATION_REQUIRES_R_TWO_THIRDS_DEPLETION`
- A2 theorem: open
- L5: active
- C2-MIX-DERIVE: NF4 sharpened
- MATHCERT adjudication: absent
- Evidence class: conditional critical bridge refinement plus exact scaling
  obstruction for absolute whole-space derivation

L5-27 proves a conditional critical packet bridge using an `O(h)`
demodulated residual in a fixed ordinary Sobolev norm.

That residual norm is stronger than the critical Fourier-moment argument
intrinsically requires.

The correct critical norm is semiclassical:

```math
\|f\|_{H_h^2}^2
=
\sum_{j=0}^2
\|(h\partial_Y)^j f\|_2^2.
```

The L5-27 bridge remains valid if its initialization and residual hypotheses are
weakened to `O(h)` in `H_h^2`.

This removes an artificial derivative penalty from the rapid demodulating
phase.  A function oscillating at critical frequency `h^{-1}` has ordinary
derivatives of size `h^{-j}`, but its semiclassical derivatives
`(h\partial_Y)^j` remain order one.

After this weakening, one genuine equation-level requirement remains:

```math
\boxed{
\text{nonprincipal active-band forcing}
=
O(h^2)
\times
\text{generic same-band forcing}.
}
```

Since

```math
h=R^{-1/3},
```

this is the relative depletion factor

```math
\boxed{
h^2
=
R^{-2/3}.
}
```

Protected L5-16 shows that incompressibility, Leray projection, fixed-width
same-band support, and amplitude information alone do not supply any such
factor: the projected interaction can attain the full physical scale
`\lambda A^2`.

Therefore the absolute NF4 derivation route is terminated.

A whole-space bridge must prove genuine dynamic/geometric depletion of the
nonprincipal active interaction, or replace NF4 by a different equation-derived
mechanism.

## 1. Critical normal form from L5-27

Retain the L5-27 normal form

```math
\partial_s\Phi_h
+
i h^{-1}a_h(s)g(Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h
+
r_h.
```

Define

```math
q_h'(s)
=
h^{-1}a_h(s),
\qquad
p_h=hq_h,
\qquad
\Phi_h=e^{-iq_hg}A_h.
```

Then

```math
\boxed{
\partial_sA_h
=
\mathcal L_h A_h
+
\widetilde r_h,
}
```

where

```math
\widetilde r_h=e^{iq_hg}r_h
```

and

```math
\mathcal L_h
=
(h\partial_Y-ip_hg')^2-h^2.
```

Expanding gives the L5-27 equation

```math
\mathcal L_hA
=
h^2A_{YY}
-
2ihp_hg'A_Y
-
ihp_hg''A
-
p_h^2(g')^2A
-
h^2A.
```

## 2. Covariant dissipativity

Set

```math
\mathcal C_h
=
h\partial_Y-ip_hg'.
```

On the periodic line, both terms are skew-adjoint, hence
`\mathcal C_h` is skew-adjoint and

```math
\operatorname{Re}
\langle A,\mathcal C_h^2A\rangle
=
-\|\mathcal C_hA\|_2^2.
```

Therefore

```math
\boxed{
\operatorname{Re}
\langle A,\mathcal L_hA\rangle
=
-\|\mathcal C_hA\|_2^2
-
h^2\|A\|_2^2.
}
```

This is the natural critical energy identity.

It shows why ordinary unscaled derivatives are not the fundamental object.

## 3. Semiclassical initialization and residual contract

Replace L5-27 NF3--NF4 by:

### NF3-sc

```math
\boxed{
\|A_h(0)-A_{\rm in}\|_{H_h^2}
\le
C_{\rm in}h.
}
```

### NF4-sc

```math
\boxed{
\left(
\int_0^{s_1}
\|\widetilde r_h(s)\|_{H_h^2}^2\,ds
\right)^{1/2}
\le
C_rh.
}
```

Retain NF1, NF2, and NF5 from L5-27.

Only two semiclassical derivatives are required because the critical-band
argument uses moments only through order four.

## 4. Semiclassical commutator structure

Let

```math
D_h=h\partial_Y.
```

Then

```math
[D_h,\mathcal C_h]
=
-ihp_hg''.
```

Thus every commutator of one semiclassical derivative with the covariant
critical operator gains one explicit factor `h`.

For fixed smooth `g` and bounded `p_h`,

```math
[D_h,\mathcal L_h]
=
O(h)\mathcal C_h
+
O(h^2)
```

as an energy-form identity with bounded smooth coefficients.

Applying `D_h^j`, for `j=0,1,2`, to the inhomogeneous equation and using
covariant dissipativity gives by induction

```math
\boxed{
\sup_{0\le s\le s_1}
\|A_h(s)\|_{H_h^2}
\le
C.
}
```

The constant is independent of `h`.

## 5. Semiclassical convergence to the critical amplitude

As in L5-27,

```math
A_0(s,Y)
=
A_{\rm in}(Y)
\exp\left(
-\frac{s^3}{3}|g'(Y)|^2
\right).
```

Let

```math
W_h=A_h-A_0.
```

Because `p_h=s+O(h^2)`,

```math
(\mathcal L_h+s^2(g')^2)A_0
=
O(h)
```

in `H_h^2` on every fixed critical window.

Indeed:

- the first-order covariant corrections carry one explicit factor `h`;
- `p_h^2-s^2=O(h^2)`;
- diffusion and the scalar `-h^2` term are `O(h^2)`;
- semiclassical differentiation does not introduce inverse powers of `h`.

Using NF3-sc, NF4-sc, the commutator estimate, and Gronwall gives

```math
\boxed{
\sup_{0\le s\le s_1}
\|A_h(s)-A_0(s)\|_{H_h^2}
\le
Ch.
}
```

This is the bridge convergence actually matched to the critical frequency
scale.

## 6. Scaled Fourier moments still converge

Write

```math
\Phi_h
=
\sum_n c_n^{(h)}e^{inY}.
```

The first derivative identity is

```math
h\partial_Y\Phi_h
=
e^{-iq_hg}
\left(
h\partial_YA_h
-
ip_hg'A_h
\right).
```

The semiclassical convergence gives

```math
h\partial_YA_h
=
O(h)
```

in `L^2`, while
`A_h\to A_0` and `p_h\to s`.

Hence

```math
\boxed{
h^2
\sum_n n^2|c_n^{(h)}|^2
\longrightarrow
s^2\|g'A_0\|_2^2.
}
```

Likewise,

```math
\begin{aligned}
h^2\partial_Y^2\Phi_h
=
e^{-iq_hg}
[
&
h^2A_{YY}
-
2ihp_hg'A_Y
-
ihp_hg''A
\\
&-
p_h^2(g')^2A
].
\end{aligned}
```

Every term except the last tends to zero in `L^2` under the
`H_h^2` convergence.

Therefore

```math
\boxed{
h^4
\sum_n n^4|c_n^{(h)}|^2
\longrightarrow
s^4\|(g')^2A_0\|_2^2.
}
```

The zeroth moment converges as before.

Thus the Paley--Zygmund/Markov critical-band argument of L5-27 is unchanged.

## 7. Semiclassical bridge conclusion

Under NF1, NF2, NF3-sc, NF4-sc, and NF5, the L5-27 conclusion still holds:

```math
\Lambda(t)
\ge
cN R^{1/3}
```

throughout one fixed critical interval and

```math
\boxed{
\int_{I_{\rm crit}}
\Lambda(t)^2\,dt
\ge
\frac{c_*}{\nu}.
}
```

Thus ordinary `H^k` residual regularity is not the material bridge
requirement.

The material requirement is residual **amplitude depletion at critical
scaling**.

## 8. Whole-space active-scale normalization

Consider one upper-band packet at physical frequency scale `N` and amplitude

```math
A
=
R\nu N.
```

Normalize

```math
X=N(x-x_0),
\qquad
u=A U,
\qquad
\tau=AN(t-t_0).
```

The projected NSE has the dimensionless turnover form

```math
\boxed{
\partial_\tau U
+
\mathbb P(U\cdot\nabla_XU)
=
R^{-1}\Delta_XU.
}
```

Set

```math
h=R^{-1/3},
\qquad
s=h\tau.
```

Then

```math
\boxed{
\partial_s U
+
h^{-1}
\mathbb P(U\cdot\nabla_XU)
=
h^2\Delta_XU.
}
```

Therefore a generic order-one same-band nonlinear interaction on turnover
scale becomes order

```math
h^{-1}
```

in critical variables.

## 9. What NF4-sc requires physically

Suppose the leading extracted transverse shear interaction is assigned to the
principal term

```math
i h^{-1}a_hg\,\Phi_h.
```

Let
`\mathcal R_{\rm turn}`
denote the remaining normalized nonprincipal nonlinear interaction before the
critical time rescaling.

Then the critical residual is schematically

```math
r_h
=
h^{-1}
\mathcal R_{\rm turn}.
```

NF4-sc requires

```math
\|r_h\|_{L^2_sH_h^2}
\lesssim
h
```

after the packet demodulation.

Consequently the turnover-normalized nonprincipal interaction must satisfy

```math
\boxed{
\|\mathcal R_{\rm turn}\|_{L^2_sH_h^2}
\lesssim
h^2.
}
```

Relative to the generic order-one turnover nonlinearity, this is the depletion

```math
\boxed{
h^2
=
R^{-2/3}.
}
```

In physical forcing units,

```math
\boxed{
\text{NF4-sc residual scale}
\lesssim
R^{-2/3}A^2N.
}
```

This is the exact bridge cost.

## 10. L5-16 blocks an absolute algebraic derivation

Protected L5-16 constructs a divergence-free same-band Fourier fixture for
which

```math
\boxed{
\|\mathbb P(u\cdot\nabla u)_{\rm target}\|
\asymp
A^2N.
}
```

All interacting frequencies lie in one fixed-width annular cluster, and Leray
projection removes no derivative or overshoot factor.

Thus no estimate using only

- incompressibility;
- Leray projection;
- fixed-width same-band support; and
- an amplitude scale `A`

can produce the required universal factor

```math
R^{-2/3}.
```

The finite-mode fixture also makes clear that passing to the semiclassical norm
does not manufacture amplitude smallness. Critical demodulation may move
frequency to order `h^{-1}`, but `H_h^2` is designed precisely so such
oscillation remains order one rather than order `h^{-2}`.

Therefore

```text
ABSOLUTE SAME-BAND ALGEBRA
        does not imply
NF4-sc.
```

This is a route obstruction, not a whole-space NSE counterexample.

## 11. A2 and Leray scalar budgets do not supply the missing factor pointwise

The A2 hypothesis controls

```math
\int\Lambda(t)^2\,dt.
```

The Leray energy inequality controls total energy and integrated dissipation.

Neither scalar budget contains packet orientation, transverse deformation,
phase alignment, or a pointwise decomposition of the active-band quadratic
interaction into principal and residual pieces.

Protected L5-15 already shows that arbitrarily large overshoot episodes with
turnover-scale duration are compatible with the scalar A2/energy/dissipation
budgets in the route-separation sense.

Therefore the missing
`R^{-2/3}`
factor cannot be obtained by merely combining the absolute same-band estimate
with those scalar budgets.

A successful NF4 derivation must be a genuinely equation-specific dynamic or
geometric depletion theorem.

## 12. Exact status of the derivation problem

After this tranche the NF4 question is no longer obscured by an unnecessarily
strong ordinary Sobolev norm.

The live statement is:

> Can the selected whole-space NSE force the nonprincipal active-packet
> interaction to be smaller than the generic same-band quadratic scale by the
> factor `R^{-2/3}` on a critical interval?

Equivalent admissible formulations include:

- an `R^{-2/3}` relative bound on the demodulated nonprincipal packet
  interaction;
- a geometric depletion theorem that makes the active quadratic interaction
  asymptotically rank-one/shear-like;
- a signed/dynamic cancellation theorem whose critical
  `L^2_sH_h^2` residual is `O(h)`;
- an equation-derived decomposition into several bridge packets whose total
  nonprincipal residual obeys the same critical bound.

## 13. Next live obligation: C2-MIX-DEPLETION

The smallest safe successor is:

> Test whether incompressibility, local strain geometry, pressure cancellation,
> or active-packet polarization can force the required `R^{-2/3}` depletion
> of the nonprincipal interaction.

The first calculation should retain the L5-16 exact projected symbol and ask
which additional geometric invariant would annihilate or suppress it.

Do not repeat an absolute bilinear estimate: that route is closed by L5-16 and
the scaling calculation above.

If every natural geometric projection still permits an order-one normalized
residual, record the exact obstruction and terminate the bridge route rather
than weakening NF4 below what the critical charge proof needs.

## 14. Hard rejection tests

Reject any successor that:

- treats ordinary `H^k` demodulation growth as the material obstruction;
- drops the residual amplitude requirement below what is needed for critical
  moment survival;
- assumes `R^{-2/3}` depletion from A2 alone;
- treats the L5-16 algebraic fixture as a whole-space NSE trajectory;
- applies strict-high smallness at the active shell;
- differentiates the moving selector;
- calls the conditional bridge a proof of A2.

## 15. Claim boundary

The protected claim sought from this tranche is exactly

```text
SEMICLASSICAL_BRIDGE_RESIDUAL_WEAKENING_PROVED
__ABSOLUTE_NF4_DERIVATION_REQUIRES_R_TWO_THIRDS_DEPLETION.
```

It proves:

- ordinary residual `H^k` in L5-27 can be replaced by semiclassical
  `H_h^2`;
- the critical scaled second/fourth moment argument survives this weakening;
- the conditional `c_*/\nu` selector-charge theorem remains valid;
- whole-space critical normalization turns generic same-band forcing into an
  `O(h^{-1})` term;
- NF4-sc therefore requires relative nonprincipal depletion
  `h^2=R^{-2/3}`;
- protected L5-16 excludes obtaining that factor from absolute
  incompressibility/Leray/fixed-band algebra alone.

It does not derive the depletion from selected whole-space NSE.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
