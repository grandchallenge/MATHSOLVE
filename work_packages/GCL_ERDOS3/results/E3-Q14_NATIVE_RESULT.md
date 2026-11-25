# E3-Q14 — recursion-only exponent threshold and the beta^4 no-go

Disposition: **PROVED_NATIVE_RECURSION_EXPONENT_NO_GO**.

This is native GCL work. It sharpens the low-order residual after E3-Q13 by proving that repeated density increments of order (eta^4), even at a fixed one-step dyadic lag, are logically insufficient to imply convergence of the extremal-density series.

No external theorem is used.

## Strongest exact statement

Let (p>1), and put

[
s:=rac1{p-1},
qquad
b_n:=(n+1)^{-s}.
]

Then for every (nge1),

[
oxed{
b_{n-1}-b_n
ge
rac1{p-1},b_n^p.
}
]

Moreover,

[
sum_{nge1} b_n
]

converges if and only if

[
p<2.
]

Therefore:

> A monotone positive sequence may satisfy a fixed-step density-loss law of order (b_n^p) at every scale and still have divergent sum whenever (pge2).

In particular, with (p=4),

[
b_n=(n+1)^{-1/3}
]

satisfies

[
oxed{
b_{n-1}-b_ngerac13 b_n^4
}
]

for every (nge1), while

[
oxed{
sum_n b_n=infty.
}
]

Thus the order-(eta^4) increment supplied by Q11/Q13 cannot, by recursion alone, prove the campaign target

[
sum_n a_n<infty.
]

This remains true even if one strengthens Q13's variable lag

[
n-m=O(log(1/eta))
]

to the strictly stronger fixed lag (n-m=1).

## Proof

### 1. Exact backward increment

For

[
f(x):=x^{-s},
]

one has

[
-f'(x)=s x^{-s-1}.
]

Hence

[
b_{n-1}-b_n
=
n^{-s}-(n+1)^{-s}
=
int_n^{n+1}s x^{-s-1},dx.
]

Since (xle n+1) on the interval of integration,

[
x^{-s-1}ge(n+1)^{-s-1}.
]

Therefore

[
b_{n-1}-b_n
ge
s(n+1)^{-s-1}.
]

But

[
s+1
=
rac1{p-1}+1
=
rac{p}{p-1}
=
sp,
]

so

[
(n+1)^{-s-1}
=
(n+1)^{-sp}
=
b_n^p.
]

Thus

[
b_{n-1}-b_n
ge
s b_n^p
=
rac1{p-1}b_n^p.
]

### 2. Exact summability threshold

The sequence is the (s)-power law

[
b_n=(n+1)^{-s}.
]

Its series converges exactly when

[
s>1.
]

Since

[
s=rac1{p-1},
]

this is equivalent to

[
rac1{p-1}>1,
]

hence

[
p<2.
]

At (p=2), (b_n=(n+1)^{-1}) is harmonic and diverges.

For every (p>2), (s<1), so the series also diverges.

### 3. Specialization to Q13

Q13 provides an additive backward density increment of scale

[
ceta^4
]

after a dyadic lag

[
O(log(1/eta)).
]

The abstract model above with (p=4) satisfies the stronger law

[
b_{n-1}-b_n
ge
rac13 b_n^4
]

at the fixed lag (1).

Yet

[
sum_n b_n
=
sum_n (n+1)^{-1/3}
=
infty.
]

Therefore no argument that uses only:

1. monotonicity;
2. repeated backward increments of order (a^4); and
3. controlled scale lag,

can by itself imply the summability required by E3-Q4-SERIES.

Additional arithmetic structure must improve the effective exponent below (2), or supply a qualitatively stronger mechanism.

## Why this matches the promoted density-loss exponent

The protected frontier target is

[
a_{n+L}
le
a_n(1-ca_n^	heta),
qquad
0<	heta<1.
]

Equivalently,

[
a_n-a_{n+L}
gtrsim
a_n^{1+	heta}.
]

Its effective exponent is

[
p=1+	heta<2.
]

Q14 shows that (p<2) is not an arbitrary aesthetic choice: it is exactly the power-law threshold at which a pure discrete differential inequality becomes summability-forcing.

Q11/Q13 currently have

[
p=4,
]

far on the nonsummable side of that threshold.

## Claim boundary

Q14 is a proof-strategy obstruction.

It does **not** prove that the actual extremal density sequence (a_n) behaves like ((n+1)^{-1/3}).

It does **not** refute Q11 or Q13.

It proves only that the information those lemmas currently supply—an order-(eta^4) density increment with controlled dyadic scale—is insufficient on its own to prove convergence of (sum a_n).

The actual arithmetic problem may contain additional structure absent from the model sequence.

## First defect

The low-order arm can no longer be closed by recursion-only amplification at exponent (4).

The surviving target is:

> **E3-B-LOW-ORDER-EXPONENT-UPGRADE.**
>
> Starting from the Q11/Q13 low-order carry-kernel density increment, exploit additional four-fibre near-extremality, carry compatibility, or interaction with the Q12 high-order branch to improve the effective loss exponent from (4) to some
> [
> p<2,
> ]
> equivalently
> [
> p=1+	heta,qquad0<	heta<1.
> ]

A merely more efficient iteration of the same (eta^4) increment is insufficient.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- `E3-B-DYADIC-SHORT-STEP-LOCALIZATION`: remains **PROVED_NATIVE**.
- `E3-B-DYADIC-DENSITY-INCREMENT-RECURSION`: **REDUCED / STRATEGY-NO-GO**.
- New lemma `E3-B-RECURSION-SUMMABILITY-THRESHOLD`: **PROVED_NATIVE**.
- New smallest low-order residual: `E3-B-LOW-ORDER-EXPONENT-UPGRADE`.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-Q11 native short-step density increment.
- E3-Q13 native dyadic localization.
