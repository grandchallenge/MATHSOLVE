# NS-CI-L5-RESTART-001 — exact critical-integral decomposition

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Obligations executed here: `L5-0`, `L5-1`, `L5-2`
- Result: `EXACT_DECOMPOSITION_WITH_OPEN_INTEGRABILITY_BLOCKERS`
- Accepted critical-integral estimate: absent
- A2 theorem: open
- MATHCERT adjudication: absent

This record fixes the normalizations and derives the requested shell ledgers. It
does **not** prove that the critical integral is finite. In particular, it does
not import the low-mode coefficient `f in L1_t`, and it does not promote a
pointwise decomposition into a regularity result.

## L5-0 — normalization, dimensions, and scaling

### Equation and energy budget

On `R3`, let `u` be an unforced Leray–Hopf solution of

```math
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=0,
\qquad \nabla\cdot u=0,
\qquad \nu>0.
```

Write `U_0=||u_0||_2`. The only solution budgets admitted in this lane are

```math
\|u\|_{L^\infty(0,T;L^2)}\le U_0,
\qquad
2\nu\int_0^T\|\nabla u(t)\|_2^2dt\le U_0^2,
```

and the selected hypothesis

```math
L_\Lambda^2:=\int_0^T\Lambda(t)^2dt<\infty.
```

No conclusion about `f` is an input.

### Littlewood–Paley partition

Fix one smooth inhomogeneous dyadic partition

```math
u=\sum_{q\ge-1}u_q,
\qquad u_q=\Delta_qu,
\qquad \lambda_q=2^q\kappa_0.
```

Here `kappa_0` is the fixed base wavenumber; the repository convention
`lambda_q=2^q` is the nondimensional choice `kappa_0=1`. The block `q=-1` is
supported in a fixed ball and every `q>=0` block in a fixed annulus. Constants
`C_LP`, `C_S`, and `C_B` below depend only on this partition (and the exponent),
never on `Q`, time, or a terminal frequency truncation.

For `q>=0`, put

```math
E_q=\|u_q\|_2^2,
\qquad
A_q=\lambda_q^2E_q.
```

Thus `A_q` is shell enstrophy up to a partition constant and
`D_q=nu A_q` is shell dissipation density. The base block is always retained as
a fixed-frequency remainder and is never assigned annular equivalence.

### Dissipation wavenumber

With the same `c_0>0` as the source-normalized L4 record, define

```math
Q(t)=\min\left\{q\ge0:
\lambda_p^{-1}\|u_p(t)\|_\infty<c_0\nu
\text{ for every }p>q\right\},
\qquad
\Lambda(t)=\lambda_{Q(t)}.
```

For finite `Q(t)`, the upper threshold is available only for `p>Q(t)`. If
`Q(t)>=1`, minimality instead gives the lower bound

```math
\|u_{Q(t)}(t)\|_\infty\ge c_0\nu\Lambda(t).
```

There is no upper threshold estimate at `p=Q(t)` or below.

### Physical dimensions

With `[x]=L`, `[t]=T`, `[u]=L T^-1`, and `[nu]=L^2 T^-1`, one has

| Quantity | Physical dimension |
|---|---:|
| `lambda_q`, `Lambda` | `L^-1` |
| `||u||_2` | `L^(5/2) T^-1` |
| `||u||_6` | `L^(3/2) T^-1` |
| `A_q=lambda_q^2||u_q||_2^2` | `L^3 T^-2` |
| `D_q=nu A_q` | `L^5 T^-3` |
| `||u||_6^4` | `L^6 T^-4` |
| `int ||u||_6^4 dt` | `L^6 T^-3` |

For example, `U_0^2 Lambda^2 A_q` has dimension `L^6 T^-4`, so the
low-frequency baseline below is dimensionally consistent even though its time
integrability fails.

### Navier–Stokes scaling

For a dyadic `rho=2^m`, set

```math
u_\rho(x,t)=\rho u(\rho x,\rho^2t).
```

Viscosity is fixed, corresponding annular indices shift by `m`, and

