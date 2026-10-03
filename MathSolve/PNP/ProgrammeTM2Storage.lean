import MathSolve.PNP.ProgrammeTM2StepPreservation

/-!
# Reverse-simulator finite storage measure

The Programme-to-TM2 simulator represents each two-way tape by two finite side
stacks and one scanned symbol.  This file tracks only the side-stack cells that
terminal cleanup must later remove.
-/

namespace MathSolve.PNP

noncomputable section

open Turing
open scoped BigOperators

/-- Explicit side-stack cells for the simulated immutable input tape. -/
def programmeTM2InputSideSize (M : ProgrammeMachine)
    (stk : ProgrammeTM2Stacks M) : Nat :=
  (stk .inputLeft).length + (stk .inputRight).length

/-- Explicit side-stack cells for one simulated work tape. -/
def programmeTM2WorkSideSize (M : ProgrammeMachine)
    (stk : ProgrammeTM2Stacks M) (tape : Fin M.workTapeCount) : Nat :=
  (stk (.workLeft tape)).length + (stk (.workRight tape)).length

/-- Total run-mode side-stack storage requiring terminal cleanup. -/
def programmeTM2RunStorage (M : ProgrammeMachine)
    (stk : ProgrammeTM2Stacks M) : Nat :=
  programmeTM2InputSideSize M stk +
    ∑ tape : Fin M.workTapeCount, programmeTM2WorkSideSize M stk tape

/-- Input movement increases explicit input-side storage by at most one cell. -/
theorem programmeTM2AfterInput_inputSideSize_le
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) :
    programmeTM2InputSideSize M
        (programmeTM2AfterInputStacks M s stk) ≤
      programmeTM2InputSideSize M stk + 1 := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove
  · cases hleft : stk .inputLeft <;>
      simp [programmeTM2InputSideSize, programmeTM2AfterInputStacks,
        hmove, Function.update, hleft] <;> omega
  · simp [programmeTM2InputSideSize, programmeTM2AfterInputStacks, hmove]
  · cases hright : stk .inputRight <;>
      simp [programmeTM2InputSideSize, programmeTM2AfterInputStacks,
        hmove, Function.update, hright] <;> omega

/-- Input movement does not change any work-side storage. -/
theorem programmeTM2AfterInput_workSideSize
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) (tape : Fin M.workTapeCount) :
    programmeTM2WorkSideSize M
        (programmeTM2AfterInputStacks M s stk) tape =
      programmeTM2WorkSideSize M stk tape := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
    simp [programmeTM2WorkSideSize, programmeTM2AfterInputStacks,
      hmove, Function.update]

/-- One work-tape update increases that tape's explicit side storage by at most
one cell. -/
theorem programmeTM2AfterWork_workSideSize_self_le
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2WorkSideSize M
        (programmeTM2AfterWorkStacks M tape s stk) tape ≤
      programmeTM2WorkSideSize M stk tape + 1 := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape
  · cases hleft : stk (.workLeft tape) <;>
      simp [programmeTM2WorkSideSize, programmeTM2AfterWorkStacks,
        hmove, Function.update, hleft] <;> omega
  · simp [programmeTM2WorkSideSize, programmeTM2AfterWorkStacks, hmove]
  · cases hright : stk (.workRight tape) <;>
      simp [programmeTM2WorkSideSize, programmeTM2AfterWorkStacks,
        hmove, Function.update, hright] <;> omega

/-- Updating one work tape leaves every different work-side size unchanged. -/
theorem programmeTM2AfterWork_workSideSize_ne
    (M : ProgrammeMachine) {tape other : Fin M.workTapeCount}
    (hne : other ≠ tape)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2WorkSideSize M
        (programmeTM2AfterWorkStacks M tape s stk) other =
      programmeTM2WorkSideSize M stk other := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2WorkSideSize, programmeTM2AfterWorkStacks,
      hmove, Function.update, hne]

