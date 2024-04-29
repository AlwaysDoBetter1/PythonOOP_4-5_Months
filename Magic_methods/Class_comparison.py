'''
We will call any sequence of one or more Latin letters a word.

Implement a Word class that describes a word. When instantiated, the class must take one argument:

word - word
An instance of the Word class must have the following formal string representation:

Word('<word in original form>')
And the following informal string representation:

<a word in which the first letter is capitalized and all other letters are lowercase>
Also, instances of the Word class must support all comparison operations with each other using the operators ==, !=,
>, <, >=, <=. Two words are considered equal if their lengths are the same. A word is considered larger than
another word if its length is greater.
'''

from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f"Word('{self.word}')"

    def __str__(self):
        return self.word.capitalize()

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        else:
            return NotImplemented


# Example:
print(Word('bee') == Word('hey'))
print(Word('bee') < Word('geek'))
print(Word('bee') > Word('geek'))
print(Word('bee') <= Word('geek'))
print(Word('bee') >= Word('gee'))

# Output:
# True
# True
# False
# True
# True
