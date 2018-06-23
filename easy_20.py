# create a program that will find all prime numbers below 2000


def find_next(nums):
    while True:
        for item in nums:
            if item[1]:
                return item[0]


def eratosthenes(size):
    output = [[x, True] for x in range(2, size)]
    p = 2
    while True:
        if p >= len(output):
            break
        for x in output[p:]:
            if x[0] % p == 0:
                x[1] = False
        p = find_next(output[p - 1:])
    return [x[0] for x in output if x[1]]


print(eratosthenes(80))
