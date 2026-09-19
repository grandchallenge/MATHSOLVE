# NS-CI-R014-A2-L5-11 — Source and capture audit

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Governing predecessor: `NS_CI_R014_A2_L5_10_FIELD_CALIBRATION_FREQUENCY_SCALE_HANDOFF.md`
- Companion work package: `NS_CI_R014_A2_L5_11_FORCED_CORE_SHELL_CALIBRATION.md`
- Purpose: close two implicit regularity/summation obligations in the finite-shell capture argument and correct the source pointer used for the correction hierarchy.
- A2 theorem: open
- L5: active
- MATHCERT adjudication: absent
- Claim class: theorem-grade calibration of the explicit forced construction only

This audit is normative for L5-11.  Where it sharpens wording in the companion work package, this file controls.  It does not change the forced/unforced claim boundary.

## 1. Source corrections

The correction hierarchy used in L5-11 is supported by the following chain in the September 2026 OpenAI manuscript.

1. `Definition 9.4` defines the finite correction state.  There is no `Proposition 9.4` carrying the cumulative correction estimate.
2. Equation `(9.9)`, proved in the initialization and retained by `Proposition 9.6`, gives the cumulative positive-order correction classes.  In particular the primary curl correction has normalized exponent `>0.68`, while the mean increments and pressure changes have exponent `>0.9` (with the radial mean one order higher).
3. The finite-stage physical derivative estimate `(9.17)` states that every retained stage-`j` increment has normalized exponent at least `j/10`, with physical velocity prefactor bounded by `Q^{-A}`.
4. `Proposition 9.9` applies the summation lemma to the finite correction states and proves that the summed local field preserves all conclusions of `Theorem 3.1`, including endpoint regularity, the exact exterior heat field, and the inner velocity-growth formula.
5. The summation lemma's estimate `(5.35)` controls the difference between the infinite cutoff sum and any fixed finite partial sum after any fixed number of Cartesian space-time derivatives.

Accordingly, the phrase `Proposition 9.4/9.9` in the companion work package must be read as

```text
Definition 9.4 + equation (9.9) + Proposition 9.6 + Proposition 9.9,
with the infinite tail controlled by Lemma 5.4, equation (5.35).
```

No mathematical inference below depends on a nonexistent Proposition 9.4.

## 2. Infinite-summation closure for the normalized core profile

The companion package defines

```math
A=\frac12+h,
\qquad
U_\tau(y)=\tau^A u(\sqrt\tau\,y,1-\tau).
```

Its finite-stage argument shows that, on every fixed compact set in `y`, the base field has a nonconstant limit and each fixed finite collection of corrections vanishes after multiplication by `tau^A`.

The only remaining issue is interchange of the terminal limit `tau -> 0` with the infinite correction sum.

Let `U^{[J]}` be a fixed finite partial sum and `U` the final summed field.  The summation lemma gives, for every fixed derivative order `m`,

```math
|U-U^{[J]}|_m
\le
C_{J,m}
q^{g_{J+1}/2-\ell'_m}
```

on a sufficiently small `q`-neighbourhood after the first `J` cutoffs have become one.  In the stage construction one may take `g_j` increasing linearly with `j` (the retained stage increments have normalized exponent at least `j/10`).  Hence, for `m=0`, choose one finite `J` so large that

```math
A+g_{J+1}/2-\ell'_0>0.
```

Since the physical velocity rescaling contributes the fixed factor `q^{-A}`, multiplication by `q^A` gives

```math
q^A |u-u^{[J]}|
\le
C_J q^{A+g_{J+1}/2-\ell'_0}
\longrightarrow 0.
```

At core scale `x=sqrt(tau)y`, one has

```math
q=\tau(1+O(\tau^{2h})),
```

uniformly on each fixed compact set in `y`.  Therefore the same conclusion holds with `tau^A` in place of `q^A`:

```math
\tau^A |u-u^{[J]}|(\sqrt\tau y,1-\tau)
\longrightarrow0
```

locally uniformly.

For the fixed finite partial sum, equation `(9.9)` and the positive normalized correction exponents imply that every correction vanishes after the `tau^A` normalization.  Thus the final summed field has the same local normalized limit `V` as the leading profile.