| Quantity | Scaling factor |
|---|---:|
| `dt` | `rho^-2` |
| `lambda_q`, `Lambda` | `rho` |
| `||u||_2` | `rho^-1/2` |
| `||u||_6^2` | `rho` |
| `A_q` | `rho` |
| `D_q` | `rho` |
| `||u||_6^4` | `rho^2` |
| `Lambda^2` | `rho^2` |

Therefore both `int ||u||_6^4 dt` and `int Lambda^2 dt` are invariant. The
inhomogeneous base block is not exactly covariant across the fixed unit scale;
it is a fixed-frequency energy-controlled remainder rather than part of a
critical shell argument.

## L5-1 — exact `L6` representation and the losses

### Square-function equivalence

For every finite dyadic truncation `v`, define

```math
S(v)(x)=\left(\sum_{q\ge-1}|\Delta_qv(x)|^2\right)^{1/2}.
```

The exact tool used is the two-sided inhomogeneous Littlewood–Paley norm
equivalence

```math
C_{LP}^{-1}\|v\|_6
\le \|S(v)\|_6
\le C_{LP}\|v\|_6.
```

Consequently

```math
\|v\|_6^2
\simeq_{C_{LP}}
\left\|\sum_q|v_q|^2\right\|_3,
\qquad
\|v\|_6^4
\simeq_{C_{LP}}
\left\|\sum_q|v_q|^2\right\|_3^2.
```

These are norm equivalences, not literal identities and not an absolute shell
sum.

### Homogeneous versus inhomogeneous Sobolev

For whole-space functions in `dot H^1(R3)`, homogeneous Sobolev gives

```math
\|v\|_6\le C_S\|\nabla v\|_2.
```

For an inhomogeneous block decomposition this yields

```math
\|v\|_6^2
\le C_S^2\|\nabla v\|_2^2
\lesssim
\sum_{q\ge0}A_q + C_{-1}E_{-1}.
```

The `q=-1` term is written separately. Replacing this with
`||v||_6 \lesssim ||v||_{H^1}` introduces a harmless fixed-frequency `L2`
remainder but must not be called the homogeneous estimate.

### The dyadic-triangle loss

Minkowski applied after the square-function equivalence gives the one-way bound

```math
\left\|\sum_q|v_q|^2\right\|_3
\le
\sum_q\||v_q|^2\|_3
=
\sum_q\|v_q\|_6^2.
```

Thus

```math
\|v\|_6^4
\lesssim
\left(
\sum_q b_q
\right)^2,
\qquad b_q:=\|v_q\|_6^2,
```

and only at this lossy step does the absolute double shell sum appear:

```math
\left(\sum_qb_q\right)^2
=
\sum_qb_q^2+2\sum_{p<r}b_pb_r.
```

The first sum is the diagonal and the second is the off-diagonal. Neither term
is an exact expansion of the original `L6` norm: both belong to the
triangle-majorant ledger. No later use of cancellation may be attributed to
this already absolute sum.

### Low-shell exponent ledger

For annular `p<=Q`, Bernstein gives

```math
b_p=\|u_p\|_6^2
\le C_B^2\lambda_p^2\|u_p\|_2^2
=C_B^2A_p.
```

Hence, apart from the fixed base block,

```math
\|u_{\le Q}\|_6^4
\lesssim
\sum_{p\le Q}A_p^2
+2\sum_{p<r\le Q}A_pA_r.
```

For `p<=r`, energy and `lambda_p/lambda_r=2^{-(r-p)}` give

```math
A_pA_r
\le U_0^2\lambda_p^2A_r
=U_0^2\lambda_r^2 2^{-2(r-p)}A_r.
```

The row sum is exact:

```math
\sum_{p=0}^{r}2^{-2(r-p)}
=\sum_{j=0}^{r}4^{-j}
\le\frac43.
```

Therefore the triangle-majorant ledger reduces to

```math
\|u_{\le Q}\|_6^4
\lesssim
U_0^2\sum_{r=0}^{Q}\lambda_r^2A_r
\le
U_0^2\Lambda^2\sum_{r=0}^{Q}A_r.
```

