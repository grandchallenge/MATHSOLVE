# E3-Q07 — finite linear-phase algebra is not the missing incompatibility

Disposition: **PROVED_NATIVE_FINITE_PHASE_ALGEBRA_INSUFFICIENT**.

This is native GCL work. It composes the protected L01 ten-family core with the strengthened Q04 aligned Fourier witness and Q05 Parseval capacity bound. It does not assert existence of actual near-extremal fibres realizing the abstract Fourier data.

## Strongest exact statement

Let
\[
K=\{F_1,F_2,F_3,F_4,F_6,F_7,F_9,F_{10},F_{15},F_{16}\}
\]
be the exact ten-family E3-L01 core.

Fix a nonzero frequency parameter
\[
r\in\mathbb Z/P\mathbb Z,
\qquad P>3,
\]
so that \(r,2r,3r\) are nonzero and distinct.  For each physical fibre
\[
j\in\{0,1,2,3\}
\]
and harmonic
\[
k\in\{1,2,3\},
\]
write
\[
\theta_{j,k}:=\arg \widehat g_j(kr).
\]
Because the physical balanced indicators are real-valued,
\[
\arg \widehat g_j(-kr)=-\theta_{j,k}
\quad(\bmod 2\pi),
\]
so these twelve variables already encode the conjugate-symmetry constraint.

For each family in \(K\), choose the following Q04 triple branch:

| family | chosen labelled positions |
|---|---|
| \(F_1\) | \(\{0,1,2\}\) |
| \(F_2\) | \(\{0,1,2\}\) |
| \(F_3\) | \(\{0,1,2\}\) |
| \(F_4\) | \(\{0,1,2\}\) |
| \(F_6\) | \(\{0,1,2\}\) |
| \(F_7\) | \(\{0,2,3\}\) |
| \(F_9\) | \(\{0,1,3\}\) |
| \(F_{10}\) | \(\{0,1,3\}\) |
| \(F_{15}\) | \(\{0,1,3\}\) |
| \(F_{16}\) | \(\{0,2,3\}\) |

For a triple \(t_1<t_2<t_3\), Q04's exact Fourier multipliers are
\[
(t_2-t_3)r,\qquad
(t_3-t_1)r,\qquad
(t_1-t_2)r.
\]

The carry translations
\[
C_t=c_tN+B_{j_t}
\]
contribute a known phase offset to each triple product.  Therefore asking that the selected triple product have any prescribed phase, in particular the negative phase required by a signed cancellation argument, gives one affine linear equation in the twelve variables \(\theta_{j,k}\).

Let
\[
A:\mathbb R^{12}\to\mathbb R^{10}
\]
be the resulting coefficient map, in family order
\[
(F_1,F_2,F_3,F_4,F_6,F_7,F_9,F_{10},F_{15},F_{16})
\]
and variable order
\[
(\theta_{0,1},\theta_{0,2},\theta_{0,3},
\theta_{1,1},\theta_{1,2},\theta_{1,3},
\theta_{2,1},\theta_{2,2},\theta_{2,3},
\theta_{3,1},\theta_{3,2},\theta_{3,3}).
\]

The exact matrix rows are
\[
\begin{pmatrix}
-1& 1&0&-1&0&0&0&0&0&0&0&0\\
-1& 0&0&-1&1&0&0&0&0&0&0&0\\
 0& 0&0&-2&1&0&0&0&0&0&0&0\\
 0& 0&0&-1&1&0&-1&0&0&0&0&0\\
 0& 0&0& 0&0&0&-2&1&0&0&0&0\\
 0& 0&0& 0&0&0&-1&0&0&0&-1&1\\
 0&-1&0& 0&0&1&-1&0&0&0&0&0\\
 0& 0&0& 0&-1&0&0&0&1&-1&0&0\\
 0&-1&0& 0&0&1&0&0&0&-1&0&0\\
-1& 0&0& 0&0&0&0&0&1&0&-1&0
\end{pmatrix}.
\]

Take the ten columns
\[
(\theta_{0,1},\theta_{0,2},
\theta_{1,1},\theta_{1,2},\theta_{1,3},
\theta_{2,1},\theta_{2,2},\theta_{2,3},
\theta_{3,1},\theta_{3,2}).
\]
The corresponding \(10\times10\) minor has exact determinant
\[
\boxed{-3}.
\]

Hence
\[
\operatorname{rank}A=10.
\]

Therefore \(A\) is surjective.  In particular:

> **For every vector of carry-translation phase offsets and every prescribed phase for the ten selected Q04 triple products, there is a simultaneous assignment of the twelve physical-fibre harmonic phases that realizes all ten affine phase equations.**

