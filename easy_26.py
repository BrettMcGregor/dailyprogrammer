# you have a string "ddaaiillyypprrooggrraammeerr".
# We want to remove all the consecutive duplicates and
# put them in a separate string, which yields two
# separate instances of the string "dailyprogramer".
#
# use this list for testing:
#
# input: "balloons"
#
# expected output: "balons" "lo"
#
# input: "ddaaiillyypprrooggrraammeerr"
#
# expected output: "dailyprogramer" "dailyprogramer"
#
# input: "aabbccddeded"
#
# expected output: "abcdeded" "abcd"
#
# input: "flabby aapples"
#
# expected output: "flaby aples" "bap"


def out_dups(s):
    o = ""
    p = ""
    for i in range(len(s)-1):
        if s[i + 1] == s[i]:
            o += s[i]
        else:
            p += s[i]
    p += s[i+1]
    return p, o











print(out_dups("ddaaiillyypprrooggrraammeerr"))
print(out_dups("balloons"))
print(out_dups("aabbccddeded"))
print(out_dups("flabby aapples"))
