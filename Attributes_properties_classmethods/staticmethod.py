'''
Implement the StrExtension class, which describes a set of functions for working with strings.
When instantiated, the class must not accept any arguments.

The StrExtension class must have three static methods:
remove_vowels() is a method that takes a string as an argument, removes all vowels from it, case insensitive,
and returns the result.

leave_alpha() is a method that takes a string as an argument, removes all characters that are not Latin letters from it,
and returns the result
replace_all() is a method that takes three string arguments string, chars and char, replaces all characters in string
from chars to char, case sensitive, and returns the result.

Note 1: It is guaranteed that all alphabetic characters belong to the Latin alphabet.
'''

import re

class StrExtension:
    @staticmethod
    def remove_vowels(strr):
        return re.sub(r'[aeiouyAEIOUY]', '', strr)

    @staticmethod
    def leave_alpha(strr):
        return re.sub(r'[^a-zA-Z]', '', strr)

    @staticmethod
    def replace_all(strr, chars, cha):
        return re.sub(fr'[{chars}]', cha, strr)

# Example:
print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))

# Output:
# -y-ho-
# S#epi#
