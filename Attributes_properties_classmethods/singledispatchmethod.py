'''
Implement the Formatter class. When instantiated, the class must not accept any arguments.

The Formatter class must have one static method:

format() is a method that takes an object of type int, float, tuple, list, or dict as an argument and
displays information about the passed object in a format depending on its type. If the passed object
is of any other type, a TypeError exception must be raised with the text:
The passed type argument is not supported
'''

from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError("Argument of the provided type is not supported")

    @format.register(int)
    def intt(data):
        print(f"Integer: {data}")

    @format.register(float)
    def fl(data):
        print(f"Float: {data}")

    @format.register(tuple)
    def tpl(data):
        print(f"Tuple elements: {', '.join(map(str, data))}")

    @format.register(list)
    def lst(data):
        print(f"List elements: {', '.join(map(str, data))}")

    @format.register(dict)
    def dct(data):
        print(f"Dictionary pairs: {', '.join(map(str, data.items()))}")


# Example:
Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))

# Output:
# List elements: 10, 20, 30, 40, 50
# Tuple elements: [1, 3], [2, 4, 6]
