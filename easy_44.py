# our challenge today is to write a program that can draw
# a checkered grid (like a chessboard) to any dimension.

# *********************************
# *   *###*   *###*   *###*   *###*
# *   *###*   *###*   *###*   *###*
# *   *###*   *###*   *###*   *###*
# *********************************
# *###*   *###*   *###*   *###*   *
# *###*   *###*   *###*   *###*   *
# *###*   *###*   *###*   *###*   *
# *********************************
# *   *###*   *###*   *###*   *###*
# *   *###*   *###*   *###*   *###*
# *   *###*   *###*   *###*   *###*
# *********************************


def draw_board(x=8, y=8, size=6):  # x is width of board y is height
    h = "*" * size
    empty = "*" + " " * (size - 1)
    full = "*" + "#" * (size - 1)
    rows = 0
    for i in range(y):
        print(h * x + "*")
        state = 0
        if rows == 0:
            for j in range(size-1):
                for k in range(x):
                    if state == 0:
                        print(empty, end="")
                        state = 1
                    elif state == 1:
                        print(full, end="")
                        state = 0
                print("*")
            rows = 1
        elif rows == 1:
            for j in range(size-1):
                for k in range(x):
                    if state == 0:
                        print(full, end="")
                        state = 1
                    elif state == 1:
                        print(empty, end="")
                        state = 0
                print("*")
            rows = 0
    print(h * x + "*")


draw_board()
