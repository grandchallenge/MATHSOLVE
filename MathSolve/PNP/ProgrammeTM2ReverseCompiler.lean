import MathSolve.PNP.ProgrammeTM2TerminalCleanup
import MathSolve.PNP.ModelBridge

/-!
# Quantitative Programme-to-TM2 compiler

This file closes the reverse half of PNP-BRIDGE-MODEL-001 by composing the
already-proved initialization, one-step run transfer, and terminal cleanup.
-/

namespace MathSolve.PNP

noncomputable section

/-- Exact composed reverse budget for an input length and a source step budget. -/
def programmeTM2TotalBudget (M : ProgrammeMachine)
    (inputLength sourceSteps : Nat) : Nat :=
  2 * inputLength + 3 + sourceSteps +
    programmeTM2CleanupBudget M inputLength sourceSteps

/-- Reverse target runtime induced by one Programme decider. -/
def programmeTM2ReverseRuntime {decision : List Bool → Bool}
    (source : ProgrammeDecider decision) : BinaryRuntimeCost :=
  fun input =>
    programmeTM2TotalBudget source.machine input.length (source.runtime input)

/-- The composed reverse budget is monotone in the source-step argument. -/
theorem programmeTM2TotalBudget_mono
    (M : ProgrammeMachine) (inputLength : Nat) {s t : Nat}
    (hst : s ≤ t) :
    programmeTM2TotalBudget M inputLength s ≤
      programmeTM2TotalBudget M inputLength t := by
  have hw :
      2 * M.workTapeCount * (s + 1) ≤
        2 * M.workTapeCount * (t + 1) := by
    exact Nat.mul_le_mul_left (2 * M.workTapeCount)
      (Nat.add_le_add_right hst 1)
  unfold programmeTM2TotalBudget programmeTM2CleanupBudget
  omega

/-- The reverse machine computes the same Boolean decision within the exact
translated runtime. -/
def programmeTM2Machine_outputs
    {decision : List Bool → Bool}
    (source : ProgrammeDecider decision) (input : List Bool) :
    StateTransition.EvalsToInTime
      (programmeTM2Machine source.machine).step
      (Turing.initList (programmeTM2Machine source.machine) input)
      (some
        (Turing.haltList (programmeTM2Machine source.machine)
          [decision input]))
      (programmeTM2ReverseRuntime source input) := by
  let terminal : ProgrammeConfig source.machine :=
    Classical.choose (source.outputs input)
  have hspec := Classical.choose_spec (source.outputs input)
  let hsource :
      StateTransition.EvalsToInTime
        (source.machine.step input)
        (source.machine.init input)
        (some terminal)
        (source.runtime input) :=
    Classical.choice hspec.1
  have hnone : source.machine.step input terminal = none := hspec.2.1
  have hout : source.machine.output terminal = some (decision input) := hspec.2.2
  let hinit :
      StateTransition.EvalsToInTime
        (programmeTM2Machine source.machine).step
        (Turing.initList (programmeTM2Machine source.machine) input)
        (some (programmeTM2ReadyInitCfg source.machine input))
        (2 * input.length + 3) :=
    Classical.choice (programmeTM2_initialization_run source.machine input)
  let htransfer :=
    programmeTM2_transfer_run source.machine input hsource
  let target : (programmeTM2Machine source.machine).Cfg :=
    Classical.choose htransfer
  have htransferSpec := Classical.choose_spec htransfer
  have hrep := htransferSpec.1
  let hrun :
      StateTransition.EvalsToInTime
        (programmeTM2Machine source.machine).step
        (programmeTM2ReadyInitCfg source.machine input)
        (some target)
        hsource.steps :=
    Classical.choice htransferSpec.2
  let hcleanup :
      StateTransition.EvalsToInTime
        (programmeTM2Machine source.machine).step
        target
        (some
          (Turing.haltList (programmeTM2Machine source.machine)
            [decision input]))
        (programmeTM2CleanupBudget source.machine input.length hsource.steps) :=
    Classical.choice
      (programmeTM2_cleanup_terminal hrep hnone
        (decision input) hout)
  have hprefix :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine source.machine).step
      (2 * input.length + 3) hsource.steps
      (Turing.initList (programmeTM2Machine source.machine) input)
      (programmeTM2ReadyInitCfg source.machine input)
      (some target)
      hinit hrun
  have hprefixBound :
      hsource.steps + (2 * input.length + 3) =
        2 * input.length + 3 + hsource.steps := by
    omega
  have hprefix' :
      StateTransition.EvalsToInTime
        (programmeTM2Machine source.machine).step
        (Turing.initList (programmeTM2Machine source.machine) input)
        (some target)
        (2 * input.length + 3 + hsource.steps) :=
    hprefixBound ▸ hprefix
  have hall :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine source.machine).step
      (2 * input.length + 3 + hsource.steps)
      (programmeTM2CleanupBudget source.machine input.length hsource.steps)
      (Turing.initList (programmeTM2Machine source.machine) input)
      target
      (some
        (Turing.haltList (programmeTM2Machine source.machine)
          [decision input]))
      hprefix' hcleanup
  have hbudget :
      programmeTM2CleanupBudget source.machine input.length hsource.steps +
          (2 * input.length + 3 + hsource.steps) =
        programmeTM2TotalBudget source.machine input.length hsource.steps := by
    unfold programmeTM2TotalBudget
    omega
  have hexact :
      StateTransition.EvalsToInTime
        (programmeTM2Machine source.machine).step
        (Turing.initList (programmeTM2Machine source.machine) input)
        (some
          (Turing.haltList (programmeTM2Machine source.machine)
            [decision input]))
        (programmeTM2TotalBudget source.machine input.length hsource.steps) :=
    hbudget ▸ hall
  have hwiden :=
    programmeTM2_evalsToInTime_mono hexact
      (programmeTM2TotalBudget_mono source.machine input.length
        hsource.steps_le_m)
  exact hwiden

