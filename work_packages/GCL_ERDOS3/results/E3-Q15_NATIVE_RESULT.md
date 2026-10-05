# E3-Q15 — exact dyadic cardinalities of the core D01 carry cells

Disposition: **PROVED_NATIVE_CORE_CARRY_CELL_CARDINALITIES**.

This is native GCL work. It gives exact cardinalities for the six distinct carry cells used by the ten-family L01 core and sharpens the quantitative constants in Q12/Q13.

## Statement

Let
\[
N=2^n,\qquad n\ge1,
\]
and for a carry vector
\[
c=(c_0,c_1,c_2,c_3)
\]
define
\[
\Omega_c(N)
=
\left\{
(u,v)\in[0,N-1]^2:
\left\lfloor\frac{u+tv}{N}\right\rfloor=c_t
\ \text{for }t=0,1,2,3
\right\}.
\]

For the eight possible D01 carry vectors one has, on every dyadic \(N\),

\[
\boxed{
|\Omega_{0000}|
=
\frac{N^2+3N+2}{6},
}
\]

\[
\boxed{
|\Omega_{0123}|
=
\frac{N^2-3N+2}{6},
}
\]

\[
\boxed{
|\Omega_{0001}|
=
|\Omega_{0012}|
=
|\Omega_{0111}|
=
|\Omega_{0122}|
=
\frac{N^2-4}{12},
}
\]

and

\[
\boxed{
|\Omega_{0011}|
=
|\Omega_{0112}|
=
\frac{N^2+2}{6}.
}
\]

The ten-family L01 core uses only

\[
0000,\ 0001,\ 0011,\ 0111,\ 0112,\ 0123.
\]

Therefore for every
\[
N\ge16
\]
and every core carry \(c\),

\[
\boxed{
\frac{|\Omega_c(N)|}{N^2}
\ge
\frac{21}{256}.
}
\]

The minimum is attained at \(N=16\) by the \(1/12\)-type cells.

## Proof

### 1. The \(0000\) cell

The carry vector \(0000\) is equivalent to

\[
u+3v<N.
\]

Hence

\[
|\Omega_{0000}|
=
\sum_{v=0}^{\lfloor(N-1)/3\rfloor}
(N-3v).
\]

Because \(N=2^n\) is not divisible by \(3\), writing \(N=3m+1\) or \(N=3m+2\) and evaluating the arithmetic progression gives in both cases

\[
|\Omega_{0000}|
=
\frac{N^2+3N+2}{6}.
\]

### 2. The \(0123\) cell

The carry vector \(0123\) is equivalent to

\[
u+3v\ge3N.
\]

Indeed the \(t=3\) inequality forces
\[
u+3v\ge3N,
\]
and because \(u,v<N\), this automatically implies
\[
u+v\ge N,\qquad
u+2v\ge2N,
\]
while all required upper bounds are automatic.

The reflection
\[
R(u,v)=(N-1-u,N-1-v)
\]
sends
\[
u+3v=s
\]
to
\[
4N-4-s.
\]

Therefore \(R\) gives a bijection from \(\Omega_{0123}\) onto the subset of \(\Omega_{0000}\) satisfying

\[
u+3v\le N-4.
\]

The difference is the boundary strip

\[
N-3\le u+3v\le N-1.
\]

For \(s<N\), the number of solutions to
\[
u+3v=s,\qquad u,v\ge0
\]
is
\[
\left\lfloor\frac{s}{3}\right\rfloor+1.
\]

For dyadic \(N\), summing this quantity over
\[
s=N-3,N-2,N-1
\]
gives exactly
\[
N.
\]

Hence

\[
|\Omega_{0123}|
=
|\Omega_{0000}|-N
=
\frac{N^2-3N+2}{6}.
\]

### 3. The \(0001\) cell

Let
\[
A_2(N):=
\#\{(u,v)\in[0,N-1]^2:u+2v<N\}.
\]

Since \(N\) is even,

\[
A_2(N)
=
\sum_{v=0}^{N/2-1}(N-2v)
=
\frac{N^2+2N}{4}.
\]

The cell \(0001\) is precisely the region

\[
u+2v<N\le u+3v.
\]

Therefore

\[
|\Omega_{0001}|
=
A_2(N)-|\Omega_{0000}|.
\]

Substituting the formulas gives

\[
|\Omega_{0001}|
=
\frac{N^2-4}{12}.
\]

### 4. Exact symmetry classes

Consider the two bijections of \(\mathbb Z_N^2\)

\[
R_{\rm rev}(u,v)
=
(u+3v\bmod N,\,-v\bmod N)
\]

and

\[
R_{\rm neg}(u,v)
=
(N-1-u\bmod N,\,-v\bmod N).
\]

Direct Euclidean-division substitution gives the exact carry mappings

\[
0001
\overset{R_{\rm rev}}{\longleftrightarrow}
0012,
\]

\[
0012
\overset{R_{\rm neg}}{\longleftrightarrow}
0111,
\]

\[
0111
\overset{R_{\rm rev}}{\longleftrightarrow}
0122,
\]

