# NS-CI-R014-A2-L4-4 — Signed cancellation and active-diagonal decorrelation

## Status

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Tracker: `MATHSOLVE#58`
- Predecessor: `NS_CI_R014_A2_L4_WEIGHTED_COLUMN.md`
- Result: `PROVED_SELECTOR_IDENTITY_SIGNED_ROUTE_TERMINATED`
- L4 disposition: `EXHAUSTED_UNDER_AUDITED_INTERFACES`
- Successor: `MATHSOLVE#59`, direct critical-integral lane L5
- A2 status: unproved
- Numerical lane: closed

## 1. Exact obligation

L4-3 proved that the positive active-shell quantity

```math
S_Q(t)
=
\sum_{p\le Q(t)}
2^{-2(Q(t)-p)}\lambda_pD_p(t)
```

is not controlled by `Lambda in L2_t` and the Leray budgets. The obstruction is already present on the diagonal

```math
\mathfrak D_{\mathrm{diag}}
=
\sum_{q\ge0}\lambda_q
\int_{E_q}D_q(t)dt,
\qquad
E_q=\{t:Q(t)=q\}.
```

L4-4 asks whether the Navier–Stokes equation supplies one of the missing mechanisms:

1. signed shell or cumulative-flux cancellation;
2. a commutator or depletion identity removing the active diagonal;
3. a dynamic decorrelation estimate between `D_q` and `E_q`.

This package proves the exact selector-weighted shell identity, audits each mechanism, and constructs a conservative nearest-neighbour shell ledger satisfying the exact energy-transfer identities while retaining a divergent active diagonal. No non-circular L4 mechanism survives. L4 is therefore closed and L5 becomes the primary lane.

## 2. Fixed-shell energy identity

Use mutually orthogonal Fourier projections `P_q` for the exact energy ledger. For a smooth divergence-free Navier–Stokes solution, define

```math
e_q(t)=\frac12\|P_qu(t)\|_2^2,
```

```math
d_q(t)=\nu\|\nabla P_qu(t)\|_2^2,
```

and

```math
\mathcal T_q(t)
=-\langle P_q(u\cdot\nabla u),P_qu\rangle.
```

Then

```math
e_q'(t)+d_q(t)=\mathcal T_q(t).
```

The pressure term vanishes by divergence freedom, and the nonlinear transfer is conservative:

```math
\sum_q\mathcal T_q(t)=0.
```

The smooth Littlewood–Paley blocks used in the dissipation-wavenumber definition have finite overlap rather than exact orthogonality. They may be compared to this ledger with fixed overlap constants, but no exact telescoping is claimed for their raw shell energies.

For Leray–Hopf solutions, the identities are interpreted first on smooth Galerkin or mollified approximants and then passed to each fixed finite shell range.

## 3. Selector-weighted identity

Let

```math
\chi_q(t)=1_{E_q}(t),
\qquad
E_q=\{t\in U:Q(t)=q\}.
```

Suppose first that `chi_q` has bounded variation and `e_q` is absolutely continuous. Multiplying the shell identity by `chi_q` and applying Stieltjes integration by parts gives

```math
\int_0^T\chi_qd_qdt
=
\int_0^T\chi_q\mathcal T_qdt
+
\int_{(0,T)}e_qd\chi_q
-
[\chi_qe_q]_{0}^{T}.
```

Multiplying by `lambda_q` and summing gives the exact active-diagonal ledger

```math
\mathfrak D_{\mathrm{diag}}
=
\sum_q\lambda_q\int\chi_q\mathcal T_qdt
+
\sum_q\lambda_q\int e_qd\chi_q
-
\sum_q\lambda_q[\chi_qe_q]_{0}^{T}.
```

This formula has two independent obstructions:

1. the **selected transfer term** `sum_q lambda_q chi_q T_q` does not inherit `sum_q T_q=0`;
2. the **selector-variation term** requires weighted control of the entry and exit boundaries of the active sets.

