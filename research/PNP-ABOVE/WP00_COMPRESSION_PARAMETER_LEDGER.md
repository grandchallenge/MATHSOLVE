# PNP-ABOVE-WP00 — exact three-stage compression parameter ledger

**Disposition:** SOURCE-PINNED SYMBOLIC LEDGER, not executable instantiation, independent proof of the cited results, a new lower bound, or mathematical certification.

**Scope:** Theorem 12.1 and its proof (Figures 15, Table 2, equations (182)–(192)); [parent research issue](https://github.com/grandchallenge/MATHSOLVE/issues/1136); [previous source extraction](https://github.com/grandchallenge/MATHSOLVE/pull/1140), [resource-semantics audit](https://github.com/grandchallenge/MATHSOLVE/pull/1142).

## Source identity and verification method

Z. Ji, A. Natarajan, T. Vidick, J. Wright, H. Yuen, *MIP*=RE*, **arXiv:2001.04383v4**, dated **2026-10-16**: https://arxiv.org/pdf/2001.04383v4 . Inspected typeset PDF pages numbered **54, 184–189**, rather than trusting flattened PDF superscripts. This is an exact version/locus reference, not a byte SHA-256 lock (downloading the source file for hashing was unsuccessful). Equations below transcribe the displayed mathematics on those pages; no numeric values are inferred for existential universal constants.

**Resource convention:** Definition 5.12 (page 54): $\mathcal E(G,\nu)$ is the minimum Schmidt rank of a finite-dimensional tensor-product strategy that achieves win probability at least $\nu$, or infinity if none exists. It is not time, circuit size, or an NP witness bound. Definition 5.11: PCC means projective, consistent and commuting.

## The exact domain of the theorem

Take a verifier $\mathcal V=(S,D)$, a positive integer $\lambda$, an index $n$, and $N=2^n$. The transformation outputs a normal-form 9-level verifier for all inputs. Its **completeness and entanglement-soundness conclusions** require that the *input* $\mathcal V$ already be **9-level normal form** and **$\lambda$-bounded** in the sense of Definition 5.32, and that $n\geq C_0$. Bounds on the sampler and decider of the output do not require those extra input hypotheses. The transformed sampler's description is independent of $\mathcal V$ and depends only on $\lambda$ (Lemma 12.2); this does not construct a winning prover strategy.

## Construction ledger — Figure 15

| Stage | Transformation | Output levels | Sampler time | Decider time | Perfect PCC completeness |
|---|---|---:|---|---|---|
| 1, introspection | ComputeIntroVerifier($\mathcal V,\lambda,9$) | 5 | $\operatorname{poly}(n,\lambda)$ | $\operatorname{poly}(N^\lambda)$ | preserved from $\mathcal V_N$ |
| 2, answer reduction | ComputeAnsRedVerifier($\mathcal V^{(1)},\lambda,\mu,\sigma$) | 7 | $\operatorname{poly}(n,\lambda)$ | $\operatorname{poly}(n,\lambda)$ | preserved from stage 1 |
| 3, anchored repetition | ComputeRepeatedVerifier($\mathcal V^{(2)},\lambda,\tau$) | 9 | $\operatorname{poly}(n,\lambda)$ | $\operatorname{poly}(n,\lambda)$ | preserved from stage 2 |

At stage 3, $k(n)=(\lambda n)^\tau$ repetitions. Stages invoke Theorems 8.3, 10.30, and 11.4, respectively; their combination yields Theorem 12.1. See Figure 15/Table 2 on PDF pages 185–186. Do **not** confuse a verifier with a family of explicitly expanded game tables.

## Symbols and universal parameters

Let $a_1,a_2>0$, $0<b_1,b_2<1$, and $C_{\rm INTRO}\geq2$ be the universal constants referred to in the proof. They are not numerically fixed in Theorem 12.1.

**Introspection, equations (182)–(184):** For every $\lambda\geq1$, $n\geq2$,

$$
\operatorname{TIME}_{S^{(1)}}(n)\leq(\lambda n)^{C_{\rm INTRO}},\qquad
\operatorname{TIME}_{D^{(1)}}(n)\leq 2^{C_{\rm INTRO}\lambda n},\qquad
|D^{(1)}|\leq C_{\rm INTRO}\lambda^{C_{\rm INTRO}}.
$$

Define

$$
\delta_1(\epsilon_1,n)
=a_1\left((\lambda n)^{a_1}\epsilon_1^{b_1}+(\lambda n)^{-b_1}\right).
$$

$$
\epsilon_1=\left(\frac{1}{8a_1(\lambda n)^{a_1}}\right)^{1/b_1},
\qquad C_1=(4a_1)^{1/b_1}.
$$

The first summand of $\delta_1$ is exactly $1/8$. For $n\geq C_1$ and $\lambda\geq1$, the other is at most $1/4$, hence $\delta_1\leq3/8<1/2$ (the proof uses the looser $<1/2$). The first stage therefore preserves the lower bound at threshold $1-\epsilon_1$ in Table 2.

**Answer reduction, equations (185)–(189):** With universal $C_{\rm INTRO}$ from above,

$$
\sigma=\left\lceil C_{\rm INTRO}\lambda^{C_{\rm INTRO}}\right\rceil,
\qquad
\mu=\left\lceil\max\left\{C_{\rm INTRO},
\frac{9a_1+2a_2C_{\rm INTRO}}{b_1b_2}\right\}\right\rceil.
$$

$$
\delta_2(\epsilon_2,n)=
\sigma^{a_2}\left((\lambda n)^{a_2\mu}\epsilon_2^{b_2}
+(\lambda n)^{-b_2\mu}\right).
$$

$$
\epsilon_2=
\left(\frac{\epsilon_1}
{3\sigma^{a_2}(\lambda n)^{a_2\mu}}\right)^{1/b_2}.
$$

The first term of $\delta_2$ is exactly $\epsilon_1/3$. The choice of $\mu$ controls the second term strictly below $\epsilon_1/2$, for $n\geq2$ and $\lambda\geq1$, so $\delta_2<5\epsilon_1/6<\epsilon_1$. The answer-reduced verifier has timeout bound and sampler dimension controlled by

$$
\max\{\operatorname{TIME}_{S^{(2)}}(n),
\operatorname{TIME}_{D^{(2)}}(n),B_{D^{(2)}}(n)\}
\leq(\lambda n)^{C_2},\qquad
s_{S^{(2)}}(n)\leq B_{D^{(2)}}(n),
$$

where $C_2$ is universal and $n\geq C_2$. These bounds derive from Theorem 10.30, not from an asserted polynomial bound on quantum provers.

**Parallel repetition, equation (190):** Let $c_3,c'_3>0$ denote universal constants from Theorem 11.4, and $C_{\rm AR}$ its answer-reduction prerequisite constant. Choose $\tau$ to be the *least integer* satisfying $\tau\geq\max\{C_{\rm AR},C_2\}$ and, for all $n\geq\tau$ and all integers $\lambda\geq1$,

$$
\frac{4}{\epsilon_2}
\exp\left(-c_3\epsilon_2^{17}
\frac{(\lambda n)^\tau}
{\big(c'_3(\lambda n)^{C_2}\big)^{c'_3}}\right)
<\frac12.
$$

The source establishes the existence of such a **universal** $\tau$ because $\epsilon_2^{-1}$ grows as a fixed polynomial in $\lambda n$ and the negative exponent can overpower it by raising $\tau$. This is not a numerical algorithm for $\tau$ without the earlier constants. The repetition theorem gives $\mathcal E(\mathcal V^{(3)}_n,1/2)\geq\mathcal E(\mathcal V^{(2)}_n,1-\epsilon_2)$ and $s_{S^{(3)}}(n)\leq B_{D^{(3)}}(n)$.

**Global threshold, equation (192):**

$$
C_0=\max\{C_1,C_2,C_{\rm AR},\tau\}.
$$

All conclusions below apply for $n\geq C_0$ under the input normal-form and boundedness hypotheses. When implementing, additionally take $n\geq2$ for unambiguous alignment with the stated intermediate estimates.

## Quantitative entanglement inequality (Theorem 12.1, source discrepancy)

**Corrected source audit, 2026-11-01:** The **printed statement** of Theorem 12.1 on page 184 says

$
\mathcal E(\mathcal V_n^{\rm COMPR},1/2)
\geq \max\left\{
\frac12\mathcal E(\mathcal V_N,1/2),\,
2^{N^\lambda-1}
\right\},\qquad N=2^n.
$

But Table 2 (printed page 186) and the **final proof chain** on page 189 imply only

$
\mathcal E(\mathcal V_n^{\rm COMPR},1/2)
\geq \frac12\max\left\{
\mathcal E(\mathcal V_N,1/2),\,
2^{N^\lambda-1}
\right\}.
$

The previous edition labelled this weaker proof-supported inequality an *exact theorem transcription*. That was incorrect. Conversely, the stronger second branch in the printed theorem is not justified by the displayed final chain without an additional argument. This is a source-semantic reconciliation obligation, not a conclusion that the paper's other results fail. The following **conservative**, proof-supported implication remains correct without assuming the stronger printed bound or any classical cost bound:

$$
\mathcal E(\mathcal V_n^{\rm COMPR},1/2)
\geq 2^{2^{\lambda n}-2}.
$$

For the conservative bound, the logarithmic Schmidt-rank consequence is $\log_2\mathcal E\geq2^{\lambda n}-2$. Its resource semantics are exclusively entangled-strategy size.

**Derivation from Table 2 (conditional on cited theorems):**

$$
\begin{aligned}
\mathcal E(\mathcal V^{(3)}_n,1/2)
&\geq\mathcal E(\mathcal V^{(2)}_n,1-\epsilon_2)\\
&\geq\tfrac12\mathcal E(\mathcal V^{(1)}_n,1-\epsilon_1)\\
&\geq\tfrac12\max\{\mathcal E(\mathcal V_N,1/2),2^{N^\lambda-1}\}.
\end{aligned}
$$

This algebraic chaining is checked, but the three underlying transformation theorems have **not** been independently proved here. Local symbolic checks of the leading error terms agree with the substitutions: $a_1(\lambda n)^{a_1}\epsilon_1^{b_1}=1/8$ and $\sigma^{a_2}(\lambda n)^{a_2\mu}\epsilon_2^{b_2}=\epsilon_1/3$.

## Constructivity and nontransfer boundaries

The paper supplies a polynomial-time Turing-machine **constructor** for the verifier description. It does not give a small numerical value of $C_0$ or explicit machine code and universal constants suitable for certifying a chosen modest $n$. Consequently, an actual finite compressed game cannot be claimed executed from this ledger alone.

It is false to infer from the very large lower bound on $\mathcal E$ that evaluating a game's accept/reject predicate, deciding SAT, or constructing a small classical circuit is equally difficult. The remaining prospective transfer must define one explicit uniform classical decision or strategy-construction problem and show exactly how a hypothetical polynomial-time SAT decider would produce a *low-Schmidt-rank tensor-product winning strategy*, if indeed that is the resource chosen. Such an implication is absent from the theorem and may be false.

## Gate result / next action

**Completed:** full symbolic stages, source equation references, threshold/cost bookkeeping, error substitutions, quantified $\tau$ obligation, and exact entanglement-bound transcription. **Open:** numerical source constants, source byte hash, an explicit compliant input verifier with machine encoding, an executable finite instance, and any SAT-to-classical-cost transfer theorem. **Next genuine mathematical work:** choose an explicitly encoded 9-level $\lambda$-bounded input verifier and assess which machine/timeout conditions can be witnessed constructively without relying on unnamed universal constants. Alternatively prove a restricted no-transfer counterexample with an exact classical strategy cost measure.

Claim status of PNP-001 unchanged; no new circuit or time lower bound, no P vs NP separation, no novelty or certification claim.
