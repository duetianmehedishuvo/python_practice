def greet(name):
    print("hello,", name + '.Good Morning')


greet("SHUVO")


# Example of returns
def absoluteValue(num):
    if num >= 0:
        return num
    else:
        return -num


print(absoluteValue(10))
print(absoluteValue(-10))

print("SHUVO")


# Scope and Lifetime of Variables
def myFun():
    x = 10
    print("Value inside function", x)


x = 20
myFun()
print("Value outside functions:", x)
