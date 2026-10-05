# E3-Q13 — controlled dyadic extraction from the Q11 density increment

Disposition: **PROVED_NATIVE_DYADIC_EXTRACTION_WITH_EXPONENT4_BARRIER**.

This is native GCL work. It sharpens the low-order Q11 arm by converting the arbitrary short-step progression into a genuine dyadic extremal comparison with controlled scale loss.

## Strongest exact statement

Assume Q11 produces, inside one physical fibre \(B_j\subseteq[0,N-1]\) with \(N=2^n\), an arithmetic-progression segment

\[
J=\{u_0,u_0+q,\ldots,u_0+(M-1)q\},
\qquad q\in\{1,2,3\},
\]

such that, writing

\[
\alpha_j:=\frac{|B_j|}{N},
\qquad
\delta_\beta:=\frac{\beta^4}{15\cdot16^4},
\]

one has

\[
|B_j\cap J|-\alpha_jM
>
10\delta_\beta N.
\]

Set

\[
e_\beta:=10\delta_\beta
=
\frac{2}{3\cdot16^4}\beta^4.
\]

Assume only

\[
e_\beta N\ge4.
\]

Then there exists an integer \(k\ge0\) and a subprogression

\[
J'\subseteq J
\]

with the same common difference \(q\), exactly \(2^k\) points, and

\[
\boxed{
2^k>\frac{e_\beta}{4}N
}
\]

such that

