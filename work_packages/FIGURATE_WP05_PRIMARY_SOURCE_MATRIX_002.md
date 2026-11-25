# FIGURATE-WP05 — theorem and proof-dependency register, revision 002

**Record date:** 2026-11-03. **Authority:** MATH-PROGRAMME #3093 / WP05 #3096.
**Status:** primary-source reconstruction substantially advanced; **not** independent proof certification.
**Evidence discipline:** distinguish inspected primary full text (P), publisher/author abstract (A), and an accessible *third-party reproduction* of primary text (R). Never treat R as the primary edition or treat an inaccessible proof as checked.

## Exact statements and proof dependencies

| Source | Access tier | Theorem / condition | Actual scope | Argument and dependency notes |
| --- | --- | --- | --- | --- |
| Filipin–Szalay, *Triangular Diophantine tuples from {1,2}*, Rad HAZU 27 (2023), pp.55–70, [journal-hosted PDF](https://hrcak.srce.hr/en/file/443905), DOI 10.21857/ygjwrcp48y | **P: full original journal PDF inspected** | Definition 1.2: distinct positive integers with all pair products +1 triangular. Theorem 1.3: no triangular Diophantine quadruple **containing both 1 and 2**. | Type B, polygonal order 3, offset +1, prescribed pair. **Not** global absence of Type B triangular quadruples. | Lemma 2.1 handles {1,2,27}; equations (2.1)–(2.4) reduce extension to Pell-like constraints. Proof uses generated sequence of possible third entries, simultaneous Pell recurrences, elliptic-curve integral-point computations, logarithmic-form bounds, Baker–Davenport reduction and Magma computations. Proposition 6.2 excludes sufficiently large sequence-index extensions (k>27 in paper's recurrence notation), not all triples. The paper reports an explicit quadruple {14,31,135,3510} in its introduction. |
| Filipin–Jurasić–Szalay, *Extensions of the triangular D(3)-pair {3,6}*, Math. Slovaca 75(4) (2025), pp.775–790, DOI 10.1515/ms-2025-0057, [author/institution record](https://www.croris.hr/crosbi/publikacija/prilog-casopis/878863) | **A: publisher/institution abstract, original complete proof not retrieved** | No four distinct positive integers {3,6,c,d} with all pair products +3 triangular. | Type B, order 3, offset +3, prescribed pair. | Abstract advertises simultaneous Pellian equations and linear forms in logarithms. Theorem numbers and lemma dependencies **unverified**. |
| Filipin–Jurasić–Togbé, *A note on the extension of some triangular Diophantine sets*, An. St. Univ. Ovidius Constanţa 34(2) (2026), pp.29–43, DOI 10.2478/auom-2026-0018, [publisher record](https://reference-global.com/article/10.2478/auom-2026-0018) | **A plus R:** publisher abstract independently matched to accessible third-party transcription [here](https://www.scribd.com/document/1068711764/A-Note-on-the-Extension-of-Some-Triangular-Diophan); original publisher PDF not retrieved | Transcription identifies Theorem 1.1: no triangular D(k) quadruple of form {k,2k,c,d} for **k=10 or 28**. Here k is additive offset (FIGURATE uses k for polygonal order). | Type B, order 3, offsets 10 and 28, specified pair. It does not prove nonextension for all offsets. | Transcription identifies Lemma 4.1 (linear form bound), Lemma 5.2 (lower bound on recurrence index), Theorem 6.1 (Baker–Wüstholz linear forms), Proposition 6.2 (nonextension if c>=1.57e43), and a final Pari/GP Baker–Davenport reduction of the finite remainder. **These dependencies are provisional until checked against publisher PDF and original computational evidence.** |
| Bagchi–Zhou-Zheng, *Diophantine m-tuples of Triangular Numbers*, [arXiv:2608.27697v1](https://arxiv.org/abs/2608.27697), posted 2026-08-27 | **A:** arXiv author abstract only; full manuscript unavailable in this audit | No all-triangular D(1) classical quadruple; infinite constructed family of all-triangular D(1) triples, **conjectured** complete; no all-triangular D(n) pair for n congruent to 2 or 5 mod 9. | Type A (triangular entries, square outputs), not Type B. Variable-n exclusions concern Type A only. | Abstract also claims generalized-Pell pair test O(sqrt(a)) and local solutions over Q_p except p=3. Exact theorem numbers, hypotheses, complexity conventions and proof dependencies not checked. |
| Radić, *On some D(u²)-triples and quadruples of triangular numbers*, [arXiv:2609.28018v1](https://arxiv.org/abs/2609.28018), posted 2026-09-23 | **A:** arXiv author abstract only; full manuscript unavailable in this audit | Classifies all all-triangular D(u²) triples with least member T_(4u-1) or T_(4u); proves infinitely many positive u admit all-triangular D(u²) quadruples. | Type A with varying square offset u²; compatible with D(1) quadruple nonexistence. | Exact parameterized constructions, dependence on regularity and theorem numbering uninspected. |

## Critical counterexample against false global Type B quadruple claims

The original 2023 paper explicitly exhibits the **Type B triangular-output, offset +1 quadruple**

    {14, 31, 135, 3510}.

Its six pairwise shifted products are 435, 1891, 49141, 4186, 108811 and 473851, equal respectively to triangular numbers at indices 29, 61, 313, 91, 466 and 973. Hence **Type B triangular-output quadruples exist**, even though Type B quadruples *containing {1,2}* are ruled out. The small FIGURATE L60 archive finds none at offset +1 because its **maximum entry is 60**, not because of global nonexistence.

The original paper also cites the triple {1,2,27} and shows its nonextension (Lemma 2.1), invoking computational resolution of a simultaneous Pell system in Magma. Replaying Magma and integral-point computations is a separate mathematical-verification task, not something established by reading the paper.

## Logical novelty exclusions

- Do **not** pursue global nonexistence of Type A all-triangular D(1) quadruples as an original finding (Bagchi–Zhou-Zheng).
- Do **not** transfer that result to Type B: the above {14,31,135,3510} quadruple refutes such a transfer.
- Do **not** assert that Type B pairs can be eliminated for all unrestricted entries at a fixed polygonal order and offset: constructive pairs {1,P_k(t)-c} exist for all k>=3 and integer c, at sufficiently large t (FIGURATE WP05 checkpoint 001).
- Do **not** propose the known nonextensions of Type B prescribed pairs {1,2} at offset 1, {3,6} at offset 3, or {10,20}/{28,56} at corresponding offsets as original results.
- Do **not** confuse Type A D(u²) existence for variable u with the fixed D(1) nonexistence.
- **Viable focus:** higher polygonal orders, specific extension phenomena outside known pairs, Type C, and rigorously safe congruence sieves.

## Evidence and acceptance ledger

| Required WP05 item | Evidence available | State |
| --- | --- | --- |
| Exact family taxonomy | definitions A/B/C and offset distinction | DONE |
| Primary full-paper theorem reconstruction for 2023 Type B | original PDF, theorem 1.3, lemma 2.1, proposition 6.2 and proof outline | DONE AT SOURCE-READING LEVEL |
| 2025 prescribed pair full-paper dependency reconstruction | abstract only | OPEN: full primary text |
| 2026 publisher article full-paper dependency reconstruction | publisher abstract; third-party transcription with numbered results | OPEN: verify publisher original + computational appendix |
| 2026 arXiv Type A proof reconstruction | abstracts only | OPEN: obtain full manuscripts and extract exact numbered theorems |
| Mathematical certification of cited proofs | source-reading does not replay cited computer calculations | NOT REQUESTED AS WP05; independent math review if reused in a claim |
| Novelty exclusions / next theorem targets | explicit list above | DONE AT DOCUMENTARY LEVEL |

**Disposition:** Do not mark WP05 fully closed while the three 2026/2025 original manuscript dependencies remain inaccessible. Completion requires original full-source access or a governed adjustment of the gate, **not** representation of abstracts as complete proofs.

**Sources:** [2023 journal PDF](https://hrcak.srce.hr/en/file/443905), [2025 author/institution record](https://www.croris.hr/crosbi/publikacija/prilog-casopis/878863), [2026 publisher abstract](https://reference-global.com/article/10.2478/auom-2026-0018), [2026 third-party reproduction](https://www.scribd.com/document/1068711764/A-Note-on-the-Extension-of-Some-Triangular-Diophan), [2026 arXiv first](https://arxiv.org/abs/2608.27697), [2026 arXiv second](https://arxiv.org/abs/2609.28018).

