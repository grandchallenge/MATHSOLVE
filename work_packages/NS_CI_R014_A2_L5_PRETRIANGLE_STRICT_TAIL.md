# NS-CI-R014-A2-L5-3 — Pre-triangle strict-high square-function audit

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected predecessor: `6cdaecdbf5d3acd1389c5f2bbbbf91ea3b32af58`
- Candidate: `PRETRIANGLE_STRICT_HIGH_SQUARE_FUNCTION`
- Result: `L5_CANDIDATE_ROUTE_TERMINATED__CHARACTERIZED_BLOCKER`
- A2 theorem: open
- MATHCERT adjudication: absent

This tranche returns to the Littlewood--Paley square function before the lossy
Minkowski shell sum. It proves a uniform strict-high quartic estimate and then
computes the exact `L6` endpoint produced by the same interaction argument. The
quartic gain is real; the `L6` lift requires a strict-tail `H^2` density that is
not controlled by the selected hypothesis or the Leray budget.

The result terminates only the candidate that the strict-high threshold plus
pre-triangle square-function interaction closes blocker B3 by itself. It does
not terminate L5 as a whole and does not prove or refute A2.

## 1. Imported protected interface

Use the protected L5 normalization. For annular shells

```math
E_p=\|u_p\|_2^2,
\qquad
A_p=\lambda_p^2E_p,
```

and, at almost every time with finite `Q=Q(t)`,

```math
\|u_p\|_\infty<c_0\nu\lambda_p
\qquad\text{only for }p>Q.
```

The admitted budgets are

```math
\|u\|_{L^\infty_tL^2_x}\le U_0,
\qquad
2\nu\int_0^T\|\nabla u\|_2^2dt\le U_0^2,
\qquad
\int_0^T\Lambda^2dt<\infty.
```

Fix `K>=2` and define the strict tail

```math
u_{\rm tail}=\sum_{p>Q+K}u_p.
```

Every shell used below is therefore strictly above `Q`; no threshold estimate
is used at `p=Q` or below.

For a finite terminal index `N`, write

```math
S_N(x)^2
=
\sum_{Q+K<p\le N}|u_p(x)|^2.
```

Littlewood--Paley equivalence gives constants independent of `Q`, `N`, and time
such that

```math
\|u_{\rm tail}^{(N)}\|_r\lesssim\|S_N\|_r,
\qquad r\in\{4,6\}.
```

## 2. Residual ledger before the candidate

| Blocker | Protected residual | Candidate relevance |
|---|---|---|
| B1 low core | `Lambda^2` correlated with low dissipation | untouched |
| B2 near cluster | `(sum_{|p-Q|<=K} A_p)^2` | untouched |
| B3 strict tail | absolute-shell `+2/3` frequency power | directly audited before Minkowski |
| B4 selector motion | no variation/sign budget for moving `Q` | untouched; no time differentiation here |

The present candidate is intentionally disjoint from the terminated L4 active
diagonal: it uses only shells `p>Q+K` and no low-mode coefficient, selected
active shell, moving-selector derivative, or positive kernel below the cutoff.

## 3. L5-3A — strict-high quartic bridge

### Proposition

For every finite truncation `N>Q+K`,

```math
\|u_{\rm tail}^{(N)}(t)\|_4^4
\lesssim
c_0^2\nu^2
\sum_{Q+K<p\le N}A_p(t),
```

with a constant independent of `Q`, `N`, and time. Consequently,

```math
\int_0^T\|u_{\rm tail}(t)\|_4^4dt
\lesssim
c_0^2\nu U_0^2.
```

### Proof

Before Minkowski,

```math
\|S_N\|_4^4
=
\int\left(\sum_p|u_p|^2\right)^2dx
=
\sum_{p,r}\int|u_p|^2|u_r|^2dx.
```

Order a pair as `p<=r`. The strict-high threshold on the lower-frequency factor
gives

```math
\int|u_p|^2|u_r|^2dx
\le
\|u_p\|_\infty^2\|u_r\|_2^2
\le
c_0^2\nu^2\lambda_p^2E_r
=
c_0^2\nu^2
\left(\frac{\lambda_p}{\lambda_r}\right)^2A_r.
```

