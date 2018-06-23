# write a program that will print the song "99 bottles of beer on the wall".
#
# for extra credit, do not allow the program to print each loop on a new line.

num = 99

while num > -1:
    print(f"{num} bottles of beer on the wall,", end=" ")
    print(f"{num} bottles of beer on the wall.", end=" ")
    if num == 0:
        print("No more beer :(")
        break
    else:
        print("If one of those bottles should accidentally fall there'll be", end=" ")
    num -= 1
