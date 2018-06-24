# The array duplicates problem is when one integer
# is in an array more than once.
#
# If you are given an array with integers between
# 1 and 1,000,000 or in some other interval and one
# integer is in the array twice. How can you determine which one?
#
# Your task is to write code to solve the challenge.
#
# Note: try to find the most efficient way to solve this challenge.

import random

# make an array with a single randomly-placed duplicate
array = [x for x in range(100)]
array.insert(random.randint(0, len(array)), random.randint(0, len(array)))


# generator function for array
def gen_next(a):
    i = 0
    while True:
        yield a[i]
        i += 1


# find the duplicate by iterating through the list using the generator
def find_duplicate(a):
    a = sorted(a)
    x = gen_next(a)
    print(a)  # for testing
    for i in range(len(a)):
        if a[i-1] == next(x):
            return a[i-1]


print(find_duplicate(array))
