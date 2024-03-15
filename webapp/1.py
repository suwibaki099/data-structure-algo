# Exercise
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

''' grab the first index[0] list in first loop and the second loop 
grab the value of the first list, index[0][0] and print * if encounter 1. '''

fill = '*'
empty = ' '
for row in picture:
    for pixel in row:
        # inside the second loop
        if pixel:  # using truthy and false concept
            print(fill, end='')
        else:
            print(empty, end='')
    # inside the first loop
    print('')  # generate a new line for every row