If `chi_q` is not of bounded variation, the Stieltjes term is not a finite measure and the identity cannot be used as an estimate. The assumption `Lambda in L2_t` controls only

```math
\sum_q\lambda_q^2|E_q|,
```

not the temporal variation or number of components of `E_q`.

## 4. Why signed transfer does not telescope after active selection

At each time,

```math
\sum_q\mathcal T_q(t)=0.
```

But the active selector retains one weighted shell:

```math
\sum_q\lambda_q\chi_q(t)\mathcal T_q(t)
=
\lambda_{Q(t)}\mathcal T_{Q(t)}(t).
```

There is no cancellation with the transfers on nonselected shells. Replacing the selected transfer by its absolute value is even stronger and destroys every signed conservation law.

The same issue appears in the cumulative-flux formulation. If

```math
E_{\le q}=\frac12\|P_{\le q}u\|_2^2,
\qquad
D_{\le q}=\nu\|\nabla P_{\le q}u\|_2^2,
```

and

```math
\frac d{dt}E_{\le q}+D_{\le q}+\Pi_q=0,
```

then

```math
d_q=D_{\le q}-D_{\le q-1}
```

and

```math
\mathcal T_q=-(\Pi_q-\Pi_{q-1}).
```

Multiplication by `lambda_q chi_q` prevents telescoping in `q`, while integration over `E_q` creates the same selector-boundary terms. Thus fixed-cutoff flux telescoping does not become moving-active-shell decorrelation.

## 5. Selector variation is not controlled by occupancy

Assume for illustration that each `E_q` is a finite union of intervals `(a_{q,k},b_{q,k})`. Then

```math
\int e_qd\chi_q
=
\sum_k
\left(e_q(a_{q,k})-e_q(b_{q,k})\right).
```

The pointwise energy bound gives only

```math
0\le e_q(t)\le\frac12\|u_0\|_2^2.
```

Therefore the absolute weighted boundary ledger is bounded only by

```math
\frac12\|u_0\|_2^2
\sum_q\lambda_qN_q,
```

where `N_q` is the number of components of `E_q`. The `Lambda L2` hypothesis imposes no bound on this quantity.

The threshold lower bound is also unusable for an upper estimate. On an active threshold shell,

```math
e_q(t)\gtrsim\nu^2\lambda_q^{-1},
```

so

```math
\lambda_qe_q(t)\gtrsim\nu^2.
```

Consequently every threshold-compatible entry can carry a frequency-independent weighted jump. Infinitely many very short active intervals are compatible with finite `sum lambda_q^2 |E_q|`.

This is a variation obstruction, not an assertion that every Leray–Hopf dissipation wavenumber has infinite variation.

## 6. Threshold and commutator audit

The projected nonlinearity can be decomposed into low–high transport, near-shell interactions, and strictly high interactions. The principal low–high transport is removed along the low-mode flow, leaving a commutator coefficient

```math
G_q(t)=\|\nabla u_{\le q-2}(t)\|_\infty.
```

A standard commutator estimate has the form

```math
|\mathcal T_q^{LH}(t)|
\lesssim
G_q(t)e_q(t).
```

The strict high-mode threshold may be used only for shells `p>Q(t)`. Even granting absorption of every strictly high contribution by viscosity, the active shell `q=Q(t)`, its lower neighbours, the coefficient `G_q`, and near-shell transfer remain uncontrolled.

Any estimate of the schematic form

```math
|\mathcal T_q|
\le
\varepsilon d_q
+
C G_qe_q
+
\text{near-shell terms}
```

therefore leaves quantities whose time control is at least as strong as the previously audited low-mode or neighbour-cluster criteria. It does not produce decorrelation between `d_q` and `E_q` from `Lambda in L2_t`.

In particular:

- using the strict threshold at `q=Q` is invalid;
- bounding `G_q` by an imported integrable coefficient is circular;
- taking absolute values of near-shell transfer destroys signed cancellation;
- the shell identity alone does not force active-shell depletion.

