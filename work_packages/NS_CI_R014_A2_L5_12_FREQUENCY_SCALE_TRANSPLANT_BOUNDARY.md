# NS-CI-R014-A2-L5-12 — Frequency--scale transplant boundary

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected base: `499a521870d01aecc9b5ddad8c7db291b999263a`
- Predecessor: `NS-CI-R014-A2-L5-11`
- Governing handoff: `NS_CI_R014_A2_L5_10_FIELD_CALIBRATION_FREQUENCY_SCALE_HANDOFF.md`
- C3 result: `SOURCE_TWO_INDEX_KERNEL_CONFIRMED__DIRECT_CHEMIN_LERNER_IMPORT_BLOCKED_BY_ACTIVE_DIAGONAL`
- A2 theorem: open
- L5: active
- C3: active, narrowed
- MATHCERT adjudication: absent
- Evidence class: exact source-mechanism audit plus algebraic/scaling obstruction; **not** a PDE counterexample

This package executes the first bounded tranche of C3.  It answers a narrower question before attempting a new local-energy proof:

> Can the Guo--Wang--Xiong frequency--scale kernel be imported directly, with its source coefficient sequence controlled from A2 plus the Leray energy class?

The answer is **no**.  The two-index mechanism itself is genuine and survives audit, but the published recursion consumes an `ell^1` sequence of critical dyadic component norms.  A2 plus the Leray budgets do not imply that sequence, and the diagonal `K_0=1` means the off-diagonal kernel cannot manufacture the missing summability.

This does **not** close C3.  It identifies the exact object that must be replaced in the next tranche.

## 1. Primary source and exact mechanism

Primary source:

Maotuo Guo, Wendong Wang, and Shiyang Xiong,
*A Critical Chemin--Lerner Regularity Criterion via One Velocity Component for the Three-Dimensional Navier--Stokes Equations*, arXiv:2609.03877v1, submitted 3 September 2026.

- `https://arxiv.org/abs/2609.03877`
- `https://arxiv.org/pdf/2609.03877`

Fix

```math
2<p<\infty,
\qquad
m=\frac{3p}{p-2}>3,
\qquad
\frac2p+\frac3m=1.
```

The source defines

```math
a_j
:=
\|\dot\Delta_j u^3\|_{L^p_tL^m_x}
```

and assumes

```math
\sum_{j\in\mathbb Z} a_j<\infty.
```

After introducing a physical observation index `k` independently of the dyadic frequency `j`, the paper derives the two-sided kernel

```math
K_d=
\begin{cases}
2^{-d/m}, & d\ge L,\\
1, & |d|<L,\\
2^d, & d\le-L,
\end{cases}
```

and

```math
B_k=\sum_{j\in\mathbb Z}K_{k-j}a_j.
```

The three ranges have distinct origins:

1. `j << k`: the thin physical slab gives `2^{-(k-j)/m}`;
2. `|j-k|<L`: no scale gain is asserted;
3. `j >> k`: self-adjoint transfer of the annular projection to the localized flux, followed by inverse Bernstein, gives `2^{-(j-k)}`.

For spatially separated pressure sources, harmonic decay supplies an additional one-sided convolution in the physical scale.  The local-energy recursion eventually has coefficient sequence built from `B_j` and that pressure convolution.

The mechanism therefore passes the first C3 hard test: frequency and physical scale really are kept independent until after the gains are derived.  It is not the already-closed scale-neutral direct-L6 commutator estimate.

## 2. Exact kernel facts

### Lemma 2.1 — two-sided summability

For every `m>0` and fixed integer `L>=1`,

```math
K\in\ell^1(\mathbb Z).
```

Indeed,

```math
\sum_{d\ge L}2^{-d/m}<\infty,
\qquad
\sum_{d\le-L}2^d<\infty,
```

and the central band contains only finitely many terms.

Hence, for every nonnegative `a in ell^1`, discrete Young/Tonelli gives

```math
\sum_k B_k
\le
\|K\|_{\ell^1}\sum_j a_j.
```

This is the positive part of the field-development transplant.

### Lemma 2.2 — the diagonal cannot improve source summability

The same kernel satisfies

```math
K_0=1.
```

Therefore, for every nonnegative sequence,

```math
B_k\ge a_k.
```

Consequently,

```math
\sum_{k\ge k_0}a_k=\infty
\quad\Longrightarrow\quad
\sum_{k\ge k_0}B_k=\infty.
```

Thus the two-sided off-diagonal decay can redistribute an already summable critical source sequence, but it cannot turn a nonsummable diagonal source sequence into the `ell^1` coefficient tail required by the source recursion.

This is the decisive distinction for A2.

## 3. What the Leray class gives at the critical source norm

Let

```math
D_j
:=
\nu\int_I \lambda_j^2\|u_j(t)\|_2^2\,dt,
```

so that the Leray dissipation budget gives

```math
\sum_j D_j<\infty.
```

