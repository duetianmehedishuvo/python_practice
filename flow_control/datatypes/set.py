''' A set is an unordered collection of items. Every set element is unique
 (no duplicates) and must be immutable (cannot be changed).'''

my_set = {1, 2, 3}
print(my_set)
# Set of mixed Data Types
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# Set Cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# initialize a with {}
a = {}
# check data type of a
print(type(a))
# initialize a with set()
a = set()
# check data type of a
print(type(a))

# Practice 3
# initialize my_set
my_set = {1, 3}
print(my_set)
# add an element
my_set.add(2)
print(my_set)
# add multiple elements
my_set.update([2, 3, 4])
print(my_set)
# add list and set
my_set.update([4, 5], {1, 6, 8})
print(my_set)

# practice 4 Removing elements from a set
my_set = {1, 3, 4, 5, 6}
print(my_set)
# discard an element
my_set.discard(4)
print(my_set)
# remove an element
my_set.remove(6)
print(my_set)

# practice 5
# initialize my_set
my_set = set('HelloWorld')
print(my_set)
print(my_set.pop())
my_set.pop()
print(my_set)
# clear my_set
my_set.clear()
print(my_set)

# Practice 6 Set Union & Intersection
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# for union
print(A | B)
# use union function
print(A.union(B))
# for Intersection
print(A & B)
# use intersection function
print(A.intersection(B))

# Practice 7 Set Difference && Symmetric Difference
# Use - operator on A
print(A - B)
# Use difference function on A
print(A.difference(B))
print(B - A)
print(B.difference(A))

# for symmetric A and B
# use ^ operator
print(A ^ B)
# or use symmetric function on A
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

# practice 7 Iterating Through a Set
for letter in set("apple"):
    print(letter)