## 7. Conservative nearest-neighbour shell fixture

The L4-3 packet boxes can be upgraded to satisfy exact energy balance and a conservative nearest-neighbour flux ledger.

Let

```math
\lambda_q=2^q,
```

and choose disjoint plateau intervals `I_q` of lengths

```math
\tau_q
=
\frac{\lambda_q^{-5/2}}{q+1}.
```

Choose smooth nonnegative bump functions `h_q` supported in slightly larger disjoint windows, equal to one on `I_q`, and with disjoint supports. Let `E_*>0` be small and set

```math
e_q(t)=E_*h_q(t),
```

```math
d_q(t)=c_d\nu\lambda_q^2e_q(t),
```

for the active shell. All intermediate shells have zero energy and dissipation. Introduce a reservoir shell `0` with energy `e_0(t)` and zero dissipation.

For each active window define the signed nearest-neighbour flux across every edge from shell `0` to shell `q` by

```math
F_{p+1/2}(t)
=e_q'(t)+d_q(t),
\qquad 0\le p<q.
```

The shell balances are

```math
e_0'(t)=-F_{1/2}(t),
```

```math
e_p'(t)+d_p(t)
=F_{p-1/2}(t)-F_{p+1/2}(t)=0,
\qquad 1\le p<q,
```

and

```math
e_q'(t)+d_q(t)=F_{q-1/2}(t).
```

Thus every window obeys exact local conservation and the total nonlinear transfer sums to zero. Since `h_q` returns to zero,

```math
\int F_{p+1/2}(t)dt
=
\int d_q(t)dt.
```

The reservoir loses only total physical dissipation. Because

```math
\sum_q\int d_qdt
\asymp
\nu E_*
\sum_q\frac{\lambda_q^{-1/2}}{q+1}
<\infty,
```

`e_0(0)` may be chosen so that all shell energies remain nonnegative and the total kinetic-energy budget remains bounded.

Attach to shell `q` an `L2`-normalized divergence-free annular packet as in L4-3. For sufficiently large `q`, its plateau amplitude satisfies the dissipation-wavenumber threshold and hence `Q=q` on `I_q`. Then

```math
\int\Lambda^2dt
\asymp
\sum_q\lambda_q^2\tau_q
=
\sum_q\frac{\lambda_q^{-1/2}}{q+1}
<\infty,
```

while

```math
\sum_q\lambda_q\int_{I_q}d_qdt
\asymp
\nu E_*
\sum_q\frac{\lambda_q^{1/2}}{q+1}
=\infty.
```

The fixture satisfies:

1. bounded pointwise total energy;
2. finite total dissipation;
3. finite `Lambda L2` occupancy;
4. exact shell energy identities;
5. instantaneous conservation of signed transfer;
6. nearest-neighbour flux locality;
7. the threshold relation on each plateau;
8. divergent active-diagonal weighted dissipation.

It is an algebraic shell-and-packet fixture, not a Navier–Stokes solution. It proves that shell energy balance, signed conservation, and local transfer structure do not by themselves yield the missing decorrelation estimate.

## 8. Dynamic decorrelation is the missing theorem, not a deduction

The desired estimate is

```math
\sum_q\lambda_q
\int_{E_q}D_q(t)dt
<\infty.
```

After L4-3 and the selector identity, a statement such as

```math
\int_{E_q}D_q(t)dt
\le
C\lambda_q^{-1}a_q,
\qquad
\sum_qa_q<\infty,
```

would close the diagonal. But no such estimate follows from occupancy, energy, fixed-shell balance, transfer conservation, or strict-high-mode smallness.

Calling this a “decorrelation hypothesis” is mathematically legitimate, but it is a new conditional regularity criterion. Without a separately proved Navier–Stokes mechanism, it merely restates the L4 obstruction.

## 9. Reopening conditions

L4 may be reopened only if one of the following is supplied with a complete proof:

