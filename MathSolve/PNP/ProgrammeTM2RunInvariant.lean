import MathSolve.PNP.ProgrammeTM2StepPreservation
import MathSolve.PNP.ProgrammeTM2InitRepresentation

/-!
# Quantitative run invariant for the reverse Programme-to-TM2 compiler

The semantic representation is strengthened with exact auxiliary-stack
emptiness and simple per-side length bounds.  Starting from the normalized
initial configuration, one simulated Programme step can increase each
left/right tape-side stack by at most one cell.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Quantitative representation after at most `steps` simulated Programme
transitions. -/
structure ProgrammeTM2BoundedRepresents
    (M : ProgrammeMachine) (input : List Bool)
    (source : ProgrammeConfig M) (target : (programmeTM2Machine M).Cfg)
    (steps : Nat) : Prop where
  represents : ProgrammeTM2Represents M input source target
  raw_empty : target.stk .rawInput = []
  temp_empty : target.stk .inputTemp = []
  output_empty : target.stk .output = []
  inputLeft_bound : (target.stk .inputLeft).length ≤ steps
  inputRight_bound : (target.stk .inputRight).length ≤ input.length + steps
  workLeft_bound :
    ∀ tape : Fin M.workTapeCount,
      (target.stk (.workLeft tape)).length ≤ steps
  workRight_bound :
    ∀ tape : Fin M.workTapeCount,
      (target.stk (.workRight tape)).length ≤ steps

/-- Input movement can grow either explicit input side by at most one cell. -/
theorem programmeTM2AfterInput_inputLeft_length_le
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) :
    ((programmeTM2AfterInputStacks M s stk) .inputLeft).length ≤
      (stk .inputLeft).length + 1 := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
    simp [programmeTM2AfterInputStacks, hmove, Function.update] <;> omega

theorem programmeTM2AfterInput_inputRight_length_le
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) :
    ((programmeTM2AfterInputStacks M s stk) .inputRight).length ≤
      (stk .inputRight).length + 1 := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
    simp [programmeTM2AfterInputStacks, hmove, Function.update] <;> omega

/-- Input movement does not touch auxiliary or work stacks. -/
theorem programmeTM2AfterInput_raw
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) :
    programmeTM2AfterInputStacks M s stk .rawInput = stk .rawInput := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
    simp [programmeTM2AfterInputStacks, hmove, Function.update]

theorem programmeTM2AfterInput_temp
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) :
    programmeTM2AfterInputStacks M s stk .inputTemp = stk .inputTemp := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
    simp [programmeTM2AfterInputStacks, hmove, Function.update]

theorem programmeTM2AfterInput_output
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) :
    programmeTM2AfterInputStacks M s stk .output = stk .output := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
    simp [programmeTM2AfterInputStacks, hmove, Function.update]

theorem programmeTM2AfterInput_workLeft
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) (tape : Fin M.workTapeCount) :
    programmeTM2AfterInputStacks M s stk (.workLeft tape) =
      stk (.workLeft tape) := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
    simp [programmeTM2AfterInputStacks, hmove, Function.update]

theorem programmeTM2AfterInput_workRight
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) (tape : Fin M.workTapeCount) :
    programmeTM2AfterInputStacks M s stk (.workRight tape) =
      stk (.workRight tape) := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
    simp [programmeTM2AfterInputStacks, hmove, Function.update]

/-- One work action grows either side of its selected work tape by at most one. -/
theorem programmeTM2AfterWork_workLeft_length_le
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    ((programmeTM2AfterWorkStacks M tape s stk) (.workLeft tape)).length ≤
      (stk (.workLeft tape)).length + 1 := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2AfterWorkStacks, hmove, Function.update] <;> omega

theorem programmeTM2AfterWork_workRight_length_le
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    ((programmeTM2AfterWorkStacks M tape s stk) (.workRight tape)).length ≤
      (stk (.workRight tape)).length + 1 := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2AfterWorkStacks, hmove, Function.update] <;> omega

