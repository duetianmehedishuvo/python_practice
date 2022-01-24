numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for val in numbers:
    sum = sum + val
print('sum is:', sum)

# Range

print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(0, 10, 2)))

genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
    print("I like", genre[i])
else:
    print("No items left.")
