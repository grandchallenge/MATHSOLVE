# NS-CI-R014-A2-L5-33 — transverse direction-defect scaling audit

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor:
  `b4456f7f399c27c4118f0828d2c3659e06e44199`
- Result:
  `TRANSVERSE_DIRECTION_DEFECT_AS_RESIDUAL_REQUIRES_H_CUBED__LARGER_DEFECT_MUST_BE_PROMOTED_OR_CHARGED`
- A2 theorem: open
- L5: active
- C2-MIX-DIRECTION: residual route quantified
- MATHCERT adjudication: absent
- Evidence class: conditional critical normal-form scaling theorem;
  not a selected whole-space NSE direction-coherence theorem

L5-32 removes small instantaneous **profile** drift as a necessary condition.
A scalar time-dependent transverse profile can be absorbed by exact
accumulated-phase removal.

A change of **transport direction** is different.

In a local packet normal form, the first effect of a direction defect is a
transverse derivative leakage.  The model term has the critical form

```math
\mathcal D_h\Phi_h
=
h^{-1}
\theta_h(s)
B_h(s,Y)
\partial_Y\Phi_h.
```

Here:

- `\theta_h` is the dimensionless direction defect;
- `B_h` is an order-one smooth coupling profile;
- `\partial_Y` differentiates across the transverse coordinate of the
  L5-32 phase-mixing packet.

This tranche does **not** claim that every whole-space direction error reduces
exactly to this scalar model.

It asks a narrower question:

> if such a transverse derivative term is present, how small must it be before
> it can honestly be hidden inside the protected L5-28/L5-32 residual?

The answer is one power stronger than a pre-mixing estimate might suggest.

On the L5-32 critical band,

```math
\partial_Y\Phi_h
\sim
h^{-1}\Phi_h.
```

After exact phase removal,

```math
e^{iF_h/h}
\partial_Y\Phi_h
=
\partial_YA_h
-
ih^{-1}(F_h)_YA_h.
```

Therefore the direction-defect term has leading demodulated size

```math
\boxed{
\widetilde{\mathcal D}_h
\sim
-i
\theta_h
h^{-2}
B_h
(F_h)_Y
A_h.
}
```

If the direction coupling is nondegenerate on the critical interval, the
protected NF4 residual requirement

```math
\|\widetilde r_h\|_{L^2_sH_h^2}
=
O(h)
```

forces

```math
\boxed{
\|\theta_h\|_{L^2_s}
=
O(h^3).
}
```

Since

```math
h=\rho^{-1/3},
```

this is

```math
\boxed{
\|\theta_h\|_{L^2_s}
=
O(\rho^{-1}).
}
```

For a direction defect that persists at roughly constant size over one fixed
critical interval, the pointwise scale is therefore

```math
|\theta_h|
\lesssim
h^3
=
\rho^{-1}.
```

A larger direction defect cannot be classified as the protected small
residual.

It must instead be:

1. promoted into the principal critical dynamics;
2. shown to cancel through additional structure; or
3. converted into a selector/dissipation charge.

This tranche proves only the residual exclusion.

It does not yet prove that larger direction drift pays a charge.

## 1. Protected accumulated-phase input

Retain the L5-32 equation

```math
\partial_s\Phi_h
+
ih^{-1}G_h(s,Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h
+
r_h.
```

Define

```math
F_h(s,Y)
=
\int_0^s
G_h(\sigma,Y)\,d\sigma.
```

Assume the L5-32 accumulated-phase hypotheses and write

```math
\Phi_h
=
e^{-iF_h/h}A_h.
```

Then, on a fixed critical interval `J=[s_-,s_+]`,

```math
A_h
\to
A_0
```

in `H_h^2`, and

```math
h\partial_YA_h
\to
0.
```

Also

```math
(F_h)_YA_h
\to
(F_0)_YA_0
```

strongly in `L^2`.

## 2. Direction-defect normal-form term

Add one transverse derivative leakage term

```math
\boxed{
\mathcal D_h\Phi_h
=
h^{-1}
\theta_h(s)
B_h(s,Y)
\partial_Y\Phi_h.
}
```

Assume:

- `B_h` is uniformly bounded in `L^\infty_sW^{2,\infty}_Y`;
- `B_h\to B_0` uniformly on the fixed critical interval;
- `\theta_h` is scalar and measurable in critical time.

No sign of `\theta_h` is assumed.

The model is deliberately minimal.

It isolates only the transverse derivative leakage associated with failure of
one fixed transport direction.

## 3. Exact demodulation of the direction term

Because

```math
\Phi_h
=
e^{-iF_h/h}A_h,
```

one has

