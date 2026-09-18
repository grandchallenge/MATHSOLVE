# NS-CI-R014-A2-L5-14 — C2 active-band intermittency reduction

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected base: `de840d9d4bcba97f340a7ed5259140fa6d929d76`
- Predecessor: `NS-CI-R014-A2-L5-13`
- Result:
  `A2_FAR_LOW_PACKET_REGION_CONTROLLED__SINGULARITY_REQUIRES_TOP_THIRD_D1_CONCENTRATION`
- A2 theorem: open
- L5: active
- C2-DIAG: active, narrowed
- MATHCERT adjudication: absent
- Evidence class: exact analytic reduction plus structural translation to the
  Cheskidov--Peng intermittency variable

This tranche executes the first C2-DIAG reduction after L5-13.  It does not
prove the missing active-band depletion theorem.  It proves that ordinary
Bernstein plus the energy supremum already removes a much larger portion of
the packet sum than the fixed-band language of C3-DIAG suggests.

The only possible obstruction to the L5-10 high-`Lambda` packet target lies
in the top logarithmic third of the active frequency range.

## 1. Protected inputs

The campaign uses

```math
\lambda_q=2^q,
\qquad
\Lambda(t)=\lambda_{Q(t)},
\qquad
S_1(t)=\sum_{q\le Q(t)}\|u_q(t)\|_\infty^2.
```

The Leray energy bound is

```math
\sum_q\|u_q(t)\|_2^2
\lesssim
U_0^2
```

for almost every time, up to the fixed LP overlap constant.

L5-8 proved

```math
f(t)^2\lesssim \Lambda(t)^2S_1(t),
```

where

```math
f(t)=\sup_{q\le Q(t)}\lambda_q\|u_q(t)\|_\infty.
```

L5-10 then proved that, under the selected A2 hypothesis
`Lambda in L2_t`, it is enough to show for some finite `R`

```math
\int_{\{\Lambda>R\}}S_1(t)\,dt<\infty.
```

L5-13 terminated the generic C3 central-band repairs and selected an
equation-derived intermittency/anti-concentration theorem as the preferred
successor.

## 2. Far-low packet region

For `Q\ge3`, define

```math
R_Q=\left\lfloor\frac{2Q}{3}\right\rfloor.
```

Write

```math
S_{\mathrm{far}}(t)
=
\sum_{0\le q\le R_Q}\|u_q(t)\|_\infty^2,
```

with the fixed inhomogeneous base block treated as the usual finite remainder.

### Lemma 2.1 — the lower two-thirds are already A2 controlled

Bernstein gives

```math
\|u_q\|_\infty^2
\lesssim
\lambda_q^3\|u_q\|_2^2.
```

Hence

```math
S_{\mathrm{far}}
\lesssim
\lambda_{R_Q}^3
\sum_{q\le R_Q}\|u_q\|_2^2
\lesssim
U_0^2\lambda_{R_Q}^3.
```

Because

```math
3R_Q\le2Q,
```

one has exactly

```math
\lambda_{R_Q}^3
=
2^{3R_Q}
\le
2^{2Q}
=
\Lambda^2.
```

Therefore

```math
\boxed{
S_{\mathrm{far}}(t)
\lesssim
U_0^2\Lambda(t)^2.
}
```

Under A2,

```math
\int_0^T S_{\mathrm{far}}(t)\,dt
<\infty.
```

No selector derivative, residence estimate, intermittency assumption, or
strict-high estimate is used.

### Sharpness of the exponent for this energy-only argument

If the relative cutoff is `q\le\alpha Q`, the same argument produces

```math
S_{\le\alpha Q}
\lesssim
U_0^2\Lambda^{3\alpha}.
```

The A2 budget is exactly sufficient when

```math
3\alpha\le2.
```

Thus

```math
\alpha=\frac23
```

is the largest relative cutoff available from ordinary Bernstein plus the
energy supremum alone.  Any improvement beyond `2/3` requires new
information.

## 3. The top-third packet target

Define the moving top band

```math
\mathcal B(t)
=
\left\{
q:
\left\lfloor\frac{2Q(t)}3\right\rfloor<q\le Q(t)
\right\}
```

