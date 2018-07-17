# We were all taught addition, multiplication, and exponentiation in our early years of math.
# You can view addition as repeated succession. Similarly, you can view multiplication as
# repeated addition. And finally, you can view exponentiation as repeated multiplication.
# But why stop there? Knuth's up-arrow notation takes this idea a step further.
# The notation is used to represent repeated operations.
#
# In this notation a single ↑ operator corresponds to iterated multiplication. For example:
#
# 2 ↑ 4 = ?
# = 2 * (2 * (2 * 2))
# = 2^4
# = 16
#
# While two ↑ operators correspond to iterated exponentiation. For example:
#
# 2 ↑↑ 4 = ?
# = 2 ↑ (2 ↑ (2 ↑ 2))
# = 2^2^2^2
# = 65536
#
# Consider how you would evaluate three ↑ operators. For example:
#
# 2 ↑↑↑ 3 = ?
# = 2 ↑↑ (2 ↑↑ 2)
# = 2 ↑↑ (2 ↑ 2)
# = 2 ↑↑ (2 ^ 2)
# = 2 ↑↑ 4
# = 2 ↑ (2 ↑ (2 ↑ 2))
# = 2 ^ 2 ^ 2 ^ 2
# = 65536
#
# In today's challenge, we are given an expression in Kuth's up-arrow notation to evaluate.
#
# 5 ↑↑↑↑ 5 # too much computation cost
# 7 ↑↑↑↑↑ 3 # too much computation cost
# -1 ↑↑↑ 3
# 1 ↑ 0
# 1 ↑↑ 0
# 12 ↑↑↑↑↑↑↑↑↑↑↑ 25 # too much computation cost


def kuth_arrow(string):
    s = string.split()
    if s[1] == "^":
        return int(s[0]) ** int(s[2])
    else:
        result = int(s[0])
        for i in range(1, int(s[2]) + len(s[1])-1):
            result **= int(s[0])
        return result

print(kuth_arrow("2 ^ 4"))
print(kuth_arrow("2 ^^ 4"))
print(kuth_arrow("2 ^^^ 3"))

print(kuth_arrow("-1 ^^^ 3"))