# NS-CI-R014-A2-L5-13 — C3 diagonal closure audit

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected base at tranche start: `eacdde093d7f515f890f055cd46f32a7998fac1d`
- Predecessor: `NS-CI-R014-A2-L5-12`
- Governing field-development route: C3 frequency--physical-scale matching
- Result:
  `C3_DIAGONAL_GENERIC_REPAIRS_TERMINATED__STRICT_HIGH_NO_ELL1__UNSIGNED_RENORMALIZATION_RETURNS_L4__LOCAL_SIGN_NOT_UNIVERSAL`
- A2 theorem: open
- L5: active
- MATHCERT adjudication: absent
- Evidence class: exact exponent reduction plus algebraic/scaling fixtures; not an NSE counterexample

This package executes the three `C3-DIAG` variants left open by
`NS_CI_R014_A2_L5_12_FREQUENCY_SCALE_TRANSPLANT_BOUNDARY.md`.

The outcome is negative for the three **generic** repairs.  It does not close
frequency--scale matching as a research idea.  It shows that the central band
cannot be repaired merely by moving the observation scale, replacing the
source norm by unsigned dissipation/threshold quantities, or retaining the
instantaneous signed localized energy flux without a new PDE theorem.

The live successor is therefore a genuinely dynamic active-band depletion,
anti-concentration, or time-correlated flux-coherence statement.

## 1. Protected predecessor

L5-12 verified the Guo--Wang--Xiong two-index kernel

```math
K_{k-j}
\sim
\begin{cases}
2^{-(k-j)/m}, & j\ll k,\\
1, & |j-k|=O(1),\\
2^{-(j-k)}, & j\gg k,
\end{cases}
```

with

```math
2<p<\infty,
\qquad
m=\frac{3p}{p-2}>3,
\qquad
\frac2p+\frac3m=1.
```

The source coefficient is

```math
a_j=\|\dot\Delta_j u^3\|_{L^p_tL^m_x},
```

and the source recursion assumes `sum_j a_j<infinity`.

The A2/Leray interpolation available in L5-12 gives

```math
a_j
\lesssim
U_0^{1-2/p}\nu^{-1/p}
\lambda_j^{1/2}D_j^{1/p},
```

where

```math
D_j=\nu\int_I\lambda_j^2\|u_j(t)\|_2^2dt,
\qquad
\sum_jD_j<\infty.
```

Thus the central issue is the half-derivative factor `lambda_j^(1/2)`.

## 2. Variant A — shifted observation scale

The proposed repair is to observe an active source shell `j` at a strictly
finer physical scale `k>j`, so that the low-frequency side of the source
kernel contributes

```math
2^{-(k-j)/m}.
```

Write

```math
s_j=k-j.
```

Then the Leray-controlled contribution has weight

```math
w_j
=
2^{-s_j/m}\lambda_j^{1/2}
=
2^{j/2-s_j/m}.
```

### Lemma 2.1 — fixed shifts cannot repair the half derivative

If `s_j=O(1)`, then

```math
w_j\asymp2^{j/2},
```

so the shifted kernel leaves the same exponentially growing deficit.

More generally, if

```math
s_j=\alpha j+O(1),
```

then

```math
w_j\asymp2^{(1/2-\alpha/m)j}.
```

To control

```math
\sum_j w_jD_j^{1/p}
```

uniformly for every nonnegative `D in ell^1`, duality between
`ell^p` and `ell^{p'}` requires

```math
w\in\ell^{p'},
\qquad
p'=\frac p{p-1}.
```

Therefore a linear shift must satisfy strictly

```math
\boxed{\alpha>\frac m2.}
```

At the borderline `alpha=m/2`, `w_j\asymp1`; this is not enough.
For example

```math
D_j=j^{-p}
```

belongs to `ell^1`, while

```math
D_j^{1/p}=j^{-1}
```

is not summable.

Thus the observation scale needed to absorb the scalar half derivative is not
a fixed buffer.  It has

```math
k
>
\left(1+\frac m2\right)j+O(j),
```

and hence

```math
r_k=2^{-k}
\ll
\lambda_j^{-1}.
```

Because `m>3`, the physical scale is already finer than
`lambda_j^{-5/2}` at the threshold slope, and its parabolic time scale is
far shorter than the natural `lambda_j^{-2}` dissipative time.

This geometric observation alone is not a rejection: a sparse physical-scale
subsequence can still be continuation-relevant.  The decisive problem is the
source diagonal at the new physical scale.

### Lemma 2.2 — moving one active source off the diagonal does not remove the new diagonal

