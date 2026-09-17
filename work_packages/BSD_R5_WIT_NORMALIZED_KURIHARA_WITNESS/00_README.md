# BSD R5-WIT — normalized finite Kurihara mod-2 witness

Operation: `BSD-R5-WIT` / `grandchallenge/MATHSOLVE#282`.

Protected predecessor: completed `BSD-R5-RECIP`, substantive merge `31abc7b8f8953499c93eea23b9dafdfa4e11f551`, completion overlay `9c9bd9077f8b269277366c7ee81dcdcd7f701217`.

This work branch has been reconciled through protected post-R5-RECIP repository advances. The current protected MATHFORGE local-torsion provider is

`grandchallenge/MATHFORGE@2a112e28026d33062ea314c55e69c157bf9ae863`.

Entering frontier:

`MISSING_P2_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS`.

This tranche resolves the first local branch point on the protected regime-A/B diagnostic controls `53a1` and `203b1`. Protected R5-RECIP proves that each has exactly one nonzero rational point of order two in the formal subgroup and that, since `q_2=#E(F_2)=4`, the possible local exponents satisfy `1<=t_2<=3`. The admitted Ozeki–Yoshida interface shows that higher good-ordinary local torsion is possible in general, so `t_2=1` cannot be inferred from good ordinarity alone.

The exact division-polynomial certificate in this package proves for each protected control that:

1. the affine two-division polynomial has no root modulo `16`, excluding any second nonformal `Q_2`-rational point of order two;
2. the non-2-torsion fourth-division factor has one possible integral residue class modulo `16`, but the corresponding `y`-discriminant is `20 mod 32` for both lifts modulo `32`, hence is not a `Q_2`-square and yields no point of order four.

Together with the protected formal order-two point this gives

`#E(Q_2)[2^infinity]=2`

and

`t_2=1`

for both controls.

Consequently the protected normalized Kurihara object is

`Delta_n^(2)=2*delta_tilde_n`

on both controls, so the direct mod-2 witness route is not annihilated by the `t_2>=2` obstruction there.

This does not prove `t_2=1` uniformly across the full selected class, and it does not prove that any `Delta_n^(2)` is nonzero. The active next obligation is to evaluate or prove nonvanishing of a legitimate finite derivative on a protected `t_2=1` lane. Provider-side source/software reconnaissance is tracked by `grandchallenge/MATHFORGE#236`.

No R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, public certification, or MATHCERT certification claim is made.
