import PNPAbove.WP20Law

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Finset
open scoped Classical

/-- The source CHSH bit for a GCL field bit. -/
def bit (z : 𝔽₂) : Bool := decide (z = 1)

/-- A synchronous, answer-sensitive *mathematical* CHSH acceptance rule,
with binary answers. Source Cost.Prog realization is a distinct obligation. -/
def parityAccept (x y : Questions) (a b : Bool) : Bool :=
  decide (a.xor b = (bit (x 0) && bit (y 8))) &&
    (if x = y then decide (a = b) else true)

/-- The rule is synchronous on **all** questions (including unsampled ones). -/
theorem parityAccept_synchronous (x : Questions) (a b : Bool) (hne : a ≠ b) :
    parityAccept x x a b = false := by
  simp [parityAccept, hne]

/-- The actual CL source questions induce the CHSH parity check, even when
Alice's and Bob's original questions happen to coincide. -/
theorem parityAccept_source (z : Questions) (a b : Bool) :
    parityAccept (aliceCL.eval z) (bobCL.eval z) a b =
      decide (a.xor b = (bit (z 0) && bit (z 8))) := by
  rw [alice_eval, bob_eval]
  by_cases he : (fun i : Fin 9 => if i = 8 then 0 else z i) =
      (fun i : Fin 9 => if i = 0 then 0 else z i)
  · have h0 : z 0 = 0 := by
      have ht := congrFun he (0 : Fin 9)
      simpa using ht
    have h8 : z 8 = 0 := by
      have ht := congrFun he (8 : Fin 9)
      simpa using ht.symm
    cases a <;> cases b <;>
      simp [parityAccept, bit, he, h0, h8]
  · simp [parityAccept, bit, he]
    rfl

/-- The four Bell-square parity constraints are inconsistent under every
classical deterministic assignment. This is the exact four-input CHSH
classical bound; the 16 possible assignments are checked by Lean. -/
theorem chsh_four_classical_bound (a0 a1 b0 b1 : Bool) :
    (if a0.xor b0 = false then (1 : ℝ) else 0) +
    (if a0.xor b1 = false then (1 : ℝ) else 0) +
    (if a1.xor b0 = false then (1 : ℝ) else 0) +
    (if a1.xor b1 = true then (1 : ℝ) else 0) ≤ 3 := by
  cases a0 <;> cases a1 <;> cases b0 <;> cases b1 <;>
    norm_num [Bool.xor]

/-- Apply the CHSH inconsistency to the four original nonzero-mass edges. -/
theorem square_classical_bound (f : Questions → Bool) :
    (if (f (left 0)).xor (f (right 0)) = false then (1 : ℝ) else 0) +
    (if (f (left 0)).xor (f (right 1)) = false then (1 : ℝ) else 0) +
    (if (f (left 1)).xor (f (right 0)) = false then (1 : ℝ) else 0) +
    (if (f (left 1)).xor (f (right 1)) = true then (1 : ℝ) else 0) ≤ 3 :=
  chsh_four_classical_bound _ _ _ _

/-- There is no deterministic assignment winning all four sampled edges. -/
theorem square_has_classical_loss (f : Questions → Bool) :
    ¬ ((f (left 0)).xor (f (right 0)) = false ∧
       (f (left 0)).xor (f (right 1)) = false ∧
       (f (left 1)).xor (f (right 0)) = false ∧
       (f (left 1)).xor (f (right 1)) = true) := by
  intro h
  have hh := square_classical_bound f
  simp [h.1, h.2.1, h.2.2.1, h.2.2.2] at hh
  norm_num at hh

end PNPAbove.WP20
