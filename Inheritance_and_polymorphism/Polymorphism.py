'''
1. Implement a USADate class that describes a date in American format. When instantiated, the class must
take three arguments in the following order:

year - year
month - month
day - day
The USADate class must have two instance methods:

format() is a method that returns a string representing a date in the format MM-DD-YYYY
iso_format() is a method that returns a string representing a date in YYYY-MM-DD format
2. Also implement an ItalianDate class, which describes a date in Italian format, whose constructor takes three arguments:

year - year
month - month
day - day
The ItalianDate class must have two instance methods:

format() - a method that returns a string representing a date in DD/MM/YYYY format
iso_format() is a method that returns a string representing a date in YYYY-MM-DD format
'''

class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f"{self.month:02d}-{self.day:02d}-{self.year}"

    def iso_format(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"


class ItalianDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def iso_format(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

# Example
usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())
# Output
# 04-06-2023
# 2023-04-06