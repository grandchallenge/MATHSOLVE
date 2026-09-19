# RH-R042-PARITY-BOTTOM-PARAMETER-CONTINUITY-001

Campaign: RH-001

Status:
ADMISSION_CANDIDATE__PROVIDER_PROTECTED

Protected provider audit:
grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320
reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md

Protected theorem substrate:
- RH-R036-QW-PARITY-GAP-REDUCTION-001
- RH-R037-QW-SECTOR-GALERKIN-001
- grandchallenge/MATHSOLVE@139f35f14ee831aa5aa3ed83b774b762965d58b3:work_packages/RH_R045_PARITY_SENSITIVE_REMAINDER.md

Primary analytic source:
Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
arXiv:2606.09096v2, especially Sections 4.1--4.5.

## 1. Claim

Let \(A_a\) be the canonical self-adjoint operator representing the
localized Weil quadratic form on \(L^2(-a,a)\), and let

\[
\epsilon_+(e^a),\qquad \epsilon_-(e^a)
\]

denote its lowest even- and odd-sector eigenvalues in the notation of
RH-R036.

Then the two functions

\[
a\longmapsto\epsilon_+(e^a),
\qquad
a\longmapsto\epsilon_-(e^a)
\]

are continuous on \((0,\infty)\).

Consequently,

\[
g(a):=\epsilon_-(e^a)-\epsilon_+(e^a)
\]

is continuous on \((0,\infty)\).

No sign of \(g(a)\) is asserted by this theorem.

## 2. Why a proof is required

Suzuki proves continuity of the unrestricted lowest eigenvalue

\[
\lambda_a=\min\{\epsilon_+(e^a),\epsilon_-(e^a)\},
\]

but explicitly notes that earlier assertions of continuity for the
parity-restricted minima did not provide full details.

The argument below supplies those details by applying Suzuki's fixed-interval
compactness proof separately on the two closed parity subspaces.

## 3. Fixed Hilbert space and parity sectors

Scale \(L^2(-a,a)\) to

\[
H:=L^2(-1,1).
\]

Let

\[
(Jw)(x)=w(-x)
\]

and define the orthogonal parity projections

\[
P_\pm=\frac12(I\pm J),
\qquad
H_\pm=P_\pm H.
\]

The subspaces \(H_\pm\) are closed in \(H\).

Suzuki's scaled closed form is denoted by \(\bar q_a\).  Its Rayleigh
quotient has the same spectrum as the original localized Weil form.

Because the source kernel is even in \(x-y\), the form is parity invariant:

\[
\bar q_a(Ju,Jv)=\bar q_a(u,v).
\]

By polarization, the even and odd sectors are form-orthogonal:

\[
\bar q_a(u_+,u_-)=0
\]

whenever \(u_\pm\in H_\pm\) lie in the form domain.

Hence the form domain is invariant under \(P_\pm\), and

\[
\bar q_a(w)
=
\bar q_a(P_+w)+\bar q_a(P_-w).
\]

After adding a sufficiently large scalar multiple of \(\|w\|^2\), the
form norm is positive and the projections \(P_\pm\) are contractions in
that form norm.

## 4. Parity-preserving form core

Suzuki proves that \(C_c^\infty(-1,1)\) is a form core for the scaled
closed form.

Fix \(a_0>0\), \(\sigma\in\{+,-\}\), and

\[
w\in\mathfrak D(\bar q_{a_0})\cap H_\sigma.
\]

Choose global core approximants

\[
u_n\in C_c^\infty(-1,1),
\qquad
u_n\to w
\]

in the \(\bar q_{a_0}\)-form norm.

Set

\[
w_n=P_\sigma u_n.
\]

Reflection preserves \(C_c^\infty(-1,1)\), so

\[
w_n\in C_c^\infty(-1,1)\cap H_\sigma.
\]

Since \(P_\sigma\) is a contraction in the shifted form norm,

\[
w_n\to P_\sigma w=w
\]

in the same form norm.

Therefore

\[
C_c^\infty(-1,1)\cap H_\sigma
\]

is a form core for the parity-restricted closed form.

This is the key point missing from simply citing continuity of the
unrestricted minimum.

## 5. Sector minima exist

Suzuki proves compactness of the embedding of the scaled form domain into
\(L^2(-1,1)\).

A closed subspace of a compactly embedded form domain remains compactly
embedded.  Therefore each parity restriction has compact resolvent.

For each \(a>0\) and \(\sigma\in\{+,-\}\), the sector minimum