/-- Concrete exact-timed imported TM2 decider emitted by the reverse compiler. -/
def programmeTM2TimedDecider {decision : List Bool → Bool}
    (source : ProgrammeDecider decision) :
    ImportedTM2TimedDecider decision where
  tm := programmeTM2Machine source.machine
  inputAlphabet := Equiv.refl Bool
  outputAlphabet := Equiv.refl Bool
  runtime := programmeTM2ReverseRuntime source
  outputsFun := by
    intro input
    change StateTransition.EvalsToInTime
      (programmeTM2Machine source.machine).step
      (Turing.initList (programmeTM2Machine source.machine)
        (List.map (fun b : Bool => b) input))
      (some
        (Turing.haltList (programmeTM2Machine source.machine)
          (List.map (fun b : Bool => b)
            (Computability.encodeBool (decision input)))))
      (programmeTM2ReverseRuntime source input)
    have hmap :
        List.map (fun b : Bool => b) input = input := by
      induction input with
      | nil => rfl
      | cons b rest ih =>
          simp [ih]
    rw [hmap]
    simpa [Computability.encodeBool] using
      programmeTM2Machine_outputs source input

/-- The exact reverse runtime is affine in input length and source runtime. -/
theorem programmeTM2ReverseRuntime_affine
    {decision : List Bool → Bool}
    (source : ProgrammeDecider decision) :
    AffineSimulationOverhead source.runtime
      (programmeTM2ReverseRuntime source) := by
  let w := source.machine.workTapeCount
  refine ⟨9 + 2 * w, 3, 3 + 2 * w, ?_⟩
  intro input
  apply le_of_eq
  unfold programmeTM2ReverseRuntime programmeTM2TotalBudget
    programmeTM2CleanupBudget
  dsimp [w]
  ring

/-- Construct the quantitative Programme-to-FinTM2 compiler required by the
model bridge. -/
theorem programmeToTM2Compiler_constructive :
    ProgrammeToTM2Compiler := by
  intro decision source
  exact ⟨programmeTM2TimedDecider source,
    programmeTM2ReverseRuntime_affine source⟩

#print axioms programmeTM2TotalBudget_mono
#print axioms programmeTM2Machine_outputs
#print axioms programmeTM2ReverseRuntime_affine
#print axioms programmeToTM2Compiler_constructive

end

end MathSolve.PNP
