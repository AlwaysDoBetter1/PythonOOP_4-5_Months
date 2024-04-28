'''
Every month there is a Python meetup in San Diego on the fourth Thursday of the month.

Write a program that determines the day of the next Python meeting in San Diego.

Input format
The program is given two natural numbers representing the year and month, each on a separate line.

Output format
The program must determine the day of the meeting in San Diego in the specified year and month and output the result
in the format DD.MM.YYYY.
'''

import calendar
from datetime import date

def fourth_thursday(year, month):
    first_day_of_month = calendar.weekday(year, month, 1)
    offset = (3 - first_day_of_month + 7) % 7
    fourth_thursday_date = offset + 1 + (4 - 1) * 7
    return fourth_thursday_date

year, month = int(input()), int(input())
res = str(date(year, month, fourth_thursday(year, month))).split("-")[::-1]
print(".".join(res))


# Example
# Input
# 2018
# 6
# Output:
# 28.06.2018