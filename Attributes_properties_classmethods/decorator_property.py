'''
Example of decorator property
'''


class ElectricCar:
    def __init__(self, owner):
        self._owner = owner

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if isinstance(owner, str) and owner.isalpha():
            self._owner = owner
        else:
            raise ValueError


car = ElectricCar(['Gvido', 'Elon'])

print(car.owner)

"""In the __init__() method, the attribute is accessed, thereby checking the input data that is in the 
# property does not work."""
# output
# Elon