/-- A work action on a different tape leaves the requested side unchanged. -/
theorem programmeTM2AfterWork_workLeft_ne
    (M : ProgrammeMachine) {tape other : Fin M.workTapeCount}
    (hne : other ≠ tape)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2AfterWorkStacks M tape s stk (.workLeft other) =
      stk (.workLeft other) := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2AfterWorkStacks, hmove, Function.update, hne]

theorem programmeTM2AfterWork_workRight_ne
    (M : ProgrammeMachine) {tape other : Fin M.workTapeCount}
    (hne : other ≠ tape)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2AfterWorkStacks M tape s stk (.workRight other) =
      stk (.workRight other) := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2AfterWorkStacks, hmove, Function.update, hne]

/-- Work actions do not touch the non-work stack families. -/
theorem programmeTM2AfterWork_raw
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2AfterWorkStacks M tape s stk .rawInput = stk .rawInput := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2AfterWorkStacks, hmove, Function.update]

theorem programmeTM2AfterWork_temp
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2AfterWorkStacks M tape s stk .inputTemp = stk .inputTemp := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2AfterWorkStacks, hmove, Function.update]

theorem programmeTM2AfterWork_output
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2AfterWorkStacks M tape s stk .output = stk .output := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2AfterWorkStacks, hmove, Function.update]

theorem programmeTM2AfterWork_inputLeft
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2AfterWorkStacks M tape s stk .inputLeft = stk .inputLeft := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2AfterWorkStacks, hmove, Function.update]

theorem programmeTM2AfterWork_inputRight
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    programmeTM2AfterWorkStacks M tape s stk .inputRight = stk .inputRight := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2AfterWorkStacks, hmove, Function.update]

/-- A work phase that does not contain a tape leaves its raw side lists unchanged. -/
theorem programmeTM2WorkPhase_workLeft_of_not_mem
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M)
    (targetTape : Fin M.workTapeCount) (hnot : targetTape ∉ tapes) :
    (programmeTM2WorkPhase M tapes s stk).2 (.workLeft targetTape) =
      stk (.workLeft targetTape) := by
  induction tapes generalizing s stk with
  | nil => rfl
  | cons tape rest ih =>
      have hne : targetTape ≠ tape := by
        intro h; subst targetTape; exact hnot (by simp)
      have hrest : targetTape ∉ rest := by
        intro h; exact hnot (by simp [h])
      simp only [programmeTM2WorkPhase]
      rw [ih _ _ hrest]
      exact programmeTM2AfterWork_workLeft_ne M hne s stk

theorem programmeTM2WorkPhase_workRight_of_not_mem
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M)
    (targetTape : Fin M.workTapeCount) (hnot : targetTape ∉ tapes) :
    (programmeTM2WorkPhase M tapes s stk).2 (.workRight targetTape) =
      stk (.workRight targetTape) := by
  induction tapes generalizing s stk with
  | nil => rfl
  | cons tape rest ih =>
      have hne : targetTape ≠ tape := by
        intro h; subst targetTape; exact hnot (by simp)
      have hrest : targetTape ∉ rest := by
        intro h; exact hnot (by simp [h])
      simp only [programmeTM2WorkPhase]
      rw [ih _ _ hrest]
      exact programmeTM2AfterWork_workRight_ne M hne s stk

/-- In a duplicate-free work phase, one listed tape side grows by at most one. -/
theorem programmeTM2WorkPhase_workLeft_length_le
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (hnodup : tapes.Nodup)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M)
    (targetTape : Fin M.workTapeCount) (hmem : targetTape ∈ tapes) :
    ((programmeTM2WorkPhase M tapes s stk).2 (.workLeft targetTape)).length ≤
      (stk (.workLeft targetTape)).length + 1 := by
  induction tapes generalizing s stk with
  | nil => simp at hmem
  | cons tape rest ih =>
      rw [List.nodup_cons] at hnodup
      rcases hnodup with ⟨htapeNot, hrestNodup⟩
      rcases List.mem_cons.mp hmem with hEq | hmemRest
      · subst targetTape
        simp only [programmeTM2WorkPhase]
        rw [programmeTM2WorkPhase_workLeft_of_not_mem M rest _ _ tape htapeNot]
        exact programmeTM2AfterWork_workLeft_length_le M tape s stk
      · have hne : targetTape ≠ tape := by
          intro h; subst targetTape; exact htapeNot hmemRest
        simp only [programmeTM2WorkPhase]
        have hrec := ih hrestNodup
          (programmeTM2AfterWorkState M tape s stk)
          (programmeTM2AfterWorkStacks M tape s stk) hmemRest
        rw [programmeTM2AfterWork_workLeft_ne M hne s stk] at hrec
        exact hrec

