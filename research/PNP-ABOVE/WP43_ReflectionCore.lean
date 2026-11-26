import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring

namespace PNPAbove.WP43
open scoped BigOperators

variable {A B : Type*} [CommRing A] [CommRing B]

def boolAxiom (x : A) : A := x ^ 2 - x

def bitValue (a : Bool) : A := if a then 1 else 0

def bitSelector (x : A) (a : Bool) : A := if a then x else 1 - x

def bitSign (a : Bool) : A := if a then 1 else -1

theorem bitValue_axiom (a : Bool) :
    boolAxiom (bitValue (A := A) a) = 0 := by
  cases a <;> simp [boolAxiom, bitValue]

theorem selector_delta (x : A) (a : Bool) :
    bitSelector x a * (x - bitValue a) =
      bitSign a * boolAxiom x := by
  cases a <;> simp [bitSelector, bitValue, bitSign, boolAxiom] <;> ring

theorem difference_product {ι : Type*} [Fintype ι]
    (u u' v v' : A) (d p q : ι → A)
    (hu : u-u' = ∑ i, d i * p i)
    (hv : v-v' = ∑ i, d i * q i) :
    u*v-u'*v' = ∑ i, d i * (u*q i + v'*p i) := by
  calc
    u*v-u'*v' = u*(v-v') + v'*(u-u') := by ring
    _ = u*(∑ i, d i*q i) + v'*(∑ i, d i*p i) := by rw [hu,hv]
    _ = ∑ i, d i * (u*q i+v'*p i) := by
      rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
      apply Finset.sum_congr rfl
      intro i _
      ring

theorem selector_prod_delta {ι : Type*} [Fintype ι] [DecidableEq ι]
    (u : ι → A) (a : ι → Bool) (i : ι) :
    (∏ j, bitSelector (u j) (a j)) * (u i-bitValue (a i)) =
      boolAxiom (u i) *
        (bitSign (a i) * ∏ j ∈ Finset.univ.erase i, bitSelector (u j) (a j)) := by
  have h := Finset.prod_erase_mul (s := Finset.univ)
    (f := fun j => bitSelector (u j) (a j)) (Finset.mem_univ i)
  rw [← h]
  calc
    ((∏ j ∈ Finset.univ.erase i, bitSelector (u j) (a j)) *
        bitSelector (u i) (a i)) * (u i-bitValue (a i)) =
      (∏ j ∈ Finset.univ.erase i, bitSelector (u j) (a j)) *
        (bitSelector (u i) (a i) * (u i-bitValue (a i))) := by ring
    _ = _ := by rw [selector_delta]; ring

theorem singleton_lift {ι κ : Type*} [Fintype ι] [Fintype κ] [DecidableEq ι]
    (u : ι → A) (a : ι → Bool) (x : κ → A)
    (V S : A) (D : ι → A) (H : κ → A)
    (hd : V-S = ∑ i, (u i-bitValue (a i))*D i)
    (hs : S = ∑ j, boolAxiom (x j)*H j) :
    (∏ i, bitSelector (u i) (a i))*V =
      (∑ i, boolAxiom (u i) *
        (bitSign (a i) * (∏ k ∈ Finset.univ.erase i, bitSelector (u k) (a k)) * D i)) +
      ∑ j, boolAxiom (x j)*((∏ i, bitSelector (u i) (a i))*H j) := by
  let E := ∏ i, bitSelector (u i) (a i)
  change E*V = _
  calc
    E*V = E*(V-S)+E*S := by ring
    _ = E*(∑ i, (u i-bitValue (a i))*D i)+E*(∑ j, boolAxiom (x j)*H j) := by rw [hd,hs]
    _ = _ := by
      rw [Finset.mul_sum, Finset.mul_sum]
      congr 1
      · apply Finset.sum_congr rfl
        intro i _
        rw [← mul_assoc]
        change ((∏ k, bitSelector (u k) (a k))*(u i-bitValue (a i)))*D i = _
        rw [selector_prod_delta]
        ring
      · apply Finset.sum_congr rfl
        intro j _
        ring

theorem reflection_specialization {ι τ κ : Type*}
    [Fintype ι] [Fintype τ] [Fintype κ]
    (f : A →+* B) (u : ι → A) (w : τ → A) (x : κ → A)
    (R V : A) (U : ι → A) (W : τ → A) (H : κ → A)
    (hr : R*V = (∑ i, boolAxiom (u i)*U i) +
      (∑ k, boolAxiom (w k)*W k) + ∑ j, boolAxiom (x j)*H j)
    (ha : ∀ i, boolAxiom (f (u i)) = 0)
    (ht : ∀ k, boolAxiom (f (w k)) = 0)
    (hR : f R = 1) :
    f V = ∑ j, boolAxiom (f (x j))*f (H j) := by
  have h := congrArg f hr
  simp only [map_mul, map_add, map_sum, boolAxiom, map_sub, map_pow] at h
  have hau : ∀ i, f (u i)^2-f (u i) = 0 := ha
  have htw : ∀ k, f (w k)^2-f (w k) = 0 := ht
  simpa [hR,hau,htw,boolAxiom] using h

end PNPAbove.WP43
