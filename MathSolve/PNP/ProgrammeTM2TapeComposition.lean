import MathSolve.PNP.ProgrammeTM2PhysicalEffects
import MathSolve.PNP.ProgrammeTM2SemanticInvariant

/-! Concrete stack updates and the frame property for the reverse compiler. -/
namespace MathSolve.PNP
noncomputable section
open Turing

abbrev ReverseCfg (M : ProgrammeMachine) := (programmeTM2Machine M).Cfg

/-- The literal physical update before the continuation of a work move. -/
def reverseWorkUpdate (M : ProgrammeMachine) (k : Fin M.workTapeCount)
    (c : ReverseCfg M) : ReverseCfg M :=
  match (c.var.snapshotAction M).workMove k with
  | .left => { c with
      var := c.var.setWorkSymbol M k ((c.stk (.workLeft k)).head?.getD M.blank)
      stk := Function.update
        (Function.update c.stk (.workRight k)
          ((c.var.snapshotAction M).write k :: c.stk (.workRight k)))
        (.workLeft k) (c.stk (.workLeft k)).tail }
  | .right => { c with
      var := c.var.setWorkSymbol M k ((c.stk (.workRight k)).head?.getD M.blank)
      stk := Function.update
        (Function.update c.stk (.workLeft k)
          ((c.var.snapshotAction M).write k :: c.stk (.workLeft k)))
        (.workRight k) (c.stk (.workRight k)).tail }
  | .stay => { c with var := c.var.setWorkSymbol M k ((c.var.snapshotAction M).write k) }

/-- The literal physical update before the continuation of an input move. -/
def reverseInputUpdate (M : ProgrammeMachine) (c : ReverseCfg M) : ReverseCfg M :=
  match (c.var.snapshotAction M).inputMove with
  | .left => { c with
      var := { c.var with inputSymbol := (c.stk .inputLeft).head?.getD none }
      stk := Function.update (Function.update c.stk .inputRight
        (c.var.snapshotInputSymbol :: c.stk .inputRight)) .inputLeft (c.stk .inputLeft).tail }
  | .right => { c with
      var := { c.var with inputSymbol := (c.stk .inputRight).head?.getD none }
      stk := Function.update (Function.update c.stk .inputLeft
        (c.var.snapshotInputSymbol :: c.stk .inputLeft)) .inputRight (c.stk .inputRight).tail }
  | .stay => c

theorem reverseWorkUpdate_exec (M : ProgrammeMachine) (k : Fin M.workTapeCount)
    (next : ProgrammeTM2Stmt M) (c : ReverseCfg M) :
    TM2.stepAux (programmeTM2ApplyWorkMove M k next) c.var c.stk =
      TM2.stepAux next (reverseWorkUpdate M k c).var (reverseWorkUpdate M k c).stk := by
  cases h : (c.var.snapshotAction M).workMove k with
  | left => simpa [reverseWorkUpdate, h] using programmeTM2_workMove_left_exec M k next c.var c.stk h
  | right => simpa [reverseWorkUpdate, h] using programmeTM2_workMove_right_exec M k next c.var c.stk h
  | stay => simpa [reverseWorkUpdate, h] using programmeTM2_workMove_stay_exec M k next c.var c.stk h

theorem reverseInputUpdate_exec (M : ProgrammeMachine) (next : ProgrammeTM2Stmt M)
    (c : ReverseCfg M) :
    TM2.stepAux (programmeTM2ApplyInputMove M next) c.var c.stk =
      TM2.stepAux next (reverseInputUpdate M c).var (reverseInputUpdate M c).stk := by
  cases h : (c.var.snapshotAction M).inputMove with
  | left => simpa [reverseInputUpdate, h] using programmeTM2_inputMove_left_exec M next c.var c.stk h
  | right => simpa [reverseInputUpdate, h] using programmeTM2_inputMove_right_exec M next c.var c.stk h
  | stay => simpa [reverseInputUpdate, h] using programmeTM2_inputMove_stay_exec M next c.var c.stk h

theorem reverseWorkUpdate_snapshot (M : ProgrammeMachine) (k : Fin M.workTapeCount)
    (c : ReverseCfg M) : (reverseWorkUpdate M k c).var.snapshotAction M = c.var.snapshotAction M := by
  cases h : (c.var.snapshotAction M).workMove k <;> simp only [reverseWorkUpdate, h] <;> rfl

theorem reverseInputUpdate_snapshot (M : ProgrammeMachine) (c : ReverseCfg M) :
    (reverseInputUpdate M c).var.snapshotAction M = c.var.snapshotAction M := by
  cases h : (c.var.snapshotAction M).inputMove <;> simp only [reverseInputUpdate, h] <;> rfl

