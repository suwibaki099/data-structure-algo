from random import randint
import sys

while True:
    try:
        random_number = randint(int(sys.argv[1]), int(sys.argv[2]))
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])

        # print(random_number) # to view the answer just undone the comment here to test it

        number = int(input(f'Please choose a number {num1}~{num2}: '))
        if int(sys.argv[1]) <= number <= int(sys.argv[2]):
            if number == random_number:
                print("You're a genius!")
                break
            else:
                print('Try again!')
        else:
            print(f'Please input the number between {num1}~{num2}')
    except ValueError:
        print("Please enter a number!")
        continue
