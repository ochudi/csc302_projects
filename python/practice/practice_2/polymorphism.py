# Parent class representing a bird
class Bird:

    def intro(self):
        """
        Introduction to birds.
        """
        print("There are many types of birds.")

    def flight(self):
        """
        Flight capability of birds.
        """
        print("Most of the birds can fly but some cannot.")


# Child class representing a sparrow
class Sparrow(Bird):

    def flight(self):
        """
        Flight capability of sparrows.
        """
        print("Sparrows can fly.")


# Child class representing an ostrich
class Ostrich(Bird):

    def flight(self):
        """
        Flight capability of ostriches.
        """
        print("Ostriches cannot fly.")


# Creating instances of Bird, Sparrow, and Ostrich
obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

# Calling methods on the instances to demonstrate polymorphism
obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
