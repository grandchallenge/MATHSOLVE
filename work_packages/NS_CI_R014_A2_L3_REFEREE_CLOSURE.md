# NS-CI-R014-A2-L3 — Referee closure of the excursion programme

## Decision

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Decision: `CLOSE_L3_AS_EXHAUSTED_UNDER_AUDITED_INTERFACES`
- Selected target `A2`: remains unproved and remains under investigation
- Successor lanes: `MATHSOLVE#58` and `MATHSOLVE#59`
- WP03: closed

The excursion-persistence programme is closed as a primary proof route. It produced several rigorous intermediate lemmas and exact obstruction results, but every audited charge ultimately reduces to a dyadically summable inverse-frequency cost or requires an unproved threshold buffer, low-mode Lipschitz bound, or anti-fragmentation law.

This is a route decision, not a statement that A2 is false.

## 1. Original target and reduction

The selected restricted target is

```math
\Lambda\in L^2(0,T)
\Longrightarrow
\int_0^T\|u(t)\|_6^4dt<\infty.
```

The first L3 result proved that a parabolic superlevel-persistence condition of the form

```math
|\{\Lambda\ge2^{k+1}\}|>0
\Longrightarrow
|\{\Lambda\ge2^k\}|\gtrsim2^{-2k}
```

would force `Lambda` to remain bounded under the assumed `L2_t` control. Thus any hypothetical failure must use increasingly high excursions with strictly sub-parabolic occupancy.

## 2. What the energy class supplies

The projected mild equation and Leray interpolation give relaxed-threshold persistence only on

```math
\delta_q
\lesssim
\min\left\{
\nu^{-1}\lambda_q^{-2},
\nu^7\|u_0\|_2^{-8}\lambda_q^{-6}
\right\}.
```

At fixed energy the nonlinear interval scales like `lambda_q^-6`, not the required `lambda_q^-2`. The estimate also preserves only a fixed fraction of the defining threshold.

For a localized forcing bound with frequency cost `lambda_q^alpha` and time exponent `r`, a parabolic estimate requires

```math
\alpha+2/r\le3.
```

The direct energy-class pair gives `4`, exposing one missing frequency power.

## 3. Interaction decomposition

The Bony and commutator audit recovered the derivative in the principal low–high transport term. The remaining low-mode deformation is governed by a Lipschitz coefficient whose energy estimate leaves a half-frequency-power deficit. Absolute high–high estimates reduce to the scale-invariant local quantity

```math
\mathcal E_q(I)
=
\frac{\lambda_q}{\nu}
\int_I\|\nabla u\|_2^2dt.
```

The energy inequality supplies no uniform smallness of this number on threshold boxes.

A stricter threshold wavenumber cannot be controlled from the original threshold and energy budgets alone; an explicit packet fixture separates the two thresholds.

## 4. Dynamic exit result

For a factor-two buffered exit with bounded finite-neighbour amplitude ratio `K`, the low-mode characteristic argument proved

```math
1
\lesssim
K\mathcal E_q(I)^{1/2}
+
\mathcal E_q(I).
```

Hence each rapid buffered exit has `mathcal E_q(I)>=epsilon_K`. Pairwise disjoint exits satisfy

```math
\sum_j\lambda_{q_j}^{-1}
\lesssim_K
\nu^{-2}\|u_0\|_2^2.
```

The weight `lambda_q^-1=2^-q` is summable, so the estimate permits one charged exit at every dyadic level.

## 5. Signed flux and tree bookkeeping

A threshold shell has only the energy floor

```math
\|u_q\|_2^2
\gtrsim
\nu^2\lambda_q^{-1}.
```

A same-annulus packet-splitting fixture can halve the shell supremum while nearly preserving its `L2` energy. Therefore amplitude exit does not impose a universal sign on shell-energy transfer. Taking absolute values destroys flux telescoping.

Moving cutoffs introduce explicit jump terms on the same inverse-frequency scale. A conservative-dissipative shell-chain fixture reaches all levels while preserving finite signed transfer, finite dissipation, and finite critical wavenumber occupancy.

## 6. Concentration and multiplicity

A threshold maximum produces a ball of radius `c lambda_q^-1` with local kinetic-energy floor

```math
\int_B|u_q|^2dx
\gtrsim
\nu^2\lambda_q^{-1}.
```

This is not additional energy; it is a localized form of the same shell-energy floor.

The dimensionless inverse-concentration functional

```math
M_q
=
\lambda_q^3\|u_q\|_2^2/\|u_q\|_\infty^2
```

is scale and translation invariant. A cluster version controls the finite-neighbour ratio, so bounded multiplicity yields a valid buffered residence-or-dissipation dichotomy. Its physical cost remains `nu^2 lambda_q^-1`.

Multiplicity may reset at the next scale. Packet splitting, threshold-compatible transfer, and short occupancy can be repeated across all dyadic levels with finite abstract budgets.

## 7. Exhausted interfaces

The following are closed as standalone A2 routes under the stated hypotheses:

1. direct energy-class temporal persistence;
2. absolute nonlinear forcing estimates;
3. robust comparison of threshold constants from energy alone;
4. local dissipation packing of rapid exits;
5. shell-energy and signed-flux telescoping;
6. moving-cutoff energy bookkeeping;
7. unrestricted frequency-tree packing;
8. static concentration balls;
9. bounded packet multiplicity;
10. fragmentation charged only by absolute transfer or low-mode deformation.

Each route either loses a required frequency power, assumes a missing threshold margin, or yields a summable inverse-frequency charge.

## 8. What would reopen L3

L3 may be reopened only if a new theorem supplies at least one of:

- actual parabolic residence at the defining threshold;
- a non-summable equation-derived cost for each newly reached scale;
- a cross-level coherence law preventing packet reset;
- an anti-fragmentation charge with a finite global budget;
- a threshold-cluster estimate independent of the low-mode regularity criterion.

Renaming the inverse-frequency energy floor or adding another absolute-value decomposition is not sufficient.

## 9. Pivot decision

The campaign pivots to two mathematically distinct lanes:

- **L4 weighted dissipation:** seek a scale-critical weighted coupling among `Lambda`, shell dissipation, and the low-mode coefficient;
- **L5 direct critical integral:** decompose `||u||_6^4` directly at the moving cutoff and seek an `L1_t` majorant without first proving the low-mode criterion.

L4 is the primary lane. L5 runs as an independent cross-check and must not silently reproduce L4 or the existing low-mode criterion.

## 10. Pedagogical standard for successor work

Every successor artifact must proceed in this order:

1. state the exact target and imported hypotheses;
2. define all quantities and active sets;
3. give a scaling table;
4. draw the proof-obligation DAG;
5. derive each inequality line by line;
6. list the known time-integrability class of every factor;
7. run adversarial counterfixtures before promotion;
8. separate proved lemmas, conditional interfaces, and failed routes;
9. conclude with a Referee disposition.

No claim may be promoted from a schematic inequality whose constants, cutoff dependence, or time exponents are unresolved.

## Claim boundary

This closure does not prove or disprove A2. It records that the excursion-persistence family has been investigated to the point where further variants require genuinely new dynamic information rather than further rearrangement of energy, flux, or packet geometry.