import MathSolve.PNP.TM2PrefixLift

/-! A concrete two-pass finite-stack prefix for fixed two-symbol expansion.
The scan pushes two symbols per input letter onto the temporary stack; the
rewind restores them in order to the original machine's input stack. -/
namespace MathSolve.PNP
namespace TM2PairExpand
open Turing TM2PrefixLift
noncomputable section

variable (tm : FinTM2)
abbrev B := tm.Γ tm.k₀

def extraAlphabet : Bool → Type
  | false => Option Bool
  | true => B tm

abbrev Aux := Option (Option Bool) × Option (B tm)
def reset : Aux tm := (none, none)

abbrev Stmt := TM2.Stmt (alphabet tm.Γ (extraAlphabet tm))
    (tm.Λ ⊕ Bool) (tm.σ × Aux tm)

def prefixProgram (f : Option Bool → B tm × B tm) (defaultB : B tm) : Bool → Stmt tm
  | false => .pop (.inr false) (fun v a => (v.1,(a,none)))
      (.branch (fun v => v.2.1.isSome)
        (.push (.inr true) (fun v => (f (v.2.1.getD none)).1)
          (.push (.inr true) (fun v => (f (v.2.1.getD none)).2)
            (.load (fun v => (v.1,reset tm)) (.goto (fun _ => .inr false)))))
        (.load (fun v => (v.1,reset tm)) (.goto (fun _ => .inr true))))
  | true => .pop (.inr true) (fun v a => (v.1,(none,a)))
      (.branch (fun v => v.2.2.isSome)
        (.push (.inl tm.k₀) (fun v => v.2.2.getD defaultB)
          (.load (fun v => (v.1,reset tm)) (.goto (fun _ => .inr true))))
        (.load (fun v => (v.1,reset tm)) (.goto (fun _ => .inl tm.main))))

def machine (f : Option Bool → B tm × B tm) (defaultB : B tm) : FinTM2 := by
  letI := tm.Γk₀Fin
  exact TM2PrefixLift.machine tm Bool Bool (Aux tm) (extraAlphabet tm)
    false false (reset tm) (prefixProgram tm f defaultB)

def extra (raw : List (Option Bool)) (temp : List (B tm)) :
    StackFamily (extraAlphabet tm)
  | false => raw
  | true => temp

def stacks (raw : List (Option Bool)) (temp out : List (B tm)) :
    StackFamily (alphabet tm.Γ (extraAlphabet tm)) :=
  liftStacks (initList tm out).stk (extra tm raw temp)

def state (mode : Bool) (raw : List (Option Bool)) (temp out : List (B tm)) :
    TM2.Cfg (alphabet tm.Γ (extraAlphabet tm)) (tm.Λ ⊕ Bool) (tm.σ × Aux tm) :=
  { l := some (.inr mode)
    var := (tm.initialState, reset tm)
    stk := stacks tm raw temp out }

def expand (f : Option Bool → B tm × B tm) : List (Option Bool) → List (B tm)
  | [] => []
  | a :: as => (f a).1 :: (f a).2 :: expand f as

theorem expand_length (f : Option Bool → B tm × B tm) (raw : List (Option Bool)) :
    (expand tm f raw).length = 2 * raw.length := by
  induction raw with
  | nil => rfl
  | cons a as ih => simp [expand, ih]; omega

@[simp] theorem stacks_raw (raw : List (Option Bool)) (temp out : List (B tm)) :
    stacks tm raw temp out (.inr false) = raw := rfl
@[simp] theorem stacks_temp (raw : List (Option Bool)) (temp out : List (B tm)) :
    stacks tm raw temp out (.inr true) = temp := rfl
@[simp] theorem stacks_out (raw : List (Option Bool)) (temp out : List (B tm)) :
    stacks tm raw temp out (.inl tm.k₀) = out := by
  simp [stacks, liftStacks, initList]

