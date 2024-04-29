'''
By default, Python uses a dictionary to manage the attributes of a class instance. If necessary, the dictionary allows
you to add additional attributes to the instance. However, this at the same time entails memory consumption, for example,
if there are quite a lot of class instances.

To optimize memory consumption, slots were added to Python. If instances of some class contain only a fixed (predefined)
set of attributes, we can use slots so that a more compact data structure is used instead of dictionaries.
'''

class Car:
    def __init__(self, color, owner):
        self.color = color
        self.owner = owner

class ElectricCar(Car):
    __slots__ = ('power_reserve',)

    def __init__(self, color, owner, power_reserve):
        super().__init__(color, owner)
        self.power_reserve = power_reserve


car = ElectricCar('yellow', 'Gvido', 400)

print(car.__slots__)
print(car.__dict__)

# Output
# ('power_reserve',)
# {'color': 'yellow', 'owner': 'Gvido'}