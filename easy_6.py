# You're challenge for today is to create a program that can calculate pi accurately to at least 30 decimal places.
#
# Try not to cheat :)


def odd_generator():
    odd = 1
    while True:
        odd += 2
        yield odd


def gregory_leibniz():
    odds = odd_generator()
    pi = 4
    while True:
        pi -= 4/next(odds)
        yield pi
        pi += 4/next(odds)
        yield pi


def n_seq():
    x, y, z = 2, 3, 4
    while True:
        yield x * y * z
        x += 2
        y += 2
        z += 2


def nilakantha():
    seq = n_seq()
    pi = 3
    while True:
        pi += 4 / (next(seq))
        yield pi
        pi -= 4 / (next(seq))
        yield pi


n = nilakantha()
for i in range(100000):
    print(next(n))




