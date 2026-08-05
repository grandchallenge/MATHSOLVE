# EUCLID-DIOPHANTINE-E2E-002 — Solve candidate

## Two exact tasks

The constructive task is

\[
252x + 105y = 84.
\]

Stage 1 protected

\[
-2\cdot252 + 5\cdot105 = 21.
\]

Since \(84 = 4\cdot21\), the deterministic producer scales the protected coefficients:

\[
x=-8,\qquad y=20,
\]
and therefore
\[
-8\cdot252 + 20\cdot105 = 84.
\]

The obstruction task is

\[
252x + 105y = 20.
\]

The protected gcd is \(21\), while

\[
20 = 0\cdot21 + 20,\qquad 0<20<21.
\]

The nonzero remainder is candidate obstruction evidence. A timeout, failed search, or missing witness is not unsatisfiability evidence.

## Object, witness, obstruction, and certificate

| Surface | Meaning |
|---|---|
| Object | an integer solution of \(ax+by=c\), when one exists |
| Constructive witness | explicit integers \(x,y\) satisfying the equation |
| Obstruction | an exact nonzero remainder of \(|c|\) modulo the protected gcd |
| Candidate output | deterministic JSON emitted by MATHSOLVE |
| Certificate disposition | an independent MATHCERT judgment and Lean theorem |

These surfaces are not interchangeable.

## Bounded producer scope

The producer reuses the protected Stage 1 certificate for the coefficient family

\[
(|a|,|b|)=(252,105).
\]

It does not recompute gcd and does not claim a general algorithm for arbitrary coefficient pairs. It handles signed coefficients by sign-normalizing the protected Bézout witness. It handles \(c=0\) with the explicit witness \(x=y=0\).

## Modern theorem target

MATHCERT #89 must independently formalize the classical theorem for integers \(a,b,c\), with \((a,b)\ne(0,0)\):

\[
(\exists x,y\in\mathbb Z,\ ax+by=c)
\iff
\gcd(|a|,|b|)\mid |c|.
\]

MATHSOLVE does not prove this theorem.

## Historical boundary

This is a modern normalized extension. It is not attributed verbatim to Euclid. Proposition-level historical concordance remains reserved for the source-locked Book VII microcampaign.

## Authority boundary

The committed outputs are candidate evidence only. They do not certify either case, prove the equivalence theorem, establish completeness for arbitrary Diophantine equations, or support novelty, priority, first-formalization, or historical-verbatim-equivalence claims.
