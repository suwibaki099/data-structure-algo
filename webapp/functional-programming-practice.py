from functools import reduce

my_pets = ['sisi', 'bibi', 'titi', 'carla']

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

scores = [73, 20, 65, 19, 76, 100, 88]


def all_caps(item):
    return item.upper()


def pass_over50(item):
    return item > 50


def accumulator(acc, item):
    return acc + item


print('Output: ', list(map(all_caps, my_pets)))
print('Output:', list(zip(my_strings, sorted(my_numbers))))
print('Output of pass over 50: ', list(filter(pass_over50, scores)))
print('Output of combine numbers and scores: ', reduce(accumulator, my_numbers + scores))
