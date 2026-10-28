# E3-Q13 — carry-section geometry bias forces an end-interval density increment

Disposition: **PROVED_NATIVE_CARRY_GEOMETRY_DENSITY_INCREMENT**.

This is native GCL work. It resolves the singleton branch of Q12 into an explicit one-dimensional density increment inside the physical fibre.

## Strongest exact statement

Use the exact Q12 setting. Fix one L01 core family (F=(i,q,c)) and one labelled position (t).

Let
[
m_{F,t}(r)
=
rac1N
#left{
(u,v)inOmega_c(N):
r_t(u,v)=r
ight},
qquad
0le r<N.
]

Then the normalized carry-section weight has discrete total variation
[
oxed{
sum_{r=0}^{N-2}
|m_{F,t}(r+1)-m_{F,t}(r)|
<2.
}
]

Consequently, if the Q12 singleton branch occurs:
[
left|
rac1Nsum_{r=0}^{N-1}
h_t(r)
igl(m_{F,t}(r)-overline m_{F,t}igr)
ight|
gedelta,
]
then there exists a prefix or suffix interval
[
Jsubseteq[0,N-1]
]
such that
[
oxed{
|B_{j_t}cap J|
-
alpha_t|J|
ge
rac{delta N}{2}.
}
]

In particular,
[
oxed{
|J|gerac{delta N}{2}
}
]
and
[
oxed{
rac{|B_{j_t}cap J|}{|J|}
ge
alpha_t+rac{delta}{2}.
}
]

Applying the Q12 value
[
delta=rac{eta^4}{3840}
]
gives:

> Every Q12 singleton carry-geometry witness yields a prefix or suffix (J) of the physical fibre with
> [
> |J|
> ge
> rac{eta^4}{7680}N
> ]
> and AP-free density at least
> [
> alpha_t+rac{eta^4}{7680}.
> ]

Thus the singleton branch is not merely Fourier/support geometry: it is an explicit local density increment for an internally 4-AP-free set.

## Proof

### 1. Fixed-residue sections are integer intervals

Fix
[
r=r_t(u,v)=u+tv-c_tN.
]

Then
[
u=r+c_tN-tv.
]

Substitute this into every defining inequality of the carry cell:
[
0le u,vle N-1,
]
and
[
c_sNle u+svle(c_s+1)N-1,
qquad s=0,1,2,3.
]

For (s
e t),
[
u+sv
=
r+c_tN+(s-t)v.
]

Therefore each cell constraint gives either a lower or upper bound on (v) of the form
[
vge a r+b
qquad	ext{or}qquad
vle a r+b,
]
with
[
|a|=rac1{|s-t|}le1.
]

The bounds (0le vle N-1) have slope (0). The (u)-bounds have slope (1/t) when (t>0), again of magnitude at most (1); for (t=0), (r=u) already lies in ([0,N-1]).

Hence for each (r), the feasible integer (v)-values form an interval
[
L(r)le vle U(r),
]
where the integer lower and upper endpoints can each change by at most (1) when (r) is replaced by (r+1):
[
|L(r+1)-L(r)|le1,
qquad
|U(r+1)-U(r)|le1.
]

The unnormalized section count is
[
A(r):=N,m_{F,t}(r)
=
max{0,U(r)-L(r)+1}.
]

Since (xmapstomax(0,x)) is 1-Lipschitz,
[
|A(r+1)-A(r)|
le
|U(r+1)-U(r)|
+
|L(r+1)-L(r)|
le2.
]

Therefore
[
|m_{F,t}(r+1)-m_{F,t}(r)|
lerac2N.
]

Summing over (N-1) adjacent pairs gives
[
sum_{r=0}^{N-2}
|m_{F,t}(r+1)-m_{F,t}(r)|
le
rac{2(N-1)}N
<2.
]

### 2. Summation by parts

Write
[
h(r):=1_{B_{j_t}}(r)-alpha_t.
]

Then
[
sum_{r=0}^{N-1}h(r)=0.
]

Let
[
w(r):=m_{F,t}(r)-overline m_{F,t},
]
so (w) has the same adjacent differences as (m_{F,t}).

Define prefix discrepancies
[
H(k):=sum_{r=0}^{k}h(r),
qquad
0le kle N-1.
]

Because the total sum is zero,
[
H(N-1)=0.
]

