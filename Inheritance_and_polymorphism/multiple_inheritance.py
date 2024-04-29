'''
Implement the MROHelper class, which describes a set of functions for working with MRO of arbitrary classes.
When instantiated, the class must not accept any arguments.

The MROHelper class must have three static methods:

len() is a method that takes a class as an argument and returns the number of elements in its MRO
class_by_index() is a method that takes as arguments the class cls and an integer n, which defaults to zero, and
returns the class with index n in the MRO of class cls
index_by_class() - a method that takes two classes child and parent as arguments and returns an integer - the index
of the parent class in the MRO of the child class
'''

class MROHelper:
    def __init__(self):
        pass

    @staticmethod
    def len(cls):
        return len(cls.__mro__)

    @staticmethod
    def class_by_index(cls, n=0):
        return cls.__mro__[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.__mro__.index(parent)

# Example
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(MROHelper.class_by_index(D, 2))
print(MROHelper.class_by_index(B))
# Output
# <class '__main__.C'>
# <class '__main__.B'>