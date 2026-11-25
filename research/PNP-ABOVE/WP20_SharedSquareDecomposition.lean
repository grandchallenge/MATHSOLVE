import PNPAbove.WP20Quantum

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Matrix Finset
open scoped Classical

/-- The seven shared register values label 128 independent CHSH squares. -/
abbrev Shared := Fin 7 → 𝔽₂

/-- Reassemble one seed from its seven shared coordinates and two independent
player-private bits, without erasing any of the original nine input cells. -/
def assemble (m : Shared) (a b : 𝔽₂) : Questions :=
  fun i =>
    if h0 : i = 0 then a
    else if h8 : i = 8 then b
    else m ⟨i.val-1, by
      have h8v : i.val ≠ 8 := by
        intro h
        exact h8 (Fin.ext h)
      have hlt : i.val < 9 := i.isLt
      omega⟩

/-- Exact left inverse of the nine-source-bit assembly. -/
theorem assemble_extract (z : Questions) :
    assemble (fun i : Fin 7 => z ⟨i.val+1, by omega⟩) (z 0) (z 8) = z := by
  funext i
  fin_cases i <;> simp [assemble]

/-- Exact right inverse. -/
theorem extract_assemble_middle (m : Shared) (a b : 𝔽₂) :
    (fun i : Fin 7 => (assemble m a b) ⟨i.val+1, by omega⟩) = m := by
  funext i
  fin_cases i <;> simp [assemble]

theorem extract_assemble_left (m : Shared) (a b : 𝔽₂) :
    (assemble m a b) 0 = a := by simp [assemble]

theorem extract_assemble_right (m : Shared) (a b : 𝔽₂) :
    (assemble m a b) 8 = b := by simp [assemble]

/-- Bijection: exactly 128 shared configurations times four private settings
equals all 512 original nine-bit seeds. -/
def seedsEquiv : Questions ≃ Shared × (𝔽₂ × 𝔽₂) where
  toFun z := ((fun i : Fin 7 => z ⟨i.val+1, by omega⟩), (z 0,z 8))
  invFun v := assemble v.1 v.2.1 v.2.2
  left_inv z := assemble_extract z
  right_inv v := by
    rcases v with ⟨m,⟨a,b⟩⟩
    apply Prod.ext
    · exact extract_assemble_middle m a b
    · exact Prod.ext (extract_assemble_left m a b)
        (extract_assemble_right m a b)

def leftQ (m : Shared) (a : 𝔽₂) : Questions :=
  aliceCL.eval (assemble m a 0)

def rightQ (m : Shared) (b : 𝔽₂) : Questions :=
  bobCL.eval (assemble m 0 b)

theorem alice_assemble (m : Shared) (a b : 𝔽₂) :
    aliceCL.eval (assemble m a b) = leftQ m a := by
  rw [alice_eval]
  funext i
  fin_cases i <;> simp [leftQ, alice_eval, assemble]

theorem bob_assemble (m : Shared) (a b : 𝔽₂) :
    bobCL.eval (assemble m a b) = rightQ m b := by
  rw [bob_eval]
  funext i
  fin_cases i <;> simp [rightQ, bob_eval, assemble]

theorem leftQ_distinct (m : Shared) : leftQ m 0 ≠ leftQ m 1 := by
  intro h
  have ht := congrFun h (0:Fin 9)
  norm_num [leftQ, alice_eval, assemble] at ht

theorem rightQ_distinct (m : Shared) : rightQ m 0 ≠ rightQ m 1 := by
  intro h
  have ht := congrFun h (8:Fin 9)
  norm_num [rightQ, bob_eval, assemble] at ht

/-- Every one of the 128 components contains four original equally-weighted
CL question pairs (not just a sampled witness square). -/
theorem every_component_has_four_edges (m : Shared) (a b : 𝔽₂) :
    clDist aliceCL.eval bobCL.eval (leftQ m a) (rightQ m b) =
      (1/512 : ℝ) := by
  rw [← alice_assemble m a b, ← bob_assemble m a b]
  exact exact_original_mass (assemble m a b)

/-- The four exact CHSH constraints on *each* shared-register component are
jointly inconsistent for any global deterministic classical response. -/
theorem every_component_classical_bound (f : Questions → Bool) (m : Shared) :
    (if (f (leftQ m 0)).xor (f (rightQ m 0)) = false
        then (1:ℝ) else 0) +
    (if (f (leftQ m 0)).xor (f (rightQ m 1)) = false
        then (1:ℝ) else 0) +
    (if (f (leftQ m 1)).xor (f (rightQ m 0)) = false
        then (1:ℝ) else 0) +
    (if (f (leftQ m 1)).xor (f (rightQ m 1)) = true
        then (1:ℝ) else 0) ≤ 3 :=
  chsh_four_classical_bound _ _ _ _

theorem shared_card : Fintype.card Shared = 128 := by
  have h : Fintype.card 𝔽₂ = 2 := by decide
  simp [Shared, h]

end PNPAbove.WP20
