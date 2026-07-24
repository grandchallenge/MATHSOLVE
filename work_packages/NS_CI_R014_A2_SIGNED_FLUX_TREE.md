# NS-CI-R014-A2-L3d — Signed shell flux and cross-level packing

## Status

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Tracker: `MATHSOLVE#32`
- Result: `PROVED_SHELL_ENERGY_FLOOR_SIGNED_FLUX_ONLY_ROUTE_TERMINATED`
- A2 status: unproved

This package derives the exact shell and cumulative energy identities, proves the energy floor forced by a dissipation-threshold shell, and audits whether signed flux or frequency-tree bookkeeping strengthens the summable exit charge from `NS-CI-R014-A2-L3c`.

The result is negative but exact. A threshold shell carries at least order `nu^2 lambda_q^{-1}` of `L2` energy. This is the same summable inverse-frequency scale already found in the exit-charge proof. A drop in shell `L-infinity` amplitude does not force a signed decrease of shell `L2` energy: a single packet can split into several separated packets in the same annulus while nearly preserving energy and halving the supremum. Consequently the signed shell identity has no universal sign at an amplitude exit. Exact cumulative flux telescoping also acquires moving-cutoff jump terms of the same summable size. An abstract conservative-dissipative shell chain reaches every dyadic level while satisfying threshold energy floors, signed flux balance, and finite total dissipation.

Therefore signed energy flux and tree bookkeeping, without an additional coherent concentration or occupancy theorem, do not close A2.

## I. Exact shell-energy identity

For the telescoping audit, use mutually orthogonal Fourier projections `P_q` onto disjoint annuli and write

```math
v_q=P_qu,
\qquad
P_{\le q}=\sum_{p\le q}P_p.
```

For a smooth divergence-free Navier–Stokes solution,

```math
\frac12\frac d{dt}\|v_q\|_2^2
+\nu\|\nabla v_q\|_2^2
=\mathcal T_q,
```

where

```math
\mathcal T_q
=-\langle P_q(u\cdot\nabla u),v_q\rangle.
```

The pressure term vanishes because `P_q` commutes with derivatives and `v_q` is divergence-free. Summing over all shells gives

```math
\sum_q\mathcal T_q
=-\langle u\cdot\nabla u,u\rangle
=0.
```

For Leray–Hopf solutions, the identity is first established on smooth Galerkin or mollified approximants. Passing to the limit in a fixed finite set of shells is an imported compactness interface. No shellwise equality for an infinite sum is asserted without that limiting argument.

## II. Fixed-cutoff cumulative flux

Define

```math
E_{\le q}
=\frac12\|P_{\le q}u\|_2^2,
\qquad
D_{\le q}
=\nu\|\nabla P_{\le q}u\|_2^2,
```

and the signed outward flux

```math
\Pi_q
=\langle P_{\le q}(u\cdot\nabla u),P_{\le q}u\rangle.
```

Then

```math
\frac d{dt}E_{\le q}+D_{\le q}+\Pi_q=0.
```

Orthogonality gives

```math
-\Pi_q=\sum_{p\le q}\mathcal T_p.
```

This is exact telescoping for the orthogonal shell ledger. The campaign's smooth Littlewood–Paley blocks have finite overlap rather than exact orthogonality; their corresponding identities carry fixed overlap matrices. No argument below depends on replacing finite overlap by exact equality at the dissipation-wavenumber threshold.

## III. Threshold-to-energy floor

Return to a standard smooth dyadic block `u_q=Delta_q u`, as used in the dissipation-wavenumber definition. Bernstein gives

```math
\|u_q\|_\infty
\le C_B\lambda_q^{3/2}\|u_q\|_2.
```

Hence a threshold event

```math
\|u_q(t)\|_\infty
\ge c_0\nu\lambda_q
```

implies

```math
\|u_q(t)\|_2^2
\ge
C_B^{-2}c_0^2\nu^2\lambda_q^{-1}.
```

