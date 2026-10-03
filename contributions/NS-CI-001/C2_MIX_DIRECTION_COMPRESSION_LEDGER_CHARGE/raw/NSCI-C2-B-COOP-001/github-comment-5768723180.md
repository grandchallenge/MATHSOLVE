GCL-CONTRIBUTION-RESULT/1
dispatch_id: NSCI-C2-B-COOP-001
assignment: B
disposition: REFUTED
context_class: ZERO_CONTEXT
external_sources: NONE
timebox_observed: YES

## Strongest exact statement

A lower bound on the integrated fourth-moment damping $D_4 = \int_0^S Q_4(s)\,ds \ge c_0 > 0$ does not imply a lower bound on critical-band Fourier mass $\sum_{c_- \le |hn| \le c_+} |c_n^{(h)}(s)|^2$ on any set of positive measure for any fixed annulus $[c_-, c_+]$, nor does it force a physical dissipation-selector charge. Specifically:
1. For any $S > 0$, $K > 0$, and any fixed scaled annulus $0 < c_- < c_+ < \infty$, there exists a family of valid limiting packet states with unit zeroth mass $M_0(s) \equiv 1$ and $D_4 = K$ whose Fourier mass in $[c_-, c_+]$ is identically zero for all $s \in [0, S]$, with second moment $Q_2(s) \to 0$ arbitrarily small.
2. In the physical Navier-Stokes scaling, $D_4$ corresponds to an integrated $\dot{H}^2$ semiclassical curvature quantity ($N h^{-2} \int \|\nabla^2 u\|^2$), which has no counterpart in the finite $L_t^2 \dot{H}^1$ Leray-Hopf energy dissipation budget.
3. To convert $D_4 \ge c_0 > 0$ into critical-band mass and selector charge, it is necessary and sufficient to impose an inverse spectral concentration bound $\sup_{s \in I} \frac{M_0(s) Q_4(s)}{Q_2(s)^2} \le C_* < \infty$ on a set $I \subset [0, S]$ of positive measure, together with an upper envelope bound $\sup_{s\in I} Q_4(s) \le M_4 < \infty$.

## Derivation

1. Spectral Measure Separator (Questions 1 & 2):
Under the transfer theorem (Section 5), $Q_k(s) = \int \xi^k\, d\mu_s(\xi)$ where $\xi = hn$ and $d\mu_s$ is the weak limit of $\sum_n |c_n^{(h)}(s)|^2 \delta_{hn}$. Fix $S > 0$, $K > 0$, and annulus $[c_-, c_+]$ with $0 < c_- < c_+ < \infty$. For parameter $\lambda > c_+$, define the probability measure:
$$\mu_s = (1 - \delta)\delta_0 + \delta \delta_\lambda, \qquad \delta := \frac{K}{S \lambda^4}.$$
For any $\lambda > (2K/S)^{1/4}$, $\delta \in (0, 1/2)$, so $\mu_s$ is a strictly positive, valid probability measure with:
- Zeroth mass: $M_0(s) = \int 1\, d\mu_s = 1$.
- Annular critical mass: Since $\mathrm{supp}(\mu_s) = \{0, \lambda\}$ and $0 < c_- < c_+ < \lambda$, $\mu_s([c_-, c_+]) = 0$ for all $s \in [0, S]$.
- Fourth moment: $Q_4(s) = \int \xi^4\, d\mu_s = \delta \lambda^4 = K/S$.
- Integrated fourth moment: $D_4 = \int_0^S Q_4(s)\,ds = K$.
- Second moment: $Q_2(s) = \int \xi^2\, d\mu_s = \delta \lambda^2 = \frac{K}{S \lambda^2}$.
Taking $\lambda \to \infty$, $D_4 = K$ remains fixed (or arbitrarily large), while $Q_2(s) \to 0$ and critical annular mass remains identically zero. In characteristic coordinates, this corresponds to a spatial packet partitioned into a dominant zero-phase bulk of mass $1-\delta$ and an escaped high-frequency tail of mass $\delta$ with $J^{-1} H = \lambda$. Thus, $D_4$ alone does not force positive mass in any fixed critical annulus, refuting the direct implication.

