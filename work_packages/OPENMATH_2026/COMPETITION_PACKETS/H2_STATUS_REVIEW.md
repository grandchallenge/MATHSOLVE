# OM26-H2 freeze-date status review

**Hill:** `alejandrozu/busy-beaver-6-certificates`  
**Candidate:** W89911  
**Protected candidate:** `work_packages/OPENMATH_2026/CONTEST_CANDIDATES/H2/solution.json`  
**SHA-256:** `f8eaa4dbcbc3ecb18f8ddd1734cffe0079457ff3e26a51a25e81f3f6e988ead2`

## Exact surviving claim

The only promoted mathematical claim is:

> Under the protected six-state/two-symbol blank-zero evaluator semantics, W89911 halts after exactly 89,911 transitions with 185 ones, tape span 541, and all six non-halting states reached.

The broader exact-search-validation claim was rejected and remains excluded.

## Freeze-date context

The registered Hill accepts any valid six-state halting machine and ranks by exact runtime. Thus W89911 is a valid finite lower-bound witness if the official evaluator accepts it.

It is **not** a state-of-the-art lower bound for BB(6). Public Busy Beaver records exceeded this runtime decades before the competition: Marxen and Buntrock reported a six-state machine with 13,122,572,797 shifts, and current BB(6) lower bounds are vastly larger. The current BBchallenge record is far beyond ordinary decimal-scale runtimes.

A public exact-string search performed 2026-10-01 did not locate this exact W89911 transition table. Absence from search is not proof that the machine is novel.

## Competition disposition

- **Mathematical validity:** PASS for the finite witness under protected semantics.
- **Event-window provenance:** PASS.
- **State-of-the-art/open-problem advance:** FAIL.
- **Exact machine originality:** UNRESOLVED.
- **Hill-score eligibility:** possible, subject to official evaluator.
- **Handbook novelty credit:** at most a narrow original finite witness if the exact machine is genuinely new; do not describe it as improving the known BB(6) lower bound.

H2 is therefore lower priority than H4. It should be submitted only if the competition workflow permits the exact valid artifact without displacing stronger work or requiring additional mathematical repair.

## Freeze-date sources

- BusyBeaverWiki, BB(6), current/history of lower bounds: https://wiki.bbchallenge.org/wiki/BB%286%29
- bbchallenge historical Busy Beaver page documenting Marxen–Buntrock six-state runtime: https://docs.bbchallenge.org/other/busy.html

## Claim boundary

No claim of S(6) optimality, state-of-the-art lower bound, record discovery, exact-search completeness, or machine novelty.
