'''
Implement a @type_check decorator class that takes one argument:

types - a list whose elements are data types
The decorator must check that the types of all positional arguments passed to the function being decorated match exactly
those in the types list, that is, the type of the first argument is the first element of the types list, the type of the
second argument is the second element of the types list, and so on. If this condition is not met, a TypeError exception
must be raised.

If the number of positional arguments is greater than the number of elements in the types list, then unmatched arguments
should not be taken into account when checking. If the number of positional arguments is less than the number of elements
in the types list, then unmatched types in the types list should not be taken into account when checking.
'''

import functools


class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            k = zip(args, self.types)
            for i in k:
                if type(i[0]) != i[1]:
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper

# Example
@type_check([int, int, str, list])
def add(a, b):
    """sum a and b"""
    return a + b

print(add.__name__)
print(add.__doc__)
print(add(1, 2))

# Output
# add
# sum a and b
# 3