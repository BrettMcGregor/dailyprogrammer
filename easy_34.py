# A very basic challenge:
#
# In this challenge, the
#
# input is are : 3 numbers as arguments
#
# output: the sum of the squares of the two larger numbers.
#
# Your task is to write the indicated challenge.


def larger_squares(a, b, c):
    return sum(x**2 for x in sorted([a, b, c])[-2:])


print(larger_squares(4, 9, 2))
