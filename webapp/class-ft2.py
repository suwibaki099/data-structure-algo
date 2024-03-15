class Pets:
    def __init__(self, animal):
        self.animal = animal  # We have a list here and the data is the instantiate object of Cat class

    def walk(self):
        for animal in self.animal:
            print(animal.walk())  # call the walk method from Cats class


class Cats:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        """
        Info: walk your cat.
        :return:
        """
        return f'{self.name} is just walking...'


my_cats = []  # container of our cats so that we can use in our Pets class
cat1 = Cats('Winnie', 9)  # instantiate this object
cat2 = Cats('John', 3)  # instantiate this object
cat3 = Cats('Mark', 2)  # instantiate this object

my_cats.append(cat1)
my_cats.append(cat2)
my_cats.append(cat3)

# instantiate the Pets class
my_pets = Pets(my_cats)

# call the walk method
# my_pets.walk()

# call the name of cat1 for example
# print(cat1.name)

# call the age of cat1 for example
print(cat1.walk())
