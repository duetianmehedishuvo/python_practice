# demo 01
x = "global"


def foo():
    print("X inside:", x)


foo()
print("X outside:", x)

# demo 02
x = "global "


def foo():
    global x
    y = 'local'
    x = x * 2
    print(x)
    print(y)


foo()

# demo 03 Global variable and local variable with same name
x = 5


def foo():
    x = 10
    print("Local x:", x)


foo()
print("global x:", x)


# demo 04 NonLocal
def outer():
    x = "Local"

    def inner():
        nonlocal x
        x = 'nonLocal'
        print("Inner:", x)

    inner()
    print("Outer:", x)


outer()


# demo 05 Global
def foo():
    x = 20

    def bar():
        global x
        x = 25

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)


foo()
print("x in main: ", x)
