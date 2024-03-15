# fibonacci numbers generator

def fib(numbers):
    f1 = 0
    f2 = 1
    for number in range(numbers+1):
        yield f1
        temp = f1
        f1 = f2
        f2 += temp


for item in fib(10):
    print(item)