theorem programmeTM2WorkPhase_workRight_length_le
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (hnodup : tapes.Nodup)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M)
    (targetTape : Fin M.workTapeCount) (hmem : targetTape ∈ tapes) :
    ((programmeTM2WorkPhase M tapes s stk).2 (.workRight targetTape)).length ≤
      (stk (.workRight targetTape)).length + 1 := by
  induction tapes generalizing s stk with
  | nil => simp at hmem
  | cons tape rest ih =>
      rw [List.nodup_cons] at hnodup
      rcases hnodup with ⟨htapeNot, hrestNodup⟩
      rcases List.mem_cons.mp hmem with hEq | hmemRest
      · subst targetTape
        simp only [programmeTM2WorkPhase]
        rw [programmeTM2WorkPhase_workRight_of_not_mem M rest _ _ tape htapeNot]
        exact programmeTM2AfterWork_workRight_length_le M tape s stk
      · have hne : targetTape ≠ tape := by
          intro h; subst targetTape; exact htapeNot hmemRest
        simp only [programmeTM2WorkPhase]
        have hrec := ih hrestNodup
          (programmeTM2AfterWorkState M tape s stk)
          (programmeTM2AfterWorkStacks M tape s stk) hmemRest
        rw [programmeTM2AfterWork_workRight_ne M hne s stk] at hrec
        exact hrec

/-- The work phase leaves all auxiliary/input stacks unchanged. -/
theorem programmeTM2WorkPhase_raw
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    (programmeTM2WorkPhase M tapes s stk).2 .rawInput = stk .rawInput := by
  induction tapes generalizing s stk with
  | nil => rfl
  | cons tape rest ih =>
      simp only [programmeTM2WorkPhase]
      rw [ih]
      exact programmeTM2AfterWork_raw M tape s stk

theorem programmeTM2WorkPhase_temp
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    (programmeTM2WorkPhase M tapes s stk).2 .inputTemp = stk .inputTemp := by
  induction tapes generalizing s stk with
  | nil => rfl
  | cons tape rest ih =>
      simp only [programmeTM2WorkPhase]
      rw [ih]
      exact programmeTM2AfterWork_temp M tape s stk

theorem programmeTM2WorkPhase_output
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    (programmeTM2WorkPhase M tapes s stk).2 .output = stk .output := by
  induction tapes generalizing s stk with
  | nil => rfl
  | cons tape rest ih =>
      simp only [programmeTM2WorkPhase]
      rw [ih]
      exact programmeTM2AfterWork_output M tape s stk

theorem programmeTM2WorkPhase_inputLeft
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    (programmeTM2WorkPhase M tapes s stk).2 .inputLeft = stk .inputLeft := by
  induction tapes generalizing s stk with
  | nil => rfl
  | cons tape rest ih =>
      simp only [programmeTM2WorkPhase]
      rw [ih]
      exact programmeTM2AfterWork_inputLeft M tape s stk

theorem programmeTM2WorkPhase_inputRight
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    (programmeTM2WorkPhase M tapes s stk).2 .inputRight = stk .inputRight := by
  induction tapes generalizing s stk with
  | nil => rfl
  | cons tape rest ih =>
      simp only [programmeTM2WorkPhase]
      rw [ih]
      exact programmeTM2AfterWork_inputRight M tape s stk

/-- Raw-stack facts for the complete run core. -/
theorem programmeTM2RunCore_raw
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg) :
    (programmeTM2RunCore M target).2 .rawInput = target.stk .rawInput := by
  unfold programmeTM2RunCore
  rw [programmeTM2WorkPhase_raw]
  exact programmeTM2AfterInput_raw M (target.var.snapshot M) target.stk

