# E3-S02 — exact quantitative frontier after the equivalence

Disposition: **SOURCE_INTERFACE_FOUND**.

## Exact equivalence source

Green–Tao 2017 explicitly state that Erdős's reciprocal-sum conjecture is
equivalent to

[
sum_{n=1}^{infty}rac{r_k(2^n)}{2^n}<infty
]

for every (kge3), citing Tao–Vu, *Additive Combinatorics*, Exercise 10.0.6.

## Minimal unresolved case

For (k=4), Green–Tao prove

[
r_4(N)ll N(log N)^{-c}
]

for some absolute constant (c>0).

At dyadic scale this yields

[
a_n=rac{r_4(2^n)}{2^n}ll n^{-c}.
]

The stated theorem does not supply (c>1), so the pointwise estimate alone does
not establish (sum_n a_n<infty).

Green's 2026 JLMS survey identifies the reciprocal-sum problem as still far
beyond the current length-four quantitative theory.

## Research consequence

After E3-B02 there is no need to search for a logically different bridge from
reciprocal divergence to arithmetic progressions: any proof of the fixed-(k)
conjecture is equivalent to convergence of this extremal series.

Different proof mechanisms remain possible, but their mathematical output must
ultimately imply the series convergence.

The campaign should therefore target sequence-level information stronger than
the currently stated pointwise estimate: improved decay, averaged decay, or a
cross-scale recurrence for (a_n).
