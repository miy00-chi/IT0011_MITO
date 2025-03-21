A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'd', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

intersection_A_B = A & B
print("Elements in A and B:", intersection_A_B)
print("Count:", len(intersection_A_B))

difference_B_AC = B - (A | C)
print("Elements in B but not in A and C:", difference_B_AC)
print("Count:", len(difference_B_AC))

print("\nSet Operations:")
print("i. [h, i, j, k]:", B & C)
print("ii. [c, d, f]:", A & B & C)
print("iii. [b, c, h]:", (A & B) | (B & C) - (A & B & C))
print("iv. [d, f]:", A & C)
print("v. [c]:", A & B & C & {'c'})
print("vi. [l, m, o]:", B - (A | C))
