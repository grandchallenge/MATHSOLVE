# RH-R030 — Prime-5 compact-window Weil positivity

## Disposition

`RH-R030_SELECTED__FIRST_BRIDGE_PROVED`

Campaign: `RH-001`  
Terminal target: `RH-T-000` — open  
Selected WP02 bridge: `RH-T-160` (Weil positivity), using `RH-T-100` (explicit-formula transport)  
Source gate: `RH-D-009` route-specific audit protected in MATHFORGE merge `5393699f6f3fbdcc38c729e9871c126936110618`  
Certification state: existing RH statement interface only; no restricted theorem is yet MATHCERT-certified

## Why this target

The protected WP02 theorem graph left the Weil route semantically under-specified. A current source audit changes that frontier.

Xuefeng Zhu, arXiv:2608.24827v2 (2026-09-02), fixes an exact geometric-side normalization and proves unconditional positivity for every complex test function supported in `[-0.8,0.8]`, with a certified lower bound `8.9e-18 ||f||_2^2`. The same version retracts an earlier claimed certificate at `L=1.19` because a prime-comb bound was used in the wrong direction.

Therefore `L <= 0.8` is not a defensible new restricted target. The first prime threshold above that frontier is

`(log 5)/2 = 0.804718956...`.

We select the smallest simple rational window across it:

`L = 161/200 = 0.805`.

This choice forces a real arithmetic change: the `n=5` von Mangoldt term enters the exact Weil symbol. It is not merely a cosmetic epsilon extension.

No novelty or priority claim is made. The bounded 2026-09-16 audit did not locate an all-test-function theorem beyond `L=0.8`; that search result is used only to justify restricted-target selection.

## Exact theorem target

Let

`L := 161/200`.

For every complex `f in L^2(R)` with

`supp f subset [-L,L]`,

prove

`Q(f) >= 0`,

where `Q` is exactly the Riemann-Weil quadratic form in arXiv:2608.24827v2.

For real even `f`, with

`F(t) = integral_R f(u) exp(i t u) du`, 

the locked geometric normalization is

`Q(f) = 2 F(i/2)^2 + (1/(2*pi)) integral_R |F(t)|^2 Psi_L(t) dt`, 

with

`Psi_L(t) = Re psi(1/4 + i t/2) - log pi - sum_{log n < 2L} (2 Lambda(n)/sqrt(n)) cos(t log n)`.

The complex theorem uses the source's real/imaginary and even/odd decompositions. In particular, the odd pole term has the source-prescribed sign reversal. No prime, pole, archimedean, parity, or tail term may be dropped.

At the selected window, the active prime powers are exactly

`{2,3,4,5}`.

Thus

`A_L = sqrt(2) log 2 + (2/sqrt(3)) log 3 + log 2 + (2/sqrt(5)) log 5`.

## Why this is strictly narrower than RH

Weil's criterion requires non-negativity on the full admissible test-function class, equivalently across unbounded support. `RH-R030` fixes one compact window only.

Even a complete proof of `RH-R030` would not imply positivity at any larger support and would not prove `RH-T-000`.

A genuine negative value of `Q` for one admissible test function in this window would, by contrast, falsify RH. That asymmetry is part of the exact target and is why numerical negative eigenvalues are treated with extreme care.

## Candidate set and dispositions

The MATHFORGE `RH-D-009` audit considered four distinct bridge families.

| Candidate | Parent | Disposition | Reason |
|---|---|---|---|
| density estimate to prime-distribution consequence | `RH-T-050` | rejected for this tranche | current source already develops consequences of the 2026 density exponent; a generic bridge duplicates source-adjacent prior art |
| Nyman-Beurling approximation increment | `RH-T-120` | rejected for immediate selection | `RH-D-003` semantic debt still prevents a stable exact target, and finite approximation must not be promoted to closure |
| Hilbert-Pólya no-go for natural operator classes | `RH-T-200` | rejected in generic form | Watson-Valentinuzzi 2026 already establishes broad heat-trace / spectral-dimension obstructions; `RH-D-007` still blocks a positive operator lane |
| compact-window Weil positivity beyond `L=0.8` | `RH-T-160` / `RH-T-100` | selected | exact current frontier, exact arithmetic threshold, bounded certificate mechanism, and a falsifiable fixed-window theorem |

## First substantive result — `RH-R030-L001`

### Statement

At `L=161/200`:

1. the active prime powers in `Psi_L` are exactly `{2,3,4,5}`;
2. the prime-comb mass is the exact `A_L` displayed above;
3. for `T# = 600`, the one-stroke envelope parameter

   `beta* = log(600/(2*pi)) - 1/600 - A_L`

   satisfies

   `beta* > 97217/600000 > 0`;
