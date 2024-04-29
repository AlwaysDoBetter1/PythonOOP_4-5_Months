'''
Example of interesting working dicts
'''


class AlwaysEquals:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return True

    def __hash__(self):
        return 1

    def __repr__(self):
        return f'AlwaysEquals({repr(self.data)})'


data = {}
obj1 = AlwaysEquals('bee')
obj2 = AlwaysEquals('geek')

data[obj1] = 'пчела'
data[obj2] = 'гик'

print(data)

# Output:
# {AlwaysEquals('bee'): 'гик'}