theorem programmeTM2RunCore_temp
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg) :
    (programmeTM2RunCore M target).2 .inputTemp = target.stk .inputTemp := by
  unfold programmeTM2RunCore
  rw [programmeTM2WorkPhase_temp]
  exact programmeTM2AfterInput_temp M (target.var.snapshot M) target.stk

theorem programmeTM2RunCore_output
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg) :
    (programmeTM2RunCore M target).2 .output = target.stk .output := by
  unfold programmeTM2RunCore
  rw [programmeTM2WorkPhase_output]
  exact programmeTM2AfterInput_output M (target.var.snapshot M) target.stk

theorem programmeTM2RunCore_inputLeft_length_le
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg) :
    ((programmeTM2RunCore M target).2 .inputLeft).length ≤
      (target.stk .inputLeft).length + 1 := by
  unfold programmeTM2RunCore
  rw [programmeTM2WorkPhase_inputLeft]
  exact programmeTM2AfterInput_inputLeft_length_le
    M (target.var.snapshot M) target.stk

theorem programmeTM2RunCore_inputRight_length_le
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg) :
    ((programmeTM2RunCore M target).2 .inputRight).length ≤
      (target.stk .inputRight).length + 1 := by
  unfold programmeTM2RunCore
  rw [programmeTM2WorkPhase_inputRight]
  exact programmeTM2AfterInput_inputRight_length_le
    M (target.var.snapshot M) target.stk

theorem programmeTM2RunCore_workLeft_length_le
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg)
    (tape : Fin M.workTapeCount) :
    ((programmeTM2RunCore M target).2 (.workLeft tape)).length ≤
      (target.stk (.workLeft tape)).length + 1 := by
  unfold programmeTM2RunCore
  let snapped := target.var.snapshot M
  let inputState := programmeTM2AfterInputState M snapped target.stk
  let inputStacks := programmeTM2AfterInputStacks M snapped target.stk
  have hphase :=
    programmeTM2WorkPhase_workLeft_length_le M
      (programmeTM2WorkTapes M) (List.nodup_finRange M.workTapeCount)
      inputState inputStacks tape (List.mem_finRange tape)
  have hinput :
      inputStacks (.workLeft tape) = target.stk (.workLeft tape) := by
    exact programmeTM2AfterInput_workLeft M snapped target.stk tape
  rw [hinput] at hphase
  exact hphase

theorem programmeTM2RunCore_workRight_length_le
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg)
    (tape : Fin M.workTapeCount) :
    ((programmeTM2RunCore M target).2 (.workRight tape)).length ≤
      (target.stk (.workRight tape)).length + 1 := by
  unfold programmeTM2RunCore
  let snapped := target.var.snapshot M
  let inputState := programmeTM2AfterInputState M snapped target.stk
  let inputStacks := programmeTM2AfterInputStacks M snapped target.stk
  have hphase :=
    programmeTM2WorkPhase_workRight_length_le M
      (programmeTM2WorkTapes M) (List.nodup_finRange M.workTapeCount)
      inputState inputStacks tape (List.mem_finRange tape)
  have hinput :
      inputStacks (.workRight tape) = target.stk (.workRight tape) := by
    exact programmeTM2AfterInput_workRight M snapped target.stk tape
  rw [hinput] at hphase
  exact hphase

/-- The ready reverse-simulator configuration satisfies the zero-step bounds. -/
theorem programmeTM2ReadyInitCfg_bounded
    (M : ProgrammeMachine) (input : List Bool) :
    ProgrammeTM2BoundedRepresents M input (M.init input)
      (programmeTM2ReadyInitCfg M input) 0 := by
  refine
    { represents := programmeTM2ReadyInitCfg_represents M input
      raw_empty := ?_
      temp_empty := ?_
      output_empty := ?_
      inputLeft_bound := ?_
      inputRight_bound := ?_
      workLeft_bound := ?_
      workRight_bound := ?_ }
  · rfl
  · rfl
  · rfl
  · rfl
  · cases input with
    | nil =>
        simp [programmeTM2ReadyInitCfg, programmeTM2InitStacks]
    | cons bit tail =>
        simp [programmeTM2ReadyInitCfg, programmeTM2InitStacks]
  · intro tape; rfl
  · intro tape; rfl

