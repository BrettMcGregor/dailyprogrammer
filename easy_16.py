# Write a function that takes two strings and removes
# from the first string any character that appears in
# the second string. For instance, if the first string
# is “Daily Programmer” and the second string is “aeiou ”
# the result is “DlyPrgrmmr”.
# note: the second string has [space] so the space between
# "Daily Programmer" is removed


def remove_char(first, second):
    output = ""
    for char in first:
        if char in second:
            pass
        else:
            output += char
    return output


print(remove_char("Daily Programmer", "aeiou "))
