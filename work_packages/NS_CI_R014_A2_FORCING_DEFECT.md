# NS-CI-R014-A2-L3b — Parabolic forcing-defect decomposition

## Status

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Tracker: `MATHSOLVE#28`
- State: `ABSOLUTE_DECOMPOSITION_AUDITED_DYNAMIC_CANCELLATION_OPEN`
- A2 status: unproved

The previous energy-class audit showed that an undifferentiated forcing estimate loses one full frequency power on a parabolic interval. This package decomposes that loss. The low–high transport structure recovers one derivative, but standard energy control still leaves a half-power deficit. Absolute high–high estimates reduce to a scale-critical local dissipation mass and do not force persistence. A robust comparison between different dissipation thresholds fails at the level of the definition plus energy bounds.

## Normalized defect

For

```math
F_q=\Delta_q\mathbb P\nabla\cdot(u\otimes u),
```

define

```math
\mathfrak D_q(I)
=
\frac{1}{\nu\lambda_q}
\int_I\|F_q(t)\|_\infty dt,
\qquad
|I|=c(\nu\lambda_q^2)^{-1}.
```

A uniformly small defect, together with a threshold buffer or a robust-threshold theorem, would yield parabolic shell persistence.

## Bony interaction ledger

Write schematically

```math
u\cdot\nabla u
=
\sum_p u_{\le p-2}\cdot\nabla u_p
+
\sum_p u_p\cdot\nabla u_{\le p-2}
+
\sum_p\sum_{|p-p'|\le1}u_p\cdot\nabla u_{p'}.
```

After applying `Delta_q`, the first two sums have `p=q+O(1)`, while the high–high sum has `p,p'>=q-O(1)`.

| Interaction | Absolute structure | Available gain | Remaining obstruction |
|---|---|---|---|
| principal low–high | transport plus commutator | derivative on the high shell can be removed | low-mode Lipschitz integral |
| high–low | derivative already falls on the low mode | one high-frequency derivative avoided | low-mode Lipschitz integral |
| pressure correction | band-limited order `-1` operator after divergence identity | derivative transfers to low mode | low-mode Lipschitz integral and finite-neighbour coupling |
| near-threshold high–high | no transport structure | none from absolute values | uncontrolled threshold cluster |
| far high–high to low | output derivative is `lambda_q`, not input frequency | can be bounded by high-frequency energy tail | local dissipation mass is not uniformly small |
| heat decrement | semigroup control | parabolic | threshold margin still required |

## Low–high transport and commutator gain

For a low-frequency divergence-free drift `a=u_{<=q-2}` and a `q`-shell `b=u_q`,

```math
\Delta_q(a\cdot\nabla b)
=
a\cdot\nabla b
+
[\Delta_q,a\cdot\nabla]b
```

up to the finite overlap of the dyadic partition. The main term is transport. The commutator obeys

```math
\|[\Delta_q,a\cdot\nabla]b\|_\infty
\lesssim
\|\nabla a\|_\infty\|b\|_\infty.
```

The pressure correction has the same schematic cost. Indeed, using `div a=div b=0`,

```math
\nabla\cdot(a\cdot\nabla b)
=
\partial_i a_j\,\partial_j b_i.
```

On output frequency `q`, the operator `nabla Delta^{-1}` gains one factor `lambda_q^{-1}`, cancelling the derivative on `b`. Thus the projected low–high remainder is bounded by

```math
\|R_q^{LH}\|_\infty
\lesssim
G_q\,A_q^*,
```

where

```math
G_q=\|\nabla u_{\le q-2}\|_\infty,
\qquad
A_q^*=\max_{|p-q|\le C}\|u_p\|_\infty.
```

This is a genuine one-derivative structural gain over treating the entire nonlinearity as undifferentiated forcing. It is not a closure because `G_q` is not controlled at the required scale.

## Energy bound for the low-mode Lipschitz coefficient

Bernstein and Cauchy–Schwarz give

```math
G_q
\lesssim
\sum_{p\le q-2}\lambda_p^{5/2}\|u_p\|_2
\lesssim
\lambda_q^{3/2}\|\nabla u\|_2.
```

Therefore, on a parabolic interval `I`,

```math
\int_I G_qdt
\lesssim
\lambda_q^{3/2}|I|^{1/2}
\left(\int_I\|\nabla u\|_2^2dt\right)^{1/2}
```

and hence

```math
\int_I G_qdt
\lesssim
c^{1/2}
\left(
\frac{\lambda_q}{\nu^2}
\mu(I)
\right)^{1/2},
\qquad
\mu(I)=\nu\int_I\|\nabla u\|_2^2dt.
```

Using only the global energy inequality yields

```math
\int_I G_qdt
\lesssim
c^{1/2}U\nu^{-1}\lambda_q^{1/2}.
```

Thus the transport/commutator structure reduces the frequency deficit from one full power to one half power, but it does not provide a uniform parabolic bound.

A global assumption making `G_q` integrable uniformly in `q` is essentially the low-mode regularity route already under audit and cannot be inserted as a proof of A2.

## High–high absolute estimate

For the high–high contribution with inputs at frequencies at least `q-O(1)`, an `L^1_x` product estimate and output Bernstein give

