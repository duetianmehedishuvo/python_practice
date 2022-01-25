# defining strings in Python
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

# 2nd Step
# Accessing string characters in Python
str = 'programiz'
print('str = ', str)

# first character
print('str[0] = ', str[0])

# last character
print('str[-1] = ', str[-1])

# slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

# slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

# step 3
# Concatenation of Two or More Strings
# Python String Operations
str1 = 'Hello'
str2 = 'World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)

# step 4
# Iterating through a string
count = 0
for letter in 'Hello World':
    if (letter == 'l'):
        count += 1
print(count, 'letters found')

# The format() Method for Formatting Strings
# Python string format() method

# default(implicit) order
default_order = "{}, {} and {}".format('John', 'Bill', 'Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John', 'Bill', 'Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John', b='Bill', s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

# Old Style Formatting
x = 12.3456789
print("the value of x is %3.2f" % x)
print("the value of x is %3.4f" % x)

# common Python Strings Methods
print("SHUVO".lower())
print("mehedi".upper())
message="This is mehedi Hasan Shuvo"

print(message.split())
print(len(message.split()))
print(message.lower().find('hasan'))
print(message.lower().replace('hasan','Khan'))
