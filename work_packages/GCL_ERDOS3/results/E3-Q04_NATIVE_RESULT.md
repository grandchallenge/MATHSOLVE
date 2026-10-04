# E3-Q04 — aligned Fourier-or-fourfold witness dichotomy

Disposition: **PROVED_NATIVE_JOINT_WITNESS_DICHOTOMY**.

This is native GCL work. It refines E3-Q03 by retaining the actual mixed correlation that forces structure instead of collapsing it immediately to a scalar \(U^3\) norm.

## Strongest exact statement

Use the E3-Q02 cyclic embedding for any valid adjacent \(0011\) family
\[
F_1=(0,0,0011),\qquad
F_4=(1,0,0011),\qquad
F_7=(2,0,0011).
\]

Let the two physical fibres used by the chosen family have density at least \(\beta\) in their length-\(N\) blocks. Let
\[
C_0,C_1,C_2,C_3\subseteq G:=\mathbb Z/P\mathbb Z,
\qquad 8N<P<16N,
\]
be the four labelled translated sets from Q02, and write
\[
1_{C_t}=\rho_t+g_t,\qquad \mathbb E g_t=0.
\]

If the physical gluing is globally 4-AP-free, then one of the following two alternatives holds.

### Linear witness alternative

There exists a triple of labelled positions
\[
S=\{t_1<t_2<t_3\}\subseteq\{0,1,2,3\}
\]
such that
\[
\left|
\mathbb E_{x,d}
\prod_{t\in S}g_t(x+td)
\right|
\ge
\frac{1}{5}\prod_{t\in S}\rho_t
>
\frac{\beta^3}{5\cdot16^3}.
\]

Moreover there exists a **nonzero common frequency parameter**
\[
r\in\mathbb Z/P\mathbb Z\setminus\{0\}
\]
such that, with normalized Fourier transform
\[
\widehat f(\xi)=\mathbb E_x f(x)e_P(-\xi x),
\]
the three linked Fourier coefficients
\[
\widehat g_{t_1}\!\big((t_2-t_3)r\big),\qquad
\widehat g_{t_2}\!\big((t_3-t_1)r\big),\qquad
\widehat g_{t_3}\!\big((t_1-t_2)r\big)
\]
all have magnitude at least
\[
\boxed{
\left(\frac{\beta^3}{5\cdot16^3}\right)^3
=
\frac{\beta^9}{5^3\,16^9}.
}
\]

Thus the triple case supplies an explicitly **aligned** Fourier witness shared by the two physical fibres, not merely independent large Fourier coefficients.

### Quadratic/joint-fourfold alternative

The fully balanced fourfold correlation satisfies
\[
\boxed{
\left|
\Lambda(g_0,g_1,g_2,g_3)
\right|
\ge
\frac{\rho_0\rho_1\rho_2\rho_3}{5}
>
\frac{\beta^4}{5\cdot16^4}.
}
\]

This correlation itself is a joint degree-2 witness. In particular generalized von Neumann gives
\[
\|g_t\|_{U^3}
>
\frac{\beta^4}{5\cdot16^4}
\qquad(t=0,1,2,3).
\]

For an adjacent \(0011\) family, these four labelled positions are translations of only two physical fibres, so both physical fibres participate in the same large fourfold correlation.

Therefore every adjacent pair
\[
(B_0,B_1),\qquad(B_1,B_2),\qquad(B_2,B_3)
\]
comes with either:
1. an explicit common-frequency Fourier relation; or
2. a large joint fourfold correlation.

This is a finite witness-level interface for the current GCL residual.

It does not yet imply a point-deletion lower bound.

## Proof

### 1. Five-term cancellation

Q03 proves that singleton and pair balanced terms vanish exactly. Therefore
\[
0
=
\rho_0\rho_1\rho_2\rho_3
+
\sum_{|S|=3}\rho_{S^c}\Lambda_S
+
\Lambda_{\{0,1,2,3\}},
\]
where \(S^c\) is the unique omitted position for a triple.

Hence either the fourfold term has magnitude at least
\[
\rho_0\rho_1\rho_2\rho_3/5,
\]
or one of the four weighted triple terms does:
\[
\rho_{S^c}|\Lambda_S|
\ge
\rho_0\rho_1\rho_2\rho_3/5.
\]

In the latter case,
\[
|\Lambda_S|
\ge
\frac15\prod_{t\in S}\rho_t.
\]

Since each \(\rho_t>\beta/16\),
\[
|\Lambda_S|>\frac{\beta^3}{5\cdot16^3}.
\]

This proves the correlation dichotomy.

### 2. Fourier form of a triple correlation

Let
\[
S=\{t_1<t_2<t_3\}.
\]

