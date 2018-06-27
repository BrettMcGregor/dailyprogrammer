# A Palindrome is a sequence that is the same in
# reverse as it is forward.
#
# I.e. hannah, 12321.
#
# Your task is to write a function to determine
# whether a given string is palindromic or not.
#
# Bonus: Support multiple lines in your function
# to validate Demetri Martin's 224 word palindrome poem.
import os


def palindrome(s):
    if os.path.exists(f"{s}"):
        with open(f"{s}", encoding="utf-8") as file:  # check if argument is a file
            next(file)  # skip title
            contents = file.readlines()
            contents = "".join("".join(x.strip("\n").lower().split()) for x in contents)  # join into one string
            p = ""
            for char in contents:  # remove punctuation
                if char.isalpha():
                    p += char
                else:
                    continue
            if p == p[::-1]:  # check if palindrome
                    return True
            return False
    else:
        if s == s[::-1]:  # check if string argument palindrome
            return True
        return False


print(palindrome("poem.txt"))
print(palindrome("hannah"))
print(palindrome("not a palindrome"))
