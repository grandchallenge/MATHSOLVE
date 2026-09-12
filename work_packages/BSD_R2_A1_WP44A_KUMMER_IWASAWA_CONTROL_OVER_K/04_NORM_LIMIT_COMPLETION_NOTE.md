# WP44A proof note — completed norm limits and base projection

This note makes explicit the completion step in `BSD-A1-WP44A-NORM-LIMIT-IMAGE-001`.

Fix a relevant local tower

`F_n/F_0`

and put

`A_n:=E(F_n)^hat_2`.

Let

`M:=inverse_limit_n A_n`

under the completed norm maps and let

`p_0:M->A_0`

be base projection.

Protected WP25 proves that the raw base norm images

`N_n:=N_{F_n/F_0}E(F_n)`

stabilize: there is `n_0` such that

`N_n=N^infty`

for all `n>=n_0`, where

`N^infty=intersection_n N_n`.

## Lemma

`im(p_0)=closure(N^infty)` inside `A_0`.

### Proof

For every `n`, the image in `A_0` of the completed norm map

`A_n -> A_0`

is the closure of the raw norm image `N_n`. Indeed, the completed norm map is continuous, `A_n` is compact, and its image is therefore compact and closed; the raw points are dense in `A_n`, so their norm image is dense in the completed image.

For `n>=n_0`, this image is therefore exactly

`closure(N^infty)`.

If `(x_n)_n in M`, then

`x_0=N_{F_n/F_0}(x_n)`

for every `n`. Hence

`x_0 in closure(N^infty)`.

This proves

`im(p_0) subset closure(N^infty)`.

Conversely fix

`x_0 in closure(N^infty)`.

For every integer `m>=n_0`, the element `x_0` lies in the image of the completed norm map

`A_m -> A_0`.

Choose a preimage `y_m in A_m`; norming `y_m` to the intermediate layers produces a compatible finite prefix

`(x_0,x_1,...,x_m)`.

Consider the compact product

`product_n A_n`.

The condition that the zeroth coordinate is the fixed element `x_0` and each relation

`N_{n+1/n}(x_{n+1})=x_n`

holds is closed. Every finite family of these closed conditions is satisfiable by the finite-prefix construction from a sufficiently high layer. By compactness and the finite-intersection property, all conditions are simultaneously satisfiable. Thus there is a full compatible sequence in `M` projecting to `x_0`.

Therefore

`closure(N^infty) subset im(p_0)`.

The two inclusions prove the lemma. QED.

## Cokernel

Protected WP25 proves

`U:=E(F_0)/N^infty`

is a finite `2`-primary group. Therefore passage from `E(F_0)` to its pro-`2` completion identifies

`A_0/closure(N^infty) ~= U`.

Combined with the lemma,

`coker(p_0) ~= U`.

This is exactly the local augmentation-cokernel statement used in WP44A. No commutation of arbitrary inverse limits with completion is assumed.