The dyadic row sum is uniform:

```math
\sum_{p\le r}
\left(\frac{\lambda_p}{\lambda_r}\right)^2
\le
\sum_{j\ge0}4^{-j}
=
\frac43.
```

Accounting for the two pair orderings and Littlewood--Paley equivalence proves
the finite-`N` estimate. The constant is uniform in `N`, so monotone/Fatou
passage at the square-function level gives the infinite-tail estimate.
Integrating in time and using the Leray dissipation budget proves the displayed
space-time bound.

### What changed

The protected L5-2 triangle route produced

```math
\sum_p\lambda_p^{2/3}A_p^{1/3}
```

and an unsummable positive shell-frequency remainder. The pre-triangle quartic
calculation has no such remainder. The strict-high threshold supplies exactly
the lower-frequency factor needed for a geometric pair sum.

This is a genuine estimate gain, but it is subcritical with respect to the
`L^4_tL^6_x` target.

## 4. L5-3B — exact `L6` endpoint of the same mechanism

### Proposition

For every finite truncation `N>Q+K`,

```math
\|u_{\rm tail}^{(N)}(t)\|_6^6
\lesssim
c_0^4\nu^4
\sum_{Q+K<s\le N}\lambda_s^2A_s(t).
```

Equivalently,

```math
\|u_{\rm tail}^{(N)}(t)\|_6^4
\lesssim
c_0^{8/3}\nu^{8/3}
\left(
\sum_{Q+K<s\le N}\lambda_s^2A_s(t)
\right)^{2/3}.
```

The right-hand shell density is

```math
Z_{\rm tail}(t)
:=
\sum_{s>Q+K}\lambda_s^2A_s(t)
=
\sum_{s>Q+K}\lambda_s^4\|u_s(t)\|_2^2,
```

an `H^2` density. The Leray budget controls `sum A_s`, not `Z_tail`.

### Proof

Again work before Minkowski:

```math
\|S_N\|_6^6
=
\int\left(\sum_p|u_p|^2\right)^3dx
=
\sum_{p,r,s}
\int|u_p|^2|u_r|^2|u_s|^2dx.
```

Order a triple as `p<=r<=s`. Apply the strict-high threshold to the two lower
frequency factors:

```math
\int|u_p|^2|u_r|^2|u_s|^2dx
\le
\|u_p\|_\infty^2
\|u_r\|_\infty^2
\|u_s\|_2^2
```

and hence

```math
\le
c_0^4\nu^4
\frac{\lambda_p^2\lambda_r^2}{\lambda_s^2}A_s.
```

For fixed `s`,

```math
\sum_{r\le s}\sum_{p\le r}
\frac{\lambda_p^2\lambda_r^2}{\lambda_s^2}
\le
\frac43
\sum_{r\le s}\frac{\lambda_r^4}{\lambda_s^2}
\le
\frac43\frac{16}{15}\lambda_s^2.
```

The six triple orderings only change the absolute constant. This proves the
finite-`N` estimate and, after taking the `2/3` power, the fourth-power form.

The calculation is scale-critical: `Z_tail` scales like `rho^3`, so
`Z_tail^(2/3)` scales like `rho^2`, exactly as `||u||_6^4`.

## 5. First exact failure

To close the strict tail through this candidate one would need

```math
\int_0^T Z_{\rm tail}(t)^{2/3}dt<\infty.
```

A sufficient stronger condition would be `Z_tail in L1_t`, since finite-time
Holder would then give the required `L^(2/3)_t` integral. No such `H^2`
dissipation budget is admitted for a Leray--Hopf solution.

The failure is therefore not the earlier absolute shell-Hölder divergence. The
pre-triangle calculation removes that artifact and exposes a sharper endpoint:

> the strict-high threshold converts two factors to `L-infinity`, but the
> remaining highest-frequency factor carries one derivative beyond the Leray
> `H^1` dissipation level, namely the `H^2` density `sum lambda_s^2 A_s`.

An equation-specific theorem controlling this density, or a signed/nonlinear
identity avoiding it, would be new information. It is not supplied by
`Lambda in L2_t` plus the static Leray budgets.

