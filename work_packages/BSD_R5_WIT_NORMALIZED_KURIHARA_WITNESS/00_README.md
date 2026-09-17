# BSD R5-WIT — normalized finite Kurihara mod-2 witness

Operation: `BSD-R5-WIT` / `grandchallenge/MATHSOLVE#282`.

Protected predecessor: completed `BSD-R5-RECIP`, substantive merge `31abc7b8f8953499c93eea23b9dafdfa4e11f551`, completion overlay `9c9bd9077f8b269277366c7ee81dcdcd7f701217`.

Live branch base: `5b31fda9c4836454d957c4cb9e8ed8cfdb72cf0b`; the intervening protected advance is unrelated NS-CI work.

Entering frontier:

`MISSING_P2_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS`.

This tranche resolves the first local branch point on the protected regime-A/B diagnostic controls `53a1` and `203b1`. Protected R5-RECIP proves that each has a unique nonzero formal rational 2-torsion point and that, since `q_2=#E(F_2)=4`, the only possible local exponents are `t_2 in {1,2,3}`. The exact division-polynomial congruence certificate in this package proves that neither control has a `Q_2`-rational point of order four. Therefore

`#E(Q_2)[2^infinity]=2`

and

`t_2=1`

for both controls.

Consequently the protected normalized Kurihara object is

`Delta_n^(2)=2*delta_tilde_n`

on both controls, so the direct mod-2 witness route is not annihilated by the `t_2>=2` obstruction.

This does not prove that any `Delta_n^(2)` is nonzero. The active next obligation is to evaluate or prove nonvanishing of a legitimate finite derivative on a `t_2=1` selected lane. Provider-side source/software reconnaissance is tracked by `grandchallenge/MATHFORGE#236`.

No R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, public certification, or MATHCERT certification claim is made.