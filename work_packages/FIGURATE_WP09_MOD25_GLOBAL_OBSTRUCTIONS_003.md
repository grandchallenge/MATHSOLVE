# FIGURATE WP09-003 — global Type B triple obstruction modulo 25

**Status:** internal elementary theorem with complete finite certificate; novelty and independent mathematical certification NOT claimed. Parent: MATH-PROGRAMME #3145. The separate WP05 original-publication gap does not gate this bounded result.

## Statement

Let `P_k(t)=t+(k-2)t(t-1)/2` for integer `k>=3` and positive integer `t`. A Type B triple consists of three distinct positive integers `a,b,d` for which `ab+c`, `ad+c`, `bd+c` are positive-index `k`-gonal numbers. Then **no such triple exists** whenever either:

1. `k=1 (mod 5)`, `c=3 (mod 5)`, and `c != k-3 (mod 25)`; or
2. `k=3 (mod 5)`, `c=3 (mod 5)`, and `c != k (mod 25)`.

This excludes 40 of the 625 order/offset residue cells modulo 25. For each excluded cell, the congruence obstruction is global in entry size and does not impose a bound on a,b,d. By contrast, **modulo 5 alone excludes none** of the 25 order/offset cells. This is a modulo-25 theorem; nonexcluded cells are NOT certified integer solutions or all-prime local solutions.

## Finite proof with exact certificate

The order-lifting formula `P_k(t)=t+(k-2)*binom(t,2)` shows that its residue modulo 25 depends only on `k mod 25`. For odd modulus `q`, the difference `P_k(t+q)-P_k(t)=q[1+(k-2)t+(k-2)(q-1)/2]` is divisible by `q`; hence positive indices `1,...,q` exhaust the polygonal image modulo `q`.

For each of 25 order classes and 25 offset classes, construct the exact output image `I={P_k(t) mod25:1<=t<=25}` and permitted pair-product set `S={v-c mod25:v in I}`. A congruence-compatible triple exists **if and only if** there are residues `a,b,d in {0,...,24}` with `ab,ad,bd in S`. Repeated residue classes MUST be allowed because distinct positive integers may be congruent. Exhausting all 25^3 ordered triples per cell gives precisely the 40 excluded cells in the two families stated above. The full decision predicate, both directions of its equivalence to this finite search, and independent direct-polynomial cross-check are executable in the accompanying source and tests. A residue-compatible triple for an included cell witnesses local compatibility only, not actual integral polygonal outputs.

The certificate is an exhaustive **finite proof** of the residue classification; it is not an unverified inference from bounded enumeration of integer triples. The infinite integer theorem follows since every exact Type B triple reduces to a compatible residue triple modulo 25.

A further direct number-theoretic proof of the two formula families would improve explanation and is a valid independent successor, but is not silently claimed here.

## Reproduce and stress

Run `python3 -m research.figurate_wp09_mod25_global`; expected `{'cells': 625, 'excluded': 40, 'admitted': 585}`. Run `python3 -m unittest tests.test_figurate_wp09_mod25_global` from repository root. The independent checker constructs polygonal residues from the alternate quadratic expression and inspects every ordered residue triple without the producer's pair prefilter. Tests cover the complete 625-cell table, every modulo-5 class, order and offset lifting, negative offsets, and repeated residues.

Example: `k=3,c=8` is excluded modulo 25 but compatible modulo 5, whereas `k=3,c=3` remains modulo-25 compatible.

## Claim and source limits

This is Type B only. It implies neither Type A/C results nor a novelty claim, independent MATHCERT certification, nonexistence for nonexcluded cells, or any failure of a full local-to-global principle. Literature comparison to polygonal tuple papers and earlier modular obstruction results is still required before priority or publication claims. The protected CI/merge and readback must be recorded before marking tranche 003 admitted.
