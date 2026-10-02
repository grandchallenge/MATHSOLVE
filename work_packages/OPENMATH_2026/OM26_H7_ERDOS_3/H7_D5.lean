import FormalConjecturesUtil
import Mathlib.Analysis.SumOverResidueClass

namespace Erdos3

def ReciprocalDivergent (A : Set Nat) : Prop :=
  ¬ Summable (fun a : A => 1 / (a : Real))

private noncomputable def recip (n : Nat) : Real := 1 / (n : Real)

lemma reciprocal_divergent_diff_finite
    {A : Set Nat} (hA : ReciprocalDivergent A) {F : Set Nat} (hF : F.Finite) :
    ReciprocalDivergent (A \ F) := by
  intro hdiff
  apply hA
  have hdiff' : Summable ((A \ F).indicator recip) := by
    exact summable_subtype_iff_indicator.mp hdiff
  have hcomp : Summable (Fᶜ.indicator (A.indicator recip)) := by
    simpa only [Set.indicator_indicator, Set.compl_inter, Set.diff_eq, Set.inter_comm] using hdiff'
  have hcomp_sub : Summable (fun x : {n : Nat // n ∈ Fᶜ} => A.indicator recip x) :=
    summable_subtype_iff_indicator.mpr hcomp
  have hAind : Summable (A.indicator recip) :=
    hF.summable_compl_iff.mp hcomp_sub
  have hAsub : Summable (fun a : A => recip a) :=
    summable_subtype_iff_indicator.mpr hAind
  simpa [recip] using hAsub

lemma reciprocal_divergent_tail
    {A : Set Nat} (hA : ReciprocalDivergent A) (N : Nat) :
    ReciprocalDivergent (A ∩ {n : Nat | N ≤ n}) := by
  have hIio_fin : (Set.Iio N).Finite := Set.finite_Iio N
  have heq : A ∩ {n : Nat | N ≤ n} = A \ Set.Iio N := by
    ext x
    simp only [Set.mem_inter_iff, Set.mem_setOf_eq, Set.mem_diff, Set.mem_Iio, not_lt]
  rw [heq]
  exact reciprocal_divergent_diff_finite hA hIio_fin

lemma reciprocal_divergent_zmod_fiber
    {A : Set Nat} (hA : ReciprocalDivergent A) {m : Nat} (hm : 0 < m) :
    ∃ r : ZMod m, ReciprocalDivergent {n : Nat | n ∈ A ∧ (n : ZMod m) = r} := by
  letI : NeZero m := ⟨Nat.ne_of_gt hm⟩
  by_contra h
  simp only [not_exists, ReciprocalDivergent, not_not] at h
  apply hA
  have hAind : Summable (A.indicator recip) := by
    rw [Finset.sum_indicator_mod m (A.indicator recip)]
    convert!
      summable_sum (s := Finset.univ) fun r _ => by
        have hr_sub :
            Summable (fun a : {n : Nat | n ∈ A ∧ (n : ZMod m) = r} => recip a) := by
          simpa [recip] using h r
        have hr_ind :
            Summable ({n : Nat | n ∈ A ∧ (n : ZMod m) = r}.indicator recip) :=
          summable_subtype_iff_indicator.mp hr_sub
        have hset :
            {n : Nat | n ∈ A ∧ (n : ZMod m) = r} =
              A ∩ {n : Nat | (n : ZMod m) = r} := by
          ext n
          simp
        rw [hset] at hr_ind
        simpa only [Set.indicator_indicator, Set.inter_comm] using hr_ind
    simp only [Finset.sum_apply, Set.indicator_indicator, Set.inter_comm]
  have hAsub : Summable (fun a : A => recip a) :=
    summable_subtype_iff_indicator.mpr hAind
  simpa [recip] using hAsub

#print axioms reciprocal_divergent_diff_finite
#print axioms reciprocal_divergent_tail
#print axioms reciprocal_divergent_zmod_fiber

end Erdos3
