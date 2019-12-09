# PART 1 KEEPING IT CLASSY

from random import randint

class Product():
    """
    A product of Acme Corporation.
    """

# Attributes: name, price, weight, flammability, identifier
# importing 'random', use randint which return random integers from the “discrete uniform” distribution
# identifier is an interger generated as a random number

    def __init__(prod, name, price=10, weight=20, flammability=0.5,
        identifier=randint(1000000, 9999999)):

        prod.name = name
        prod.price = 10
        prod.weight = 20
        prod.flammability = 0.5
        prod.identifier = randint(1000000, 9999999)

        pass

# PART 2 OBJECTS THAT GO
# A class method is a method that is bound to a class rather than its object

# method 1 - stealability(self)

    def stealability(self):
        st = self.price/self.weight
        if st < 0.5:
            return "Not So stealable..."
        elif st >= 0.5 and st < 1.0:
            return "Kinda Stealable"
        else:
            return "Very stealable!"

# method 2 - explode(self)
    def explode(self):
        ex = self.flammability * self.weight

    def explode(self):
        ex = self.flammability * self.weight
        if ex < 10:
            return "...Fizzle"
        elif ex >= 10  and ex < 50:
             return "...boom!"
        else:
             return "...BABOOM!!"

# Part 3 - A Proper Inheritance

#change the default weight to 10

class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5,
        identifier=randint(1000000, 9999999)):

        self.name = name
        self.price = 10
        self.weight = 10
        self.flammability = 0.5
        self.identifier = randint(1000000, 9999999)

        pass

#override the explode method to 'its a glove'

    def explode(self):
        print("it's a glove")

#Add a punch method that returns "That tickles"

    def punch(self):
        z = self.weight
        if z < 5:
            print("That tickles")
        elif (z >= 5  and z < 15):
             print("Hey that hurt!")
        else:
             print("OUCH!")