This remains true for the exact negative phases that a strengthened signed Q04 extraction could require.

Thus the finite ten-family system has **no abstract one-scale phase-algebra contradiction**.

## Why this is stronger than Q05

Q05 proved that the support/magnitude requirements of finitely many Q04 linear witnesses are compatible with Parseval: the abstract spectra
\[
S_j=\{\pm r,\pm2r,\pm3r\}
\]
already contain all harmonic modes needed by the adjacent witness clauses, and the Q04 threshold
\[
\lambda_\beta=\frac{\beta^3}{20\cdot16^3}
\]
is far below the finite Parseval capacity.

Q07 now adds the phase information.

Even if one retains:
- the exact physical-fibre labels;
- the exact \(1,2,3\) harmonic multipliers;
- every carry-translation phase offset;
- real-valued Fourier conjugacy;
- and one selected negative-phase triple witness for **every one of the ten L01 core families**,

the resulting affine phase system is still simultaneously solvable.

Therefore the finite one-witness-per-family linear route is not blocked by support **or** phase consistency.

## Proof

### 1. Physical block words

Using the exact D01 compiler, the ten core families have physical labelled block words

\[
\begin{array}{c|c}
F_1&(0,0,1,1)\\
F_2&(0,1,1,1)\\
F_3&(1,1,1,2)\\
F_4&(1,1,2,2)\\
F_6&(2,2,2,3)\\
F_7&(2,2,3,3)\\
F_9&(0,1,1,2)\\
F_{10}&(1,2,2,3)\\
F_{15}&(0,1,2,3)\\
F_{16}&(0,1,2,3).
\end{array}
\]

For a selected triple, substitute Q04's multiplier vector into the physical fibres in those labelled positions.  Negative modes contribute the negative of the corresponding positive-mode phase because the functions are real.

This gives the displayed ten rows.

### 2. Translation phases are only right-hand sides

Q02 maps the labelled factors by
\[
C_t=c_tN+B_{j_t}.
\]
Fourier translation multiplies a coefficient by
\[
e_P(-\xi c_tN),
\]
which adds a known scalar phase to the triple product.  It does not change the coefficient matrix multiplying the unknown physical phases \(\theta_{j,k}\).

Thus every carry pattern changes only the right-hand side
\[
A\theta=b.
\]

### 3. Exact rank certificate

The replay tool evaluates the displayed integer matrix with exact Bareiss elimination.  The displayed ten-column minor has determinant
\[
-3\ne0.
\]
So the ten rows are linearly independent and
\[
A\mathbb R^{12}=\mathbb R^{10}.
\]

For any real representatives of the desired phases modulo \(2\pi\), solve
\[
A\theta=b.
\]
Reducing the solution modulo \(2\pi\) gives the required simultaneous phase assignment.

No numerical rank calculation is used.

## Replay

Exact pure-Python certificate:

`work_packages/GCL_ERDOS3/tools/e3_q07_phase_matrix.py`.

It regenerates:
1. the ten D01 physical block words;
2. the selected Q04 triple rows;
3. the full \(10\times12\) integer phase matrix;
4. the ten-column minor;
5. the determinant \(-3\).

## Claim boundary

This is a **proof-strategy no-go**, not a construction of 4-AP-free fibres.

The phase variables in this abstract model are not asserted to be Fourier data of actual indicator functions.  In particular Q07 does not prove:
- positive-definite realizability of the prescribed coefficients;
- compatibility with all unselected large correlations;
- compatibility across many scales or translated localizations;
- near-extremality;
- or a counterexample to the four-fibre deficit theorem.

Those omitted constraints are now exactly where a successful linear-lane proof must obtain additional force.

## First defect

The linear residual can be reduced further:

> **E3-B-LINEAR-WITNESS-REALIZABILITY-OR-AMPLIFICATION.**  
> Starting from Q04/Q05, prove that actual near-extremal locally 4-AP-free fibre indicators cannot realize the abstract finite harmonic data above, **or** prove that the carry system/scale recursion forces many additional independent witnesses beyond one solvable phase equation per family, enough to produce the required deletion cost.

In particular, another finite system of one phase equation per L01 family is not sufficient.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- `E3-B-LINEAR-WITNESS-AMPLIFICATION`: **REDUCED**.
- New smallest linear residual: `E3-B-LINEAR-WITNESS-REALIZABILITY-OR-AMPLIFICATION`.
- `E3-B-DERIVATIVE-SPECTRAL-ALIGNMENT`: unchanged and still open.
- No parent theorem or gluing-radius candidate is promoted.
