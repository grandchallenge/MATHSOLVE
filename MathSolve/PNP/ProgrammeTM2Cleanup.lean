import MathSolve.PNP.ProgrammeTM2InitRun
import MathSolve.PNP.ProgrammeTM2TerminalEntry

/-! Actual finite-TM2 cleanup, from the represented terminal state to the
canonical Mathlib haltList. Stack lengths, not represented tape extents, pay
for every pop and empty test. -/
namespace MathSolve.PNP
noncomputable section
open Turing

abbrev CleanupStacks (M : ProgrammeMachine) :=
  ∀ k : ProgrammeTM2Stack M.workTapeCount, List (programmeTM2StackAlphabet M k)

def reverseCleanCfg (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (mode : ProgrammeTM2Mode M.workTapeCount) (S : CleanupStacks M) : (programmeTM2Machine M).Cfg :=
  { l := some mode, var := { s with mode := mode }, stk := S }

/-- The literal cleanup statement used by each non-emitting cleanup label. -/
def reverseCleanStmt (M : ProgrammeMachine) (k : ProgrammeTM2Stack M.workTapeCount)
    (mode : ProgrammeTM2Mode M.workTapeCount)
    (next : ProgrammeTM2State M → ProgrammeTM2Mode M.workTapeCount) : ProgrammeTM2Stmt M :=
  .pop k (fun s a => { s with mode := match a with | none => next s | some _ => mode })
    (.goto fun s => s.mode)

theorem reverseCleanStep (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (k : ProgrammeTM2Stack M.workTapeCount) (mode finish : ProgrammeTM2Mode M.workTapeCount)
    (next : ProgrammeTM2State M → ProgrammeTM2Mode M.workTapeCount)
    (hp : programmeTM2Program M mode = reverseCleanStmt M k mode next)
    (hn : next { s with mode := mode } = finish) (S : CleanupStacks M) :
    (programmeTM2Machine M).step (reverseCleanCfg M s mode S) =
      some (reverseCleanCfg M s (match (S k).head? with | none => finish | some _ => mode)
        (Function.update S k (S k).tail)) := by
  change some (TM2.stepAux (programmeTM2Program M mode) {s with mode := mode} S) = _
  rw [hp]
  cases h : S k <;> simp [reverseCleanStmt, reverseCleanCfg, TM2.stepAux, h, hn] <;> rfl

/-- One cleanup phase pops its entire stack and performs one empty check. -/
theorem reverseCleanPhase_run (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (k : ProgrammeTM2Stack M.workTapeCount) (mode finish : ProgrammeTM2Mode M.workTapeCount)
    (next : ProgrammeTM2State M → ProgrammeTM2Mode M.workTapeCount)
    (hp : programmeTM2Program M mode = reverseCleanStmt M k mode next)
    (hn : next { s with mode := mode } = finish) :
    ∀ (l : List (programmeTM2StackAlphabet M k)) (S : CleanupStacks M), S k = l →
      Nonempty (StateTransition.EvalsToInTime (programmeTM2Machine M).step
        (reverseCleanCfg M s mode S) (some (reverseCleanCfg M s finish (Function.update S k [])))
        (l.length + 1)) := by
  intro l
  induction l with
  | nil =>
    intro S hs
    have h := reverseCleanStep M s k mode finish next hp hn S
    have he : (programmeTM2Machine M).step (reverseCleanCfg M s mode S) =
      some (reverseCleanCfg M s finish (Function.update S k [])) := by
      simpa [hs] using h
    exact ⟨by simpa using programmeTM2_one_step_in_time he⟩
  | cons a l ih =>
    intro S hs
    let S' : CleanupStacks M := Function.update S k l
    have h := reverseCleanStep M s k mode finish next hp hn S
    have he : (programmeTM2Machine M).step (reverseCleanCfg M s mode S) =
      some (reverseCleanCfg M s mode S') := by simpa [hs, S'] using h
    rcases ih S' (by simp [S']) with ⟨ht⟩
    have hh := StateTransition.EvalsToInTime.trans (programmeTM2Machine M).step
      1 (l.length+1) _ _ _ (programmeTM2_one_step_in_time he) ht
    exact ⟨by simpa [S', Function.update_idem, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using hh⟩

/-- Widen the exact stack-length cleanup budget to a uniform length bound. -/
theorem reverseCleanPhase_bound (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (k : ProgrammeTM2Stack M.workTapeCount) (mode finish : ProgrammeTM2Mode M.workTapeCount)
    (next : ProgrammeTM2State M → ProgrammeTM2Mode M.workTapeCount)
    (hp : programmeTM2Program M mode = reverseCleanStmt M k mode next)
    (hn : next { s with mode := mode } = finish) (S : CleanupStacks M) (b : Nat)
    (hb : (S k).length ≤ b) :
    Nonempty (StateTransition.EvalsToInTime (programmeTM2Machine M).step
      (reverseCleanCfg M s mode S) (some (reverseCleanCfg M s finish (Function.update S k []))) (b+1)) := by
  rcases reverseCleanPhase_run M s k mode finish next hp hn (S k) S rfl with ⟨h⟩
  exact ⟨⟨h.toEvalsTo, h.steps_le_m.trans (by omega)⟩⟩

/-- Clearing a stack cannot increase the uniform stack bound. -/
theorem reverseClean_bound_update (M : ProgrammeMachine) (S : CleanupStacks M) (b : Nat)
    (k : ProgrammeTM2Stack M.workTapeCount) (h : ∀ j, (S j).length ≤ b) :
    ∀ j, ((Function.update S k []) j).length ≤ b := by
  intro j
  by_cases he : j = k
  · subst j; simp
  · simpa [Function.update_of_ne he] using h j

/-- The work-cleaning mode for the next natural tape index, or final emission. -/
def reverseCleanWorkMode (M : ProgrammeMachine) (i : Nat) (s : ProgrammeTM2State M) :
    ProgrammeTM2Mode M.workTapeCount :=
  if h : i < M.workTapeCount then .cleanWorkLeft ⟨i,h⟩ else .emit (programmeTM2TerminalResult M s)

def ReverseCleanPrefix (M : ProgrammeMachine) (i : Nat) (S : CleanupStacks M) : Prop :=
  S .rawInput = [] ∧ S .inputTemp = [] ∧ S .inputLeft = [] ∧ S .inputRight = [] ∧ S .output = [] ∧
  ∀ j : Fin M.workTapeCount, j.val < i → S (.workLeft j) = [] ∧ S (.workRight j) = []

/-- Two work-stack clears advance the completed prefix by one tape. -/
theorem reverseCleanPrefix_succ (M : ProgrammeMachine) (S : CleanupStacks M)
    (i : Nat) (hi : i < M.workTapeCount) (h : ReverseCleanPrefix M i S) :
    ReverseCleanPrefix M (i+1)
      (Function.update (Function.update S (.workLeft ⟨i,hi⟩) []) (.workRight ⟨i,hi⟩) []) := by
  rcases h with ⟨hraw,htemp,hl,hr,ho,hwork⟩
  refine ⟨?_,?_,?_,?_,?_,?_⟩
  all_goals try simp [Function.update_of_ne, hraw, htemp, hl, hr, ho]
  intro j hj
  by_cases he : j.val = i
  · have he' : j = (⟨i,hi⟩ : Fin M.workTapeCount) := Fin.ext he
    subst j; simp [Function.update_of_ne]
  · have hlt : j.val < i := by omega
    have hne : j ≠ (⟨i,hi⟩ : Fin M.workTapeCount) := fun hh => he (congrArg Fin.val hh)
    have hll : (ProgrammeTM2Stack.workLeft j : ProgrammeTM2Stack M.workTapeCount) ≠ .workLeft ⟨i,hi⟩ := fun hh => hne (ProgrammeTM2Stack.workLeft.inj hh)
    have hrr : (ProgrammeTM2Stack.workRight j : ProgrammeTM2Stack M.workTapeCount) ≠ .workRight ⟨i,hi⟩ := fun hh => hne (ProgrammeTM2Stack.workRight.inj hh)
    simpa [Function.update_of_ne, hll, hrr] using hwork j hlt

/-- Emission resets local state and places precisely one bit on the previously
empty output stack; all other stacks are empty in the native haltList. -/
theorem reverseEmit_step (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (S : CleanupStacks M) (result : Bool) (he : ∀ k, S k = []) :
    (programmeTM2Machine M).step (reverseCleanCfg M s (.emit result) S) =
      some (Turing.haltList (programmeTM2Machine M) [result]) := by
  change some (TM2.stepAux (programmeTM2Program M (.emit result))
    {s with mode := .emit result} S) = _
  have hS : S = (fun k => []) := funext he
  subst S
  simp [programmeTM2Program, TM2.stepAux, Turing.haltList, programmeTM2Machine]
  congr 1
  congr 1
  funext k
  cases k <;> simp [Function.update] <;> rfl

/-- Starting at natural work index i, clear every remaining work pair and
emit. A uniform bound b on all physical stack lengths pays for each pop. -/
theorem reverseWorkCleanup_run (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (b : Nat) : ∀ (remaining i : Nat) (S : CleanupStacks M),
      i + remaining = M.workTapeCount → (∀ k, (S k).length ≤ b) → ReverseCleanPrefix M i S →
      Nonempty (StateTransition.EvalsToInTime (programmeTM2Machine M).step
        (reverseCleanCfg M s (reverseCleanWorkMode M i s) S)
        (some (Turing.haltList (programmeTM2Machine M) [programmeTM2TerminalResult M s]))
        (2 * remaining * (b+1) + 1)) := by
  intro remaining
  induction remaining with
  | zero =>
    intro i S hi _ hp
    have hie : i = M.workTapeCount := by omega
    have he : ∀ k, S k = [] := by
      rcases hp with ⟨ha,hb,hc,hd,ho,hw⟩
      intro k
      cases k with
      | rawInput => exact ha
      | inputTemp => exact hb
      | inputLeft => exact hc
      | inputRight => exact hd
      | output => exact ho
      | workLeft j => exact (hw j (by omega)).1
      | workRight j => exact (hw j (by omega)).2
    have hnot : ¬ i < M.workTapeCount := by omega
    simpa [reverseCleanWorkMode, hnot] using
      (show Nonempty (StateTransition.EvalsToInTime (programmeTM2Machine M).step
        (reverseCleanCfg M s (.emit (programmeTM2TerminalResult M s)) S)
        (some (Turing.haltList (programmeTM2Machine M) [programmeTM2TerminalResult M s])) 1) from
        ⟨programmeTM2_one_step_in_time (reverseEmit_step M s S _ he)⟩)
  | succ remaining ih =>
    intro i S hi hb hp
    have hlt : i < M.workTapeCount := by omega
    let j : Fin M.workTapeCount := ⟨i,hlt⟩
    let S1 : CleanupStacks M := Function.update S (.workLeft j) []
    let S2 : CleanupStacks M := Function.update S1 (.workRight j) []
    have hb1 := reverseClean_bound_update M S b (.workLeft j) hb
    have hb2 := reverseClean_bound_update M S1 b (.workRight j) hb1
    have hp2 : ReverseCleanPrefix M (i+1) S2 := reverseCleanPrefix_succ M S i hlt hp
    rcases reverseCleanPhase_bound M s (.workLeft j) (.cleanWorkLeft j) (.cleanWorkRight j)
      (fun _ => .cleanWorkRight j) rfl rfl S b (hb (.workLeft j)) with ⟨hl⟩
    rcases reverseCleanPhase_bound M s (.workRight j) (.cleanWorkRight j) (reverseCleanWorkMode M (i+1) s)
      (programmeTM2NextWorkOrEmit M j) rfl (by rfl) S1 b (hb1 (.workRight j)) with ⟨hr⟩
    rcases ih (i+1) S2 (by omega) hb2 hp2 with ⟨ht⟩
    have h12 := StateTransition.EvalsToInTime.trans (programmeTM2Machine M).step
      (b+1) (b+1) _ _ _ hl hr
    have hall := StateTransition.EvalsToInTime.trans (programmeTM2Machine M).step
      (b+1+(b+1)) (2*remaining*(b+1)+1) _ _ _ h12 ht
    rw [reverseCleanWorkMode, dif_pos hlt]
    exact ⟨by convert hall using 1 <;> ring⟩

/-- Clear the four non-work stacks, every work pair, and emit one Boolean.
The bound includes all empty checks, even if input scratch stacks are empty. -/
theorem reverseCleanup_run (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (S : CleanupStacks M) (b : Nat) (hb : ∀ k, (S k).length ≤ b)
    (ho : S .output = []) :
    Nonempty (StateTransition.EvalsToInTime (programmeTM2Machine M).step
      (reverseCleanCfg M s .cleanRaw S)
      (some (Turing.haltList (programmeTM2Machine M) [programmeTM2TerminalResult M s]))
      ((2*M.workTapeCount+4)*(b+1)+1)) := by
  let S1 : CleanupStacks M := Function.update S .rawInput []
  let S2 : CleanupStacks M := Function.update S1 .inputTemp []
  let S3 : CleanupStacks M := Function.update S2 .inputLeft []
  let S4 : CleanupStacks M := Function.update S3 .inputRight []
  have hb1 := reverseClean_bound_update M S b .rawInput hb
  have hb2 := reverseClean_bound_update M S1 b .inputTemp hb1
  have hb3 := reverseClean_bound_update M S2 b .inputLeft hb2
  have hb4 := reverseClean_bound_update M S3 b .inputRight hb3
  have hp : ReverseCleanPrefix M 0 S4 := by
    refine ⟨?_,?_,?_,?_,?_,?_⟩
    all_goals try simp [S4,S3,S2,S1,Function.update_of_ne,ho]
    intro j hj; omega
  rcases reverseCleanPhase_bound M s .rawInput .cleanRaw .cleanTemp
    (fun _ => .cleanTemp) rfl rfl S b (hb .rawInput) with ⟨h1⟩
  rcases reverseCleanPhase_bound M s .inputTemp .cleanTemp .cleanInputLeft
    (fun _ => .cleanInputLeft) rfl rfl S1 b (hb1 .inputTemp) with ⟨h2⟩
  rcases reverseCleanPhase_bound M s .inputLeft .cleanInputLeft .cleanInputRight
    (fun _ => .cleanInputRight) rfl rfl S2 b (hb2 .inputLeft) with ⟨h3⟩
  rcases reverseCleanPhase_bound M s .inputRight .cleanInputRight (reverseCleanWorkMode M 0 s)
    (programmeTM2FirstWorkOrEmit M) rfl (by rfl) S3 b (hb3 .inputRight) with ⟨h4⟩
  rcases reverseWorkCleanup_run M s b M.workTapeCount 0 S4 (by omega) hb4 hp with ⟨hw⟩
  have h12 := StateTransition.EvalsToInTime.trans (programmeTM2Machine M).step (b+1) (b+1) _ _ _ h1 h2
  have h123 := StateTransition.EvalsToInTime.trans (programmeTM2Machine M).step (b+1+(b+1)) (b+1) _ _ _ h12 h3
  have h1234 := StateTransition.EvalsToInTime.trans (programmeTM2Machine M).step (b+1+(b+1)+(b+1)) (b+1) _ _ _ h123 h4
  have hall := StateTransition.EvalsToInTime.trans (programmeTM2Machine M).step
    (b+1+(b+1)+(b+1)+(b+1)) (2*M.workTapeCount*(b+1)+1) _ _ _ h1234 hw
  exact ⟨by convert hall using 1 <;> ring⟩

/-- Complete termination and native output agreement from any represented terminal
configuration with bounded finite stacks and an initially empty output stack. -/
theorem programmeTM2_terminal_cleanup_run {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg} {b : Nat}
    (hrep : ProgrammeTM2Represents M input source target)
    (hterm : source.state = M.accept ∨ source.state = M.reject)
    (hb : ∀ k, (target.stk k).length ≤ b) (ho : target.stk .output = []) :
    ∃ result : Bool, M.output source = some result ∧
      Nonempty (StateTransition.EvalsToInTime (programmeTM2Machine M).step target
        (some (Turing.haltList (programmeTM2Machine M) [result]))
        ((2*M.workTapeCount+4)*(b+1)+2)) := by
  let result := programmeTM2TerminalResult M target.var
  have hstep : (programmeTM2Machine M).step target = some (programmeTM2TerminalEntry M target) := by
    rcases hterm with h | h
    · exact programmeTM2_step_accept_enters_cleanup hrep h
    · exact programmeTM2_step_reject_enters_cleanup hrep h
  rcases reverseCleanup_run M target.var target.stk b hb ho with ⟨hc⟩
  have hentry : programmeTM2TerminalEntry M target = reverseCleanCfg M target.var .cleanRaw target.stk := rfl
  rw [← hentry] at hc
  have hall := StateTransition.EvalsToInTime.trans (programmeTM2Machine M).step
    1 ((2*M.workTapeCount+4)*(b+1)+1) _ _ _ (programmeTM2_one_step_in_time hstep) hc
  exact ⟨result, programmeTM2_terminal_result_agrees_with_source hrep hterm,
    ⟨by simpa [result, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using hall⟩⟩

#print axioms reverseCleanStep
#print axioms reverseCleanPhase_run
#print axioms reverseWorkCleanup_run
#print axioms reverseCleanup_run
#print axioms programmeTM2_terminal_cleanup_run
end
end MathSolve.PNP
