'''
A predicate is a function that returns True or False depending on the arguments passed.

Implement the @predicate decorator, which will allow you to conveniently combine predicates using the &, | operators. and ~:

@predicate
def is_even(num):
     return num % 2 == 0

@predicate
def is_positive(num):
     return num > 0

print((is_even & is_positive)(4)) # True; equivalent to is_even(4) and is_positive(4)
print((is_even & is_positive)(3)) # False; equivalent to is_even(3) and is_positive(3)
print((is_even | is_positive)(3)) # True; equivalent to is_even(3) or is_positive(3)
print((~is_even & is_positive)(3)) # True; equivalent to not is_even(3) and is_positive(3)
The decorator must be able to work with any predicates, no matter how many arguments they take
Both positional and named arguments should also be supported
The decorated function must be available outside of combinations with other functions and behave like the original function
'''

from functools import wraps

class predicate:
    def __init__(self, func):
        self.func = func

    def __and__(self, other):
        @wraps(self.func)
        def wrapper(*args, **kwargs):
            return self.func(*args, **kwargs) and other(*args, **kwargs)
        return predicate(wrapper)

    def __or__(self, other):
        @wraps(self.func)
        def wrapper(*args, **kwargs):
            return self.func(*args, **kwargs) or other(*args, **kwargs)
        return predicate(wrapper)

    def __invert__(self):
        @wraps(self.func)
        def wrapper(*args, **kwargs):
            return not self.func(*args, **kwargs)
        return predicate(wrapper)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

# Example
@predicate
def to_be():
    return True

print((to_be | ~to_be)())                     # True; equal to_be() or not to_be()

@predicate
def is_equal(a, b):
    return a == b

@predicate
def is_less_than(a, b):
    return a < b

print((is_less_than | is_equal)(1, 2))        # True; equal is_less_than(1, 2) or is_equal(1, 2)