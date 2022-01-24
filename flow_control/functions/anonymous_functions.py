# anonymous functions is a functions that is defined without a name
# Hence, anonymous functions are also called lambda functions

result = lambda x: x * 2
print(result(2))

# Example with filter
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
newList = list(filter(lambda x: (x % 2 == 0), my_list))
print(newList)

# example use with map()
newList = list(map(lambda x: x * 2, my_list))
print(newList)
