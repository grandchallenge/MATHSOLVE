# NS-CI-R014-A2-L5-27 — critical shear-packet normal-form bridge

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor:
  `68a74e1af2ce1bb1453bf1c9cc9c313a0f6c3bb2`
- Result:
  `CRITICAL_SHEAR_PACKET_NORMAL_FORM_BRIDGE_PROVED__WHOLE_SPACE_DERIVATION_REMAINS_OPEN`
- A2 theorem: open
- L5: active
- C2-MIX-BRIDGE: conditional selector-free bridge proved
- MATHCERT adjudication: absent
- Evidence class: conditional stability theorem for a local active packet;
  deriving the normal-form hypotheses from the selected whole-space NSE remains
  open

L5-26 proves that the exact cosine-shear calibration produces a nonvanishing
critical selector charge. The useful part of that proof is not the cosine
profile itself. It is the following normal form:

```math
\partial_s\Phi_h
+
i h^{-1}a_h(s)g(Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h
+
r_h.
```

If

- the normalized transverse phase `g` has a nontrivial gradient;
- `a_h(s)=1+O(h^2)`;
- the demodulated residual is `O(h)` on a fixed critical interval;
- the initial demodulated amplitude has nonzero mass where `g'\ne0`;
- and the packet Fourier coefficients reconstruct into physical LP blocks with
  uniform constants,

then the L5-26 argument is stable.

The demodulated critical limit is

```math
A_0(s,Y)
=
A_{\rm in}(Y)
\exp\left(
-\frac{s^3}{3}|g'(Y)|^2
\right).
```

It has a positive scaled second Fourier moment on every compact positive
critical interval. Hence a fixed positive amount of finite-`h` packet mass
lies at

```math
|n|\asymp h^{-1}=R^{1/3}.
```

The reconstructed physical packet therefore forces

```math
\Lambda(t)
\ge
cN R^{1/3}
```

throughout a critical interval and

```math
\int\Lambda(t)^2\,dt
\ge
\frac{c_*}{\nu}.
```

This is the requested portable, selector-free bridge theorem.

It is still conditional. Nothing in this tranche proves that an arbitrary
selected whole-space upper-band overshoot satisfies the normal-form contract.
That derivation is the next live obligation.

## 1. Critical packet normal-form contract

Fix one critical interval

```math
s_0\le s\le s_1,
\qquad
0<s_0<s_1<\infty.
```

Let

```math
h=R^{-1/3}.
```

A family of normalized active packets satisfies the
**critical shear-packet normal-form contract** if, after a fixed spatial
rotation, Galilean phase removal, active-frequency normalization, and
polarization projection, one scalar packet component
`\Phi_h(s,Y)` obeys

```math
\boxed{
\partial_s\Phi_h
+
i h^{-1}a_h(s)g(Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h
+
r_h.
}
```

The contract requires constants independent of `h` such that:

### NF1 — smooth nondegenerate transverse phase

For some fixed integer `k\ge4`,

```math
g\in C^{k+2}(\mathbb T;\mathbb R),
\qquad
\|g\|_{C^{k+2}}\le C_g.
```

There is a fixed initial demodulated amplitude
`A_{\rm in}\in H^k(\mathbb T)` with

```math
\boxed{
\int_{\mathbb T}
|g'(Y)|^2
|A_{\rm in}(Y)|^2\,dY
\ge
m_{\rm nd}>0.
}
```

This is the transverse-deformation nondegeneracy.

### NF2 — critical shear strength

The scalar coefficient satisfies

```math
\boxed{
\sup_{0\le s\le s_1}
|a_h(s)-1|
\le
C_a h^2.
}
```

The `h^2` accuracy matches the exact decaying-shear calibration but is not
otherwise tied to the cosine profile.

### NF3 — demodulated initial stability

Define the exact packet phase

```math
q_h(s)
=
h^{-1}
\int_0^s a_h(\sigma)\,d\sigma,
\qquad
p_h(s)=h q_h(s).
```

