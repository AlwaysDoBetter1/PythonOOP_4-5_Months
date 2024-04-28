'''
Implement a Pet class that describes a pet. When instantiated, the class must take one argument:

name — pet name
An instance of the Pet class must have one attribute:
name — pet name

The Pet class must have three class methods:
first_pet() is a method that returns the very first created instance of the Pet class. If no instance has yet
been created, the method should return None

last_pet() is a method that returns the most recently created instance of the Pet class.
If no instance has yet been created, the method should return None

num_of_pets() - method that returns the number of created instances of the Pet class
'''


class Pet:
    names = []

    def __init__(self, name):
        self.name = name
        self.__class__.names.append(self)

    @classmethod
    def first_pet(cls):
        return cls.names[0] if cls.names else None

    @classmethod
    def last_pet(cls):
        return cls.names[-1] if cls.names else None

    @classmethod
    def num_of_pets(cls):
        return len(cls.names)

# Example:
pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())

# Output:
# Ratchet
# Rivet
# 3
