# E3-Q11 — low-order carry kernels force a short-step density increment

Disposition: **PROVED_NATIVE_LOW_ORDER_DENSITY_INCREMENT**.

This is native GCL work. It sharpens the low-order arm of E3-Q10 for the adjacent `0011` families. No external theorem is used.

## Strongest exact statement

Assume the hypotheses of E3-Q10. Write

[
delta_eta:=rac{eta^4}{15cdot16^4}.
]

Suppose one adjacent `0011` family lands in Q10 alternative A or B, i.e. it has either

1. a singleton carry-kernel correlation
   [
   left|mathbb E_y h_t(y)kappa_{F,t}(y)ight|>delta_eta,
   ]
   or

2. a pair carry-kernel correlation
   [
   left|mathbb E_{y,z}h_a(y)h_b(z)kappa_{F,a,b}(y,z)ight|>delta_eta.
   ]

Then there exists one of the two physical fibres (B_j) used by that adjacent family and an arithmetic-progression segment

[
J={u_0,u_0+q,ldots,u_0+(M-1)q}
subseteq[0,N-1],
]

with

[
qin{1,2,3},
qquad
Mge1,
]

such that, writing

[
alpha_j:=rac{|B_j|}{N},
]

one has the **positive local density discrepancy**

[
oxed{
|B_jcap J|-alpha_j M
>
10,delta_eta N.
}
]

Consequently

[
oxed{
rac{|B_jcap J|}{M}
>
alpha_j+10delta_eta
}
]

and, because affine rescaling of an arithmetic-progression segment preserves 4-AP-freeness,

[
oxed{
rac{r_4(M)}{M}
>
alpha_j+10delta_eta.
}
]

Thus every Q10 low-order witness yields an actual density increment on a subprogression of common difference at most (3). The increment is of order (eta^4).

This does not yet have the exponent required for the parent density-loss theorem.

## Proof

### 1. Singleton carry kernel

Take Q10 alternative A at labelled position (t).

Let

[
m_t(y)
:=
#left{
din G:
prod_{s
e t}
1_{I_s}igl(y+(s-t)digr)=1
ight}.
]

Since

[
kappa_{F,t}(y)=rac{m_t(y)}{P},
]

the Q10 correlation gives

[
left|
sum_{yin G}h_t(y)m_t(y)
ight|
>
delta_eta P^2.
]

The fluctuation (h_t) is supported on the translated interval (I_t), which has exactly (N) points, and

[
sum_{yin I_t}h_t(y)=0.
]

Translate (I_t) to ({0,ldots,N-1}), write the translated fluctuation as (h(u)), and write the corresponding extension count as (m(u)).

#### Variation bound

For consecutive (u,u+1), the product

[
prod_{s
e t}
1_{I_s}igl(u+(s-t)digr)
]

can change only if at least one of its three interval indicators changes.

For one fixed (s
e t), shifting (u) by one changes

[
1_{I_s}igl(u+(s-t)digr)
]

only when its argument crosses one of the two endpoints of (I_s). Since (P>3) is prime and (s-tin{pm1,pm2,pm3}), each endpoint equation has at most one solution (din G).

Hence at most two (d)'s per (s) can change, so

[
|m(u+1)-m(u)|le6.
]

Therefore

[
sum_{u=0}^{N-2}|m(u+1)-m(u)|
le6(N-1).
]

Let

[
H(k):=sum_{u=0}^{k}h(u).
]

Because (H(N-1)=0), discrete summation by parts gives

[
sum_{u=0}^{N-1}h(u)m(u)
=
-sum_{k=0}^{N-2}
H(k)igl(m(k+1)-m(k)igr).
]

Thus

[
delta_eta P^2
<
6(N-1)max_{0le k<N-1}|H(k)|.
]

Since (P>8N),

[
max_k|H(k)|
>
rac{delta_eta P^2}{6(N-1)}
>
rac{32}{3}delta_eta N.
]

If the maximizing prefix has positive discrepancy, take that prefix as (J).

If its discrepancy is negative, use the complementary suffix. Since the total discrepancy on the whole physical interval is zero, the suffix has the same discrepancy with positive sign.

Hence in the singleton case there is a contiguous interval (J) satisfying

[
|B_jcap J|-alpha_j|J|
>
rac{32}{3}delta_eta N
>
10delta_eta N.
]

This is the desired result with (q=1).

### 2. Pair carry kernel

Take Q10 alternative B at positions (a<b), and put

[
q:=b-ain{1,2,3}.
]

The correlation inequality is

[
left|
sum_{y,zin G}
h_a(y)h_b(z)kappa_{F,a,b}(y,z)
ight|
>
delta_eta P^2.
]

Only (N) values of (y) lie in the support interval of (h_a), and (|h_a(y)|le1). Therefore

[
delta_eta P^2
<
sum_{yin I_a}
left|
sum_z h_b(z)kappa_{F,a,b}(y,z)
ight|.
]

Hence for some (yin I_a),

[
left|
sum_z h_b(z)kappa_{F,a,b}(y,z)
ight|
>
rac{delta_eta P^2}{N}
>
64delta_eta N.
]

Define

[
K_y
:=
{zin I_b:kappa_{F,a,b}(y,z)=1}.
]

