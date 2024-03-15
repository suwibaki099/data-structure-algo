while True:
    try:
        age = int(input('What is your age: '))
    except ValueError as err:
        print(f'Please input numbers {err}')
    else:
        print('Thank you!')
        break
    finally:
        print('hello im here')
