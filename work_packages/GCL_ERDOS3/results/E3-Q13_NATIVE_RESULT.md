# E3-Q13 — dyadic localization of the short-step density increment

Disposition: **PROVED_NATIVE_DYADIC_SHORT_STEP_LOCALIZATION**.

This is native GCL work. It sharpens E3-Q11 by removing the arbitrary-length defect in the low-order carry-kernel arm. No external theorem is used.

## Strongest exact statement

Assume the hypotheses and conclusion of E3-Q11.

Let
[
N=2^n,
qquad
delta_eta:=rac{eta^4}{15cdot16^4},
]
and let
[
B_jsubseteq[0,N-1]
]
be the physical fibre supplied by Q11, with density
[
alpha_j:=rac{|B_j|}{N}.
]

Q11 supplies an arithmetic-progression segment
[
J={u_0,u_0+q,ldots,u_0+(M-1)q},
qquad
qin{1,2,3},
]
such that
[
Delta
:=
|B_jcap J|-alpha_j M
>
10delta_eta N.
]

Assume
[
10delta_eta Nge 8.
]

Then there exists a **dyadic** arithmetic-progression subsegment
[
J'
=
{v_0,v_0+q,ldots,v_0+(2^m-1)q}
subseteq J
]
with the same step (q), such that

