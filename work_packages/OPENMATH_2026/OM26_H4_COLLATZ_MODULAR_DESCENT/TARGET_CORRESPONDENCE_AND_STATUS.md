# OM26-H4 target correspondence and replay closure

**Hill:** `alejandrozu/collatz-modular-descent`  
**Protected source bind:** `grandchallenge/MATHSOLVE@50b88f51032a14aeae5c3969e14dd8c5a8728bac`  
**Candidate:** `work_packages/OPENMATH_2026/CONTEST_CANDIDATES/H4/solution.json`  
**Candidate SHA-256:** `b14c4804dae95df88ffa7dcef865205edd295e1f2e8c4daeba75333053a6673a`

## Exact registered task

The protected Hill asks for finite exact certificates for odd dyadic residue classes under the accelerated odd Collatz map
[
C(n)=(3n+1)/2^{v_2(3n+1)}.
]
A rule fixes `n ≡ r (mod 2^k)` and an exact sequence of 2-adic valuations. The evaluator admits a rule only when the valuation pattern is stable on the whole class and the resulting affine map strictly descends on the whole class.

The score is held-out target coverage, then minimum affine descent margin, then rule count. The Hill explicitly states that a high score is not a proof of the Collatz conjecture.

## Candidate correspondence

The retained payload has 23 rules. Independent replay on GitHub Actions run `36877035405`, job `110418981039`, checked:

- both a direct accelerated-trajectory implementation and a separately written affine-coefficient implementation;
- all 1,016 candidate prefixes in the bounded region `2 <= k <= 8`, depth `1..4`;
- 309 valid bounded rules;
- deterministic containment reduction to exactly the 23 retained rules;
- exact full-catalog SHA-256 `951521f5064f0842993e895648b2b8bde2b29dda0d47c9d586ddac498bfa4f55`.

The independent replay therefore closes the GCL replay/correspondence gate for the bounded mathematical claim:

> Each retained rule is an exact stable accelerated-Collatz residue-class descent certificate, and the 23-rule payload is exactly the deterministic reduction of the independently reconstructed bounded catalog.

This is correspondence to the registered Hill target. It is **not** correspondence to a claim of global Collatz convergence.

## Novelty/status boundary

The mathematical mechanism is not new. Classical stopping-time work by Terras (1976) and Everett (1977) studies residue/parity classes with finite stopping time, and later tabulations explicitly list congruence classes sharing stopping times. OEIS A177789 records such residue classes, and later work continues modular first-descent analysis.

A freeze-date search performed 2026-10-01 found no exact match for this specific 23-rule `k<=8`, depth-`<=4`, containment-reduced catalog in the searched public sources. That absence is not a proof of novelty.

Accordingly the competition-facing claim shall be conservative:

- do not claim a new general Collatz theorem or new residue-class mechanism;
- present the event-window contribution, if admitted, as the exact finite certificate collection and its independently reproducible bounded classification;
- let competition review determine whether that finite classification earns M1 formalized-partial credit (the handbook explicitly allows narrow certified computations/finite classifications at P1/P2 scope) or is prior-overlap/M2-only.

## Sources checked for status

- Riho Terras, *A stopping time problem on the positive integers*, Acta Arithmetica 30 (1976), 241–252, DOI 10.4064/aa-30-3-241-252.
- C. J. Everett, *Iteration of the number-theoretic function f(2n)=n, f(2n+1)=3n+2*, Advances in Mathematics 25 (1977), 42–45.
- OEIS A177789, residue classes associated with Collatz dropping/stopping times.
- Mike Winkler, *On the Structure and the Behavior of Collatz 3n+1 Sequences*, arXiv:1412.0519.
- Mike Winkler, *New results on the stopping time behaviour of the Collatz 3x+1 function*, arXiv:1504.00212.
- Seyma Yaman Kayadibi, *A Modular Classification of Pre-Descent Resistance in Accelerated Odd Collatz Dynamics* (2026), as additional freeze-date context.

## Remaining competition gates

1. organizer official evaluator report / held-out score;
2. competition submission ID and workflow;
3. entrant roster/class and full Section 8 disclosure packet;
4. organizer mathematical novelty/status adjudication.

No mathematical repair is required for the 23-rule bounded certificate claim after the trusted replay pass.