```math
\partial_Y\Phi_h
=
e^{-iF_h/h}
\left(
\partial_YA_h
-
ih^{-1}(F_h)_YA_h
\right).
```

Hence the demodulated direction term is exactly

```math
\boxed{
\widetilde{\mathcal D}_h
=
h^{-1}
\theta_hB_h\partial_YA_h
-
i
h^{-2}
\theta_h
B_h(F_h)_YA_h.
}
```

The first term is not the leading critical contribution.

Multiply by `h^2`:

```math
\boxed{
h^2
\theta_h^{-1}
\widetilde{\mathcal D}_h
=
hB_h\partial_YA_h
-
i
B_h(F_h)_YA_h
}
```

wherever `\theta_h\ne0`.

The bracket has a nonzero limit whenever the direction coupling is
nondegenerate.

## 4. Critical coupling observable

Define

```math
\boxed{
C_0(s,Y)
=
B_0(s,Y)
(F_0)_Y(s,Y)
A_0(s,Y).
}
```

Assume the coupling is nontrivial on the fixed critical interval:

```math
\boxed{
\|C_0\|_{L^2(J\times\mathbb T)}
>
0.
}
```

For a uniform persistent-coupling statement, one may use the stronger
condition

```math
\inf_{s\in J}
\|C_0(s)\|_2
\ge
c_{\rm dir}>0.
```

The theorem below first uses only the integrated nondegeneracy.

## 5. Leading-order direction residual

L5-32 gives

```math
h\partial_YA_h
\to
0
```

in `L^2` and

```math
B_h(F_h)_YA_h
\to
C_0.
```

Therefore

```math
\boxed{
h^2
\theta_h^{-1}
\widetilde{\mathcal D}_h
\to
-iC_0
}
```

in the sense of the coefficient multiplying `\theta_h`.

Equivalently, if

```math
Z_h
=
hB_h\partial_YA_h
-
iB_h(F_h)_YA_h,
```

then

```math
Z_h
\to
-iC_0
```

strongly in `L^2(J\times\mathbb T)`, and

```math
\boxed{
\widetilde{\mathcal D}_h
=
h^{-2}
\theta_h Z_h.
}
```

Thus the exact critical amplification of direction leakage is `h^{-2}`.

## 6. Weighted necessary condition for NF4 admission

The protected L5-28/L5-32 residual contract implies in particular

```math
\|\widetilde r_h\|_{L^2_sL^2_Y}
\le
Ch.
```

If the direction term is assigned to that residual, it must satisfy

```math
\|\widetilde{\mathcal D}_h\|_{L^2_sL^2_Y}
\le
Ch.
```

Using

```math
\widetilde{\mathcal D}_h
=
h^{-2}\theta_hZ_h,
```

this is

```math
\boxed{
\|\theta_hZ_h\|_{L^2(J\times\mathbb T)}
\le
Ch^3.
}
```

Since

```math
Z_h\to-iC_0,
```

the intrinsic necessary condition is

```math
\boxed{
\|\theta_h C_0\|_{L^2(J\times\mathbb T)}
=
O(h^3)
}
```

up to the vanishing strong-convergence error.

This weighted form is the exact statement.

## 7. Uniformly nondegenerate direction coupling

Assume the stronger pointwise-in-time lower bound

```math
\|C_0(s)\|_2
\ge
c_{\rm dir}>0
```

throughout `J`.

If `\theta_h` depends only on critical time, then

```math
\|\theta_hC_0\|_{L^2_{s,Y}}
\ge
c_{\rm dir}
\|\theta_h\|_{L^2(J)}.
```

Hence NF4 admission forces

```math
\boxed{
\|\theta_h\|_{L^2(J)}
\le
C h^3.
}
```

This is the clean direction-coherence corridor.

## 8. Persistent direction defect

Suppose the defect has comparable magnitude over a fixed positive fraction of
the critical interval:

```math
|\theta_h(s)|
\ge
\theta_*
```

on a set of critical-time measure at least `c_J>0`.

Then

```math
\|\theta_h\|_{L^2(J)}
\ge
c_J^{1/2}\theta_*.
```

Therefore residual admission requires

```math
\boxed{
\theta_*
\lesssim
h^3.
}
```

A direction error larger than `h^3` that persists for order-one critical
time cannot be hidden in the L5-28 residual.

## 9. Effective-Reynolds form

For the critical mixing parameter

```math
h
=
\rho^{-1/3},
```

one has

```math
h^3
=
\rho^{-1}.
```

Thus

```math
\boxed{
\|\theta_h\|_{L^2(J)}
=
O(\rho^{-1})
}
```

under uniform nondegenerate coupling.

For a persistent approximately constant defect,

```math
\boxed{
|\theta_h|
\lesssim
\rho^{-1}.
}
```

