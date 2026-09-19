# YM-D001-R005-L001 — exact physical scale law for regulated spectral gaps

## Statement

Let `K_n` be a nonnegative self-adjoint operator on a Hilbert space `K_n^{space}`.

Interpret `K_n` as a **dimensionless** generator: one unit of its evolution parameter corresponds to a positive physical Euclidean time

`tau_n > 0`.

Define the physically normalized generator

`H_n := tau_n^{-1} K_n`.

Let `delta_n >= 0` satisfy

`sigma(K_n) subset {0} union [delta_n,infinity)`.

Then

`sigma(H_n) subset {0} union [delta_n/tau_n,infinity)`.

If `delta_n` is the supremal dimensionless spectral exclusion, then `delta_n/tau_n` is the supremal physical spectral exclusion.

Consequently:

### Uniform-gap criterion

There exists `Delta>0` and `N` such that, for all `n>=N`,

`sigma(H_n) subset {0} union [Delta,infinity)`

if and only if

`liminf_{n->infinity} delta_n/tau_n > 0`

when `delta_n` denotes the exact regulated gap.

For merely proved lower bounds `underline_delta_n <= delta_n`, the condition

`liminf underline_delta_n/tau_n > 0`

is sufficient.

## Proof

For every real scalar `c>0` and self-adjoint operator `A`,

`sigma(cA) = c sigma(A)`.

This follows directly from the resolvent identity

`cA-zI = c(A-(z/c)I)`:

`cA-zI` is boundedly invertible exactly when `A-(z/c)I` is boundedly invertible.

Apply this with

`c=tau_n^{-1}`

and `A=K_n`.

Then

`sigma(H_n)=tau_n^{-1}sigma(K_n)`.

Therefore

`sigma(K_n) subset {0} union [delta_n,infinity)`

implies

`sigma(H_n) subset {0} union [delta_n/tau_n,infinity)`.

If `delta_n` is the exact supremal exclusion, scalar multiplication preserves the order of the nonzero spectrum, so the exact physical exclusion is `delta_n/tau_n`.

For the uniform criterion, suppose first that

`L:=liminf delta_n/tau_n>0`.

Choose any `Delta` with `0<Delta<L`. By the definition of liminf, `delta_n/tau_n >= Delta` for all sufficiently large `n`, which gives the required common physical exclusion.

Conversely, if one common `Delta>0` is valid eventually, exactness of `delta_n` gives

`delta_n/tau_n >= Delta`

eventually, so

`liminf delta_n/tau_n >= Delta >0`.

QED.

## Transfer-operator corollary

Assume in addition that

`T_n = exp(-K_n)`

is the regulated positive transfer operator.

Suppose `1` is the vacuum spectral point and the non-vacuum transfer spectrum satisfies

`sigma(T_n) \ {1} subset [0,r_n]`

for some `0<r_n<1`.

Because `x -> exp(-x)` is decreasing on `[0,infinity)`,

`sigma(K_n) \ {0} subset [-log(r_n),infinity)`.

Hence

`sigma(H_n) subset {0} union [-log(r_n)/tau_n,infinity)`.

If `r_n` is the exact upper edge of the non-vacuum transfer spectrum, then the exact physical generator gap is

`-log(r_n)/tau_n`.

## FP1 — positivity at every cutoff can still vanish physically

Let

`tau_n = 1/n`

and let the exact dimensionless gap be

`delta_n = 1/n^2`.

Then `delta_n>0` for every `n`, but

`delta_n/tau_n = 1/n -> 0`.

Thus pointwise positivity of regulated dimensionless gaps does not imply any positive cutoff-uniform physical gap.

## FP2 — dimensionless operator data do not determine a physical gap

Fix any sequence of dimensionless generators with exact gaps

`delta_n=1/n`.

Three scale choices give three incompatible physical conclusions:

- `tau_n=1/n`: physical gap `=1`;
- `tau_n=1/sqrt(n)`: physical gap `=1/sqrt(n) ->0`;
- `tau_n=1/n^2`: physical gap `=n -> infinity`.

The same dimensionless spectral data therefore do not determine a physical continuum scale. The clock calibration is additional mathematical data.

## FP3 — transfer eigenvalue separation is not generator energy

For `T_n=exp(-K_n)`, a non-vacuum transfer edge `r_n` corresponds exactly to generator energy

`-log(r_n)`.

The quantity

`1-r_n`

has the same first-order small-gap asymptotics but is not equal to `-log(r_n)` except at the trivial point `r_n=1`.

Thus replacing the logarithm by `1-r_n` requires an explicit approximation/error theorem and may not be used as an exact spectral conversion.

## Yang-Mills interpretation

The protected WP00 warning

`inf_a delta(a)/a > 0`

is recovered from this lemma only in a convention where the physical Euclidean time represented by one transfer step is exactly

`tau(a)=a`.

That identification is itself part of scale setting.

The protected Yang-Mills estate currently contains:

- fixed-regulator transfer matrices;
- source coupling conventions;
- perturbative UV beta-function information;
- partial Euclidean RG recursion;
- an abstract continuum OS reconstruction interface.

It does not currently contain a protected theorem assigning the same nonperturbative physical `tau(a)` to the actual regulated family across the continuum trajectory.

R005 therefore proves the scale law but does not manufacture the missing Yang-Mills calibration.
