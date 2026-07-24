# NS-CI-R014-A2-L4-0/2 — Source, scaling, and active-shell envelope

## Status

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Tracker: `MATHSOLVE#58`
- Obligations: `L4-0`, `L4-1`, `L4-2`
- Result: `PROVED_SOURCE_NORMALIZATION_AND_WEIGHTED_ENVELOPE`
- Sufficiency for A2: no
- Numerical lane: closed

This artifact reconstructs the exact whole-space definitions used by Cheskidov–Shvydkoy, restores the viscosity and energy factors suppressed by source comparison notation, verifies Navier–Stokes scaling and physical dimensions, and proves the first weighted active-shell envelope.

The output is the correct starting point for `L4-3`. It does not yet control the time integral of the weighted dissipation kernel.

## 1. Primary source

The source is:

> A. Cheskidov and R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944v2; J. Math. Fluid Mech. 16 (2014), 263–273.

The relevant source locations are:

| Source item | Location |
|---|---|
| inhomogeneous Littlewood–Paley blocks | Section 2 |
| dissipation wavenumber | equation (5) |
| threshold-shell lower bound | equation (6) |
| low-mode coefficient `f` | immediately after equation (6) |
| regularity from `f in L1` | Theorem 3.1 and Corollary 3.3 |
| source envelope `Lambda^2 lesssim f lesssim Lambda^(5/2)` | equation (14) |
| active set and threshold relation | equation (15) |
| `Lambda in L1` for Leray–Hopf solutions | Lemma 4.1 |

The proof of Lemma 4.1 contains a printed set expression `U=[0,T] union {Lambda>1}`. The preceding definition and the subsequent integrals show that the intended set is

```math
U=[0,T]\cap\{t:\Lambda(t)>1\}
 =\{t\in[0,T]:\Lambda(t)>1\}.
```

This artifact uses the intended active set and records the source typo rather than propagating it.

## 2. Littlewood–Paley conventions

Let

```math
\lambda_q=2^q,
\qquad q\ge-1,
```

and let `Delta_q` be the source's inhomogeneous Littlewood–Paley projection:

```math
u_q=\Delta_qu,
\qquad
u_{\le Q}=\sum_{q\le Q}u_q.
```

The block `q=-1` is supported in a fixed low-frequency ball. Blocks `q>=0` are supported in fixed-width annuli. Consequently:

```math
\|\nabla u_q\|_2\simeq\lambda_q\|u_q\|_2,
\qquad q\ge0,
```

with constants depending only on the fixed partition. The lower block must be handled separately whenever annular equivalence is used.

The source defines the inhomogeneous Besov norm by

```math
\|v\|_{B^s_{p,\infty}}
=
\sup_{q\ge-1}\lambda_q^s\|v_q\|_p.
```

Finite overlap of the smooth multipliers changes exact equalities involving a projected partial sum only by partition-dependent constants. To avoid ambiguity, the shell formula below is taken as the operational definition of `f`.

## 3. Exact dissipation-wavenumber definition

For viscosity `nu>0`, define

```math
Q(t)
=
\min\left\{
q\ge0:
\lambda_p^{-1}\|u_p(t)\|_\infty<c_0\nu
\text{ for every }p>q
\right\},
```

and

```math
\Lambda(t)=\lambda_{Q(t)}.
```

If the defining set is empty, set `Q(t)=infinity` and `Lambda(t)=infinity`. For Leray–Hopf solutions, the source proves `Lambda(t)<infinity` for almost every time.

### 3.1 What the definition controls

For every finite `Q(t)`,

```math
\lambda_p^{-1}\|u_p(t)\|_\infty<c_0\nu,
\qquad p>Q(t).
```

This is a strict-high-mode upper bound. It gives no upper bound for `p=Q(t)` or for lower shells.

### 3.2 Minimality and the threshold shell

Assume `Q(t)>=1`. Since `Q(t)-1` is not admissible, there is a shell `p>Q(t)-1` violating the strict inequality. All shells `p>Q(t)` satisfy it, so the violating shell must be `p=Q(t)`. Therefore

```math
\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu\Lambda(t).
```

Equivalently,

```math
\lambda_{Q(t)}\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu\Lambda(t)^2.
```

This is a lower bound, not a buffered event and not an upper threshold estimate.

## 4. Active and inactive times

Define

```math
U
=
\{t\in[0,T]:\Lambda(t)>1\}
=
\{t:Q(t)\ge1\}.
```

