# NS-CI-R014-A2-L5-39 — C2 direction occupation calibration

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Dependency: protected L5-38 merge
  `866612322207cb9e25530215bbfc064dd865ee60`
- Dependency status: protected and fresh protected-main Solve/GCL/CodeQL replay succeeded.
- Result class: bounded exact calibration
- Result:
  `UNIFORM_PATHWISE_DIRECTION_STRAIN_NOT_CONTROLLED_BY_SCALAR_A2_LERAY_BUDGETS__PACKET_OCCUPATION_OR_NONDEGENERACY_REQUIRED`
- A2 theorem: open
- L5: active
- L3/L4: closed
- MATHCERT adjudication: absent

L5-38 proved that A2 plus Leray controls far-low raw Eulerian jets and that

```math
|b|^2 |\nabla(b/|b|)|^2 \le |\nabla b|^2
```

on `{b\ne0}`.  The unresolved question is whether equation dynamics can turn
that amplitude-weighted Eulerian information into the unweighted pathwise
direction-strain cocycle required by L5-37.

This tranche gives an exact dynamic separator for any **uniform all-streamline**
bridge based only on scalar shell-supremum, A2-occupancy, energy, and
dissipation budgets.

## 1. Exact elliptically polarized shear

Work on the periodic three-torus only as a mechanism calibration.  Let

```math
k\in\mathbb N,
\qquad
0<\varepsilon\le1,
\qquad
a(t)=A_0 e^{-\nu k^2 t},
```

and define

```math
u_{k,\varepsilon}(t,x,y,z)
=
a(t)
\bigl(
0,
\varepsilon\cos(kx),
\sin(kx)
\bigr).
```

Then

```math
\nabla\cdot u_{k,\varepsilon}=0.
```

Moreover `u_x=0` and the field depends only on `x`, so

```math
(u\cdot\nabla)u
=
u_y\partial_yu+u_z\partial_zu
=
0.
```

Since

```math
\Delta u_{k,\varepsilon}=-k^2u_{k,\varepsilon},
\qquad
\partial_tu_{k,\varepsilon}=-\nu k^2u_{k,\varepsilon},
```

the field is an exact smooth unforced periodic Navier--Stokes solution with
constant pressure.

This is not a whole-space finite-energy solution and is not an A2
counterexample.  It is an exact equation-level calibration of the proposed
local bridge.

## 2. Scalar budgets are uniform in the ellipticity parameter

For `0<\varepsilon\le1`,

```math
\|u_{k,\varepsilon}(t)\|_\infty
=
a(t).
```

Thus the annular supremum does not deteriorate as `\varepsilon\downarrow0`.

With normalized torus volume,

```math
\|u_{k,\varepsilon}(t)\|_2^2
=
\frac{a(t)^2}{2}(1+\varepsilon^2),
```

and

```math
\|\nabla u_{k,\varepsilon}(t)\|_2^2
=
\frac{a(t)^2k^2}{2}(1+\varepsilon^2).
```

Hence the kinetic-energy and Leray-dissipation budgets remain bounded above
and below, up to fixed constants, uniformly in `\varepsilon`.

On any interval of parabolic length

```math
|I|=\frac{c}{\nu k^2},
```

a one-annulus threshold calibration with `\Lambda\simeq k` has

```math
\int_I \Lambda(t)^2\,dt
\simeq
\frac{c}{\nu},
```

again independent of `\varepsilon`, provided `A_0` is chosen so that the
annular threshold remains active on `I`.  Fixed Littlewood--Paley overlap
constants do not affect the separator.

## 3. An invariant low-amplitude streamline

Because `u_x=0`, every plane `x=x_0` is invariant under the flow.  In
particular, a trajectory launched at `x=0` satisfies

```math
x(t)\equiv0.
```

Along that trajectory,

```math
u(t,X(t))
=
a(t)(0,\varepsilon,0),
```

so its amplitude is the fraction `\varepsilon` of the annular supremum for
the entire interval.

Let

```math
e_{k,\varepsilon}
=
\frac{u_{k,\varepsilon}}{|u_{k,\varepsilon}|}.
```

At `x=0`,

```math
e_{k,\varepsilon}=(0,1,0),
\qquad
\partial_xe_{k,\varepsilon}
=
\left(0,0,\frac{k}{\varepsilon}\right).
```

Therefore

```math
\boxed{
|\nabla e_{k,\varepsilon}(t,X(t))|
=
\frac{k}{\varepsilon}.
}
```

