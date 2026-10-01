import Mathlib

namespace Erdos3

-- Same subtype-indexed reciprocal hypothesis as the protected statement.
def R (A : Set ℕ) : Prop := ¬ Summable (fun a : A => 1 / (a : ℝ))

lemma reciprocal_divergent_diff_finite
    {A : Set ℕ} (hA : R A) {F : Set ℕ} (hF : F.Finite) :
    R (A \ F) := by
  classical
  intro hdiff
  have hinter_fin : (A ∩ F).Finite := hF.subset (Set.inter_subset_right A F)
  have hinter_sum : Summable (fun a : (A ∩ F : Set ℕ) => 1 / (a : ℝ)) :=
    hinter_fin.summable (fun n : ℕ => 1 / (n : ℝ))
  obtain ⟨a_val, ha⟩ := hdiff
  obtain ⟨b_val, hb⟩ := hinter_sum
  have hdisj : Disjoint (A \ F) (A ∩ F) := by
    apply Set.disjoint_left.mpr
    intro x hx hy
    exact hx.2 hy.2
  have h_add := HasSum.add_disjoint hdisj ha hb
  rw [Set.sdiff_union_inter] at h_add
  exact hA ⟨a_val + b_val, h_add⟩

lemma reciprocal_divergent_tail
    {A : Set ℕ} (hA : R A) (N : ℕ) :
    R (A ∩ {n : ℕ | N ≤ n}) := by
  have heq : A ∩ {n : ℕ | N ≤ n} = A \ Set.Iio N := by
    ext x
    simp only [Set.mem_inter_iff, Set.mem_setOf_eq, Set.mem_diff, Set.mem_Iio, not_lt]
  rw [heq]
  exact reciprocal_divergent_diff_finite hA (Set.finite_Iio N)

-- A reusable finite-partition lemma, not an arithmetic-progression theorem.
lemma reciprocal_divergent_finite_partition
    {ι : Type*} [Fintype ι] {A : Set ℕ} (hA : R A) (f : ℕ → ι) :
    ∃ r : ι, R {n : ℕ | n ∈ A ∧ f n = r} := by
  classical
  by_contra h
  push_neg at h
  have hi (r : ι) : Summable
      ({n : ℕ | n ∈ A ∧ f n = r}.indicator (fun n : ℕ => 1 / (n : ℝ))) :=
    summable_subtype_iff_indicator.mp (h r)
  have hs := summable_sum (s := Finset.univ) (fun r _ => hi r)
  apply hA
  apply summable_subtype_iff_indicator.mpr
  convert hs using 1
  funext n
  by_cases hn : n ∈ A <;> simp [Set.indicator_apply, hn]

lemma reciprocal_divergent_mod_fiber
    {A : Set ℕ} (hA : R A) {m : ℕ} (hm : 0 < m) :
    ∃ r : Fin m, R {n : ℕ | n ∈ A ∧ n % m = r.val} := by
  let f : ℕ → Fin m := fun n => ⟨n % m, Nat.mod_lt n hm⟩
  obtain ⟨r, hr⟩ := reciprocal_divergent_finite_partition hA f
  refine ⟨r, ?_⟩
  simpa [f, Fin.ext_iff] using hr

#print axioms reciprocal_divergent_diff_finite
#print axioms reciprocal_divergent_tail
#print axioms reciprocal_divergent_finite_partition
#print axioms reciprocal_divergent_mod_fiber

end Erdos3