/-- A single work-tape update increases the total run storage by at most one. -/
theorem programmeTM2AfterWork_storage_le
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2RunStorage M
        (programmeTM2AfterWorkStacks M tape s stk) ≤
      programmeTM2RunStorage M stk + 1 := by
  have hpoint :
      ∀ other : Fin M.workTapeCount,
        programmeTM2WorkSideSize M
            (programmeTM2AfterWorkStacks M tape s stk) other ≤
          programmeTM2WorkSideSize M stk other +
            (if other = tape then 1 else 0) := by
    intro other
    by_cases h : other = tape
    · subst other
      simpa using programmeTM2AfterWork_workSideSize_self_le M tape s stk
    · rw [programmeTM2AfterWork_workSideSize_ne M h s stk]
      simp [h]
  have hsum :
      (∑ other : Fin M.workTapeCount,
          programmeTM2WorkSideSize M
            (programmeTM2AfterWorkStacks M tape s stk) other) ≤
        (∑ other : Fin M.workTapeCount,
          programmeTM2WorkSideSize M stk other) + 1 := by
    calc
      (∑ other : Fin M.workTapeCount,
          programmeTM2WorkSideSize M
            (programmeTM2AfterWorkStacks M tape s stk) other) ≤
        ∑ other : Fin M.workTapeCount,
          (programmeTM2WorkSideSize M stk other +
            (if other = tape then 1 else 0)) := by
              exact Finset.sum_le_sum fun other _ => hpoint other
      _ = (∑ other : Fin M.workTapeCount,
            programmeTM2WorkSideSize M stk other) + 1 := by
              rw [Finset.sum_add_distrib]
              simp
  have hinput :
      programmeTM2InputSideSize M
          (programmeTM2AfterWorkStacks M tape s stk) =
        programmeTM2InputSideSize M stk := by
    cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
      simp [programmeTM2InputSideSize, programmeTM2AfterWorkStacks,
        hmove, Function.update]
  unfold programmeTM2RunStorage
  rw [hinput]
  omega

/-- The complete finite work phase increases storage by at most the number of
work-tape wrappers executed. -/
theorem programmeTM2WorkPhase_storage_le
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2RunStorage M
        (programmeTM2WorkPhase M tapes s stk).2 ≤
      programmeTM2RunStorage M stk + tapes.length := by
  induction tapes generalizing s stk with
  | nil =>
      simp [programmeTM2WorkPhase]
  | cons tape rest ih =>
      simp only [programmeTM2WorkPhase]
      have hrest :=
        ih (programmeTM2AfterWorkState M tape s stk)
          (programmeTM2AfterWorkStacks M tape s stk)
      have hone := programmeTM2AfterWork_storage_le M tape s stk
      simp only [List.length_cons]
      omega

/-- One complete simulated Programme run step increases cleanup storage by at
most one input-side cell plus one cell per work tape. -/
theorem programmeTM2RunCore_storage_le
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg) :
    programmeTM2RunStorage M (programmeTM2RunCore M target).2 ≤
      programmeTM2RunStorage M target.stk + (M.workTapeCount + 1) := by
  unfold programmeTM2RunCore
  let snapped := target.var.snapshot M
  let inputState := programmeTM2AfterInputState M snapped target.stk
  let inputStacks := programmeTM2AfterInputStacks M snapped target.stk
  have hinputSide :=
    programmeTM2AfterInput_inputSideSize_le M snapped target.stk
  have hworkSides :
      (∑ tape : Fin M.workTapeCount,
        programmeTM2WorkSideSize M inputStacks tape) =
        ∑ tape : Fin M.workTapeCount,
          programmeTM2WorkSideSize M target.stk tape := by
    apply Finset.sum_congr rfl
    intro tape _
    exact programmeTM2AfterInput_workSideSize M snapped target.stk tape
  have hinputStorage :
      programmeTM2RunStorage M inputStacks ≤
        programmeTM2RunStorage M target.stk + 1 := by
    unfold programmeTM2RunStorage
    rw [hworkSides]
    omega
  have hwork :=
    programmeTM2WorkPhase_storage_le M (programmeTM2WorkTapes M)
      inputState inputStacks
  simpa [programmeTM2WorkTapes] using
    le_trans hwork (by
      have hlen : (List.finRange M.workTapeCount).length =
          M.workTapeCount := by simp
      rw [hlen]
      omega : programmeTM2RunStorage M inputStacks + M.workTapeCount ≤
        programmeTM2RunStorage M target.stk + (M.workTapeCount + 1))

