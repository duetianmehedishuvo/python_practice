# check Data type
a = 5
a = 2.3
a = True
a = 1.2j
print(type(a))

# python List
a = [5, 10, 15, 20, 25, 30, 35, 40]

# a[2]=15
print("a[2] = ", a[2])

# a[0:3]=[5,10,15]
print("a[0:3] = ", a[:3])
print("a[0:3] = ", a[0:3])

# a[5: ]=[30,35,40]
print("a[5:] = ", a[5:])

# tuple
# Tuple is an ordered sequence of items same as a list.
# The only difference is that tuples are immutable. Tuples once created cannot be modified.

t = (5, 'program', 1 + 3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
# t[0] = 10

# Set
a = {1, 2, 2, 3, 3, 3}
print(a)

# Dictionary
# Dictionary is an unordered collection of key-value pairs.
d = {1: 'value', 'key': 2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
# print("d[2] = ", d[2])

# Conversion between data types
num = 10.21
secondNumber = int(num)
print(secondNumber)
print(float('2.5'))
print(list('hello'))

# implicit Type Conversion
# when we use lower to higher then no problems here is example
num_int = 123
num_float = 1.23
newNum = num_int + num_float
print(newNum)

# But when we are use higher to lower then show error
num_int = 123
num_str = '456'
# when i use num_int + num_str then show Error
# now try to solve using explicit conversion
newNum = num_int + int(num_str)
print(newNum)
