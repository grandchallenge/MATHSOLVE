import PNPAbove.WP19Native

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Finset
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

abbrev Questions := Fin 9 → 𝔽₂

/-- Each of the nine registers is occupied, while one chosen register is
masked to zero by a (still genuine) linear stage map. -/
def maskedTail : (is : List (Fin 9)) → (kill : Fin 9) →
    CLFun 𝔽₂ (Fin 9) is.length
  | [], _ => .zero
  | i :: is, kill =>
      .cons {i} (if i = kill then 0 else RegLinear.id {i})
        (fun _ => maskedTail is kill)

/-- Alice reads bits 0..7 and ignores bit 8, with nine occupied stages. -/
def aliceCL : CLFun 𝔽₂ (Fin 9) 9 :=
  .cons {0} (RegLinear.id {0})
    (fun _ => maskedTail WP14.tailCoordinates 8)

/-- Bob ignores bit 0 and reads bits 1..8, with nine occupied stages. -/
def bobCL : CLFun 𝔽₂ (Fin 9) 9 :=
  .cons {0} 0 (fun _ => WP14.tailChain WP14.tailCoordinates true)

/-- Source-native conditional-linear semantics of Alice's player question. -/
theorem alice_eval (z : Questions) :
    aliceCL.eval z = (fun i : Fin 9 => if i = 8 then 0 else z i) := by
  funext i
  fin_cases i <;>
    simp [aliceCL, maskedTail, WP14.tailCoordinates,
      CLFun.eval, RegLinear.id_apply, proj_apply, Finset.mem_singleton]

/-- Source-native conditional-linear semantics of Bob's player question. -/
theorem bob_eval (z : Questions) :
    bobCL.eval z = (fun i : Fin 9 => if i = 0 then 0 else z i) := by
  funext i
  fin_cases i <;>
    simp [bobCL, WP14.tailChain, WP14.tailCoordinates,
      CLFun.eval, RegLinear.id_apply, proj_apply, Finset.mem_singleton]

/-- Every register remains occupied, despite exactly one suppressed
measurement per player. This is no empty-register padding. -/
theorem alice_factor (j : Nat) (h1 : 1 ≤ j) (h9 : j ≤ 9)
    (u : Questions) :
    aliceCL.factorOfPrefix (j-1) u =
      ({⟨j-1, by omega⟩} : Finset (Fin 9)) := by
  interval_cases j <;>
    simp [aliceCL, maskedTail, WP14.tailCoordinates]

theorem bob_factor (j : Nat) (h1 : 1 ≤ j) (h9 : j ≤ 9)
    (u : Questions) :
    bobCL.factorOfPrefix (j-1) u =
      ({⟨j-1, by omega⟩} : Finset (Fin 9)) := by
  interval_cases j <;>
    simp [bobCL, WP14.tailChain, WP14.tailCoordinates]

/-- The masked chain still partitions exactly its indicated factor set. -/
theorem maskedTail_exact (is : List (Fin 9)) (hd : is.Nodup)
    (kill : Fin 9) :
    (maskedTail is kill).ExactlyOn is.toFinset := by
  induction is with
  | nil => rfl
  | cons i is ih =>
      have hi : i ∉ is := (List.nodup_cons.mp hd).1
      have his : is.Nodup := (List.nodup_cons.mp hd).2
      change ({i} : Finset (Fin 9)) ⊆ (i :: is).toFinset ∧
        ∀ v, (maskedTail is kill).ExactlyOn ((i :: is).toFinset \ {i})
      constructor
      · simp
      · intro v
        have hdiff : (i :: is).toFinset \ ({i} : Finset (Fin 9)) = is.toFinset := by
          ext x
          constructor
          · intro hx
            rcases Finset.mem_sdiff.mp hx with ⟨hm, hne⟩
            rcases Finset.mem_insert.mp (by simpa only [List.toFinset_cons] using hm) with heq | hmem
            · exact False.elim (hne (by simpa [heq]))
            · exact hmem
          · intro hx
            apply Finset.mem_sdiff.mpr
            constructor
            · simpa only [List.toFinset_cons] using Finset.mem_insert_of_mem hx
            · simp only [Finset.mem_singleton]
              intro hxi
              exact hi (by simpa [hxi] using hx)
        simpa only [hdiff] using ih his