For every physical index `k`, the source kernel still has

```math
K_0a_k=a_k.
```

Thus mapping a particular active shell `j` to a finer observation scale
`k(j)` only moves that one contribution into the low-frequency tail.  The
frequency `k(j)` itself remains on the central diagonal.

The only scalar information that could distinguish that new diagonal from the
old one is the dissipation selector: if one knew `k>Q(t)` throughout the
time interval used by the local-energy test, the shell would be strict high.
The next fixture shows that even this is insufficient to manufacture the
source `ell^1` sequence from the current budgets.

## 3. Strict-high separator

Choose a fixed divergence-free annular Schwartz packet `phi` with nonzero
third component and scale it on pairwise disjoint time intervals `I_j` as

```math
u_j(x,t)
=
c\nu\lambda_j\phi(\lambda_jx),
\qquad
t\in I_j,
```

where `c>0` is chosen, after accounting for the fixed finite LP overlap, so
that every nonzero high block obeys

```math
\lambda_p^{-1}\|u_p\|_\infty<c_0\nu.
```

Take

```math
|I_j|=\lambda_j^{-2}.
```

There are no active high shells in this fixture; the selector can be kept at
the fixed base value `Q=0`.

This is a static/scaling fixture only.  It is not asserted to solve
Navier--Stokes.

### 3.1 A2 and Leray-type budgets are finite

The total occupied time is

```math
\sum_j|I_j|
=
\sum_j\lambda_j^{-2}
<\infty.
```

Since `Q=0`, `Lambda` is fixed and its `L^2_t` budget is finite.

For a scaled packet,

```math
\|u_j\|_2^2
\asymp
\nu^2\lambda_j^{-1}.
```

Thus the energy supremum is finite and

```math
\nu\sum_j
\lambda_j^2\|u_j\|_2^2|I_j|
\asymp
\nu^3\sum_j\lambda_j^{-1}
<\infty.
```

### 3.2 The source critical sequence still diverges

At the critical source exponent,

```math
1-\frac3m=\frac2p.
```

Hence

```math
\|u_j^3\|_m
\asymp
\nu\lambda_j^{2/p},
```

and therefore

```math
a_j
\asymp
\nu\lambda_j^{2/p}|I_j|^{1/p}
=
\nu.
```

Consequently

```math
\sum_ja_j=\infty.
```

This proves the scalar non-implication

```text
A2 + Leray budgets + strict-high threshold control
DO NOT imply the source Chemin--Lerner ell^1 coefficient sequence.
```

The key point is that the strict-high definition supplies an upper **level**
`c_0 nu lambda_p`, not any decay in the distance `p-Q`.

### Disposition of Variant A

A fixed shift gives no asymptotic gain.  A linearly growing shift can attenuate
the chosen active shell, but every physical scale retains its own unit
diagonal; declaring that diagonal strict high does not provide source
summability.

A time-dependent choice `k=k(Q(t))` would additionally make the physical
localizer move with the selector.  Freezing it over a backward cylinder would
require a persistence/coherence statement keeping `Q(t)` below it.  Those are
respectively B4/L3 reopening obligations and are not supplied here.

Therefore the generic absolute shifted-scale repair is terminated:

```text
SHIFTED_SCALE_ABSOLUTE_ROUTE_BLOCKED__STRICT_HIGH_NO_ELL1.
```

This does not rule out a new PDE theorem coupling selector motion to physical
cylinders.

## 4. Variant B — unsigned diagonal renormalization

The second proposal is to replace `a_j` by a threshold defect or
energy/dissipation amplitude whose central band is A2/Leray controlled.

The active threshold shell has the wrong one-sided information for such a
repair:

```math
\|u_Q\|_\infty
\ge
c_0\nu\Lambda.
```

There is no threshold upper bound at `Q`.

For an unsigned dissipative estimate, standard Bernstein gives

```math
\|u_Q\|_\infty^2
\lesssim
\lambda_Q^3\|u_Q\|_2^2.
```

With the shell dissipation density

```math
D_Q(t)
=
\nu\lambda_Q^2\|u_Q(t)\|_2^2,
```

this becomes exactly

```math
\boxed{
\|u_Q\|_\infty^2
\lesssim
\nu^{-1}\lambda_QD_Q.
}
```

The same calculation applies to every shell in a fixed band
`Q-L<=p<=Q`, up to fixed dyadic constants.

But

```math
\lambda_QD_Q
```

is precisely the active diagonal of the protected L4 weighted column.  L4
already established that the present scalar budgets do not control its time
integral.

