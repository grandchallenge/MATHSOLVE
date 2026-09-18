# BSD R5-WIT — normalized finite Kurihara mod-2 witness

Operation: `BSD-R5-WIT` / `grandchallenge/MATHSOLVE#282`.

Protected predecessor: completed `BSD-R5-RECIP`, substantive merge `31abc7b8f8953499c93eea23b9dafdfa4e11f551`, completion overlay `9c9bd9077f8b269277366c7ee81dcdcd7f701217`.

Current protected provider inputs:

- local-torsion classification: `grandchallenge/MATHFORGE@2a112e28026d33062ea314c55e69c157bf9ae863`;
- reconciled pinned `79a1` ecdata input: `grandchallenge/MATHFORGE@aeb6588785e70bb7477cdcf44b018c150674c8e4`.

Entering frontier:

`MISSING_P2_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS`.

This tranche resolves the local exponent on three protected selected/diagnostic instances.

For `53a1` and `203b1`, the exact division-polynomial certificate proves

`E(Q_2)[2^infinity] ~= Z/2Z`, hence `t_2=1`.

For the pinned selected instance `79a1`, the exact local certificate proves

`E(Q_2)[2^infinity] ~= Z/4Z`, hence `t_2=2`.

The `79a1` proof is exact: the fourth-division factor has a simple root `x=9 mod 16`, Hensel therefore gives a unique `Z_2` root, the associated Weierstrass discriminant is `4 mod 32` and hence a `Q_2` square, while the exact-order-eight factor has no root modulo `16`. The affine two-division polynomial has no integral root modulo `16`, so no second nonformal order-two point occurs.

Consequently the protected R5-RECIP normalized object stratifies as follows:

- `53a1`, `203b1`: `Delta_n^(2)=2*delta_tilde_n`; the direct mod-2 witness route remains open.
- `79a1`: `Delta_n^(2)=4*delta_tilde_n=0 mod 2` for every admitted derivative level; this particular local-regulator witness route is automatically annihilated.

Thus `t_2=1` is not a uniform consequence of the BSD-001 hard filter. R5-WIT now has two distinct successor obligations:

1. on the protected `t_2=1` controls, compute or prove a legitimate finite `Delta_n^(2) != 0 mod 2`;
2. on the protected `t_2=2` instance `79a1`, identify an alternative residual Kato/Kolyvagin witness not killed by the normalized local regulator.

Provider-side source/software reconnaissance for the finite Kurihara computation is tracked by `grandchallenge/MATHFORGE#236`.

No R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, public certification, or MATHCERT certification claim is made.
