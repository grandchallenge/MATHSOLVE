import PNPAbove.WP23BConcrete
import MIPRE.Foundations.SAT.Flatten
import MIPRE.Foundations.GameTransport

/-!
A genuine formula-dependent game, over the original MIPRE Games and SAT.Fml
interfaces. This is a formal game-model construction, not yet a Cost.Prog
normal-form Verifier 7; that separate compiler obligation is explicit.
-/

namespace PNPAbove.WP24
open MIPRE MIPRE.SAT MIPRE.Cost

/-- Read a finite assignment as an infinite assignment with false padding. -/
def bitsAt (w : Fin n → Bool) (i : Nat) : Bool :=
  if h : i < n then w ⟨i, h⟩ else false

@[simp]
theorem bitsAt_fin (w : Fin n → Bool) (i : Fin n) :
    bitsAt w i.val = w i := by
  simp [bitsAt, i.isLt]

/-- Instance-dependent satisfiability, including arbitrary unsatisfiable formulas. -/
def Satisfiable (n : Nat) (f : SAT.Fml) : Prop :=
  ∃ w : Fin n → Bool, f.eval (bitsAt w) = true

/-- An original MIPRE synchronous game: the two provers return assignments,
and a joint success is only possible if the instance is satisfied. -/
noncomputable def satGame (n : Nat) (f : SAT.Fml) :
    MIPRE.SynchronousGame Unit (Fin n → Bool) where
  μ := fun _ _ => 1
  μ_nonneg := by intro _ _; norm_num
  μ_sum_one := by simp
  D := fun _ _ a b => f.eval (bitsAt a) && decide (a = b)
  synchronous := by
    intro _ a b hab
    simp [hab]

/-- The native game predicate accepts precisely a satisfying, common response. -/
theorem accepts_iff (n : Nat) (f : SAT.Fml) (a b : Fin n → Bool) :
    (satGame n f).D () () a b = true ↔
      f.eval (bitsAt a) = true ∧ a = b := by
  simp [satGame, Bool.and_eq_true]

/-- Exact classical witness transfer, in both directions. -/
theorem exists_accepted_iff_sat (n : Nat) (f : SAT.Fml) :
    (∃ a b : Fin n → Bool, (satGame n f).D () () a b = true) ↔
    Satisfiable n f := by
  constructor
  · rintro ⟨a, b, hab⟩
    exact ⟨a, (accepts_iff n f a b).mp hab |>.1⟩
  · rintro ⟨w, hw⟩
    exact ⟨w, w, (accepts_iff n f w w).mpr ⟨hw, rfl⟩⟩

/-- A satisfiable instance admits an actual original MIPRE PCC strategy
with winning probability exactly one, not merely a combinatorial witness. -/
theorem perfectPCC_of_sat (n : Nat) (f : SAT.Fml)
    (h : Satisfiable n f) :
    ∃ S : MIPRE.SyncStrategy (satGame n f), S.IsPCC ∧ S.value = 1 := by
  obtain ⟨w, hw⟩ := h
  refine ⟨MIPRE.SyncStrategy.const (satGame n f) w,
    MIPRE.SyncStrategy.isPCC_const (satGame n f) w, ?_⟩
  rw [MIPRE.SyncStrategy.value_const]
  simp [satGame, hw]

/-- An unsatisfiable instance has *zero quantum value*: no answer pair can win. -/
theorem quantum_zero_of_unsat (n : Nat) (f : SAT.Fml)
    (h : ¬ Satisfiable n f) :
    MIPRE.quantumValue (satGame n f).toGame = 0 := by
  apply MIPRE.quantumValue_eq_zero_of_reject
  intro x y a b
  have ha : f.eval (bitsAt a) = false := by
    cases ha : f.eval (bitsAt a) with
    | false => rfl
    | true => exact False.elim (h ⟨a, ha⟩)
  simp [MIPRE.SynchronousGame.toGame, satGame, ha]

/-- A satisfiable instance has *quantum value exactly one* in the original
finite-dimensional tensor-product model. -/
theorem quantum_one_of_sat (n : Nat) (f : SAT.Fml)
    (h : Satisfiable n f) :
    MIPRE.quantumValue (satGame n f).toGame = 1 := by
  obtain ⟨S, _, hv⟩ := perfectPCC_of_sat n f h
  apply le_antisymm (MIPRE.quantumValue_le_one _)
  calc
    1 = S.value := hv.symm
    _ ≤ MIPRE.syncValue (satGame n f) :=
      le_ciSup (MIPRE.SyncStrategy.bddAbove_range_value _) S
    _ ≤ MIPRE.quantumValue (satGame n f).toGame :=
      MIPRE.syncValue_le_quantumValue _

/-- Exact formula-dependent promise, no conjectural gap estimate. -/
theorem quantum_value_eq_one_iff_sat (n : Nat) (f : SAT.Fml) :
    MIPRE.quantumValue (satGame n f).toGame = 1 ↔ Satisfiable n f := by
  constructor
  · intro hv
    by_contra h
    have hz := quantum_zero_of_unsat n f h
    rw [hz] at hv
    norm_num at hv
  · exact quantum_one_of_sat n f

/-- Perfect PCC completeness is also *necessary*: a perfect strategy
for this game exists only when there is a satisfying Boolean assignment. -/
theorem perfectPCC_iff_sat (n : Nat) (f : SAT.Fml) :
    (∃ S : MIPRE.SyncStrategy (satGame n f),
        S.IsPCC ∧ S.value = 1) ↔ Satisfiable n f := by
  constructor
  · rintro ⟨S, _, hS⟩
    apply (quantum_value_eq_one_iff_sat n f).mp
    apply le_antisymm (MIPRE.quantumValue_le_one _)
    calc
      1 = S.value := hS.symm
      _ ≤ MIPRE.syncValue (satGame n f) :=
        le_ciSup (MIPRE.SyncStrategy.bddAbove_range_value _) S
      _ ≤ MIPRE.quantumValue (satGame n f).toGame :=
        MIPRE.syncValue_le_quantumValue _
  · exact perfectPCC_of_sat n f

/-- Stronger than the original compression soundness threshold, *at the
game level*: the unsatisfiable game has value zero, hence at most half. -/
theorem soundness_half_of_unsat (n : Nat) (f : SAT.Fml)
    (h : ¬ Satisfiable n f) :
    MIPRE.quantumValue (satGame n f).toGame ≤ (1 / 2 : Real) := by
  rw [quantum_zero_of_unsat n f h]
  norm_num

/-- The ORIGINAL pinned Lean program, not an abstract algorithm, compiles
Boolean formulas to circuits with an explicit polynomial Cost.Prog bound. -/
noncomputable def uniformCircuit :
    MIPRE.Cost.PolyTimeFun (Nat × SAT.Fml) SAT.Circuit :=
  SAT.Fml.toCircuitF

/-- The constructed circuit has precisely the original formula semantics. -/
theorem uniformCircuit_correct (n : Nat) (f : SAT.Fml)
    (w : Fin n → Bool) :
    (uniformCircuit (n, f)).eval (bitsAt w) = f.eval (bitsAt w) := by
  exact SAT.Fml.eval_toCircuit n f (bitsAt w)

/-- The witness includes the actual original interpreter and an explicit
polynomial in the source encoding size, not a complexity assertion in prose. -/
theorem uniformCircuit_polytime (p : Nat × SAT.Fml) :
    ∃ t ≤ uniformCircuit.timeBound.eval (esize p),
      uniformCircuit.code.Runs (encode p) (encode (uniformCircuit p)) t :=
  uniformCircuit.computes p

end PNPAbove.WP24
