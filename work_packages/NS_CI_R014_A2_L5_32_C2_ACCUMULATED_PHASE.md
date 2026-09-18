# NS-CI-R014-A2-L5-32 — time-dependent transverse profile bridge

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor:
  `93aa46b1a1911793f771212303ddea14e7fff5eb`
- Result:
  `TIME_DEPENDENT_TRANSVERSE_PROFILE_BRIDGE_PROVED__ACCUMULATED_PHASE_GRADIENT_IS_CRITICAL_INVARIANT`
- A2 theorem: open
- L5: active
- C2-MIX-COHERENCE: instantaneous profile freezing no longer required
- MATHCERT adjudication: absent
- Evidence class: conditional critical normal-form theorem;
  not a derivation from selected whole-space NSE

L5-31 treats a fixed finite coherent shear family as one slowly heat-evolving
transverse profile.

The critical phase-mixing proof is more robust than that calibration suggests.

The profile itself does **not** need to stay close to one frozen function.
What enters the exact demodulated equation is its **accumulated transverse
phase**

```math
F_h(s,Y)
=
\int_0^s G_h(\sigma,Y)\,d\sigma.
```

Consider the critical normal form

```math
\partial_s\Phi_h
+
i h^{-1}G_h(s,Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h
+
r_h.
```

If the accumulated phase satisfies

```math
F_h
=
F_0
+
O(h)
```

in a fixed spatial smooth norm, then exact phase removal gives a critical
amplitude limit

```math
\boxed{
A_0(s,Y)
=
\exp\left(
-
\int_0^s
|\partial_YF_0(\sigma,Y)|^2\,d\sigma
\right).
}
```

The scaled Fourier moments are governed by the current accumulated phase
gradient:

```math
h^2
\sum_n n^2|c_n^{(h)}(s)|^2
\longrightarrow
\|\partial_YF_0(s)A_0(s)\|_2^2,
```

and

```math
h^4
\sum_n n^4|c_n^{(h)}(s)|^2
\longrightarrow
\|(\partial_YF_0(s))^2A_0(s)\|_2^2.
```

Thus any fixed positive critical interval on which

```math
\|\partial_YF_0(s)A_0(s)\|_2
\ge
m_*>0
```

has the same positive critical-band mass and the same `c/\nu` selector-charge
mechanism as L5-26--L5-31.

This admits order-one instantaneous profile drift.

For example,

```math
G_h(s,Y)
=
G_0(Y)
+
\sin(s/h)H(Y)
```

has order-one oscillatory drift, but

```math
F_h(s,Y)
=
sG_0(Y)
+
h(1-\cos(s/h))H(Y),
```

so

```math
F_h-sG_0
=
O(h).
```

The oscillatory profile therefore has the same critical accumulated phase
limit as the frozen profile.

The live whole-space obligation is correspondingly weaker and sharper:

> extract a common transverse transport direction whose **accumulated phase
> gradient** is nondegenerate over a critical interval, with all remaining
> errors below the semiclassical residual threshold.

Small instantaneous profile drift is not required.

## 1. Conditional critical equation

Fix

```math
0<s_-<s_+<\infty.
```

For

```math
0<h\le h_0,
```

let `\Phi_h` solve on \([0,s_+]\times\mathbb T\)

```math
\boxed{
\partial_s\Phi_h
+
i h^{-1}G_h(s,Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h
+
r_h.
}
```

Assume `G_h` is real-valued.

Define

```math
F_h(s,Y)
=
\int_0^sG_h(\sigma,Y)\,d\sigma.
```

No smallness of `G_h-G_h(0)` is assumed.

## 2. Accumulated-phase hypotheses

Assume there exists a real limit phase

```math
F_0
\in
C([0,s_+];W^{4,\infty}(\mathbb T))
```

with

```math
F_0(0,\cdot)=0
```

such that

```math
\boxed{
\sup_{0\le s\le s_+}
\|F_h(s)-F_0(s)\|_{W^{4,\infty}}
\le
C_F h.
}
```

Also assume

```math
\sup_{0\le s\le s_+}
\|F_h(s)\|_{W^{4,\infty}}
\le
C_F.
```

These are accumulated-phase conditions.

They do not require pointwise or strong convergence of the instantaneous
profiles `G_h`.

## 3. Semiclassical initialization and residual

Use the L5-28 semiclassical norm

```math
\|f\|_{H_h^2}^2
=
\sum_{j=0}^2
\|(h\partial_Y)^jf\|_2^2.
```