This is the strongest lower bound available from Bernstein alone. Its frequency weight is

```math
\lambda_q^{-1}=2^{-q},
```

which is summable. Thus even one threshold-compatible energy packet at every level is consistent with a finite total energy budget.

## IV. Amplitude exit does not imply shell-energy loss

### Packet-splitting lemma

Fix a nonzero divergence-free Schwartz vector field `phi` whose Fourier support lies in a compact annulus and normalize

```math
\|\phi\|_\infty=1.
```

For `lambda=lambda_q`, set

```math
\phi_{q,x}(y)=\phi(\lambda(y-x)),
\qquad
\theta=c_0\nu\lambda.
```

Then

```math
\|\phi_{q,x}\|_2^2
=\lambda^{-3}\|\phi\|_2^2.
```

Define the initial one-packet field

```math
f_q=2\theta\phi_{q,0}.
```

Choose four translation centers separated by distances tending to infinity in units of `lambda^{-1}` and define

```math
g_{q,R}
=\theta\sum_{j=1}^4\phi_{q,x_j(R)}.
```

Translations preserve the same annular Fourier support. Schwartz decay and translation orthogonality give, as `R` tends to infinity,

```math
\|g_{q,R}\|_\infty
\longrightarrow\theta,
```

and

```math
\|g_{q,R}\|_2^2
\longrightarrow
4\theta^2\lambda^{-3}\|\phi\|_2^2
=
\|f_q\|_2^2.
```

Consequently, for every `epsilon>0`, there are same-annulus divergence-free fields satisfying

```math
\|f_q\|_\infty=2\theta,
\qquad
\|g_q\|_\infty\le(1+\epsilon)\theta,
```

while

```math
\left|
\|f_q\|_2^2-\|g_q\|_2^2
\right|
\le
\epsilon\theta^2\lambda^{-3}.
```

This is a kinematic estimate fixture, not a Navier–Stokes trajectory. It proves that no uniform positive shell-energy drop can be inferred from a factor-two `L-infinity` exit using frequency localization, divergence freedom, and endpoint amplitudes alone.

### Consequence for signed shell transfer

Integrating the exact shell identity gives

```math
\int_s^t\mathcal T_q(r)dr
=
\frac12\left(
\|v_q(t)\|_2^2-\|v_q(s)\|_2^2
\right)
+
\nu\int_s^t\|\nabla v_q\|_2^2dr.
```

The packet-splitting lemma shows that an `L-infinity` exit does not determine the sign or a positive lower magnitude of the endpoint energy difference. Replacing signed transfer by its absolute value destroys the telescoping property. Therefore amplitude exit plus the shell identity supplies no non-summable signed-flux charge.

## V. Moving cutoff identity

Let `Q(t)` be a piecewise constant integer-valued cutoff with jump times `t_j`. Define

```math
\mathscr E(t)=E_{\le Q(t)}(t).
```

On fixed-cutoff intervals the cumulative identity holds. Summing those intervals gives

```math
\mathscr E(b)-\mathscr E(a)
+
\int_a^b
\left(
D_{\le Q(t)}+\Pi_{Q(t)}
\right)dt
=
\sum_{t_j\in(a,b)}
\left(
E_{\le Q(t_j+)}(t_j)
-
E_{\le Q(t_j-)}(t_j)
\right).
```

The right side is the cutoff-motion ledger. An upward jump by one shell contributes that shell's energy; a downward jump subtracts it. These terms have no fixed sign over a general moving cutoff and cannot be discarded.

At a threshold-compatible upward crossing, the natural shell-energy scale is only

```math
\nu^2\lambda_q^{-1}.
```

Thus moving-cutoff bookkeeping reproduces the already-summable energy scale rather than a stronger cross-level charge.

## VI. Conservative-dissipative shell-chain fixture

The insufficiency can be encoded in an exact scalar shell-balance model.

Let

