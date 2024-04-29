'''
Implement the MutableString class, a descendant of the UserString class that describes the mutable string.
The process for creating an instance of the MutableString class must be the same as the process for creating an
instance of the UserString class.

The MutableString class must have three instance methods:

lower() - a method that converts all characters of the modified string to lower case
upper() - a method that converts all characters of the string being modified to uppercase
sort() is a method that sorts the characters of the string being changed. Can take two optional named arguments key and
reverse, serving the same purpose as sorted()
An instance of the MutableString class must allow the values of its elements to be retrieved, modified, and deleted
using indexes, both positive and negative.
'''

from collections import UserString

class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data = self.data[:index] + value + self.data[index+1:]

    def __delitem__(self, index):
        self.data = self.data[:index] + self.data[index+1:]

# Example
mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
mutablestring.sort()
print(mutablestring)
# Output:
# beegeek
# BEEGEEK
# BEEEEGK