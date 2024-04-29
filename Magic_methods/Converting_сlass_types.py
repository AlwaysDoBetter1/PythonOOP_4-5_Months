'''
Implement a Vector class that describes a vector on a plane. When instantiated, the class must take two arguments
in the following order:

x — vector coordinate along the x axis
y — vector coordinate along the y axis

An instance of the Vector class must have the following informal string representation:
(<x-coordinate>, <y-coordinate>)

Also, an instance of the Vector class must support casting to bool, int, float and complex types:
when cast to type bool, the value of the vector must be True if at least one of its coordinates is not zero, or
False otherwise
when casting to an int type, the value of the vector must be its modulus in the form of an integer with the fractional
part discarded
when casting to a float type, the value of the vector must be its modulus in the form of a real number
when casting to complex type, the value of the vector must be a complex number, the real part of which is equal to the
vector coordinate along the x axis, and the imaginary part is equal to the vector coordinate along the y axis
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __int__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __float__(self):
        return float((self.x ** 2 + self.y ** 2) ** 0.5)

    def __complex__(self):
        return complex(self.x, self.y)

# Example:
vector = Vector(3, 4)

print(vector)
print(int(vector))
print(float(vector))
print(complex(vector))
print(bool(Vector(1, 2)))

# Output:
# (3, 4)
# 5
# 5.0
# (3+4j)
# True