The kernel is summable, but its endpoint retains `lambda_r^2`. The last bound
is the product of the unrelated `L1_t` quantities `Lambda^2` and
`sum A_r`. It is not controlled by the selected budgets. This proves an
estimate obstruction only; it is not the L4 coefficient `f`, and it supplies
no new cancellation, depletion, commutator, or decorrelation estimate for the
terminated L4 active diagonal.

| Low contribution | Shell factor before energy bound | Scaling | Available time control | Disposition |
|---|---:|---:|---|---|
| diagonal `p=r` | `A_r^2` | `rho^2` | only `A_r in L1_t` after shell sum | open blocker |
| off-diagonal `p<r` | `A_p A_r` | `rho^2` | `U_0^2 lambda_r^2 4^{-(r-p)}A_r` | endpoint weight remains |
| summed low majorant | `U_0^2 sum_{r<=Q}lambda_r^2A_r` | `rho^2` | no `L1_t` bound | rejected as closure |
| coarser endpoint | `U_0^2 Lambda^2 sum_{r<=Q}A_r` | `rho^2` | product of two `L1_t` factors | rejected as closure |

## L5-2 — moving-cutoff decomposition

Fix once and for all an integer overlap width `K>=2`, independent of `Q` and
any terminal truncation. At almost every time with finite `Q=Q(t)`, use the
exact block partition

```math
u=u_{\mathrm{core}}+u_{\mathrm{near}}+u_{\mathrm{tail}},
```

where

```math
u_{\mathrm{core}}=\sum_{p<Q-K}u_p,
\qquad
u_{\mathrm{near}}=\sum_{Q-K\le p\le Q+K}u_p,
\qquad
u_{\mathrm{tail}}=\sum_{p>Q+K}u_p.
```

This refines, without changing,

```math
u=u_{\le Q}+u_{>Q}.
```

The near cluster contains at most `2K+1` annular blocks (plus the base-block
edge case). It intentionally contains shells on both sides of the threshold.
The strict-high upper bound applies to its `p>Q` members, but not to `p=Q` or
below. Keeping this finite cluster separate prevents a false uniform-tail
argument from hiding the uncontrolled threshold shell.

The finite-sum inequality gives

```math
\|u\|_6^4
\le 27\left(
\|u_{\mathrm{core}}\|_6^4
+\|u_{\mathrm{near}}\|_6^4
+\|u_{\mathrm{tail}}\|_6^4
\right).
```

### Near-threshold cluster

Bernstein and the dyadic-triangle step give

```math
\|u_{\mathrm{near}}\|_6^4
\lesssim_K
\left(\sum_{|p-Q|\le K}A_p\right)^2.
```

Finiteness of the cluster removes no time exponent: the square of a locally
finite dissipation density is not controlled by its `L1_t` norm. In particular,
the `p=Q` diagonal cannot use the strict-high threshold.

### Strict high tail

For every `p>Q` the dissipation-wavenumber definition and interpolation give

```math
\|u_p\|_6
\le \|u_p\|_2^{1/3}\|u_p\|_\infty^{2/3},
```

and therefore

```math
b_p=\|u_p\|_6^2
\lesssim
\nu^{4/3}\lambda_p^{2/3}A_p^{1/3}.
```

The exponent arithmetic is

```math
\lambda_p^{4/3}\|u_p\|_2^{2/3}
=
\lambda_p^{4/3}(\lambda_p^{-2}A_p)^{1/3}
=
\lambda_p^{2/3}A_p^{1/3}.
```

Consequently the absolute-shell majorant for the strict tail has

```math
\|u_{\mathrm{tail}}\|_6^4
\lesssim
\nu^{8/3}
\left(
\sum_{p>Q+K}\lambda_p^{2/3}A_p^{1/3}
\right)^2.
```

Attempting Hölder in shell index with exponents `3` and `3/2` exposes the
endpoint failure:

```math
\sum_{p>Q+K}\lambda_p^{2/3}A_p^{1/3}
\le
\left(\sum_{p>Q+K}A_p\right)^{1/3}
\left(\sum_{p>Q+K}\lambda_p\right)^{2/3},
```

and the second series diverges. On the diagonal the same failure appears as

```math
b_p^2
\lesssim
\nu^{8/3}\lambda_p^{4/3}A_p^{2/3},
```