This closes the infinite-summation step in Lemma 2.1 of the companion package rather than assuming that the summation cutoffs preserve the asymptotic.

## 3. Uniform global bound for the rescaled fields

The finite-shell transfer argument needs a global `L^infinity` bound on `U_tau`, not only compact convergence.

The required bound follows by splitting the final field into three regions.

### 3.1 Active similarity region

There `q>=tau`.  The fixed background and every finite-stage correction have physical velocity prefactor at worst `q^{-A}` times a uniformly bounded normalized coefficient.  Positive powers of `q^h` and fixed powers of `|log q|` are bounded after shrinking the terminal neighbourhood.  The infinite tail is controlled by the `m=0` case of `(5.35)` after choosing `J` as in Section 2.  Therefore

```math
|u(x,1-\tau)|\le C q^{-A}\le C\tau^{-A}.
```

### 3.2 Exact exterior

The final local field agrees with the exterior azimuthal heat field

```math
K(r,\tau)=r^{-1-2h}H_{ext}(\tau/r^2),
```

where `H_ext` is smooth on the nonnegative half-line and every fixed derivative is bounded.  In the exterior region `r>=c sqrt(tau)`, hence

```math
|K(r,\tau)|\le C\tau^{-1/2-h}=C\tau^{-A}.
```

### 3.3 Cutoff-transition / nonsingular region

The whole-space localization is supported away from the singular point there.  The endpoint-regularity conclusion preserved by Proposition 9.9 and the final whole-space construction gives a uniform physical bound, which is stronger than `C tau^{-A}` for `0<tau<tau_0`.

Combining the regions yields

```math
\sup_{0<\tau<\tau_0}\|U_\tau\|_\infty<\infty.
```

## 4. Bounded derivative of the limiting profile

Lemma 3.1 in the companion work package uses the high-frequency estimate

```math
\|T_bV_2\|_\infty
\le Cb^{-1}\|\nabla V_2\|_\infty.
```

Thus `V` must be in `W^{1,infinity}`, not merely smooth and bounded.  This is true for the constructed limit.

In the inner and joining profile regions, `V` is obtained from fixed smooth similarity profiles at `eta=0`; regularity at the axis and smooth matching across the fixed joins give bounded first derivatives on each bounded normalized-radius region.

In the exact exterior, after the isotropic rescaling `r=sqrt(tau) R`, the normalized azimuthal limit has the form

```math
V_{ext}(R)
=
R^{-1-2h}H_{ext}(R^{-2})e_\theta
```

up to the fixed normalization constants.  The source proves boundedness of every fixed derivative of `H_ext` on `[0,infinity)`.  Differentiating the displayed expression therefore gives a bounded first derivative for `R` bounded away from zero; this exterior is entered only beyond a fixed positive normalized radius.  Smooth profile matching covers the join.

Consequently

```math
V\in W^{1,\infty}(\mathbb R^3),
```

and in fact the fixed derivatives needed by any finite version of the capture argument are bounded.

The statement of Lemma 2.1 should therefore be read with the stronger conclusion

```text
V is bounded, smooth, and has bounded first derivative.
```

## 5. Dyadic-phase-uniform capture: audited proof skeleton

Fix the second Cartesian component and points `y_0,y_1` with

```math
d=V_2(y_1)-V_2(y_0)>0.
```

Let `T_b` be the continuous-frequency annular operator associated with the fixed campaign dyadic partition.

For each phase `a in [1,2]`, the shifted family `T_{a2^j}` telescopes with its associated low-pass operators.  Taking the difference between `y_1` and `y_0` removes the low-frequency constant mode, so

```math
d
=
\sum_{j\in\mathbb Z}
\big(T_{a2^j}V_2(y_1)-T_{a2^j}V_2(y_0)\big).
```

The tails are uniform in `a`:

- as `b->0`, differentiating the convolution kernel gives

  ```math
  |T_bV_2(y_1)-T_bV_2(y_0)|
  \le C|y_1-y_0|b\|V_2\|_\infty;
  ```

