# Formal problem statement and notation

## 1. Global data

Let `E/Q` be an elliptic curve such that the two-dimensional `F_2[G_Q]`-module `E[2]` is irreducible. Let `K/Q` be a quadratic extension, let `G = Gal(K/Q) = {1,tau}`, let `chi : G_Q -> {+1,-1}` be its character, and let `E^d/Q` be the associated quadratic twist.

For `n >= 1`, put

`A_n = E[2^n]`,

and identify `E^d[2^n]` with the quadratic twist `A_n tensor chi`. After restriction to `G_K`, fix the standard `K`-isomorphism between `E^d` and `E`.

## 2. Finite Selmer groups

For a number field `F`, define the classical finite Selmer group

`Sel_{2^n}(E/F) = ker(H^1(F,A_n) -> product_v H^1(F_v,A_n)/L_{v,n}(E/F))`,

where

`L_{v,n}(E/F) = image(E(F_v)/2^n E(F_v) -> H^1(F_v,A_n))`

is the Kummer local condition.

Write

`M_n = Sel_{2^n}(E/K)`.

The `G`-action on `M_n` defines

`M_n^+ = ker(tau-1)` and `M_n^- = ker(tau+1)`.

For `n=1`, plus and minus coincide because `-1=+1` on exponent-2 groups; no direct-sum claim is made.

## 3. Relaxed local descent conditions

For a place `v` of `Q`, let the product run over all `w|v` in `K`. Define

`F_{v,n}^+(E,K) = {c in H^1(Q_v,A_n) : res_w(c) in L_{w,n}(E/K) for every w|v}`.

For the twist, define

`F_{v,n}^-(E^d,K) = {c in H^1(Q_v,E^d[2^n]) : iota_* res_w(c) in L_{w,n}(E/K) for every w|v}`,

where `iota` is the fixed `K`-isomorphism `E^d_K -> E_K`.

The ordinary Kummer local conditions over `Q_v` are contained in these relaxed conditions.

Define the local descent defects

`Delta_{v,n}^+ = F_{v,n}^+(E,K) / L_{v,n}(E/Q)`

and

`Delta_{v,n}^- = F_{v,n}^-(E^d,K) / L_{v,n}(E^d/Q)`.

## 4. Global descent defects

Restriction gives injections of the base Selmer groups into the relevant eigenspaces. Define

`D_n^+ = M_n^+ / res Sel_{2^n}(E/Q)`

and

`D_n^- = M_n^- / res_d Sel_{2^n}(E^d/Q)`.

The theorem below embeds these groups into the direct sums of the local defects.

## 5. Integral splitting defects

Define

`I_n = M_n^+ intersect M_n^-`

and

`Q_n = M_n / (M_n^+ + M_n^-)`.

These are the exact substitutes for an unavailable integral plus/minus projector.

## 6. Ordinary local condition at 2

Assume now that `E/Q_2` has good ordinary reduction. Let `Ecal/Z_2` be its good integral model. Its 2-divisible group has the connected-etale exact sequence

`0 -> Ecal[2^infinity]^0 -> Ecal[2^infinity] -> Ecal[2^infinity]^et -> 0`,

with connected and etale parts of height one.

On geometric generic fibres write `A^ord,+` for the connected part and `A^ord,-` for the etale quotient. The ordinary Greenberg local condition is defined by

`H^1_ord(Q_2,E[2^infinity]) = ker(H^1(Q_2,E[2^infinity]) -> H^1(I_2,A^ord,-))`.

This definition is tied to the actual ordinary 2-divisible group. It is not obtained by substituting `p=2` into an odd-prime slogan.