On `U`, the threshold-shell lower bound holds almost everywhere.

On the inactive set `U^c`, one has `Q(t)=0`, hence `f` contains only the fixed low block and shell zero. Bernstein at the fixed unit scale gives

```math
f(t)\lesssim\|u(t)\|_2
\le\|u_0\|_2,
\qquad t\in U^c.
```

Therefore

```math
\int_{U^c}f(t)dt
\lesssim
T\|u_0\|_2.
```

The critical problem is entirely on `U`.

## 5. Exact low-mode coefficient

The source coefficient is

```math
f(t)
=
\|u_{\le Q(t)}(t)\|_{B^1_{\infty,\infty}}
:=
\sup_{-1\le p\le Q(t)}
\lambda_p\|u_p(t)\|_\infty.
```

Using vorticity `omega=curl u` and annular multiplier equivalence,

```math
f(t)
\simeq
\|\omega_{\le Q(t)}(t)\|_{B^0_{\infty,\infty}},
```

up to constants depending only on the partition.

Corollary 3.3 of the source states that a Leray–Hopf solution is regular on `(0,T]` if

```math
f\in L^1(0,T).
```

Thus L4 must prove time integrability of the shell supremum, not of an unweighted shell sum.

## 6. Restored source envelope

The source writes, using comparison notation with viscosity and the energy bound fixed,

```math
\Lambda^2\lesssim f\lesssim\Lambda^{5/2}
\qquad\text{on }U.
```

The fully normalized inequalities are

```math
c_0\nu\Lambda(t)^2
\le
f(t)
\le
C_{LP}\|u(t)\|_2\Lambda(t)^{5/2}
\le
C_{LP}\|u_0\|_2\Lambda(t)^{5/2}.
```

### Proof of the lower bound

The shell `Q(t)` appears in the supremum defining `f`, and minimality gives

```math
f(t)
\ge
\lambda_{Q(t)}\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu\Lambda(t)^2.
```

### Proof of the upper bound

For every `p<=Q(t)`, Bernstein gives

```math
\lambda_p\|u_p(t)\|_\infty
\le
C_{LP}\lambda_p^{5/2}\|u_p(t)\|_2
\le
C_{LP}\Lambda(t)^{5/2}\|u(t)\|_2.
```

Taking the supremum yields the result.

The missing half power is now explicit:

```math
\Lambda^2
\quad\text{versus}\quad
\Lambda^{5/2}.
```

## 7. Scaling and dimensions

### 7.1 Physical dimensions

Use

```math
[x]=L,
\qquad
[t]=T,
\qquad
[u]=L/T,
\qquad
[\nu]=L^2/T,
\qquad
[\lambda]=L^{-1}.
```

Then

| Quantity | Physical dimension |
|---|---:|
| `Lambda` | `L^-1` |
| `lambda_p ||u_p||_infinity` | `T^-1` |
| `f` | `T^-1` |
| `nu Lambda^2` | `T^-1` |
| `D_p=nu||grad u_p||_2^2` | `L^5 T^-3` |
| `nu^-2 lambda_p D_p` | `T^-1` |

This corrects a schematic ambiguity in the pivot document: a pointwise term `lambda_p D_p` has the correct Navier–Stokes homogeneity but not the same physical dimension as `f`. The dimensionally normalized weighted term is

```math
\nu^{-2}\lambda_pD_p.
```

### 7.2 Navier–Stokes scaling

Under

```math
u_\rho(x,t)=\rho u(\rho x,\rho^2t),
```

viscosity remains fixed. For exact shell-index covariance, take a dyadic scale `rho=2^m`. Then

```math
Q_\rho(t)=Q(\rho^2t)+m,
\qquad
\Lambda_\rho(t)=\rho\Lambda(\rho^2t).
```

For corresponding shells,

```math
\|(u_\rho)_p(t)\|_\infty
=
\rho\|u_{p-m}(\rho^2t)\|_\infty,
```

```math
\|(u_\rho)_p(t)\|_2
=
\rho^{-1/2}\|u_{p-m}(\rho^2t)\|_2,
```

and

```math
D_p[u_\rho](t)
=
\rho D_{p-m}[u](\rho^2t).
```

Hence

