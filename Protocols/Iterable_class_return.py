'''
Implement the Peekable class. When instantiated, the class must take one argument:

iterable — iterable object
An instance of the Peekable class must be an iterator that generates the elements of the iterable object in the original
order and then raises a StopIteration exception.

The Peekable class must have one instance method:

peek() is a method that returns the next element of the iterator, similar to the next() function, but does not shift
the iterator. If the iterator is empty, a StopIteration exception must be raised. The method must also be able to accept
one optional argument default - an object that will be returned instead of raising a StopIteration exception if the
iterator is empty
'''

from itertools import tee


class Peekable:
    def __init__(self, iterable):
        self.iterr = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterr)

    def peek(self, default=StopIteration):
        self.iterr, k = tee(self.iterr, 2)
        try:
            return next(k)
        except:
            if default is StopIteration:
                raise StopIteration
            else:
                return default

# Example
iterator = Peekable('Python')

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())

# Output:
# P
# y
# y
# y
# t
# t