/-- Native source level-count and partition requirements on both players. -/
theorem alice_exact : aliceCL.ExactlyOn (Finset.univ : Finset (Fin 9)) := by
  change ({0} : Finset (Fin 9)) ⊆ Finset.univ ∧
    ∀ v, (maskedTail WP14.tailCoordinates 8).ExactlyOn (Finset.univ \ {0})
  constructor
  · exact Finset.subset_univ _
  · intro v
    have h := maskedTail_exact WP14.tailCoordinates (by decide) 8
    have heq : WP14.tailCoordinates.toFinset =
        Finset.univ \ ({0} : Finset (Fin 9)) := by decide
    simpa only [← heq] using h

theorem bob_exact : bobCL.ExactlyOn (Finset.univ : Finset (Fin 9)) := by
  change ({0} : Finset (Fin 9)) ⊆ Finset.univ ∧
    ∀ v, (WP14.tailChain WP14.tailCoordinates true).ExactlyOn (Finset.univ \ {0})
  constructor
  · exact Finset.subset_univ _
  · intro v
    have h := WP14.tailChain_exactlyOn WP14.tailCoordinates (by decide) true
    have heq : WP14.tailCoordinates.toFinset =
        Finset.univ \ ({0} : Finset (Fin 9)) := by decide
    simpa only [← heq] using h

/-- Two independent input bits vary the left and right vertices of a square;
the remaining seven shared coordinates label 128 disjoint square components. -/
def seed (a b : 𝔽₂) : Questions :=
  fun i => if i = 0 then a else if i = 8 then b else 0

def left (a : 𝔽₂) : Questions := aliceCL.eval (seed a 0)
def right (b : 𝔽₂) : Questions := bobCL.eval (seed 0 b)

theorem left_seed (a b : 𝔽₂) : aliceCL.eval (seed a b) = left a := by
  rw [alice_eval]
  funext i
  fin_cases i <;> simp [seed, left, alice_eval]

theorem right_seed (a b : 𝔽₂) : bobCL.eval (seed a b) = right b := by
  rw [bob_eval]
  funext i
  fin_cases i <;> simp [seed, right, bob_eval]

theorem left_distinct : left 0 ≠ left 1 := by
  intro h
  have ht := congrFun h (0 : Fin 9)
  norm_num [left, alice_eval, seed] at ht

theorem right_distinct : right 0 ≠ right 1 := by
  intro h
  have ht := congrFun h (8 : Fin 9)
  norm_num [right, bob_eval, seed] at ht

/-- All four edges of one square occur with positive probability in the exact
original conditional-linear question distribution. -/
theorem square_edge_positive (a b : 𝔽₂) :
    0 < clDist aliceCL.eval bobCL.eval (left a) (right b) := by
  classical
  unfold clDist
  have hmem : seed a b ∈
      (Finset.univ.filter (fun z : Questions =>
        aliceCL.eval z = left a ∧ bobCL.eval z = right b)) := by
    simp [left_seed, right_seed]
  have hc : (0 : ℝ) <
      ((Finset.univ.filter (fun z : Questions =>
        aliceCL.eval z = left a ∧ bobCL.eval z = right b)).card : ℝ) := by
    exact_mod_cast Finset.card_pos.mpr ⟨seed a b, hmem⟩
  have hd : (0 : ℝ) < Fintype.card Questions := by
    exact_mod_cast Fintype.card_pos
  exact div_pos hc hd

/-- An original CL joint question mapping has a genuine four-cycle.
This is incompatible with the WP19 star-plus-isolated-matching criterion. -/
theorem original_cl_four_cycle :
    left 0 ≠ left 1 ∧ right 0 ≠ right 1 ∧
    (∀ a b : 𝔽₂,
      0 < clDist aliceCL.eval bobCL.eval (left a) (right b)) :=
  ⟨left_distinct, right_distinct, square_edge_positive⟩

end PNPAbove.WP20
