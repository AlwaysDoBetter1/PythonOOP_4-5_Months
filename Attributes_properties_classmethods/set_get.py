'''
Implement a Person class that describes a person. When instantiated, the class must take two arguments
in the following order:

name - person's name
surname - person's last name
An instance of the Person class must have two attributes:

name - person's name
surname - person's last name
The Person class must have one property:

fullname is a read/write property that returns the person's full name as a string:
<name> <last name>
'''


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def getfullname(self):
        return self.name + " " + self.surname

    def setfullname(self, *nname):
        for i in nname:
            nname = list(nname[1:]) + i.split()
        self.name = nname[0]
        self.surname = nname[1]

    fullname = property(fget=getfullname, fset=setfullname)


# Example
person = Person('Meg', 'Fox')

person.name = 'Stefani'
print(person.fullname)

# output
# Stefani Fox