/-- Raw/temp/output stacks remain clean throughout run-mode simulation. -/
def ProgrammeTM2AncillaryClean (M : ProgrammeMachine)
    (stk : ProgrammeTM2Stacks M) : Prop :=
  stk .rawInput = [] ∧ stk .inputTemp = [] ∧ stk .output = []

theorem programmeTM2AfterInput_ancillaryClean
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M)
    (h : ProgrammeTM2AncillaryClean M stk) :
    ProgrammeTM2AncillaryClean M
      (programmeTM2AfterInputStacks M s stk) := by
  rcases h with ⟨hraw, htemp, hout⟩
  constructor
  · cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
      simp [programmeTM2AfterInputStacks, hmove, Function.update, hraw]
  constructor
  · cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
      simp [programmeTM2AfterInputStacks, hmove, Function.update, htemp]
  · cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
      simp [programmeTM2AfterInputStacks, hmove, Function.update, hout]

theorem programmeTM2AfterWork_ancillaryClean
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M)
    (h : ProgrammeTM2AncillaryClean M stk) :
    ProgrammeTM2AncillaryClean M
      (programmeTM2AfterWorkStacks M tape s stk) := by
  rcases h with ⟨hraw, htemp, hout⟩
  constructor
  · cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
      simp [programmeTM2AfterWorkStacks, hmove, Function.update, hraw]
  constructor
  · cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
      simp [programmeTM2AfterWorkStacks, hmove, Function.update, htemp]
  · cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
      simp [programmeTM2AfterWorkStacks, hmove, Function.update, hout]

theorem programmeTM2WorkPhase_ancillaryClean
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M)
    (h : ProgrammeTM2AncillaryClean M stk) :
    ProgrammeTM2AncillaryClean M
      (programmeTM2WorkPhase M tapes s stk).2 := by
  induction tapes generalizing s stk with
  | nil =>
      exact h
  | cons tape rest ih =>
      simp only [programmeTM2WorkPhase]
      exact ih _ _ (programmeTM2AfterWork_ancillaryClean M tape s stk h)

/-- Run-core execution preserves the clean ancillary-stack invariant. -/
theorem programmeTM2RunCore_ancillaryClean
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg)
    (h : ProgrammeTM2AncillaryClean M target.stk) :
    ProgrammeTM2AncillaryClean M (programmeTM2RunCore M target).2 := by
  unfold programmeTM2RunCore
  let snapped := target.var.snapshot M
  let inputState := programmeTM2AfterInputState M snapped target.stk
  let inputStacks := programmeTM2AfterInputStacks M snapped target.stk
  apply programmeTM2WorkPhase_ancillaryClean M
  exact programmeTM2AfterInput_ancillaryClean M snapped target.stk h

/-- The initialized run configuration starts with at most one explicit
side-stack cell per remaining input bit. -/
theorem programmeTM2ReadyInitCfg_storage_le
    (M : ProgrammeMachine) (input : List Bool) :
    programmeTM2RunStorage M (programmeTM2ReadyInitCfg M input).stk ≤
      input.length := by
  simp [programmeTM2RunStorage, programmeTM2InputSideSize,
    programmeTM2WorkSideSize, programmeTM2ReadyInitCfg,
    programmeTM2InitStacks]
  omega

/-- Reverse initialization leaves raw/temp/output stacks empty. -/
theorem programmeTM2ReadyInitCfg_ancillaryClean
    (M : ProgrammeMachine) (input : List Bool) :
    ProgrammeTM2AncillaryClean M (programmeTM2ReadyInitCfg M input).stk := by
  simp [ProgrammeTM2AncillaryClean, programmeTM2ReadyInitCfg,
    programmeTM2InitStacks]

