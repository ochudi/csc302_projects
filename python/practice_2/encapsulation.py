# Python program to demonstrate parent polymorphism

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"  # Private member


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling the constructor of the Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        # Accessing the private member of the Base class
        print(self._Base__c)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting the line below will raise an AttributeError
# print(obj1.__c)

# Uncommenting the line below will also raise an AttributeError
# as the private member of the base class is called inside the derived class
# obj2 = Derived()
