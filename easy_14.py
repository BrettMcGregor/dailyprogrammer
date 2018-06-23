# Input: list of elements and a block size k
# or some other variable of your choice
#
# Output: return the list of elements with every
#  block of k elements reversed, starting from
# the beginning of the list.
#
# For instance, given the list 12, 24, 32, 44, 55, 66
# and the block size 2, the result is 24, 12, 44, 32, 66, 55.


def reverse_blocks(array, k):
    new_array = []
    x = k
    for i in range(int(len(array)/k)):
        new_array.extend(sorted(array[k-x:k], reverse=True))
        k += x
    return new_array


collection = [12, 24, 32, 44, 55, 66]
print(reverse_blocks(collection, 2))
