# lambda practice

my_list = [5, 4, 3]

# Square
# print('output:', list(map(lambda squire: squire ** 2, my_list)))

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])

print('output', a)

