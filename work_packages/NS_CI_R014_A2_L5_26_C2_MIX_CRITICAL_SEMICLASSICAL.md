# NS-CI-R014-A2-L5-26 — critical shear-chain semiclassical mass survival

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor: `79055e1d254362e27a2566521f0b5214fddb3968`
- Result:
  `SHEAR_CHAIN_CRITICAL_SEMICLASSICAL_MASS_SURVIVAL_PROVED__UNIFORM_POSITIVE_SELECTOR_CHARGE_LOWER_BOUND`
- A2 theorem: open
- L5: active
- C2-MIX-CRITICAL: resolved positively in the exact shear calibration
- MATHCERT adjudication: absent
- Evidence class: exact asymptotic theorem for the smooth unforced periodic
  2.5D shear calibration protected in L5-23--L5-25; not the selected
  whole-space A2 class

L5-24 and L5-25 pin the threshold front of the exact shear calibration to the
power-law scale `R^{1/3+o(1)}`, but stop at the exact critical window
`\tau\asymp R^{1/3}`.

That critical window can be resolved nonperturbatively.

Set

```math
h=R^{-1/3},
\qquad
\varepsilon=h^3,
\qquad
s=h\tau.
```

After exact removal of the rapidly oscillating shear phase, the critical
amplitude converges on every fixed positive `s\)-interval to

```math
\boxed{
A_0(s,Y)
=
\exp\left(
-\frac{s^3}{3}\sin^2Y
\right).
}
```

This limiting amplitude is strictly positive and retains a nondegenerate
semiclassical frequency distribution.

Consequently, on one fixed critical interval, for example

```math
1\le s\le2,
```

the exact finite-viscosity chain has a fixed positive amount of Fourier mass in

```math
c_-\le |hn|\le c_+
```

for all sufficiently small `h`.

The band contains only `O(h^{-1})` modes, so at each critical time one
coefficient satisfies

```math
|a_n|
\ge
c h^{1/2}.
```

After restoring physical scaling, a nearby LP block at frequency
`\lambda_p\asymp Nh^{-1}=NR^{1/3}` has

```math
\lambda_p^{-1}\|u_p\|_\infty
\ge
c\nu h^{-3/2},
```

and hence violates the campaign threshold by a diverging factor.

Therefore throughout the critical interval,

```math
\boxed{
\Lambda(t)
\ge
cN R^{1/3}.
}
```

The physical interval has length `O(h^2/(\nu N^2))`, and the resulting
selector charge satisfies

```math
\boxed{
\int \Lambda(t)^2\,dt
\ge
\frac{c_*}{\nu},
}
```

with `c_*>0` independent of `R`.

Thus the exact phase-locked shear calibration realizes a genuine nonvanishing
critical A2-scale cost. This does not prove A2, but it supplies the first exact
calibration mechanism in this lane whose overshoot-generated selector charge
does not vanish as `R\to\infty`.

## 1. Critical scaling of the exact shear chain

Retain the exact scalar equation from L5-23:

```math
\partial_\tau\phi_\varepsilon
+
i e^{-\varepsilon\tau}\cos Y\,\phi_\varepsilon
=
\varepsilon(\partial_Y^2-1)\phi_\varepsilon,
\qquad
\phi_\varepsilon(0,Y)=1.
```

Set

```math
\varepsilon=h^3,
\qquad
s=h\tau,
\qquad
\Phi_h(s,Y)
=
\phi_{h^3}(s/h,Y).
```

Then

```math
\boxed{
\partial_s\Phi_h
+
i h^{-1}e^{-h^2s}\cos Y\,\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h.
}
```

The critical time scale is now `s=O(1)`.

## 2. Exact critical phase removal

Define

```math
q_h(s)
=
h^{-3}(1-e^{-h^2s}),
\qquad
p_h(s)
=
h q_h(s)
=
h^{-2}(1-e^{-h^2s}).
```

Then

```math
q_h'(s)
=
h^{-1}e^{-h^2s},
```

so the fast potential can be removed exactly by

```math
\Phi_h(s,Y)
=
e^{-iq_h(s)\cos Y}
A_h(s,Y).
```

Since

```math
p_h(s)
=
s+O(h^2)
```

uniformly on every fixed `s\)-interval, `p_h` has a finite nonzero critical
limit.

