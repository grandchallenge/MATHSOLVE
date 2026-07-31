import Mathlib.Analysis.Distribution.SchwartzSpace.Basic

/-!
# Programme-owned Navier--Stokes critical-integrability target

This file states `NS-CI-001` without identifying it with the Clay-A existence
statement. The PDE and mixed-norm predicates are imported analytic interfaces.
They are declared as axioms so that the trust boundary is explicit. No target
or bridge is proved here.
-/

namespace MathSolve.FormalConjectures.NS

/-- The whole-space spatial domain `R^3`. -/
abbrev R3 := Fin 3 → ℝ

/-- A velocity vector in `R^3`. -/
abbrev Velocity := R3

/-- Fefferman rapidly decreasing initial velocity data, represented by Schwartz maps. -/
abbrev RapidlyDecreasingDatum := SchwartzMap R3 Velocity

/-- A time-dependent whole-space velocity field. -/
abbrev VelocityField := ℝ → R3 → Velocity

/-- Mixed-norm exponents. The time exponent is stored first. -/
structure MixedNormExponents where
  timeExponent : ℕ
  spaceExponent : ℕ
  deriving DecidableEq

/-- The critical Serrin pair `L^4_t L^6_x`. -/
def criticalL4L6 : MixedNormExponents :=
  { timeExponent := 4, spaceExponent := 6 }

/-- Imported predicate for unforced Leray--Hopf solutions on `R^3`. -/
axiom IsUnforcedLerayHopfSolution :
  (viscosity : ℝ) → RapidlyDecreasingDatum → VelocityField → Prop

/-- Imported predicate that the stated mixed norm is finite on `(0,T)`. -/
axiom MixedNormFiniteOnZeroT :
  MixedNormExponents → (T : ℝ) → VelocityField → Prop

/-- Imported positive Clay whole-space alternative. -/
axiom PositiveClayWholeSpaceAlternative : Prop

/--
The canonical universal critical-integrability target.

Quantifier order is part of the contract: positive viscosity, rapidly decreasing
initial data, every unforced Leray--Hopf solution, and every finite positive time
horizon. The mixed norm is `L^4_t L^6_x` because `criticalL4L6` stores the time
exponent first.
-/
def UniversalCriticalIntegrability : Prop :=
  ∀ (viscosity : ℝ), 0 < viscosity →
    ∀ (u0 : RapidlyDecreasingDatum) (u : VelocityField),
      IsUnforcedLerayHopfSolution viscosity u0 u →
        ∀ (T : ℝ), 0 < T → MixedNormFiniteOnZeroT criticalL4L6 T u

/-- The one-way continuation bridge is an unproved downstream obligation. -/
def CriticalIntegrabilityImpliesClay : Prop :=
  UniversalCriticalIntegrability → PositiveClayWholeSpaceAlternative

/-- The time exponent is exactly four. -/
theorem criticalL4L6_timeExponent : criticalL4L6.timeExponent = 4 := by
  rfl

/-- The space exponent is exactly six. -/
theorem criticalL4L6_spaceExponent : criticalL4L6.spaceExponent = 6 := by
  rfl

/-- Explicit unfolded form used by downstream replay packages. -/
theorem universalCriticalIntegrability_iff :
    UniversalCriticalIntegrability ↔
      ∀ (viscosity : ℝ), 0 < viscosity →
        ∀ (u0 : RapidlyDecreasingDatum) (u : VelocityField),
          IsUnforcedLerayHopfSolution viscosity u0 u →
            ∀ (T : ℝ), 0 < T → MixedNormFiniteOnZeroT criticalL4L6 T u := by
  rfl

end MathSolve.FormalConjectures.NS
