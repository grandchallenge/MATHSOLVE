# BSD R5-WIT — normalized finite witness and residual bypass

Operation: `BSD-R5-WIT` / `grandchallenge/MATHSOLVE#282`.

Protected operation base: `grandchallenge/MATHSOLVE@8e692aaca7b0932c412a03eb33985ba5994b1d5f`.

Protected predecessor: completed `BSD-R5-RECIP`, substantive merge `31abc7b8f8953499c93eea23b9dafdfa4e11f551`, completion overlay `9c9bd9077f8b269277366c7ee81dcdcd7f701217`.

Protected provider authority:

`grandchallenge/MATHFORGE@3a097cf5f1ad5e12eeba83a08dccfbf7bc49b5f4`.

Entering frontier:

`MISSING_P2_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS`.

## Exact local stratification

The exact division-polynomial certificates prove:

- `53a1`, `61a1`, `83a1`, `203b1`: `t_2=1`;
- `79a1`, `201b1`: `t_2=2`;
- `89a1`: `t_2=3`.

Protected R5-RECIP proves

`Delta_n^(2)=2^t_2 delta_tilde_n`

and therefore forces `Delta_n^(2)=0 mod 2` at every admitted derivative level whenever `t_2>=2`. This only annihilates the normalized local-regulator/Kurihara detector; it does not annihilate the global residual Kato/Kolyvagin class.

## Finite normalized witness search

The exact PARI/GP 2.15.4 probe gives no single-prime normalized mod-two witness through `ell<=2000` on `53a1` or `203b1`.

The deterministic expanded cohort scan through `ell<=500` gives exactly

`DISCOVERY_HITS []`.

The negative scans are bounded evidence. They do not prove nonexistence of a normalized witness on a `t_2=1` curve.

## Direct residual bypass

Protected WP60T gives

`kappa_m(c)_1=c_Q mod 2^m`.

For the Kato Euler system at `m=1` this yields

`kappa_1^Kato{}_1=c_Q^Kato mod 2`.

Thus a proof or exact legitimate computation of

`c_Q^Kato mod 2 !=0`

would itself provide a finite residual witness compatible with protected R5-PRIM finite detection and bypass the normalized Kurihara coordinate.

Protected MATHFORGE `3a097cf5...` admits the direct-detector source audit but does not supply a literal-`2` indivisibility theorem or exact computation establishing this nonvanishing on the selected rank-one anomalous ordinary lane.

## Candidate disposition

`BLOCKED`

on

`MISSING_P2_BASE_KATO_CLASS_MOD2_NONVANISHING_ON_SELECTED_RANK_ONE_LANE`.

This is a substantive evidentiary/theorem boundary. It is not a claim that every other finite residual detector has been excluded.

No R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, public certification, or MATHCERT certification claim is made.
