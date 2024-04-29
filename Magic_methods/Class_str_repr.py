'''
Implement the AnyClass class. When an instance is created, the class must accept an arbitrary number of named
arguments and set them as attributes to the instance being created.

An instance of the AnyClass class must have the following formal string representation:

AnyClass(<1st attribute name>=<1st attribute value>, <2nd attribute name>=<2nd attribute value>, ...)
And the following informal string representation:

AnyClass: <1st attribute name>=<1st attribute value>, <2nd attribute name>=<2nd attribute value>, ...
'''


class AnyClass:
    def __init__(self, **kwargs):
        self.dct = []
        for i, j in kwargs.items():
            setattr(self, i, j)
            if isinstance(j, str):
                j = f"'{j}'"
            self.dct.append(f"{i}={j}")

    def __str__(self):
        return f"{type(self).__name__}: {', '.join(self.dct)}"

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(self.dct)})"


# Example:
cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))

# Output:
# AnyClass: name='John', surname='Marston'
# AnyClass(name='John', surname='Marston')
