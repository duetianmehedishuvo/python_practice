"""
Additionally, we use the super() function inside the __init__() method.
This allows us to run the __init__() method of the parent class inside the child class.

1. single inheritance

class Base1:
    pass

class Derived(Base1):
    pass

2. Multiple Inheritance

class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

3.Multilevel Inheritance

class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass

"""


# parent class
class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")
    # child class


class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run Faster")


paggy = Penguin()
paggy.whoisThis()
paggy.swim()
paggy.run()
