class Dog:

    # Class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name


# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
# Accessing class attribute using the class name
print("Rodger is a {}".format(Dog.attr1))
print("Tommy is also a {}".format(Dog.attr1))

# Accessing instance attributes
# Accessing instance attribute of Rodger
print("My name is {}".format(Rodger.name))