theorem update_raw (raw raw' : List (Option Bool)) (temp out : List (B tm)) :
    Function.update (stacks tm raw temp out) (.inr false) raw' =
      stacks tm raw' temp out := by
  funext k
  cases k with
  | inl k => simp [Function.update, stacks, liftStacks, extra]
  | inr k => cases k <;> simp [Function.update, stacks, liftStacks, extra]

theorem update_temp (raw : List (Option Bool)) (temp temp' out : List (B tm)) :
    Function.update (stacks tm raw temp out) (.inr true) temp' =
      stacks tm raw temp' out := by
  funext k
  cases k with
  | inl k => simp [Function.update, stacks, liftStacks, extra]
  | inr k => cases k <;> simp [Function.update, stacks, liftStacks, extra]

theorem update_out (raw : List (Option Bool)) (temp out out' : List (B tm)) :
    Function.update (stacks tm raw temp out) (.inl tm.k₀) out' =
      stacks tm raw temp out' := by
  funext k
  cases k with
  | inl k =>
    by_cases h : k = tm.k₀
    · subst k; simp [Function.update, stacks, liftStacks, initList]
    · simp [Function.update, stacks, liftStacks, initList, h]
  | inr k => cases k <;> simp [Function.update, stacks, liftStacks, extra]

theorem init_eq (f : Option Bool → B tm × B tm) (d : B tm) (raw : List (Option Bool)) :
    initList (machine tm f d) raw = state tm false raw [] [] := by
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k with
    | inl k =>
      by_cases h : k = tm.k₀
      · subst k; simp [initList, machine, TM2PrefixLift.machine, state, stacks, liftStacks]
      · simp [initList, machine, TM2PrefixLift.machine, state, stacks, liftStacks, h]
    | inr k => cases k <;> rfl

variable (f : Option Bool → B tm × B tm) (d : B tm)

theorem scan_cons (a : Option Bool) (raw : List (Option Bool)) (temp out : List (B tm)) :
    (machine tm f d).step (state tm false (a :: raw) temp out) =
      some (state tm false raw ((f a).2 :: (f a).1 :: temp) out) := by
  change some (TM2.stepAux (prefixProgram tm f d false) (tm.initialState, reset tm)
    (stacks tm (a :: raw) temp out)) = _
  apply congrArg some
  simp [prefixProgram, TM2.stepAux, state, reset, update_raw, update_temp]

theorem scan_nil (temp out : List (B tm)) :
    (machine tm f d).step (state tm false [] temp out) =
      some (state tm true [] temp out) := by
  change some (TM2.stepAux (prefixProgram tm f d false) (tm.initialState, reset tm)
    (stacks tm [] temp out)) = _
  apply congrArg some
  simp [prefixProgram, TM2.stepAux, state, reset, update_raw]

theorem rewind_cons (b : B tm) (temp out : List (B tm)) :
    (machine tm f d).step (state tm true [] (b :: temp) out) =
      some (state tm true [] temp (b :: out)) := by
  change some (TM2.stepAux (prefixProgram tm f d true) (tm.initialState, reset tm)
    (stacks tm [] (b :: temp) out)) = _
  apply congrArg some
  simp [prefixProgram, TM2.stepAux, state, reset, update_temp, update_out]

theorem rewind_nil (out : List (B tm)) :
    (machine tm f d).step (state tm true [] [] out) =
      some (cfg (μ := Bool) (initList tm out) (fun _ : Bool => []) (reset tm)) := by
  change some (TM2.stepAux (prefixProgram tm f d true) (tm.initialState, reset tm)
    (stacks tm [] [] out)) = _
  apply congrArg some
  simp [prefixProgram, TM2.stepAux, cfg, reset, update_temp, stacks] <;>
    (congr 1; funext k; cases k <;> rfl)

private def oneStep {C : Type} {step : C → Option C} {a b : C}
    (h : step a = some b) : StateTransition.EvalsToInTime step a (some b) 1 :=
  { steps := 1, evals_in_steps := by simpa using h, steps_le_m := le_rfl }

theorem scan_run : ∀ (raw : List (Option Bool)) (temp out : List (B tm)),
    Nonempty (StateTransition.EvalsToInTime (machine tm f d).step
      (state tm false raw temp out)
      (some (state tm true [] ((expand tm f raw).reverse ++ temp) out)) (raw.length+1)) := by
  intro raw
  induction raw with
  | nil =>
    intro temp out
    exact ⟨oneStep (scan_nil tm f d temp out)⟩
  | cons a raw ih =>
    intro temp out
    rcases ih ((f a).2 :: (f a).1 :: temp) out with ⟨hr⟩
    have hs := oneStep (scan_cons tm f d a raw temp out)
    have ht := StateTransition.EvalsToInTime.trans (machine tm f d).step 1
      (raw.length+1) _ _ _ hs hr
    simpa [expand, List.reverse_cons, List.append_assoc, Nat.add_assoc] using Nonempty.intro ht

theorem rewind_run : ∀ (temp out : List (B tm)),
    Nonempty (StateTransition.EvalsToInTime (machine tm f d).step
      (state tm true [] temp out)
      (some (cfg (μ := Bool) (initList tm (temp.reverse ++ out))
        (fun _ : Bool => []) (reset tm))) (temp.length+1)) := by
  intro temp
  induction temp with
  | nil =>
    intro out
    exact ⟨oneStep (rewind_nil tm f d out)⟩
  | cons b temp ih =>
    intro out
    rcases ih (b :: out) with ⟨hr⟩
    have hs := oneStep (rewind_cons tm f d b temp out)
    have ht := StateTransition.EvalsToInTime.trans (machine tm f d).step 1
      (temp.length+1) _ _ _ hs hr
    simpa [List.reverse_cons, List.append_assoc, Nat.add_assoc] using Nonempty.intro ht

/-- Actual prefix execution consumes 3n+2 outer TM2 steps. -/
theorem expand_prefix_run (raw : List (Option Bool)) :
    Nonempty (StateTransition.EvalsToInTime (machine tm f d).step
      (initList (machine tm f d) raw)
      (some (cfg (μ := Bool) (initList tm (expand tm f raw))
        (fun _ : Bool => []) (reset tm))) (3*raw.length+2)) := by
  rw [init_eq]
  rcases scan_run tm f d raw [] [] with ⟨hs⟩
  simp only [List.append_nil] at hs
  rcases rewind_run tm f d (expand tm f raw).reverse [] with ⟨hr⟩
  simp only [List.reverse_reverse, List.append_nil, List.length_reverse, expand_length] at hr
  have ht := StateTransition.EvalsToInTime.trans (machine tm f d).step
    (raw.length+1) (2*raw.length+1) _ _ _ hs hr
  exact ⟨by convert ht using 1 <;> omega⟩

#print axioms scan_cons
#print axioms rewind_cons
#print axioms expand_prefix_run
end
end TM2PairExpand
end MathSolve.PNP
