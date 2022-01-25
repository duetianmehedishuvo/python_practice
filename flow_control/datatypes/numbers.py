# module 01
a = 5
print(type(a))
print(type(5.0))
c = 5 + 3j
print(c + 3)

print(isinstance(c, complex))
print(isinstance(a, int))

# module 02

# Output: 107
print(0b01101011)
# Output: 253 (251 + 2)
print(0xFB + 0b10)
# Output: 13
print(0o15)

# Random
import random

print(random.randrange(1, 5))
x = ['a', 'e', 'i', 'o', 'u']
print(random.choice(x))
random.shuffle(x)
print(x)
print(random.random())
