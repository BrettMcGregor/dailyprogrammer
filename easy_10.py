# The exercise today asks you to validate a telephone number,
# as if written on an input form. Telephone numbers can be written
# as ten digits, or with dashes, spaces, or dots between the three
#  segments, or with the area code parenthesized; both the area
# code and any white space between segments are optional.
#
# Thus, all of the following are valid telephone numbers:
# 1234567890, 123-456-7890, 123.456.7890, (123)456-7890,
# (123) 456-7890 (note the white space following the area code),
# and 456-7890.
#
# The following are not valid telephone numbers: 123-45-6789,
# 123:4567890, and 123/456-7890.


def ph_num_validation(number):
    ok = "()-. "
    count = 0
    for char in number:
        if char.isnumeric():
            count += 1
        elif char in ok:
            continue
        else:
            return False
    if count == 10:
        return True
    return False


print(ph_num_validation("(123) 456-7890"))
print(ph_num_validation("123:4567890"))
print(ph_num_validation("123-45-6789"))
print(ph_num_validation("123.456.7890"))
