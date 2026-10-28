# PR890 collision-safe mathematical review packet (source Q10–Q15)

Source: grandchallenge/MATHSOLVE PR #890, head e89a67a1cdf3af585bce84a7738976e4ec6898fd.
Baseline: protected main 7507b802e4d92d45b681687f833c00c13c128fab.

**UNADMITTED RESEARCH CANDIDATES; NOT PROTECTED RESULTS.**

The old branch reuses IDs E3-Q10..E3-Q15 for different claims than
protected main. The source documents are preserved verbatim here, outside
authoritative result paths; source numbering is historical only.

Before promotion: independently verify all mathematical proofs; allocate
noncolliding permanent IDs and correct internal cross-references; reconcile
current frontier nodes and statuses; register campaign and CI bindings;
obtain distinct authorized review and protected merge/readback.

No E3-Q4 theorem, V03 verification, or gluing-radius state is promoted.
Source Q16 is separated into its own review PR.

## Bounded mathematical verification — historical source-Q15 (2026-10-28)

Checked the *self-contained cardinality sublemma*, not the wider source-Q15 or source-Q14 theorem. With `N=2^n`, `n>=1`, and `c_t=floor((u+t v)/N)` for `0<=u,v<N`, each point has precisely one carry vector, and the possible vectors are `0000, 0001, 0011, 0012, 0111, 0112, 0122, 0123`. The `0000` count is the finite arithmetic sum of `N-3v` over `0<=v< N/3`. Reflection gives the `0123` count by subtracting the `N` boundary-strip points. The `0001` count equals `A_2(N)-|Omega_0000|` with `A_2(N)=(N^2+2N)/4`. The two explicitly specified invertible transformations `R_rev(u,v)=((u+3v) mod N,(-v) mod N)` and `R_neg(u,v)=((N-1-u) mod N,(-v) mod N)` map the four `1/12`-type cells within their symmetry class and the two `1/6`-type cells within theirs. The partition then determines the final class.

Exact formulas reviewed: `|Omega_0000|=(N^2+3N+2)/6`, `|Omega_0123|=(N^2-3N+2)/6`, four cells `0001,0012,0111,0122` each `(N^2-4)/12`, and `0011,0112` each `(N^2+2)/6`. Independent direct enumeration of all `N^2` pairs at dyadic `N=2,4,8,16,32,64` matches every count, including zero-population cells at `N=2`. For `N>=16`, the six L01 core carries have density at least `21/256` (minimum at `N=16`) and less than `1/4`; the eight-cell partition and the corresponding zero-sum intrinsic fluctuation relation are therefore supported at this bounded level.

**Excluded from this verification:** the historical Q15 `7 beta^4/1280` correlation amplification, historical Q14 Fourier normalization and source-to-protected Q02/Q12 dependencies, and the complete Q16 trichotomy. The identifiers source-Q14/source-Q15 remain *unadmitted* PR890 candidates; protected E3-Q14/E3-Q15 are different results. No parent Erdős-3 claim or new live frontier entry is promoted. A distinct material critic pass and source-level admission reconciliation remain necessary.

## Historical source-Q14 Fourier identity — bounded independent check (2026-10-28)

For `G=Z/PZ` with prime `P`, normalized Fourier convention `hat f(xi)=E_G f(x)e_P(-xi x)` and `hat K(a,b)=E_{G²}K(u,v)e_P(-au-bv)`, Fourier inversion of each centered, zero-extended fibre factor `H_t(u+t v-c_t N)` gives the source-Q14 exact formula with phase `e_P(-N sum_t c_t xi_t)` and kernel argument `(-sum_t xi_t,-sum_t t xi_t)`. The `P²/N²` scale factor follows directly from converting the kernel-restricted sum from prime-group normalization to the original `N²` denominator. Since distinct time indices differ by at most three and `P>3`, the unrestricted prime-group singleton and pair correlations vanish by the zero-frequency constraints; the three-factor unrestricted constraint leaves one free frequency. This establishes the algebraic harmonic identity **conditional on** the stated exact carry cell and Q12 definitions; it is not a verification of the upstream Q12 witness inequality.

Independent finite numerical diagnostic: for `N=4`, `P=37`, carry `0001`, bounded centered binary fibre arrays, direct `G²` kernel correlation and the fully summed discrete Fourier representation match for `S={0,2}` (absolute discrepancy ~`3.1e-20`) and `S={0,1,3}` (zero at printed precision). The test uses normalized NumPy FFTs, exact integer carry enumeration, and the source formula's translation phase. This checks normalization/phase on a bounded instance, not the general theorem by computation.

**Remaining unverified dependencies:** the Q12 localized-correlation lower bound, its historical source-Q15 sharpening to `7 beta^4/1280`, consistency of the D01 indexed fibre occurrences with the protected definition, and any claim of full theorem-level certification. The source-Q14 and source-Q15 labels remain historical, unadmitted identifiers conflicting with protected E3-Q14/E3-Q15. No live frontier promotion.

## Source-Q15 sharpened cancellation constant — exact conditional verification (2026-10-28)

