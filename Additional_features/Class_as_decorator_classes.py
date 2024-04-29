'''
Any user class by default is capable of creating an infinite number of instances of itself. The singleton design pattern,
in contrast, ensures that a class has only one instance of itself, and when attempting to create a new one, it returns
the existing one.

Implement a @limiter decorator to decorate a class, which can be used to limit the number of instances of the decorated
class that can be created to a certain number. The decorator must take three arguments in the following order:

limit — the number of instances that the decorated class can create
unique is the name of an attribute of an instance of the decorated class, the value of which is its identifier. Two
instances with the same ID cannot exist. If an attempt is made to create an instance whose ID matches the ID of one
of the previously created instances, that previously created instance must be returned
lookup - determines which object should be returned if the limit is exceeded and the unique attribute value has not
been previously used. If the value is FIRST, the very first instance created is returned, if the value is LAST, the
most recently created instance is returned.
'''


def limiter(limit, unique, lookup):
    instances = {}
    lookups = {}

    def wrapper(cls):
        def get_instance(*args, **kwargs):
            instance = cls(*args, **kwargs)
            lookups.setdefault("FIRST", instance)
            identifier = getattr(instance, unique)
            if len(instances) < limit:
                if identifier not in instances:
                    lookups['LAST'] = instances[identifier] = instance
                return instances[identifier]
            return instances.get(identifier) or lookups.get(lookup)

        return get_instance

    return wrapper


# Example
@limiter(3, 'ID', 'LAST')
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value


obj1 = MyClass(1, 5)  # An instance of the class is created with ID 1
obj2 = MyClass(2, 8)  # An instance of the class is created with ID 2
obj3 = MyClass(3, 10)  # An instance of the class is created with ID 3

obj4 = MyClass(4, 0)  # The limit is exceeded, returning the last created instance
obj5 = MyClass(2, 20)  # obj2 is returned, as an instance with ID 2 already exists

print(obj4.value)
print(obj5.value)

# Output
# 10
# 8