This is much smaller than an order-one angular uncertainty.

## 10. Why the extra power appears

Before critical phase mixing, the direction term carries one explicit
critical factor

```math
h^{-1}.
```

After phase mixing has created transverse frequency

```math
|n|
\asymp
h^{-1},
```

the derivative itself contributes another

```math
h^{-1}.
```

Thus the direction defect appears at scale

```math
\theta_hh^{-2}.
```

The protected residual scale is `h`.

Balancing gives

```math
\theta_hh^{-2}
\sim
h,
```

hence

```math
\boxed{
\theta_h
\sim
h^3.
}
```

This is not an arbitrary bookkeeping choice; it is the post-mixing derivative
amplification.

## 11. Accumulated profile drift and direction drift are distinct

L5-32 permits

```math
G_h
=
G_0
+
O(1)
```

instantaneously when the accumulated scalar phase error is only `O(h)`.

That mechanism does not remove

```math
\theta_hB_h\partial_Y.
```

The latter is a differential operator, not a scalar potential.

A scalar phase gauge can cancel

```math
ih^{-1}G_h
```

but cannot in general cancel a transverse derivative operator.

Therefore profile coherence and direction coherence are genuinely different
obligations.

## 12. Constant spatial rotations do not select a direction

The Navier--Stokes equations and the scalar shell norms used by the campaign
are invariant under one fixed orthogonal spatial rotation.

Thus a constant rotation of any calibration preserves:

- energy;
- dissipation;
- frequency magnitudes;
- threshold ratios;
- A2-type scalar selector charge.

This elementary symmetry confirms that scalar shell data do not contain a
preferred absolute transport direction.

The present theorem does not use this as a time-dependent trajectory
construction.

It only records why direction coherence must come from relational packet
geometry/dynamics, not from scalar shell data.

## 13. What this tranche does not prove

It does not prove:

- that selected whole-space NSE admits the displayed direction-defect normal
  form;
- that every direction change has nondegenerate coupling `C_0`;
- that a defect larger than `h^3` necessarily produces selector charge;
- that direction drift is dynamically persistent;
- that an order-one direction change is impossible.

It proves only that a nondegenerately coupled direction defect cannot be
classified as the protected small residual unless it satisfies the
`h^3` corridor.

## 14. Consequence for the bridge architecture

The bridge now has a clean trichotomy.

### Scalar transverse-profile variation

Handled by L5-32 through accumulated phase.

### Tiny direction leakage

May be assigned to the L5-28 residual only at the weighted scale

```math
O(h^3).
```

### Larger direction leakage

Must be promoted into principal dynamics or independently charged.

This prevents the whole-space derivation from silently hiding transport
rotation inside NF4.

## 15. Next live obligation: C2-MIX-DIRECTION-PRINCIPAL

The smallest safe successor is:

> What happens when the direction defect is larger than the
> `h^3=\rho^{-1}` residual corridor?

Two routes remain admissible:

1. **moving-frame principal dynamics**:
   incorporate transport-direction motion into the principal critical
   operator and test whether a generalized phase/characteristic transform
   preserves positive critical Fourier variance;

2. **direction-drift charge**:
   prove that persistent nonresidual direction motion itself generates
   selector growth or dissipation with a non-summable cost.

The first audit should not assume the moving direction can be represented by a
scalar phase.

## 16. Hard rejection tests

Reject any successor that:

- hides an `O(h^2)` or order-one direction defect inside NF4 after critical
  mixing;
- confuses scalar accumulated-profile drift with derivative direction drift;
- assumes nondegenerate direction coupling without stating it;
- treats constant rotational symmetry as a time-dependent NSE trajectory;
- claims that larger direction drift is already charged;
- uses shell energy to infer a preferred direction;
- promotes the conditional normal-form calculation to A2 closure.

## 17. Claim boundary

The protected claim sought from this tranche is exactly

```text
TRANSVERSE_DIRECTION_DEFECT_AS_RESIDUAL_REQUIRES_H_CUBED
__LARGER_DEFECT_MUST_BE_PROMOTED_OR_CHARGED.
```

It proves:

- exact demodulation of a transverse derivative direction-defect term;
- post-mixing amplification from `h^{-1}` to `h^{-2}`;
- the weighted NF4 necessity
  `\|\theta_hC_0\|_{L^2}=O(h^3)`;
- under uniform nondegenerate coupling,
  `\|\theta_h\|_{L^2}=O(h^3)`;
- for persistent defects, the direction corridor is
  `|\theta_h|\lesssim h^3=\rho^{-1}`;
- scalar accumulated-phase coherence does not remove derivative direction
  leakage.

It does not prove the larger-defect principal dynamics or charge theorem.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
