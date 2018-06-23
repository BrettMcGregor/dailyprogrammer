# Write a program to left or right justify a text file


def justify(option):
    with open("justify.txt", "r") as file:
        content = file.readlines()
        out = []
        for line in content:
            out.append(line.lstrip())
    if option == "right":
        with open("justify.txt", "w") as file:
            for line in out:
                file.write(f"{line:>50}")
    elif option == "left":
        with open("justify.txt", "w") as file:
            for line in out:
                file.write(f"{line}")


justify('left')