A direct differentiation gives

```math
\boxed{
\begin{aligned}
\partial_s A_h
={}&
h^2\partial_Y^2A_h
+
2ihp_h\sin Y\,\partial_YA_h
+
ihp_h\cos Y\,A_h
\\
&-
p_h^2\sin^2Y\,A_h
-
h^2A_h.
\end{aligned}
}
```

The order-one real term is the critical mixing-diffusion damping.

## 3. Critical limiting amplitude

Formally setting `h=0` gives the scalar ODE

```math
\partial_s A_0
=
-s^2\sin^2Y\,A_0,
\qquad
A_0(0,Y)=1.
```

Therefore

```math
\boxed{
A_0(s,Y)
=
\exp\left(
-\frac{s^3}{3}\sin^2Y
\right).
}
```

The limit is smooth and strictly positive for every finite `s`.

## 4. Uniform fixed-window Sobolev control of the amplitude

Fix an integer `k>=0` and a finite critical horizon `0<=s<=S`.

On that interval,

```math
0\le p_h(s)\le s\le S.
```

The amplitude equation has:

- diffusion coefficient `h^2`;
- first-order coefficient of size `O(h)`;
- smooth bounded zeroth-order coefficients;
- nonpositive real potential `-p_h^2\sin^2Y-h^2`.

Differentiate `k` times in `Y`. The top first-order term is bounded by

```math
Ch
\|\partial_Y^{k+1}A_h\|_2
\|\partial_Y^kA_h\|_2
```

and is absorbed by the `h^2` diffusion through Young's inequality.
All commutators have bounded coefficients and lower derivative order.

A standard periodic energy induction therefore gives

```math
\boxed{
\sup_{0<h\le1}
\sup_{0\le s\le S}
\|A_h(s)\|_{H^k}
\le
C_{k,S}.
}
```

No inverse power of `h` appears in the demodulated amplitude norms.

## 5. Strong convergence to the critical amplitude

Let

```math
W_h=A_h-A_0.
```

Write the amplitude equation as

```math
\partial_sA_h=L_h(s)A_h,
\qquad
\partial_sA_0=L_0(s)A_0,
```

where

```math
L_0(s)
=
-s^2\sin^2Y.
```

The forcing generated by applying `L_h-L_0` to the fixed smooth function
`A_0` consists of

```math
h^2\partial_Y^2A_0,
\quad
2ihp_h\sin Y\,\partial_YA_0,
\quad
ihp_h\cos Y\,A_0,
\quad
-h^2A_0,
\quad
-(p_h^2-s^2)\sin^2Y\,A_0.
```

On a fixed critical horizon,

```math
p_h-s=O(h^2),
\qquad
p_h^2-s^2=O(h^2),
```

so for every fixed `k`,

```math
\|(L_h-L_0)A_0\|_{H^k}
\le
C_{k,S}h.
```

The same energy estimate used above gives a uniform `H^k` growth bound for
the inhomogeneous equation for `W_h`.

Since `W_h(0)=0`, Gronwall yields

```math
\boxed{
\sup_{0\le s\le S}
\|A_h(s)-A_0(s)\|_{H^k}
\le
C_{k,S}h.
}
```

Thus the critical limit is strong enough to control scaled Fourier moments.

## 6. Critical zeroth, second, and fourth moments

Write the Fourier expansion at critical time as

```math
\Phi_h(s,Y)
=
\sum_{n\in\mathbb Z}
a_n^{(h)}(s)e^{inY}.
```

Because the demodulating phase has unit modulus,

```math
\|\Phi_h\|_2
=
\|A_h\|_2.
```

Hence

```math
\sum_n|a_n^{(h)}|^2
\longrightarrow
E_0(s)
:=
\|A_0(s)\|_2^2.
```

For the first derivative,

```math
h\partial_Y\Phi_h
=
e^{-iq_h\cos Y}
\left(
h\partial_YA_h
+
ip_h\sin Y\,A_h
\right).
```

Using the strong `H^1` convergence and `p_h\to s`,