- as `b->infinity`, zero mean and the `W^{1,infinity}` bound give

  ```math
  \|T_bV_2\|_\infty
  \le Cb^{-1}\|\nabla V_2\|_\infty.
  ```

Both tails are geometric.  Hence one fixed finite offset set `J={-M,...,M}`, independent of the dyadic phase, captures at least a fixed fraction of `d`.

For `p_0(tau)` defined by

```math
1\le \lambda_{p_0}\sqrt\tau<2,
```

the exact scaling identity is

```math
\tau^A(\Delta_{p_0+j}u)_2(\sqrt\tau y,1-\tau)
=
T_{a_\tau2^j}(U_\tau)_2(y),
\qquad
a_\tau=\lambda_{p_0}\sqrt\tau\in[1,2).
```

Sections 2 and 3 give local convergence plus a global uniform `L^infinity` bound.  Uniform Schwartz tails of the compact kernel family then transfer the finite-set lower bound from `V` to `U_tau`.  Therefore, for every sufficiently small `tau`, at least one `j in J` obeys

```math
\|\Delta_{p_0+j}u(1-\tau)\|_\infty
\ge c\tau^{-1/2-h}.
```

This validates the finite-offset, every-late-time shell capture used in Theorem 4.1.

## 6. Consequence audit

For arbitrary fixed viscosity, the paper's scaling

```math
u_\nu(x,t)=\sqrt\nu\,u(x/\sqrt\nu,t)
```

moves the captured shell to

```math
\lambda_p\asymp(\nu\tau)^{-1/2},
\qquad
\|u_{\nu,p}\|_\infty\gtrsim\sqrt\nu\,\tau^{-1/2-h}.
```

Therefore

```math
\lambda_p^{-1}\|u_{\nu,p}\|_\infty
\gtrsim
\nu\tau^{-h}.
```

For sufficiently small `tau`, this violates the fixed strict-high threshold `c_0 nu`.  Hence the captured shell satisfies `p<=Q`, and

```math
\Lambda_\nu(1-\tau)
\gtrsim
(\nu\tau)^{-1/2}.
```

Thus

```math
\int_{1-\delta}^1\Lambda_\nu(t)^2dt=\infty.
```

The same active shell gives

```math
f(1-\tau)\gtrsim\tau^{-1-h},
\qquad
S_1(1-\tau)\gtrsim\nu\tau^{-1-2h},
```

so both corresponding terminal integrals diverge.  In particular, every finite high-`Lambda` packet tail on this forced singular construction has infinite `S_1` mass.

This is calibration evidence only.  The selected A2 target is unforced; the explicit construction has a nonzero smooth compactly supported force.  Nothing in this audit transfers the result across that class boundary.

## 7. Adversarial checks

The L5-11 claim survives the following exact checks.

1. **No pointwise-to-shell shortcut.**  The shell lower bound is obtained from a nonconstant normalized profile plus dyadic telescoping and uniform tail control, not inferred directly from `||u||_infinity` growth.
2. **No subsequence weakening.**  The phase-uniform finite offset set gives a violating shell at every sufficiently late time.
3. **No hidden terminal-frequency constant.**  The offset set and capture constant are fixed before `tau` tends to zero.
4. **No unproved global derivative assumption.**  The required `W^{1,infinity}` bound is supplied by the fixed smooth inner profiles, exact exterior formula, and bounded derivatives of `H_ext`.
5. **No illicit interchange with the infinite correction sum.**  Equation `(5.35)` is used after a fixed large finite truncation to make the normalized infinite tail vanish.
6. **No forced/unforced promotion.**  The conclusion is only that the explicit forced singular construction lies outside the A2 hypothesis because its campaign `Lambda` is not in `L^2_t`.

## 8. Successor

With these source and capture obligations explicit, C1 from L5-10 is closed positively as a bounded calibration tranche.

The next analytic obligation is C3: construct a local energy/pressure estimate retaining dyadic frequency `q` and physical backward scale `k` independently until a summable two-sided kernel in `q-k` is proved.  Only after that gain exists may `k` be tied to `Q(t)` or to `Q`-level sets.
