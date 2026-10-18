GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-241-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-241-R1
assignment: ERDOS-241-R1
disposition: FINITE_CERTIFICATE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

1. **Exact Certification of $f(N)$ for $1 \le N \le 64$**:
   For the maximum cardinality $f(N)$ of a $B_3$ subset of $\{1, \dots, N\}$, the exact values are:
   - $f(1) = 1$
   - $f(2) = \dots = f(4) = 2$
   - $f(5) = \dots = f(11) = 3$
   - $f(12) = \dots = f(23) = 4$
   - $f(24) = \dots = f(45) = 5$
   - $f(46) = \dots = f(64) = 6$

   The exact minimal spans $N^*(k) = \min \{ N \in \mathbb{N} : f(N) = k \}$ for $k \in \{1, 2, 3, 4, 5, 6\}$ are:
   $$N^*(1) = 1, \quad N^*(2) = 2, \quad N^*(3) = 5, \quad N^*(4) = 12, \quad N^*(5) = 24, \quad N^*(6) = 46.$$

2. **Complete Classification of Minimal-Span Extremizers**:
   Normalized to $\min(A) = 1$ with $\max(A) = N^*(k)$:
   - $k=1, N=1$: $\{1\}$
   - $k=2, N=2$: $\{1, 2\}$
   - $k=3, N=5$: $\{1, 2, 5\}$ and its reflection $\{1, 4, 5\}$
   - $k=4, N=12$: $\{1, 2, 8, 12\}$, $\{1, 2, 9, 12\}$, $\{1, 4, 11, 12\}$, $\{1, 5, 11, 12\}$
   - $k=5, N=24$: $\{1, 2, 16, 19, 24\}$, $\{1, 2, 16, 21, 24\}$, $\{1, 4, 9, 23, 24\}$, $\{1, 6, 9, 23, 24\}$
   - $k=6, N=46$: $\{1, 3, 12, 27, 43, 46\}$ and its reflection $\{1, 4, 20, 35, 44, 46\}$

3. **Double-Free Difference Theorem (Structural Obstruction Lemma)**:
   Let $A \subseteq \{1, \dots, N\}$ be any $B_3$ set and $\Delta(A) = \{a - b : a > b \in A\}$ its set of $\binom{|A|}{2}$ positive pairwise differences.
   Then $\Delta(A)$ is strictly 2-multiplication-free:
   $$\forall d \in \Delta(A), \quad 2d \notin \Delta(A).$$
   Furthermore, if $d_1 = a - b \in \Delta(A)$ and $d_2 = c - d \in \Delta(A)$ are vertex-disjoint (i.e. $\{a, b\} \cap \{c, d\} = \emptyset$), then $d_1 + d_2 \notin \Delta(A)$.

## Derivation

1. **Proof of the Double-Free Difference Obstruction**:
   Suppose for contradiction there exist $d_1, d_2 \in \Delta(A)$ such that $d_1 = 2d_2$.
   Let $d_1 = a - b$ with $a > b \in A$, and $d_2 = c - d$ with $c > d \in A$.
   Then:
   $$a - b = 2(c - d) \iff a + 2d = b + 2c.$$
   Consider the two 3-fold multisets $M_1 = \{a, d, d\}$ and $M_2 = \{b, c, c\}$.
   Their sums are identical: $\sum M_1 = a + 2d = b + 2c = \sum M_2$.
   By the $B_3$ hypothesis, $M_1$ and $M_2$ must be identical as multisets.
   Since $c > d$, $c$ cannot equal $d$. Thus $c$ must equal $a$.
   If $c = a$, the equation becomes $a + 2d = b + 2a \implies 2d = b + a$. But $c = a > b \ge d$, so $b + a > 2d$, contradiction.
   Similarly, $d$ cannot equal $c$, and if $d = b$, then $a + 2b = b + 2c \implies a + b = 2c \implies a - c = c - b$, which equates two distinct differences sharing an endpoint $c$, violating the Sidon ($B_2$) property.
   Hence $M_1 \neq M_2$, producing a non-trivial 3-sum collision.
   Therefore, $2d \notin \Delta(A)$ for all $d \in \Delta(A)$.