The strict-high fixture in Section 3 also shows that the normalized ratio

```math
\frac{\|u_p\|_\infty}{\nu\lambda_p}
```

need not decay with `p-Q` under threshold logic alone.  Thus a
distance-dependent threshold defect cannot be inferred from the definition.

### Disposition of Variant B

Any unsigned diagonal repair based only on ordinary Bernstein plus shell
dissipation returns the protected L4 active column.  Improving the exponent
requires new spatial anti-concentration, improved Bernstein saturation, or an
equivalent dynamic depletion theorem.

```text
UNSIGNED_DIAGONAL_RENORMALIZATION_RETURNS_L4_ACTIVE_COLUMN.
```

A renormalized quantity derived from a genuinely new signed/local identity is
not excluded by this statement.

## 5. Variant C — signed central-band local energy flux

The remaining generic possibility is that the absolute source norm destroys a
cancellation already present in the exact localized convection-plus-pressure
flux.

For a smooth incompressible field, the relevant total energy flux is

```math
F
=
\left(\frac{|u|^2}{2}+p\right)u,
```

and localization contributes

```math
\int F\cdot\nabla\varphi.
```

The following exact finite-band fixture rules out a universal algebraic
cancellation or favorable sign for this term.

### Lemma 5.1 — exact finite-band sign-indefinite localized flux

Work on the periodic `(x_1,x_3)` torus and embed the field in three dimensions
with no `x_2` dependence.  Let

```math
\psi(x_1,x_3)
=
\cos(x_1-x_3)
+
\sin(2x_1+2x_3)
+
\cos(3x_1+x_3),
```

and define

```math
u=(\partial_3\psi,0,-\partial_1\psi).
```

Then `div u=0`.  Let `p` be the zero-mean periodic pressure determined by

```math
-\Delta p
=
\partial_i\partial_j(u_i u_j).
```

The three velocity wavevectors have squared lengths

```text
2, 8, 10,
```

so they lie in one fixed finite-width frequency band.

Define the strictly positive test

```math
\varphi(x_3)
=
1+\frac14\sin(4x_3),
\qquad
\partial_3\varphi=\cos(4x_3).
```

An exact rational Fourier convolution gives the horizontally averaged vertical
energy flux

```math
\left\langle
\left(\frac{|u|^2}{2}+p\right)u_3
\right\rangle_{x_1,x_2}
=
\frac35
-
\frac3{10}\cos(4x_3).
```

Therefore, with normalized torus mean,

```math
\boxed{
\left\langle
\left(\frac{|u|^2}{2}+p\right)u_3
\partial_3\varphi
\right\rangle
=
-\frac3{20}.
}
```

If `u` is replaced by `-u`, the pressure is unchanged because it is
quadratic in `u`, while the total energy flux changes sign.  Hence the same
pairing becomes

```math
+\frac3{20}.
```

The example persists at arbitrary high central frequency.  For integer
`N>=1`, set

```math
\psi_N(x_1,x_3)
=
N^{-1}\psi(Nx_1,Nx_3),
```

so the velocity is `u(Nx_1,Nx_3)`, and use

```math
\varphi_N(x_3)
=
1+\frac1{4N}\sin(4Nx_3).
```

Then `varphi_N>0`, its derivative is `cos(4Nx_3)`, all velocity
frequencies are multiplied by `N`, and the normalized pairing retains the
same nonzero sign-indefinite value.

The fixture is an algebraic identity test.  It is not an NSE trajectory and
does not rule out cancellation produced by time evolution, a selected
space-time geometry, or another PDE-specific structure.

### Relation to the Guo--Wang--Xiong endpoint test

The source local energy identity contains the exact signed convection and
pressure terms

```math
\int |u|^2u^3\,\eta\partial_3\Phi_n,
\qquad
\int \pi u^3\,\eta\partial_3\Phi_n,
```

before they are bounded by positive coefficient convolutions.

Lemma 5.1 shows that incompressibility, the pressure Poisson relation, a
positive localization, and finite-band frequency support do not by themselves
make the combined central energy flux vanish or give it one sign.

Thus a successful signed repair must be a **dynamic** theorem: for example a
time-correlated cancellation across nested backward cylinders or a
selected-transfer coherence law.  It cannot be a universal instantaneous
algebraic identity.

### Disposition of Variant C

```text
UNIVERSAL_SIGNED_CENTRAL_LOCAL_FLUX_CANCELLATION_FALSIFIED.
```

Equation-specific time-correlated signed depletion remains live.

