'''
Implement a FieldTracker class that gives its descendants the ability to track the state of certain attributes of
their instances of the class. Child classes must inherit four instance methods:

base() is a method that takes an attribute name as an argument and returns either the current value of this attribute
or the original (specified during definition) value of this attribute if it has been changed
has_changed() - a method that takes an attribute name as an argument and returns True if the value of this attribute
has been changed at least once, or False otherwise
changed() - a method that returns a dictionary in which the keys are the names of the attributes that changed their
values, and the values are their original values
save() is a method that resets tracking. After calling the method, it is considered that all attributes have not
previously changed their values, and their current values are considered initial

It is guaranteed that the descendants of the FieldTracker class:
always have a fields class attribute containing a tuple of attributes that need to be tracked
in their initializer they always call the initializer of the FieldTracker class after setting the primary values for
the tracked attributes
'''


class FieldTracker:
    def __init__(self):
        self._values = {
            field: getattr(self, field)
            for field in self.fields
        }

    def base(self, field):
        return self._values[field]

    def has_changed(self, field):
        return self._values[field] != getattr(self, field)

    def changed(self):
        return {
            field: self.base(field)
            for field in self.fields
            if self.has_changed(field)
        }

    def save(self):
        for field in self.fields:
            self._values[field] = getattr(self, field)

# Example
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)

print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())
# Output:
# 1
# False
# {}