Then

[
left|
sum_{zin K_y}h_b(z)
ight|
>
64delta_eta N.
]

#### Exact shape of the slice

Protected Q02/S04 no-wrap guarantees that a modular labelled progression whose four points all lie in the four carry windows is an ordinary integer 4-AP.

Fixing the point at labelled position (a), every compatible point at position (b) therefore has the form

[
z=y+qd
]

for an integer common difference (d).

The conditions that (zin I_b) and that the two remaining labelled points lie in their prescribed intervals are each interval constraints on (d). Their intersection is therefore either empty or a contiguous interval of integers.

Consequently (K_y) is either empty or an arithmetic-progression segment of common difference (q).

It is nonempty here because its discrepancy is nonzero.

Translate (K_y) back into the physical fibre (B_jsubseteq[0,N-1]); call the resulting progression segment (K).

If

[
sum_{uin K}
igl(1_{B_j}(u)-alpha_jigr)
>
64delta_eta N,
]

take (J=K).

Otherwise the discrepancy on (K) is negative with magnitude (>64delta_eta N). The discrepancy over the entire physical interval is zero, so the complement ([0,N-1]setminus K) has positive discrepancy (>64delta_eta N).

Because (K) occupies one residue class modulo (q), its complement can be partitioned into at most

[
2+(q-1)=q+1le4
]

arithmetic-progression segments of common difference (q):

- at most one segment before (K) in the same residue class;
- at most one after (K);
- one full segment for each of the other (q-1) residue classes.

Therefore at least one of these at most four segments has positive discrepancy

[
>
rac{64}{4}delta_eta N
=
16delta_eta N
>
10delta_eta N.
]

This proves the pair case.

### 3. Convert the discrepancy to a genuine local density increment

In either case we now have an arithmetic-progression segment

[
Jsubseteq[0,N-1]
]

with common difference (qle3), length (M), and

[
|B_jcap J|-alpha_jM
>
10delta_eta N.
]

Since (Mle N),

[
rac{|B_jcap J|}{M}
>
alpha_j+10delta_etarac{N}{M}
ge
alpha_j+10delta_eta.
]

The affine map

[
u_0+ell qlongmapstoell
]

takes (J) bijectively to ({0,ldots,M-1}) and preserves 4-term arithmetic progressions.

Since (B_j) is 4-AP-free, its image (B_jcap J) is 4-AP-free. Hence

[
r_4(M)ge|B_jcap J|,
]

which gives

[
rac{r_4(M)}{M}
>
alpha_j+10delta_eta.
]

## Quantitative scale

Since

[
delta_eta
=
rac{eta^4}{15cdot16^4},
]

the guaranteed density increment is

[
10delta_eta
=
rac{2}{3cdot16^4}eta^4.
]

This is a genuine arithmetic density increment, but its exponent is (4).

It therefore does not by itself yield the campaign target

[
eta^{1+	heta},
qquad
0<	heta<1.
]

## What this changes

Q10 reduced the de-windowed lane to:

1. low-order carry-kernel correlation; or
2. all-four intrinsic (U^3) structure.

Q11 eliminates the abstract-kernel ambiguity in the first arm:

> **Every low-order carry-kernel witness produces a positive density increment on an actual short-step arithmetic subprogression of one physical fibre.**

So the low-order arm is now an extremal-density recursion problem, not a harmonic-analysis problem.

## Claim boundary

Q11 does not prove:

- that the subprogression length (M) is a fixed positive fraction of (N);
- that (M) can be chosen dyadic;
- that the (eta^4) increment amplifies to exponent below (2);
- that repeated density increments preserve the near-extremal hypotheses needed by Q10;
- or that the all-four (U^3) arm aligns quadratic witnesses.

No parent theorem is promoted.

## First defect

The de-windowed residual separates into two sharply different tasks.

### Low-order arm

> **E3-B-SHORT-STEP-DENSITY-INCREMENT-AMPLIFICATION.**
>
> Starting from Q11, show that repeated short-step density increments, near-extremality, or a scale-control lemma upgrades the order-(eta^4) increment to a gluing deficit of order
> [
> eta^{1+	heta}N
> ]
> for some (	heta<1), or prove this arm cannot achieve the required exponent.

### High-order arm

> **E3-B-ALLFIBRE-DEWINDOWED-ALIGNMENT.**
>
> Starting from Q10's all-four intrinsic (U^3) arm, align derivative-frequency or quadratic witnesses strongly enough to force the same deletion scale.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- `E3-B-DEWINDOWED-ORDER-DICHOTOMY`: remains **PROVED_NATIVE**.
- New lemma `E3-B-LOW-ORDER-SHORT-STEP-DENSITY-INCREMENT`: **PROVED_NATIVE**.
- `E3-B-DEWINDOWED-CARRY-KERNEL-OR-ALLFIBRE-ALIGNMENT`: **REDUCED** into the two named arms above.
- No gluing-radius or parent-frontier promotion occurs.

## Protected basis

- E3-Q02 / E3-S04 no-wrap carry embedding.
- E3-Q09 de-windowed window-baseline expansion.
- E3-Q10 de-windowed correlation-order dichotomy.
