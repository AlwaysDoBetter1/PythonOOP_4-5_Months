'''
Implement a @CachedFunction decorator that caches the computed values of the function being decorated.
The cache must be accessible via the cache attribute and be a dictionary, the key of which is a tuple with arguments,
and the value is the return value of the decorated function when called with these arguments.

Note 1: For unambiguous caching, it is guaranteed that the function being decorated takes only positional arguments.
'''


class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

# Example:
@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


slow_fibonacci(5)

for args, value in sorted(slow_fibonacci.cache.items()):
    print(args, value)

# Output:
# (2,) 1
# (3,) 1
# (4,) 2
# (5,) 3
