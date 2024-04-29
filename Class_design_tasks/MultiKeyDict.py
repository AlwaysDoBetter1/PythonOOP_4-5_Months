'''
Implement a MultiKeyDict class that replicates the dict class in almost every way. Creating an instance of the
MultiKeyDict class should be similar to creating an instance of the dict class:

multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])
print(multikeydict1['x']) # 1
print(multikeydict2['z']) #3

A feature of the MultiKeyDict class should be the alias() method, which should allow you to give aliases to existing
keys. Accessing the created alias should be no different from accessing the original key, that is, from the moment the
alias is created, the value has two keys (or more if there are several aliases):

multikeydict = MultiKeyDict(x=100, y=[10, 20])
multikeydict.alias('x', 'z') # add alias 'z' to key 'x'
multikeydict.alias('x', 't') # add alias 't' to key 'x'
print(multikeydict['z']) # 100
multikeydict['t'] += 1
print(multikeydict['x']) # 101

multikeydict.alias('y', 'z') # now 'z' becomes an alias for key 'y'

multikeydict['z'] += [30]
print(multikeydict['y']) # [10, 20, 30]

The value should remain accessible by alias even if the original key has been deleted:

multikeydict = MultiKeyDict(x=100)
multikeydict.alias('x', 'z')
del multikeydict['x']
print(multikeydict['z']) # 100
Keys must take precedence over aliases. If some key and alias coincide, then all operations accessing them must be
performed with the key:

multikeydict = MultiKeyDict(x=100, y=[10, 20])
multikeydict.alias('x', 'y')
print(multikeydict['y']) # [10, 20]
'''

from collections import UserDict

class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._aliases = {}
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        if key in self.data:
            return super().__getitem__(key)
        elif key in self._aliases:
            return super().__getitem__(self._aliases[key])
        else:
            raise KeyError

    def __setitem__(self, key, value):
        if key in self._aliases:
            key = self._aliases[key]
        super().__setitem__(key, value)

    def __delitem__(self, key):
        if key in self.data:
            f = False
            ff = None
            for i, k in self._aliases.copy().items():
                if k == key:
                    if f == False:
                        f = True
                        ff = i
                        super().__setitem__(i, self.data[key])
                        del self._aliases[i]
                    else:
                        self._aliases[i] = ff
            super().__delitem__(key)

    def alias(self, original_key, alias_key):
        if original_key in self.data:
            self._aliases[alias_key] = original_key