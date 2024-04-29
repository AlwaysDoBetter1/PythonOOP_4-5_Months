'''
Implement a RandomNumber class that describes a descriptor that, when accessed at an attribute, returns a random
integer within a given range. When instantiated, the class must take three arguments in the following order:

start — integer
end — integer
cache — boolean value, defaults to False
The handle must be assigned to an attribute that has the same name as the variable to which the handle is assigned.

When accessing an attribute, the handle must return a random integer from start to end, inclusive. If the cache
parameter was set to True when the descriptor was created, each time the attribute is accessed, the descriptor
must return the number that was generated the first time it was accessed.

When setting or changing the value of an attribute, the descriptor must raise an AttributeError exception with the text:

Change is not possible
'''

import random


class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache
        self.cached_value = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.cache and self.cached_value is not None:
            return self.cached_value
        else:
            random_num = random.randint(self.start, self.end)
            if self.cache:
                self.cached_value = random_num
            return random_num

    def __set__(self, instance, value):
        raise AttributeError("Изменение невозможно")

    def __delete__(self, instance):
        pass

# Exmple
class MagicPoint:
    x = RandomNumber(0, 5, True)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

magicpoint = MagicPoint()
value = magicpoint.x

print(magicpoint.x in [0, 1, 2, 3, 4, 5])
print(magicpoint.x == value)
print(magicpoint.x == value)
print(magicpoint.x == value)
# Output:
# True
# True
# True
# True