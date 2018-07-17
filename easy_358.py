# Description
#
# Today's challenge will be to create a program to decipher a seven segment display,
# commonly seen on many older electronic devices.
# Input Description
#
# For this challenge, you will receive 3 lines of input, with each line being 27
# characters long (representing 9 total numbers), with the digits spread across the 3 lines.
# Your job is to return the represented digits. You don't need to account for odd spacing
# or missing segments.
# Output Description
#
# Your program should print the numbers contained in the display.
# Challenge Inputs
#
"""
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

    _  _  _  _  _  _  _  _ 
|_| _| _||_|| ||_ |_| _||_ 
  | _| _||_||_| _||_||_  _|

 _  _  _  _  _  _  _  _  _ 
|_  _||_ |_| _|  ||_ | ||_|
 _||_ |_||_| _|  ||_||_||_|

 _  _        _  _  _  _  _ 
|_||_ |_|  || ||_ |_ |_| _|
 _| _|  |  ||_| _| _| _||_ 
"""#
# Challenge Outputs
#
# 123456789
# 433805825
# 526837608
# 954105592


def seven_segments(a, b, c):
    num_dict = {
        "1": ["   ", "  |", "  |"],
        "2": [" _ ", " _|", "|_ "],
        "3": [" _ ", " _|", " _|"],
        "4": ["   ", "|_|", "  |"],
        "5": [" _ ", "|_ ", " _|"],
        "6": [" _ ", "|_ ", "|_|"],
        "7": [" _ ", "  |", "  |"],
        "8": [" _ ", "|_|", "|_|"],
        "9": [" _ ", "|_|", " _|"],
        "0": [" _ ", "| |", "|_|"]
    }
    num_list = []
    j = 0
    while j <= 26:
        num_list.append([a[j:j+3], b[j:j+3], c[j:j+3]])
        j += 3
    output = ""
    for num in num_list:
        for k, v in num_dict.items():
            if num == v:
                output += k
    return output


print(seven_segments("    _  _     _  _  _  _  _ ",
                     "  | _| _||_||_ |_   ||_||_|",
                     "  ||_  _|  | _||_|  ||_| _|"))

print(seven_segments("    _  _  _  _  _  _  _  _ ",
                     "|_| _| _||_|| ||_ |_| _||_ ",
                     "  | _| _||_||_| _||_||_  _|"))

