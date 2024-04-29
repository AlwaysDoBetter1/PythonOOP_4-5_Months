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

class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, num=1):
        self.value += num

    def dec(self, num=1):
        self.value -= num
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def dec(self, num=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        self.value = start
        self.limit = limit

    def inc(self, num=1):
        self.value += num
        if self.value > self.limit:
            self.value = self.limit

# Exmple
counter = Counter()

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(3)
print(counter.value)
counter.dec(10)
print(counter.value)
# Output:
# 0
# 6
# 2
# 0