Assume the carrier starts from the constant profile up to

```math
\boxed{
\|\Phi_h(0)-1\|_{H_h^2}
\le
C_{\rm in}h.
}
```

Since `F_h(0)=0`, no initial phase correction is needed.

Define the demodulated residual

```math
\widetilde r_h
=
e^{iF_h/h}r_h.
```

Assume

```math
\boxed{
\left(
\int_0^{s_+}
\|\widetilde r_h(s)\|_{H_h^2}^2\,ds
\right)^{1/2}
\le
C_rh.
}
```

This is exactly the L5-28 residual size.

## 4. Exact time-dependent phase removal

Set

```math
\boxed{
\Phi_h
=
e^{-iF_h/h}A_h.
}
```

Because

```math
\partial_sF_h=G_h,
```

the entire fast potential cancels exactly.

A direct differentiation gives

```math
\boxed{
\begin{aligned}
\partial_sA_h
={}&
h^2\partial_Y^2A_h
-
2ih(F_h)_Y\partial_YA_h
-
ih(F_h)_{YY}A_h
\\
&-
|(F_h)_Y|^2A_h
-
h^2A_h
+
\widetilde r_h.
\end{aligned}
}
```

The instantaneous profile `G_h` no longer appears.

Only its accumulated phase `F_h` remains.

## 5. Covariant form

Define

```math
\mathcal C_h(s)
=
h\partial_Y
-
i(F_h)_Y(s,Y).
```

Then

```math
\boxed{
\partial_sA_h
=
\left(
\mathcal C_h(s)^2-h^2
\right)A_h
+
\widetilde r_h.
}
```

For each fixed `s`, `\mathcal C_h(s)` is skew-adjoint.

Therefore

```math
\boxed{
\operatorname{Re}
\langle A_h,
(\mathcal C_h^2-h^2)A_h
\rangle
=
-\|\mathcal C_hA_h\|_2^2
-
h^2\|A_h\|_2^2.
}
```

No derivative of `G_h` in critical time is required for this energy identity.

## 6. Semiclassical commutators

Let

```math
D_h=h\partial_Y.
```

Then

```math
[D_h,\mathcal C_h]
=
-ih(F_h)_{YY}.
```

Hence every spatial commutator gains one explicit factor `h`.

The uniform `W^{4,\infty}` bound on `F_h` gives, for `j=0,1,2`,

```math
\boxed{
\sup_{0\le s\le s_+}
\|D_h^jA_h(s)\|_2
\le
C.
}
```

The constant depends on the fixed accumulated-phase bounds and residual
constant but not on `h`.

Thus

```math
\sup_s
\|A_h(s)\|_{H_h^2}
\le
C.
```

## 7. Critical amplitude limit

Define

```math
\boxed{
A_0(s,Y)
=
\exp\left(
-
\int_0^s
|(F_0)_Y(\sigma,Y)|^2
\,d\sigma
\right).
}
```

Then

```math
\partial_sA_0
=
-|(F_0)_Y(s,Y)|^2A_0,
\qquad
A_0(0)=1.
```

Since `F_0` is bounded in `W^{4,\infty}`,

```math
A_0
```

is smooth and strictly positive on the fixed interval.

## 8. Strong semiclassical convergence

Set

```math
W_h=A_h-A_0.
```

The defect obtained by inserting `A_0` into the `A_h` equation is

```math
\begin{aligned}
\mathcal E_h
={}&
h^2(A_0)_{YY}
-
2ih(F_h)_Y(A_0)_Y
-
ih(F_h)_{YY}A_0
\\
&-
\left(
|(F_h)_Y|^2
-
|(F_0)_Y|^2
\right)A_0
-
h^2A_0.
\end{aligned}
```

The accumulated-phase hypothesis gives

```math
\boxed{
\sup_s
\|\mathcal E_h(s)\|_{H_h^2}
\le
Ch.
}
```

Indeed:

- every explicit first-order term carries `h`;
- the diffusion and scalar terms carry `h^2`;
- the squared-gradient coefficient difference is `O(h)`;
- semiclassical differentiation introduces no inverse powers of `h`.

Using the covariant energy estimate, the initialization hypothesis, and the
L5-28 residual bound gives

```math
\boxed{
\sup_{0\le s\le s_+}
\|A_h(s)-A_0(s)\|_{H_h^2}
\le
Ch.
}
```

