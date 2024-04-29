'''
Implement a HistoryDict class that describes a dictionary that remembers the previous values for each key.
When instantiated, the class must take one argument:

data is a dictionary that defines the initial set of elements of an instance of the HistoryDict class.
If not passed, the initial set of elements is considered empty

The HistoryDict class must have five instance methods:
keys() - a method that returns an iterable object whose elements are the keys of an instance of the HistoryDict class
values() - a method that returns an iterable object whose elements are the key values of an instance of the HistoryDict
class
items() - a method that returns an iterable object whose elements are the elements of an instance of the HistoryDict
class in the form of tuples (<key>, <value>)
history() is a method that takes a key as an argument and returns a list whose elements are all the values that were
ever contained in an instance of the HistoryDict class for the specified key. If the given key is not contained in the
HistoryDict instance (it was removed or was never added), the method should return an empty list
all_history() is a method that returns a dictionary whose keys are the keys of an instance of the HistoryDict class,
and the values are lists containing all the values that were ever contained by these keys

When passing an instance of the HistoryDict class to the len() function, the number of elements in it must be returned.

Also, an instance of the HistoryDict class must be an iterable object, that is, allow iterate over its keys, for example,
using a for loop.

Finally, an instance of the HistoryDict class must allow you to get and change the values of its elements by their keys,
add new pairs (key, value) and delete existing ones.

Note 1: An instance of the HistoryDict class should not depend on the dictionary from which it was created. In other
words, if the original dictionary changes, then the HistoryDict instance should not change.
'''

class HistoryDict:
    def __init__(self, data=None):
        self._history = {}
        if data:
            for key, value in data.items():
                self._history[key] = [value]

    def keys(self):
        return iter(self._history.keys())

    def values(self):
        return iter([history[-1] for history in self._history.values()])

    def items(self):
        return iter([(key, history[-1]) for key, history in self._history.items()])

    def history(self, key):
        return self._history.get(key, [])

    def all_history(self):
        return {key: history[:] for key, history in self._history.items()}

    def __len__(self):
        return sum(len(history) for history in self._history.values())

    def __iter__(self):
        return iter(self._history)

    def __getitem__(self, key):
        return self._history.get(key, [])[0] if key in self._history else None

    def __setitem__(self, key, value):
        if key in self._history:
            self._history[key].append(value)
        else:
            self._history[key] = [value]

    def __delitem__(self, key):
        del self._history[key]

    def __repr__(self):
        return repr(self._history)

# Example
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['dogs'] = 1
print(len(historydict))
del historydict['ducks']
del historydict['cats']
print(len(historydict))

# Output:
# 3
# 1