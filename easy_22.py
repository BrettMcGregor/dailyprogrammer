# Write a program that will compare two lists, and append
# any elements in the second list that doesn't exist in the first.
#
# input: ["a","b","c",1,4,], ["a", "x", 34, "4"]
#
# output: ["a", "b", "c",1,4,"x",34, "4"]


def compare_add(a, b):
    for item in b:
        if item not in a:
            a.append(item)
    return a


print(compare_add(["a","b","c",1,4,], ["a", "x", 34, "4"]))
















