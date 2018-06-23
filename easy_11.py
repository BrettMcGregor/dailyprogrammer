# The program should take three arguments.
# The first will be a day, the second will be month,
#  and the third will be year. Then, your program
# should compute the day of the week that date will fall on.

import datetime


def weekday_finder(day, month, year):
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    d = weekdays[datetime.date(year, month, day).weekday()]
    return d


print(weekday_finder(21, 4, 1976))