Write

```math
\Phi_h
=
e^{-iq_h(s)g(Y)}
A_h.
```

The initial amplitude satisfies

```math
\boxed{
\|A_h(0)-A_{\rm in}\|_{H^k}
\le
C_{\rm in}h.
}
```

### NF4 — small demodulated residual

Let

```math
\widetilde r_h
=
e^{iq_hg}r_h.
```

Require

```math
\boxed{
\int_0^{s_1}
\|\widetilde r_h(s)\|_{H^k}\,ds
\le
C_rh.
}
```

The residual may contain pressure, non-shear velocity components, packet
localization errors, and neighboring-band interactions. The theorem uses only
this demodulated bound.

### NF5 — physical packet reconstruction

Let the physical active scale be `N` and packet amplitude scale

```math
A_{\rm phys}
=
R\nu N
=
h^{-3}\nu N.
```

For every normalized Fourier coefficient of `\Phi_h` at index
`|n|\asymp h^{-1}`, the fixed physical packet reconstruction and LP
partition must supply at least one physical velocity block satisfying

```math
\boxed{
\lambda_p
\asymp
Nh^{-1},
\qquad
\|u_p\|_\infty
\ge
c_{\rm rec}
A_{\rm phys}
|\widehat{\Phi_h}(n)|.
}
```

The constants are independent of `R`.

NF5 does not mention the dissipation selector. The bridge is therefore
selector-free.

## 2. Exact demodulated equation

Because

```math
q_h'
=
h^{-1}a_h(s),
```

the fast potential cancels exactly.

For a general real phase `g`,

```math
\partial_Y
(e^{-iq_hg}A_h)
=
e^{-iq_hg}
(
\partial_YA_h-iq_hg'A_h
).
```

A second derivative gives

```math
\partial_Y^2
(e^{-iq_hg}A_h)
=
e^{-iq_hg}
\left[
\partial_Y^2A_h
-
2iq_hg'\partial_YA_h
-
iq_hg''A_h
-
q_h^2(g')^2A_h
\right].
```

Therefore

```math
\boxed{
\begin{aligned}
\partial_sA_h
={}&
h^2\partial_Y^2A_h
-
2ihp_hg'\partial_YA_h
-
ihp_hg''A_h
\\
&-
p_h^2(g')^2A_h
-
h^2A_h
+
\widetilde r_h.
\end{aligned}
}
```

NF2 gives

```math
p_h(s)
=
\int_0^s a_h(\sigma)\,d\sigma
=
s+O(h^2)
```

uniformly on the fixed critical interval.

## 3. Universal critical limit

Set

```math
L_0(s)
=
-s^2(g')^2.
```

The limiting equation is

```math
\partial_sA_0
=
-s^2(g')^2A_0,
\qquad
A_0(0)=A_{\rm in}.
```

Thus

```math
\boxed{
A_0(s,Y)
=
A_{\rm in}(Y)
\exp\left(
-\frac{s^3}{3}|g'(Y)|^2
\right).
}
```

This reduces to L5-26 when
`g(Y)=\cos Y` and `A_{\rm in}=1`.

## 4. Uniform Sobolev stability

On `0\le s\le s_1`, `p_h` is uniformly bounded.

For fixed `k`, differentiated energy estimates for the demodulated equation
give

```math
\frac d{ds}
\|A_h\|_{H^k}^2
+
c h^2
\|A_h\|_{H^{k+1}}^2
\le
C
\|A_h\|_{H^k}^2
+
C
\|\widetilde r_h\|_{H^k}^2.
```

The top first-order term has coefficient `O(h)` and is absorbed by the
`h^2` diffusion through Young's inequality. All coefficient commutators are
bounded by NF1.

Using NF3--NF4 and Gronwall,

```math
\boxed{
\sup_{0\le s\le s_1}
\|A_h(s)\|_{H^k}
\le
C.
}
```

