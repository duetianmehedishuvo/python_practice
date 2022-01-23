print("Hello world")
print(1 + 1)

# Python Statement, Indentation and Comments

# Multi Line Statement

# \ mean Continuous Character
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

print(a)

# parentheses ()
# brackets []
# braces {}

a = (1 + 2 + 3 +
     4 + 5 + 6 + 7 + 8)
print(a)
a = [1 + 2 + 3 +
     4 + 5 + 6 + 7 + 8]
print(a)

# We Can also PUT Multiple statements in a single line using smicolons
a = 1;
b = 2;
c = 3

'''Most of the programming languages like C, C++, and Java use braces { } 
    to define a block of code. Python, however, uses indentation. Generally, 
    four whitespaces are used for indentation and are preferred over tabs.'''
if True:
    print("Hello ")

if True: print("Hello")


# doc strings
def double(num):
    '''Function to double the value
        My Name is Mehedi Hasan shuvo'''
    return 2 * num


print(double.__doc__)
