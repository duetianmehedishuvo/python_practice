# Access List Elements
my_list = ['p', 'r', 'o', 'b', 'e']

# first item
print(my_list[0])  # p

# third item
print(my_list[2])  # o

# fifth item
print(my_list[4])  # e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])
print(n_list[1][3])
print(my_list[4])

# Negative indexing
# Negative indexing in lists
print("\n\n\n\n\n")
my_list = ['p', 'r', 'o', 'b', 'e']

# last item
print(my_list[-1])

# fifth last item
print(my_list[-5])

# List Slicing in Python
# List slicing in Python

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

# elements from index 2 to index 4
print(my_list[2:5])

# elements from index 5 to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

# Add or changing list of elements
odd = [2, 4, 6, 8]
odd[0] = 1
print(odd)

# change second to 4th items
odd[1:4] = [3, 5, 7]
print(odd)

# We can add one item to a list using the append() method or add several items using the extend() method.
odd.append(9)
print(odd)
odd.extend([11, 13, 15])
print(odd)
odd.extend([17])
print(odd)

# Concatenating and repeating lists
odd = [1, 3, 5]
print(odd + [7, 9, 11])
print(['sh'] * 3)
print(odd * 3)

# Furthermore, we can insert one item at a desired location by using the method insert()
# or insert multiple items by squeezing it into an empty slice of a list.

odd = [1, 9]
print(odd)
odd.insert(1, 3)
print(odd)
odd.insert(0, 10)
print(odd)
odd.insert(9, 11)
print(odd)

odd[2:2] = [5, 7]
print(odd)

# Deleting List Elements
my_list = ['a', 'e', 'i', 'o', 'u']
print(my_list)
del my_list[2]
print(my_list)
del my_list
# print(my_list)

# We can use remove() to remove the given item
# pop() to remove an item at the given index.
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm', 'p']
my_list.remove('p')
print(my_list)
print(my_list.pop(1))
print(my_list)
print(my_list.pop())
print(my_list)
my_list.clear()
print(my_list)

# Example on Python list methods
my_list = [3, 8, 1, 6, 8, 8, 4]
# add a to the end
my_list.append('a')
print(my_list)
# Index of first occurrence of 3
print(my_list.index(3))
# Count of 8 in the list
print(my_list.count(8))

# List Comprehension: Elegant way to create Lists
# Here is an example to make a list with each item being increasing power of 2.
pow2 = [2 ** x for x in range(10)]
print(pow2)

pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)
odd = [x for x in range(20) if x % 2 == 1]
print(odd)
data = [x + y for x in ['python ', 'C '] for y in ['Language', 'Programming']]
print(data)

# List Membership Test
# We can test if an item exists in a list or not, using the keyword in.
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
# Output: True
print('p' in my_list)
print('P' in my_list)
print('P' not in my_list)

# Iterating Through a List
for fruit in ['apple', 'banana', 'mango']:
    print("I like", fruit)