## 5. Strong convergence of the bridge packet

Let

```math
W_h=A_h-A_0.
```

The fixed smooth limit `A_0` satisfies

```math
\|(L_h-L_0)A_0\|_{H^{k-2}}
\le
Ch,
```

because

- the first-order and imaginary zeroth-order terms carry a factor `h`;
- `p_h^2-s^2=O(h^2)`;
- diffusion and the `-h^2` term are `O(h^2)`.

Together with NF3 and NF4, the same uniform energy estimate yields

```math
\boxed{
\sup_{0\le s\le s_1}
\|A_h(s)-A_0(s)\|_{H^{k-2}}
\le
Ch.
}
```

The loss of two fixed derivatives is harmless because `k\ge4`.

## 6. Nondegenerate critical Fourier moments

Write

```math
\Phi_h(s,Y)
=
\sum_n
c_n^{(h)}(s)e^{inY}.
```

Multiplication by the phase is unitary in `L^2`, so

```math
\sum_n|c_n^{(h)}|^2
=
\|A_h\|_2^2
\longrightarrow
E_0(s)
=
\|A_0(s)\|_2^2.
```

Also,

```math
h\partial_Y\Phi_h
=
e^{-iq_hg}
\left(
h\partial_YA_h
-
ip_hg'A_h
\right),
```

hence

```math
\boxed{
h^2
\sum_n n^2|c_n^{(h)}|^2
\longrightarrow
M_2(s)
=
s^2
\|g'A_0(s)\|_2^2.
}
```

Similarly,

```math
\boxed{
h^4
\sum_n n^4|c_n^{(h)}|^2
\longrightarrow
M_4(s)
=
s^4
\|(g')^2A_0(s)\|_2^2.
}
```

The convergence is uniform on
`[s_0,s_1]`.

By NF1 and the explicit positive damping factor,

```math
\inf_{s\in[s_0,s_1]}
M_2(s)
>
0.
```

The zeroth mass is uniformly positive and the fourth moment uniformly finite.

## 7. Fixed positive critical-band mass

Normalize

```math
\pi_n^{(h,s)}
=
\frac{|c_n^{(h)}(s)|^2}
{\sum_m|c_m^{(h)}(s)|^2}
```

and set

```math
X=(hn)^2.
```

The moment bounds give constants

```math
0<m_*\le\mathbb E[X],
\qquad
\mathbb E[X^2]\le M_*<\infty
```

uniformly on the critical interval for all sufficiently small `h`.

Paley--Zygmund gives fixed positive mass above a fixed lower
`|hn|` cutoff. Fourth-moment Markov gives a fixed upper cutoff.

Therefore there exist

```math
0<C_-<C_+<\infty,
\qquad
m_{\rm band}>0
```

such that

```math
\boxed{
\sum_{C_-\le|hn|\le C_+}
|c_n^{(h)}(s)|^2
\ge
m_{\rm band}
}
```

for every
`s\in[s_0,s_1]`.

## 8. Critical coefficient and LP threshold

The fixed scaled band contains `O(h^{-1})` integer indices. Hence for each
critical time there is an index `n_h(s)` with

```math
\boxed{
|c_{n_h(s)}^{(h)}(s)|
\ge
c h^{1/2}.
}
```

NF5 then produces a physical block with

```math
\lambda_p
\asymp
Nh^{-1}
```

and

```math
\|u_p\|_\infty
\ge
c
h^{-3}\nu N
h^{1/2}.
```

Therefore

```math
\boxed{
\lambda_p^{-1}
\|u_p\|_\infty
\ge
c\nu h^{-3/2}.
}
```

For sufficiently small `h`, that block violates the fixed campaign
strict-high threshold.

Thus the actual dissipation selector satisfies

```math
\boxed{
\Lambda(t)
\ge
cN h^{-1}
=
cN R^{1/3}
}
```

throughout the critical interval.