| Quantity | Scaling factor |
|---|---:|
| `dt` | `rho^-2` |
| `Lambda`, `lambda_p` | `rho` |
| `f` | `rho^2` |
| `nu Lambda^2` | `rho^2` |
| `D_p` | `rho` |
| `lambda_p D_p` | `rho^2` |
| `nu^-2 lambda_p D_p` | `rho^2` |
| `f dt` | invariant |
| `Lambda^2 dt` | invariant |
| `nu^-2 lambda_p D_p dt` | invariant |

The inhomogeneous base block is not exactly scale covariant when a rescaling crosses the fixed unit cutoff. It is already controlled as an integrable remainder and is excluded from the critical kernel calculation.

## 8. Shell dissipation density

For annular shells `p>=0`, define

```math
D_p(t)
=
\nu\|\nabla u_p(t)\|_2^2.
```

Annular equivalence gives

```math
D_p(t)
\simeq
\nu\lambda_p^2\|u_p(t)\|_2^2.
```

Almost orthogonality and the Leray energy inequality yield

```math
\sum_{p\ge0}\int_0^TD_p(t)dt
\lesssim
\|u_0\|_2^2.
```

No pointwise bound on `sum_p D_p(t)` and no bound on

```math
\sum_p\int_0^T\lambda_pD_p(t)dt
```

is imported.

## 9. L4-2: exact active-shell decomposition

Set

```math
a_p(t)=\lambda_p\|u_p(t)\|_\infty.
```

On `U`, decompose

```math
f(t)
=
\max\left\{
 a_{-1}(t),
 \sup_{0\le p\le Q(t)}a_p(t)
\right\}.
```

The base-shell term satisfies

```math
a_{-1}(t)\lesssim\|u_0\|_2.
```

For a fixed integer `J>=0`, define the far and near envelopes

```math
f_{\mathrm{far}}^{(J)}(t)
=
\sup_{0\le p\le Q(t)-J-1}a_p(t),
```

and

```math
f_{\mathrm{near}}^{(J)}(t)
=
\max_{\max(0,Q(t)-J)\le p\le Q(t)}a_p(t).
```

An empty supremum is zero. Then

```math
f(t)
\le
C\|u_0\|_2
+
f_{\mathrm{far}}^{(J)}(t)
+
f_{\mathrm{near}}^{(J)}(t).
```

The near cluster has at most `J+1` shells. The far region has infinitely many possible shells as `Q` grows, but gains a geometric ratio relative to `Lambda`.

## 10. Weighted shell-envelope lemma

### Lemma `NS-CI-A2-L4-Lemma-1`

For almost every `t in U`, define

```math
S_Q(t)
=
\sum_{p=0}^{Q(t)}
2^{-2(Q(t)-p)}\lambda_pD_p(t).
```

Then

```math
f(t)
\le
C_{LP}\|u_0\|_2
+
C_{LP}\nu^{-1/2}\Lambda(t)S_Q(t)^{1/2}.
```

Consequently, for every `epsilon>0`,

```math
f(t)
\le
C_{LP}\|u_0\|_2
+
\epsilon\nu\Lambda(t)^2
+
C_{LP}\epsilon^{-1}\nu^{-2}S_Q(t).
```

### Proof

For `p>=0`, Bernstein and annular equivalence give

```math
a_p(t)^2
\le
C_{LP}\lambda_p^5\|u_p(t)\|_2^2
\le
C_{LP}\nu^{-1}\lambda_p^3D_p(t).
```

Since `Lambda=lambda_Q`, the exact dyadic identity

```math
\lambda_p^3
=
\Lambda^2
2^{-2(Q-p)}\lambda_p
```

holds for `p<=Q`. Therefore

```math
a_p(t)^2
\le
C_{LP}\nu^{-1}\Lambda(t)^2
2^{-2(Q(t)-p)}\lambda_pD_p(t).
```

Taking the supremum and using `sup b_p <= sum b_p` for nonnegative terms yields

```math
\sup_{0\le p\le Q}a_p(t)^2
\le
C_{LP}\nu^{-1}\Lambda(t)^2S_Q(t).
```

Taking square roots and restoring the base-shell remainder proves the first inequality. Young's inequality with

```math
A=\nu^{1/2}\Lambda,
\qquad
B=C_{LP}\nu^{-1}S_Q^{1/2}
```

gives the second.

### Scaling check

The kernel

```math
K_{p,Q}=2^{-2(Q-p)}
```

is invariant under the simultaneous shift `(p,Q)->(p+m,Q+m)`. The quantity `S_Q` scales by `rho^2`, so

```math
\nu^{-1/2}\Lambda S_Q^{1/2}
```

