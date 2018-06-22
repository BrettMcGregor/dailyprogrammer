# Welcome to cipher day!
# write a program that can encrypt texts with an alphabetical
# caesar cipher. This cipher can ignore numbers, symbols,
# and whitespace.
# for extra credit, add a "decrypt" function to your program!


def caesar(text, offset, mode):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    output = []
    if mode == "encode":
        for char in text:
            if char in upper:
                output.append(upper[((upper.find(char) + offset) % 26)])
            else:
                output.append(lower[((lower.find(char) + offset) % 26)])
        print("".join(output))
    elif mode == "decode":
        for char in text:
            if char in upper:
                output.append(upper[((upper.find(char) - offset) % 26)])
            else:
                output.append(lower[((lower.find(char) - offset) % 26)])
        print("".join(output))


caesar(input("Please enter your text for cipher processing\n> "), 15, "decode")
