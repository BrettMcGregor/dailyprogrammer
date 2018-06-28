# Description
#
# In mathematics the regular paperfolding sequence, also known
# as the dragon curve sequence, is an infinite automatic sequence
# of 0s and 1s. At each stage an alternating sequence of 1s
# and 0s is inserted between the terms of the previous sequence.
# The first few generations of the sequence look like this:
#
# 1
# 1 1 0
# 1 1 0 1 1 0 0
# 1 1 0 1 1 0 0 1 1 1 0 0 1 0 0
# 1 1 0 1 1 0 0 1 1 1 0 0 1 0 0 1 1 1 0 1 1 0 0 0 1 1 0 0 1 0 0
#
# The sequence takes its name from the fact that it represents
# the sequence of left and right folds along a strip of paper
# that is folded repeatedly in half in the same direction. If
# each fold is then opened out to create a right-angled corner,
# the resulting shape approaches the dragon curve fractal.
# Challenge Input
#
# Your challenge today is to implement a regular paperfold
# sequence generator up to 8 cycles (it gets lengthy quickly).


# generator function for infinite series

def binary_generator():
    nums = [1, 0]
    while True:
        yield nums
        nums.extend(nums)


# x = binary_generator()
#
# for i in range(4):
#     print(next(x))


def dragon_curve():
    seq = [1]
    x = binary_generator()
    for j in range(n):
        b = next(x)
        print(b)
        yield seq




n = 4
result = dragon_curve()

for i in range(n):
    print(next(result))