## 9. Zeroth Fourier moment

Write

```math
\Phi_h(s,Y)
=
\sum_{n\in\mathbb Z}
c_n^{(h)}(s)e^{inY}.
```

Phase multiplication preserves `L^2`, so

```math
\sum_n
|c_n^{(h)}(s)|^2
=
\|A_h(s)\|_2^2.
```

Therefore

```math
\boxed{
\sum_n
|c_n^{(h)}(s)|^2
\longrightarrow
\|A_0(s)\|_2^2.
}
```

On the compact interval \([s_-,s_+]\), the limiting mass is uniformly
positive.

## 10. Scaled second Fourier moment

Differentiate the exact phase representation:

```math
h\partial_Y\Phi_h
=
e^{-iF_h/h}
\left(
h\partial_YA_h
-
i(F_h)_YA_h
\right).
```

The strong `H_h^2` convergence gives

```math
h\partial_YA_h
\longrightarrow
0
```

in `L^2`.

The accumulated-phase convergence gives

```math
(F_h)_YA_h
\longrightarrow
(F_0)_YA_0.
```

Hence

```math
\boxed{
h^2
\sum_n
n^2|c_n^{(h)}(s)|^2
\longrightarrow
\|(F_0)_Y(s)A_0(s)\|_2^2
}
```

uniformly on the fixed interval.

This is the decisive critical observable.

## 11. Scaled fourth Fourier moment

A second differentiation gives

```math
\begin{aligned}
h^2\partial_Y^2\Phi_h
=
e^{-iF_h/h}
[
&
h^2(A_h)_{YY}
-
2ih(F_h)_Y(A_h)_Y
\\
&-
ih(F_h)_{YY}A_h
-
(F_h)_Y^2A_h
].
\end{aligned}
```

The first three terms vanish in `L^2` as `h\to0`.

Therefore

```math
\boxed{
h^4
\sum_n
n^4|c_n^{(h)}(s)|^2
\longrightarrow
\|(F_0)_Y(s)^2A_0(s)\|_2^2
}
```

uniformly on the fixed interval.

The fourth scaled moment is uniformly finite.

## 12. Accumulated-phase nondegeneracy

Assume there exists

```math
m_*>0
```

such that

```math
\boxed{
\inf_{s_-\le s\le s_+}
\|(F_0)_Y(s)A_0(s)\|_2
\ge
m_*.
}
```

Because `A_0>0`, this is equivalent to requiring genuine accumulated
transverse phase variation throughout the chosen interval.

It does not require the instantaneous profile `G_h(s)` to be close to a
fixed function.

## 13. Positive critical-band mass

The zeroth mass is uniformly positive.

The scaled second moment is uniformly bounded below by `m_*^2`.

The scaled fourth moment is uniformly finite.

Therefore the same normalized Paley--Zygmund plus Markov argument used in
L5-26--L5-31 gives constants

```math
0<c_-<c_+<\infty,
\qquad
\eta_*>0,
```

such that, for sufficiently small `h`,

```math
\boxed{
\sum_{c_-\le|hn|\le c_+}
|c_n^{(h)}(s)|^2
\ge
\eta_*
}
```

uniformly for

```math
s\in[s_-,s_+].
```

Thus order-one profile drift does not destroy critical mixing when the
accumulated phase is coherent.

## 14. One critical coefficient

The band

```math
c_-\le|hn|\le c_+
```

contains `O(h^{-1})` integer frequencies.

Hence at each critical time there is at least one coefficient satisfying

```math
\boxed{
|c_n^{(h)}(s)|
\ge
c h^{1/2}.
}
```

As before, finite Littlewood--Paley overlap converts this to one physical block
once the packet reconstruction contract is supplied.

## 15. Physical selector charge

Suppose the normal form is reconstructed from one coherent transport channel
with effective Reynolds parameter

```math
\rho
\to
\infty,
\qquad
h=\rho^{-1/3},
```

base frequency `N`, and carrier amplitude `A=R\nu N`, with

```math
0<\rho\le R.
```

Then the critical block frequency is

```math
\lambda_p
\asymp
Nh^{-1}
=
N\rho^{1/3}.
```

Its physical amplitude is at least

```math
cAh^{1/2}.
```

Therefore

```math
\lambda_p^{-1}\|u_p\|_\infty
\ge
c\nu
\frac{R}{\sqrt\rho}
\ge
c\nu\sqrt R.
```