\[
\Lambda_\sigma(a)
:=
\inf_{\substack{
0\ne w\in\mathfrak D(\bar q_a)\cap H_\sigma
}}
\frac{\bar q_a(w)}{\|w\|^2}
\]

is attained by a normalized vector in the corresponding parity sector.

Under the exact coordinate identification used in RH-R036,

\[
\Lambda_+(a)=\epsilon_+(e^a),
\qquad
\Lambda_-(a)=\epsilon_-(e^a).
\]

It therefore suffices to prove continuity of \(\Lambda_\sigma\).

## 6. Source decomposition

Suzuki decomposes the fixed-interval closed form as

\[
\bar q_a=\bar q^0+\bar q_a^1,
\]

where

\[
\bar q^0(w)
=
\overline{\mathcal L}(w)
-
(2A+1)\|w\|^2
\]

is independent of \(a\), closed, and lower bounded.

The remaining part \(\bar q_a^1\) consists of:

- the scalar term \(-\log a\,\|w\|^2\);
- finitely many prime-translation forms;
- the bounded integral-kernel remainder.

On every compact \(a\)-interval \(K\Subset(0,\infty)\),

\[
|\bar q_a^1(w)|
\le C_K\|w\|^2.
\]

More precisely, on a compact \(a\)-interval the bounded part is represented
by a uniformly bounded family of self-adjoint operators \(V_a\) that is
strongly continuous in \(a\).

For the prime terms, after zero-extension to \(L^2(\mathbb R)\), translation
is strongly continuous in its shift.  The interval compression is multiplication
by moving characteristic functions, which is also strongly continuous.  At a
prime-entry threshold \(2a=\log n\), the overlap interval shrinks to measure
zero, so the corresponding compressed translation converges strongly to zero.
No operator-norm continuity of translations is asserted.

The archimedean remainder kernels vary locally in Hilbert--Schmidt norm, and
the scalar term is norm-continuous.  Therefore, if

\[
a_n\to a_0,
\qquad
w_n\to w_*
\quad\text{in }L^2(-1,1),
\]

then uniform boundedness plus strong continuity gives

\[
\langle w_n,V_{a_n}w_n\rangle
\to
\langle w_*,V_{a_0}w_*\rangle.
\]

This is the joint continuity statement actually required below.

## 7. Upper semicontinuity in a fixed parity sector

Fix \(a_0>0\) and \(\sigma\in\{+,-\}\).

Let \(w_0\in\mathfrak D(\bar q_{a_0})\cap H_\sigma\) be a normalized
sector minimizer:

\[
\bar q_{a_0}(w_0)=\Lambda_\sigma(a_0).
\]

By Section 4, choose normalized parity-preserving smooth approximants

\[
w_k\in C_c^\infty(-1,1)\cap H_\sigma
\]

such that

\[
w_k\to w_0
\]

in the \(\bar q_{a_0}\)-form norm.

For every fixed \(k\),

\[
\Lambda_\sigma(a)\le\bar q_a(w_k).
\]

The explicit source formula gives

\[
\bar q_a(w_k)\to\bar q_{a_0}(w_k)
\quad(a\to a_0).
\]

Hence

\[
\limsup_{a\to a_0}\Lambda_\sigma(a)
\le
\bar q_{a_0}(w_k).
\]

Letting \(k\to\infty\),

\[
\boxed{
\limsup_{a\to a_0}\Lambda_\sigma(a)
\le
\Lambda_\sigma(a_0).
}
\]

## 8. Lower semicontinuity in a fixed parity sector

Let

\[
a_n\to a_0.
\]

Pass to a subsequence realizing

\[
\liminf_{n\to\infty}\Lambda_\sigma(a_n).
\]

For each \(n\), choose a normalized sector minimizer

\[
w_n\in\mathfrak D(\bar q_{a_n})\cap H_\sigma,
\qquad
\bar q_{a_n}(w_n)=\Lambda_\sigma(a_n).
\]

Choose one fixed nonzero smooth parity vector

\[
\phi\in C_c^\infty(-1,1)\cap H_\sigma.
\]

Since

\[
\Lambda_\sigma(a_n)
\le
\frac{\bar q_{a_n}(\phi)}{\|\phi\|^2}
\]

and the right side is bounded for \(a_n\) in a compact neighborhood of
\(a_0\), the sequence \(\Lambda_\sigma(a_n)\) is bounded above.

Using

\[
\bar q_{a_n}(w_n)
=
\bar q^0(w_n)+\bar q_{a_n}^1(w_n)
\]

and the uniform bounded-form estimate for \(\bar q_a^1\), we obtain a
uniform upper bound on

\[
\overline{\mathcal L}(w_n).
\]

