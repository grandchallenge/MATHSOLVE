GCL-CONTRIBUTION-DISPATCH/1

# NSCI-C2-B-COOP-001 — Assignment B

## Your entire work-set

This GitHub issue is your complete operational and mathematical context.

You must do exactly four things:

1. Read this issue only.
2. Work on Assignment B for at most 22 minutes.
3. Post exactly one GitHub issue comment in the required `GCL-CONTRIBUTION-RESULT/1` format stated at the end of this issue.
4. Stop.

Do not create branches, pull requests, files, commits, issues, notes, attachments, images, notebooks, scripts, or supplementary documents. Do not edit this issue. Do not inspect other issues or repository material. Do not use external URLs or sources. Do not ask for additional context. If the mathematics cannot be completed, return `BLOCKED` with the exact blocker.

Dispatch ID: `NSCI-C2-B-COOP-001`
Assignment: `B`
Concurrency mode: `cooperative_claimed`
Context class required: `ZERO_CONTEXT`
External sources: `NONE`
Wall-clock limit: `22 minutes`

The source mathematical handoff was frozen at:

`grandchallenge/MATHSOLVE@490bb2da6b6d315193c86ae934a49241735d027c:handoffs/NS-CI-001/C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE_ZERO_CONTEXT.md`

Source handoff blob: `e49bf0c5b88567ea50a91e655b631cdc4f83daeb`

Source handoff SHA-256: `6b975cf1cfa17cf61e8f44350eb9ed41cef88876bae35555234e961ec2adbdb5`

You do not need to open that source. Its relevant mathematical content is reproduced below.

## Isolation contract

This is a zero-context comparison contribution. Do not inspect blind-cohort issues or results. Do not search repository history or external sources. Work only from this bootstrap plus standard mathematical facts.

---

# C2-MIX-DIRECTION-COMPRESSION-LEDGER-CHARGE
## Zero-context independent-agent handoff

### Read this first

This file is intentionally self-contained.

You do **not** need prior knowledge of GCL, MATHSOLVE, NS-CI, or any preceding conversation. Treat campaign labels as names only. The mathematical problem, all protected inputs needed for the work, the prohibited shortcuts, and the time-boxed assignments are stated below.

Do not spend your time reconstructing institutional context. Do not infer that a prior result proves more than is written here. Work only from the mathematical inputs in this document plus standard mathematical facts you can derive yourself.

For this assignment, a useful result is any one of:

1. a correct conditional lemma that materially advances the stated goal;
2. a correct counterexample or separator showing a proposed implication is false under the stated inputs;
3. a sharp reduction that identifies the smallest additional hypothesis needed for a desired implication.

A negative result is fully acceptable if it is exact.

---

## 1. One-sentence goal

Determine whether the **compression ledger**

\[
C_2^- = Q_2(S)+C_2^+-P_{\rm tot}+2D_4
\]

can be converted into a **physical Littlewood-Paley threshold event and dissipation-selector charge**, by proving that large compression must either produce reconstructible critical Fourier mass or pay another controlled physical cost.

The immediate priority is the pair

\[
D_4
\qquad\text{and}\qquad
Q_2/Q_4\text{ reconstruction}.
\]

Expansion and the signed phase source are secondary escape channels that must also be audited.

---

## 2. Global PDE setting

The parent problem is the three-dimensional incompressible Navier-Stokes equation on \(\mathbb R^3\), unforced, with viscosity \(\nu>0\), in the Leray-Hopf class.

The restricted hypothesis is a dissipation-wavenumber condition

\[
\Lambda\in L_t^2.
\]

The target theorem is not proved.

The campaign seeks to show that a genuinely dangerous high-frequency episode must pay a fixed amount of the finite quantity

\[
\int \Lambda(t)^2\,dt.
\]

The local packet analysis below is one route toward that objective.

You are **not** being asked to prove global regularity or the full parent theorem in one short assignment.

---

## 3. What a selector charge means here