and

```math
S_{\mathrm{top}}(t)
=
\sum_{q\in\mathcal B(t)}
\|u_q(t)\|_\infty^2.
```

Then, apart from the fixed base remainder,

```math
S_1=S_{\mathrm{far}}+S_{\mathrm{top}}.
```

### Corollary 3.1 — reduced packet theorem

Under A2, it is enough to prove

```math
\boxed{
\int_{\{\Lambda>R\}}S_{\mathrm{top}}(t)\,dt<\infty
}
```

for some finite `R`.

Indeed, the far-low part is already integrable by Lemma 2.1, so this condition
implies the L5-10 high-`Lambda` `S_1) tail theorem and therefore
`f in L1_t`.

The same statement is terminal-local: for a putative singular time `T`, it
is enough to prove the displayed estimate on
`(T-\delta,T)\cap\{\Lambda>R\}` for some finite `R,\delta>0`.

### Corollary 3.2 — necessary concentration signature of any A2 singularity

Suppose, contrary to A2, an unforced solution satisfying
`Lambda in L2(0,T)` were singular at `T`.

Then for every `\delta>0` and every finite `R`,

```math
\boxed{
\int_{(T-\delta,T)\cap\{\Lambda>R\}}
S_{\mathrm{top}}(t)\,dt
=
\infty.
}
```

Otherwise Corollary 3.1 would give the protected low-mode continuation
criterion through `T`.

This is a necessary condition only.  It does not construct a singular
trajectory and does not prove that such concentration can occur.

## 4. Dimension-one concentration variable

Assume `U_0>0`; the zero-energy case is trivial.  Retain the whole-space
intrinsic wavenumber from L5-8,

```math
\lambda_E
=
\left(\frac{\nu}{U_0}\right)^2.
```

For every nonzero shell define the dimensionless concentration factor

```math
\chi_q(t)
=
\frac{\|u_q(t)\|_\infty^2}
{\lambda_E\lambda_q^2\|u_q(t)\|_2^2}.
```

Set `chi_q=0` when the shell is zero.

Also define the instantaneous shell dissipation density

```math
d_q(t)
=
\nu\lambda_q^2\|u_q(t)\|_2^2.
```

Then exactly

```math
\boxed{
\|u_q\|_\infty^2
=
\frac{\lambda_E}{\nu}\chi_q d_q.
}
```

Therefore the missing top-band packet target is equivalently

```math
\int_{\{\Lambda>R\}}
\sum_{q\in\mathcal B(t)}
\chi_q(t)d_q(t)\,dt
<\infty.
```

The Leray inequality already gives

```math
\int_0^T\sum_qd_q(t)\,dt<\infty.
```

Thus the exact residual is no longer ordinary dissipation.  It is the
**dissipation-weighted concentration factor** on the top active band.

## 5. Effective active volume

Define

```math
V_q(t)
=
\frac{\|u_q(t)\|_2^2}
{\|u_q(t)\|_\infty^2}
```

for a nonzero shell.  This has the dimensions of spatial volume and

```math
\chi_q
=
\frac{1}
{\lambda_E\lambda_q^2V_q}.
```

Hence the dimension-one scale is

```math
V_q
\asymp
\lambda_E^{-1}\lambda_q^{-2}.
```

The desired C2-DIAG theorem is therefore an anti-concentration theorem: on
high-`Lambda` top-band shells, the effective volume must not be too much
smaller than the dimension-one scale in a dissipation-weighted time-average
sense.

### Active threshold shell

At `q=Q(t)`, minimality of the dissipation index gives the protected lower
threshold

```math
\|u_Q\|_\infty
\ge
c_0\nu\Lambda.
```

Together with `\|u_Q\|_2^2\le U_0^2`, this gives

```math
V_Q
\le
c_0^{-2}\lambda_E^{-1}\Lambda^{-2}.
```

Equivalently,

```math
\chi_Q
\ge
c_0^2\frac{U_0^2}{\|u_Q\|_2^2}
\ge
c_0^2.
```

This is an important orientation check.

The selector forces the threshold shell to be **at least** dimension-one
concentrated in this normalization; it does not provide the missing upper
bound on `chi_Q`.  A C2-DIAG theorem must prevent much stronger
concentration, rather than prove concentration exists.

## 6. Relation to Cheskidov--Peng 2026

Primary source:

Alexey Cheskidov and Qirui Peng,
*An optimal upper bound on the determining wavenumber for 3D Navier--Stokes
Equations*, NoDEA 33, 92 (2026), published 2 June 2026.

- `https://link.springer.com/article/10.1007/s00030-026-01232-0`
- preprint: `https://arxiv.org/abs/2407.06474`