2. Physical Scaling and Dissipation Budget (Question 4):
Physical time and frequency scale as $dt = \frac{h^2}{\nu N^2} ds$ and $\xi = hn \sim h \frac{\lambda_{\mathrm{phys}}}{N}$. The physical kinetic energy and dissipation scale as $\|u(t)\|_{L^2}^2 \sim N^{-1} M_0$ and $\nu \|\nabla u(t)\|_{L^2}^2 \sim \nu N h^{-2} Q_2(s)$. Integrating dissipation in physical time gives $\nu \int \|\nabla u\|_{L^2}^2 dt \sim N^{-1} Q_2 ds$. In contrast, $Q_4(s) = \lim h^4 \sum n^4 |c_n|^2$ represents the physical $\dot{H}^2$ norm $\|\nabla^2 u(t)\|_{L^2}^2 \sim N^3 h^{-4} Q_4(s)$. Restoring physical time scaling gives $\nu \int \|\nabla^2 u\|_{L^2}^2 dt \sim \frac{N}{h^2} Q_4 ds$. This carries an explicit singular factor $h^{-2}$ and corresponds to an enstrophy dissipation / $\dot{H}^2$ budget, which is not bounded by the finite Leray-Hopf energy inequality $\nu \int_0^T \|\nabla u\|_{L^2}^2 dt \le \frac{1}{2} \|u_0\|_{L^2}^2$. Hence, $D_4$ is an exact packet damping moment, but possesses no direct Leray dissipation counterpart.

3. Moment Relations and Paley-Zygmund Obstruction (Question 3):
By Cauchy-Schwarz on $X = (hn)^2$, $\mathbb{E}[X]^2 \le \mathbb{E}[X^2]$, so $Q_2(s)^2 \le M_0(s) Q_4(s)$. For Paley-Zygmund lower bounds:
$$\mathbb{P}(X > \theta \mathbb{E}[X]) \ge (1 - \theta)^2 \frac{\mathbb{E}[X]^2}{\mathbb{E}[X^2]} = (1 - \theta)^2 \frac{Q_2(s)^2}{M_0(s) Q_4(s)}.$$
Crucially, $Q_4$ appears in the denominator: large $Q_4$ weakens the Paley-Zygmund lower bound unless $Q_2^2$ grows proportionally. Moreover, fourth-moment Markov gives $\mathbb{P}(X > c_+^2) \le \frac{Q_4(s)}{M_0(s) c_+^4}$. If $Q_4$ is large without an upper bound, $c_+$ must diverge as $Q_4^{1/4}$, causing the mass to escape to arbitrarily high frequencies.

4. Weakest Plausible "$D_4$-Plus-Something" Formulation (Question 5):
To extract selector charge from $D_4$, one must prevent high-frequency spectral escape. The minimal missing hypothesis is an inverse concentration (kurtosis) bound $\kappa(s) := \frac{M_0(s) Q_4(s)}{Q_2(s)^2} \le C_* < \infty$ on a measurable set $I \subset [0, S]$ with $|I| > 0$, alongside an upper bound $\sup_{s\in I} Q_4(s) \le M_4 < \infty$. Under this hypothesis:
$$Q_2(s) \ge \sqrt{\frac{m_0}{C_*}} Q_4(s)^{1/2}, \qquad \int_I Q_2(s)\,ds \ge \sqrt{\frac{m_0}{C_* M_4}} \int_I Q_4(s)\,ds.$$
Then Paley-Zygmund and Markov apply uniformly with $c_-^2 = \theta \frac{m_2}{m_0}$ and $c_+^4 = \frac{2 M_4}{m_0 (1-\theta)^2 / C_*}$, yielding fixed critical-band mass $m_{\mathrm{band}} > 0$ and triggering the selector charge $c_*/\nu$.

## Assumptions beyond bootstrap

NONE

## Verification / falsification hooks

1. Discrete test: For $\mu = (1-\delta)\delta_0 + \delta \delta_\lambda$ with $K=1, S=1, \lambda=10^3, \delta=10^{-12}$, check that $M_0 = 1, D_4 = 1$, while the interval $[1/2, 2]$ contains 0 mass and $Q_2 = 10^{-6} \ll 1$.
2. Falsification of direct bridge: Any claim that $D_4 \ge c > 0$ alone implies $\inf_s \mu_s([c_-, c_+]) > 0$ is falsified by testing against the sequence $\mu_s^{(k)} = (1 - k^{-4})\delta_0 + k^{-4}\delta_k$ as $k \to \infty$.
3. Scaling check: The ratio $\frac{\nu \int \|\nabla^2 u\|^2 dt}{\nu \int \|\nabla u\|^2 dt} \sim h^{-2} \frac{Q_4}{Q_2}$ confirms that $Q_4$ has higher differential order and is not controlled by the $L_t^2 \dot{H}^1$ Leray budget.

## Claim boundary

This result does not prove that compression cannot lead to turbulence or breakdown. It does not bound $C_2^+$ or $P_{\mathrm{tot}}$. It does not prove or disprove global Navier-Stokes regularity, nor does it establish whether the coupled characteristic system dynamically enforces the moment ratio bound $M_0 Q_4 / Q_2^2 \le C_*$.

## Next residual

Audit the expansion channel $C_2^+$ and the signed phase source $P_{\mathrm{tot}}$ to determine whether geometric constraints prevent them from canceling large $C_2^-$. In parallel, analyze whether the characteristic transport equation dynamically bounds the moment ratio $M_0 Q_4 / Q_2^2$ to rule out high-frequency escape. These two steps are required to close the compression ledger dichotomy.