Expanding the three functions in Fourier series and averaging over \(x,d\) imposes the two linear constraints
\[
\xi_1+\xi_2+\xi_3=0,
\]
\[
t_1\xi_1+t_2\xi_2+t_3\xi_3=0.
\]

Their solution space is one-dimensional. Writing its parameter as \(r\),
\[
(\xi_1,\xi_2,\xi_3)
=
\big(
(t_2-t_3)r,\,
(t_3-t_1)r,\,
(t_1-t_2)r
\big).
\]

Thus
\[
\Lambda_S
=
\sum_{r\in G}
a_r b_r c_r,
\]
where
\[
a_r=\widehat g_{t_1}((t_2-t_3)r),
\]
\[
b_r=\widehat g_{t_2}((t_3-t_1)r),
\]
\[
c_r=\widehat g_{t_3}((t_1-t_2)r).
\]

Parseval gives
\[
\sum_r|a_r|^2,\quad
\sum_r|b_r|^2,\quad
\sum_r|c_r|^2
\le1
\]
because \(|g_t|\le1\).

Let
\[
M:=\max_r|a_rb_rc_r|.
\]

Then
\[
|a_rb_rc_r|
\le
M^{1/3}|a_rb_rc_r|^{2/3}.
\]

Summing and applying Hölder,
\[
\sum_r|a_rb_rc_r|
\le
M^{1/3}
\left(\sum_r|a_r|^2\right)^{1/3}
\left(\sum_r|b_r|^2\right)^{1/3}
\left(\sum_r|c_r|^2\right)^{1/3}
\le
M^{1/3}.
\]

Therefore
\[
M\ge|\Lambda_S|^3.
\]

So there exists \(r\) with
\[
|a_rb_rc_r|
\ge
|\Lambda_S|^3.
\]

Every Fourier coefficient of a bounded function has magnitude at most \(1\). Hence each of the three factors individually has magnitude at least
\[
|\Lambda_S|^3
>
\frac{\beta^9}{5^3\,16^9}.
\]

Finally, \(r\ne0\): at \(r=0\) all three coefficients are \(\widehat g_t(0)=\mathbb E g_t=0\).

This proves the aligned nonzero-frequency witness.

## Exact multiplier patterns

The four possible triple-position sets give:

\[
\{0,1,2\}:
\quad(-r,\,2r,\,-r),
\]

\[
\{0,1,3\}:
\quad(-2r,\,3r,\,-r),
\]

\[
\{0,2,3\}:
\quad(-r,\,3r,\,-2r),
\]

\[
\{1,2,3\}:
\quad(-r,\,2r,\,-r).
\]

For an \(0011\) physical pattern \((A,A,B,B)\), a triple witness therefore forces one of the following:
- \(A\) has large coefficients at linked modes \(r,2r\), while \(B\) has one at \(r\);
- \(A\) has linked modes \(2r,3r\), while \(B\) has one at \(r\);
- \(B\) has linked modes \(2r,3r\), while \(A\) has one at \(r\);
- \(B\) has linked modes \(r,2r\), while \(A\) has one at \(r\),

up to signs and translation phases.

The translations introduced by the carry embedding multiply Fourier coefficients by unit-modulus phase factors and therefore preserve both frequency locations and magnitudes.

## What this changes

E3-Q03 established that every physical fibre has scalar \(U^3\) structure.

Q04 shows that the forcing mechanism contains strictly more information:
- in the triple regime, it gives a common nonzero frequency parameter and exact harmonic multipliers across the two fibres;
- in the fourfold regime, it gives a large joint four-function correlation before any inverse theorem is applied.

Thus the current native residual should not apply a \(U^3\) inverse theorem independently to each fibre and then try to compare arbitrary chosen phases. The better object is the **joint correlation witness already present in the carry equation**.

## First defect

The remaining theorem is now a finite witness-compatibility problem across the L01 core.

For each core family, select one of:
- a triple/Fourier witness with its exact multiplier relation; or
- a large fourfold degree-2 correlation.

Prove that these witness choices cannot all be realized by four near-extremal locally 4-AP-free fibres across many scales/locations without a deletion cost
\[
\gtrsim\beta^{1+\theta}N,
\qquad \theta<1.
\]

The missing amplification is quantitative: finitely many large correlations at one scale do not by themselves force enough independent Fourier modes or quadratic complexity to beat the target exponent.

## Frontier effect

- E3-Q4-DENSITY-LOSS remains **OPEN**.
- E3-B-FOUR-FIBRE-DEFICIT remains **OPEN_NATIVE_SUBTARGET**.
- E3-B-ALL-FIBRE-U3-FORCING remains **PROVED_NATIVE**.
- The live native residual is sharpened from generic joint witness alignment to a **finite linear-vs-quadratic correlation-witness compatibility problem**.
- No parent theorem or gluing-radius candidate is promoted.