[
oxed{
rac{|B_jcap J'|}{2^m}
>
alpha_j+5delta_eta.
}
]

Consequently, after affine rescaling,

[
oxed{
a_m
=
rac{r_4(2^m)}{2^m}
>
alpha_j+5delta_eta.
}
]

Moreover the dyadic scale is quantitatively controlled:

[
oxed{
2^m>rac54,delta_eta N,
}
]
and therefore

[
oxed{
0le n-m
<
log_2!left(rac{4}{5delta_eta}ight)
=
4log_2!rac1eta
+
log_2(12cdot16^4).
}
]

Thus Q11's low-order witness yields a genuine dyadic backward density increment after only

[
O(log(1/eta))
]

dyadic levels.

This removes the arbitrary-(M) scale-conversion defect in Q11.

It does **not** improve the increment exponent: the guaranteed additive gain remains order (eta^4).

## Proof

### 1. Q11 already forces the original segment to be macroscopic at the discrepancy scale

Since
[
1_{B_j}(u)-alpha_jle 1
]
pointwise, positive discrepancy on a set of (M) points is at most (M). Hence

[
MgeDelta>10delta_eta N.
]

So the Q11 progression is already longer than the total discrepancy scale.

### 2. Choose a dyadic block length comparable to the total discrepancy

Let (K=2^m) be the largest power of two satisfying

[
Klerac{Delta}{4}.
]

Because (Delta>10delta_eta Nge8), one has (Delta/4>2), so such a positive dyadic (K) exists.

By maximality,

[
rac{Delta}{8}<Klerac{Delta}{4}.
]

In particular,

[
K>rac{10}{8}delta_eta N
=
rac54delta_eta N.
]

Also (K<M), because (Deltale M).

### 3. Partition the progression coordinate into full dyadic blocks

Identify (J) with the index interval
[
{0,ldots,M-1}
]
through the affine map
[
ellmapsto u_0+ell q.
]

Partition this index interval into consecutive full blocks of length (K), plus one final remainder (R) of length strictly less than (K).

For any subset (E) of the progression coordinate, define its discrepancy by

[
D(E)
:=
|B_jcap E|-alpha_j|E|.
]

Suppose, for contradiction, that every full (K)-block (Q) satisfies

[
D(Q)
le
rac{Delta}{2M}K.
]

The union of all full blocks has total length at most (M), so their total discrepancy is at most

[
rac{Delta}{2M}M
=
rac{Delta}{2}.
]

The final remainder has length (<K), and pointwise discrepancy is at most (1), hence

[
D(R)le |R|<Klerac{Delta}{4}.
]

Therefore

[
D(J)
<
rac{Delta}{2}
+
rac{Delta}{4}
=
rac{3Delta}{4},
]

contradicting

[
D(J)=Delta.
]

Hence some full dyadic block (Q) satisfies

[
D(Q)
>
rac{Delta}{2M}K.
]

Let (J') be the corresponding arithmetic-progression subsegment of (J).

### 4. The dyadic block preserves a definite density increment

Dividing the last inequality by (K=2^m),

[
rac{|B_jcap J'|}{2^m}
>
alpha_j+rac{Delta}{2M}.
]

Since (Mle N),

[
rac{Delta}{2M}
ge
rac{Delta}{2N}
>
5delta_eta.
]

Thus

[
rac{|B_jcap J'|}{2^m}
>
alpha_j+5delta_eta.
]

Because (J') has common difference (qin{1,2,3}), affine rescaling maps (J') bijectively to

[
{0,ldots,2^m-1}
]

and preserves nontrivial 4-term arithmetic progressions.

Since (B_j) is 4-AP-free,

[
r_4(2^m)ge |B_jcap J'|.
]

Therefore

[
a_m
=
rac{r_4(2^m)}{2^m}
>
alpha_j+5delta_eta.
]

### 5. Quantitative dyadic scale control

From

[
2^m=K>rac54delta_eta 2^n
]

we obtain

[
2^{n-m}
<
rac{4}{5delta_eta}.
]

Hence

[
n-m
<
log_2!left(rac{4}{5delta_eta}ight).
]

Since

[
delta_eta
=
rac{eta^4}{15cdot16^4},
]

[
rac{4}{5delta_eta}
=
rac{12cdot16^4}{eta^4},
]

so

[
n-m
<
4log_2!rac1eta
+
log_2(12cdot16^4).
]

This proves the claimed (O(log(1/eta))) scale drop.

## Eventual applicability in the campaign regime

The auxiliary condition

[
10delta_eta Nge8
]

is harmless in the asymptotic near-extremal regime relevant to GCL-ERDOS3.

Protected E3-A03 gives

[
a_n
ge
2^{-(C_*+o(1))sqrt n},
qquad
C_*approx2.666539.
]

If, as in the near-extremal four-fibre contradiction regime, one takes

[
etagerac12 a_n,
]

then

[
Neta^4
ge
2^ncdot 2^{-4(C_*+o(1))sqrt n-4}
	oinfty.
]

Therefore

[
10delta_eta N	oinfty,
]

so the dyadic-localization condition holds for all sufficiently large (n).

## What this changes

Q11 left four explicit low-order defects:

1. no control of (M/N);
2. arbitrary (M), not dyadic;
3. no exponent improvement beyond (eta^4);
4. no proved recursion preserving the hypotheses needed for another Q10 step.

Q13 resolves the first two in the form actually needed by the dyadic extremal sequence:

- one can choose a dyadic subprogression;
- its scale satisfies
  [
  2^mgtrsimeta^4N;
  ]
- equivalently
  [
  n-m=O(log(1/eta));
  ]
- and the additive density increment remains
  [
  gtrsimeta^4
  ]
  with no fixed-factor density loss.

The remaining obstruction is therefore no longer arbitrary-scale conversion.

## Claim boundary

Q13 does **not** prove:

- an increment with exponent below (2);
- that the Q10/Q11 low-order arm recurs at the new dyadic scale;
- that a near-extremal four-fibre gluing exists at the new scale;
- that one may iterate the increment without losing the hypotheses needed for Q10;
- or any bound
  [
  H_{2,n}gtrsim Na_n^{1+	heta},
  qquad 	heta<1.
  ]

The exponent remains (4).

No parent theorem, gluing-radius equivalence, or density-loss theorem is promoted.

## First defect

The low-order residual reduces to:

> **E3-B-DYADIC-DENSITY-INCREMENT-RECURSION.**
>
> Starting from Q13's dyadic scale (m) with
> [
> n-m=O(log(1/eta))
> ]
> and
> [
> a_m>alpha_j+ceta^4,
> ]
> prove that the near-extremal/gluing hypotheses recur strongly enough across a controlled sequence of dyadic scales to amplify these order-(eta^4) increments into a gluing deficit
> [
> gtrsimeta^{1+	heta}N
> ]
> for some (	heta<1), or prove that this recursion route cannot reach the required exponent.

This is strictly narrower than Q11's residual because the arbitrary-(M) and dyadic-conversion defects are discharged.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- `E3-B-LOW-ORDER-SHORT-STEP-DENSITY-INCREMENT`: remains **PROVED_NATIVE**.
- New lemma `E3-B-DYADIC-SHORT-STEP-LOCALIZATION`: **PROVED_NATIVE**.
- `E3-B-SHORT-STEP-DENSITY-INCREMENT-AMPLIFICATION`: **REDUCED**.
- New smallest low-order residual: `E3-B-DYADIC-DENSITY-INCREMENT-RECURSION`.
- No parent-frontier promotion occurs.

## Protected basis

- E3-Q11 native short-step density increment.
- E3-A03 protected pointwise lower construction, used only for eventual applicability of the auxiliary size condition.
