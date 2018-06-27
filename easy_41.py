# Write a program that will accept a sentence as input
# and then output that sentence surrounded by some
# type of an ASCII decoration banner.
#
# Sample run:
#
# Enter a sentence: So long and thanks for all the fish
#
# Output
#
# *****************************************
# *                                       *
# *  So long and thanks for all the fish  *
# *                                       *
# *****************************************


def print_banner(string):
    header = "*" * (len(string) + 6)
    spacer = "*"+" " * (len(string) + 4)+"*"
    print(header + "\n" + spacer)
    print(f"*  {string}  *")
    print(spacer + "\n" + header)


print_banner("So long and thanks for all the fish")