/-- One Programme transition preserves the strengthened relation and increments
all side-length budgets by one. -/
theorem programmeTM2_bounded_step
    {M : ProgrammeMachine} {input : List Bool}
    {source source' : ProgrammeConfig M}
    {target : (programmeTM2Machine M).Cfg} {steps : Nat}
    (hrep : ProgrammeTM2BoundedRepresents M input source target steps)
    (hstep : M.step input source = some source') :
    ∃ target',
      ProgrammeTM2BoundedRepresents M input source' target' (steps + 1) ∧
      (programmeTM2Machine M).step target = some target' := by
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
    have h := M.step_eq_some_afterAction input source haccept hreject
    rw [h] at hstep
    exact (Option.some.inj hstep).symm
  let target' := programmeTM2RunStepTarget M target
  have htargetStep :
      (programmeTM2Machine M).step target = some target' :=
    programmeTM2_step_run_nonterminal hrep.represents haccept hreject
  have htargetRep :
      ProgrammeTM2Represents M input source' target' := by
    subst source'
    exact programmeTM2RunStepTarget_represents_afterAction hrep.represents
  refine ⟨target', ?_, htargetStep⟩
  refine
    { represents := htargetRep
      raw_empty := ?_
      temp_empty := ?_
      output_empty := ?_
      inputLeft_bound := ?_
      inputRight_bound := ?_
      workLeft_bound := ?_
      workRight_bound := ?_ }
  · dsimp [target']
    rw [programmeTM2RunStepTarget_eq_core]
    change (programmeTM2RunCore M target).2 .rawInput = []
    rw [programmeTM2RunCore_raw]
    exact hrep.raw_empty
  · dsimp [target']
    rw [programmeTM2RunStepTarget_eq_core]
    change (programmeTM2RunCore M target).2 .inputTemp = []
    rw [programmeTM2RunCore_temp]
    exact hrep.temp_empty
  · dsimp [target']
    rw [programmeTM2RunStepTarget_eq_core]
    change (programmeTM2RunCore M target).2 .output = []
    rw [programmeTM2RunCore_output]
    exact hrep.output_empty
  · dsimp [target']
    rw [programmeTM2RunStepTarget_eq_core]
    change ((programmeTM2RunCore M target).2 .inputLeft).length ≤ steps + 1
    exact (programmeTM2RunCore_inputLeft_length_le M target).trans
      (Nat.add_le_add_right hrep.inputLeft_bound 1)
  · dsimp [target']
    rw [programmeTM2RunStepTarget_eq_core]
    change ((programmeTM2RunCore M target).2 .inputRight).length ≤
      input.length + (steps + 1)
    have h := Nat.add_le_add_right hrep.inputRight_bound 1
    simpa [Nat.add_assoc] using h
  · intro tape
    dsimp [target']
    rw [programmeTM2RunStepTarget_eq_core]
    change ((programmeTM2RunCore M target).2 (.workLeft tape)).length ≤
      steps + 1
    exact (programmeTM2RunCore_workLeft_length_le M target tape).trans
      (Nat.add_le_add_right (hrep.workLeft_bound tape) 1)
  · intro tape
    dsimp [target']
    rw [programmeTM2RunStepTarget_eq_core]
    change ((programmeTM2RunCore M target).2 (.workRight tape)).length ≤
      steps + 1
    exact (programmeTM2RunCore_workRight_length_le M target tape).trans
      (Nat.add_le_add_right (hrep.workRight_bound tape) 1)

#print axioms programmeTM2ReadyInitCfg_bounded
#print axioms programmeTM2_bounded_step
#print axioms programmeTM2RunCore_inputLeft_length_le
#print axioms programmeTM2RunCore_inputRight_length_le
#print axioms programmeTM2RunCore_workLeft_length_le
#print axioms programmeTM2RunCore_workRight_length_le

end

end MathSolve.PNP
