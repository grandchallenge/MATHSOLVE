GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-Q01-IA-001
assignment: E3-Q01
agent_ref: INDEPENDENT-AGENT-E3-Q01-001
disposition: EXACT_BLOCKER
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_ALLOWED

## Strongest exact statement

Let
\[
a_n:=\frac{r_4(2^n)}{2^n}.
\]
The Green–Tao 2017 argument, as stated and iterated in its quantitative core, is a **single-ambient-scale recurrence theorem** on \(\mathbb Z/p\mathbb Z\). It yields the pointwise consequence
\[
a_n\ll n^{-c}
\]
for some absolute \(c>0\), but it does not output an averaged estimate in the scale variable \(n\), nor a recurrence relating \(r_4(N)\) to \(r_4(M)\) at two different ambient sizes.

Moreover, interval localization alone gives only the exact subadditivity bound
\[
r_4(N)\le \Big\lfloor\frac NM\Big\rfloor r_4(M)+r_4(N\bmod M),
\]
hence, when \(M\mid N\),
\[
\frac{r_4(N)}N\le \frac{r_4(M)}M.
\]
At dyadic scales this is only \(a_n\le a_m\) for \(n\ge m\), i.e. the already-known monotonicity. Combining localization with the Green–Tao pointwise theorem gives no stronger bound: for \(m\le n\),
\[
a_n\le a_m\ll m^{-c},
\]
whose strongest choice is \(m=n\).

A concrete theorem-grade sequence estimate that *would* close the series is the following cross-scale contraction: if there exist \(q<1/2\) and \(n_0\) such that
\[
a_{2n}\le q,a_n\qquad(n\ge n_0),
\]
then \(\sum_n a_n<\infty\). More generally, if \(\lambda>1\) and \(q<1/\lambda\) satisfy \(a_{\lfloor\lambda n\rfloor}\le q a_n\) eventually, then the series converges.

Thus the smallest named missing estimate exposed by this attack is:

**E3-Q4-CROSS-SCALE-CONTRACTION:** prove any theorem-grade extremal recurrence/average estimate that creates genuine decay across the scale index, e.g. \(a_{2n}\le q a_n\) with \(q<1/2\), or a weaker averaged analogue whose block masses are summable.

## Derivation / evidence

**Protected-packet identity check.** The immutable task and all supplied packet objects were read at commit
\[
\texttt{bf9bc7f448f92d71afeae937fda133b0e1d4de80}
\]
and their Git blob SHA-1 identities matched exactly:

- E3-Q01: \(\texttt{2199cf558a812a7c2fe517129de1e6e058d2912c}\);
- E3-B02_RESULT: \(\texttt{0c6a3192294f9017a2e6bb18fa1cd4063d78a818}\);
- E3-S02_RESULT: \(\texttt{bf52757797483b09b29292a326f0cecd3779ca9b}\);
- FRONTIER.json: \(\texttt{464574eb705c841e332035f35a4b44b83d57c296}\).

No later repository state or other contributor return was used.

**Sourced fact 1 — what Green–Tao actually prove.** Green–Tao, arXiv:1705.01703v3, Theorem 3.1, prove that for a fixed prime \(p\), parameter \(\eta\), and function \(f:\mathbb Z/p\mathbb Z\to[-1,1]\), there exist generally coupled random variables \(\mathbf a,\mathbf r\) with near-uniform mean, a Khintchine-type four-term recurrence lower bound, and a thickness bound
\[
\mathbb P(\mathbf r=0)\ll \exp(-\eta^{-O(1)})/p.
\]
Applying this to a 4-AP-free indicator and choosing \(\eta\) as a negative power of \(\log p\) gives Theorem 1.1,
\[
r_4(N)\ll N(\log N)^{-c}.
\]
The paper's abstract explicitly says this polylogarithmic bound “appears to be the limit of our methods.”