theorem reverseWorkUpdate_input (M : ProgrammeMachine) (k : Fin M.workTapeCount)
    (c : ReverseCfg M) : programmeTM2InputTape M (reverseWorkUpdate M k c) = programmeTM2InputTape M c := by
  cases h : (c.var.snapshotAction M).workMove k <;>
    simp [reverseWorkUpdate, h, programmeTM2InputTape, ProgrammeTM2State.setWorkSymbol, Function.update_of_ne]

theorem reverseInputUpdate_work (M : ProgrammeMachine) (k : Fin M.workTapeCount)
    (c : ReverseCfg M) : programmeTM2WorkTape M (reverseInputUpdate M c) k = programmeTM2WorkTape M c k := by
  cases h : (c.var.snapshotAction M).inputMove <;>
    simp [reverseInputUpdate, h, programmeTM2WorkTape, Function.update_of_ne]

theorem reverseWorkUpdate_other (M : ProgrammeMachine) (k j : Fin M.workTapeCount)
    (c : ReverseCfg M) (hne : j ≠ k) :
    programmeTM2WorkTape M (reverseWorkUpdate M k c) j = programmeTM2WorkTape M c j := by
  have hll : (ProgrammeTM2Stack.workLeft j : ProgrammeTM2Stack M.workTapeCount) ≠ .workLeft k := by
    intro he; exact hne (ProgrammeTM2Stack.workLeft.inj he)
  have hrr : (ProgrammeTM2Stack.workRight j : ProgrammeTM2Stack M.workTapeCount) ≠ .workRight k := by
    intro he; exact hne (ProgrammeTM2Stack.workRight.inj he)
  have hlr : (ProgrammeTM2Stack.workLeft j : ProgrammeTM2Stack M.workTapeCount) ≠ .workRight k := by intro he; cases he
  have hrl : (ProgrammeTM2Stack.workRight j : ProgrammeTM2Stack M.workTapeCount) ≠ .workLeft k := by intro he; cases he
  cases h : (c.var.snapshotAction M).workMove k <;>
    simp only [reverseWorkUpdate, h, programmeTM2WorkTape, ProgrammeTM2State.setWorkSymbol,
      Function.update_of_ne hne, Function.update_of_ne hll, Function.update_of_ne hrr,
      Function.update_of_ne hlr, Function.update_of_ne hrl]

theorem reverseWorkUpdate_own (M : ProgrammeMachine) (k : Fin M.workTapeCount)
    (c : ReverseCfg M) :
    programmeTM2WorkTape M (reverseWorkUpdate M k c) k =
      programmeTM2TapeMove ((c.var.snapshotAction M).workMove k)
        ((programmeTM2WorkTape M c k).write ((c.var.snapshotAction M).write k)) := by
  cases h : (c.var.snapshotAction M).workMove k with
  | left =>
    simpa [reverseWorkUpdate, h, programmeTM2TapeMove, programmeTM2WorkTape, programmeTM2WorkTapeRaw,
      ProgrammeTM2State.setWorkSymbol, Function.update_of_ne] using
      (programmeTM2WorkTapeRaw_write_move_left (M := M) (c.var.workSymbol k)
        ((c.var.snapshotAction M).write k) (c.stk (.workLeft k)) (c.stk (.workRight k)))
  | right =>
    simpa [reverseWorkUpdate, h, programmeTM2TapeMove, programmeTM2WorkTape, programmeTM2WorkTapeRaw,
      ProgrammeTM2State.setWorkSymbol, Function.update_of_ne] using
      (programmeTM2WorkTapeRaw_write_move_right (M := M) (c.var.workSymbol k)
        ((c.var.snapshotAction M).write k) (c.stk (.workLeft k)) (c.stk (.workRight k)))
  | stay =>
    simpa [reverseWorkUpdate, h, programmeTM2TapeMove, programmeTM2WorkTape, programmeTM2WorkTapeRaw,
      ProgrammeTM2State.setWorkSymbol] using
      (programmeTM2WorkTapeRaw_write_stay (M := M) (c.var.workSymbol k)
        ((c.var.snapshotAction M).write k) (c.stk (.workLeft k)) (c.stk (.workRight k)))

