'''
Implement a pluck() function that takes three arguments in the following order:

data — dictionary of arbitrary nesting
path is a string representing a key or a sequence of keys separated by a dot.
default — arbitrary object, default value; is None unless passed explicitly
The function must return the value for the path key from the data dictionary. If path is a sequence of keys,
for example key1.key2, then the return value of the function should be the value of key2 from the dictionary data[key1].
If the specified key or at least one key from the sequence of keys is not in the dictionary, the function must
return the default value.
'''

def pluck(data, path, default=None):
    val = data
    for i in path.split("."):
        val = val.get(i, default)
        if val == default:
            return val
    return val


d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck(d, 'a.b.c'))

# Output:
# {'d': {'e': 4}}