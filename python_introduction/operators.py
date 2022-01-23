# Arithmetic operators

x = 5
y = 2
print('x + y =', x + y)
print('x - y =', x - y)
print('x * y =', x * y)
print('x % y =', x % y)
print('x / y =', x / y)
print('x // y =', x // y)  # Floor division
print('x ** y =', x ** y)  # Exponent  x**y (x to the power y)

# Comparison operators
x = 10
y = 12
print('x > y is', x > y)
print('x < y is', x < y)
print('x == y is', x == y)
print('x != y is', x != y)
print('x >= y is', x >= y)
print('x <= y is', x <= y)

# Logical operators
x = True
y = False
print('x and y is', x and y)
print('x or y is', x or y)
print('not x is', not x)

# Bitwise operators
# Identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

# Membership operators
x = 'Hello world'
y = {1: 'a', 2: 'b'}
print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)

# namespace
a = 2
print('id(a) =', id(a))
a=2.2
print('id(a) =', id(a))