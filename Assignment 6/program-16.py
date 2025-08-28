# Define the sets
A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}

# Elements common to all three sets (intersection)
common_elements = A & B & C

# Elements present in at least one set (union)
at_least_one = A | B | C

print("Elements common to all three sets:", common_elements)
print("Elements present in at least one set:", at_least_one)