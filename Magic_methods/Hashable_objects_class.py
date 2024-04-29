'''
Example of a hashable objects class
'''


class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.name == other.name
        return NotImplemented

    def __hash__(self):
        return hash(self.name)


cat1 = Cat('Kemal')
cat2 = Cat('Kemal')

print(cat1 == cat2)
print(hash(cat1) == hash(cat2))

# Output:
# True
# True