For large `R` this violates the fixed campaign threshold.

The critical physical time element is

```math
dt
=
\frac{\rho^{-2/3}}{\nu N^2}\,ds.
```

Hence

```math
\boxed{
\int_{I_{\rm crit}}
\Lambda(t)^2\,dt
\ge
\frac{c_*}{\nu}.
}
```

The constant depends on the fixed accumulated-phase nondegeneracy and
reconstruction constants, not on `R`.

## 16. Order-one instantaneous profile drift is admissible

Take fixed smooth real profiles `G_0,H` and set

```math
G_h(s,Y)
=
G_0(Y)
+
\sin(s/h)H(Y).
```

Then

```math
\|G_h(s)-G_0\|_{W^{4,\infty}}
```

is generally order one.

But

```math
\begin{aligned}
F_h(s,Y)
&=
\int_0^sG_h(\sigma,Y)\,d\sigma
\\
&=
sG_0(Y)
+
h(1-\cos(s/h))H(Y).
\end{aligned}
```

Thus

```math
\boxed{
\sup_s
\|F_h(s)-sG_0\|_{W^{4,\infty}}
\le
2h\|H\|_{W^{4,\infty}}.
}
```

The critical theorem therefore sees the same limiting phase as the frozen
profile `G_0`.

This example proves that small instantaneous profile drift is not the correct
coherence requirement.

## 17. Relation to L5-31

L5-31 has

```math
G_h(s)
=
e^{h^2s\partial_Y^2}G,
```

so

```math
G_h
=
G+O(h^2).
```

Its accumulated phase is

```math
F_h(s)
=
sG+O(h^2).
```

Thus L5-31 is a strict special case of the present bridge.

The present tranche removes profile freezing from the protected mechanism.

## 18. What remains unresolved

The theorem still assumes:

- one common transport direction;
- one common transverse coordinate;
- an accumulated phase compactness law
  `F_h=F_0+O(h)`;
- nondegeneracy of `(F_0)_Y` on the critical interval;
- the L5-28 small semiclassical residual;
- physical reconstruction into LP blocks.

None of these is derived here from an arbitrary selected whole-space
upper-band overshoot.

In particular, changing transport direction cannot be encoded by a scalar
phase `F_h(s,Y)` in one transverse coordinate.

## 19. Next live obligation: C2-MIX-DIRECTION

The smallest safe successor is now:

> Can selected whole-space active-band dynamics provide one approximately
> common transport direction and transverse coordinate over the critical
> interval, or must order-one direction drift itself generate a non-summable
> selector/dissipation cost?

Do not require the instantaneous transverse profile to remain frozen.
L5-32 shows that requirement is unnecessary.

The first audit should therefore separate:

1. scalar profile drift within a fixed transport direction, now allowed through
   accumulated-phase control;
2. actual rotation/change of transport direction, which is not removed by the
   scalar phase transform.

A positive theorem should express direction coherence in a coordinate-free
projected symbol or moving-frame formulation.

## 20. Hard rejection tests

Reject any successor that:

- treats `G_h-G_0=O(h)` pointwise as necessary;
- differentiates `G_h` in critical time merely to control the phase;
- discards order-one fast oscillatory profile drift when its accumulated phase
  is only `O(h)`;
- assumes a common transport direction without stating it;
- promotes this conditional bridge to selected whole-space A2 closure;
- weakens the L5-28 residual amplitude requirement;
- sums overlapping selector charges without a valid ledger.

## 21. Claim boundary

The protected claim sought from this tranche is exactly

```text
TIME_DEPENDENT_TRANSVERSE_PROFILE_BRIDGE_PROVED
__ACCUMULATED_PHASE_GRADIENT_IS_CRITICAL_INVARIANT.
```

It proves:

- exact fast-phase removal for arbitrary real time-dependent transverse
  profiles;
- the demodulated equation depends only on accumulated phase `F_h`;
- `O(h)` convergence of `F_h` in fixed spatial smooth norm, together with
  the L5-28 residual contract, gives `O(h)` semiclassical convergence;
- scaled second/fourth Fourier moments are controlled by
  `(F_0)_Y A_0` and `(F_0)_Y^2A_0`;
- nondegenerate accumulated phase produces positive critical-band mass and a
  `c/\nu` selector charge;
- order-one instantaneous profile drift can be admissible.

It does not derive a common transport direction or accumulated-phase
compactness from selected whole-space NSE.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