**Sourced fact 2 — the internal iteration is not a recurrence in ambient size.** Proposition 3.3 and the proof of Theorem 3.1 iterate structured local approximants while keeping the same prime \(p\) fixed. The iteration alternates energy decrements and quadratic-dimension decrements, with the largeness condition
\[
p>\exp(\eta^{-3C_5}).
\]
This mechanism controls complexity and error inside one ambient cyclic group; it never produces a second ambient size \(p'\), a subproblem value \(r_4(M)\), or a scale-index recurrence for \(a_n\).

**Sourced fact 3 — the paper identifies the relevant loss of uniform recurrence.** Immediately after deriving Theorem 1.1, Green–Tao note that an earlier independent-\(\mathbf a,\mathbf r\) formulation gave a many-differences recurrence statement, but state that the present method does not seem to provide a good bound of that form because \(\mathbf a\) and \(\mathbf r\) are coupled. This removes the most obvious route from their recurrence theorem to an interval-uniform or scale-uniform extremal recurrence.

**Own derivation 1 — exact localization inequality.** Let \(A\subseteq[1,N]\) be 4-AP-free and partition \([1,N]\) into \(\lfloor N/M\rfloor\) full intervals of length \(M\) plus one remainder of length \(s=N\bmod M\). Translation preserves 4-AP-freeness, so each full interval contains at most \(r_4(M)\) points of \(A\), and the remainder at most \(r_4(s)\). Maximizing over \(A\) proves
\[
r_4(N)\le \lfloor N/M\rfloor r_4(M)+r_4(s).
\]
For \(M\mid N\), division by \(N\) gives normalized monotonicity and nothing stronger.

**Own derivation 2 — why reblocking Green–Tao cannot improve the exponent.** For dyadic \(M=2^m\mid 2^n=N\), localization plus Green–Tao gives
\[
a_n\le a_m\ll m^{-c}.
\]
Since \(m\le n\), the smallest right-hand side obtainable from this family is attained at \(m=n\), namely the original \(a_n\ll n^{-c}\). Therefore no choice of interval block size generates an averaged or recursive gain.

**Own derivation 3 — a sufficient cross-scale recurrence.** Assume \(a_n\) is nonincreasing and \(a_{2n}\le q a_n\) eventually with \(q<1/2\). Iterating gives \(a_{2^j n_0}\le q^j a_{n_0}\). Monotonicity then bounds the whole index block:
\[
\sum_{n=2^j n_0}^{2^{j+1}n_0-1}a_n
\le 2^j n_0\,a_{2^j n_0}
\le n_0a_{n_0}(2q)^j.
\]
Because \(2q<1\), the block masses form a geometric series, so \(\sum_n a_n<\infty\). The same proof gives the \((\lambda,q)\) criterion with \(\lambda q<1\).

## Adversarial checks

1. **No hidden gain from monotonicity.** A positive nonincreasing sequence may satisfy \(a_n\ll n^{-c}\) for any fixed \(0<c\le1\) and still have divergent sum; \(a_n=n^{-c}\) is the basic model. Thus monotonicity plus the current exponent cannot close the frontier.

2. **No gain from choosing smaller localization scales.** The bound \(a_n\le C m^{-c}\) becomes weaker as \(m\) is decreased. Reblocking therefore cannot manufacture a stronger exponent.

3. **Internal “recurrence” is not scale recurrence.** The Green–Tao word “recurrence” concerns four-term progression counts for coupled random variables inside one \(\mathbb Z/p\mathbb Z\). Treating it as a recurrence for \(a_n\) would conflate two different variables and is not justified by the theorem.

4. **The contraction criterion is sufficient, not claimed necessary.** Summability may follow from weaker averaged or irregular cross-scale information; the displayed \(q<1/2\) condition is an explicit theorem-grade target showing what kind of genuinely new sequence-level output suffices.

## First defect

The first defect in the proposed extraction route is that the Green–Tao quantitative recurrence theorem does not preserve an uncoupled, interval-uniform family of common differences and does not emit a smaller ambient extremal problem. Its proof iteration is entirely internal to one fixed \(p\), so there is no object from which a nontrivial relation between \(a_n\) and \(a_m\) can be read off.

## Frontier effect

No proof of \(\sum_n a_n<\infty\) is obtained. The attack rules out two apparent low-cost upgrades:

- extracting a cross-scale recurrence directly from the published Green–Tao iteration;
- obtaining one by interval localization/reblocking of the pointwise theorem.

The frontier is sharpened from “seek averaged decay or recurrence” to the requirement for a genuinely new **ambient-scale transfer estimate**. Any future use of the Green–Tao machinery for this purpose must add a theorem that transports quantitative information between different ambient scales, rather than merely re-running the fixed-scale theorem.

## Next residual

Establish or refute an ambient-scale transfer statement that survives extremization, for example a strict normalized contraction between \(r_4(2^{2n})/2^{2n}\) and \(r_4(2^n)/2^n\), or an averaged substitute with summable index-block mass. Evidence from the published proof shows that this transfer is not already present in its fixed-\(p\) energy/dimension-decrement iteration.

## Sources

- Ben Green and Terence Tao, **“New bounds for Szemerédi's theorem, III: A polylogarithmic bound for \(r_4(N)\)”**, arXiv:1705.01703v3 (10 Aug 2017): https://arxiv.org/abs/1705.01703 ; PDF: https://arxiv.org/pdf/1705.01703
- Published version: *Mathematika* 63 (2017), 944–1040, DOI 10.1112/S0025579317000316: https://doi.org/10.1112/S0025579317000316

