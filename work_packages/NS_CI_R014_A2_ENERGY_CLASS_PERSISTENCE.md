# NS-CI-R014-A2-L3 — Energy-class shell persistence

## Status

- Campaign: `NS-CI-001`
- Selected target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#26`
- Result: `PROVED_RELAXED_THRESHOLD_SUBPARABOLIC_MODULUS`
- Sufficiency for A2: no

This work package asks what persistence of a dissipation-threshold shell follows from the Leray–Hopf energy class alone. The answer is precise but insufficient: energy-class temporal control gives a scale-covariant `lambda_q^{-6}` interval for a **relaxed threshold**, not the `lambda_q^{-2}` same-threshold persistence needed by the merged layer-cake reduction.

## Setting

Let `u` be a Leray–Hopf solution on `R^3` with viscosity `nu>0`. Write

```math
U=\|u_0\|_2,
\qquad
u\int_0^T\|\nabla u(t)\|_2^2dt\lesssim U^2.
```

Let `u_q=Delta_q u` and `lambda_q=2^q`. At a Lebesgue time `s`, suppose

```math
\|u_q(s)\|_\infty\ge c_0\nu\lambda_q.
```

For `t>s`, the projected equation is represented by

```math
u_q(t)
=
 e^{\nu(t-s)\Delta}u_q(s)
-
\int_s^t e^{\nu(t-r)\Delta}
\Delta_q\mathbb P\nabla\cdot(u\otimes u)(r)dr.
```

All estimates below are schematic up to constants depending only on the Littlewood–Paley partition.

## Lemma 1 — Energy-class interpolation

The Leray bounds imply

```math
u\in L^{8/3}(0,T;L^4),
\qquad
u\otimes u\in L^{4/3}(0,T;L^2),
```

and quantitatively

```math
\big\|\|u\|_4^2\big\|_{L^{4/3}(0,T)}
\lesssim U^2\nu^{-3/4}.
```

### Proof

The three-dimensional Gagliardo–Nirenberg inequality gives

```math
\|u\|_4
\lesssim
\|u\|_2^{1/4}\|\nabla u\|_2^{3/4}.
```

Hence

```math
\|u\|_4^{8/3}
\lesssim
\|u\|_2^{2/3}\|\nabla u\|_2^2.
```

Taking the time integral and using the energy inequality yields

```math
\int_0^T\|u\|_4^{8/3}dt
\lesssim
U^{2/3}\frac{U^2}{\nu}
=
U^{8/3}\nu^{-1}.
```

Raising to the `3/4` power gives the stated bound for `||u||_4^2` in `L^{4/3}_t`.

## Lemma 2 — Localized forcing modulus

Define

```math
F_q=\Delta_q\mathbb P\nabla\cdot(u\otimes u).
```

Then

```math
\|F_q(t)\|_\infty
\lesssim
\lambda_q^{5/2}\|u(t)\|_4^2,
```

and for every interval `I` of length `delta`,

```math
\int_I\|F_q(t)\|_\infty dt
\lesssim
\lambda_q^{5/2}\delta^{1/4}U^2\nu^{-3/4}.
```

### Proof

The derivative costs one factor `lambda_q`, and Bernstein from `L^2` to `L^infinity` costs `lambda_q^{3/2}`. Therefore

```math
\|F_q\|_\infty
\lesssim
\lambda_q^{5/2}\|u\otimes u\|_2
=
\lambda_q^{5/2}\|u\|_4^2.
```

Hölder in time with exponent `4/3` gives the interval factor `delta^{1/4}`.

## Proposition — Relaxed-threshold persistence

Fix `eta` with `0<eta<1`. There is a constant `c_eta>0` such that if

```math
\|u_q(s)\|_\infty\ge c_0\nu\lambda_q,
```

then for every

```math
0\le t-s\le\delta_q,
```

where

```math
\delta_q
=
c_\eta
\min\left\{
\nu^{-1}\lambda_q^{-2},
 c_0^4\nu^7U^{-8}\lambda_q^{-6}
\right\},
```

one has

```math
\|u_q(t)\|_\infty
\ge
\eta c_0\nu\lambda_q.
```

### Proof

For band-limited data,

```math
\|(e^{\nu\tau\Delta}-I)u_q(s)\|_\infty
\lesssim
\nu\lambda_q^2\tau\|u_q(s)\|_\infty.
```

Choosing `tau<=c_eta nu^{-1}lambda_q^{-2}` makes the heat decrement at most `(1-eta)/2` of the initial shell amplitude.

The Duhamel contribution is bounded by Lemma 2:

```math
\left\|
\int_s^t e^{\nu(t-r)\Delta}F_q(r)dr
\right\|_\infty
\lesssim
\lambda_q^{5/2}\tau^{1/4}U^2\nu^{-3/4}.
```