The established conditional packet mechanism has the following form.

Let \(h\to0\) be the small semiclassical parameter for a selected packet, and let \(N\) be its carrier scale. If a normalized packet has fixed positive Fourier mass in a scaled annulus

\[
c_-\le |hn|\le c_+,
\]

then the annulus contains only \(O(h^{-1})\) integer modes, so at least one Fourier coefficient satisfies

\[
|c_n|\gtrsim h^{1/2}.
\]

Under the established physical reconstruction contract, such a coefficient gives a physical LP block at frequency

\[
\lambda_p\asymp Nh^{-1}
\]

with amplitude large enough to violate the strict-high threshold that defines the dissipation selector. Therefore

\[
\Lambda(t)\gtrsim Nh^{-1}
\]

throughout the corresponding critical packet interval.

The critical time scaling is

\[
dt=\frac{h^2}{\nu N^2}\,ds.
\]

Hence a fixed positive \(s\)-interval on which the threshold is violated gives

\[
\int_{I_{\rm crit}}\Lambda(t)^2\,dt
\ge \frac{c_*}{\nu},
\]

where \(c_*>0\) is independent of the overshoot size.

This fixed \(c_*/\nu\) lower bound is the relevant **selector charge**.

The missing problem is to derive the hypotheses needed for this reconstruction from the compression ledger rather than assume them.

---

## 4. The characteristic-frame variables

The local packet is written in a one-dimensional transverse characteristic coordinate.

Let the direction transport field be \(v(s,Y)\), and let

\[
\partial_s\chi(s,Z)=v(s,\chi(s,Z)),
\qquad
\chi(0,Z)=Z.
\]

Define the Jacobian

\[
J(s,Z)=\partial_Z\chi(s,Z)>0.
\]

Then

\[
\partial_s\log J
=
\alpha(s,Z),
\qquad
\alpha(s,Z):=(\partial_Yv)(s,\chi(s,Z)).
\]

Split

\[
\alpha=\alpha_+-\alpha_-,
\qquad
\alpha_+=(\alpha)_+,
\qquad
\alpha_-=(-\alpha)_+.
\]

Thus \(\alpha_-\) is compression and \(\alpha_+\) is expansion.

The packet carries an accumulated phase \(F(s,Z)\). Write

\[
H:=F_Z.
\]

For the limiting packet,

\[
F_s=G(s,\chi(s,Z)),
\]

hence

\[
H_s
=
J\,(\partial_YG)(s,\chi(s,Z)).
\]

Let \(A(s,Z)\) be the limiting complex amplitude and

\[
R:=|A|^2.
\]

The established amplitude equation is

\[
A_s=-J^{-2}H^2A,
\]

so

\[
R_s=-2J^{-2}H^2R.
\]

All formulas in this handoff use this limiting first-order packet system unless explicitly stated otherwise.

---

## 5. The physical second- and fourth-moment densities

Define

\[
q_2
=
J^{-1}H^2R
\]

and

\[
q_4
=
J^{-3}H^4R.
\]

Define the total moments

\[
Q_2(s)=\int q_2(s,Z)\,dZ,
\qquad
Q_4(s)=\int q_4(s,Z)\,dZ.
\]

These are not arbitrary bookkeeping variables.

Under the bounded smooth characteristic-frame transfer theorem, they are the limits of the physical scaled Fourier moments:

\[
h^2\sum_n n^2|c_n^{(h)}(s)|^2
\longrightarrow Q_2(s),
\]

and

\[
h^4\sum_n n^4|c_n^{(h)}(s)|^2
\longrightarrow Q_4(s).
\]

The corresponding zeroth mass is

\[
M_0(s)
=
\lim_{h\to0}\sum_n|c_n^{(h)}(s)|^2
=
\int J|A|^2\,dZ,
\]

and is positive under the established bounded-frame normal form.

Therefore \(Q_2\) and \(Q_4\) are exactly the moments needed by the existing critical-band reconstruction.

