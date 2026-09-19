# BSD R5-RECIP — literal-2 normalized Kato/Kurihara reciprocity

## Operation

Campaign `BSD-001`; theorem operation `grandchallenge/MATHSOLVE#278`.

Exact protected mathematical predecessor: `24081fcc1b212d33dd865cc5512a837b8101faf1` (R5-RES completion). Exact live branch base: `7d72d4f8aec2019a8eefb4db4fe151e4f14b1211`. Protected source provider: `grandchallenge/MATHFORGE@cd814844128167d0e4cdb48f69f9d01c6c0be883`.

The operation addresses only

`MISSING_P2_NORMALIZED_ANOMALOUS_ORDINARY_KATO_KURIHARA_RECIPROCITY`.

It has two theorem layers.

1. `R5-RECIP-LOCAL`: compute the selected good-ordinary literal-2 Kummer/logarithm and Bloch–Kato dual-exponential lattice, including local 2-power torsion and torsion coefficients.
2. `R5-RECIP-SYMBOL`: prove selected-lane 2-saturation of the relative modular-symbol lattice, retain the real-component factor, replay the scaled KKS derivative identity, and combine it with literal-2 Kato reciprocity.

## Candidate result

The normalized finite quantity is

`Delta_n^(2) := 2^t_2 * delta_tilde_n`,

where `2^t_2=#E(Q_2)[2^infinity]`.

For every admitted finite derivative level `I_n`, the operation proves

`xi_n(exp^*_{omega_E,I_n}(loc^s_2(kappa_n^Kato))) = u_n * Delta_n^(2) in Z_2/I_n`,

with `u_n` a unit. This is the selected literal-2 normalized reciprocity law.

The operation does not prove that any `Delta_n^(2)` is nonzero modulo 2. The successor arithmetic frontier is

`MISSING_P2_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS`.

If `t_2>=2`, the proved half-integrality bound implies `Delta_n^(2)=0 mod 2` for every `n`; in that sublane this particular local-regulator witness route cannot establish residual nonvanishing.

## Firewall

R5-LIFT remains protected. R5-PRIM and R5-RES remain unestablished. No D2d, BSD-R2-A1, novelty/priority, public certification, or MATHCERT certification claim is made.