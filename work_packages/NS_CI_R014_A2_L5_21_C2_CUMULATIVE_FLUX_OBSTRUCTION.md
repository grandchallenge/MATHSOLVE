# NS-CI-R014-A2-L5-21 — cumulative upper-band flux obstruction

## Disposition

- Campaign: \`NS-CI-001\`
- Restricted target: \`NS-CI-R014-A2\`
- Tracker: \`MATHSOLVE#59\`
- Protected base: \`af4578938868b265f2734d70e27adc2a9a582f7f\`
- Protected predecessor: \`NS-CI-R014-A2-L5-20\`
- Result:
  \`C2_FLUX_GENERIC_BAND_ENERGY_ROUTE_TERMINATED__OVERSHOOT_DIVERGES_WITH_SUMMABLE_BOUNDARY_FLUX\`
- A2 theorem: open
- L5: active
- C2-FLUX: generic band-energy variant terminated
- MATHCERT adjudication: absent
- Evidence class: exact conservative shell-and-packet scaling fixture; not a
  Navier--Stokes trajectory

L5-20 closed propagation distance as the missing charge mechanism in the exact
2.5D temporal calibration and moved the live route back to the selected
whole-space upper active band.

The first C2-FLUX question is whether one can keep the shell-energy transfer
signed, sum a complete retained upper band, and use the resulting cumulative
boundary flux plus dissipation to control the L5-15 overshoot quantity

\`\`\`math
\Omega(t)
=
\sup_{\lfloor4Q(t)/5\rfloor<p\le Q(t)}
\lambda_p
\big(
\|u_p(t)\|_\infty-c_0\nu\lambda_p
\big)_+.
\`\`\`

This tranche gives a bounded negative answer for the **generic band-energy
identity alone**.

There is an exact conservative nearest-neighbour shell ledger, compatible with
the threshold orientation and with turnover-rate energy variation, for which:

- the A2 selector charge is finite;
- the Leray dissipation budget is finite;
- the total kinetic energy is bounded;
- every active episode obeys an exact fixed-band energy balance;
- the signed cumulative boundary flux is summable;
- even the absolute unweighted boundary-flux variation is summable;
- but the overshoot integral \`\int\Omega\,dt\` diverges.

Therefore summing complete bands and retaining sign does not by itself produce
the missing cumulative cost. Any successful C2-FLUX theorem must use
additional Navier--Stokes structure that excludes this shell ledger, such as
triadic phase coherence, a directionality theorem for active-band flux, or a
new relation between threshold overshoot and frequency-weighted flux.

## 1. Scaling inherited from L5-15/L5-16

Work in nondimensional viscosity \`\nu=1\`; restoring a fixed positive viscosity
only multiplies the displayed charges by fixed powers and does not change the
summability exponents.

Choose overshoot ratios and dyadic frequencies

\`\`\`math
R_n=2^n,
\qquad
\lambda_n=R_n^4=2^{4n}.
\`\`\`

Let \`q_n=4n\`, so \`\lambda_{q_n}=\lambda_n\`.

The threshold-sized plateau amplitude is

\`\`\`math
a_n
=
R_n\lambda_n.
\`\`\`

For a Bernstein-saturating annular packet at frequency \`\lambda_n\`, the
corresponding shell energy scale is

\`\`\`math
E_n
\asymp
\frac{a_n^2}{\lambda_n^3}
=
\frac{R_n^2}{\lambda_n}
=
R_n^{-2}.
\`\`\`

The nonlinear turnover-time scale is

\`\`\`math
\delta_n
=
(\lambda_n a_n)^{-1}
=
(R_n\lambda_n^2)^{-1}
=
R_n^{-9}.
\`\`\`

These are exactly the L5-15 overshoot exponents.

## 2. Smooth disjoint episode windows

Choose one fixed smooth bump

\`\`\`math
H\in C_c^\infty((0,3)),
\qquad
0\le H\le1,
\`\`\`

with

\`\`\`math
H=1
\quad\text{on }[1,2].
\`\`\`

Let the episode supports be pairwise disjoint intervals

\`\`\`math
J_n
=
[t_n,t_n+3\delta_n].
\`\`\`

Define

\`\`\`math
h_n(t)
=
H\left(\frac{t-t_n}{\delta_n}\right).
\`\`\`

The active-shell energy is

\`\`\`math
e_{q_n}(t)
=
E_n h_n(t).
\`\`\`

All nonreservoir shells other than \`q_n\` have zero energy during the
\`n\`th episode.

On the plateau interval

\`\`\`math
I_n
=
[t_n+\delta_n,t_n+2\delta_n],
\`\`\`

the packet amplitude is \`a_n\`.

Because every shell above \`q_n\` is zero and shell \`q_n\` violates the
strict-high threshold for large \`R_n\`, the dissipation index on the plateau is

\`\`\`math
Q(t)=q_n.
\`\`\`

No claim is made about the selector during the smooth entry and exit portions;
for the A2 upper budget it is enough that no frequency above \`q_n\` is present.

## 3. Exact shell-energy and nearest-neighbour flux ledger

Set the active-shell dissipation to the standard frequency scale

\`\`\`math
d_{q_n}(t)
=
c_d\lambda_n^2e_{q_n}(t),
\`\`\`

with one fixed positive annular constant \`c_d\`.

Introduce a reservoir shell \`0\` with energy \`e_0(t)\` and zero dissipation.

During the \`n\`th episode define the nearest-neighbour flux across every edge
from shell \`0\` to shell \`q_n\` by

\`\`\`math
F_{p+1/2}(t)
=
e_{q_n}'(t)+d_{q_n}(t),
\qquad
m_n-1\le p<q_n.
\`\`\`

Set all other edge fluxes to zero.

Then the shell balances are exact:

\`\`\`math
e_{m_n-1}'
=
-F_{m_n-1/2},
\`\`\`

\`\`\`math
e_p'+d_p
=
F_{p-1/2}-F_{p+1/2}
=
0,
\qquad
m_n\le p<q_n,
\`\`\`

and

\`\`\`math
e_{q_n}'+d_{q_n}
=
F_{q_n-1/2}.
\`\`\`

Thus the transfer is conservative and nearest-neighbour local in shell index.

Summing the complete band \`1\le p\le q_n\` cancels every internal edge:

\`\`\`math
\frac d{dt}
\sum_{p=m_n}^{q_n}e_p
+
\sum_{p=m_n}^{q_n}d_p
=
F_{m_n-1/2}.
\`\`\`

This is exactly the kind of signed complete-band identity the C2-FLUX route
seeks to exploit.

## 4. Net signed boundary flux is only the dissipative cost

Each bump returns to zero, so

\`\`\`math
\int_{J_n}e_{q_n}'(t)\,dt
=
0.
\`\`\`

Therefore

\`\`\`math
\boxed{
\int_{J_n}F_{m_n-1/2}(t)\,dt
=
\int_{J_n}d_{q_n}(t)\,dt.
}
\`\`\`

The dissipation charge has scale

\`\`\`math
\lambda_n^2E_n\delta_n
=
\lambda_n^2
\frac{R_n^2}{\lambda_n}
\frac1{R_n\lambda_n^2}
=
\frac{R_n}{\lambda_n}
=
R_n^{-3}.
\`\`\`

Hence

\`\`\`math
\sum_n
\left|
\int_{J_n}F_{m_n-1/2}(t)\,dt
\right|
<
\infty.
\`\`\`

The reservoir loses only this summable total amount, so \`e_0(0)\` can be
chosen to keep the total shell energy nonnegative and uniformly bounded.

## 5. Even absolute unweighted boundary-flux variation is summable

The entry and exit energy variation satisfies

\`\`\`math
\int_{J_n}|e_{q_n}'(t)|\,dt
=
E_n
\int_0^3|H'(\tau)|\,d\tau.
\`\`\`

Thus

\`\`\`math
\int_{J_n}|e_{q_n}'(t)|\,dt
\asymp
E_n
=
R_n^{-2}.
\`\`\`

Using

\`\`\`math
|F_{m_n-1/2}|
\le
|e_{q_n}'|+d_{q_n},
\`\`\`

gives

\`\`\`math
\boxed{
\int_{J_n}|F_{m_n-1/2}(t)|\,dt
\lesssim
R_n^{-2}+R_n^{-3}.
}
\`\`\`

Therefore

\`\`\`math
\sum_n
\int_{J_n}|F_{m_n-1/2}(t)|\,dt
<
\infty.
\`\`\`

The same remains true if one sums the absolute flux over **every**
nearest-neighbour edge in the cascade path. There are \`q_n=4n\` such edges, so

\`\`\`math
\sum_n
q_n
\int_{J_n}|F_{m_n-1/2}(t)|\,dt
\lesssim
\sum_n
n2^{-2n}
<
\infty.
\`\`\`

Thus neither net signed boundary flux nor total unweighted boundary-flux
variation supplies the missing non-summable episode cost.

## 6. The ledger respects turnover-rate energy variation

The characteristic entry/exit derivative is

\`\`\`math
\frac{E_n}{\delta_n}
=
R_n^{-2}R_n^9
=
R_n^7.
\`\`\`

The turnover rate associated with the packet amplitude is

\`\`\`math
\lambda_n a_n
=
R_n^4R_n^5
=
R_n^9.
\`\`\`

Multiplying by the shell energy gives the turnover-scale energy-transfer size

\`\`\`math
(\lambda_na_n)E_n
=
R_n^9R_n^{-2}
=
R_n^7.
\`\`\`

Hence the shell ledger does not require energy variation faster than the
turnover scale already shown algebraically possible by L5-16/L5-17.

The fixture is still not asserted to be an NSE trajectory. This calculation
only prevents dismissal of the ledger on the ground that its transfer rate is
super-turnover.

## 7. A2 occupancy is summable

During the whole episode support, no shell above \`q_n\` carries energy.
Therefore

\`\`\`math
\Lambda(t)
\lesssim
\lambda_n
\qquad
(t\in J_n).
\`\`\`

The resulting A2 charge satisfies

\`\`\`math
\int_{J_n}\Lambda(t)^2\,dt
\lesssim
\lambda_n^2\delta_n
=
\frac1{R_n}.
\`\`\`

Thus

\`\`\`math
\boxed{
\sum_n
\int_{J_n}\Lambda(t)^2\,dt
<
\infty.
}
\`\`\`

On the plateau the sharper identity \`Q=q_n\` holds, but it is not needed for
the upper budget.

## 8. Leray dissipation and energy are finite

The total shell dissipation satisfies

\`\`\`math
\sum_n
\int_{J_n}d_{q_n}(t)\,dt
\lesssim
\sum_nR_n^{-3}
<
\infty.
\`\`\`

The episode energies are

\`\`\`math
E_n=R_n^{-2}.
\`\`\`

Because the supports are disjoint,

\`\`\`math
\sup_t\sum_qe_q(t)
\le
E_{reservoir}(0)+\sup_nE_n
<
\infty.
\`\`\`

Thus the fixture preserves the selected scalar energy and dissipation budgets.

## 9. The overshoot integral diverges

On \`I_n\),

\`\`\`math
Q=q_n,
\qquad
q_n\in
\{\lfloor4Q/5\rfloor<p\le Q\}.
\`\`\`

The active packet has

\`\`\`math
\|u_{q_n}\|_\infty
\asymp
a_n
=
R_n\lambda_n.
\`\`\`

For all sufficiently large \`n\`,

\`\`\`math
\Omega(t)
\gtrsim
\lambda_n
(R_n\lambda_n-c_0\lambda_n)
=
(R_n-c_0)\lambda_n^2.
\`\`\`

The plateau length is \`\delta_n=(R_n\lambda_n^2)^{-1}\`, so

\`\`\`math
\int_{I_n}\Omega(t)\,dt
\gtrsim
1-\frac{c_0}{R_n}.
\`\`\`

Consequently

\`\`\`math
\boxed{
\sum_n
\int_{I_n}\Omega(t)\,dt
=
\infty.
}
\`\`\`

Thus the exact conservative flux ledger satisfies finite A2 occupancy,
finite dissipation, bounded energy, and summable boundary-flux cost while the
L5-15 continuation residual remains nonintegrable.

## 10. What the fixture does and does not exclude

The fixture excludes the following generic implication:

\`\`\`text
A2 occupancy
+ Leray energy/dissipation
+ threshold orientation
+ exact fixed-band energy balance
+ conservative nearest-neighbour transfer
+ signed cumulative boundary flux
    =>
Omega in L1.
\`\`\`

It actually falsifies a stronger version in which the **absolute unweighted**
boundary-flux variation is also assumed summable.

This result is distinct from the L4 signed-decorrelation closure.

L4 showed that moving active selection destroys shell-flux telescoping and
that selector variation is uncontrolled.

L5-21 grants a selector-free fixed-band identity episode by episode and shows
that, even after internal transfer telescopes exactly, the resulting unweighted
boundary energy flux can be too cheap to control threshold overshoot.

The remaining opportunity is therefore not generic energy conservation.

## 11. Why frequency weighting is not imported for free

One might try to repair the fixture by weighting the boundary flux by the
active frequency.

For the present episode,

\`\`\`math
\lambda_n
\int|F_{m_n-1/2}|\,dt
\asymp
\lambda_nE_n
=
R_n^2,
\`\`\`

which is indeed large.

But no selected A2/Leray budget controls this weighted flux.

Introducing such a weight without a new PDE theorem simply replaces the cheap
energy flux by a frequency-weighted active quantity of the same general type
that caused the L4 weighted-column obstruction.

Therefore a successful frequency-weighted flux route must prove a genuinely
new Navier--Stokes estimate. It cannot assume the needed weight as part of the
ledger.

## 12. Next live obligation: C2-TRIAD

The generic cumulative band-energy route is terminated.

The smallest safe successor is an equation-specific triadic-coherence test.

The required question is:

> Does the actual Navier--Stokes triad geometry prevent an active shell from
> undergoing arbitrarily many turnover-scale overshoot episodes with only
> summable unweighted boundary energy flux?

A useful next tranche should keep a fixed finite frequency cluster and examine
the **time derivative of the transfer phase/correlation itself**, not merely
the shell energy.

Valid positive mechanisms include:

- a phase-decoherence time shorter than the overshoot recycling time;
- a lower bound on the creation of additional interacting triads;
- a signed transfer-correlation identity that cannot be represented by the
  conservative shell ledger;
- an equation-derived frequency-weighted flux estimate that does not reduce to
  the L4 active diagonal.

If the exact triad dynamics permits repeated turnover-scale recycling with no
additional non-summable cost, record that obstruction and move again.

## 13. Hard rejection tests

Reject any successor that:

- treats the shell-and-packet fixture as an NSE trajectory;
- claims generic shell conservation already controls \`\Omega\`;
- differentiates the moving selector;
- converts unweighted flux to frequency-weighted flux without a new estimate;
- treats the L4 weighted column as newly available;
- uses turnover residence as a reopening of L3;
- assumes a favorable flux sign from energy conservation alone;
- imports \`f\in L^1_t\`, an LPS norm, or uniform \`H^1\`.

## 14. Claim boundary

The protected claim sought from this tranche is exactly

\`\`\`text
C2_FLUX_GENERIC_BAND_ENERGY_ROUTE_TERMINATED
__OVERSHOOT_DIVERGES_WITH_SUMMABLE_BOUNDARY_FLUX.
\`\`\`

It proves a conservative shell-ledger obstruction to one cumulative C2-FLUX
variant.

It does not prove A2.

It does not prove that actual Navier--Stokes solutions realize the fixture.

It does not exclude equation-specific triadic phase coherence, dynamic
directionality, or a new frequency-weighted flux theorem.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
