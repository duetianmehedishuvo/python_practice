import constants

# Python is a type-inferred language, so you don't have to explicitly define the variable type.

website = "google.com"
print(website)

# changes the value of a variable

website = "shuvo.com"
print(website)

# assignment multiple values to multiple variables
a, b, c = 10, 10.2, 'SHUVO'
print(a)
print(b)
print(c)

# if we want to assign the same value to multiple variables at once, we can do this as:
a = b = c = 'Mehedi'
print(a)
print(b)
print(c)

# constants
print(constants.PI)
print(constants.GRAVITY)

# Literals
a = 0b10101  # Binary Literals
b = 100  # Decimal Literal
c = 0o310  # octal  Literal
d = 0x12c  # Hexadecimal Literal
print(a, b, c, d)

# Float Literals
float_1 = 10.3
float_2 = 1.5e2
print(float_1, float_2)

# complex Literals
x = 3.14j
print(x)

# string literials
unicode = u"copywrite\u00A92019"
rawString = r"Raw \n strings "
print(unicode)
print(rawString)

# Boolean Literals
x = (1 == True)
y = (1 == False)
print(x, y)

a = True + 4
b = False + 10
print(a, b)

# Special literals
drink = 'Available'
food = None


def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)


menu(drink)
menu(food)

# Literals Collection
# there are four different literal collection List literals, Tuple Literals, Dict Literals, Set Literals

fruits = ['apple', 'mango', 'orange']  # List
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u', 'a'}  # set
print(fruits)
print(numbers)
print(alphabets)
print(vowels)
