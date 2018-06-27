# Write a program that will take a number and print a
# right triangle attempting to use all numbers from 1 to that number.
#
# Sample Run:
#
# Enter number: 10
#
# Output:
#
# 7 8 9 10
#
# 4 5 6
#
# 2 3
#
# 1


def print_triangle(num):
    lines = [x for x in range(1, num+1)]
    result = []
    j = 0
    k = 1
    i = 1
    while k <= num:
        result.append(lines[j: k])
        j = k
        i += 1
        k += i
    for line in result[::-1]:
        print(" ".join(str(x) for x in line))
        print()


print_triangle(20)
