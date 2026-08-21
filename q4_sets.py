roll_no = "1024170404"
digits = [int(d) for d in roll_no][:8]

A = {d * 7 for d in digits}
B = {d * 9 for d in digits}
print("Set A =", A)
print("Set B =", B)

union_ab = A.union(B)
print("vi. Union A ∪ B:", union_ab)

intersection_ab = A.intersection(B)
print("vii. Intersection A ∩ B:", intersection_ab)

diff_a_minus_b = A.difference(B)
diff_b_minus_a = B.difference(A)
print("viii. A - B:", diff_a_minus_b)
print("viii. B - A:", diff_b_minus_a)
print("viii. difference() gives values only in one set relative to the other (one direction at a time), while symmetric_difference() gives all values that are in exactly one of the two sets combined (both directions at once).")

sym_diff = A.symmetric_difference(B)
print("ix. Symmetric difference:", sym_diff)

is_subset = A.issubset(B)
is_superset = B.issuperset(A)
print("x. Is A a subset of B?", is_subset)
print("x. Is B a superset of A?", is_superset)

X = int(input("xi. Enter a value X to remove from set A: "))
A.discard(X)
print("xi. Set A after discard:", A)
print("xi. discard() is safer than remove() because discard() does nothing if the value is not present, while remove() raises a KeyError, so discard() avoids crashing the program when unsure if the value exists.")
