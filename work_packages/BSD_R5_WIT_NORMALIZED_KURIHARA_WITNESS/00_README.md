# BSD R5-WIT — normalized finite Kurihara mod-2 witness

Operation: `BSD-R5-WIT` / `grandchallenge/MATHSOLVE#282`.

Protected predecessor: completed `BSD-R5-RECIP`, substantive merge `31abc7b8f8953499c93eea23b9dafdfa4e11f551`, completion overlay `9c9bd9077f8b269277366c7ee81dcdcd7f701217`.

Current protected source authorities:

- good-ordinary `Q_2` torsion classification: `grandchallenge/MATHFORGE@2a112e28026d33062ea314c55e69c157bf9ae863`;
- reconciled pinned `79a1` ecdata input: `grandchallenge/MATHFORGE@aeb6588785e70bb7477cdcf44b018c150674c8e4`.

Entering frontier:

`MISSING_P2_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS`.

This tranche resolves the local-exponent branch point rather than assuming a uniform value of `t_2`.

The protected A/B diagnostic controls satisfy

`E_53a1(Q_2)[2^infinity] ~= Z/2Z`,

`E_203b1(Q_2)[2^infinity] ~= Z/2Z`,

so

`t_2(53a1)=t_2(203b1)=1`.

The independently admitted selected curve `79a1`, with model `[1,1,1,-2,0]`, satisfies instead

`E_79a1(Q_2)[2^infinity] ~= Z/4Z`,

so

`t_2(79a1)=2`.

Thus the selected BSD-001 hard filter is genuinely stratified by local 2-primary torsion. Protected R5-RECIP gives

`Delta_n^(2)=2^t_2*delta_tilde_n`

and proves automatic mod-2 vanishing when `t_2>=2`. Therefore every normalized Kurihara witness vanishes mod 2 on `79a1`, while the same automatic obstruction does not apply to the protected `t_2=1` controls.

This does **not** prove that the residual Kato/Kolyvagin class vanishes on `79a1`. It proves only that the normalized local-regulator witness is incapable of detecting it there.

The active theorem frontier is consequently split:

- `MISSING_P2_T2_EQ_1_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS`;
- `MISSING_P2_T2_GE_2_ALTERNATIVE_RESIDUAL_KATO_KOLYVAGIN_WITNESS`.

Provider-side source/software reconnaissance for the first lane is tracked by `grandchallenge/MATHFORGE#236` and remains active.

No R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, public certification, or MATHCERT certification claim is made.
