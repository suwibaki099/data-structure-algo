# create my own decorator

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


def ordinary():
    print("I am ordinary")


a = make_pretty(ordinary)
a()  # Output: I am ordinary
