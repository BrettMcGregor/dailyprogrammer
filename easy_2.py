# Hello, coders! An important part of programming is being able
# to apply your programs, so your challenge for today is to create
#     a calculator application that has use in your life. It might
#     be an interest calculator, or it might be something that you
#     can use in the classroom. For example, if you were in physics
#     class, you might want to make a F = M * A calc.
#
# EXTRA CREDIT: make the calculator have multiple functions!
# Not only should it be able to calculate F = M * A,
# but also A = F/M, and M = F/A!


def calculator():
    f, m, a = "force", "mass", "acceleration"
    calc_type = input("Please choose equation to evaluate.\n"
                      f"1. {f} = {m} * {a}\n"
                      f"2. {a} = {f} / {m}\n"
                      f"3. {m} = {f} / {a}\n"
                      "Q to quit\n> ")
    if calc_type.upper() == "Q":
        exit()
    elif int(calc_type) == 1:
        x, y = get_values(m, a)
        print(f"{x} * {y} = {x * y}")
    elif int(calc_type) == 2:
        x, y = get_values(f, m)
        print(f"{x} / {y} = {x / y}")
    elif int(calc_type) == 3:
        x, y = get_values(f, a)
        print(f"{x} / {y} = {x / y}")
    print()


def get_values(a, b):
    x = int(input(f"Please enter a value for {a}\n> "))
    y = int(input(f"Please enter a value for {b}\n> "))
    return x, y


while True:
    calculator()
