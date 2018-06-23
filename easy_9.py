# write a program that will allow the user to input digits, and arrange them in numerical order.
#
# for extra credit, have it also arrange strings in alphabetical order


def sorter(source):
        return "".join(sorted(source))


print(sorter(input("enter a string or integer")))
