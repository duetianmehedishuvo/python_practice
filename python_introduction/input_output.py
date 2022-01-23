import  math
import  sys
# python output using Printf()

print('this sentence us output to the screen')

a = 5
print("the value of a is", a)
print("the value of a is " + str(a))

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*', end='@')
print(end='\n')

# Output formatting
x = 5
y = 10
print("The value of x is {1} and y is {0}".format(x, y))
print("The value of x is {} and y is {}".format(x, y))

# We can use keyword arguments to format the strings
print('hello {name}, {greeting}'.format(greeting='Good Morning', name="Shuvo"))

# Input
num=input("Enter a number: ")
print(num)
print(int(num))

# import math
print(math.pi)
print(sys.path)