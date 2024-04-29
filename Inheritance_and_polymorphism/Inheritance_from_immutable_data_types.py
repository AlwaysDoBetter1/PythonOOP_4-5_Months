'''
Implement the AdvancedTuple class, a descendant of the tuple class, which describes a tuple that can perform the
addition operation (+, +=) not only with instances of the AdvancedTuple and tuple classes, but also with any
iterable objects. The process for creating an instance of the AdvancedTuple class must be the same as the process
for creating an instance of the tuple class.

Note 1: Whether addition is performed using the + or += operator, the result of the operation must be a new instance
of the AdvancedTuple class.
'''


class AdvancedTuple(tuple):
    def __new__(cls, iterable=()):
        return super().__new__(cls, iterable)

    def __add__(self, other):
        return AdvancedTuple(super().__add__(tuple(other)))

    def __radd__(self, other):
        return AdvancedTuple(tuple(other).__add__(self))

# Example
advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({'a': 1, 'b': 2} + advancedtuple)
# Output:
# (1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# ('a', 'b', 1, 2, 3)