No selector motion hypothesis is used.

## 9. Portable selector-charge lower bound

The bridge normalization is the same as the shear calibration:

```math
s
=
hAN(t-t_0),
\qquad
A=R\nu N=h^{-3}\nu N.
```

Hence

```math
dt
=
\frac{h^2}{\nu N^2}\,ds.
```

Combining with the selector lower bound,

```math
\boxed{
\int_{I_{\rm crit}}
\Lambda(t)^2\,dt
\ge
\frac{c_*}{\nu},
}
```

where `c_*>0` depends only on the fixed normal-form constants and
`[s_0,s_1]`, not on `R`.

This is the portable conditional charge theorem.

## 10. Why this is materially stronger than the calibration alone

The theorem no longer requires:

- the cosine phase;
- exact phase locking;
- zero residual;
- exact passive-scalar reduction;
- the exact Bessel chain.

It tolerates:

- any fixed smooth transverse phase with nonzero gradient on packet mass;
- `O(h^2)` critical shear-strength modulation;
- `O(h)` demodulated equation residual;
- `O(h)` initial-amplitude perturbation.

Thus the critical selector charge is structurally stable under a concrete
class of active-packet perturbations.

The theorem is still conditional because NF1--NF5 have not been derived from
an arbitrary selected whole-space overshoot.

## 11. Relation to previous closures

The bridge does not reopen the closed generic routes.

- It does not use turnover residence alone, so it does not reopen L3 by fiat.
- It does not use generic signed shell conservation, so it does not reopen L4.
- It excludes the L5-21 shell-ledger fixture because that fixture has no
  physical packet satisfying the transverse-phase normal form and
  reconstruction contract.
- It does not require phase decoherence, consistent with L5-22/L5-23.

The new object is a local deformation-driven packet normal form.

## 12. Next live obligation: C2-MIX-DERIVE

The smallest safe successor is no longer another calibration.

It is:

> Derive, weaken, or rigorously separate NF1--NF5 from the selected
> whole-space upper-band Navier--Stokes equations near a threshold overshoot.

The first audit should decompose the five hypotheses by source:

- NF1: can a transverse phase/deformation direction be extracted from the
  active packet without a geometric nondegeneracy assumption?
- NF2: can active-scale normalization make the leading advecting coefficient
  constant to critical accuracy?
- NF3: is a stable demodulated packet initialization automatic after choosing
  the critical start time?
- NF4: can pressure, localization, neighboring-band, and genuinely 3D errors
  be bounded by `O(h)` in the demodulated norm from A2/Leray data?
- NF5: which packet decomposition gives uniform reconstruction into LP
  blocks?

The likely decisive hypothesis is NF4. It must be tested first rather than
assuming the whole normal form.

## 13. Hard rejection tests

Reject any successor that:

- treats NF1--NF5 as already implied by a threshold overshoot;
- calls the conditional bridge a proof of A2;
- assumes every active packet has a nondegenerate transverse phase;
- hides pressure or 3D interaction terms inside an unproved `O(h)` residual;
- differentiates the moving selector;
- uses the bridge charge to reopen L3 without deriving the bridge hypotheses;
- imports generic signed-flux cancellation from L4.

## 14. Claim boundary

The protected claim sought from this tranche is exactly

```text
CRITICAL_SHEAR_PACKET_NORMAL_FORM_BRIDGE_PROVED
__WHOLE_SPACE_DERIVATION_REMAINS_OPEN.
```

It proves:

- a general critical packet normal form sufficient for the L5-26 mechanism;
- strong convergence to the universal damped critical amplitude;
- positive critical semiclassical mass for any nondegenerate smooth transverse
  phase;
- threshold reach at `NR^{1/3}`;
- a selector-charge lower bound `c_*/\nu`;
- stability under explicit `O(h)` demodulated residual and initialization
  perturbations.

It does not prove NF1--NF5 for selected whole-space solutions.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
