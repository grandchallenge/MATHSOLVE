# WP16B local-condition and normalization matrix

This matrix is part of the theorem contract. It prevents a later Selmer-complex or Euler-system source from changing the integral object silently.

| Surface | WP16B exact choice | What is forbidden without proof | WP17 comparison obligation |
|---|---|---|---|
| Coefficient ring | `R = Z_2` | replacing `2` by an odd prime; inverting `2`; passing to `Q_2` when integral length is being measured | theorem must be integral at `2` over an explicitly comparable coefficient ring |
| Finite coefficients | `E[2^n]` for every `n >= 1` | using only mod-2 information to infer higher length | exact compatibility through the full `2^n` tower |
| Infinite discrete module | `E[2^infinity]` as the direct-limit coefficient object underlying the Kummer tower | an unproved ordinary quotient or relaxed coefficient object | identify the theorem's coefficient module with this object or compute the exact defect |
| Global Selmer object | `Sel_{2^infinity}^{Kum}(E/Q) := colim_n Sel_{2^n}(E/Q)` | replacing the direct-limit primitive tower by a different Selmer structure without comparison | exact equality or finite kernel/cokernel comparison |
| Real place | levelwise local Kummer image | deleting the archimedean place merely because it is harmless for odd `p` | retain or prove the exact `2`-primary archimedean defect is zero |
| Place `2` | finite classical Kummer image `E(Q_2)/2^n -> H^1(Q_2,E[2^n])` | identifying Kummer and Greenberg/ordinary conditions automatically | exact comparison with the connected-etale ordinary condition if the source uses it |
| Good ordinary fact at `2` | selected hypothesis; WP07 local facts remain active | treating good ordinary as residual `2`-distinguished | source must survive the protected failure of the standard residual distinguished condition |
| Good primes `ell` not dividing `2N` | full levelwise Kummer condition | unnecessary local-condition replacement | prove any alternate unramified formulation is exactly equivalent in the theorem's normalization |
| Bad semistable primes `ell | N` | full primitive Kummer image | silently replacing by unramified, strict, relaxed, or imprimitive condition | compute the exact local comparison defect |
| Tamagawa factors | no separate factor inserted into `T_E`; analytic side remains `delta_2(E)=ord_2(L'/(Omega Reg))-sum ord_2(c_ell)` | calling `c_ell` a unit at `2`; assuming an imprimitive defect equals the Tamagawa term without proof | match every local defect against protected WP13 exact valuations |
| Residual conductor | both WP13 regimes retained | restricting silently to `N(rho_bar)=N` or all `c_ell` odd | theorem must cover even-Tamagawa residual-conductor drop or state a genuinely restricted result |
| Rank-one free direction | canonical saturated quotient `X_E/Tor(X_E) ~= L_E`, where `L_E := (E(Q) tensor (Q_2/Z_2))^vee` is free of rank one | choosing a basis of `L_E` and treating it as canonical; replacing the saturated free line by the span of a nonprimitive point without its index | compute the exact index of any Heegner/Euler-system generator sublattice |
| Finite integral invariant | `T_E := Tor_{Z_2}(X_E)` | applying `Fitt^0` to the whole rank-one module | theorem must control `T_E` or an exactly comparable torsion/determinant object |
| Fitting normalization | `Fitt^0_{Z_2}(T_E) = 2^{len T_E} Z_2` | a generator equality merely `up to a unit` when a power of `2` is missing | equality/divisibility of ideals with exact valuation information |
| Primitive/imprimitive convention | primitive at every finite prime | dropping Euler factors without a local ledger | restore every deleted local factor and show its exact `ord_2` contribution |
| Quadratic base change | protected WP09 field `K`; use WP06 exact restriction/corestriction discrepancy accounting | odd-prime `(1 +/- tau)/2` splitting | carry every WP06 exponent-2 kernel/cokernel term; exploit split places only where WP06 proves zero defect |
| Certification | none | treating source admission, CI, or theorem packaging as certification | MATHCERT only after an exact selected equality is proved |

## Exact invariant

Write

`X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`

and

`T_E := Tor_{Z_2}(X_E)`.

Protected WP16B proves

`Fitt^0_{Z_2}(T_E) = 2^{lambda_E} Z_2`,

where

`lambda_E = lim_n (ord_2 #Sel_{2^n}(E/Q) - n)`.

Thus the exact remaining analytic-to-arithmetic theorem is

`delta_2(E) = v_2(Fitt^0_{Z_2}(T_E))`.

## Tamagawa regime discipline

Protected WP13 supplies two regimes.

### Regime A

Every bad `c_ell` is odd and the residual conductor does not drop. Then the explicit Tamagawa sum in `delta_2(E)` is zero.

### Regime B

One or more bad `c_ell` are even and the residual conductor drops exactly at those primes. WP13 records the exact `2`-adic Tamagawa depths. WP16B retains this regime unchanged.

An external theorem restricted to Regime A is a restricted theorem. It may not be promoted to the selected full class.

## Kummer versus ordinary discipline at `2`

Protected WP06 failure analysis explicitly terminates the shortcut that identifies finite Kummer and Greenberg ordinary conditions at `2`. WP16B therefore treats these as distinct interfaces.

The fact that the protected WP09 field `K` splits `2` is useful for base-change transport: WP06 proves split local descent has zero extension defect. It does not, by itself, prove equality between two different local conditions on the same field.

## Basis and unit discipline

The Fitting **ideal** is basis-independent. If a presentation determinant changes by a unit of `Z_2`, the generated ideal is unchanged and so is its valuation.

This does not license the loss of a factor `2^m`. A factor `2^m` is not a unit for `m>0`.

Likewise, choosing a nonprimitive rank-one generator can change a lattice by index `2^m`; that index belongs in the theorem, not in an unspecified unit.
