# Input: a number
#
# Output : the next higher number that uses the same set of digits.
from itertools import permutations as p


def next_higher(num):
    try:
        return f"{sorted(set(''.join(x) for x in p(str(num))))[int(sorted(set(''.join(x) for x in p(str(num)))).index(str(num))) + 1]} is the next highest number"
    except IndexError:
        return f"Your number, {num}, is the highest number!"


print(next_higher(5411))