The form \(\overline{\mathcal L}\) is lower bounded, so the normalized
sequence is bounded in Suzuki's \(H^{\log}(-1,1)\) form space.

By Suzuki's compact embedding theorem, after passing to a further
subsequence,

\[
w_n\to w_*
\quad\text{in }L^2(-1,1).
\]

Because \(H_\sigma\) is closed,

\[
w_*\in H_\sigma.
\]

Norm convergence and \(\|w_n\|=1\) give

\[
\|w_*\|=1.
\]

The continuous bounded part satisfies

\[
\bar q_{a_n}^1(w_n)
\to
\bar q_{a_0}^1(w_*).
\]

The fixed closed form is lower semicontinuous:

\[
\liminf_{n\to\infty}\bar q^0(w_n)
\ge
\bar q^0(w_*).
\]

Therefore

\[
\begin{aligned}
\liminf_{n\to\infty}\Lambda_\sigma(a_n)
&=
\liminf_{n\to\infty}
\left[
\bar q^0(w_n)+\bar q_{a_n}^1(w_n)
\right]
\\
&\ge
\bar q^0(w_*)+\bar q_{a_0}^1(w_*)
\\
&=
\bar q_{a_0}(w_*)
\\
&\ge
\Lambda_\sigma(a_0).
\end{aligned}
\]

Thus

\[
\boxed{
\liminf_{a\to a_0}\Lambda_\sigma(a)
\ge
\Lambda_\sigma(a_0).
}
\]

## 9. Continuity

Sections 7 and 8 give, for each \(\sigma\in\{+,-\}\),

\[
\lim_{a\to a_0}\Lambda_\sigma(a)
=
\Lambda_\sigma(a_0).
\]

Since \(a_0>0\) was arbitrary,

\[
\boxed{
\Lambda_+,\Lambda_- \text{ are continuous on }(0,\infty).
}
\]

Equivalently,

\[
\boxed{
a\mapsto\epsilon_+(e^a),
\quad
a\mapsto\epsilon_-(e^a)
\text{ are continuous.}
}
\]

Therefore

\[
\boxed{
g(a)=\epsilon_-(e^a)-\epsilon_+(e^a)
\text{ is continuous on }(0,\infty).
}
\]

## 10. Continuation corollary conditional on RH-R045 effective admission

The protected RH-R045-PARITY-SENSITIVE-REMAINDER-001 proves

\[
g(a)>0
\quad
(0<a\le2/15).
\]

Once that theorem is protected, continuity implies that

\[
\mathcal P:=\{a>0:g(a)>0\}
\]

is open and has a connected component adjacent to \(a=0\) containing
\((0,2/15]\).

Write that component as

\[
(0,a_*),
\qquad
a_*\in(2/15,\infty].
\]

If \(a_*<\infty\), then necessarily

\[
\boxed{g(a_*)=0.}
\]

Thus a failure of the simple-even parity ordering cannot occur by a jump.

Combined with the RH-R041 scalar resolvent interface, a finite endpoint
can be attacked through the exact pole-localization and Herglotz margins.

The continuity theorem itself is independent of RH-R041. The endpoint classification through the scalar resolvent interface is used only after RH-R041 is protected.

## 11. Falsification checks

The proof specifically addresses the following failure modes.

1. Global continuity does not imply sector continuity.
   The proof is repeated separately inside fixed closed parity subspaces.

2. Form domains vary with \(a\).
   Upper semicontinuity uses common smooth core vectors.
   Lower semicontinuity uses the source decomposition into one fixed closed
   form plus bounded \(a\)-dependent forms.

3. A global core need not automatically be a sector core.
   The proof explicitly applies parity projections and uses their form-norm
   contractivity.

4. Prime thresholds could cause jumps.
   The translation terms enter with overlap intervals of vanishing length;
   Suzuki's bounded-form part is continuous in \((a,w)\), including those
   thresholds.

5. An \(L^2\) compactness limit could leave the parity sector.
   It cannot because \(H_\pm\) are closed.

6. Continuity of \(g\) does not prove \(g>0\).
   No all-\(a\) sign claim is made.

## 12. Claim boundary

This theorem does not prove:

- \(g(a)>0\) for all \(a\);
- even-sector simplicity for all \(a\);
- monotonicity of either sector bottom;
- monotonicity of the Herglotz margin;
- determinant convergence to \(\Xi\);
- RH;
- novelty or priority.

## 13. Terminal candidate disposition

RH-R042_PARITY_SECTOR_BOTTOM_CONTINUITY_PROVED__READY_FOR_EXACT_HEAD_ADMISSION
