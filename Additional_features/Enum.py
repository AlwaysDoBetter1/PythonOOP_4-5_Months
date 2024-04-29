'''
Implement a Seasons class that describes an enum with the seasons. The enum must have four elements:

WINTER - element with value 1
SPRING - element with value 2
SUMMER - element with value 3
FALL - element with value 4
An enum element must have one method:

text_value() is a method that takes the country code en or ru as an argument and returns the string value of the element
depending on the argument passed. For WINTER en and ru the values are winter and winter, respectively, for SPRING - spring
and spring, for SUMMER - summer and summer, for FALL - fall and autumn
'''

from enum import Enum


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, language):
        translations = {
            "WINTER": {"en": "winter", "ru": "зима"},
            "SPRING": {"en": "spring", "ru": "весна"},
            "SUMMER": {"en": "summer", "ru": "лето"},
            "FALL": {"en": "fall", "ru": "осень"}
        }
        return translations[self.name][language]

# Example
for season in Seasons:
    print(season.text_value('en'), '->', season.text_value('ru'))
# Output
# winter -> зима
# spring -> весна
# summer -> лето
# fall -> осень