theorem reverseInputUpdate_own (M : ProgrammeMachine) (c : ReverseCfg M)
    (hs : c.var.snapshotInputSymbol = c.var.inputSymbol) :
    programmeTM2InputTape M (reverseInputUpdate M c) =
      programmeTM2TapeMove (c.var.snapshotAction M).inputMove (programmeTM2InputTape M c) := by
  cases h : (c.var.snapshotAction M).inputMove with
  | left =>
    simpa [reverseInputUpdate, h, hs, programmeTM2TapeMove, programmeTM2InputTape, programmeTM2InputTapeRaw,
      Function.update_of_ne] using
      (programmeTM2InputTapeRaw_move_left c.var.inputSymbol (c.stk .inputLeft) (c.stk .inputRight))
  | right =>
    simpa [reverseInputUpdate, h, hs, programmeTM2TapeMove, programmeTM2InputTape, programmeTM2InputTapeRaw,
      Function.update_of_ne] using
      (programmeTM2InputTapeRaw_move_right c.var.inputSymbol (c.stk .inputLeft) (c.stk .inputRight))
  | stay => simp [reverseInputUpdate, h, programmeTM2TapeMove]

/-- Sequential physical updates, in precisely the order of the native statement. -/
def reverseWorkFold (M : ProgrammeMachine) : List (Fin M.workTapeCount) → ReverseCfg M → ReverseCfg M
  | [], c => c
  | k :: ks, c => reverseWorkFold M ks (reverseWorkUpdate M k c)

theorem reverseWorkFold_exec (M : ProgrammeMachine) (ks : List (Fin M.workTapeCount))
    (next : ProgrammeTM2Stmt M) (c : ReverseCfg M) :
    TM2.stepAux (programmeTM2ApplyWorkMoves M ks next) c.var c.stk =
      TM2.stepAux next (reverseWorkFold M ks c).var (reverseWorkFold M ks c).stk := by
  induction ks generalizing c with
  | nil => rfl
  | cons k ks ih =>
    rw [programmeTM2ApplyWorkMoves, reverseWorkUpdate_exec]
    exact ih _

theorem reverseWorkFold_snapshot (M : ProgrammeMachine) (ks : List (Fin M.workTapeCount))
    (c : ReverseCfg M) : (reverseWorkFold M ks c).var.snapshotAction M = c.var.snapshotAction M := by
  induction ks generalizing c with
  | nil => rfl
  | cons k ks ih =>
    simp only [reverseWorkFold, ih, reverseWorkUpdate_snapshot]

theorem reverseWorkFold_input (M : ProgrammeMachine) (ks : List (Fin M.workTapeCount))
    (c : ReverseCfg M) : programmeTM2InputTape M (reverseWorkFold M ks c) = programmeTM2InputTape M c := by
  induction ks generalizing c with
  | nil => rfl
  | cons k ks ih => simp only [reverseWorkFold, ih, reverseWorkUpdate_input]

theorem reverseWorkFold_absent (M : ProgrammeMachine) (ks : List (Fin M.workTapeCount))
    (c : ReverseCfg M) (j : Fin M.workTapeCount) (hj : j ∉ ks) :
    programmeTM2WorkTape M (reverseWorkFold M ks c) j = programmeTM2WorkTape M c j := by
  induction ks generalizing c with
  | nil => rfl
  | cons k ks ih =>
    have hne : j ≠ k := fun h => hj (by simp [h])
    have hn : j ∉ ks := fun h => hj (by simp [h])
    rw [reverseWorkFold, ih _ hn, reverseWorkUpdate_other M k j c hne]

