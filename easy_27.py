# Write a program that accepts a year as input and outputs
# the century the year belongs in (e.g. 18th century's year
# ranges are 1701 to 1800) and whether or not the year is
# a leap year. Pseudocode for leap year can be found here.
## Leap Year pseudocode
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)

# Sample run:
#
# Enter Year: 1996
#
# Century: 20
#
# Leap Year: Yes
#
# Enter Year: 1900
#
# Century: 19
#
# Leap Year: No


def year_info(year):
    century = "".join(str(year + 99)[:2]) + "th century"
    if year % 4 != 0:
        leap = "No"
    elif year % 100 != 0:
        leap = "Yes"
    elif year % 400 != 0:
        leap = "No"
    else:
        leap = "Yes"

    return year, century, leap


print(year_info(1976))
print(year_info(1900))