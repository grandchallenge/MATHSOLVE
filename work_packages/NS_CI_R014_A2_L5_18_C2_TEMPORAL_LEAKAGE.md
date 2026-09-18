# NS-CI-R014-A2-L5-18 — exact 2.5D temporal leakage calibration

## Disposition

- Campaign: NS-CI-001
- Restricted target: NS-CI-R014-A2
- Tracker: MATHSOLVE#59
- Protected base: 8e692aaca7b0932c412a03eb33985ba5994b1d5f
- Protected mathematical predecessor: d9ce36bdb27c9075c1104cb33c199d0b8f640bdd
- Predecessor: NS-CI-R014-A2-L5-17
- Result:
  EXACT_2P5D_NSE_EMBEDDING_PROVED__FINITE_DISTANCE_TEMPORAL_SPECTRAL_LEAKAGE_PROVED__LEAKAGE_AMPLITUDE_NOT_THRESHOLD_CHARGE
- A2 theorem: open
- L5: active
- C2-TIME: active, narrowed to quantitative threshold-sized temporal leakage
- MATHCERT adjudication: absent
- Evidence class: exact theorem for an unforced periodic 2.5D Navier–Stokes trajectory used only as temporal calibration; not the selected whole-space A2 class

L5-17 proved that a large active target can have turnover-size instantaneous variation while all input Fourier support lies at or below the target. The live question was whether the same algebra can persist dynamically without creating higher-frequency consequences.

This tranche embeds the L5-17 plus-phase snapshot into an exact time-evolving unforced periodic Navier–Stokes solution. The horizontal velocity closes as a decaying 2D Euler eigenfield and the vertical component becomes a passive advection–diffusion scalar. Its Fourier ODE has a nearest-neighbour lattice structure.

The exact consequence is two-sided.

First, the L5-17 configuration does leak to higher frequencies dynamically: every fixed finite lattice distance from the target has a nonzero first-possible temporal jet.

Second, the leading Taylor coefficient at lattice distance r carries a factorial penalty. Mere nonzero support at higher frequency therefore does not provide the lower bound needed to violate the dissipation-wavenumber threshold or to create a non-summable A2 charge.

The live successor is thus quantitative amplitude leakage, not support leakage.

## 1. Exact 2.5D embedding

Work on the periodic three-torus and take fields independent of x_3. Let

$$
a(t)=A e^{-\nu N^2 t},
$$

and define the horizontal velocity

$$
v(t,x_1,x_2)
=
\big(
a(t)\cos(Nx_2),
a(t)\cos(Nx_1)
\big).
$$

It is divergence free. Its convection is

$$
(v\cdot\nabla)v
=
-a(t)^2 N
\big(
\cos(Nx_1)\sin(Nx_2),
\sin(Nx_1)\cos(Nx_2)
\big),
$$

which is exactly

$$
-\nabla\left(
a(t)^2\sin(Nx_1)\sin(Nx_2)
\right).
$$

Hence the Leray projection of the horizontal convection vanishes. Since both horizontal modes have Laplace eigenvalue minus N^2,

$$
\partial_t v
=
\nu\Delta v.
$$

Thus v is an exact unforced 2D Navier–Stokes velocity after the pressure absorbs the displayed gradient.

Now let w(t,x_1,x_2) solve

$$
\partial_t w+v\cdot\nabla w=\nu\Delta w
$$

with initial datum

$$
w(0)
=
A\cos(Nx_1)
+
A\cos(Nx_2)
+
C\sin(Nx_1+Nx_2).
$$

Then

$$
u=(v_1,v_2,w)
$$

is an exact smooth unforced 3D Navier–Stokes solution in the 2.5D periodic class.

At t=0 this is exactly the sigma=+1 L5-17 field

$$
u(0)
=
A(0,1,1)\cos(Nx_1)
+
A(1,0,1)\cos(Nx_2)
+
C e_3\sin(Nx_1+Nx_2).
$$

The point of this embedding is not to change the selected domain. It is to test the temporal coherence mechanism on a genuine NSE trajectory rather than on one frozen Fourier snapshot.

## 2. Exact vertical Fourier system

Write

$$
w(t,x_1,x_2)
=
\sum_{m,n\in\mathbb Z}
W_{m,n}(t)e^{iN(mx_1+nx_2)}.
$$

The passive scalar equation gives the exact coefficient system

