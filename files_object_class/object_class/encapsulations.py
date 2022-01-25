class Computer:
    def __init__(self):
        self.__maxPrice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxPrice))

    def setMaxPrice(self, price):
        self.__maxPrice = price


c = Computer()
c.sell()

# change the Price
c.__maxPrice = 1000
c.sell()

# using setter functions
c.setMaxPrice(1000)
c.sell()