---

## 6. The established critical-band moment lemma

At a fixed time, normalize the physical Fourier mass by

\[
\pi_n
=
\frac{|c_n|^2}{\sum_m|c_m|^2},
\]

and define the nonnegative random variable

\[
X=(hn)^2.
\]

Then

\[
\mathbb E[X]
=
\frac{h^2\sum n^2|c_n|^2}
{\sum |c_n|^2},
\]

and

\[
\mathbb E[X^2]
=
\frac{h^4\sum n^4|c_n|^2}
{\sum |c_n|^2}.
\]

If, uniformly in a time interval,

\[
M_0\ge m_0>0,
\qquad
Q_2\ge m_2>0,
\qquad
Q_4\le m_4<\infty,
\]

then Paley-Zygmund provides fixed positive mass above a fixed lower scaled frequency, while fourth-moment Markov provides a fixed upper scaled-frequency cutoff. Consequently there exist constants

\[
0<c_-<c_+<\infty,
\qquad
m_{\rm band}>0,
\]

such that

\[
\sum_{c_-\le |hn|\le c_+}|c_n|^2
\ge m_{\rm band}
\]

uniformly on the interval for sufficiently small \(h\).

This is enough for the selector-charge mechanism in Section 3.

Important: the compression ledger below does **not** automatically provide uniform positive \(Q_2\) and uniform bounded \(Q_4\). That gap is the present problem.

---

## 7. Exact compression production law

Differentiating

\[
q_2=J^{-1}H^2R
\]

and using

\[
(J^{-1})_s=-\alpha J^{-1},
\]

\[
(H^2)_s
=
2HJ(\partial_YG)\circ\chi,
\]

and

\[
R_s=-2J^{-2}H^2R
\]

gives the exact identity

\[
\boxed{
\partial_s q_2
=
\alpha_-q_2
-
\alpha_+q_2
+
P
-
2q_4,
}
\]

where

\[
P
=
2H\,((\partial_YG)\circ\chi)\,R.
\]

Interpretation:

- \(\alpha_-q_2\) is exact positive production by compression;
- \(-\alpha_+q_2\) is exact removal by expansion;
- \(P\) is a signed phase-gradient source;
- \(-2q_4\) is exact fourth-moment damping.

The actual \(q_2\) is therefore **source-driven**. It is not a passively transported density.

---

## 8. Exact integrated ledger

Define

\[
C_2^-
=
\int_0^S\int \alpha_-q_2\,dZ\,ds,
\]

\[
C_2^+
=
\int_0^S\int \alpha_+q_2\,dZ\,ds,
\]

\[
P_{\rm tot}
=
\int_0^S\int P\,dZ\,ds,
\]

and

\[
D_4
=
\int_0^S Q_4(s)\,ds.
\]

The accumulated phase is initialized by \(F(0,Z)=0\), so \(H(0,Z)=0\) and

\[
Q_2(0)=0.
\]

Integrating the pointwise law gives

\[
\boxed{
C_2^-
=
Q_2(S)
+
C_2^+
-
P_{\rm tot}
+
2D_4.
}
\]

Equivalently,

\[
C_2^-
\le
Q_2(S)
+
C_2^+
+
|P_{\rm tot}|
+
2D_4.
\]

Therefore persistent compression cannot disappear. If \(C_2^-\) is large, at least one of the four ledger channels is large.

This is the current starting point.

---

## 9. Earlier compression result that should not be confused with the ledger

For an arbitrary fixed nonnegative label density \(q(Z)\), if \(\mathcal C_K^-\) is the set of labels whose characteristic Jacobian first reaches \(J=e^{-K}\), then

\[
\int_{\mathcal C_K^-}q(Z)\,dZ
\le
K^{-1}W_{q,K}^-,
\]

with

\[
W_{q,K}^-
=
\int q(Z)
\int_0^{\tau_K^-(Z)}
(-\partial_Yv(s,\chi(s,Z)))_+
\,ds\,dZ.
\]