Let

```math
U_0:=\|u\|_{L^\infty_tL^2_x}.
```

Bernstein on a `lambda_j` shell and the critical relation give

```math
\|u_j(t)\|_m
\lesssim
\lambda_j^{3(1/2-1/m)}\|u_j(t)\|_2
=
\lambda_j^{1/2+2/p}\|u_j(t)\|_2.
```

Therefore

```math
a_j^p
\lesssim
\lambda_j^{p/2+2}
\int_I\|u_j(t)\|_2^pdt.
```

Using the energy supremum for `p-2` powers and the shell dissipation for the remaining two gives

```math
a_j^p
\lesssim
U_0^{p-2}\nu^{-1}\lambda_j^{p/2}D_j,
```

hence

```math
\boxed{
a_j
\lesssim
U_0^{1-2/p}\nu^{-1/p}\lambda_j^{1/2}D_j^{1/p}.
}
```

The factor `lambda_j^(1/2)` is the exact half-derivative gap between the energy interpolation line

```math
\frac2r+\frac3s=\frac32
```

and the critical source line

```math
\frac2p+\frac3m=1.
```

Neither `sum D_j<infinity` nor A2 removes this factor by a scalar interpolation argument.

## 4. A2 level-set information does not supply the missing half derivative

Let

```math
A_j:=\{t:Q(t)\ge j\}.
```

On `A_j`,

```math
\Lambda(t)\ge\lambda_j.
```

Therefore A2 implies the Chebyshev bound

```math
|A_j|
\le
\lambda_j^{-2}\int_I\Lambda(t)^2dt.
```

If one uses only this measure gain and the energy supremum, then

```math
\|1_{A_j}u_j\|_{L^p_tL^m_x}
\lesssim
U_0\lambda_j^{1/2+2/p}|A_j|^{1/p}
\lesssim
U_0
\left(\int_I\Lambda^2\right)^{1/p}
\lambda_j^{1/2}.
```

The `lambda_j^(2/p)` time-frequency factor is exactly canceled by the A2 level-set measure, leaving the same `lambda_j^(1/2)` deficit.

This estimate is not claimed sharp.  The point is narrower: the two obvious scalar resources, Leray dissipation and A2 residence measure, do not produce the source's `ell^1` critical sequence.

## 5. Exact packet fixture separating A2 from the source hypothesis

The non-implication is not merely an artefact of the preceding upper bounds.

Fix any `p>2`, put `m=3p/(p-2)`, and let

```math
\lambda_j=2^j,
\qquad
b_j=j^{-p},
\qquad
\mu_j=b_j\lambda_j^{-2},
\qquad j\ge2.
```

Choose pairwise disjoint time intervals `I_j` of length `mu_j`.  On `I_j`, consider one ideal dyadic packet at shell `j`, with threshold-scale amplitude

```math
\|u_j\|_\infty\asymp\nu\lambda_j,
\qquad
\|u_j\|_2^2\asymp\nu^2\lambda_j^{-1},
```

and no higher-frequency packet.  These scalings are realized by a fixed annular Schwartz packet under

```math
u_j(x)=\nu\lambda_j\phi(\lambda_jx)
```

up to harmless fixed constants and finite neighboring-shell leakage.  The fixture is used only as an algebraic/scaling falsifier; it is **not** asserted to solve Navier--Stokes.

The selector can be normalized so that `Q=j+O(1)` on `I_j`; fixed index shifts do not change any convergence statement below.

### 5.1 A2 budget

```math
\int\Lambda^2dt
\asymp
\sum_j\lambda_j^2\mu_j
=
\sum_j b_j
=
\sum_j j^{-p}
<\infty.
```

### 5.2 Energy and Leray dissipation budgets

The kinetic-energy supremum is finite because

```math
\|u_j\|_2^2\asymp\nu^2 2^{-j}.
```

The integrated shell dissipation is

```math
\nu\sum_j\lambda_j^2\|u_j\|_2^2\mu_j
\asymp
\nu^3\sum_j\lambda_j\mu_j
=
\nu^3\sum_j j^{-p}2^{-j}
<\infty.
```

Thus the scalar A2, energy, and dissipation budgets all converge.

### 5.3 The desired packet-tail quantity is also finite

At the active packet,

```math
S_1(t)\asymp\nu^2\lambda_j^2.
```

Hence

```math
\int S_1(t)dt
\asymp
\nu^2\sum_j\lambda_j^2\mu_j
=
\nu^2\sum_jj^{-p}
<\infty.
```

Likewise

```math
\int f(t)dt
\asymp
\nu\sum_j\lambda_j^2\mu_j
<\infty.
```

So this fixture is deliberately **not** an obstruction to the L5-10 successor target.  It isolates only the mismatch between that target and the stronger source hypothesis.

### 5.4 The Guo--Wang--Xiong source sequence diverges

For a frequency-`lambda_j` rescaling of a fixed packet,

