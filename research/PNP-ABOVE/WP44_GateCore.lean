import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring

namespace PNPAbove.WP44
open scoped BigOperators
variable {A : Type*} [CommRing A]

def b (x : A) := x^2-x

theorem and_relation (z u v : A) :
    z-u*v = z*(1-u)+u*(z*(1-v))-(1-z)*u*v := by ring

theorem not_relation (z u : A) :
    z-(1-u) = z*u-(1-z)*(1-u) := by ring

theorem defect_mul (u v : A) :
    b (u*v) = v^2*b u+u*b v := by unfold b; ring

theorem defect_not (u : A) : b (1-u) = b u := by unfold b; ring

theorem and_substitution (u v : A) :
    (u*v)*(1-u) = -v*b u ∧
    (u*v)*(1-v) = -u*b v ∧
    (1-u*v)*u*v = -b (u*v) := by
  unfold b
  constructor
  · ring
  constructor <;> ring

theorem not_substitution (u : A) :
    (1-u)*u = -b u ∧ (1-(1-u))*(1-u) = -b u := by
  unfold b
  constructor <;> ring

theorem propagate_and (z u v g h : A) :
    z-g*h = (z-u*v)+u*(v-h)+h*(u-g) := by ring

theorem propagate_not (z u g : A) :
    z-(1-g) = (z-(1-u))-(u-g) := by ring

theorem reverse_lift {ι : Type*} [Fintype ι]
    (g U : A) (x L D : ι → A)
    (h : 1 = U*(1-g)+∑ i, b (x i)*L i)
    (hd : b g = ∑ i, b (x i)*D i) :
    g = ∑ i, b (x i)*(g*L i-U*D i) := by
  calc
    g = g*(U*(1-g)+∑ i, b (x i)*L i) := by rw [← h, mul_one]
    _ = g*(∑ i, b (x i)*L i)-U*b g := by unfold b; ring
    _ = _ := by
      rw [hd,Finset.mul_sum,Finset.mul_sum,← Finset.sum_sub_distrib]
      apply Finset.sum_congr rfl
      intro i _
      ring

theorem forward_lift {ι κ : Type*} [Fintype ι] [Fintype κ]
    (z g : A) (c V : ι → A) (x H : κ → A)
    (h : z-g = ∑ i, c i*V i)
    (hg : g = ∑ j, b (x j)*H j) :
    (1:A) = (1-z)+(∑ i, c i*V i)+∑ j, b (x j)*H j := by
  rw [← h,← hg]
  ring

end PNPAbove.WP44

#print axioms PNPAbove.WP44.and_relation
#print axioms PNPAbove.WP44.not_relation
#print axioms PNPAbove.WP44.defect_mul
#print axioms PNPAbove.WP44.defect_not
#print axioms PNPAbove.WP44.and_substitution
#print axioms PNPAbove.WP44.not_substitution
#print axioms PNPAbove.WP44.propagate_and
#print axioms PNPAbove.WP44.propagate_not
#print axioms PNPAbove.WP44.reverse_lift
#print axioms PNPAbove.WP44.forward_lift