```math
\boxed{
h^2
\sum_n
n^2|a_n^{(h)}|^2
\longrightarrow
M_2(s)
:=
s^2
\|\sin Y\,A_0(s)\|_2^2.
}
```

Similarly,

```math
\begin{aligned}
h^2\partial_Y^2\Phi_h
=
e^{-iq_h\cos Y}
\big[
&
h^2\partial_Y^2A_h
+
2ihp_h\sin Y\,\partial_YA_h
\\
&+
ihp_h\cos Y\,A_h
-
p_h^2\sin^2Y\,A_h
\big].
\end{aligned}
```

The strong `H^2` convergence therefore gives

```math
\boxed{
h^4
\sum_n
n^4|a_n^{(h)}|^2
\longrightarrow
M_4(s)
:=
s^4
\|\sin^2Y\,A_0(s)\|_2^2.
}
```

All three convergences are uniform on compact positive `s\)-intervals.

## 7. Uniform critical band mass

Fix the critical interval

```math
1\le s\le2.
```

On this interval:

- `E_0(s)>0`;
- `M_2(s)>0`;
- `M_4(s)<\infty`;

and all three are continuous.

Normalize the finite-`h` Fourier weights by

```math
\pi_n^{(h,s)}
=
\frac{|a_n^{(h)}(s)|^2}
{\sum_m|a_m^{(h)}(s)|^2}.
```

Consider the nonnegative random variable

```math
X=(hn)^2.
```

The moment convergences imply uniform constants

```math
0<m_*\le
\mathbb E[X],
\qquad
\mathbb E[X^2]\le M_*<\infty
```

for all sufficiently small `h` and every `s\in[1,2]`.

Paley--Zygmund gives a uniform constant `c_*>0` such that

```math
\mathbb P(
X\ge m_*/2
)
\ge
c_*.
```

Choose a fixed `C_+<\infty` large enough that Markov gives

```math
\mathbb P(
|hn|>C_+
)
\le
c_*/2.
```

Set

```math
C_-=\sqrt{m_*/2}.
```

Then there is a fixed `m_{\rm band}>0` such that

```math
\boxed{
\sum_{C_-\le|hn|\le C_+}
|a_n^{(h)}(s)|^2
\ge
m_{\rm band}
}
```

for every `s\in[1,2]` and all sufficiently small `h`.

This is the critical finite-viscosity mass-survival theorem.

## 8. One critical coefficient is large

The band

```math
C_-\le|hn|\le C_+
```

contains at most `C h^{-1}` integer indices.

Therefore at each `s\in[1,2]` there exists
`n_h(s)` in that band such that

```math
\boxed{
|a_{n_h(s)}^{(h)}(s)|
\ge
c h^{1/2}.
}
```

The selected index may vary with `s\). No residence of one Fourier mode is
assumed.

## 9. Convert critical mass to the campaign threshold

The corresponding physical Fourier frequency is

```math
N(1,n_h(s),0),
```

so

```math
|k|
\asymp
Nh^{-1}
=
N R^{1/3}.
```

The physical vertical velocity has coefficient, up to a fixed real-part
normalization,

```math
A a_{n_h(s)}^{(h)},
\qquad
A=R\nu N=h^{-3}\nu N.
```

Finite overlap of the fixed smooth LP partition gives at least one nearby
block with

```math
\|u_p(t)\|_\infty
\ge
c A h^{1/2}.
```

Since

```math
\lambda_p
\asymp
Nh^{-1},
```

one obtains

```math
\boxed{
\lambda_p^{-1}
\|u_p(t)\|_\infty
\ge
c\nu h^{-3/2}.
}
```

As `h\to0`, this exceeds the fixed campaign threshold by an unbounded factor.

Therefore, for every critical time `s\in[1,2]`,

```math
\boxed{
\Lambda(t)
\ge
cNh^{-1}
=
cN R^{1/3}.
}
```

No selector continuity and no fixed violating shell are used.

## 10. Uniform positive selector charge

Since

```math
s=h\tau,
\qquad
\tau=ANt,
```

physical time satisfies

```math
dt
=
\frac{ds}{hAN}.
```

Using

