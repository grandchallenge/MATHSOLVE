# PNP-ABOVE WP06 — Source-parameter erasure and the SAT transfer boundary

**Classification:** mathematical source deduction with explicit hypotheses, source-pinned to the **upstream code**. No new unrestricted complexity lower bound, no full compression execution, no SAT-to-quantum transfer, and no independent mathematical certification.

**Research parent:** [PNP-ABOVE](https://github.com/grandchallenge/MATHSOLVE/issues/1136). **Upstream lock:** [vidick/MIPRE-formalization at commit 5926bdff5db621f44682a101007ef2fe3ae8d970](https://github.com/vidick/MIPRE-formalization/tree/5926bdff5db621f44682a101007ef2fe3ae8d970). Source files: [DecisionCompiler.lean](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/MIPRE/Background/Introspection/DecisionCompiler.lean) and [SourceDescriptionCompiler.lean](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/MIPRE/Foundations/Introspection/SourceDescriptionCompiler.lean).

## 1. Zero-parameter decider erasure: exact source consequence

For every fixed compiler parameter $c$, clocked universal machine $U$, and input source programs $S,D$, the upstream theorem \`DecisionCompiler.compute_apply\` gives

$$
\mathrm{compute}(c,U,((S,D),0))=\mathrm{zeroProg}.
$$

The result is **syntactically the same program** for all source inputs. This follows by substituting $\lambda=0$ into the upstream displayed equality and selecting its first conditional branch. It is stronger than merely saying that two test inputs behaved alike.

The upstream theorem \`DecisionCompiler.accepts_zero\` supplies an exact interpretation for the compiled **decider**:

$$
\mathrm{Accepts}(c,U,S,D;0,n,x,y,a,b)\quad\Longleftrightarrow\quad
(x=[]) \land (y=[]) \land (|a|\leq2) \land (|b|\leq2).
$$

This predicate is independent of $S,D$, of $n$, and of $c,U$. It is a zero-resource special case, **not** a general SAT instance decision procedure.

**Scope discipline:** these statements concern the \`DecisionCompiler\` decider. They do not alone prove that an entire game's sampler, probability distribution, or quantum winning value is source-independent. This prevents an incorrect extrapolation from the decider to all of \`MIP*=RE\`.

## 2. Overbudget source-description erasure

The upstream \`SourceDescriptionCompiler.clampProgram_apply\` gives the exact source rule

$$
\mathrm{clampProgram}(p,\lambda)=
\begin{cases}
p,&\mathrm{esize}(p)\leq\lambda,\\
\mathrm{Prog.nil},&\mathrm{esize}(p)>\lambda.
\end{cases}
$$

The compiler independently clamps the sampler program $S$ and decider program $D$. Therefore, for any two source pairs $(S_1,D_1)$ and $(S_2,D_2)$ for which **all four** encoded source-program sizes strictly exceed the common $\lambda$,

$$
\mathrm{clamp}((S_1,D_1),\lambda)
=\big((\mathrm{nil},\mathrm{nil}),\lambda\big)
=\mathrm{clamp}((S_2,D_2),\lambda).
$$

The published \`DecisionCompiler.compute_apply\` factors its positive-parameter branch through this clamped input. Consequently, for fixed $c,U,\lambda$,

$$
\boxed{\mathrm{compute}(c,U,((S_1,D_1),\lambda))
=\mathrm{compute}(c,U,((S_2,D_2),\lambda))}
$$

under those four oversize hypotheses. The equality also holds when $\lambda=0$, independently of the oversize hypotheses, by the zero branch.

**Proof:** the two source descriptions are transformed into the identical clamped metadata object; \`positiveCompiler\`, \`zeroWrap\` and the conditional branch are deterministic mathematical functions of the same parameters and metadata. Equal inputs produce equal outputs. QED.

## 3. Why this is a transfer-theorem constraint rather than a P vs NP lower bound

Suppose an attempted SAT-to-compressed-decider reduction maps two semantically different source-verifier descriptions to inputs in this overbudget class, with the same $c,U,\lambda$. Their **compiled decider programs are identical**, so a decision procedure whose only distinguishing information is this program cannot recover which source problem was encoded. This is a concrete *non-injectivity barrier for an undersized parameter*.

This does **not** imply that all valid compressions fail: the upstream formalization explicitly assumes verifier size/encoding bounds. For sufficiently large $\lambda$, the upstream \`clamp_eq_self\` guarantees preservation of the descriptions, and the conditional compression theorem is unaffected. Nor does non-injectivity by itself establish a classical time lower bound or $\mathsf{P}\neq\mathsf{NP}$.

**Necessary hygiene for a faithful compiler-based transfer:** supply a source-dependent parameter $\lambda$ satisfying both $\mathrm{esize}(S)\leq\lambda$ and $\mathrm{esize}(D)\leq\lambda$ whenever the reduction's correctness relies on preserving those original program descriptions. The existence of semantically equivalent clamped programs is not excluded by the argument; this is a sufficient preservation condition and a restriction on universal source-faithfulness claims, not a claim that every oversized input is erroneous.

The earlier [WP01 explicitly tabulated classical-game SAT transfer](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/PNP-ABOVE/WP01_EXPLICIT_CLASSICAL_TRANSFER_AND_SOURCE_AUDIT.md) remains true and separate. Its cost is polynomial in the explicit game table, not automatically in the succinct compressed verifier's description.

## 4. Evidence and remaining work

The two source definitions and their theorems were inspected at exactly the pinned upstream commit. The WP05 full Lean build of \`MIPRE.Background.Introspection.DecisionCompiler\` and imported-native-program replay **have passed**, per [WP05 receipt](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/PNP-ABOVE/WP05_UPSTREAM_BUILD_AND_NATIVE_REPLAY_RECEIPT.md). Building that upstream module does *not* mean the new WP06 corollaries were themselves checked.

Companion [WP06_ParameterErasureCandidate.lean](WP06_ParameterErasureCandidate.lean) gives candidate formal statements using the actual imported Lean types and upstream theorems. **Its local proof elaboration has not yet been executed.** The source deduction above is elementary and warrants further Lean replay; it does not receive the label kernel-verified from this record.

The GCL CONTROL command transport returned a safety-check rejection even on a simple diagnostic command during WP06. The failed action was **CHAD local shell execution**, not GitHub read or the source mathematics; no policy or authority gate was overridden. The same work can continue independently under protected GitHub source and documentary governance. Before marking the Lean corollaries proved in GCL, replay the exact WP06 source on the pinned toolchain and read the complete Lean exit status.

**Next obligations:** (1) kernel-check these two Lean corollaries; (2) compile a bounded source-verifier pair with its actual \`Prog\` representation and computed \`esize\`; (3) execute and inspect the positive-\(\lambda\) \`DecisionCompiler.compute\` output with effective source constants and strict source-size checks; (4) only then pursue a nontrivial **succinct** classical invariant and SAT transfer. The full Figure 15 compressor is still not implemented here.