theorem reverseWorkFold_present (M : ProgrammeMachine) (ks : List (Fin M.workTapeCount))
    (c : ReverseCfg M) (j : Fin M.workTapeCount) (hd : ks.Nodup) (hj : j ∈ ks) :
    programmeTM2WorkTape M (reverseWorkFold M ks c) j =
      programmeTM2TapeMove ((c.var.snapshotAction M).workMove j)
        ((programmeTM2WorkTape M c j).write ((c.var.snapshotAction M).write j)) := by
  induction ks generalizing c with
  | nil => simp at hj
  | cons k ks ih =>
    have hd' := List.nodup_cons.mp hd
    rcases List.mem_cons.mp hj with rfl | hm
    · rw [reverseWorkFold, reverseWorkFold_absent M ks _ j hd'.1, reverseWorkUpdate_own]
    · have hne : j ≠ k := fun h => hd'.1 (by simpa [h] using hm)
      rw [reverseWorkFold, ih _ hd'.2 hm, reverseWorkUpdate_snapshot,
        reverseWorkUpdate_other M k j c hne]

/-- A fresh snapshot, the input update, then every work update, and a final commit. -/
def reverseRunPhysical (M : ProgrammeMachine) (c : ReverseCfg M) : ReverseCfg M :=
  let snap := { c with var := c.var.snapshot M }
  let moved := reverseInputUpdate M snap
  let finished := reverseWorkFold M (programmeTM2WorkTapes M) moved
  { finished with l := some .run, var := finished.var.commitAction M }

theorem reverseRunPhysical_exec (M : ProgrammeMachine) (c : ReverseCfg M) :
    programmeTM2RunStepTarget M c = reverseRunPhysical M c := by
  let snap : ReverseCfg M := { c with var := c.var.snapshot M }
  let last : ProgrammeTM2Stmt M := .load (ProgrammeTM2State.commitAction M) (.goto fun _ => .run)
  change TM2.stepAux (programmeTM2ApplyInputMove M
    (programmeTM2ApplyWorkMoves M (programmeTM2WorkTapes M) last)) snap.var snap.stk = _
  rw [reverseInputUpdate_exec M _ snap, reverseWorkFold_exec M _ _ (reverseInputUpdate M snap)]
  rfl

theorem reverseRunPhysical_input (M : ProgrammeMachine) (c : ReverseCfg M) :
    programmeTM2InputTape M (reverseRunPhysical M c) =
      programmeTM2TapeMove (M.transition c.var.control c.var.inputSymbol c.var.workSymbol).inputMove
        (programmeTM2InputTape M c) := by
  let snap : ReverseCfg M := { c with var := c.var.snapshot M }
  change programmeTM2InputTape M (reverseWorkFold M (programmeTM2WorkTapes M) (reverseInputUpdate M snap)) = _
  rw [reverseWorkFold_input, reverseInputUpdate_own M snap (by rfl)]
  rfl

theorem reverseRunPhysical_work (M : ProgrammeMachine) (c : ReverseCfg M) (j : Fin M.workTapeCount) :
    programmeTM2WorkTape M (reverseRunPhysical M c) j =
      programmeTM2TapeMove ((M.transition c.var.control c.var.inputSymbol c.var.workSymbol).workMove j)
        ((programmeTM2WorkTape M c j).write ((M.transition c.var.control c.var.inputSymbol c.var.workSymbol).write j)) := by
  let snap : ReverseCfg M := { c with var := c.var.snapshot M }
  change programmeTM2WorkTape M (reverseWorkFold M (programmeTM2WorkTapes M) (reverseInputUpdate M snap)) j = _
  rw [reverseWorkFold_present M (programmeTM2WorkTapes M) (reverseInputUpdate M snap) j
    (by exact List.nodup_finRange _) (by simp [programmeTM2WorkTapes]),
    reverseInputUpdate_snapshot, reverseInputUpdate_work]
  rfl

/-- Unconditional preservation of every represented cell and next control. -/
theorem programmeTM2_runStepTarget_represents {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : ReverseCfg M}
    (hrep : ProgrammeTM2Represents M input source target) :
    ProgrammeTM2Represents M input (source.afterAction (M.actionAt input source))
      (programmeTM2RunStepTarget M target) := by
  have hc := programmeTM2_runStepTarget_control hrep
  apply hrep.afterAction_of_concrete_tape_effects (M.actionAt input source) (programmeTM2_runStepTarget_label M target) hc.1 hc.2
  · rw [reverseRunPhysical_exec, reverseRunPhysical_input, hrep.action_eq]
    rfl
  · intro j
    rw [reverseRunPhysical_exec, reverseRunPhysical_work, hrep.action_eq]
    rfl

/-- Every actual source step is matched by exactly one native TM2 step. -/
theorem programmeTM2_simulates_step {M : ProgrammeMachine} {input : List Bool}
    {source source' : ProgrammeConfig M} {target : ReverseCfg M}
    (hrep : ProgrammeTM2Represents M input source target)
    (hs : M.step input source = some source') :
    ∃ target', (programmeTM2Machine M).step target = some target' ∧
      ProgrammeTM2Represents M input source' target' := by
  have ha : source.state ≠ M.accept := by
    intro h; rw [M.step_eq_none_of_accept input source h] at hs; contradiction
  have hr : source.state ≠ M.reject := by
    intro h; rw [M.step_eq_none_of_reject input source h] at hs; contradiction
  rw [M.step_eq_some_afterAction input source ha hr] at hs
  have he := Option.some.inj hs
  subst source'
  exact ⟨_, programmeTM2_step_run_nonterminal hrep ha hr, programmeTM2_runStepTarget_represents hrep⟩

#print axioms reverseRunPhysical_exec
#print axioms reverseRunPhysical_input
#print axioms reverseRunPhysical_work
#print axioms programmeTM2_runStepTarget_represents
#print axioms programmeTM2_simulates_step
end
end MathSolve.PNP