## 6. Combined C3-DIAG disposition

The three generic repairs left by L5-12 now have exact boundaries:

```text
A. shifted absolute observation:
   fixed shift -> no gain;
   growing shift -> old diagonal replaced by a new diagonal;
   strict-high threshold -> no ell^1 decay.

B. unsigned renormalization:
   Bernstein + dissipation -> nu^-1 lambda_Q D_Q,
   exactly the protected L4 active diagonal.

C. signed instantaneous localization:
   exact total convection+pressure flux is nonzero and sign-indefinite
   even for a finite central frequency band and a positive test.
```

Hence

```text
C3_DIAGONAL_GENERIC_REPAIRS_TERMINATED
__STRICT_HIGH_NO_ELL1
__UNSIGNED_RENORMALIZATION_RETURNS_L4
__LOCAL_SIGN_NOT_UNIVERSAL.
```

This is a bounded route termination, not an exhaustion theorem for all
frequency--scale methods.

## 7. What remains genuinely live

The surviving mechanism must add information not present in the three generic
repairs.

### 7.1 High-Lambda active-band anti-concentration

The most direct target is a dynamic improvement of Bernstein on high-activity
times.  At `D=1`, the dimensionally normalized form suggested by L5-8 is

```math
\|u_q(t)\|_\infty^2
\lesssim
\lambda_E\lambda_q^2\|u_q(t)\|_2^2,
\qquad
\lambda_E=(\nu/U_0)^2,
```

in a time-averaged or active-band form strong enough to control the
high-`Lambda` packet tail.

This gains one full frequency power relative to ordinary three-dimensional
Bernstein.  It must be proved dynamically; the existing packet fixtures rule
out deriving it from scalar budgets alone.

### 7.2 Time-correlated central flux cancellation

Alternatively, retain the signed central-band convection and pressure flux
across nested backward cylinders and prove cancellation after time integration.
Such a theorem must use NSE evolution and must survive the sign fixture above,
which excludes only universal instantaneous algebraic sign/cancellation.

### 7.3 Selector/physical-scale coherence

A theorem relating the moving `Q(t)` to a fixed backward cylinder strongly
enough to keep its central band strict high would also reopen the shifted-scale
route.  This is a genuine L3/B4 reopening condition and must be proved rather
than assumed.

## 8. Preferred successor: C2-DIAG

The natural next bounded tranche is now the intermittency/anti-concentration
side of the L5-10 programme, but localized to the diagonal exposed by L5-12.

Do **not** assume a global intermittency dimension.  Translate the
Cheskidov--Peng Bernstein-saturation definition into a high-`Lambda`,
finite-active-band statement and ask whether NSE dynamics force enough
dimension-one depletion near a putative singular time.

A useful target is any theorem implying

```math
\int_{(T-\delta,T)\cap\{\Lambda>R\}}
\sum_{Q(t)-L\le q\le Q(t)}
\|u_q(t)\|_\infty^2dt
<\infty
```

together with a frequency--scale estimate controlling the far-low part, or a
direct estimate of the complete high-`Lambda` `S_1` tail.

A still cleaner target is an active-band `D=1` depletion inequality whose
right-hand side is a Leray-controlled dissipation integral.

## 9. Hard rejection tests for the successor

Reject any C2-DIAG candidate that:

- merely assumes Bernstein non-saturation or an intermittency dimension;
- replaces the active diagonal by `lambda_QD_Q`;
- uses strict-high at `p=Q`;
- binds a time-dependent physical cutoff to `Q(t)` without paying selector
  variation;
- derives only a fixed-distance frequency gain;
- imports a periodic/forced averaged intermittency theorem as an unforced
  whole-space A2 theorem;
- uses the scalar fixtures as NSE counterexamples;
- introduces terminal-frequency-dependent constants.

## 10. Claim boundary

A2 remains unproved.

L5-13 proves only:

1. the exact shift rate required for the source low-frequency kernel to absorb
   the protected half-derivative deficit;
2. a strict-high scaling fixture showing that threshold control plus A2/Leray
   scalar budgets still does not imply the source critical `ell^1` sequence;
3. the exact reduction of unsigned active-diagonal Bernstein control to the
   protected L4 weighted column;
4. an exact finite-band Fourier fixture falsifying universal instantaneous
   signed cancellation/sign of the localized total energy flux.

No fixture here is an NSE trajectory.  No theorem about the selected unforced
A2 class is promoted beyond these reduction statements.  No MATHCERT,
novelty, priority, or publication claim is asserted.