and each term in the Young form scale exactly like `f`.

### Disposition

`PROVED`, but not time-integrated.

## 11. Near/far kernel ledger

Split

```math
S_Q=S_Q^{\mathrm{far},J}+S_Q^{\mathrm{near},J},
```

where

```math
S_Q^{\mathrm{far},J}
=
\sum_{0\le p\le Q-J-1}
2^{-2(Q-p)}\lambda_pD_p,
```

and

```math
S_Q^{\mathrm{near},J}
=
\sum_{\max(0,Q-J)\le p\le Q}
2^{-2(Q-p)}\lambda_pD_p.
```

The row sums are uniform:

```math
\sup_Q
\sum_{0\le p\le Q}
2^{-2(Q-p)}
\le
\sum_{j=0}^{\infty}4^{-j}
=
\frac43.
```

For the far region,

```math
\sup_Q
\sum_{0\le p\le Q-J-1}
2^{-2(Q-p)}
\le
\frac{4^{-(J+1)}}{1-1/4}.
```

For the near cluster,

```math
\sup_Q
\sum_{\max(0,Q-J)\le p\le Q}
2^{-2(Q-p)}
\le
\frac43.
```

Thus the shell-to-cutoff kernel has a uniform row bound and a tunably small far-row tail. This is a genuine improvement over an unweighted replacement of the supremum by a sum.

It does **not** close the time integral because

```math
\int_0^TS_Q(t)dt
=
\sum_{p\ge0}\lambda_p
\int_0^T
1_{\{Q(t)\ge p\}}
2^{-2(Q(t)-p)}D_p(t)dt,
```

and the Leray budget controls `D_p dt`, not `lambda_p D_p dt`. Row summability does not imply the required weighted column estimate.

## 12. Threshold-use ledger

| Shell region | Available threshold information | Use in Lemma 1 |
|---|---|---|
| `p>Q` | strict upper bound `lambda_p^-1 ||u_p||_infinity<c0 nu` | none; these shells are outside `f` |
| `p=Q` on `U` | lower bound `||u_Q||_infinity>=c0 nu Lambda` | establishes `f>=c0 nu Lambda^2`; no upper control |
| `p<Q` | no threshold bound | controlled only by Bernstein and dissipation |
| `p=-1` | fixed low-frequency block | integrable remainder |

The kernel envelope does not misuse the high-mode threshold. The moving cutoff enters only through the exact frequency ratio `lambda_p/Lambda`.

## 13. Proof-obligation DAG after L4-2

```text
L4-0a  source LP conventions                    PROVED
L4-0b  exact Q and Lambda definitions            PROVED
L4-0c  minimality -> threshold-shell lower bound PROVED
L4-0d  active/inactive split                     PROVED
L4-0e  exact f shell formula                     PROVED
          |
          v
L4-1a  physical dimensions                      PROVED
L4-1b  dyadic NS scaling                         PROVED
L4-1c  viscosity-normalized candidate terms      PROVED
          |
          v
L4-2a  base/annular separation                   PROVED
L4-2b  near/far active-shell split               PROVED
L4-2c  weighted pointwise envelope               PROVED
L4-2d  uniform row and far-tail sums             PROVED
          |
          v
L4-3a  weighted column estimate                  OPEN
L4-3b  active-set/dissipation correlation         OPEN
L4-3c  counterfixture at endpoint                OPEN
          |
          v
L4-5    Schur or Carleson closure                BLOCKED
```

## 14. Immediate next obligation

The first L4-3 question is now exact:

> Does `Lambda in L2_t`, together with the threshold definition and Leray energy inequality, control
>
> ```math
> \int_0^T
> \sum_{p=0}^{Q(t)}
> 2^{-2(Q(t)-p)}\lambda_pD_p(t)dt?
> ```

A positive answer closes `f in L1_t` through Lemma 1. A negative answer requires an explicit dyadic time-frequency profile satisfying all source-normalized constraints while making this weighted integral diverge.

The first audit should compute the column occupancy factor

```math
C_p(t)
=
1_{\{Q(t)\ge p\}}
2^{-2(Q(t)-p)}
```

against `D_p(t)dt`, and must not assume independence between dissipation and the active cutoff.

## Claim boundary

This artifact completes L4-0 through L4-2. It proves a dimensionally and scale-correct weighted pointwise envelope with a uniform geometric row kernel. It does not prove the weighted column estimate, `f in L1_t`, regularity, the critical integral, or A2.
