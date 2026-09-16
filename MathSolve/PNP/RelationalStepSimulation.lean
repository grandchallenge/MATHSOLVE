import Mathlib.Computability.StateTransition
import Mathlib.Tactic

/-!
# Bounded relational step simulation

The finite-TM2 to Programme compiler needs a relational invariant rather than a
total state encoder: internal TM2 stack symbols may live in non-finite carrier
types, while reachable cells are represented by finite provenance tokens.

A concrete compiler therefore proves that every related source/target state
pair advances to another related pair within a fixed number of target steps.
This file composes that local relation over complete bounded runs.
-/

namespace MathSolve.PNP

/-- A relational simulation with a uniform target-step bound per source step. -/
structure FixedStepRelationalSimulation {Source Target : Type}
    (sourceStep : Source → Option Source) (targetStep : Target → Option Target)
    (Rel : Source → Target → Prop) (stepFactor : Nat) : Prop where
  step : ∀ {source source' target}, Rel source target → sourceStep source = some source' →
    ∃ target', Rel source' target' ∧
      Nonempty (StateTransition.EvalsToInTime targetStep target (some target') stepFactor)
  halt : ∀ {source target}, Rel source target → sourceStep source = none →
    targetStep target = none

/-- Exact source iteration composes a bounded relational simulation. -/
theorem fixedStepRelationalSimulation_iterate
    {Source Target : Type}
    {sourceStep : Source → Option Source} {targetStep : Target → Option Target}
    {Rel : Source → Target → Prop} {stepFactor : Nat}
    (simulation : FixedStepRelationalSimulation sourceStep targetStep Rel stepFactor) :
    ∀ (steps : Nat) (source source' : Source) (target : Target),
      Rel source target →
      ((flip bind sourceStep)^[steps]) (some source) = some source' →
      ∃ target', Rel source' target' ∧
        Nonempty (StateTransition.EvalsToInTime targetStep target
          (some target') (stepFactor * steps)) := by
  intro steps
  induction steps with
  | zero =>
      intro source source' target hrel h
      simp only [Function.iterate_zero_apply] at h
      cases Option.some.inj h
      exact ⟨target, hrel, ⟨StateTransition.EvalsToInTime.refl targetStep target⟩⟩
  | succ steps ih =>
      intro source source' target hrel h
      rw [Function.iterate_succ_apply'] at h
      generalize hmid : ((flip bind sourceStep)^[steps]) (some source) = mid at h
      cases mid with
      | none =>
          simp at h
      | some middle =>
          have hstep : sourceStep middle = some source' := by
            simpa using h
          rcases ih source middle target hrel hmid with
            ⟨targetMiddle, hmiddle, ⟨initialRun⟩⟩
          rcases simulation.step hmiddle hstep with
            ⟨targetFinal, hfinal, ⟨finalRun⟩⟩
          refine ⟨targetFinal, hfinal, ⟨?_⟩⟩
          simpa [Nat.mul_succ, Nat.add_comm, Nat.add_left_comm, Nat.add_assoc] using
            StateTransition.EvalsToInTime.trans targetStep
              (stepFactor * steps) stepFactor target targetMiddle
              (some targetFinal) initialRun finalRun

/-- Transfer a source time bound through a bounded relational simulation. -/
theorem fixedStepRelationalSimulation_transfer
    {Source Target : Type}
    {sourceStep : Source → Option Source} {targetStep : Target → Option Target}
    {Rel : Source → Target → Prop} {stepFactor sourceBound : Nat}
    (simulation : FixedStepRelationalSimulation sourceStep targetStep Rel stepFactor)
    {source source' : Source} {target : Target}
    (hrel : Rel source target)
    (run : StateTransition.EvalsToInTime sourceStep source (some source') sourceBound) :
    ∃ target', Rel source' target' ∧
      Nonempty (StateTransition.EvalsToInTime targetStep target
        (some target') (stepFactor * sourceBound)) := by
  rcases fixedStepRelationalSimulation_iterate simulation run.steps source source' target
      hrel run.evals_in_steps with ⟨target', htarget, ⟨translated⟩⟩
  refine ⟨target', htarget, ⟨⟨translated.toEvalsTo, ?_⟩⟩⟩
  exact translated.steps_le_m.trans
    (Nat.mul_le_mul_left stepFactor run.steps_le_m)

#print axioms fixedStepRelationalSimulation_iterate
#print axioms fixedStepRelationalSimulation_transfer

end MathSolve.PNP