/-- The counted run-step target satisfies the same one-step storage bound as
its pure operational normal form. -/
theorem programmeTM2RunStepTarget_storage_le
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg) :
    programmeTM2RunStorage M (programmeTM2RunStepTarget M target).stk ≤
      programmeTM2RunStorage M target.stk + (M.workTapeCount + 1) := by
  rw [programmeTM2RunStepTarget_eq_core]
  exact programmeTM2RunCore_storage_le M target

/-- The counted run-step target preserves clean ancillary stacks. -/
theorem programmeTM2RunStepTarget_ancillaryClean
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg)
    (h : ProgrammeTM2AncillaryClean M target.stk) :
    ProgrammeTM2AncillaryClean M (programmeTM2RunStepTarget M target).stk := by
  rw [programmeTM2RunStepTarget_eq_core]
  exact programmeTM2RunCore_ancillaryClean M target h

/-- Strengthened reverse run relation used by the quantitative compiler. -/
def ProgrammeTM2RunRep (M : ProgrammeMachine) (input : List Bool)
    (source : ProgrammeConfig M) (target : (programmeTM2Machine M).Cfg) : Prop :=
  ProgrammeTM2Represents M input source target ∧
    ProgrammeTM2AncillaryClean M target.stk

/-- The exact post-initialization target satisfies the strengthened run relation. -/
theorem programmeTM2ReadyInitCfg_runRep
    (M : ProgrammeMachine) (input : List Bool) :
    ProgrammeTM2RunRep M input (M.init input)
      (programmeTM2ReadyInitCfg M input) := by
  exact ⟨programmeTM2ReadyInitCfg_represents M input,
    programmeTM2ReadyInitCfg_ancillaryClean M input⟩

