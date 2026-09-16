import Mathlib.Computability.StateTransition
import Mathlib.Tactic

/-!
# Bounded deterministic step simulation

This file proves the generic quantitative composition lemma used by the PNP
machine-model bridge. A concrete compiler supplies a state encoding and proves
that every one source transition is simulated by at most a fixed number of
target transitions. The theorem below composes those local witnesses over a
whole `EvalsToInTime` run.
-/

namespace MathSolve.PNP

/-- A functional simulation with a uniform target-step bound for each source step. -/
def FixedStepFunctionalSimulation {Source Target : Type}
    (sourceStep : Source → Option Source) (targetStep : Target → Option Target)
    (encode : Source → Target) (stepFactor : Nat) : Prop :=
  ∀ {source source' : Source}, sourceStep source = some source' →
    Nonempty (StateTransition.EvalsToInTime targetStep (encode source)
      (some (encode source')) stepFactor)

/-- Exact source iteration composes a fixed-step functional simulation. -/
theorem fixedStepSimulation_iterate
    {Source Target : Type}
    {sourceStep : Source → Option Source} {targetStep : Target → Option Target}
    {encode : Source → Target} {stepFactor : Nat}
    (simulation : FixedStepFunctionalSimulation sourceStep targetStep encode stepFactor) :
    ∀ (steps : Nat) (source source' : Source),
      ((flip bind sourceStep)^[steps]) (some source) = some source' →
      Nonempty (StateTransition.EvalsToInTime targetStep (encode source)
        (some (encode source')) (stepFactor * steps)) := by
  intro steps
  induction steps with
  | zero =>
      intro source source' h
      simp only [Function.iterate_zero_apply] at h
      cases Option.some.inj h
      exact ⟨StateTransition.EvalsToInTime.refl targetStep (encode source)⟩
  | succ steps ih =>
      intro source source' h
      rw [Function.iterate_succ_apply'] at h
      generalize hmid : ((flip bind sourceStep)^[steps]) (some source) = mid at h
      cases mid with
      | none =>
          simp at h
      | some middle =>
          have hstep : sourceStep middle = some source' := by
            simpa using h
          rcases ih source middle hmid with ⟨initialRun⟩
          rcases simulation hstep with ⟨finalRun⟩
          refine ⟨?_⟩
          simpa [Nat.mul_succ, Nat.add_comm, Nat.add_left_comm, Nat.add_assoc] using
            StateTransition.EvalsToInTime.trans targetStep
              (stepFactor * steps) stepFactor (encode source) (encode middle)
              (some (encode source')) initialRun finalRun

/--
A source run bounded by `sourceBound` translates to a target run bounded by
`stepFactor * sourceBound`.
-/
theorem fixedStepSimulation_transfer
    {Source Target : Type}
    {sourceStep : Source → Option Source} {targetStep : Target → Option Target}
    {encode : Source → Target} {stepFactor sourceBound : Nat}
    (simulation : FixedStepFunctionalSimulation sourceStep targetStep encode stepFactor)
    {source source' : Source}
    (run : StateTransition.EvalsToInTime sourceStep source (some source') sourceBound) :
    Nonempty (StateTransition.EvalsToInTime targetStep (encode source)
      (some (encode source')) (stepFactor * sourceBound)) := by
  rcases fixedStepSimulation_iterate simulation run.steps source source'
      run.evals_in_steps with ⟨translated⟩
  refine ⟨⟨translated.toEvalsTo, ?_⟩⟩
  exact translated.steps_le_m.trans
    (Nat.mul_le_mul_left stepFactor run.steps_le_m)

#print axioms fixedStepSimulation_iterate
#print axioms fixedStepSimulation_transfer

end MathSolve.PNP