```math
\|u_j^3\|_m
\asymp
\nu\lambda_j^{1-3/m}
=
\nu\lambda_j^{2/p}.
```

Therefore

```math
a_j
=
\|1_{I_j}u_j^3\|_{L^p_tL^m_x}
\asymp
\nu\lambda_j^{2/p}\mu_j^{1/p}
=
\nu b_j^{1/p}
=
\frac{\nu}{j}.
```

Thus

```math
\sum_j a_j=\infty.
```

Since `B_j>=a_j`, the physical-scale coefficient sequence generated by the unmodified source kernel also has divergent `ell^1` tail.

We have therefore proved the scalar non-implication

```text
A2 + Leray budgets + even finite integral S_1
DO NOT imply
sum_j ||Delta_j u^3||_{L^p_t L^m_x} < infinity.
```

Again, this is an algebraic/scaling fixture, not an NSE trajectory.  Its role is to reject an invalid proof implication, not to falsify A2.

## 6. Pressure mechanism survives the audit but does not repair the diagonal

The source pressure argument is also genuinely frequency--scale sensitive.  It spatially separates remote pressure sources before applying harmonic decay.  For source scale `j` observed at a much thinner slab `k`, the paper obtains a factor of the form

```math
2^{-\gamma(k-j)},
\qquad \gamma>0,
```

before summing source scales.

This passes the C3 pressure hard test: it is not a global scale-neutral Calderon--Zygmund estimate performed before spatial separation.

However, the resulting pressure coefficient is a further positive convolution of the already-defined `B_k`.  Positive off-diagonal convolution cannot remove the unsummed `K_0 a_k` diagonal.  Therefore pressure harmonicity is useful only after a campaign-controlled replacement for the diagonal source amplitude has been found.

## 7. What C3 has gained

This tranche changes the C3 state in three precise ways.

First, the field-development mechanism is validated as genuinely distinct:

```text
LOW frequency  -> physical slab thickness gain,
HIGH frequency -> transferred projection + inverse Bernstein gain,
FAR pressure   -> source/observer separation + harmonic decay.
```

Second, the exact two-sided kernel is now known and can be reused:

```math
K_{k-j}
\sim
\begin{cases}
2^{-(k-j)/m}, & j\ll k,\\
1, & |j-k|=O(1),\\
2^{-(j-k)}, & j\gg k.
\end{cases}
```

Third, the direct transplant is terminated for a specific reason:

```text
THE SOURCE ell^1 COEFFICIENT IS NOT AN A2/LERAY CONSEQUENCE,
AND K_0=1 LEAVES THAT DEFICIT ON THE FREQUENCY--PHYSICAL-SCALE DIAGONAL.
```

This is not the old scale-neutral commutator obstruction.  The new off-diagonal gains are real; the surviving problem is the central finite-width diagonal.

## 8. Next live obligation: C3-DIAG

The next tranche should **not** try to prove the source Chemin--Lerner hypothesis from A2.  That route is now rejected.

The live target is instead:

> Derive a campaign-specific source amplitude `c_{j,k}` for the localized energy/pressure flux such that the same off-diagonal geometry is retained, while the central band `|j-k|<L` is controlled directly by A2/Leray/strict-high structure or by a new signed/local cancellation.

Three variants remain legitimate.

1. **Shifted observation scale.** Keep `j` and `k` independent and test whether choosing the physical scale strictly finer than the active frequency scale moves the uncontrolled active packet into the low-frequency side where the slab factor is available. Any such choice must still yield a continuation-relevant local-energy quantity; a fixed arbitrary shift is not enough merely because it changes a constant.
2. **Diagonal renormalization.** Replace the source's critical component amplitude by a normalized threshold defect or an energy-flux amplitude whose diagonal is A2/Leray controlled. The new quantity must be derived from the local energy identity, not assumed.
3. **Signed diagonal cancellation.** Preserve the exact localized convection/pressure pairing through the central band and test whether a cancellation survives that is destroyed by the source's absolute `a_j` norm.

Hard rejection tests remain in force:

- do not set `j=k` before deriving the off-diagonal gains;
- do not reintroduce a selector derivative;
- do not replace the pressure separation by a global CZ estimate;
- do not use `sum a_j<infinity` or any equivalent Chemin--Lerner assumption as though A2 implied it;
- do not claim a scalar packet fixture is an NSE counterexample;
- reject constants depending on a terminal frequency cutoff.

## 9. Claim boundary

The protected result sought from this file is

```text
SOURCE_TWO_INDEX_KERNEL_CONFIRMED__DIRECT_CHEMIN_LERNER_IMPORT_BLOCKED_BY_ACTIVE_DIAGONAL.
```

It is an exact mechanism/reduction result.  It does not prove or disprove A2, does not establish the high-`Lambda` `S_1` tail theorem, and does not reopen any previously closed L3/L4/B4 route.  C3 remains active at `C3-DIAG`.