\[
\boxed{
\frac{|B_j\cap J'|}{2^k}
>
\alpha_j+\frac{e_\beta}{2}.
}
\]

Equivalently,

\[
\boxed{
a_k:=\frac{r_4(2^k)}{2^k}
>
\alpha_j+\frac{\beta^4}{3\cdot16^4}.
}
\]

The scale loss obeys

\[
\boxed{
n-k
<
\log_2\!\left(\frac4{e_\beta}\right)
=
4\log_2\!\frac1\beta
+
16+\log_2 6.
}
\]

Thus Q11 yields an exact **variable-scale dyadic density increment**:

\[
a_k-\alpha_j
>
\frac{\beta^4}{3\cdot16^4}
\]

at a previous dyadic scale no farther than

\[
O(\log(1/\beta))
\]

indices away.

## Proof

Affine-rescale the Q11 progression \(J\) by

\[
u_0+\ell q\longmapsto \ell.
\]

The image

\[
A\subseteq\{0,\ldots,M-1\}
\]

is still 4-AP-free, and

\[
E
:=
|A|-\alpha_jM
>
e_\beta N.
\]

Since each point contributes at most \(1\) to positive discrepancy,

\[
M\ge E.
\]

In particular \(E\ge4\).

Choose a power of two

\[
L=2^k
\]

such that

\[
\frac E4<L\le\frac E2.
\]

Such a power exists for every \(E\ge4\).

Partition \(\{0,\ldots,M-1\}\) into consecutive full blocks of length \(L\) and one final remainder block of length \(<L\).

The discrepancy of the remainder is at most its length, hence strictly less than

\[
L\le E/2.
\]

Therefore the full length-\(L\) blocks carry total discrepancy greater than

\[
E/2.
\]

There are at most

\[
M/L\le N/L
\]

full blocks. Hence one full block \(Q\) has discrepancy greater than

\[
\frac{E/2}{N/L}
=
\frac{EL}{2N}.
\]

Dividing by \(L\),

\[
\frac{|A\cap Q|}{L}-\alpha_j
>
\frac{E}{2N}
>
\frac{e_\beta}{2}.
\]

Pull \(Q\) back through the affine rescaling. This gives a subprogression \(J'\subseteq J\) with common difference \(q\), length \(L=2^k\), and

\[
\frac{|B_j\cap J'|}{2^k}
>
\alpha_j+\frac{e_\beta}{2}.
\]

Because affine rescaling preserves 4-term arithmetic progressions, the image of \(B_j\cap J'\) is a 4-AP-free subset of an interval of length \(2^k\). Therefore

\[
a_k
=
\frac{r_4(2^k)}{2^k}
\ge
\frac{|B_j\cap J'|}{2^k}
>
\alpha_j+\frac{e_\beta}{2}.
\]

Also

\[
2^k=L>\frac E4>\frac{e_\beta}{4}N.
\]

Since \(N=2^n\),

\[
2^{k-n}>\frac{e_\beta}{4},
\]

hence

\[
n-k<\log_2\frac4{e_\beta}.
\]

Finally

\[
e_\beta
=
\frac{2}{3\cdot16^4}\beta^4
\]

gives

\[
\frac4{e_\beta}
=
6\cdot16^4\,\beta^{-4},
\]

so

\[
\log_2\frac4{e_\beta}
=
4\log_2\frac1\beta+16+\log_2 6.
\]

## Near-extremal comparison

If the fibre deficit is

\[
\varepsilon_j
:=
a_n-\alpha_j\ge0,
\]

then Q13 gives

\[
\boxed{
a_k
>
a_n-\varepsilon_j
+\frac{\beta^4}{3\cdot16^4}.
}
\]

If in addition

\[
\beta\ge a_n/2,
\]

then

\[
\boxed{
a_k
>
a_n-\varepsilon_j
+\frac{a_n^4}{48\cdot16^4}.
}
\]

This identifies the exact quantitative barrier in the low-order arm.

The campaign target seeks a gluing deficit at scale

\[
a_n^{1+\theta},
\qquad 0<\theta<1.
\]

For small \(a_n\),

\[
a_n^4
=
o\!\left(a_n^{1+\theta}\right).
\]

Therefore the raw Q11/Q13 density gain is asymptotically much smaller than the deficit scale that the campaign must force.

In particular, a fibre deficit satisfying

\[
a_n^4\ll \varepsilon_j\ll a_n^{1+\theta}
\]

can completely absorb the Q13 increment in the comparison with \(a_n\).

So Q13 gives useful scale control but does **not** close the target exponent.

## What this changes

Q11 left two apparent defects:

1. the progression length \(M\) was uncontrolled;
2. the density increment had exponent \(4\).

Q13 removes the first defect quantitatively.

The Q11 witness always yields a dyadic subprogression with

\[
2^k
\gtrsim
\beta^4N,
\]

so the scale drop is only

\[
O(\log(1/\beta)).
\]

The remaining obstruction is now purely quantitative:

> the available density gain is still only \(c\beta^4\).

Thus the low-order arm is no longer blocked by arbitrary-scale conversion.

## First defect

The low-order residual reduces to:

> **E3-B-EXPONENT4-DENSITY-INCREMENT-AMPLIFICATION.**
>
> Starting from the Q13 variable-scale relation
> \[
> k\ge n-O(\log(1/\beta)),
> \qquad
> a_k>\alpha_j+c\beta^4,
> \]
> use near-extremality, repeated carry locations, or an additional structural argument to upgrade the gain from exponent \(4\) to a deficit scale
> \[
> \beta^{1+\theta},
> \qquad\theta<1,
> \]
> or prove that this low-order lane cannot supply such an upgrade.

A better scale-selection argument alone is no longer sufficient; Q13 already controls the scale to logarithmic loss.

## Frontier effect

- \`E3-Q4-DENSITY-LOSS\`: **OPEN**.
- \`E3-B-SHORT-STEP-DENSITY-INCREMENT-AMPLIFICATION\`: **REDUCED**.
- New lemma \`E3-B-DYADIC-SHORT-STEP-DENSITY-INCREMENT\`: **PROVED_NATIVE**.
- New smallest low-order residual: \`E3-B-EXPONENT4-DENSITY-INCREMENT-AMPLIFICATION\`.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-Q11 low-order short-step density increment.
- E3-A03 / campaign notation \(a_n=r_4(2^n)/2^n\).
