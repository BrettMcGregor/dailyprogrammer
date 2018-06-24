# Input: a list
#
# Output: Return the two halves as different lists.
#
# If the input list has an odd number, the middle item can go to any of the list.
#
# Your task is to write the function that splits a list in two halves.


def split_list(c):
    s = int(len(c)/2)
    return c[:s], c[s:]


print(split_list([1,2,3,4,5,6,7,8,9,10]))





