There is no \(e^K\) loss when packet mass is retained in label space.

However, this theorem concerns a fixed transported density \(q\).

The actual \(q_2\) above is not fixed and not passively transported. Its exact source law is Section 7.

Do not substitute one statement for the other.

---

## 10. What is already known about frame distortion

A bounded smooth frame is sufficient for the critical-mixing theorem, but such boundedness has **not** been derived from the global A2/Leray scalar budgets.

In fact, coarse scalar energy, dissipation, and annular-supremum control do not give uniform all-streamline direction strain.

The intrinsic first-order geometric quantity is the actual transport variation

\[
(-\partial_Yv)_+,
\]

not a factorization-dependent quantity.

Any argument that attempts to control the frame only from coarse scalar envelopes must account for this known obstruction.

The current route is therefore not:

> prove every characteristic has uniformly bounded distortion.

It is:

> prove that distortion overlapping critical packet mass either remains harmless or pays a physical charge.

---

## 11. The exact research question for this tranche

A complete positive resolution of this tranche would establish a conditional dichotomy of the following form.

Given a selected critical packet satisfying the existing limiting characteristic-frame equations, if \(C_2^-\) is large on a critical interval, then at least one of the following holds:

1. \(Q_2\) and \(Q_4\) enter a regime that reconstructs fixed positive mass in a scaled critical annulus, yielding selector charge;
2. \(D_4\) itself controls a physical quantity that yields selector or dissipation charge;
3. the expansion term \(C_2^+\) is quantitatively controlled by a charge term or cannot persistently cancel compression;
4. the signed phase source \(P_{\rm tot}\) is quantitatively controlled by a charge term or cannot persistently cancel compression.

You are not expected to establish all four in one time box.

Your job is to advance or terminate **one** of the assignments below exactly.

---

---

## Hard wall-clock rule

Choose exactly **one** assignment.

Maximum wall-clock time: **22 minutes**.

Suggested allocation:

- 3 minutes: read the relevant assignment and restate the target;
- 14 minutes: derive, falsify, or reduce it;
- 5 minutes: write the required output.

Stop at 22 minutes even if unfinished. A precise blocker is preferable to an unverified proof sketch.

Do not spend the time searching institutional repositories, reconstructing campaign history, or producing polished prose.

---

---

## Assignment B — \(D_4\) physical-charge audit
### Priority: highest

### Target

Determine whether

\[
D_4=\int_0^S Q_4(s)\,ds
\]

can itself be converted into a physical selector/dissipation charge under the currently stated packet data, or whether an additional lower-moment or localization hypothesis is necessary.

### Inputs you may use

At each time,

\[
Q_4(s)
=
\lim_{h\to0}
h^4\sum_n n^4|c_n^{(h)}(s)|^2.
\]

The physical selector is charged only when there is enough amplitude in a critical scaled annulus to produce a threshold-violating LP block.

Large high moments can in principle arise from very small mass placed very far out in frequency.

### Questions to answer

1. Does a lower bound on \(\int Q_4\,ds\) alone force a lower bound on the measure of times at which a fixed scaled annulus carries positive mass?
2. If not, construct the cleanest spectral measure counterexample consistent with positive finite zeroth mass.
3. What additional relation among \(M_0,Q_2,Q_4\) would make \(D_4\) useful?
4. Can \(D_4\) be interpreted directly as a physically controlled dissipative quantity after restoring the packet scaling, or is it a higher moment with no immediate Leray-budget counterpart?
5. If direct selector charge fails, identify the weakest plausible “\(D_4\)-plus-something” statement worth proving next.

### Success criterion

Either a correct bridge from \(D_4\) to a physical charge with every assumption stated, or an explicit separator proving that \(D_4\) alone is insufficient, together with the minimal missing ingredient.

Do not call \(D_4\) “dissipation charge” merely because it appears with a negative sign in the amplitude equation.