```math
\lambda_q=2^q,
\qquad
e_q=\kappa\nu^2\lambda_q^{-1}.
```

At stage `q`, place energy `e_q` in shell `q`, transfer

```math
j_q=e_{q+1}
```

to shell `q+1`, and dissipate

```math
d_q=e_q-e_{q+1}.
```

Then the exact stage balance is

```math
e_q=j_q+d_q.
```

Moreover,

```math
\sum_{q\ge0}d_q=e_0,
\qquad
\sum_{q\ge0}j_q=e_0,
```

while every dyadic level is reached with the threshold-compatible energy floor `e_q`.

Assign occupancy times

```math
\tau_q
=\frac{1}{\nu\lambda_q^2(q+1)^2}.
```

Then the abstract dissipation-wavenumber cost is finite:

```math
\sum_q\lambda_q^2\tau_q
=
\nu^{-1}\sum_q\frac1{(q+1)^2}
<\infty.
```

The chain satisfies positive forward signed transfers, exact shell balance, finite total dissipation, finite total transfer, and threshold-compatible energy at every level. It nevertheless reaches arbitrarily high frequencies. This is an algebraic flux fixture, not a Navier–Stokes solution.

## VII. Frequency-tree disposition

A tree whose nodes are threshold boxes can assign each node the energy floor

```math
w_q\asymp\nu^2\lambda_q^{-1}.
```

A single infinite branch has finite total weight because

```math
\sum_qw_q<\infty.
```

Orthogonality prevents simultaneous double-counting of disjoint shell energies, but it does not make the branch weight non-summable. Signed telescoping controls net transfer across a cutoff, not the number of levels traversed. Nested time-frequency nodes also require an independent covering theorem; ordinary disjointness does not control the whole tree.

Therefore a cross-level proof needs information absent from energy and signed flux alone, such as:

1. coherent concentration preventing packet splitting;
2. a lower bound on actual residence time at each reached level;
3. a nonlocal interaction charge that grows rather than decays with frequency;
4. a geometric restriction on branching or repeated crossings;
5. a threshold-cluster estimate coupling adjacent shell amplitudes to signed flux.

## Route disposition

| Route | Disposition | Exact reason |
|---|---|---|
| fixed shell-energy identity | proved | pressure cancels and the projected equation is exact |
| fixed cumulative-flux identity | proved | orthogonal shell ledger telescopes exactly |
| threshold-to-shell-energy floor | proved | inverse Bernstein gives `nu^2 lambda_q^-1` |
| infer shell-energy drop from amplitude exit | terminated | same-annulus packet splitting preserves energy while reducing the supremum |
| signed shell flux as an exit charge | terminated in generic form | endpoint energy change has no sign; absolute values destroy telescoping |
| moving-cutoff flux | audited | jump ledger is explicit and has only inverse-frequency scale |
| signed flux plus energy tree | terminated as a standalone route | conservative-dissipative chain reaches every level with finite total charge |
| coherent concentration or occupancy enhancement | open | not implied by current scalar or energy interfaces |

## Strongest surviving interface

The next proof cannot rely only on shell energy, signed flux conservation, or orthogonality. It must couple threshold amplitude to **coherent spatial concentration or time occupancy** in a manner stable under packet splitting. A viable theorem would need to rule out the four-packet fixture dynamically or charge its creation through a stronger quantity than total kinetic energy.

## WP03 boundary

No numerical lane is authorized. A future computational task must target a precise continuum-uniform concentration, packet-multiplicity, or residence-time inequality. Observing forward flux or shell-energy transfer in finite resolution is not evidence for A2.

## Claim boundary

This package proves exact energy and flux identities, the threshold shell-energy floor, and two estimate counterfixtures. It does not construct a Navier–Stokes counterexample, prove that all signed-flux refinements fail, or prove A2. It terminates only arguments based solely on endpoint shell amplitudes, kinetic-energy balance, signed flux telescoping, and unrestricted frequency-tree bookkeeping.