$$
\dot W_{m,n}
=
-\nu N^2(m^2+n^2)W_{m,n}
-\frac{iNa(t)}2
\left[
m(W_{m,n-1}+W_{m,n+1})
+
n(W_{m-1,n}+W_{m+1,n})
\right].
$$

The initial nonzero positive-frequency coefficients relevant below are

$$
W_{1,0}(0)=\frac A2,
\qquad
W_{0,1}(0)=\frac A2,
\qquad
W_{1,1}(0)=-\frac{iC}{2},
$$

together with the conjugate coefficients required by reality.

The Fourier coupling is nearest-neighbour on the integer lattice: one nonlinear interaction changes at most one of m,n by one.

## 3. Recovery of the L5-17 target derivative

For the target coefficient W_{1,1},

$$
\dot W_{1,1}(0)
=
i\nu N^2 C
-\frac{iNA^2}{2}.
$$

Since W_{1,1}=-iC/2 for the physical sine amplitude C, this is exactly

$$
\boxed{
\dot C(0)
=
A^2N-2\nu N^2 C.
}
$$

Thus the genuine periodic trajectory reproduces the sigma=+1 L5-17 turnover-size target derivative.

For A=C=R\nu N,

$$
\frac{\dot C(0)}{C}
=
\nu N^2(R-2),
$$

which is of turnover size when R is large.

## 4. First delayed higher-frequency mode

The mode (2,1) is initially absent. Its exact first derivative is

$$
\dot W_{2,1}(0)
=
-\frac{NAC}{4}.
$$

Equivalently, the physical coefficient at frequency

$$
N(2,1,0)
$$

appears linearly in time with leading amplitude NAC/2.

This is already a temporal distinction from L5-17: strict-high input can be empty at the initial instant while higher-frequency output begins to be created immediately under the actual PDE.

However, the frequency ratio from the target N(1,1,0) to N(2,1,0) is only

$$
\sqrt{5/2},
$$

so this first leakage event must not be identified automatically with a strict-high Littlewood–Paley shell under the fixed smooth annular partition.

## 5. Shortest-path leakage theorem

For every integer r at least one, define

$$
\kappa_r
=
N(r+1,1,0).
$$

Its lattice distance from the target (1,1) is exactly r.

Because each interaction changes at most one lattice coordinate by one, all derivatives of W_{r+1,1} of order less than r vanish at t=0.

At derivative order r, there is a unique shortest path

$$
(1,1)
\to
(2,1)
\to
\cdots
\to
(r+1,1).
$$

Any viscous diagonal step, any derivative of the time-dependent coefficient a(t), or any contribution from the initial source modes consumes derivative order without advancing the full lattice distance and therefore cannot contribute at this first possible order.

Repeated use of the x_1-shift coefficient gives

$$
\boxed{
W_{r+1,1}^{(r)}(0)
=
\left(-\frac{iNA}{2}\right)^r
W_{1,1}(0)
=
(-i)^{r+1}
\frac{C(NA)^r}{2^{r+1}}.
}
$$

In particular,

$$
\left|W_{r+1,1}^{(r)}(0)\right|
=
\frac{C(NA)^r}{2^{r+1}}
>0.
$$

The first two cases are

$$
\dot W_{2,1}(0)=-\frac{NAC}{4},
$$

and

$$
\ddot W_{3,1}(0)=i\frac{N^2A^2C}{8}.
$$

Since the exact 2.5D solution is smooth in time, for each fixed r,

$$
W_{r+1,1}(t)
=
(-i)^{r+1}
\frac{C(NA)^r}{2^{r+1}r!}
t^r
+
o(t^r).
$$

Therefore each fixed finite spectral distance has a nonzero leading temporal jet and the corresponding Fourier coefficient is nonzero on a sufficiently small punctured initial interval.

This statement is pointwise in r. No uniform positive interval over all r is claimed.

## 6. Arbitrarily large finite spectral distance

The generated frequency satisfies

$$
|\kappa_r|
=
N\sqrt{(r+1)^2+1}.
$$

Relative to the original target K=N\sqrt2,

$$
\frac{|\kappa_r|^2}{K^2}
=
\frac{(r+1)^2+1}{2}
\longrightarrow\infty.
$$

Thus no finite Fourier-support barrier is preserved by this exact trajectory in the finite-jet sense above.

For any prescribed finite frequency factor M, one can choose r so that |\kappa_r|>MK and the first nonzero temporal derivative of that coefficient is explicitly known.