which is not summable from `sum_p A_p<infinity`. A finite terminal truncation
therefore gives no uniform continuum estimate.

| High contribution | Shell factor | Frequency power | Available control | Disposition |
|---|---:|---:|---|---|
| one strict shell | `nu^(4/3) lambda_p^(2/3) A_p^(1/3)` | `+2/3` | `sum A_p in L1_t` | positive power remains |
| tail diagonal | `nu^(8/3) lambda_p^(4/3) A_p^(2/3)` | `+4/3` | insufficient | open blocker |
| tail off-diagonal | `nu^(8/3)(lambda_p lambda_r)^(2/3)(A_p A_r)^(1/3)` | positive in both indices | insufficient | open blocker |
| shell Hölder remainder | `sum_{p>Q+K}lambda_p` | `+1` | divergent | rejected as closure |

### Cutoff selectors and motion

Let

```math
\chi_q(t)=\mathbf 1_{\{Q(t)=q\}}.
```

The pointwise identities above mean, for example,

```math
\sum_q\chi_q(t)\sum_{p\le q}A_p(t),
```

and use only the facts `chi_q>=0` and `sum_q chi_q=1` almost everywhere. No
time derivative of `Q`, no derivative of `chi_q`, and no cutoff-motion term is
created by this pointwise decomposition.

If a later argument differentiates `u_{<=Q(t)}`, integrates a shell balance on
components of `{Q=q}`, or telescopes between selector intervals, the entry/exit
terms and the distributional variation of `chi_q` must be recorded. They have
no sign or variation budget here and may not be silently discarded. The L4
moving-cutoff fixtures remain admissible adversarial checks, not an imported
closure theorem.

## Consolidated control ledger

| Required component | Exact or bounded expression | Actual budget | Status |
|---|---|---|---|
| low diagonal | `sum_{p<=Q} A_p^2` | `sum A_p in L1_t` | not closed |
| low off-diagonal | `2 sum_{p<r<=Q} A_p A_r` | geometric ratio after one energy bound | endpoint weight not closed |
| near cluster | `(sum_{|p-Q|<=K} A_p)^2` | finite number of shells only | not closed in time |
| strict high tail | `nu^(8/3)(sum lambda_p^(2/3)A_p^(1/3))^2` | strict-high threshold and dissipation | not closed in shell index |
| pointwise selector | `chi_q`, `sum chi_q=1` | measurability | harmless without differentiation |
| cutoff motion | entry/exit terms if differentiated | no variation/sign budget | must remain explicit |
| L4 active shell | no imported `f`; no renamed closure | L4 route terminated | excluded |

## Counterfixtures and fail-closed checks

1. `a(t)=b(t)=t^(-2/3)` on `(0,1)` are each in `L1`, while `ab` is not.
   This rejects the low endpoint product.
2. A sequence concentrated at one successively higher shell has bounded
   `sum A_p` but makes `lambda_p^(2/3)A_p^(1/3)` arbitrarily large. This rejects
   uniform strict-tail closure from dissipation alone.
3. A cutoff profile may have finite `int Lambda^2` and arbitrarily many selector
   components. Occupancy does not control cutoff variation.
4. The definition supplies no upper threshold at `p=Q`; treating the whole near
   cluster as strict high is invalid.
5. The absolute dyadic triangle sum has already discarded square-function
   cancellation; none may be restored without a new estimate before that step.

## Completed obligation and next gate

`L5-0` through `L5-2` are complete as normalization and exact-decomposition
obligations. Their output is a characterized blocker, not an accepted
critical-integral majorant. Node `A2-P04` therefore remains open and `A2-P05`
is not reached. Progress now requires a genuinely equation-specific estimate
that acts before the lossy absolute shell sum, or that supplies new
correlation, cancellation, depletion, commutator, or decorrelation control.

## Claim boundary

This artifact proves only the displayed algebraic inequalities, scaling facts,
geometric sum, and obstruction fixtures. It neither proves nor refutes the
Navier–Stokes target, changes the claim ledger, supplies MATHCERT adjudication,
or authorizes novelty, priority, publication, patentability, product, or
commercial claims.
