# Accessing Elements from Dictionary
my_dict = {"name": 'Jack', 'age': 26}
print(my_dict.get('age'))
print(my_dict['name'])

# practice 02 Changing and Adding Dictionary elements
# update value
my_dict['age'] = 10
print(my_dict)
# add item
my_dict['address'] = "Dhaka"
print(my_dict)

# Practice 03 Removing elements from Dictionary
# print(my_dict.pop('age'))
# print(my_dict)
# print(my_dict.popitem())
my_dict.clear()
print(my_dict)
# delete the dictionary itself
del my_dict

# Practice 04 Example
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)
# if i want to use key and value adjust then use .items() functions
for items in marks.items():
    print(items)
print(list(sorted(marks.keys())))
print(list(sorted(marks.values())))

# Practice 05 Python Dictionary Comprehension
squares = {x: x * x for x in range(6)}
print(squares)
odd_squares = {x: x * x for x in range(11) if x % 2 == 1}
print(odd_squares)

# practice 06
# Dictionary Built-in Functions
squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: False
print(all(squares))

# Output: True
print(any(squares))

# Output: 6
print(len(squares))

# Output: [0, 1, 3, 5, 7, 9]
print(sorted(squares))