Their intermittency dimension is defined through the degree of saturation of
Bernstein's inequality.  At `r=infinity`, the `D=1` member of their
definition has the structural form

```math
\left\langle
\sum_{q\le Q}\|u_q\|_\infty^2
\right\rangle
\lesssim
\lambda_0
\left\langle
\sum_{q\le Q}\lambda_q^2\|u_q\|_2^2
\right\rangle.
```

This is the periodic/forced analogue of the L5-8 `D=1` packet estimate,
where the fixed torus inverse length `lambda_0` is replaced in the
whole-space campaign by the intrinsic dimensionally correct inverse length
`lambda_E=(nu/U0)^2`.

This correspondence is used only as mathematical language and mechanism
guidance.  The Cheskidov--Peng theorem is periodic, forced, and time-averaged;
it is not imported as a theorem for the selected unforced whole-space A2
class.

L5-14 sharpens the campaign's use of that language further: global `D=1`
control is stronger than necessary.  Only the top-third, high-`Lambda`,
terminal concentration measure must be controlled.

## 7. What has actually been reduced

Before L5-14, C2-DIAG was phrased as active-band anti-concentration but its
frequency width was not sharp.

The exact state is now:

```text
q <= floor(2Q/3):
    already controlled by energy + Bernstein + A2.

floor(2Q/3) < q <= Q:
    only possible packet-concentration obstruction.
```

Equivalently, any hypothetical A2 singularity must carry infinite
dissipation-weighted `D=1` concentration in this top relative band near the
singular time.

This does not prove A2.  It isolates the only place where an intermittency
argument can still be necessary.

## 8. Next live obligation: C2-DYN

The next tranche must use the Navier--Stokes dynamics, not another static
interpolation.

The preferred target is a theorem of the form

```math
\int_{(T-\delta,T)\cap\{\Lambda>R\}}
\sum_{q\in\mathcal B(t)}
\chi_q(t)d_q(t)\,dt
<\infty
```

for some finite `R,\delta`, derived from the equation.

Equivalent useful forms include:

1. a dissipation-measure estimate on the tail distribution of `chi_q`;
2. an active-volume lower bound holding in a weighted time-average rather than
   pointwise;
3. a local-energy theorem showing that highly Bernstein-saturated top-band
   packets cannot persist or recur with enough total duration to make the
   displayed integral diverge;
4. a time-correlated signed central-flux estimate that directly controls the
   same top-band packet mass.

A pointwise global bound `chi_q<=C` is not required and should not be made
the default target.

## 9. Hard rejection tests

Reject any successor that:

- merely renames `S_top` as an intermittency dimension without proving a PDE
  estimate;
- assumes `chi_q` is bounded;
- uses strict-high at `q=Q`;
- replaces `chi_qd_q` by the already-closed unsigned
  `lambda_QD_Q` column;
- differentiates the moving cutoff `2Q/3` without a selector-variation
  theorem;
- treats the Cheskidov--Peng periodic/forced average estimate as applicable to
  the selected whole-space unforced class;
- uses a static packet fixture as an NSE counterexample;
- introduces a terminal-frequency-dependent constant.

## 10. Claim boundary

The protected result sought from this tranche is exactly

```text
A2_FAR_LOW_PACKET_REGION_CONTROLLED
__SINGULARITY_REQUIRES_TOP_THIRD_D1_CONCENTRATION.
```

It is a reduction theorem inside the selected A2 argument.

A2 remains unproved.  No dynamic anti-concentration estimate is proved here.
No MATHCERT, novelty, priority, or publication claim is asserted.
