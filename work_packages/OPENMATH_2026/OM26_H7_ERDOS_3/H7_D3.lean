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
  have hIcard : I.encard = (k : ℕ∞) := by
    rw [hIfin.encard_eq_coe_toFinset_card]
    simp [I]
  have hScard : S.encard = (k : ℕ∞) := by
    simpa only [ENat.card_coe_set_eq] using hcard
  have himagecard : (f '' I).encard = I.encard := by
    rw [← hSI]
    exact hScard.trans hIcard.symm
  have hfinj : Set.InjOn f I := hIfin.injOn_of_encard_image_eq himagecard
  have hJI : J ⊆ I := by
    intro n hn
    simp only [J, I, Set.mem_Iio] at hn ⊢
    exact lt_of_lt_of_le hn hmk
  have hJfin : J.Finite := Set.finite_Iio m
  have hJcard : J.encard = (m : ℕ∞) := by
    rw [hJfin.encard_eq_coe_toFinset_card]
    simp [J]
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
      exact hJcard
    · ext x
      simp [T, J, f]

#print axioms ap_subprogression_of_le

end Erdos3
