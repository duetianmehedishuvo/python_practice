def greet(name, msg):
    print("Hello", name + ', ' + msg)


greet("SHUVO", "Good Morning!")


# Python Default Arguments
def greet(name, msg="Good Morning!"):
    print("Hello", name + ', ' + msg)


greet("SHuvo")
greet("SHuvo", "Good Evening!")


# Python Arbitrary Arguments
def greet(*names):
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "john")

# Python Recursion

# example of a recursive function
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
print("the factorial of 5 is",factorial(5))

