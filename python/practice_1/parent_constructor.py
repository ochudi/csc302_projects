# Python code to demonstrate how parent constructors are called.

# Parent class
class Person(object):
    """
    This class represents a person with a name and ID number.
    """

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        """
        Initializes a Person object with the given name and ID number.
        """
        self.name = name
        self.idnumber = idnumber

    def display(self):
        """
        Displays the name and ID number of the person.
        """
        print("Name: {}".format(self.name))
        print("ID Number: {}".format(self.idnumber))

    def details(self):
        """
        Displays detailed information about the person.
        """
        print("My name is {}".format(self.name))
        print("ID Number: {}".format(self.idnumber))

# Child class
class Employee(Person):
    """
    This class represents an employee, which is a specialized type of Person.
    """

    def __init__(self, name, idnumber, salary, post):
        """
        Initializes an Employee object with the given name, ID number, salary, and job post.
        """
        self.salary = salary
        self.post = post

        # Invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        """
        Displays detailed information about the employee.
        """
        print("My name is {}".format(self.name))
        print("ID Number: {}".format(self.idnumber))
        print("Salary: {}".format(self.salary))
        print("Post: {}".format(self.post))

# Create instances of Person and Employee
somebody = Person("John Doe", 11192293473)
chudi = Employee("Chukwudi Ofoma", 20120612023, "NGN 50,000.00", "Intern Developer")

# Display details of the Person and Employee
print("Person:")
somebody.display()
print("\nEmployee:")
chudi.display()
chudi.details()
