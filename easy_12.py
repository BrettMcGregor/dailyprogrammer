# Write a small program that can take a string:
#
# "hi!"
#
# and print all the possible permutations of the string:
#
# "hi!"
#
# "ih!"
#
# "!hi"
#
# "h!i"
#
# "i!h"
#
# etc...
#
# thanks to hewts for this challenge!

from itertools import permutations as p


def all_permutations(word):
    for v in p(word):
        print(''.join(v))


all_permutations("hi!")
