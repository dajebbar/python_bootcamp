branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}

print(f"Branch A: {branch_a_products}")
print(f"Branch B: {branch_b_products}")

branch_union = branch_a_products | branch_b_products
print(f"Union of branchs A and B: {branch_union}")

branch_inter = branch_a_products & branch_b_products
print(f"Intersection of branchs A and B: {branch_inter}")


products_only_a = branch_a_products - branch_b_products
print(f"Products only in A branch: {products_only_a}")

print(f"Is ketchup available in A branch ? {'ketchup' in branch_a_products}")

essential_items = frozenset({"milk", "bread", "ketchup"})
print(f"the frozenset: {essential_items}")

