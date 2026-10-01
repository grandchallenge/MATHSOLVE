import FormalConjecturesUtil

namespace Erdos3

lemma ap_subprogression_of_le
    {A S : Set ℕ} {m k : ℕ}
    (hS : S ⊆ A) (hAP : S.IsAPOfLength k) (hmk : m ≤ k) :
    ∃ T ⊆ A, T.IsAPOfLength m := by
  rcases hAP with ⟨a, d, hcard, hset⟩
  let I : Set ℕ := Set.Iio k
  let J : Set ℕ := Set.Iio m
  let f : ℕ → ℕ := fun n => a + n • d
  have hSI : S = f '' I := by
    rw [hset]
    ext x
    simp [I, f]
  have hIfin : I.Finite := Set.finite_Iio k
  have hIcard : I.encard = k := by
    simp [I]
  have himagecard : (f '' I).encard = I.encard := by
    rw [← hSI, hcard, hIcard]
  have hfinj : Set.InjOn f I := hIfin.injOn_of_encard_image_eq himagecard
  have hJI : J ⊆ I := by
    intro n hn
    simp only [J, I, Set.mem_Iio] at hn ⊢
    exact lt_of_lt_of_le hn hmk
  let T : Set ℕ := f '' J
  refine ⟨T, ?_, ?_⟩
  · intro x hx
    apply hS
    rw [hSI]
    rcases hx with ⟨n, hn, rfl⟩
    exact ⟨n, hJI hn, rfl⟩
  · refine ⟨a, d, ?_, ?_⟩
    · change T.encard = (m : ℕ∞)
      rw [show T = f '' J by rfl, (hfinj.mono hJI).encard_image]
      simp [J]
    · ext x
      simp [T, J, f]

#print axioms ap_subprogression_of_le

end Erdos3
