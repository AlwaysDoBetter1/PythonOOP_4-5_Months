'''
Implement a User class that describes an Internet user. When instantiated, the class must take two arguments in the
following order:

name — user name. If name is not a non-empty letter-only string, a ValueError exception must be raised with the text:
Invalid name
age — user's age. If age is not an integer belonging to the interval [0; 110], a ValueError exception must be raised
with the text: 'Incorrect age'
An instance of the User class must have two attributes:

_name — user name
_age — user age
The User class must have four instance methods:

get_name() - method that returns the user name
set_name() is a method that takes new_name as an argument and changes the username to new_name. If new_name is not a non-empty letter-only string, a ValueError exception must be raised with the text:
Invalid name
get_age() - method that returns the user's age
set_age() is a method that takes new_age as an argument and changes the user's age to new_age. If new_age is not an integer belonging to the interval [0; 110], a ValueError exception must be raised with the text:
Incorrect age
'''


class User:
    def __init__(self, name, age):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError("Invalid name")
        if isinstance(age, int) and 0 <= age <= 110:
            self._age = age
        else:
            raise ValueError("Invalid age")

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError("Invalid name")

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 <= new_age <= 110:
            self._age = new_age
        else:
            raise ValueError("Invalid age")


# Example
user = User('Гвидо', 67)

user.set_name('Тимур')
user.set_age(30)

print(user.get_name())
print(user.get_age())

# output
# Тимур
# 30