## 6. Static-budget counterfixture

The missing endpoint cannot be recovered from the existing scalar budgets by
another Holder rearrangement.

Take dyadic levels `q_n=6n`, `lambda_{q_n}=2^(6n)`, disjoint time intervals
with

```math
|I_n|=2^{-13n},
\qquad Q=q_n,
```

and place a strict-tail shell at `p_n=q_n+K+1` with

```math
A_{p_n}=2^{9n}.
```

Then, up to fixed `K`-dependent constants,

```math
\sum_n\lambda_{q_n}^2|I_n|
=
\sum_n2^{-n}
<\infty,
```

and

```math
\sum_nA_{p_n}|I_n|
=
\sum_n2^{-4n}
<\infty.
```

The kinetic energy of that shell is also bounded:

```math
E_{p_n}
=A_{p_n}/\lambda_{p_n}^2
\asymp
2^{-3n}.
```

But

```math
Z_{\rm tail}
\asymp
\lambda_{p_n}^2A_{p_n}
\asymp
2^{21n},
```

so

```math
\sum_n |I_n| Z_{\rm tail}^{2/3}
\asymp
\sum_n2^n
=\infty.
```

The strict-high `L-infinity` threshold is compatible with this scalar shell
profile: split the tail `L2` mass among approximately `2^(3n)` mutually
separated annular packets, each below the strict-high amplitude threshold. Add
a single threshold-scale packet at `q_n` to realize the cutoff; its energy and
dissipation contributions are dyadically summable on the same intervals.

This is an adversarial shell-and-packet profile, not a Navier--Stokes solution.
It proves only that the static selected budgets and strict-high amplitude cap do
not control the new `H^2` endpoint. A PDE-specific dynamic correlation may
still exclude the fixture.

## 7. Adversarial controls

1. **Threshold direction:** every threshold use is on `p>Q+K>Q`; the shell
   `p=Q` is never treated as strict high.
2. **No unrelated `L1` product:** the quartic time bound is linear in
   `sum A_p`; the failed sextic endpoint is recorded rather than multiplied by
   another `L1` factor.
3. **Uniform terminal frequency:** all pair and triple geometric constants are
   bounded independently of `N`.
4. **No restored cancellation:** the argument never attributes cancellation to
   the absolute shell sum. It works directly with the nonnegative square
   function before Minkowski.
5. **No selector variation:** `Q(t)` is used pointwise only. No derivative or
   bounded-variation property of the selector is assumed.
6. **No L4 recurrence:** the active shell and all shells below `Q` are absent
   from the proved strict-tail estimates.
7. **No hidden target norm:** no `f in L1`, LPS norm, uniform `H1`, or desired
   `L4_tL6_x` quantity is used as an input.
8. **No finite-truncation inference:** truncations are used only to justify
   finite sums; all constants are uniform before the continuum passage.

## 8. Successor state

The candidate

```text
strict-high threshold
+ exact square-function interaction
+ Leray dissipation
=> strict-tail L4_t L6_x closure
```

is terminated at the exact `H^2` endpoint above.

The proved intermediate result is the uniform strict-high quartic bridge. B3 is
therefore sharpened from

```text
absolute shell sum leaves +2/3 frequency power
```

to

```text
pre-triangle interactions remove the quartic shell residue,
but the L6 endpoint requires control of
integral (sum_{p>Q+K} lambda_p^2 A_p)^(2/3) dt.
```

B1, B2, and B4 are unchanged.

A materially new successor must supply an equation-specific dynamic estimate
for this endpoint, a cancellation/depletion identity that avoids the top
frequency factor, or a different bridge addressing B1/B2/B4. Repackaging the
static threshold and Leray budgets is excluded by the counterfixture.

## Claim boundary

This work package proves the two displayed strict-tail square-function
inequalities and the stated static-budget obstruction. It does not prove or
refute `NS-CI-R014-A2`, universal critical integrability, or global
Navier--Stokes regularity; it does not reopen L3 or L4; and it creates no
novelty, priority, publication, patentability, product, commercial, or
MATHCERT certification claim.
