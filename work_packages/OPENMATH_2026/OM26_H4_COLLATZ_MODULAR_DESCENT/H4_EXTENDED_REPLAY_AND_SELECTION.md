# H4 extended classification replay and rule selection

**Record:** `OM26-H4-EXTENDED-REPLAY-001`  
**Bound source:** predecessor `OM26-H4-WP03-IA-001` at protected source head `36b7c79bebd42fde17ea9f0f809406fb55e093f9`  
**State:** `CURRENT_CONTEXT_INDEPENDENT_RECONSTRUCTION__CI_REQUIRED__NO_CANONICAL_PROMOTION`

## Replay result

A fresh reconstruction of the deterministic accelerated-Collatz search reproduced the predecessor's stage `(kmax, depthmax) = (12, 8)` exactly:

- 32,752 deterministic prefixes;
- 10,641 valid strict-descent prefixes;
- full valid-catalog SHA-256 `65a215b170d65d7c8f66e14117cab7c7b4a3cdc8802a7a677898163c1c8adab3`;
- 107 maximal dyadic coverage classes;
- 3,352 coverable odd target classes across public target powers 8 through 12, distributed 94, 203, 421, 869, 1,765.

The stage `(14,10)` expansion is not useful for the registered evaluator's primary or secondary metrics because private targets have modulus powers only 8 through 12. Rules with modulus power 13 or 14 cannot cover those targets.

## Selection

`H4_EXTENDED_107_PROPOSED_SOLUTION.json` keeps exactly one rule for every maximal coverage class. For each fixed `(modulus_power, residue)` class it selects the valid prefix with the largest exact affine contraction margin.

This differs from the predecessor's containment reduction on seven classes, where its ordering preferred a shorter prefix before a stronger margin. The replacements are:

- `(6,33): [2] -> [2,2]`;
- `(7,65): [2] -> [2,2]`;
- `(8,129): [2] -> [2,2,2]`;
- `(9,257): [2] -> [2,2,2]`;
- `(10,513): [2] -> [2,2,2,2]`;
- `(11,1025): [2] -> [2,2,2,2]`;
- `(12,2049): [2] -> [2,2,2,2,2]`.

The proposal therefore has identical coverage classes and identical rule count to the 107-rule predecessor reduction, while its per-target best margin is never smaller and is strictly larger on some publicly possible target classes. This is a deterministic Pareto improvement requiring no hidden-target information.

Across the complete public target universe reachable by the stage-(12,8) catalog, both the full 10,641-rule catalog and this 107-rule coverage frontier have worst-case exact contraction margin `13/256`. The complete catalog has 77 target classes pinned at that margin, so no subset of the existing stage-(12,8) certificates can raise the robust worst-case margin above `13/256`.

## Why not fill all 512 slots

Additional narrower rules can improve margins for some possible hidden targets, but they cannot increase the stage-(12,8) coverage union and cannot raise the robust worst-case margin. They also increase the evaluator's tertiary rule-count metric. Without hidden-target information there is no unconditional dominance argument for adding them. The 107-rule proposal is therefore the conservative useful-rule selection.

## Claim boundary

This is current-context replay evidence and a proposed payload, not a canonical contest candidate. Do not replace `CONTEST_CANDIDATES/H4/solution.json` until the separate zero-context replay-closure successor and normal protected adjudication have completed. No organizer score, hidden-target result, novelty claim, certification, or competition submission follows.
