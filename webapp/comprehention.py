# list comprehension
# my_list = [num*2 for num in range(0, 100)]

# dictionary comprehension
# my_list = [key:value for value in "it can be other dict or list"]


# exercise: find the duplicate letters
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'c']

duplicates = list({letter for letter in some_list if some_list.count(letter) > 1})
print(duplicates)