```math
A=h^{-3}\nu N,
```

this becomes

```math
\boxed{
dt
=
\frac{h^2}{\nu N^2}\,ds.
}
```

On `s\in[1,2]`,

```math
\Lambda(t)^2
\ge
cN^2h^{-2}.
```

Hence

```math
\boxed{
\int_{1/(hAN)}^{2/(hAN)}
\Lambda(t)^2\,dt
\ge
\frac{c_*}{\nu},
}
```

where `c_*>0` is independent of `R`.

This is the first protected-route calibration in the current C2 sequence with
a nonvanishing overshoot-generated selector charge.

## 11. Relation to L5-24 and L5-25

L5-24 proves an all-time upper reach

```math
\Lambda
\le
C_\delta
N R^{1/3+\delta}.
```

L5-25 proves lower reach

```math
\Lambda
\ge
c_\eta
N R^{1/3-\eta}
```

on every subcritical moving window.

L5-26 resolves the missing exact power:

```math
\boxed{
\Lambda
\ge
c N R^{1/3}
}
```

on one fixed critical rescaled interval.

The result is still one-sided in amplitude: it does not give an exact critical
profile for the dissipation selector, only the lower reach and charge needed
for calibration.

## 12. What this proves about the C2 mechanism

The exact shear calibration now exhibits the following sequence:

1. same-band turnover forcing can remain phase coherent;
2. phase decoherence is not required;
3. mixing transports amplitude to the cubic-root frequency scale;
4. viscosity becomes order one in the demodulated critical amplitude;
5. a positive fraction of mass survives at the critical front;
6. the front produces a uniform positive selector charge.

Thus the relevant cost is not random phase loss. It is the
mixing--diffusion interaction at the critical cubic-root scale.

This is a calibration theorem. It does not show that every whole-space
upper-band overshoot contains a comparable shear packet.

## 13. Next live obligation: C2-MIX-BRIDGE

The smallest safe successor is to extract a portable whole-space condition.

Preferred target:

> Identify a selector-free local active-band hypothesis, stated directly in
> terms of the Navier--Stokes upper-band velocity and its deformation tensor,
> under which one threshold overshoot forces a critical mixing interval with
> selector charge at least `c/\nu`.

The condition must be weak enough to have a plausible route from the selected
equations, but strong enough to exclude the shell-ledger obstruction of L5-21.

Possible bridge variables include:

- one active packet with a persistent transverse velocity gradient;
- a lower bound on a directional deformation singular value;
- a packet-level nondegeneracy condition on the advecting phase;
- a critical-time lower bound on transported Fourier variance.

A successful bridge still would not prove A2 until the bridge hypothesis is
derived from the selected whole-space solution.

## 14. Hard rejection tests

Reject any successor that:

- promotes the periodic 2.5D calibration to the selected whole-space theorem;
- treats the positive critical charge as a contradiction to A2 for one event;
- assumes every upper-band overshoot contains a cosine shear packet;
- differentiates the moving selector;
- replaces the critical finite-viscosity result by the inviscid Bessel chain;
- reopens L3 without proving a portable equation-derived charge mechanism;
- reopens L4 from generic signed conservation.

## 15. Claim boundary

The protected claim sought from this tranche is exactly

```text
SHEAR_CHAIN_CRITICAL_SEMICLASSICAL_MASS_SURVIVAL_PROVED
__UNIFORM_POSITIVE_SELECTOR_CHARGE_LOWER_BOUND.
```

It proves, in the exact L5-23 shear calibration:

- the critical demodulated amplitude limit
  `A_0=exp(-s^3 sin^2Y/3)`;
- strong fixed-window Sobolev convergence `A_h->A_0`;
- nondegenerate scaled second and fourth Fourier moments;
- fixed positive Fourier mass at `|n|\asymp h^{-1}`;
- one critical coefficient of size at least `c h^{1/2}`;
- a threshold-violating LP block at frequency `NR^{1/3}`;
- selector lower reach `\Lambda>=cNR^{1/3}` on a full critical interval;
- a uniform positive selector-charge lower bound `c_*/\nu`.

It does not prove A2.

It does not prove that every whole-space overshoot realizes this mechanism.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