```math
\|F_q^{HH}\|_\infty
\lesssim
\lambda_q^4
\sum_{p\ge q-C}\|u_p\|_2^2.
```

Since

```math
\sum_{p\ge q-C}\|u_p\|_2^2
\lesssim
\lambda_q^{-2}\|\nabla u\|_2^2,
```

one obtains

```math
\|F_q^{HH}\|_\infty
\lesssim
\lambda_q^2\|\nabla u\|_2^2.
```

Consequently

```math
\frac{1}{\nu\lambda_q}
\int_I\|F_q^{HH}\|_\infty dt
\lesssim
\frac{\lambda_q}{\nu^2}\mu(I).
```

This is scale-invariant, but the energy inequality does not make the local parabolic mass `lambda_q mu(I)/nu^2` uniformly small. Absolute high–high control therefore supplies an interface, not persistence.

The dissipation-wavenumber threshold controls shells strictly above `Q`; it does not give an upper bound on the threshold shell or the lower neighbouring shells. Applying it to the entire near-threshold cluster is invalid.

## Local parabolic dissipation number

The low–high and high–high estimates are both governed by

```math
\mathcal E_q(I)
=
\frac{\lambda_q}{\nu^2}\mu(I)
=
\frac{\lambda_q}{\nu}
\int_I\|\nabla u\|_2^2dt.
```

The decomposition yields schematically

```math
\mathfrak D_q(I)
\lesssim
C_1\mathcal E_q(I)^{1/2}\,\mathcal A_q(I)
+
C_2\mathcal E_q(I)
+
\text{near-threshold coupling},
```

where `mathcal A_q` records the finite-neighbour shell-amplitude ratio. A viable route must either control this amplitude ratio and show `mathcal E_q` is small on the relevant boxes, or find cancellation not visible in the absolute estimates.

## Robust-threshold comparison fails kinematically

Let `0<eta<a<1`. Consider disjoint time intervals `I_k` with

```math
|I_k|=\frac{2^{-2k}}{k},
```

and a band-limited packet at frequency `lambda_k=2^k` whose normalized amplitude is

```math
\lambda_k^{-1}\|u_k\|_\infty=a c_0\nu.
```

The packet violates the stricter threshold `eta c_0` but not the original threshold `c_0`. Choose the packet to saturate Bernstein at the scalar level:

```math
\|u_k\|_2\asymp\nu\lambda_k^{-1/2}.
```

Then:

```math
\sup_k\|u_k\|_2^2<\infty,
```

and the total scalar dissipation budget is finite because

```math
\sum_k |I_k|\lambda_k^2\|u_k\|_2^2
\asymp
\nu^2\sum_k\frac{2^{-k}}{k}<\infty.
```

However, the stricter-threshold wavenumber has divergent critical norm:

```math
\sum_k |I_k|\lambda_k^2
=
\sum_k\frac1k
=\infty,
```

while the original-threshold wavenumber remains bounded in this abstract packet model.

Therefore no estimate of the form

```math
\Lambda_{c_0}\in L^2_t
\Longrightarrow
\Lambda_{\eta c_0}\in L^2_t
```

follows from the threshold definition plus energy and dissipation bounds alone. This is a kinematic counterfixture, not a Navier–Stokes solution.

## Route dispositions

| Route | Disposition | Exact reason |
|---|---|---|
| undifferentiated energy forcing | terminated | one full frequency-power deficit |
| low–high transport/commutator | survives as an interface | derivative gain is real, but energy leaves a half-power deficit |
| low-mode Lipschitz closure | circular in generic form | uniform integrability is the low-mode regularity criterion |
| high–high absolute estimate | survives as a local-mass interface | no uniform smallness of `mathcal E_q(I)` |
| use high-mode threshold on all near shells | rejected | threshold controls only shells strictly above `Q` |
| robust-threshold comparison from energy | terminated | explicit packet counterfixture |
| dynamic cancellation or packing | open | not captured by absolute estimates |

## Strongest surviving interface

The forcing-defect route remains viable only through a dynamic statement coupling threshold events to parabolic boxes with controlled

```math
\mathcal E_q(I),
```

finite-neighbour amplitude ratio, and pressure/commutator remainder. Equivalent admissible outcomes include:

1. a Carleson packing estimate for boxes where `mathcal E_q` is large;
2. a cancellation estimate replacing `mathcal E_q` by a signed flux quantity;
3. a bootstrap showing a threshold shell cannot exit before either accumulating a fixed `L^2_t` cost or entering a box charged to a summable dissipation measure.

## WP03 boundary

A precise computational falsification question now exists: test proposed universal inequalities relating shell-exit time to `mathcal E_q(I)` and the finite-neighbour amplitude ratio. WP03 remains closed until such an inequality is stated with continuum-uniform constants. Simulations cannot validate the decomposition or A2.

## Claim boundary

This package does not prove a small forcing defect, parabolic persistence, or A2. It proves the threshold-comparison counterfixture and records the exact structural gains and deficits of the Bony/commutator decomposition. The remaining route is genuinely dynamic rather than an absolute interpolation estimate.