The normalized direction field is time-independent because the common heat
amplitude cancels.

Consequently,

```math
\boxed{
\int_I
|\nabla e_{k,\varepsilon}(t,X(t))|
\,dt
=
\frac{k|I|}{\varepsilon}
=
\frac{c}{\nu k\varepsilon}.
}
```

For fixed `k,\nu,c`, this diverges as `\varepsilon\downarrow0` while all
scalar budgets in Section 2 stay uniformly bounded.

## 4. The amplitude-weighted estimate is exactly saturated

At the same invariant streamline,

```math
|u|^2
|\partial_x e|^2
=
a(t)^2\varepsilon^2
\frac{k^2}{\varepsilon^2}
=
a(t)^2k^2.
```

But

```math
\partial_xu(t,0,y,z)
=
a(t)(0,0,k),
```

so

```math
\boxed{
|u|^2|\partial_xe|^2
=
|\partial_xu|^2
}
```

there.  The L5-38 amplitude-weighted inequality is therefore not loose in the
relevant limit.  The missing information is genuinely the conversion from
amplitude-weighted spatial control to unweighted pathwise control.

## 5. What the calibration rejects

No estimate obtained only from the **coarse campaign budget envelopes**

```text
annular-supremum bound
+ Lambda L2 occupancy bound
+ kinetic-energy bound
+ Leray-dissipation bound
```

can yield an epsilon-independent uniform all-streamline direction-strain
constant for this family.  All of those inequalities admit constants uniform
in epsilon, while the pathwise strain diverges like 1/epsilon.

This statement is intentionally narrower than a claim about every possible
scalar diagnostic.  For example, sufficiently precise polarization-sensitive
ratios of exact scalar observables could themselves encode epsilon.  The
calibration rejects derivations from the **existing coarse A2/Leray budgets**,
not such augmented information.

The reason is structural:

```text
annular supremum:          independent of epsilon
energy/dissipation:        independent of epsilon up to fixed factors
A2 occupancy:              independent of epsilon
streamline amplitude:      proportional to epsilon
normalized direction jet:  proportional to 1/epsilon.
```

This rejects a **uniform all-streamline bridge derived only from the existing
coarse scalar budget envelopes**.  It does not reject a polarization-sensitive
diagnostic, packet-weighted, almost-everywhere, mass-selected, or whole-space
bridge using additional PDE structure.

## 6. Surviving occupation interface

Any viable successor must insert information that the calibration removes.
Natural admissible interfaces are:

1. packet-weighted occupation excluding trajectories carrying vanishing
   selected amplitude;
2. a quantitative lower-tail estimate for
   `|b(t,X(t))|/\|b(t)\|_\infty`;
3. an averaged frame theorem that needs cocycle control only on the packet mass
   entering the L5-35 observable, rather than uniformly on all labels;
4. a whole-space equation mechanism coupling top-band concentration to
   streamline residence or nondegeneracy.

A minimal pathwise factorization is

```math
|\nabla e|
\le
\frac{|\nabla b|}{|b|}.
```

Thus any pointwise/pathwise route must account for both the raw-jet trace and
the reciprocal-amplitude occupation.  L5-38 controls the far-low raw jets but
does not provide either missing top-band trace or reciprocal-amplitude bound.

## 7. Hard rejection tests

Reject any successor that:

- infers a pointwise lower bound on `|b|` from a shell supremum;
- treats the periodic calibration as a whole-space A2 counterexample;
- assumes the L5-38 weighted estimate already implies an unweighted cocycle;
- uses `\Lambda\in L^2_t` or coarse energy/dissipation envelopes as a bound
  on reciprocal streamline amplitude;
- differentiates the moving selector;
- requires uniform control of all streamlines if only packet-mass control is
  actually needed;
- reopens L3 or L4 without a new non-summable dynamic budget.

## 8. Claim boundary

The proposed bounded result is exactly

```text
UNIFORM_PATHWISE_DIRECTION_STRAIN_NOT_CONTROLLED_BY_SCALAR_A2_LERAY_BUDGETS
__PACKET_OCCUPATION_OR_NONDEGENERACY_REQUIRED.
```

It is an exact periodic NSE mechanism separator plus a narrowing of the
whole-space proof obligation.  A2 remains open.  No MATHCERT, novelty,
priority, publication, or whole-space counterexample claim is asserted.