and

\[
0011
\overset{R_{\rm rev}}{\longleftrightarrow}
0112.
\]

Hence

\[
|\Omega_{0001}|
=
|\Omega_{0012}|
=
|\Omega_{0111}|
=
|\Omega_{0122}|
=
\frac{N^2-4}{12}.
\]

Also

\[
|\Omega_{0011}|
=
|\Omega_{0112}|.
\]

### 5. Partition identity

The eight carry vectors

\[
0000,\ 0001,\ 0011,\ 0012,\ 0111,\ 0112,\ 0122,\ 0123
\]

partition the whole square

\[
[0,N-1]^2.
\]

Thus

\[
N^2
=
|\Omega_{0000}|
+
|\Omega_{0123}|
+
4|\Omega_{0001}|
+
2|\Omega_{0011}|.
\]

Substituting the formulas already proved gives

\[
|\Omega_{0011}|
=
\frac{N^2+2}{6}.
\]

Therefore also

\[
|\Omega_{0112}|
=
\frac{N^2+2}{6}.
\]

This completes the exact cardinality table.

## Uniform core lower bound

For the six core carries, the smallest exact formula is

\[
\frac{N^2-4}{12}.
\]

If
\[
N\ge16,
\]
then

\[
\frac{N^2-4}{12N^2}
=
\frac1{12}\left(1-\frac4{N^2}\right)
\ge
\frac1{12}\left(1-\frac1{64}\right)
=
\frac{21}{256}.
\]

Hence

\[
\frac{|\Omega_c|}{N^2}
\ge
\frac{21}{256}
\]
for every L01 core carry.

## Sharpened Q12 constant

Q12 expands the zero localized AP count into one density baseline plus 15 nonempty fluctuation terms.

Using Q15,

\[
W_F^{\mathrm{loc}}
=
\frac{|\Omega_c|}{N^2}
\prod_{t=0}^{3}\alpha_t
\ge
\frac{21}{256}\beta^4.
\]

Therefore at least one localized fluctuation term satisfies

\[
\boxed{
|T_{F,S}^{\mathrm{loc}}|
\ge
\frac{21}{15\cdot256}\beta^4
=
\frac{7}{1280}\beta^4.
}
\]

This replaces the conservative Q12 bound

\[
\frac{\beta^4}{3840}.
\]

The improvement factor is exactly

\[
21.
\]

## Sharpened Q13 density increment

If the large Q12/Q15 term is singleton, Q13 loses at most a factor \(2\) through bounded variation.

Therefore there exists a prefix or suffix interval \(J\) with

\[
\boxed{
|J|
\ge
\frac{7}{2560}\beta^4N
}
\]

and

\[
\boxed{
\frac{|B\cap J|}{|J|}
\ge
\alpha+\frac{7}{2560}\beta^4.
}
\]

Again this is a factor-\(21\) improvement over the conservative Q13 constant.

## Carry-kernel energy corollary

Let

\[
p_c:=\frac{|\Omega_c|}{N^2}.
\]

Because
\[
K_c=1_{\Omega_c}
\]
is Boolean,

\[
\sum_{a,b}
|\widehat K_c(a,b)|^2
=
p_c.
\]

The zero-frequency contribution is

\[
|\widehat K_c(0,0)|^2
=
p_c^2.
\]

Hence the total nonzero carry-kernel spectral energy is

\[
\boxed{
\sum_{(a,b)\ne(0,0)}
|\widehat K_c(a,b)|^2
=
p_c(1-p_c).
}
\]

For every core carry and \(N\ge16\),

\[
p_c\ge\frac{21}{256}.
\]

Also every displayed exact formula gives
\[
p_c<\frac14.
\]

Therefore

\[
\boxed{
\sum_{(a,b)\ne(0,0)}
|\widehat K_c(a,b)|^2
>
\frac34\cdot\frac{21}{256}
=
\frac{63}{1024}.
}
\]

Thus the family-specific information retained by Q14 has uniformly positive nonzero spectral energy; it is not an asymptotically vanishing boundary correction.

This does not identify where that energy lies.

## Claim boundary

Q15 sharpens constants and proves nontrivial nonzero carry-kernel spectral energy.

It does not prove:
- concentration on useful frequency lines;
- cross-family spectral alignment;
- a density-loss exponent below \(2\);
- or the four-fibre deficit theorem.

## Frontier effect

- \`E3-B-CARRY-LOCALIZED-CANCELLATION\`: quantitatively strengthened to \(7\beta^4/1280\).
- \`E3-B-CARRY-GEOMETRY-DENSITY-INCREMENT\`: quantitatively strengthened to \(7\beta^4/2560\).
- \`E3-B-CARRY-KERNEL-SPECTRAL-INCOMPATIBILITY\`: remains open, now with uniform nonzero kernel spectral energy at least \(63/1024\).
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-D01 exact carry compiler.
- E3-L01 ten-family core.
- E3-Q12 exact carry-localized cancellation.
- E3-Q13 carry-geometry density increment.
- E3-Q14 carry-kernel Fourier representation.
