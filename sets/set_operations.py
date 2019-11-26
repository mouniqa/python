A = {1,2,3,4,5}
B = {1,3,5,7,9}

def display():
  print('A = ',A)
  print('B = ',B)
  print('=====================================\n')

# A | B or A.union(B)
# Returns a set which is the union of sets A and B.
print('A | B or A.union(B) =', A|B)
display()

# A & B  or A.intersection(B)
# Returns a set which is the intersection of sets A and B.
print('A & B  or A.intersection(B) = ',A&B)
display()

# A - B or A.difference(B)
# Returns the set difference of A and B (the elements included in A, but not included in B).
print('A - B or A.difference(B) = ',A-B)
display()

# A ^ B or A.symmetric_difference(B)
# Returns the symmetric difference of sets A and B (the elements belonging to either A or B, but not to both sets simultaneously).
print('A ^ B or A.symmetric_difference(B) =',A ^ B)
display()

A = {1,2,3,4,5}
B = {1,3,5,7,9}
# A |= B or A.update(B)
# Adds all elements of array B to the set A.
print('A |= B or A.update(B) =',A.update(B))
display()


A = {1,2,3,4,5}
B = {1,3,5,7,9}
# A &= B A.intersection_update(B)
# Leaves in the set A only items that belong to the set B.
print('A &= B A.intersection_update(B) =',A.intersection_update(B))
display()


A = {1,2,3,4,5}
B = {1,3,5,7,9}
# A -= B or A.difference_update(B)
# Removes all elements of B from the set A.
print('A -= B or A.difference_update(B) =',A.difference_update(B))
display()


A = {1,2,3,4,5}
B = {1,3,5,7,9}
# A ^= B A.symmetric_difference_update(B)
# Writes in A the symmetric difference of sets A and B.
print('A ^= B A.symmetric_difference_update(B) = ',A.symmetric_difference_update(B))
display()


A = {1,2,3,4,5}
B = {1,3,5,7,9}
# A <= B or A.issubset(B)
# Returns true if A is a subset of B.
print('A <= B =',A <= B)

# A >= B or A.issuperset(B)
# Returns true if B is a subset of A.
print('A >= B =',A >= B)

# A < B
# Equivalent to (A <= B and A != B)
print('A < B =',A < B)

# A > B
# Equivalent to (A >= B and A != B)
print('A > B =',A > B)
