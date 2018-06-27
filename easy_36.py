# 1000 Lockers Problem.
#
# In an imaginary high school there exist 1000 lockers
# labelled 1, 2, ..., 1000. All of them are closed.
# 1000 students are to "toggle" a locker's state. *
# The first student toggles all of them * The second one
# toggles every other one (i.e, 2, 4, 6, ...) * The third
# one toggles the multiples of 3 (3, 6, 9, ...) and so on
# until all students have finished.
#
# To toggle means to close the locker if it is open, and
# to open it if it's closed.
#
# How many and which lockers are open in the end?


def locker_toggle():
    lockers = [[x, 1] for x in range(1, 1001)]  # 1 is closed 0 is open
    for i in range(1, 1001):
        for locker in lockers[i-1::i]:
            if locker[1] == 0:
                locker[1] = 1
            else:
                locker[1] = 0

    return f"{len([x for x in lockers if x[1] == 0])} lockers are open.\n" \
           f"{[x[0] for x in lockers if x[1] == 0]}"


print(locker_toggle())
