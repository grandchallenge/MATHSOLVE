# FIGURATE bounded census: reproducible 2026-11-03 snapshot

**Status:** exact, finite enumeration evidence; not an unbounded mathematical theorem, novelty certification or performance study.

## Inputs and outputs

[Canonical CSV](figurate_census_2026_11_03_L60.csv) contains 270 parameter rows, covering each family A (polygonal entries and square products plus offset), B (arbitrary positive entries and polygonal pairwise outputs), and C (polygonal entries and polygonal pairwise outputs). For all families the polygonal order runs from 3 to 12, the additive offset is one of -1, 0, 1, the tuple size is 2, 3 or 4, and all tuple entries are distinct positive integers at most **60**. The CSV gives tuple counts and the lexicographically first witness; an empty witness column means the bounded search found none.

A row with zero count establishes only that no solution exists inside this entry-value bound.

The snapshot was generated on 2026-11-03 with an independently implemented exact integer compatibility graph and increasing-clique algorithm; 135 parameter rows were cross-checked in a separate direct combination enumerator. The archived CSV is not a checksum or a standalone mathematical certificate. Run the source-based replay and targeted independent regressions below.

## Replay commands

From the MATHSOLVE repository root:

```sh
python3 -m research.figurate_census_replay
python3 -m unittest discover -s tests -p 'test_figurate_census_archive.py'
python3 -m unittest discover -s tests -p 'test_figurate_census.py'
python3 -m research.figurate_census --kind B --k 3 --offset 1 --limit 60 --size 3
```

The archive replay reads every row, checks the domain and parameters, recomputes tuple counts through the existing exact-integer producer, and checks the first tuple and all pairwise witnesses using the integer-only membership checker. Regression tests independently check selected cases by ordinary combinations and direct polygonal-number sets. This is an internal computational cross-check, not external verification.

## Observed totals (sum over 30 order/offset choices for each size)

| Constraint | Pairs | Triples | Quadruples |
| --- | ---: | ---: | ---: |
| A | 42 | 35 | 35 |
| B | 1312 | 137 | 41 |
| C | 65 | 38 | 35 |

The columns are **counts of tuples aggregated across distinct parameter settings**, not unique tuples across settings. The same tuple can appear under different settings.

For order 3 with offset 1, family B has 11 triples with entries at most 60, beginning with (1,2,27). For order 4 with offset 1, family B has 35 triples, beginning with (1,3,8). No positive-size-4 triples in this particular finite panel occur outside order 4, offset 0; the 41 family-B quadruples there include (1,4,9,16).

**Interpretation warning:** the offset-0 square case is structurally degenerate: any collection of distinct squares satisfies the square-product condition. It should never be presented as evidence for deep extension behaviour. Family A and C all nonzero four-tuples in this snapshot occur in that same easy case.

## Limitations and forward path

The 60-entry cap is intentionally modest, so this snapshot offers a reproducibility baseline, not a meaningful search frontier. It excludes larger examples, does not establish maximum tuple size, and gives no estimate of the asymptotic number of tuples. No wall-clock or hardware benchmark is claimed. Improve completeness by recording search version and environment, exact result hashes, separate exhaustive certification of graph construction, and larger-scope modular sieving. Prior art is catalogued in the public [FIGURATE bibliography](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/docs/campaigns/FIGURATE_SOURCES.md).

**Programme:** [MATH-PROGRAMME #3093](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093). The research pilot remains open for theorem discovery, formal checking and novelty review.