This is a temporal leakage theorem, but it is not yet a dissipation-wavenumber theorem.

## 7. Why support leakage is not threshold leakage

The physical real-mode amplitude uses both conjugate Fourier coefficients. The leading r-th Taylor contribution has magnitude

$$
C\frac{(NA t)^r}{2^r r!}.
$$

At the nominal turnover time

$$
t_{\rm turn}=(AN)^{-1},
$$

the leading term alone would have relative size

$$
\frac{1}{2^r r!}.
$$

This decreases factorially with lattice distance.

Two claim boundaries are essential.

First, this leading-jet calculation is not a finite-time lower bound at t=t_turn. Higher Taylor terms may alter or cancel it there.

Second, even an exactly nonzero high Fourier coefficient need not violate the strict-high threshold

$$
\lambda_p^{-1}\|u_p\|_\infty<c_0\nu.
$$

The threshold requires quantitative amplitude at the relevant Littlewood–Paley shell, not merely support.

Therefore L5-18 proves that delayed spectral leakage is structurally present in an exact NSE calibration, but it does not produce the non-summable charge required by A2.

## 8. Energy identity in the calibration class

The vertical equation is passive advection–diffusion by a divergence-free horizontal field, hence

$$
\frac12\|w(t)\|_2^2
+
\nu\int_0^t\|\nabla w(s)\|_2^2\,ds
=
\frac12\|w(0)\|_2^2.
$$

Thus the generated high-frequency tail is paid for inside an ordinary finite dissipation budget in this globally regular periodic calibration.

This reinforces the distinction between:

- creation of higher frequencies;
- threshold-sized high-frequency activity;
- a non-summable time-integrated cost.

Only the first is proved here.

## 9. Consequence for C2-TIME

L5-17 ruled out the pointwise implication

large rapid active-shell variation implies strict-high activity at the same instant.

L5-18 now shows that the same configuration can be evolved as a genuine NSE trajectory and that higher-frequency leakage does occur in its temporal jets.

The live question is therefore sharpened to:

Can a large upper-band overshoot repeatedly saturate same-band forcing while every generated higher-frequency contribution remains below the strict-high threshold at a total cost compatible with Lambda in L2?

A valid successor needs one of the following genuinely quantitative outputs:

1. a finite-time lower bound on at least one generated shell above the active threshold;
2. a time-integrated lower bound for generated strict-high energy or dissipation;
3. a cumulative signed-flux identity that converts repeated internal saturation into a non-summable cost;
4. a phase-decoherence estimate strong enough to bound the overshoot integral directly.

Nonzero support alone is no longer a useful target.

## 10. Hard rejection tests

Reject any successor that:

- treats this periodic 2.5D theorem as a theorem in the selected whole-space A2 class;
- identifies a Fourier frequency increase with a strict-high shell without checking the fixed Littlewood–Paley partition;
- upgrades the first nonzero Taylor coefficient to a turnover-time lower bound without controlling the remainder;
- uses nonzero support as though it violated the threshold amplitude condition;
- reopens L3 using only turnover residence;
- reopens L4 using only the unsigned active diagonal;
- assumes the selector Q remains fixed while generated modes appear.

## 11. Next live obligation: C2-AMP

The smallest safe successor is quantitative amplitude leakage.

Freeze one active shell over a short interval only if that can be done without assuming selector variation. Decompose the exact shell Duhamel term into:

- internal active-band transfer;
- newly generated higher-frequency transfer;
- already-controlled far-low terms.

Seek a lower bound that survives the smooth dyadic projection and is strong enough to charge either the strict-high threshold or an integrated dissipation/flux quantity.

The first acceptable advance is not a full A2 proof. It is a theorem that converts sustained same-band saturation into a quantitative higher-frequency or signed temporal cost stronger than turnover residence.

## 12. Claim boundary

The protected claim sought from this tranche is exactly

EXACT_2P5D_NSE_EMBEDDING_PROVED__FINITE_DISTANCE_TEMPORAL_SPECTRAL_LEAKAGE_PROVED__LEAKAGE_AMPLITUDE_NOT_THRESHOLD_CHARGE.

It proves an exact temporal-calibration theorem for an unforced periodic 2.5D NSE trajectory.

It does not prove A2.

It does not prove a strict-high shell lower bound.

It does not prove a finite-time turnover-scale leakage amplitude.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
