import MathSolve.PNP.ProgrammeTM2TapeComposition
import MathSolve.PNP.ProgrammeTM2InitRun

/-! Arbitrary finite runs of the actual reverse machine, prior to cleanup. -/
namespace MathSolve.PNP
noncomputable section

/-- Arbitrary finite source runs are simulated in exactly the same number of
counted TM2 transitions. No target terminal-state hypothesis is used. -/
theorem programmeTM2_simulates_iterate (M : ProgrammeMachine) (input : List Bool) :
    ∀ (n : Nat) (source source' : ProgrammeConfig M) (target : ReverseCfg M),
      ProgrammeTM2Represents M input source target →
      ((flip bind (M.step input))^[n]) (some source) = some source' →
      ∃ target', ProgrammeTM2Represents M input source' target' ∧
        ((flip bind (programmeTM2Machine M).step)^[n]) (some target) = some target' := by
  intro n
  induction n with
  | zero =>
    intro source source' target hrep hs
    simp only [Function.iterate_zero_apply] at hs
    cases Option.some.inj hs
    exact ⟨target, hrep, rfl⟩
  | succ n ih =>
    intro source source' target hrep hs
    rw [Function.iterate_succ_apply'] at hs
    generalize hm : ((flip bind (M.step input))^[n]) (some source) = mid at hs
    cases mid with
    | none => simp [flip] at hs
    | some middle =>
      have hstep : M.step input middle = some source' := by simpa using hs
      rcases ih source middle target hrep hm with ⟨tm, hrm, htm⟩
      rcases programmeTM2_simulates_step hrm hstep with ⟨tf, htf, hrf⟩
      refine ⟨tf, hrf, ?_⟩
      rw [Function.iterate_succ_apply', htm]
      simpa using htf

/-- Transfer any source time bound into the same number of native run-phase
steps. Unlike a halting simulation, this theorem stops at the represented
source terminal state, before the target's mandatory output cleanup. -/
theorem programmeTM2_simulates_bounded_run {M : ProgrammeMachine} {input : List Bool}
    {source source' : ProgrammeConfig M} {target : ReverseCfg M} {bound : Nat}
    (hrep : ProgrammeTM2Represents M input source target)
    (hrun : StateTransition.EvalsToInTime (M.step input) source (some source') bound) :
    ∃ target', ProgrammeTM2Represents M input source' target' ∧
      Nonempty (StateTransition.EvalsToInTime (programmeTM2Machine M).step target (some target') bound) := by
  rcases programmeTM2_simulates_iterate M input hrun.steps source source' target hrep hrun.evals_in_steps with
    ⟨target', hrep', hsteps⟩
  exact ⟨target', hrep', ⟨{ steps := hrun.steps, evals_in_steps := hsteps, steps_le_m := hrun.steps_le_m }⟩⟩

/-- The original Boolean input is normalized and then simulated through every
source transition with an explicit initialization-plus-run time bound. -/
theorem programmeTM2_simulates_from_init {M : ProgrammeMachine} {input : List Bool}
    {source' : ProgrammeConfig M} {bound : Nat}
    (hrun : StateTransition.EvalsToInTime (M.step input) (M.init input) (some source') bound) :
    ∃ target', ProgrammeTM2Represents M input source' target' ∧
      Nonempty (StateTransition.EvalsToInTime (programmeTM2Machine M).step
        (Turing.initList (programmeTM2Machine M) input) (some target')
        (2 * input.length + 3 + bound)) := by
  rcases programmeTM2_initialization_run M input with ⟨hi⟩
  rcases programmeTM2_simulates_bounded_run (programmeTM2ReadyInitCfg_represents M input) hrun with
    ⟨target', hr, ⟨ht⟩⟩
  refine ⟨target', hr, ⟨?_⟩⟩
  simpa only [Nat.add_comm bound (2 * input.length + 3)] using
    (StateTransition.EvalsToInTime.trans (programmeTM2Machine M).step
      (2 * input.length + 3) bound _ _ (some target') hi ht)

#print axioms programmeTM2_simulates_iterate
#print axioms programmeTM2_simulates_bounded_run
#print axioms programmeTM2_simulates_from_init
end
end MathSolve.PNP
