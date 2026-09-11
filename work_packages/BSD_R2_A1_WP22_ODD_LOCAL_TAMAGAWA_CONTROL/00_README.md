# BSD-R2-A1 WP22 — odd-prime cyclotomic local control equals Tamagawa depth

## Purpose

Protected WP21 proves that the entire base-to-cyclotomic primitive Kummer specialization defect is local. For each place `v`, its ambient local kernel is

`K_v = H^1(Gamma_v,E(Q_{infty,w}))[2^infinity]`.

WP22 computes this kernel at every odd prime in the protected semistable odd-conductor class.

## Main result

For every odd prime `ell`:

- if `E` has good reduction at `ell`, then `K_ell=0`;
- if `E` has multiplicative reduction of type `I_n`, then
  - split multiplicative: `K_ell` is the `2`-primary subgroup of `Z/nZ`;
  - nonsplit multiplicative: `K_ell` is the `2`-primary part of `(Z/nZ)/2(Z/nZ)`.

Using protected WP13,

`#K_ell = 2^{ord_2(c_ell)}`

for every bad odd prime `ell|N`.

Therefore, for

`K_bad := product_{ell|N} K_ell`,

one has

`len_{Z_2}(K_bad^vee) = sum_{ell|N} ord_2(c_ell)`

and

`Fitt^0_{Z_2}(K_bad^vee)
 = 2^{sum_{ell|N} ord_2(c_ell)} Z_2`.

Thus the exact Tamagawa subtraction already present in `delta_2(E)` is the exact total **ambient bad-prime local-control length** in the cyclotomic primitive-Kummer comparison.

## Proof method

No new arithmetic source premise is imported.

At an odd prime, the local cyclotomic tower is unramified. At each finite `2`-power layer:

1. the formal subgroup has trivial higher cyclic cohomology because multiplication by the `2`-power group order is invertible on the pro-`ell` formal group;
2. the connected special-fibre group has trivial cyclic `H^1` and norm quotient, proved directly from the Frobenius-minus-one and norm isogenies;
3. hence the cyclic `H^1` of local points is exactly the cyclic `H^1` of the Neron component group;
4. the component action is `+1` for split multiplicative reduction and `-1` for nonsplit multiplicative reduction;
5. passing through the unramified `Z_2` tower gives the stated groups.

## Critical boundary

WP22 computes the **ambient** bad-prime kernels. Protected WP21 defines the actual global control module as

`C_E = im(loc_Q) intersect K_loc`.

WP22 does not prove that the projection of `C_E` onto `K_bad` is all of `K_bad`, or that `C_E` splits as a product of its local projections.

The place `2` is also not evaluated here.

## Remaining D1b

After WP22, the local-control problem is reduced to:

1. the exact good-ordinary kernel
   `K_2 = H^1(Gamma_2,E(Q_{infty,2}))[2^infinity]`;
2. the Poitou-Tate/global-local incidence problem determining which elements of
   `K_2 x K_bad`
   lie in `im(loc_Q)`.

The corresponding boundaries are:

- `MISSING_P2_GOOD_ORDINARY_LOCAL_CONTROL_KERNEL_AT_2`;
- `MISSING_P2_GLOBAL_HIT_SUBGROUP_OF_LOCAL_CONTROL_KERNELS`.

D1a, D1c, and D2 from WP21 remain separately open.

`BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED`; no MATHCERT certification is asserted.