1. **Active-set variation theorem:** a frequency-uniform bound on the weighted variation of `1_{Q=q}` or on the boundary energy ledger;
2. **Selected-transfer cancellation:** an identity controlling `sum lambda_q 1_{Q=q} T_q` without absolute values and without moving-cutoff jump loss;
3. **Active-diagonal depletion:** a PDE estimate giving a genuine gain over `lambda_q int_{E_q}D_q`;
4. **Non-circular commutator estimate:** an integrable coefficient derived from `Lambda L2` and Leray data, not from `f`, `G_q`, an LPS norm, or uniform `H1`;
5. **Triadic decorrelation theorem:** a quantitative restriction on the correlation of shell dissipation with the event `Q=q` that excludes the nearest-neighbour fixture through an actual Navier–Stokes identity.

A new positive kernel, a renamed Carleson norm, or numerical evidence does not reopen L4.

## 10. Proof-obligation DAG

```text
L4-4.1 fixed shell and cumulative energy identities
    PROVED
        |
        v
L4-4.2 active-selector integration by parts
    PROVED
        |
        +----------------------------+
        |                            |
        v                            v
selected signed transfer       selector boundary ledger
NO TELESCOPING                 NO VARIATION CONTROL
        |                            |
        +-------------+--------------+
                      |
                      v
L4-4.3 strict-high threshold / commutator audit
    ACTIVE DIAGONAL AND LOW/NEAR COEFFICIENTS SURVIVE
                      |
                      v
L4-4.4 exact conservative local-flux fixture
    PROVED_COUNTERFIXTURE
                      |
                      v
L4 equation-specific route
    EXHAUSTED UNDER AUDITED INTERFACES
                      |
                      v
L5 direct critical-integral lane
    PROMOTED PRIMARY
```

## 11. Route disposition

| Candidate | Disposition | Exact reason |
|---|---|---|
| fixed-shell signed transfer | proved identity | active selector destroys global cancellation |
| cumulative flux telescoping | terminated for L4 | moving selector and shell weight create boundary terms |
| active-set integration by parts | proved identity | requires uncontrolled weighted variation of `Q` |
| strict-high absorption | insufficient | threshold excludes the active shell and lower neighbours |
| low–high commutator | circular as closure | coefficient `G_q` is not controlled by selected data |
| near-shell depletion | unproved | no sign or smallness at `q=Q` |
| dynamic decorrelation from shell balance | rejected | conservative nearest-neighbour fixture violates it |
| decorrelation as added hypothesis | conditional/tautological | equivalent to the missing diagonal bound |
| L4 weighted dissipation programme | exhausted | no non-circular equation-specific mechanism survives |
| L5 direct critical integral | promoted | genuinely different target representation remains open |

## 12. Referee decision

L4 produced two useful exact results:

1. the pointwise weighted envelope

```math
f
\le
C\|u_0\|_2
+C\nu^{-1/2}\Lambda S_Q^{1/2};
```

2. the precise identification of the active diagonal as the missing correlation.

It also proved that positive kernels, ordinary Schur estimates, fixed-shell signed conservation, moving-cutoff telescoping, and generic shell-local flux identities do not control that diagonal under the selected assumptions.

The lane is therefore **complete but unsuccessful as an A2 proof**. Further work inside L4 would require a new theorem not presently generated by the source-normalized interfaces. The programme should now execute L5 rather than iterate equivalent weighted-dissipation formulations.

## 13. Immediate successor obligation

Promote issue `MATHSOLVE#59` to the primary lane and execute:

```text
L5-0  normalize the target and constants
L5-1  prove the exact Littlewood–Paley L6 representation used
L5-2  derive the moving low/high split with all diagonal,
      off-diagonal, near-threshold, and strict-tail exponents explicit
```

The L5 proof may use the L4 counterfixtures as adversarial tests, but it may not import `f in L1` or rename the active diagonal.

## Claim boundary

This package closes the audited L4 programme, not the mathematical possibility of every future equation-specific weighted estimate. It does not construct a Navier–Stokes counterexample, disprove A2, or prove the critical integral finite.