4. therefore the hypotheses of Zhu's Theorem 1.1 hold at this exact window and frequency cutoff, and the real-even target reduces to the explicit leading Legendre matrix plus the theorem's explicit tail-deviation and leading-tail-coupling obligations.

### Proof

The exact checker is `verify_first_bridge.py`. It uses rational arithmetic only, apart from one named imported classical fact `pi < 22/7`.

For prime-comb membership, the checker encloses `exp(1.61)` by finite positive-series bounds:

`5 < exp(1.61) < 6`.

Hence the positive integers with `log n < 1.61` are exactly `n <= 5`; among `n=2,3,4,5`, all have non-zero von Mangoldt weight, so the active prime powers are exactly `{2,3,4,5}`.

For the comb mass, exact finite-series and squaring inequalities establish the safe bounds

- `log 2 < 0.694`;
- `log 3 < 1.099`;
- `log 5 < 1.61`;
- `sqrt(2) < 1.415`;
- `2/sqrt(3) < 1.155`;
- `2/sqrt(5) < 0.895`.

Therefore

`A_L < 4.386305 = 877261/200000`.

The classical `pi < 22/7` gives

`600/(2*pi) > 1050/11`.

A finite exponential-series upper bound proves

`exp(4.55) < 1050/11`,

so

`log(600/(2*pi)) > 4.55`.

Combining the inequalities gives

`beta* > 4.55 - 1/600 - 4.386305 = 97217/600000 > 0`.

This proves the first bridge exactly. It does not evaluate the matrix and does not prove `RH-R030`.

## Proof-obligation DAG

```text
RH-D-009 current source/prior-art audit
    |
    v
RH-R030-P001 normalization + prime-comb membership
    |  CLOSED by RH-R030-L001
    v
RH-R030-P002 certified T#=600 even-sector matrix assembly
    |
    v
RH-R030-P003 positive leading-block bound + tail/coupling closure
    |\
    | \ 
    |  +----------------------+
    v                         v
RH-R030-P004 odd-sector certified reduction
    \                         /
     \                       /
      +----> RH-R030-P005 <---+
             complex fixed-window theorem
                    |
                    v
             RH-R030-P006
             independent MATHCERT route
```

`P002` and `P003` are the immediate mathematical frontier. `P004` may use the same frequency/tail machinery but must preserve the sign-reversed odd pole term. `P005` cannot close from the even sector alone.

## Smallest falsifiers

Target falsifier: one rigorously evaluated admissible `f` with support in `[-161/200,161/200]` and `Q(f)<0`.

Method falsifier: failure of the certified `T#=600` leading-block/tail inequality. This would terminate this one-stroke certificate instance only; it would not falsify `RH-R030` or RH.

Neither an uncertified truncated negative eigenvalue nor a float64 sign qualifies as a falsifier.

## False-proof firewall

Reject any proposed completion that does any of the following:

- omits the newly active `n=5` term;
- substitutes a smaller prime-comb envelope without proving the required uniform inequality direction;
- proves positivity only on a finite family while leaving the tail uncontrolled;
- relies on ordinary float64 signs near the spectral floor;
- closes only the even sector while claiming arbitrary complex tests;
- uses a numerical upper bound as a positivity lower bound;
- extrapolates fixed-window positivity to all supports;
- treats the retracted `L=1.19` computation as a theorem;
- infers RH from any finite support window.

## Computational support policy

The next computation is not a broad parameter sweep. It has one theorem interface:

`L=161/200`, `T#=600`, exact prime powers `{2,3,4,5}`.

A valid certificate must include:

- high-precision or interval-closed matrix assembly;
- exact inclusion of the pole and prime terms;
- a certified quadrature error;
- a verified positive lower bound for the leading block;
- an explicit tail-deviation bound;
- an explicit leading-tail coupling bound;
- an independent replay path;
- the odd-sector analogue before any complex theorem is claimed.

Exploratory float64 calculations may be used only to debug implementation and choose precision. Their eigenvalue signs have no evidentiary status.

## Non-implications

This package does not prove or certify:

- the Riemann Hypothesis;
- positivity outside `L=161/200`;
- a new zero-free region;
- a new density estimate;
- a new critical-line proportion;
- a new certified zero range;
- a Hilbert-Pólya operator;
- novelty or priority;
- publication readiness.

## Certification route if the target closes

Only after `P005` closes should Solve prepare a new bounded MATHCERT handoff. That packet must bind the exact source version, theorem statement, certified matrix/arithmetic artifacts, imported-theorem boundary, proof-obligation lineage, replay identity, and the statement that `RH-T-000` remains open.

The existing `MC-FC-WP00-RH-001` interface qualification is not to be reopened merely to record this research lane.