/-- One source Programme step becomes one counted TM2 step, preserves the
strengthened relation, and increases cleanup storage by at most
`workTapeCount + 1`. -/
theorem programmeTM2_runRep_step
    {M : ProgrammeMachine} {input : List Bool}
    {source source' : ProgrammeConfig M}
    {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2RunRep M input source target)
    (hstep : M.step input source = some source') :
    ProgrammeTM2RunRep M input source'
        (programmeTM2RunStepTarget M target) ∧
      (programmeTM2Machine M).step target =
        some (programmeTM2RunStepTarget M target) ∧
      programmeTM2RunStorage M (programmeTM2RunStepTarget M target).stk ≤
        programmeTM2RunStorage M target.stk + (M.workTapeCount + 1) := by
  rcases hrep with ⟨hrepresented, hclean⟩
  have haccept : source.state ≠ M.accept := by
    intro h
    rw [M.step_eq_none_of_accept input source h] at hstep
    contradiction
  have hreject : source.state ≠ M.reject := by
    intro h
    rw [M.step_eq_none_of_reject input source h] at hstep
    contradiction
  have hsource :
      source' = source.afterAction (M.actionAt input source) := by
    have hs := M.step_eq_some_afterAction input source haccept hreject
    rw [hs] at hstep
    exact (Option.some.inj hstep).symm
  have htargetRep :
      ProgrammeTM2Represents M input source'
        (programmeTM2RunStepTarget M target) := by
    subst source'
    exact programmeTM2RunStepTarget_represents_afterAction hrepresented
  exact
    ⟨⟨htargetRep,
        programmeTM2RunStepTarget_ancillaryClean M target hclean⟩,
      programmeTM2_step_run_nonterminal hrepresented haccept hreject,
      programmeTM2RunStepTarget_storage_le M target⟩

/-- Exact source iteration lifts to the reverse simulator while carrying the
finite cleanup-storage bound. -/
theorem programmeTM2_runRep_iterate
    (M : ProgrammeMachine) (input : List Bool) :
    ∀ (steps : Nat) (source source' : ProgrammeConfig M)
      (target : (programmeTM2Machine M).Cfg),
      ProgrammeTM2RunRep M input source target →
      ((flip bind (M.step input))^[steps]) (some source) = some source' →
      ∃ target',
        ProgrammeTM2RunRep M input source' target' ∧
        Nonempty
          (StateTransition.EvalsToInTime
            (programmeTM2Machine M).step target (some target') steps) ∧
        programmeTM2RunStorage M target'.stk ≤
          programmeTM2RunStorage M target.stk +
            (M.workTapeCount + 1) * steps := by
  intro steps
  induction steps with
  | zero =>
      intro source source' target hrep hiter
      simp only [Function.iterate_zero_apply] at hiter
      cases Option.some.inj hiter
      exact ⟨target, hrep,
        ⟨StateTransition.EvalsToInTime.refl
          (programmeTM2Machine M).step target⟩,
        by simp⟩
  | succ steps ih =>
      intro source source' target hrep hiter
      rw [Function.iterate_succ_apply'] at hiter
      generalize hmid :
          ((flip bind (M.step input))^[steps]) (some source) = mid
        at hiter
      cases mid with
      | none =>
          simp [flip] at hiter
      | some middle =>
          have hlast : M.step input middle = some source' := by
            simpa using hiter
          rcases ih source middle target hrep hmid with
            ⟨targetMiddle, hmiddleRep, ⟨hrun⟩, hstorageMiddle⟩
          rcases programmeTM2_runRep_step hmiddleRep hlast with
            ⟨hfinalRep, htargetStep, hstorageStep⟩
          have hone := programmeTM2_one_step_in_time htargetStep
          have htime :=
            StateTransition.EvalsToInTime.trans
              (programmeTM2Machine M).step
              steps 1 target targetMiddle
              (some (programmeTM2RunStepTarget M targetMiddle))
              hrun hone
          refine ⟨programmeTM2RunStepTarget M targetMiddle,
            hfinalRep, ⟨?_⟩, ?_⟩
          · simpa [Nat.add_comm] using htime
          · simp only [Nat.mul_succ]
            omega

/-- Transfer a bounded Programme run into an equally bounded counted TM2 run,
with explicit cleanup-storage growth. -/
theorem programmeTM2_runRep_transfer
    {M : ProgrammeMachine} {input : List Bool}
    {source source' : ProgrammeConfig M}
    {target : (programmeTM2Machine M).Cfg}
    {sourceBound : Nat}
    (hrep : ProgrammeTM2RunRep M input source target)
    (run :
      StateTransition.EvalsToInTime
        (M.step input) source (some source') sourceBound) :
    ∃ target',
      ProgrammeTM2RunRep M input source' target' ∧
      Nonempty
        (StateTransition.EvalsToInTime
          (programmeTM2Machine M).step target (some target') sourceBound) ∧
      programmeTM2RunStorage M target'.stk ≤
        programmeTM2RunStorage M target.stk +
          (M.workTapeCount + 1) * sourceBound := by
  rcases programmeTM2_runRep_iterate M input run.steps
      source source' target hrep run.evals_in_steps with
    ⟨target', htargetRep, ⟨hrun⟩, hstorage⟩
  refine ⟨target', htargetRep, ⟨?_⟩, ?_⟩
  · exact programmeTM2_evalsToInTime_mono hrun run.steps_le_m
  · exact hstorage.trans (by
      have hmul :
          (M.workTapeCount + 1) * run.steps ≤
            (M.workTapeCount + 1) * sourceBound :=
        Nat.mul_le_mul_left _ run.steps_le_m
      omega)

#print axioms programmeTM2ReadyInitCfg_storage_le
#print axioms programmeTM2RunStepTarget_storage_le
#print axioms programmeTM2_runRep_step
#print axioms programmeTM2_runRep_iterate
#print axioms programmeTM2_runRep_transfer

#print axioms programmeTM2AfterInput_inputSideSize_le
#print axioms programmeTM2AfterWork_storage_le
#print axioms programmeTM2WorkPhase_storage_le
#print axioms programmeTM2RunCore_storage_le
#print axioms programmeTM2RunCore_ancillaryClean

end

end MathSolve.PNP