Let `N>=16` be dyadic, `Omega_c(N)` one of the six L01 core carry cells, `alpha_t=|B_{j_t}|/N >= beta>0`, and suppose the four labelled physical fibres form a globally 4-AP-free glued set. Each `(u,v)` in `Omega_c` determines one ordinary glued integer progression with `j_t=i+tq+c_t` and residue `u+t v-c_t N`. Therefore the exact localized indicator product vanishes pointwise, and its `N^{-2}` sum is zero. Write `1_{B_{j_t}}=alpha_t+h_t`; expansion yields precisely `2^4-1=15` nonempty terms `T_{F,S}^{loc}` and positive baseline `W_F^{loc}=|Omega_c|/N^2 prod_t alpha_t`. The independently checked historical source-Q15 cardinalities imply `W_F^{loc} >= (21/256) beta^4`. By the triangle inequality, `max_{S nonempty}|T_{F,S}^{loc}| >= W_F^{loc}/15 >= (21/(15*256)) beta^4 = (7/1280) beta^4`. This is an *exact conditional lemma*, with no use of the Fourier formulation. Compared with the historical Q12 baseline `beta^4/3840`, the improvement factor is 21. The density minimum is realized at `N=16` by each `1/12`-type core carry. Direct independent Python enumeration of all `N^2` pairs verified the minimum densities at `N=16,32,64,128` (`21/256`, `85/1024`, `341/4096`, `1365/16384` respectively).

**Scope and caution:** The calculation validates the inference assuming the stated source-Q12 gluing/zero-count premise, six-core membership, and beta-density hypotheses. It does not independently establish global glued 4-AP-freeness, identify admissible families in a particular Erdős-3 instance, justify the stronger historical Q13 prefix/suffix conclusion, or prove a parent deficit theorem. Source-Q12 and source-Q15 remain unadmitted historical PR890 candidates; do not cite them as protected E3-Q12/E3-Q15. The algebraic constant may inform internal adjudication after source hypotheses are independently checked.

## Adversarial correction: zero-step diagonal in historical source-Q12 (2026-10-28)

The historical source-Q12 assertion that *every* carry-cell point generates a forbidden 4-AP needs a nonzero-step qualification. For `F=(i,q,c)`, its four glued integer positions are `N(i+t q+c_t)+(u+t v-c_t N)=Ni+u+t(qN+v)`, with common difference `d=qN+v`. Assuming the nonnegative `q` used in the historical L01 family convention and `0<=v<N`, the only possibility `d=0` is `q=0,v=0`, when necessarily `c=0000`. This is the trivial fourfold diagonal; ordinary 4-AP-free sets do NOT exclude it. Its contribution to the localized product, if the family `F=(i,0,0000)` is included, is `|B_i|/N^2=alpha_i/N` rather than zero. All families with nonzero `d` have zero localized product under the claimed globally nontrivial-4-AP-free gluing premise.

Thus, for a generic family the exact expansion must be written `D_F = W_F^{loc} + sum_{S != empty} T_{F,S}^{loc}` with `D_F=0` for nonzero-step families, or `D_F=alpha_i/N` for the potential `q=0,c=0000` diagonal case. The universally justified inequality is `max_S |T_{F,S}^{loc}| >= |W_F^{loc}-D_F|/15`; the sharp `(7/1280) beta^4` lower bound follows unchanged only when `D_F=0` (or under an independently proved adequate lower bound on `W_F-D_F`). It is not established as a uniform statement over families including an unexcluded diagonal. Check the exact protected E3-L01 family registry before any blanket claim. In the zero-step case the correction has order `1/N` and must be carried explicitly, not silently dropped.

**Review disposition:** this supersedes the earlier README paragraph's unconditional sentence that the localized indicator product vanishes pointwise for every family. The old proposal documents remain verbatim for source provenance. No proof admission or frontier promotion is licensed until the L01 family membership and diagonal handling are reconciled.

## Exact protected L01 family-table resolution (2026-10-28)

Read back protected `work_packages/GCL_ERDOS3/results/E3-L01_NATIVE_RESULT.md`, family table and minimum ten-family certificate. The ten core families are `F1,F2,F3,F4,F6,F7,F9,F10,F15,F16`. The sole `0000` core family is `F16=(0,1,0000)` (not `q=0`); `F15=(0,0,0123)` has nonzero carry, and all other `q=0` core carries are nonzero. Therefore `d=qN+v` cannot vanish on any of these ten exact carry cells: for `q=1`, `d>=N`; for `q=0`, `v=0` would force all carries `0000`, which none of those eight other families have. Hence `D_F=0` for every member of the **specified L01 ten-family core** when the glued set is nontrivial-4-AP-free. The exact Q12 cancellation formula and its conditional `7 beta^4/1280` sharpening are valid on that core, notwithstanding the diagonal defect for a hypothetical non-core `(i,0,0000)` family. The preceding adversarial warning applies only if claims are generalized beyond the listed core.

This is a source-grounded resolution of the zero-step obligation, **not** certification of other historical source-Q12–Q16 dependencies and not an assertion that the finite N=7 certificate independently proves an asymptotic four-fibre deficit.
