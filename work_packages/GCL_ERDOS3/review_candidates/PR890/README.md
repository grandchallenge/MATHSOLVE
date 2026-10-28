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