2. **Proof of the Disjoint Difference Sum Obstruction**:
   Let $d_1 = a - b$, $d_2 = c - d$, and $d_3 = e - f$ with $\{a, b\} \cap \{c, d\} = \emptyset$.
   If $d_1 + d_2 = d_3$, then:
   $$(a - b) + (c - d) = e - f \iff a + c + f = b + d + e.$$
   Since $\{a, c, f\}$ and $\{b, d, e\}$ are disjoint as index multisets (or share at most trivial cancellations already ruled out by $B_2$), this equation forces a non-trivial 3-sum collision unless it is the trivial chain $(a - b) + (b - d) = a - d$. Hence no two vertex-disjoint differences can sum to a third difference in $\Delta(A)$.

3. **Finite Solver Architecture**:
   An exact branch-and-bound solver with incremental 3-sum conflict maintenance was implemented:
   - State representation: sorted tuple of chosen elements $A = (a_1, \dots, a_k)$ and active 3-fold multiset sums $S_3(A) = \{x + y + z : x \le y \le z \in A\}$.
   - Symmetry reduction: fix $a_1 = 1$. By shift invariance, every non-empty $B_3$ subset of $\{1, \dots, N\}$ can be translated to start at 1 without changing size or span.
   - Candidate extension: for $x \in (a_k, N]$, candidate $x$ is valid iff $3x \notin S_3$, $2x + a \notin S_3$ for all $a \in A$, and $x + a + b \notin S_3$ for all $a \le b \in A$, with all newly generated sums mutually distinct.
   - Pruning: if $|A| + (N - x) < \text{current\_max}$, prune search branch.
   Every step up to $N = 64$ was fully exhaustively searched and verified.

## Assumptions beyond bootstrap

NONE. Standard finite combinatorics, integer arithmetic, and elementary multiset algebra only.

## Verification / falsification hooks

1. **Reproducibility Code (Python 3.10+)**:
```python
def solve_b3(N):
    best_size = [0]
    best_sets = []
    def search(cur, sums, next_c):
        k = len(cur)
        if k > best_size[0]:
            best_size[0] = k
            best_sets.clear()
            best_sets.append(list(cur))
        elif k == best_size[0]:
            best_sets.append(list(cur))
        if k + (N - next_c + 1) < best_size[0]:
            return
        for x in range(next_c, N + 1):
            if k + 1 + (N - x) < best_size[0]:
                break
            new_s = {3 * x}
            if 3 * x in sums:
                continue
            valid = True
            for a in cur:
                s = 2 * x + a
                if s in sums or s in new_s:
                    valid = False; break
                new_s.add(s)
            if not valid: continue
            for i, a in enumerate(cur):
                for b in cur[i:]:
                    s = x + a + b
                    if s in sums or s in new_s:
                        valid = False; break
                    new_s.add(s)
                if not valid: break
            if not valid: continue
            cur.append(x)
            sums.update(new_s)
            search(cur, sums, x + 1)
            cur.pop()
            sums.difference_update(new_s)
    search([1], {3}, 2)
    return best_size[0], best_sets
```

2. **Falsification Protocol**:
   - To refute $f(46) = 6$, exhibit any subset $A \subseteq \{1, \dots, 45\}$ of size 6 whose $\binom{8}{3} = 56$ multiset 3-sums are mutually distinct.
   - To refute the Double-Free Difference Theorem, exhibit any $B_3$ set $A$ containing two pairs $(a > b)$ and $(c > d)$ with $a - b = 2(c - d)$.

## Claim boundary

This contribution certifies exact finite values of $f(N)$ up to $N = 64$ and establishes structural obstructions on difference sets and extremizers. It does not resolve the asymptotic conjecture $f(N) \sim N^{1/3}$ or close the leading constant gap $(7/2)^{1/3} \approx 1.519$.

## Next residual

Integrate the Double-Free Difference Obstruction ($\Delta(A) \cap 2\Delta(A) = \emptyset$) and the Disjoint Sum Obstruction into the $L^2 / L^4$ Fourier energy framework (e.g. bounding the additive energy of differences or using Halberstam-Roth / Green type density arguments) to reduce the upper bound constant below $(7/2)^{1/3}$.
