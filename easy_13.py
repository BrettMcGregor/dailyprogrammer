# Find the number of the year for the given date.
# For example, january 1st would be 1, and december 31st is 365.
#
# for extra credit, allow it to calculate leap years, as well.

import datetime


def day_num(day, month, year):
    d = datetime.date(year, month, day).toordinal() - datetime.date(year, 1, 1).toordinal()
    return d + 1


print(day_num(21, 4, 2020))