It is at most `(1-eta)c_0 nu lambda_q/2` whenever

```math
\tau
\lesssim
(1-\eta)^4c_0^4\nu^7U^{-8}\lambda_q^{-6}.
```

Combining the two decrements proves the result.

## Scaling check

Under Navier–Stokes scaling

```math
u_\rho(x,t)=\rho u(\rho x,\rho^2t),
```

one has

```math
U_\rho=\rho^{-1/2}U,
\qquad
\lambda_{q,\rho}=\rho\lambda_q.
```

Therefore

```math
U_\rho^{-8}\lambda_{q,\rho}^{-6}
=
\rho^4\rho^{-6}U^{-8}\lambda_q^{-6}
=
\rho^{-2}U^{-8}\lambda_q^{-6}.
```

Both terms in `delta_q` transform by `rho^{-2}`, so the modulus is scale-covariant despite its `lambda_q^{-6}` appearance at fixed energy.

## Two exact insufficiencies

### I. Duration deficit

The merged persistence reduction requires a same-scale duration comparable to

```math
\nu^{-1}\lambda_q^{-2}.
```

At fixed `U` and `nu`, the energy-class nonlinear estimate supplies only

```math
\nu^7U^{-8}\lambda_q^{-6}
```

at high frequency. Its contribution to the `L^2_t` layer-cake cost is

```math
\lambda_q^2\delta_q
\sim
\lambda_q^{-4},
```

which is summable over arbitrarily high levels and therefore cannot exclude an unbounded dissipation wavenumber.

### II. Threshold-margin deficit

The dissipation-wavenumber event guarantees only

```math
\lambda_q^{-1}\|u_q(s)\|_\infty\ge c_0\nu.
```

The proposition preserves a fraction `eta c_0`, not the original threshold `c_0`. Thus it gives persistence for a relaxed-threshold wavenumber, or same-threshold persistence only for a **buffered** event such as

```math
\|u_q(s)\|_\infty\ge 2c_0\nu\lambda_q.
```

No such uniform buffer follows from the definition of `Lambda`. Temporal continuity alone gives an event-dependent interval, not a uniform level-dependent interval.

## Parabolic forcing-defect interface

Define the normalized forcing defect on a parabolic interval by

```math
\mathfrak D_q(s;c)
=
\frac{1}{\nu\lambda_q}
\int_s^{s+c(\nu\lambda_q^2)^{-1}}
\|F_q(r)\|_\infty dr.
```

A uniform small bound on `mathfrak D_q`, together with a threshold buffer or a robust-threshold formulation, would yield parabolic shell persistence.

The energy-class estimate gives instead

```math
\mathfrak D_q(s;c)
\lesssim
c^{1/4}U^2\nu^{-2}\lambda_q.
```

It loses one full power of frequency.

More generally, suppose a localized forcing estimate has time exponent `r>1` and frequency cost `lambda_q^alpha`. Parabolic persistence by Hölder requires

```math
\alpha+\frac{2}{r}\le 3.
```

The energy-class pair is

```math
(\alpha,r)=(5/2,4/3),
\qquad
\alpha+2/r=4,
```

again showing a one-power deficit. The borderline can be reached by either:

- improving temporal integrability from `r=4/3` to `r=4` at the same spatial cost;
- gaining one factor of `lambda_q^{-1}` through cancellation or a shell-local estimate at the same time exponent;
- a mixed improvement satisfying `alpha+2/r<=3`.

A global `L^4_t` bound for `||u||_4^2` is itself a critical LPS-type regularity assumption, so the required gain must be localized, structural, or compensatory rather than inserted globally.

## Route disposition

| Route | Result |
|---|---|
| Leray energy plus Gagliardo–Nirenberg | proves `L^{4/3}_tL^2_x` control of `u tensor u` |
| Projected mild equation | proves relaxed-threshold persistence on a scale-covariant `lambda_q^{-6}` interval |
| Direct use in the layer-cake lemma | rejected: duration exponent is insufficient |
| Same-threshold persistence | rejected without a uniform threshold buffer |
| Parabolic upgrade | open: requires a one-frequency-power gain and a robust threshold mechanism |

## Next obligation

Derive or reject an equation-specific bound on the parabolic forcing defect `mathfrak D_q`. The admissible routes are:

1. shell-flux cancellation reducing the frequency cost from `5/2` to `3/2`;
2. time-frequency packing giving an effective local exponent satisfying `alpha+2/r<=3`;
3. a robust-threshold comparison controlling stricter dissipation wavenumbers from the selected `Lambda in L^2_t` hypothesis.

## Claim boundary

This proposition does not prove A2 or the parabolic-persistence hypothesis. It identifies the strongest direct modulus supplied by standard energy-class interpolation and the exact one-power and threshold-margin deficits that the next PDE estimate must overcome.
