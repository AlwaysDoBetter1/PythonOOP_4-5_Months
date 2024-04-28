'''
Class and class instance and their attributes, working
'''

class ElectricCar:
    def __init__(self, color, owner):
        self.color = color
        self.owner = owner


car1 = ElectricCar('black', 'Elon')
car2 = ElectricCar('yellow', 'Gvido')

print(car1.color, car1.owner)
print(car2.color, car2.owner)

# black Elon
# yellow Gvido