---

---

# 14. Hard rejection tests

Reject your own argument if it does any of the following.

1. Treats \(q_2\) as a passively transported density.
2. Drops the signed source \(P\).
3. Calls \(q_4\) an error term rather than an exact damping channel.
4. Infers selector charge from large \(C_2^-\) without accounting for \(C_2^+\), \(P_{\rm tot}\), and \(D_4\).
5. Infers critical-band mass from a large fourth moment alone.
6. Uses only a large second moment without controlling escape to arbitrarily high frequency.
7. Uses \(\int\partial_Yv=0\) to claim \(q_2\)-weighted expansion and compression cancel favorably.
8. Assumes the bounded smooth characteristic frame has already been derived from the whole-space Navier-Stokes hypothesis.
9. Promotes a limiting packet identity to a full whole-space theorem without a finite-\(h\) reconstruction argument.
10. Claims the parent A2 theorem, regularity, certification, novelty, or priority.

---

---

# 15. What counts as a materially useful contribution

A contribution is material if it does at least one of the following.

- Gives a quantitative \(M_0,M_2,M_4\) annulus lemma with constants usable in the packet reconstruction.
- Shows precisely why terminal \(Q_2\) is insufficient without a time-persistence estimate and identifies the minimal persistence norm.
- Shows by explicit construction that \(D_4\) alone cannot imply selector charge.
- Relates \(D_4\) to a physical dissipative quantity under a stated additional packet hypothesis.
- Rewrites \(P_{\rm tot}\) into a controllable source norm plus ledger terms.
- Produces a source fixture proving such an extra norm is necessary.
- Proves or refutes a nontrivial relation between \(C_2^+\) and \(C_2^-\).
- Produces a finite-channel lemma reducing the whole tranche to one sharply named missing bound.

A vague research suggestion is not material.

---

---

# 16. Frozen provenance of this handoff

This handoff was prepared from protected repository state

\[
\texttt{fdc539ba2b79b60e458a0ab4ac1370b03a0788bc}
\]

with the active NS-CI mathematical predecessor

\[
\texttt{d69a9d46ee0444c4bb80f51434e10e4dd0a43567},
\]

which contains the protected L5-44 compression-ledger result.

At preparation time, the 20 protected-main commits after L5-44 changed other campaigns and infrastructure, not the NS-CI L5-44 mathematical files. Thus the L5-44 predecessor remains the relevant mathematical state for this tranche.

The protected prior results used in this handoff are:

- L5-27: conditional critical packet normal form gives physical critical-band reconstruction and fixed selector charge \(c_*/\nu\);
- L5-35: bounded smooth characteristic deformation preserves the physical scaled zeroth/second/fourth moment reconstruction;
- L5-43: packet-weighted first-hit compression removes the earlier exponential change-of-variables loss for a fixed transported density;
- L5-44: the actual critical second-moment density has the exact source law and four-channel compression ledger stated above.

No other campaign document is required to execute Assignments A-E.

---

---

# Required GitHub return

Post exactly one issue comment. The comment must contain exactly these top-level sections in this order and no other `##` sections:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: NSCI-C2-B-COOP-001
assignment: B
disposition: PROVED | REFUTED | REDUCED | BLOCKED
context_class: ZERO_CONTEXT
external_sources: NONE
timebox_observed: YES | NO

## Strongest exact statement

<result>

## Derivation

<complete checkable derivation>

## Assumptions beyond bootstrap

NONE

## Verification / falsification hooks

<at least one concrete check>

## Claim boundary

<what this does not prove>

## Next residual

<at most three sentences>
```

No attachments. No links. No images. No code files. No second comment containing mathematical additions. If your first comment is mechanically rejected, submit one complete replacement comment; do not edit the rejected comment.

Your comment is evidence only. It does not constitute GCL adjudication, Referee acceptance, MATHCERT certification, Council action, Human Steward action, canonical admission, novelty determination, or publication authorization.
