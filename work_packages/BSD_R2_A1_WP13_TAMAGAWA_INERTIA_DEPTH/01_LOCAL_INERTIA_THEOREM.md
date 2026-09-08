# Theorem — local 2-power inertia depth at semistable bad primes

Let `ell|N`. Since the protected conductor is odd, `ell` is odd. Semistability gives multiplicative reduction of Kodaira type `I_n`, where

`n = ord_ell(Delta_min) > 0`.

We prove the local assertions for every `m>=1`.

## 1. Split multiplicative reduction

Over `Q_ell`, write `E ~= E_q` as a Tate curve. Then

`v_ell(q)=n`

and there is an exact sequence of Galois modules

`0 -> mu_{2^m} -> E_q[2^m] -> Z/2^m Z -> 0`.

Choose compatible generators represented by a primitive `2^m`-th root of unity and a `2^m`-th root `q^(1/2^m)`. Because `ell != 2`, inertia acts trivially on `mu_{2^m}`.

Write

`q = ell^n u`, `u in Z_ell^x`.

The pro-`ell` group `1+ell Z_ell` is uniquely `2^m`-divisible, and the prime-to-ell root-of-unity part of `u` becomes divisible after an unramified extension. Thus the ramified Kummer class of `q` is the same as that of `ell^n`.

On inertia, in the chosen Tate basis, the representation has the form

`rho_{2^m}(sigma) = [[1, n*t_m(sigma)], [0,1]]`,

where the tame Kummer character

`t_m : I_ell -> Z/2^m Z`

is surjective.

Therefore

`rho_{2^m}(I_ell)=1 <=> n == 0 (mod 2^m)`.

Equivalently,

`I_ell acts trivially on E[2^m] <=> 2^m | n`.

## 2. Nonsplit multiplicative reduction

A nonsplit multiplicative elliptic curve becomes a split Tate curve after an unramified quadratic extension. Passing to an unramified extension does not change inertia. The quadratic twisting character is unramified, hence is trivial on inertia.

Thus the same inertia formula and equivalence hold:

`I_ell acts trivially on E[2^m] <=> 2^m | n`.

## 3. Residual conductor

At `m=1`, `E[2]` is unramified at `ell` exactly when `n` is even.

If `n` is odd, the tame inertia image on `E[2]` is the nontrivial unipotent subgroup of `GL_2(F_2)`. Its invariant subspace has dimension one, so the residual Artin-conductor exponent at `ell` is one.

If `n` is even, the residual conductor exponent is zero.

Since the original semistable conductor is squarefree and all bad primes are odd,

`N(rho_bar_{E,2}) = product_{ell|N, n_ell odd} ell`.

## 4. Tamagawa factors

For multiplicative type `I_n`:

- split multiplicative: `c_ell=n`;
- nonsplit multiplicative: `c_ell=gcd(2,n)`, i.e. `c_ell=1` for odd `n` and `c_ell=2` for even `n`.

Hence in either reduction type,

`c_ell is odd <=> n is odd <=> E[2] is ramified at ell`.

Therefore

`N(rho_bar_{E,2}) = product_{ell|N, c_ell odd} ell`

and

`N / N(rho_bar_{E,2}) = product_{ell|N, 2|c_ell} ell`.

The exact valuations are:

### split multiplicative

`ord_2(c_ell)=v_2(n_ell)
 = max {m>=0 : I_ell acts trivially on E[2^m]}`,

where `m=0` is allowed for odd `n_ell`.

### nonsplit multiplicative

`ord_2(c_ell)=min(1,v_2(n_ell))`.

Thus the full inertia depth can exceed the Tamagawa valuation in the nonsplit case; the component-group Frobenius action truncates the rational Tamagawa contribution to one factor of `2`.

## 5. Chao Li residual-conductor condition

WP12 proves residual surjectivity automatically in the selected class. The admitted route audit records that Chao Li's source additionally imposes equality of the residual Serre conductor with `N`.

The theorem above makes that condition exact:

`N(rho_bar_{E,2})=N <=> c_ell is odd for every ell|N`.

Hence residual surjectivity does not remove the Tamagawa-odd restriction. Curves carrying any target-relevant even Tamagawa factor lie outside that residual-conductor hypothesis.

## Firewall

No statement here upgrades an odd-prime Euler-system or Kolyvagin-system Tamagawa-defect theorem to `p=2`. The theorem identifies the local 2-primary data only.