# FIGURATE WP06 — exact entry-bound 240 expansion

**Programme:** [FIGURATE-PILOT-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093), [WP06](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3097).

**Scope:** 54 parameter settings at upper *entry-value* bound 240. Type B: orders 3–8, offsets -1, 0, +1, sizes 3 and 4 (36 settings). Type A and Type C: orders 3,4,5, the same offsets, size 3 (18 controls). The known L60 archive remains separate. Parameters outside this panel are **not evaluated**.

## Artifacts and reproducibility

- [Panel runner](figurate_wp06_panel.py), exact modular prefilter and strictly increasing compatibility-graph enumeration.
- [Frozen archive](figurate_wp06_L240_panel.csv), SHA-256 `7d3be393be72d299fe0cf8a288284a35b23feb44dd61f1dcf4670cfd16422f43`.
- [Archive test](../tests/test_figurate_wp06_L240_archive.py): regenerates all 54 cases, checks byte identity and SHA-256, and compares **each** count and lexicographically first tuple against the independent exact baseline implementation.
- Existing [sieve correctness regression](../tests/test_figurate_residue_sieve.py): 270-case L60 parity, local residue preservation, larger sampled tests.

```sh
python3 -m research.figurate_wp06_panel --output research/figurate_wp06_L240_panel.csv
python3 -m unittest discover -s tests -p 'test_figurate_wp06_L240_archive.py' -v
python3 -m unittest discover -s tests -p 'test_figurate_residue_sieve.py' -v
```

The generation command overwrites its declared output file; execute in a clean checkout or temporary copy when the archived bytes should remain untouched.

## Measured run

CHAD workstation, Python 3.10.12, Linux 6.6.87.2-microsoft-standard-WSL2 x86_64. One observed execution of the panel runner:

| Measurement | Value |
| --- | ---: |
| Rows | 54 |
| Sieve panel generation | 0.992255 s |
| Independent full baseline validation | 0.749460 s |
| Summed candidate pairs across rows | 1,034,766 |
| Summed pairs rejected by residue tests | 907,694 |
| Summed exact membership calls | 127,072 |

The pair totals count repeated pair-graph construction separately for each requested tuple size: they are work counters over **settings**, not unique pairs. The timing measures **different total tasks** (the sieve computes additional telemetry and the baseline performs full witness enumeration). It does **not** establish a speedup or a complexity improvement. Independent replication with repeated seeds/runs and matched workload would be required for performance claims; randomness is absent here.

### Selected exact observations

| Parameters | Tuples | First lexicographic tuple |
| --- | ---: | --- |
| Type B, triangular (order 3), offset +1, size 3 | 63 | {1,2,27} |
| Type B, triangular, offset +1, size 4 | 0 | none within bound |
| Type B, square (order 4), offset +1, size 4 | 1 | {1,3,8,120} |
| Type B, square, offset 0, size 4 | 1685 | {1,4,9,16} |
| Type A, triangular, offset +1, size 3 | 1 | {1,3,120} |
| Type C, triangular, offset 0, size 3 | 13 | {1,3,15} |

The square-output control {1,3,8,120} is Fermat's known Diophantine quadruple. The previously recorded Type B triangular-output quadruple {14,31,135,3510} from Filipin–Szalay (2023) lies **outside** this bound. A zero in a finite row cannot be promoted to global nonexistence.

## Research next gate

**Disposition (5 November 2026): WP06's bounded acceptance is COMPLETE.** The 270-case L60 archive, complete 54-case L240 panel, exact-residue prefilter, independent full-baseline replay, frozen source/archive SHA, executable regressions and protected-main evidence satisfy the finite search/sieve work package as written. WP06 is closed as an exact *bounded* research package, not a proof of unbounded completeness or a certification of a new theorem.

**Optional future research, outside the completed WP06 acceptance:** systematic growth beyond the present bound; matched-workload repeated timing experiments before any performance claim; further completeness coverage at larger bounds; or searches motivated by later structural obstruction theorems. These are distinct potential work, **not retrospective requirements** that indefinitely keep the delivered finite experiment open. No novel theorem claim, source novelty, independent proof certification, or global classification is assigned to this archive.
