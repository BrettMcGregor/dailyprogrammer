# Write a program that takes a list of integers
# and a target number and determines if any two
# integers in the list sum to the target number.
# If so, return the two numbers. If not, return
# an indication that no such integers exist.

from itertools import permutations as perm


def sum_target(nums, target):
    a = perm(nums, 2)
    while True:
        x, y = next(a)
        print(x,y)
        if x + y == target:
            return x, y
    return False


print(sum_target([1, 3, 4, 5, 6], 9))