Discrete summation by parts gives
[
sum_{r=0}^{N-1}h(r)w(r)
=
-sum_{k=0}^{N-2}
H(k)igl(w(k+1)-w(k)igr).
]

Therefore
[
left|
rac1Nsum_rh(r)w(r)
ight|
le
rac1N
max_{0le kle N-2}|H(k)|
sum_{k=0}^{N-2}|w(k+1)-w(k)|
<
rac{2}{N}max_k|H(k)|.
]

If the left side is at least (delta), then
[
max_k|H(k)|
>
rac{delta N}{2}.
]

### 3. Convert signed prefix discrepancy to a positive interval density increment

Choose (k) with
[
|H(k)|>rac{delta N}{2}.
]

If
[
H(k)>0,
]
take the prefix
[
J=[0,k].
]
Then
[
|B_{j_t}cap J|-alpha_t|J|
=
H(k)
>
rac{delta N}{2}.
]

If
[
H(k)<0,
]
take the suffix
[
J=[k+1,N-1].
]
Since the total fluctuation is zero,
[
sum_{r=k+1}^{N-1}h(r)
=
-H(k)
>
rac{delta N}{2}.
]

Thus in either case
[
|B_{j_t}cap J|-alpha_t|J|
>
rac{delta N}{2}.
]

The left side is at most (|J|), so
[
|J|>rac{delta N}{2}.
]

Also (|J|le N), hence
[
rac{|B_{j_t}cap J|}{|J|}
=
alpha_t+
rac{|B_{j_t}cap J|-alpha_t|J|}{|J|}
>
alpha_t+rac{delta N}{2|J|}
ge
alpha_t+rac{delta}{2}.
]

This proves the theorem.

## Arithmetic interpretation

Because (B_{j_t}) is internally 4-AP-free, every subinterval intersection
[
B_{j_t}cap J
]
is also 4-AP-free.

Therefore the singleton carry-geometry branch gives a genuine extremal-density increment at a smaller interval scale:
[
r_4(|J|)
ge
|B_{j_t}cap J|
ge
left(
alpha_t+rac{eta^4}{7680}
ight)|J|,
]
with
[
|J|
ge
rac{eta^4}{7680}N.
]

No asymptotic conclusion is drawn from this inequality yet; the interval length need not be dyadic and the increment exponent (4) is not by itself sufficient for the campaign target.

## Why this matters

Q12 leaves two branches.

Q13 converts the singleton branch into a conventional density-increment object.

Thus the carry-localized programme now has an exact dichotomy:

1. **density-increment branch:** some physical fibre contains a prefix/suffix interval of relative length at least (eta^4/7680) with density increment at least (eta^4/7680);
2. **multi-correlation branch:** some exact D01 carry cell carries a multi-fluctuation correlation of magnitude at least (eta^4/3840).

This is a materially more concrete frontier than a generic “quadratic structure versus deletion” statement.

## Claim boundary

Q13 does not prove that the density increment contradicts near-extremality.

In particular:
- the increment occurs at a smaller, possibly non-dyadic interval length;
- extremal 4-AP-free density is allowed to be larger at smaller scales;
- the exponent (4) is still too weak to imply the desired (eta^{1+	heta}) deletion scale directly.

The theorem only converts the singleton geometry branch into an exact density-increment alternative.

## First defect

The carry-localized residual reduces to:

> **E3-B-DENSITY-INCREMENT-OR-LOCALIZED-MULTICORRELATION.**  
> Starting from Q12/Q13, prove that repeated carry-localized density increments or localized multi-fluctuation correlations cannot persist across the L01 core and dyadic scale recursion without producing
> [
> gtrsimeta^{1+	heta}N
> ]
> deletion cost for some (0<	heta<1).

The two immediate lanes are:
- iterate/transfer the Q13 non-dyadic density increment into a quantitative extremal recurrence;
- develop a carry-localized Fourier/derivative decomposition for the Q12 multi-correlation branch.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- New lemma `E3-B-CARRY-GEOMETRY-DENSITY-INCREMENT`: **PROVED_NATIVE**.
- `E3-B-CARRY-LOCALIZED-GEOMETRY-OR-MULTICORRELATION`: **REDUCED**.
- New smallest carry-localized residual: `E3-B-DENSITY-INCREMENT-OR-LOCALIZED-MULTICORRELATION`.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-Q12 exact carry-localized cancellation dichotomy.
- E3-D01 exact integer carry-cell compiler.
