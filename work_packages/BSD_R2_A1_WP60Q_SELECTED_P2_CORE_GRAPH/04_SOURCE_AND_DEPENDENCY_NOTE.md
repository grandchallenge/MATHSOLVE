# WP60Q source and dependency note

## Protected anchors

- constitutional authority: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`;
- mathematical base: `grandchallenge/MATHSOLVE@c8e81d262d4da1a36b312f017443777a4c7888db`;
- protected WP60N theorem merge: `grandchallenge/MATHSOLVE@e6ec267cf5de910d2cb827008c66d10f31fe92c6`, retained in current protected history;
- provider authority: `grandchallenge/MATHFORGE@280646bf69cba8fbb77ba47eb97dda0fb495baa6`;
- WP60O provider record: `sources/BSD-001/BSS_SELECTED_P2_CANONICAL_COISOTROPY_WP60O_SOURCE_AUDIT.md`;
- WP60P provider record: `sources/BSD-001/BSS_SELECTED_P2_CANONICAL_CORE_RANK_WP60P_SOURCE_AUDIT.md`.

## Hypothesis binding

Protected WP60N requires residual self-duality, residual restriction injectivity, cartesianness, core rank one, and residual coisotropy.

The exact selected application binds them as follows.

1. **Self-duality.** The Weil pairing identifies `E[2]` with its Tate dual. This is the same fixed identification used by protected WP60G, WP60H, and WP60J.
2. **Residual restriction injectivity.** WP60J proves residual BSS II Hypotheses 3.2 and 3.3, including vanishing of the relevant primal and dual finite residual auxiliary-field `H^1` groups.
3. **Cartesian.** Protected MATHFORGE WP60P admits the Mazur–Rubin source interface proving the canonical structure propagated from `T_2(E)` is cartesian on every finite quotient, including `E[2]`.
4. **Core rank one.** Protected MATHFORGE WP60P admits the literal-`2` canonical core-rank formula and computes `chi(T_2(E),Fcan)=1`; the residual quotient has the same core rank.
5. **Coisotropy.** Protected MATHFORGE WP60O proves place by place that the exact canonical residual structure is coisotropic under the Weil self-duality.

No Sakamoto `p=3` elliptic theorem is imported as literal-`2` authority.

## Protected theorem applied

MATHSOLVE WP60N proves, under exactly these hypotheses, that the full residual BSS core graph is connected at characteristic two. Its proof contains the new `F_2` exchange step and does not rely on the non-portable `F_3` multi-class localization theorem.

Therefore the selected application is a direct theorem instantiation; it introduces no new localization argument.

## Replay evidence

The WP60Q GitHub Actions workflow replays:

1. the WP60J exhaustive residual cohomology certificate; and
2. the WP60N finite `F_2` relation/exchange certificate.

These executable replays test the finite algebraic components. They do not substitute for the protected source interfaces establishing cartesianness, core rank, or local coisotropy.

## Next proof-dependency

Protected MATHFORGE WP60F records that the published Fitting-control chain passes through BSS II Theorem 5.20 and Theorem 5.2. WP60Q closes the residual core-connectivity input to that chain on the selected literal-`2` lane; WP60M separately provides all-level Selmer-restricted coefficient reduction in place of unchanged full finite Hypothesis 3.2(iii).

The remaining theorem-level implication has not yet been replayed line by line at `p=2`. The exact next obligation is therefore

`MISSING_LITERAL_P2_BSS_THEOREM_5_20_5_2_REPLAY_AFTER_REPLACEMENTS`.

A successor must trace every use of `p>3`, Hypothesis 3.2(iii), Lemma 3.9, core connectivity, and coefficient reduction inside the proofs actually needed for the selected one-sided Fitting conclusion. It must either bind each use to a protected replacement or leave a narrower named boundary.
